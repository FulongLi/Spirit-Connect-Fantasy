#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "md"
ZH_MD = ROOT / "zh_md"
ZH_HTML = ROOT / "zh_html"
ASSETS = ROOT / "assets"


CHAPTERS = [
    (0, "00_书名页与写作说明", "00_书名页_版权_献词.md", None, None),
    (1, "01_作者序", "01_作者序.md", None, None),
    (2, "02_前言：吉姆的自述", "02_前言.md", None, None),
    (3, "03_黑水与苏醒", "03_第一章_月暗之旅.md", None, "古战场遗迹"),
    (4, "04_石门之后的战场", "03_第一章_月暗之旅.md", "古战场遗迹", "沙漠与道路"),
    (5, "05_沙路、稻田与小女孩", "03_第一章_月暗之旅.md", "沙漠与道路", "时间切片"),
    (6, "06_蓝黑球体与时间井", "03_第一章_月暗之旅.md", "时间切片", None),
    (7, "07_新世纪与双生", "04_第二章_新世纪.md", None, "准备"),
    (8, "08_第二次数字矫正", "04_第二章_新世纪.md", "准备", "数字世界"),
    (9, "09_数字吉姆的空房间", "04_第二章_新世纪.md", "数字世界", None),
    (10, "10_唯一归来者", "05_第三章_月暗记录.md", None, "会议开始"),
    (11, "11_月暗记录会议", "05_第三章_月暗记录.md", "会议开始", "吉姆深吸一口气，说道：“那……我就从她给我看到的，第一个片段开始说起，生命的诞生。”"),
    (12, "12_生命起源的外壳", "05_第三章_月暗记录.md", "吉姆深吸一口气，说道：“那……我就从她给我看到的，第一个片段开始说起，生命的诞生。”", "人来自哪里？"),
    (13, "13_人类是宿主", "05_第三章_月暗记录.md", "人来自哪里？", "斯皮尔先生开口：“那么，人类的灵魂来自哪里？”"),
    (14, "14_神话开始对号", "05_第三章_月暗记录.md", "斯皮尔先生开口：“那么，人类的灵魂来自哪里？”", "月球的形成"),
    (15, "15_月球的工程真相", "05_第三章_月暗记录.md", "月球的形成", "“他们后来做了什么？”斯皮尔先生开口，语气不疾不徐。"),
    (16, "16_海底基地与监视系统", "05_第三章_月暗记录.md", "“他们后来做了什么？”斯皮尔先生开口，语气不疾不徐。", "暂时先这样"),
    (17, "17_数字亚瑟", "05_第三章_月暗记录.md", "暂时先这样", None),
    (18, "18_童年的另一个世界", "06_第四章_另一个世界.md", None, "中世纪世界"),
    (19, "19_隐藏任务", "06_第四章_另一个世界.md", "中世纪世界", "快点醒来吧，我的朋友们"),
    (20, "20_月暗副本", "06_第四章_另一个世界.md", "快点醒来吧，我的朋友们", None),
    (21, "21_克罗斯与肖恩", "07_第五章_半纪往事.md", None, "黑潮时代"),
    (22, "22_黑潮以后", "07_第五章_半纪往事.md", "黑潮时代", "坠毁飞船"),
    (23, "23_罗斯威尔遗产", "07_第五章_半纪往事.md", "坠毁飞船", "死球"),
    (24, "24_死球理论", "07_第五章_半纪往事.md", "死球", None),
    (25, "25_再见小女孩", "08_第六章_无尽的等待.md", None, "我深吸一口气，几乎是本能地问出了下一句：“那有没有办法可以阻止月球守卫他们？”"),
    (26, "26_解构倒计时", "08_第六章_无尽的等待.md", "我深吸一口气，几乎是本能地问出了下一句：“那有没有办法可以阻止月球守卫他们？”", "商量对策"),
    (27, "27_三天失败", "08_第六章_无尽的等待.md", "商量对策", "公司的往事"),
    (28, "28_斯皮尔的旧梦", "08_第六章_无尽的等待.md", "公司的往事", "卢博士低声问：“你认为……出口在月球暗面？”"),
    (29, "29_LUNA-EXIT", "08_第六章_无尽的等待.md", "卢博士低声问：“你认为……出口在月球暗面？”", None),
    (30, "30_不可返回区域", "09_第七章_接近真相.md", None, "抵达月球暗面"),
    (31, "31_发射", "09_第七章_接近真相.md", "抵达月球暗面", "月球在舷窗中逐渐变大。不是电影里那种浪漫的白色球体，而是一颗布满阴影与陨痕的冷硬天体。当飞船绕行至暗面时，地球的光彻底消失了。"),
    (32, "32_月球暗面着陆", "09_第七章_接近真相.md", "月球在舷窗中逐渐变大。不是电影里那种浪漫的白色球体，而是一颗布满阴影与陨痕的冷硬天体。当飞船绕行至暗面时，地球的光彻底消失了。", "肉体死亡"),
    (33, "33_肉体死亡", "09_第七章_接近真相.md", "肉体死亡", "泰拉撒记录。"),
    (34, "34_泰拉撒第一层门", "09_第七章_接近真相.md", "泰拉撒记录。", "未完待续......"),
    (35, "35_下一本入口", "09_第七章_接近真相.md", "未完待续......", None),
]


def find_marker(lines: list[str], marker: str, start_at: int = 0) -> int:
    for idx in range(start_at, len(lines)):
        line = lines[idx].strip()
        if line == marker or line.startswith(marker):
            return idx
    raise ValueError(f"Marker not found: {marker}")


def source_slice(filename: str, start: str | None, end: str | None) -> str:
    lines = (SRC / filename).read_text(encoding="utf-8").splitlines()
    start_idx = find_marker(lines, start) if start else 0
    end_idx = find_marker(lines, end, start_idx + 1) if end else len(lines)
    chunk = lines[start_idx:end_idx]

    while chunk and not chunk[0].strip():
        chunk.pop(0)
    if chunk and chunk[0].lstrip().startswith("# "):
        chunk = chunk[1:]
    while chunk and not chunk[0].strip():
        chunk.pop(0)
    while chunk and not chunk[-1].strip():
        chunk.pop()
    return "\n".join(chunk).strip()


def reading_markdown(stem: str, prose: str) -> str:
    title = stem.replace("_", " ", 1)
    return f"# {title}\n\n{prose.strip()}\n"


def inline_markup(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def markdown_to_html(markdown: str, title: str, css_href: str = "../assets/style.css", nav_html: str = "") -> str:
    body: list[str] = []
    in_ul = False
    in_quote = False

    def close_lists() -> None:
        nonlocal in_ul
        if in_ul:
            body.append("</ul>")
            in_ul = False

    def close_quote() -> None:
        nonlocal in_quote
        if in_quote:
            body.append("</blockquote>")
            in_quote = False

    for raw in markdown.splitlines():
        line = raw.rstrip()
        if not line:
            close_lists()
            close_quote()
            continue
        if line.startswith("# "):
            close_lists()
            close_quote()
            body.append(f"<h1>{inline_markup(line[2:].strip())}</h1>")
        elif line.startswith("## "):
            close_lists()
            close_quote()
            body.append(f"<h2>{inline_markup(line[3:].strip())}</h2>")
        elif line.startswith("### "):
            close_lists()
            close_quote()
            body.append(f"<h3>{inline_markup(line[4:].strip())}</h3>")
        elif line.startswith("- "):
            close_quote()
            if not in_ul:
                body.append("<ul>")
                in_ul = True
            body.append(f"<li>{inline_markup(line[2:].strip())}</li>")
        elif line.startswith("> "):
            close_lists()
            if not in_quote:
                body.append("<blockquote>")
                in_quote = True
            body.append(f"<p>{inline_markup(line[2:].strip())}</p>")
        else:
            close_lists()
            close_quote()
            body.append(f"<p>{inline_markup(line)}</p>")

    close_lists()
    close_quote()
    return (
        "<!doctype html>\n"
        '<html lang="zh-CN">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{html.escape(title)}</title>\n"
        f'  <link rel="stylesheet" href="{html.escape(css_href)}">\n'
        "</head>\n"
        "<body><main>\n"
        + "\n".join(body)
        + ("\n" + nav_html if nav_html else "")
        + "\n</main></body>\n</html>\n"
    )


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
        '<a href="../index.html">目录 / Index</a>\n'
        f"{next_}\n"
        "</nav>"
    )


def write_index() -> None:
    lines = [
        "# 月球暗面 V2 中文阅读目录",
        "",
        "点击章节标题开始阅读。",
        "",
        "## 章节目录",
    ]
    for _, stem, _, _, _ in CHAPTERS:
        label = stem.replace("_", " ", 1)
        lines.append(f"- [{label}](zh_html/{stem}.html)")
    lines.append("")
    index_md = "\n".join(lines) + "\n"
    (ROOT / "index.md").write_text(index_md, encoding="utf-8")
    (ROOT / "index.html").write_text(markdown_to_html(index_md, "月球暗面 V2 中文结构正文稿", "assets/style.css"), encoding="utf-8")


def update_readme() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    text = text.replace(
        "- `zh_md/`：参考《巨鲸陨落_V1》格式生成的中文章节框架卡。\n"
        "- `zh_html/`：中文章节框架卡阅读 HTML。\n",
        "- `zh_md/`：按《巨鲸陨落_V1》格式拆分后的中文结构正文稿，已填入当前 V2 母本对应正文。\n"
        "- `zh_html/`：中文结构正文稿阅读 HTML。\n",
    )
    text = text.replace(
        "- 新增 `zh_md/en_md` 是结构卡，不替代正文。\n"
        "- 后续如果采用此框架，应先由作者确认，再逐章把正文从 `md/` 迁移或扩写到新结构中。\n",
        "- `zh_md/zh_html` 现在是供阅读和讨论的结构正文稿，不替代 `md/` 母本。\n"
        "- `en_md/en_html` 仍是英文框架参考层，待中文拆分确认后再同步正文翻译。\n",
    )
    (ROOT / "README.md").write_text(text, encoding="utf-8")


def main() -> None:
    ASSETS.mkdir(exist_ok=True)
    ZH_MD.mkdir(exist_ok=True)
    ZH_HTML.mkdir(exist_ok=True)
    stems = [stem for _, stem, _, _, _ in CHAPTERS]
    for idx, (_, stem, filename, start, end) in enumerate(CHAPTERS):
        prose = source_slice(filename, start, end)
        filled = reading_markdown(stem, prose)
        md_path = ZH_MD / f"{stem}.md"
        md_path.write_text(filled, encoding="utf-8")
        html_path = ZH_HTML / f"{stem}.html"
        title = stem.replace("_", " ", 1)
        prev_stem = stems[idx - 1] if idx > 0 else None
        next_stem = stems[idx + 1] if idx + 1 < len(stems) else None
        html_path.write_text(markdown_to_html(filled, title, nav_html=chapter_nav(prev_stem, next_stem)), encoding="utf-8")
    write_index()
    update_readme()


if __name__ == "__main__":
    main()
