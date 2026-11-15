#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOVELS = ROOT.parent
SOURCE_DIR = NOVELS / "巨鲸陨落_V1" / "zh_md"
CHAPTER_DIR = ROOT / "chapters"
CONFIG = ROOT / "novel-config.tex"


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
    return index, title, lines[1:]


def body_to_tex(lines: list[str]) -> str:
    out: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            if out and out[-1] != "":
                out.append("")
            continue
        if line in {"......", "……", "---", "***"}:
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
    return f"\\chapter{{{tex_escape(title)}}}\n\n" + body_to_tex(body)


def update_config() -> None:
    CONFIG.write_text(
        r"""% ============================================================
% 小说基本信息：通常只需要修改本文件
% ============================================================
\newcommand{\noveltitle}{巨鲸陨落}
\newcommand{\novelsubtitle}{灵接科技 第二部}
\newcommand{\novelauthor}{李富龙}
\newcommand{\novelseries}{灵接科技}
\newcommand{\novelversion}{V1 中文阅读稿}
\newcommand{\noveldate}{2026年6月17日}
\newcommand{\novelpublisher}{个人作品}
\newcommand{\novelcopyright}{版权所有，未经许可不得转载。}
\newcommand{\novelisbn}{ISBN：待定}

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
    for path in CHAPTER_DIR.glob("*.tex"):
        if path.name != "chapters-list.tex":
            path.unlink()

    source_files = sorted(SOURCE_DIR.glob("*.md"))
    generated: list[Path] = []
    for md_path in source_files:
        index, title, body = parse_markdown(md_path)
        if index == 0:
            continue
        output = CHAPTER_DIR / f"{index:02d}-chapter-{index:02d}.tex"
        output.write_text(chapter_to_tex(index, title, body), encoding="utf-8")
        generated.append(output)

    lines = [
        "% 本文件由 tools/import_giant_whale_fall.py 自动生成，请勿手工修改。",
        "% 在项目根目录运行：python tools/import_giant_whale_fall.py",
    ]
    for path in sorted(generated):
        lines.append(f"\\input{{chapters/{path.stem}}}")
    (CHAPTER_DIR / "chapters-list.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")
    update_config()
    print(f"Imported {len(generated)} chapters from {SOURCE_DIR}")


if __name__ == "__main__":
    main()
