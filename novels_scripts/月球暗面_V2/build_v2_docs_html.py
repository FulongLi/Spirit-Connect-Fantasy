#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent

DOCS = [
    ("V2重启修订框架_CN.md", "V2重启修订框架_CN.html", "《月球暗面》V2 重启修订框架"),
    ("V2_restart_revision_framework_EN.md", "V2_restart_revision_framework_EN.html", "The Dark Side of the Moon V2 Restart Revision Framework"),
]

CHAPTER_DIR = ROOT / "md"
HTML_DIR = ROOT / "html"


def inline_markdown(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def render_table(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [inline_markdown(cell.strip()) for cell in line.strip().strip("|").split("|")]
        rows.append(cells)

    header = rows[0]
    body = rows[2:]
    out = ["<table>", "<thead><tr>"]
    out.extend(f"<th>{cell}</th>" for cell in header)
    out.append("</tr></thead><tbody>")
    for row in body:
        out.append("<tr>")
        out.extend(f"<td>{cell}</td>" for cell in row)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def render_markdown(md: str) -> str:
    lines = md.splitlines()
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    table_lines: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(f"<p>{inline_markdown(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            blocks.append("<ul>\n" + "\n".join(f"<li>{item}</li>" for item in list_items) + "\n</ul>")
            list_items = []

    def flush_table() -> None:
        nonlocal table_lines
        if table_lines:
            blocks.append(render_table(table_lines))
            table_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_list()
            flush_table()
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            flush_paragraph()
            flush_list()
            table_lines.append(stripped)
            continue

        flush_table()

        if stripped == "---":
            flush_paragraph()
            flush_list()
            blocks.append("<hr>")
            continue

        if stripped.startswith("#"):
            flush_paragraph()
            flush_list()
            level = min(len(stripped) - len(stripped.lstrip("#")), 4)
            title = stripped[level:].strip()
            blocks.append(f"<h{level}>{inline_markdown(title)}</h{level}>")
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            list_items.append(inline_markdown(stripped[2:].strip()))
            continue

        numbered = re.match(r"^(\d+)\.\s+(.*)$", stripped)
        if numbered:
            flush_paragraph()
            flush_list()
            blocks.append(f"<p class=\"numbered\"><span>{numbered.group(1)}.</span> {inline_markdown(numbered.group(2))}</p>")
            continue

        flush_list()
        paragraph.append(stripped)

    flush_paragraph()
    flush_list()
    flush_table()
    return "\n".join(blocks)


def render_chapter_markdown(md: str) -> str:
    blocks: list[str] = []
    for line in md.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            level = min(len(stripped) - len(stripped.lstrip("#")), 4)
            title = stripped[level:].strip()
            blocks.append(f"<h{level}>{inline_markdown(title)}</h{level}>")
        elif stripped.startswith("***") and stripped.endswith("***") and len(stripped) > 6:
            blocks.append(f"<p class=\"system-line\"><strong>{inline_markdown(stripped.strip('*'))}</strong></p>")
        elif stripped.startswith("**") and stripped.endswith("**") and len(stripped) > 4:
            blocks.append(f"<p class=\"system-line\"><strong>{inline_markdown(stripped.strip('*'))}</strong></p>")
        else:
            blocks.append(f"<p>{inline_markdown(stripped)}</p>")
    return "\n".join(blocks)


def title_from_markdown(md: str, fallback: str) -> str:
    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return fallback


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #202124;
      --muted: #5f6368;
      --line: #d8dee8;
      --paper: #fbfbf8;
      --accent: #245f73;
      --table: #f2f6f7;
    }}
    body {{
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.72;
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 48px 22px 72px;
    }}
    h1, h2, h3 {{
      line-height: 1.25;
      letter-spacing: 0;
    }}
    h1 {{
      font-size: 2.2rem;
      margin: 0 0 22px;
      color: #18333d;
    }}
    h2 {{
      margin-top: 46px;
      padding-top: 18px;
      border-top: 1px solid var(--line);
      color: var(--accent);
      font-size: 1.45rem;
    }}
    h3 {{
      margin-top: 30px;
      font-size: 1.12rem;
    }}
    p, li {{
      font-size: 1rem;
    }}
    p {{
      margin: 12px 0;
    }}
    ul {{
      margin: 10px 0 18px;
      padding-left: 1.4rem;
    }}
    code {{
      background: #e9eef0;
      padding: 0.1rem 0.32rem;
      border-radius: 4px;
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 0.92em;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 18px 0 26px;
      font-size: 0.94rem;
      background: white;
    }}
    th, td {{
      border: 1px solid var(--line);
      padding: 10px 12px;
      vertical-align: top;
    }}
    th {{
      background: var(--table);
      text-align: left;
      color: #18333d;
    }}
    .numbered span {{
      color: var(--accent);
      font-weight: 700;
    }}
    .system-line {{
      color: #37525c;
      background: #eef5f6;
      border-left: 3px solid var(--accent);
      padding: 8px 12px;
    }}
    @media (max-width: 760px) {{
      main {{
        padding: 32px 16px 56px;
      }}
      h1 {{
        font-size: 1.65rem;
      }}
      table {{
        display: block;
        overflow-x: auto;
        white-space: nowrap;
      }}
    }}
  </style>
</head>
<body>
  <main>
{body}
  </main>
</body>
</html>
"""


def main() -> None:
    for src, dst, title in DOCS:
        body = render_markdown((ROOT / src).read_text(encoding="utf-8"))
        (ROOT / dst).write_text(page(title, body), encoding="utf-8")

    HTML_DIR.mkdir(exist_ok=True)
    for src in sorted(CHAPTER_DIR.glob("*.md")):
        md = src.read_text(encoding="utf-8")
        title = title_from_markdown(md, src.stem)
        body = render_chapter_markdown(md)
        (HTML_DIR / f"{src.stem}.html").write_text(page(title, body), encoding="utf-8")


if __name__ == "__main__":
    main()
