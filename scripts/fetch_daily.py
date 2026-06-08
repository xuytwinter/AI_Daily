"""Fetch aibase.com daily AI news in 4 languages and save as Markdown.

Usage:
    python scripts/fetch_daily.py                # default: 4 langs, last 7 days
    python scripts/fetch_daily.py --days 14
    python scripts/fetch_daily.py --langs zh,en
    python scripts/fetch_daily.py --force        # re-fetch even if file exists
"""
from __future__ import annotations

import argparse
import logging
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Iterable, List

import requests

# Allow running both as a module and as a script.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.parsers import (
    LANGS,
    Article,
    ListItem,
    detail_url,
    list_url,
    parse_detail,
    parse_list,
)

logger = logging.getLogger("fetch_daily")

REPO_ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = REPO_ROOT / "daily"

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

REQUEST_TIMEOUT = 20
REQUEST_INTERVAL = 1.2  # seconds between requests, polite rate limit
MAX_RETRIES = 3


def http_get(session: requests.Session, url: str) -> str:
    last_exc: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=REQUEST_TIMEOUT)
            resp.raise_for_status()
            resp.encoding = resp.apparent_encoding or resp.encoding
            return resp.text
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            wait = attempt * 2
            logger.warning("GET %s failed (attempt %d/%d): %s; retry in %ds",
                           url, attempt, MAX_RETRIES, exc, wait)
            time.sleep(wait)
    raise RuntimeError(f"failed to fetch {url}: {last_exc}")


def output_path(d: date, lang: str) -> Path:
    return DAILY_DIR / d.isoformat() / f"{lang}.md"


def render_markdown(article: Article, list_item: ListItem | None) -> str:
    fetched_at = datetime.now(tz=timezone.utc).isoformat(timespec="seconds")
    pub = (article.publish_date or (list_item.date if list_item else None))
    pub_str = pub.isoformat() if pub else ""

    fm_lines = ["---"]
    fm_lines.append(f'title: "{article.title.replace(chr(34), chr(39))}"')
    fm_lines.append(f"id: {article.id}")
    fm_lines.append(f"lang: {article.lang}")
    fm_lines.append(f"date: {pub_str}")
    fm_lines.append(f"source: {article.source_url}")
    fm_lines.append(f"fetched_at: {fetched_at}")
    fm_lines.append("---")

    parts = ["\n".join(fm_lines), f"# {article.title}", article.body_markdown.strip()]
    return "\n\n".join(p for p in parts if p).rstrip() + "\n"


def write_article(article: Article, list_item: ListItem | None) -> Path:
    pub = article.publish_date or (list_item.date if list_item else date.today())
    path = output_path(pub, article.lang)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_markdown(article, list_item), encoding="utf-8")
    return path


def fetch_lang(
    session: requests.Session,
    lang: str,
    days_window: int,
    force: bool,
) -> list[Path]:
    written: list[Path] = []
    logger.info("[%s] fetching list page", lang)
    list_html = http_get(session, list_url(lang))
    time.sleep(REQUEST_INTERVAL)

    items = parse_list(list_html, lang=lang)
    if not items:
        logger.warning("[%s] no items parsed from list page", lang)
        return written

    today = date.today()
    cutoff = today.fromordinal(today.toordinal() - days_window)

    for item in items:
        if item.date < cutoff:
            continue
        out = output_path(item.date, lang)
        if out.exists() and not force:
            logger.debug("[%s] skip existing %s", lang, out.relative_to(REPO_ROOT))
            continue
        try:
            url = detail_url(lang, item.id)
            logger.info("[%s] fetch %s id=%s date=%s", lang, url, item.id, item.date)
            html = http_get(session, url)
            article = parse_detail(html, lang=lang, daily_id=item.id, source_url=url)
            if not article.body_markdown:
                logger.warning("[%s] empty body for id=%s; skip", lang, item.id)
                continue
            path = write_article(article, item)
            written.append(path)
            logger.info("[%s] wrote %s", lang, path.relative_to(REPO_ROOT))
        except Exception as exc:  # noqa: BLE001
            logger.error("[%s] failed id=%s: %s", lang, item.id, exc)
        finally:
            time.sleep(REQUEST_INTERVAL)

    return written


def run(langs: Iterable[str], days_window: int, force: bool) -> List[Path]:
    session = requests.Session()
    session.headers.update({
        "User-Agent": USER_AGENT,
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    })
    all_written: list[Path] = []
    for lang in langs:
        try:
            all_written.extend(fetch_lang(session, lang, days_window, force))
        except Exception as exc:  # noqa: BLE001
            logger.error("[%s] fatal: %s", lang, exc)
    return all_written


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--langs", default=",".join(LANGS),
                   help=f"comma-separated languages from {LANGS} (default: all)")
    p.add_argument("--days", type=int, default=7,
                   help="lookback window in days for catching missed entries (default: 7)")
    p.add_argument("--force", action="store_true",
                   help="re-fetch even when local file exists")
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    langs = [s.strip() for s in args.langs.split(",") if s.strip()]
    bad = [l for l in langs if l not in LANGS]
    if bad:
        raise SystemExit(f"unknown langs: {bad}; valid: {LANGS}")

    written = run(langs, args.days, args.force)
    logger.info("done; %d files written", len(written))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
