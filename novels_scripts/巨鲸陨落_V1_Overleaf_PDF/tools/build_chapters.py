#!/usr/bin/env python3
"""扫描 chapters 目录并自动生成 chapters-list.tex。

用法：
    python tools/build_chapters.py

规则：
- 文件名以数字开头，例如 01-prologue.tex、02-chapter.tex。
- 忽略 chapters-list.tex。
- 按文件名字典序排列。
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "chapters"
OUTPUT = CHAPTER_DIR / "chapters-list.tex"

files = sorted(
    p for p in CHAPTER_DIR.glob("*.tex")
    if p.name != OUTPUT.name and p.name[:1].isdigit()
)

lines = [
    "% 本文件由 tools/build_chapters.py 自动生成，请勿手工修改。",
    "% 在项目根目录运行：python tools/build_chapters.py",
]
for path in files:
    lines.append(f"\\input{{chapters/{path.stem}}}")

OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Generated {OUTPUT.relative_to(ROOT)} with {len(files)} chapters.")
