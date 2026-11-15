from __future__ import annotations

import html
import re
from pathlib import Path


BASE = Path(__file__).parent
MD_DIR = BASE / "md"
HTML_DIR = BASE / "html"


def inline_markup(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"\*\*\*([^*]+)\*\*\*", r"<strong><em>\1</em></strong>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    return escaped


def html_for_md(md_path: Path) -> str:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    title = md_path.stem
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]

    parts = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        f"  <title>{html.escape(title)} - 月球暗面 V2</title>",
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
    HTML_DIR.mkdir(exist_ok=True)
    expected_html = {md_path.stem + ".html" for md_path in MD_DIR.glob("*.md")}
    for html_path in HTML_DIR.glob("*.html"):
        if html_path.name not in expected_html:
            html_path.unlink()

    index_rows: list[tuple[str, str, str]] = []
    for md_path in sorted(MD_DIR.glob("*.md")):
        html_path = HTML_DIR / (md_path.stem + ".html")
        html_path.write_text(html_for_md(md_path), encoding="utf-8")
        title = md_path.stem
        first = md_path.read_text(encoding="utf-8").splitlines()[0]
        if first.startswith("# "):
            title = first[2:].strip()
        index_rows.append((title, md_path.relative_to(BASE).as_posix(), html_path.relative_to(BASE).as_posix()))

    index_md = [
        "# 月球暗面 V2",
        "",
        "- [V2 修订路线 CN](V2修订路线_CN.md) | [HTML](V2修订路线_CN.html)",
        "- [V2 Revision Roadmap EN](V2_revision_roadmap_EN.md) | [HTML](V2_revision_roadmap_EN.html)",
        "- [月球暗面口吻规则 CN](月球暗面_口吻规则_CN.md) | [HTML](月球暗面_口吻规则_CN.html)",
        "- [Moon Dark Side Voice Rules EN](moon_dark_side_voice_rules_EN.md) | [HTML](moon_dark_side_voice_rules_EN.html)",
        "",
    ]
    for title, md_rel, html_rel in index_rows:
        index_md.append(f"- [{title}]({md_rel}) | [HTML]({html_rel})")
    index_md.append("")
    (BASE / "index.md").write_text("\n".join(index_md), encoding="utf-8")

    index_html = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '  <meta charset="utf-8">',
        '  <meta name="viewport" content="width=device-width, initial-scale=1">',
        "  <title>月球暗面 V2</title>",
        "  <style>body{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Microsoft YaHei',sans-serif;line-height:1.8;margin:40px auto;max-width:820px;padding:0 24px;color:#1f2328;background:#fffdf9}a{color:#2458a6}li{margin:.35em 0}</style>",
        "</head>",
        "<body>",
        "  <h1>月球暗面 V2</h1>",
        '  <p><a href="V2修订路线_CN.html">V2 修订路线 CN</a> | <a href="V2_revision_roadmap_EN.html">V2 Revision Roadmap EN</a></p>',
        '  <p><a href="月球暗面_口吻规则_CN.html">月球暗面口吻规则 CN</a> | <a href="moon_dark_side_voice_rules_EN.html">Moon Dark Side Voice Rules EN</a></p>',
        "  <ul>",
    ]
    for title, md_rel, html_rel in index_rows:
        index_html.append(
            f'    <li>{html.escape(title)} - <a href="{html.escape(md_rel)}">MD</a> | <a href="{html.escape(html_rel)}">HTML</a></li>'
        )
    index_html.extend(["  </ul>", "</body>", "</html>", ""])
    (BASE / "index.html").write_text("\n".join(index_html), encoding="utf-8")

    print(f"rebuilt {len(index_rows)} chapters")


if __name__ == "__main__":
    main()
