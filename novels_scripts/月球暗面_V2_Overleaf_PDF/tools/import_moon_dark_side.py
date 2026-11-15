#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOVELS = ROOT.parent
SOURCE_DIR = NOVELS / "月球暗面_V2" / "zh_md"
CHAPTER_DIR = ROOT / "chapters"
CONFIG = ROOT / "novel-config.tex"


SPECIAL_FILES = {
    0: "00-title-notes.tex",
    1: "01-prologue.tex",
    2: "02-first-chapter.tex",
}

CHAPTER_FILE_LABELS = {
    3: "black-water-awakening",
    4: "battlefield-beyond-gate",
    5: "sand-road-rice-field-little-girl",
    6: "blue-black-sphere-time-well",
    7: "new-century-dual-born",
    8: "second-digital-correction",
    9: "digital-jim-empty-room",
    10: "only-returnee",
    11: "moon-dark-record-meeting",
    12: "origin-of-life-shell",
    13: "humanity-as-host",
    14: "myths-align",
    15: "engineered-moon",
    16: "undersea-base-monitoring",
    17: "digital-arthur",
    18: "childhood-other-world",
    19: "hidden-quest",
    20: "moon-dark-instance",
    21: "cross-and-shawn",
    22: "after-black-tide",
    23: "roswell-inheritance",
    24: "dead-world-theory",
    25: "little-girl-returns",
    26: "deconstruction-countdown",
    27: "three-days-failure",
    28: "spire-old-dream",
    29: "luna-exit",
    30: "no-return-zone",
    31: "launch",
    32: "dark-side-landing",
    33: "bodily-death",
    34: "first-terasha-gate",
    35: "next-book-door",
}


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
        "⚠": r"\textbf{!}",
        "♾": r"$\infty$",
    }
    return "".join(replacements.get(ch, ch) for ch in text if ch != "\ufe0f")


def inline_markup(text: str) -> str:
    escaped = tex_escape(text)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", escaped)
    return escaped


def chapter_filename(index: int, title: str) -> str:
    if index in SPECIAL_FILES:
        return SPECIAL_FILES[index]
    label = CHAPTER_FILE_LABELS.get(index, f"chapter-{index:02d}")
    return f"{index:02d}-{label}.tex"


def parse_markdown(path: Path) -> tuple[int, str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or not lines[0].startswith("# "):
        raise ValueError(f"Missing title in {path}")
    heading = lines[0][2:].strip()
    match = re.match(r"(\d+)\s+(.+)", heading)
    if not match:
        raise ValueError(f"Unexpected heading: {heading}")
    index = int(match.group(1))
    title = match.group(2).strip()
    body = lines[1:]
    return index, title, body


def body_to_tex(lines: list[str]) -> str:
    out: list[str] = []

    for raw in lines:
        line = raw.strip()
        if not line:
            if out and out[-1] != "":
                out.append("")
            continue
        if line == "......":
            out.append(r"\SceneBreak")
            out.append("")
            continue
        if line.startswith("#"):
            continue
        if line.startswith("***") and line.endswith("***") and len(line) > 6:
            content = line.strip("*")
            out.append(r"\begin{center}")
            out.append(r"\textbf{" + tex_escape(content) + "}")
            out.append(r"\end{center}")
            out.append("")
            continue
        if line.startswith("**") and line.endswith("**") and len(line) > 4:
            content = line.strip("*")
            out.append(r"\begin{center}")
            out.append(r"\textbf{" + tex_escape(content) + "}")
            out.append(r"\end{center}")
            out.append("")
            continue
        out.append(inline_markup(line))
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def chapter_to_tex(index: int, title: str, body: list[str]) -> str:
    escaped_title = tex_escape(title)
    if index <= 2:
        header = (
            f"\\chapter*{{{escaped_title}}}\n"
            f"\\addcontentsline{{toc}}{{chapter}}{{{escaped_title}}}\n\n"
        )
    else:
        header = f"\\chapter{{{escaped_title}}}\n\n"
    return header + body_to_tex(body)


def update_config() -> None:
    CONFIG.write_text(
        r"""% ============================================================
% 小说基本信息：通常只需要修改本文件
% ============================================================
\newcommand{\noveltitle}{月球暗面}
\newcommand{\novelsubtitle}{灵接科技 第一部}
\newcommand{\novelauthor}{李富龙}
\newcommand{\novelseries}{灵接科技}
\newcommand{\novelversion}{V2 中文阅读稿}
\newcommand{\noveldate}{2026年6月15日}
\newcommand{\novelpublisher}{个人作品}
\newcommand{\novelcopyright}{版权所有，未经许可不得转载。}
\newcommand{\novelisbn}{ISBN：978-1-xxxxxx-xx}

% 封面图片：把图片放到 assets/cover.jpg；没有图片时自动使用纯文字封面
\newcommand{\coverimage}{assets/cover.jpg}

% true / false
\newif\ifshowtoc
\showtoctrue
\newif\ifshowafterword
\showafterwordfalse
""",
        encoding="utf-8",
    )


def main() -> None:
    CHAPTER_DIR.mkdir(exist_ok=True)
    source_files = sorted(SOURCE_DIR.glob("*.md"))
    if not source_files:
        raise SystemExit(f"No Markdown files found in {SOURCE_DIR}")

    generated: list[Path] = []
    for md_path in source_files:
        index, title, body = parse_markdown(md_path)
        output = CHAPTER_DIR / chapter_filename(index, title)
        output.write_text(chapter_to_tex(index, title, body), encoding="utf-8")
        generated.append(output)

    lines = [
        "% 本文件由 tools/import_moon_dark_side.py 自动生成，请勿手工修改。",
        "% 在项目根目录运行：python tools/import_moon_dark_side.py",
    ]
    for path in sorted(generated):
        lines.append(f"\\input{{chapters/{path.stem}}}")
    (CHAPTER_DIR / "chapters-list.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    update_config()
    print(f"Imported {len(generated)} chapters from {SOURCE_DIR}")


if __name__ == "__main__":
    main()
