from __future__ import annotations

import html
import re
from pathlib import Path


BASE = Path(__file__).parent


def inline(text: str) -> str:
    value = html.escape(text)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    return value


def table_block(lines: list[str]) -> str:
    rows = []
    for line in lines:
        cells = [inline(cell.strip()) for cell in line.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in line.strip().strip("|").split("|")):
            continue
        rows.append(cells)

    if not rows:
        return ""

    out = ["<table>"]
    for index, cells in enumerate(rows):
        tag = "th" if index == 0 else "td"
        out.append("<tr>" + "".join(f"<{tag}>{cell}</{tag}>" for cell in cells) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def build(md_path: Path) -> str:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("# ") else md_path.stem
    body: list[str] = []
    index = 0
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()

        if stripped.startswith("|") and stripped.endswith("|"):
            close_list()
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|") and lines[index].strip().endswith("|"):
                table_lines.append(lines[index])
                index += 1
            body.append(table_block(table_lines))
            continue

        if not stripped:
            close_list()
            index += 1
            continue

        if stripped == "---":
            close_list()
            body.append("<hr>")
            index += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            close_list()
            level = len(heading.group(1))
            body.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            index += 1
            continue

        if stripped.startswith("> "):
            close_list()
            body.append(f"<blockquote>{inline(stripped[2:])}</blockquote>")
            index += 1
            continue

        if stripped.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{inline(stripped[2:])}</li>")
            index += 1
            continue

        close_list()
        body.append(f"<p>{inline(stripped)}</p>")
        index += 1

    close_list()

    return "\n".join(
        [
            "<!doctype html>",
            '<html lang="zh-CN">',
            "<head>",
            '  <meta charset="utf-8">',
            '  <meta name="viewport" content="width=device-width, initial-scale=1">',
            f"  <title>{html.escape(title)}</title>",
            "  <style>",
            "    body { margin: 0; background: #f6f2ea; color: #20242a; font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif; line-height: 1.78; }",
            "    main { max-width: 960px; margin: 0 auto; padding: 48px 24px 72px; background: #fffdf8; min-height: 100vh; box-sizing: border-box; }",
            "    h1 { margin: 0 0 22px; font-size: 2.1rem; line-height: 1.25; }",
            "    h2 { margin: 42px 0 14px; padding-top: 10px; border-top: 1px solid #e3dccf; font-size: 1.45rem; }",
            "    h3 { margin: 28px 0 10px; font-size: 1.15rem; }",
            "    p, li, blockquote { font-size: 1rem; }",
            "    blockquote { margin: 18px 0; padding: 12px 16px; border-left: 4px solid #486b8a; background: #f1f5f8; }",
            "    table { width: 100%; border-collapse: collapse; margin: 16px 0 24px; font-size: .95rem; }",
            "    th, td { border: 1px solid #ded7cb; padding: 8px 10px; vertical-align: top; }",
            "    th { background: #eee7db; text-align: left; }",
            "    code { background: #eee7db; padding: 1px 4px; border-radius: 4px; }",
            "    @media (max-width: 700px) { main { padding: 32px 16px 56px; } table { display: block; overflow-x: auto; white-space: nowrap; } }",
            "  </style>",
            "</head>",
            "<body>",
            "<main>",
            *body,
            "</main>",
            "</body>",
            "</html>",
            "",
        ]
    )


if __name__ == "__main__":
    for md_path in sorted(BASE.glob("*.md")):
        html_path = md_path.with_suffix(".html")
        html_path.write_text(build(md_path), encoding="utf-8")
        print(html_path)
