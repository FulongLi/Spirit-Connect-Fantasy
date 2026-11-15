from __future__ import annotations

import re
from pathlib import Path


BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
SOURCE = ROOT / "月球暗面_重写稿_v0.1.md"
MD_DIR = BASE / "md"


def slug(title: str) -> str:
    value = re.sub(r"[\\/:：*?\"<>|]+", "_", title)
    value = re.sub(r"\s+", "", value)
    return value.strip("_")


def split_sections(text: str) -> list[tuple[str, list[str]]]:
    lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    sections: list[tuple[str, list[str]]] = []
    current_title = ""
    current_lines: list[str] = []

    for line in lines:
        if line.startswith("# "):
            current_title = line[2:].strip()
            current_lines = []
            continue
        if line.startswith("## "):
            if current_title:
                sections.append((current_title, current_lines))
            current_title = line[3:].strip()
            current_lines = []
            continue
        current_lines.append(line)

    if current_title:
        sections.append((current_title, current_lines))
    return sections


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    sections = split_sections(text)

    MD_DIR.mkdir(exist_ok=True)
    for path in MD_DIR.glob("*.md"):
        path.unlink()

    for index, (title, lines) in enumerate(sections):
        filename = f"{index:02d}_{slug(title)}.md"
        body = "\n".join(lines).strip()
        content = f"# {title}\n"
        if body:
            content += f"\n{body}\n"
        (MD_DIR / filename).write_text(content, encoding="utf-8")

    print(f"wrote {len(sections)} V2 chapter files")


if __name__ == "__main__":
    main()
