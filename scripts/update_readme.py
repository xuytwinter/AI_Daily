"""Refresh README.md with an index of recent daily entries."""
from __future__ import annotations

import re
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = REPO_ROOT / "daily"
README = REPO_ROOT / "README.md"

LANG_LABEL = {"zh": "简体中文", "en": "English", "tw": "繁體中文", "ja": "日本語"}
LANG_ORDER = ["zh", "en", "tw", "ja"]

START = "<!-- BEGIN_INDEX -->"
END = "<!-- END_INDEX -->"

INDEX_LIMIT = 30  # most recent N days


def collect() -> list[tuple[date, dict[str, Path]]]:
    if not DAILY_DIR.exists():
        return []
    out: list[tuple[date, dict[str, Path]]] = []
    for sub in sorted(DAILY_DIR.iterdir(), reverse=True):
        if not sub.is_dir():
            continue
        try:
            d = date.fromisoformat(sub.name)
        except ValueError:
            continue
        files = {lang: sub / f"{lang}.md" for lang in LANG_ORDER if (sub / f"{lang}.md").exists()}
        if files:
            out.append((d, files))
    return out


def extract_title(md_path: Path) -> str:
    """Pull the article title from a generated markdown file."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except OSError:
        return ""
    # Front-matter: title: "..."
    m = re.search(r'(?m)^title:\s*"(.+?)"\s*$', text)
    if m:
        return m.group(1)
    # Fallback to first H1.
    m = re.search(r"(?m)^#\s+(.+)$", text)
    return m.group(1) if m else ""


def render_index(entries: list[tuple[date, dict[str, Path]]]) -> str:
    if not entries:
        return "_暂无内容 / No entries yet._"

    lines: list[str] = []
    header = "| 日期 Date | " + " | ".join(LANG_LABEL[l] for l in LANG_ORDER) + " |"
    sep = "| --- | " + " | ".join(["---"] * len(LANG_ORDER)) + " |"
    lines.append(header)
    lines.append(sep)

    for d, files in entries[:INDEX_LIMIT]:
        cells = [f"**{d.isoformat()}**"]
        for lang in LANG_ORDER:
            p = files.get(lang)
            if not p:
                cells.append("—")
                continue
            rel = p.relative_to(REPO_ROOT).as_posix()
            title = extract_title(p)
            short = (title[:40] + "…") if len(title) > 42 else title
            cells.append(f"[{short or LANG_LABEL[lang]}]({rel})")
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)


def update_readme() -> bool:
    entries = collect()
    index_md = render_index(entries)
    block = f"{START}\n{index_md}\n{END}"

    if README.exists():
        text = README.read_text(encoding="utf-8")
    else:
        text = ""

    if START in text and END in text:
        new_text = re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            block,
            text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        if not text.strip():
            text = "# AI_Daily\n"
        new_text = text.rstrip() + "\n\n## 最近更新 / Recent\n\n" + block + "\n"

    if new_text != text:
        README.write_text(new_text, encoding="utf-8")
        return True
    return False


if __name__ == "__main__":
    changed = update_readme()
    print("README updated" if changed else "README unchanged")
