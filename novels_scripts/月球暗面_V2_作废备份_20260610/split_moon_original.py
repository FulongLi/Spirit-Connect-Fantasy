from __future__ import annotations

import html
import re
from pathlib import Path


SOURCE = Path(
    "/Users/fulongli/.codex/attachments/84b45643-1e96-45fd-8e3e-71e3cd44c2cf/pasted-text.txt"
)
OUT_DIR = Path("/Users/fulongli/Desktop/novels/月球暗面")
MD_DIR = OUT_DIR / "md"
HTML_DIR = OUT_DIR / "html"


CHAPTER_RE = re.compile(r"^第[一二三四五六七八九十百0-9]+章[:：].+")
SECTION_TITLES = {"作者序", "前言"}


def clean_text(raw: str) -> str:
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\ufeff", "")
    text = text.replace("\f", "\n")
    lines = [line.rstrip() for line in text.split("\n")]

    cleaned: list[str] = []
    blank = False
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if not blank:
                cleaned.append("")
            blank = True
            continue
        cleaned.append(stripped)
        blank = False

    while cleaned and not cleaned[0]:
        cleaned.pop(0)
    while cleaned and not cleaned[-1]:
        cleaned.pop()
    return "\n".join(cleaned) + "\n"


def slug(title: str) -> str:
    value = re.sub(r"[\\/:：*?\"<>|]+", "_", title)
    value = re.sub(r"\s+", "", value)
    return value.strip("_")


def split_sections(text: str) -> list[tuple[str, list[str]]]:
    lines = text.splitlines()
    sections: list[tuple[str, list[str]]] = []

    front: list[str] = []
    current_title = "书名页_版权_献词"
    current_lines = front

    for line in lines:
        if line in SECTION_TITLES or CHAPTER_RE.match(line):
            if current_lines:
                sections.append((current_title, current_lines))
            current_title = line
            current_lines = []
            continue
        current_lines.append(line)

    if current_lines:
        sections.append((current_title, current_lines))

    return sections


def md_for_section(title: str, lines: list[str]) -> str:
    body = "\n".join(lines).strip()
    if body:
        return f"# {title}\n\n{body}\n"
    return f"# {title}\n"


def inline_markup(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"\*\*\*([^*]+)\*\*\*", r"<strong><em>\1</em></strong>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def html_for_section(title: str, lines: list[str]) -> str:
    parts = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{html.escape(title)} - 月球暗面</title>",
        "  <style>",
        "    :root { color-scheme: light; }",
        "    body { margin: 0; background: #f7f4ef; color: #1f2328; font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif; line-height: 1.85; }",
        "    main { max-width: 820px; margin: 0 auto; padding: 56px 24px 72px; background: #fffdf9; min-height: 100vh; box-sizing: border-box; }",
        "    h1 { margin: 0 0 32px; font-size: 2rem; font-weight: 700; line-height: 1.25; }",
        "    p { margin: 0 0 1em; font-size: 1.05rem; }",
        "    .blank { height: 1em; }",
        "    @media (max-width: 640px) { main { padding: 36px 18px 56px; } h1 { font-size: 1.6rem; } p { font-size: 1rem; } }",
        "  </style>",
        "</head>",
        "<body>",
        "  <main>",
        f"    <h1>{html.escape(title)}</h1>",
    ]

    for line in lines:
        if not line.strip():
            parts.append('    <div class="blank"></div>')
        else:
            parts.append(f"    <p>{inline_markup(line)}</p>")

    parts.extend(["  </main>", "</body>", "</html>", ""])
    return "\n".join(parts)


def main() -> None:
    text = clean_text(SOURCE.read_text(encoding="utf-8"))
    sections = split_sections(text)

    MD_DIR.mkdir(parents=True, exist_ok=True)
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    for path in list(MD_DIR.glob("*.md")) + list(HTML_DIR.glob("*.html")):
        path.unlink()
    for path in [OUT_DIR / "index.md", OUT_DIR / "index.html"]:
        if path.exists():
            path.unlink()

    index_rows: list[tuple[str, str, str]] = []
    for idx, (title, lines) in enumerate(sections):
        filename = f"{idx:02d}_{slug(title)}"
        md_path = MD_DIR / f"{filename}.md"
        html_path = HTML_DIR / f"{filename}.html"
        md_path.write_text(md_for_section(title, lines), encoding="utf-8")
        html_path.write_text(html_for_section(title, lines), encoding="utf-8")
        index_rows.append((title, md_path.relative_to(OUT_DIR).as_posix(), html_path.relative_to(OUT_DIR).as_posix()))

    index_md = ["# 月球暗面 原版章节拆分", ""]
    for title, md_rel, html_rel in index_rows:
        index_md.append(f"- [{title}]({md_rel}) | [HTML]({html_rel})")
    index_md.append("")
    (OUT_DIR / "index.md").write_text("\n".join(index_md), encoding="utf-8")

    index_html = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        "  <title>月球暗面 原版章节拆分</title>",
        "  <style>body{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.8;margin:40px auto;max-width:820px;padding:0 24px;color:#1f2328;background:#fffdf9}a{color:#2458a6}li{margin:.35em 0}</style>",
        "</head>",
        "<body>",
        "  <h1>月球暗面 原版章节拆分</h1>",
        "  <ul>",
    ]
    for title, md_rel, html_rel in index_rows:
        index_html.append(
            f'    <li>{html.escape(title)} - <a href="{html.escape(md_rel)}">MD</a> | <a href="{html.escape(html_rel)}">HTML</a></li>'
        )
    index_html.extend(["  </ul>", "</body>", "</html>", ""])
    (OUT_DIR / "index.html").write_text("\n".join(index_html), encoding="utf-8")

    print(f"Wrote {len(sections)} sections to {OUT_DIR}")
    for title, _, _ in index_rows:
        print(title)


if __name__ == "__main__":
    main()
