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


def build(md_path: Path) -> str:
    lines = md_path.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("# ") else md_path.stem
    body: list[str] = []
    in_list = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    for raw in lines:
        stripped = raw.strip()
        if not stripped:
            close_list()
            continue
        heading = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading:
            close_list()
            level = len(heading.group(1))
            body.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            continue
        if stripped.startswith("> "):
            close_list()
            body.append(f"<blockquote>{inline(stripped[2:])}</blockquote>")
            continue
        if stripped.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{inline(stripped[2:])}</li>")
            continue
        close_list()
        body.append(f"<p>{inline(stripped)}</p>")

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
            "    main { max-width: 900px; margin: 0 auto; padding: 48px 24px 72px; background: #fffdf8; min-height: 100vh; box-sizing: border-box; }",
            "    h1 { margin: 0 0 22px; font-size: 2.1rem; line-height: 1.25; }",
            "    h2 { margin: 38px 0 14px; padding-top: 10px; border-top: 1px solid #e3dccf; font-size: 1.45rem; }",
            "    h3 { margin: 26px 0 10px; font-size: 1.15rem; }",
            "    p, li, blockquote { font-size: 1rem; }",
            "    blockquote { margin: 18px 0; padding: 12px 16px; border-left: 4px solid #486b8a; background: #f1f5f8; }",
            "    code { background: #eee7db; padding: 1px 4px; border-radius: 4px; }",
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
    for md_path in [
        BASE / "V2修订路线_CN.md",
        BASE / "V2_revision_roadmap_EN.md",
        BASE / "月球暗面_口吻规则_CN.md",
        BASE / "moon_dark_side_voice_rules_EN.md",
    ]:
        html_path = md_path.with_suffix(".html")
        html_path.write_text(build(md_path), encoding="utf-8")
        print(html_path)
