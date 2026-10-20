#!/usr/bin/env python3
"""Static checks for the published site: local links, chapter twins, prev/next order,
soundtrack files and leftover placeholders. Run from anywhere:

  python3 tools/check_site.py
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
problems = []
checked = 0


def resolves(base, href):
    u = urlsplit(href)
    if u.scheme or href.startswith(("#", "mailto:", "javascript:", "//", "${")):
        return True
    path = unquote(u.path)
    if not path:
        return True
    target = (base.parent / path).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target.exists()


for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in (".git", "original-novel-texts", "node_modules")]
    for name in filenames:
        if not name.endswith((".html", ".css")):
            continue
        page = Path(dirpath) / name
        text = page.read_text(encoding="utf-8")
        for href in re.findall(r'(?:href|src)="([^"]+)"', text) + re.findall(r"url\('([^']+)'\)", text):
            checked += 1
            if not resolves(page, href):
                problems.append(f"{page.relative_to(ROOT)}: broken link {href}")
        if name.endswith(".html"):
            if re.search(r"978-1-x|xxxxxx", text):
                problems.append(f"{page.relative_to(ROOT)}: placeholder ISBN")
            if re.search(r"\*<strong>|<p>\*[^<]+\*</p>", text):
                problems.append(f"{page.relative_to(ROOT)}: unconverted Markdown emphasis")

app = (ROOT / "app.js").read_text(encoding="utf-8")
for href in re.findall(r'"((?:assets|novels)/[^"]+)"', app):
    checked += 1
    if not resolves(ROOT / "index.html", href):
        problems.append(f"app.js: broken link {href}")

for book in sorted((ROOT / "novels").iterdir()):
    zh, en = book / "zh_html", book / "en_html"
    if not zh.is_dir():
        continue
    for missing in {p.name for p in zh.glob("*.html")} ^ {p.name for p in en.glob("*.html")}:
        problems.append(f"{book.name}: chapter has no language twin: {missing}")
    index = (book / "index.html").read_text(encoding="utf-8")
    index = index[index.index("chapter-list"):]
    order = [unquote(h) for h in re.findall(r'href="zh_html/([^"]+)"', index)]
    for folder in (zh, en):
        for i, name in enumerate(order):
            text = (folder / name).read_text(encoding="utf-8")
            if text.count("<nav") != 1:
                problems.append(f"{book.name}/{folder.name}/{name}: expected exactly one nav")
            links = [unquote(h) for h in re.findall(r'href="([^"]+)"', text[text.rfind("<nav"):]) if h != "../index.html"]
            want = [n for n in ((order[i - 1] if i else None), (order[i + 1] if i + 1 < len(order) else None)) if n]
            if links != want:
                problems.append(f"{book.name}/{folder.name}/{name}: prev/next {links} != {want}")
    catalog = book / "soundtrack" / "catalog.js"
    if catalog.exists():
        for src in re.findall(r'src: "([^"]+)"', catalog.read_text(encoding="utf-8")):
            checked += 1
            if not (book / "soundtrack" / src).exists():
                problems.append(f"{book.name}: missing audio {src}")

print(f"Checked {checked} references.")
for p in problems:
    print("  -", p)
sys.exit(1 if problems else 0)
