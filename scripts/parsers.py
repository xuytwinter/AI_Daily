"""Parsers for aibase.com daily list and detail pages."""
from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta
from typing import List, Optional

from bs4 import BeautifulSoup, Tag

# Languages and their URL path segment.
# en uses an empty segment: https://news.aibase.com/daily
LANGS = ["zh", "en", "tw", "ja"]
LANG_PATH = {"zh": "zh", "en": "", "tw": "tw", "ja": "ja"}

BASE = "https://news.aibase.com"


def list_url(lang: str) -> str:
    seg = LANG_PATH[lang]
    return f"{BASE}/{seg}/daily" if seg else f"{BASE}/daily"


def detail_url(lang: str, daily_id: int | str) -> str:
    seg = LANG_PATH[lang]
    return f"{BASE}/{seg}/daily/{daily_id}" if seg else f"{BASE}/daily/{daily_id}"


@dataclass
class ListItem:
    id: str
    title: str
    summary: str
    date: date  # publish date (parsed from MM-DD with year inferred)
    url: str


@dataclass
class Article:
    id: str
    lang: str
    title: str
    body_markdown: str
    source_url: str
    publish_date: Optional[date]


# ---------------------------------------------------------------------------
# List page
# ---------------------------------------------------------------------------

_DATE_RE = re.compile(r"(\d{1,2})[-/](\d{1,2})")
# Relative-date markers across the four supported languages.
# zh / tw use "N 天前", en uses "N days ago", ja uses "N 日前".
_REL_DAYS_RE = re.compile(r"(\d+)\s*(?:days?\s*ago|天前|日前)", re.IGNORECASE)
# "Yesterday / today" markers.
_TODAY_WORDS = ("今天", "今日", "today")
_YESTERDAY_WORDS = ("昨天", "昨日", "yesterday")


def _infer_year(month: int, day: int, today: Optional[date] = None) -> int:
    """Pick a sensible year for an MM-DD shown on the list page.

    The list shows recent items first; if MM-DD parsed as the current year would
    be in the future by more than a couple days (e.g. Dec entries seen in Jan),
    treat it as the previous year. Otherwise use the current year.
    """
    today = today or date.today()
    candidate = date(today.year, month, day)
    if (candidate - today).days > 2:
        return today.year - 1
    return today.year


def parse_list(html: str, lang: str, today: Optional[date] = None) -> List[ListItem]:
    """Parse a `/daily` list page into ListItem entries (newest first)."""
    soup = BeautifulSoup(html, "lxml")
    seg = LANG_PATH[lang]
    href_prefix = f"/{seg}/daily/" if seg else "/daily/"
    items: List[ListItem] = []
    seen: set[str] = set()

    for a in soup.find_all("a", href=True):
        href: str = a["href"]
        if not href.startswith(href_prefix):
            continue
        m = re.match(rf"^{re.escape(href_prefix)}(\d+)$", href)
        if not m:
            continue
        daily_id = m.group(1)
        if daily_id in seen:
            continue

        # Title: first descendant div carrying the title (long, bolded).
        title_el = a.find(
            "div",
            class_=lambda c: c and "font600" in c and "mainColor" in c,
        )
        title = title_el.get_text(" ", strip=True) if title_el else a.get_text(" ", strip=True)

        # Summary: a sibling text block below the title.
        summary_el = a.find("div", class_=lambda c: c and "tipColor" in c and "truncate2" in c)
        summary = summary_el.get_text(" ", strip=True) if summary_el else ""

        # Date: look for an icon-rili element followed by date text.
        pub_date: Optional[date] = None
        ref_today = today or date.today()
        for icon in a.find_all("i", class_=lambda c: c and "icon-rili" in c):
            parent = icon.parent
            if not parent:
                continue
            text = parent.get_text(" ", strip=True)
            text_lower = text.lower()

            # 1) Relative "N days ago / N 天前 / N 日前".
            rm = _REL_DAYS_RE.search(text)
            if rm:
                pub_date = ref_today.fromordinal(ref_today.toordinal() - int(rm.group(1)))
                break
            # 2) Today / yesterday markers.
            if any(w in text_lower for w in _TODAY_WORDS):
                pub_date = ref_today
                break
            if any(w in text_lower for w in _YESTERDAY_WORDS):
                pub_date = ref_today.fromordinal(ref_today.toordinal() - 1)
                break
            # 3) Absolute MM-DD format.
            dm = _DATE_RE.search(text)
            if dm:
                month, day = int(dm.group(1)), int(dm.group(2))
                year = _infer_year(month, day, today=ref_today)
                try:
                    pub_date = date(year, month, day)
                except ValueError:
                    pub_date = None
                break

        if pub_date is None:
            # Last resort: fall back to today; caller can still record the item.
            pub_date = ref_today

        seen.add(daily_id)
        items.append(
            ListItem(
                id=daily_id,
                title=title,
                summary=summary,
                date=pub_date,
                url=BASE + href,
            )
        )

    return items


# ---------------------------------------------------------------------------
# Detail page
# ---------------------------------------------------------------------------


def _node_to_markdown(node: Tag) -> str:
    """Convert a single top-level child of post-content to markdown text."""
    name = node.name
    if name in {"p", "div"}:
        # Image-only paragraph?
        img = node.find("img")
        text = node.get_text(" ", strip=True)
        if img and not text:
            src = img.get("data-src") or img.get("src") or ""
            alt = img.get("alt") or ""
            return f"![{alt}]({src})" if src else ""
        # Inline images mixed with text: render text + image lines.
        if img and text:
            src = img.get("data-src") or img.get("src") or ""
            alt = img.get("alt") or ""
            extra = f"\n\n![{alt}]({src})" if src else ""
            return text + extra
        return text
    if name == "blockquote":
        text = node.get_text("\n", strip=True)
        if not text:
            return ""
        return "\n".join(f"> {line}" for line in text.splitlines() if line.strip())
    if re.fullmatch(r"h[1-6]", name or ""):
        level = int(name[1])
        return f"{'#' * level} {node.get_text(' ', strip=True)}"
    if name in {"ul", "ol"}:
        lines = []
        ordered = name == "ol"
        for i, li in enumerate(node.find_all("li", recursive=False), 1):
            prefix = f"{i}." if ordered else "-"
            lines.append(f"{prefix} {li.get_text(' ', strip=True)}")
        return "\n".join(lines)
    if name == "img":
        src = node.get("data-src") or node.get("src") or ""
        alt = node.get("alt") or ""
        return f"![{alt}]({src})" if src else ""
    if name == "hr":
        return "---"
    # Fallback: plain text.
    return node.get_text(" ", strip=True)


def parse_detail(html: str, lang: str, daily_id: str, source_url: str) -> Article:
    soup = BeautifulSoup(html, "lxml")

    # Title.
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(" ", strip=True)
    if not title and soup.title:
        title = soup.title.get_text(" ", strip=True)

    # Body content lives in div.post-content (also has class 'articleContent').
    content = soup.select_one("div.post-content") or soup.select_one("div.articleContent")
    blocks: List[str] = []
    if content:
        for child in content.children:
            if not isinstance(child, Tag):
                continue
            md = _node_to_markdown(child)
            if md:
                blocks.append(md)

    body = "\n\n".join(blocks).strip()

    # Publish date: try meta tags / time element. Aibase pages do not
    # consistently expose a structured publish date, so we leave None and let
    # the caller fall back to the list-page date.
    publish_date: Optional[date] = None
    for sel in [
        ('meta', {'property': 'article:published_time'}),
        ('meta', {'name': 'pubdate'}),
        ('meta', {'itemprop': 'datePublished'}),
    ]:
        m = soup.find(*sel)
        if m and m.get("content"):
            try:
                publish_date = date.fromisoformat(m["content"][:10])
                break
            except ValueError:
                pass
    if publish_date is None:
        t = soup.find("time")
        if t and t.get("datetime"):
            try:
                publish_date = date.fromisoformat(t["datetime"][:10])
            except ValueError:
                pass

    return Article(
        id=daily_id,
        lang=lang,
        title=title,
        body_markdown=body,
        source_url=source_url,
        publish_date=publish_date,
    )
