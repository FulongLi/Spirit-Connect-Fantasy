#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EN_MD = ROOT / "en_md"
EN_HTML = ROOT / "en_html"


def inline_markdown(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*{3}([^*]+)\*{3}", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def title_from_markdown(md: str, fallback: str) -> str:
    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return fallback


def render_markdown(md: str) -> str:
    blocks: list[str] = []
    list_items: list[str] = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            blocks.append("<ul>\n" + "\n".join(f"<li>{item}</li>" for item in list_items) + "\n</ul>")
            list_items = []

    for line in md.splitlines():
        stripped = line.strip()
        if not stripped:
            flush_list()
            continue
        if stripped.startswith("#"):
            flush_list()
            level = min(len(stripped) - len(stripped.lstrip("#")), 4)
            title = stripped[level:].strip()
            blocks.append(f"<h{level}>{inline_markdown(title)}</h{level}>")
        elif stripped.startswith("- "):
            list_items.append(inline_markdown(stripped[2:].strip()))
        elif stripped.startswith("***") and stripped.endswith("***") and len(stripped) > 6:
            flush_list()
            blocks.append(f"<p class=\"system-line\"><strong>{inline_markdown(stripped.strip('*'))}</strong></p>")
        elif stripped.startswith("**") and stripped.endswith("**") and len(stripped) > 4:
            flush_list()
            blocks.append(f"<p class=\"system-line\"><strong>{inline_markdown(stripped.strip('*'))}</strong></p>")
        else:
            flush_list()
            blocks.append(f"<p>{inline_markdown(stripped)}</p>")
    flush_list()
    return "\n".join(blocks)


def chapter_nav(prev_stem: str | None, next_stem: str | None) -> str:
    prev = (
        f'<a href="{html.escape(prev_stem)}.html">上一章 / Previous</a>'
        if prev_stem
        else '<span class="disabled">上一章 / Previous</span>'
    )
    next_ = (
        f'<a href="{html.escape(next_stem)}.html">下一章 / Next</a>'
        if next_stem
        else '<span class="disabled">下一章 / Next</span>'
    )
    return (
        '<nav class="chapter-nav">\n'
        f"{prev}\n"
        '<a href="../index_EN.html">目录 / Index</a>\n'
        f"{next_}\n"
        "</nav>"
    )


def page(title: str, body: str, css_href: str, lang: str = "en") -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{css_href}">
</head>
<body><main>
{body}
</main></body>
</html>
"""


def build_index(chapters: list[Path], titles: list[str]) -> str:
    lines = [
        "# Moon Dark Side V2 English Reading Index",
        "",
        "English prose translation of the `zh_md` chapter set. File names mirror the Chinese source files; chapter titles are translated in the documents.",
        "",
        "## Chapter Index",
    ]
    for src, title in zip(chapters, titles):
        html_name = f"{src.stem}.html"
        lines.append(f"- [{title}](en_md/{src.name}) / [HTML](en_html/{html_name})")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    EN_HTML.mkdir(exist_ok=True)
    chapters = sorted(EN_MD.glob("*.md"))
    titles: list[str] = []

    for index, src in enumerate(chapters):
        md = src.read_text(encoding="utf-8")
        title = title_from_markdown(md, src.stem)
        titles.append(title)
        prev_stem = chapters[index - 1].stem if index > 0 else None
        next_stem = chapters[index + 1].stem if index + 1 < len(chapters) else None
        body = render_markdown(md) + "\n" + chapter_nav(prev_stem, next_stem)
        (EN_HTML / f"{src.stem}.html").write_text(
            page(title, body, "../assets/style.css", "en"),
            encoding="utf-8",
        )

    index_md = build_index(chapters, titles)
    (ROOT / "index_EN.md").write_text(index_md, encoding="utf-8")
    index_body = render_markdown(index_md)
    (ROOT / "index_EN.html").write_text(
        page("Moon Dark Side V2 English Reading Index", index_body, "assets/style.css", "en"),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
