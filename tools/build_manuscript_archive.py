#!/usr/bin/env python3
"""Build the local original-manuscript archive (original-novel-texts/).

Copies author-owned manuscript files from the Novels working directory into
original-novel-texts/<work>/source/<version>/, byte for byte (timestamps
preserved, SHA-256 verified), writes a manifest.json and, for works with a
complete chapter-split text, a concatenated UTF-8 Markdown edition.

The Novels workspace is only ever read. The output directory is gitignored:
nothing here is published until the author reviews INVENTORY.md.

Usage:
  python3 tools/build_manuscript_archive.py "/Volumes/Fulong SSD/1Mac/novels"
"""

import datetime
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "original-novel-texts"
SKIP_NAMES = {".DS_Store"}

# (work, version id, label, status, source path relative to the workspace,
#  files to take: "dir/*.md" style patterns relative to that path, languages)
VERSIONS = [
    ("dark-moon", "original-pages", "Original full text (Apple Pages document)", "original",
     ".", ["月球暗面全.pages"], ["zh"]),
    ("dark-moon", "v1-original-split", "V1: original text split into chapters (from a plain-text copy of the full original)", "superseded",
     "月球暗面_V1", ["md/*.md", "index.md"], ["zh"]),
    ("dark-moon", "revision-worksheet-v0.1", "Revision worksheet v0.1 (修订工作稿)", "working-draft",
     ".", ["月球暗面_修订工作稿_v0.1.md", "月球暗面_修订工作稿_v0.1.docx"], ["zh"]),
    ("dark-moon", "rewrite-v0.1", "Rewrite draft v0.1 (重写稿)", "alternate-draft",
     ".", ["月球暗面_重写稿_v0.1.md", "月球暗面_重写稿_v0.1.docx"], ["zh"]),
    ("dark-moon", "v2-abandoned-20260610", "V2 attempt marked void by the author on 2026-06-10 (作废备份)", "abandoned",
     "月球暗面_V2_作废备份_20260610", ["md/*.md", "index.md", "V2修订路线_CN.md", "V2_revision_roadmap_EN.md", "月球暗面_口吻规则_CN.md", "moon_dark_side_voice_rules_EN.md"], ["zh", "en"]),
    ("dark-moon", "v2-master", "V2 Chinese master text (母本, renamed cast)", "canonical-master",
     "月球暗面_V2", ["md/*.md", "README.md", "V2重启修订框架_CN.md", "V2_restart_revision_framework_EN.md"], ["zh", "en"]),
    ("dark-moon", "v2-reading", "V2 structured reading edition, Chinese + English (source of the website pages)", "canonical-reading",
     "月球暗面_V2", ["zh_md/*.md", "en_md/*.md", "index.md", "index_EN.md"], ["zh", "en"]),
    ("whale-fall", "v1-reading", "V1 second-draft reading edition, Chinese + English (source of the website pages)", "canonical-reading",
     "巨鲸陨落_V1", ["zh_md/*.md", "en_md/*.md", "index.md", "index_EN.md", "README.md", "V1二稿第一轮结构修订记录.md", "修订记录_01_23_novel_writing_pass.md", "V1结构审稿报告.md"], ["zh", "en"]),
    ("crimson-cruise", "v1-chapter-seeds", "V1 chapter framework seeds (outline, not prose)", "planning",
     "血色游轮_V1", ["zh_md/*.md", "en_md/*.md", "故事框架_CN.md", "story_framework_EN.md", "README.md", "index.md", "index_EN.md"], ["zh", "en"]),
    ("spacetime-labyrinth", "framework", "Story framework (planning notes, no prose yet)", "planning",
     "时空迷宫", ["故事框架_CN.md", "README.md", "index.md"], ["zh"]),
    ("series-bible", "settings", "Series bible and collaboration rules (灵接科技 设定文档)", "reference",
     "灵接科技_设定文档", ["灵接科技_系列设定.md", "灵接科技_系列设定_EN.md", "灵接科技_总框架_创作方向_CN.md", "协作规则_CN.md", "collaboration_rules_EN.md"], ["zh", "en"]),
]

# Complete chapter-split texts that get a single-file Markdown edition.
EDITIONS = [
    ("dark-moon", "v2-reading", "zh_md", "manuscript.zh.md"),
    ("dark-moon", "v2-reading", "en_md", "manuscript.en.md"),
    ("dark-moon", "v1-original-split", "md", "original-v1.zh.md"),
    ("whale-fall", "v1-reading", "zh_md", "manuscript.zh.md"),
    ("whale-fall", "v1-reading", "en_md", "manuscript.en.md"),
]

WORKS = {
    "dark-moon": {"title": {"zh": "月球暗面", "en": "Darkside of the Moon"}, "archive": 1, "website": "novels/dark-moon/"},
    "whale-fall": {"title": {"zh": "巨鲸陨落", "en": "Whale Fall"}, "archive": 2, "website": "novels/whale-fall/"},
    "mystic-cat": {"title": {"zh": "灵猫", "en": "Mystic Cat"}, "archive": 3, "website": "novels/mystic-cat/"},
    "crimson-cruise": {"title": {"zh": "血色邮轮", "en": "The Crimson Cruise"}, "working_title": {"zh": "血色游轮", "en": "The Blood-Red Cruise"}, "archive": 4, "website": "novels/crimson-cruise/"},
    "spacetime-labyrinth": {"title": {"zh": "时空迷宫", "en": "Spacetime Labyrinth"}, "archive": 5, "website": "novels/spacetime-labyrinth/"},
    "where-souls-return": {"title": {"zh": "灵魂归处", "en": "Where Souls Return"}, "archive": 6, "website": "novels/where-souls-return/"},
    "series-bible": {"title": {"zh": "灵接科技 系列设定", "en": "Spirit Connect series bible"}, "archive": None, "website": None},
}

# Review notes recorded in the manifest (findings from comparing the sources
# with the published reading pages; update them when either side changes).
NOTES = {
    "dark-moon": {
        "publication": "Published: English e-book on Apple Books, 'Independently published', released 2025-12-31 (verified 2026-10-20). That edition predates the V2 cast renames. No ISBN found.",
        "website_comparison": [
            "Website zh_html/en_html were built from v2-reading; chapter count (36) and paragraph count match in every chapter.",
            "00 front matter: website shows a cleaned copyright page instead of the manuscript's title page / writing notes (intentional).",
            "zh_md 11 and 21: website already spells the names Elias Spire and Shawn Corbin; the manuscript still has 'Elias Speer' and 'Sean Corbin'. Website is newer.",
            "en_md 01 Author's Note: the website carries a revised translation (edited 2026-06-21 after en_md); 14 of 15 paragraphs differ. Website is newer; back-port to en_md if it is the preferred text.",
            "v2-master (md/) and v2-reading (zh_md/) are ~99.8% identical after normalising whitespace; v1-original-split differs from v2-master mainly by the cast renames (Jim Dickens -> Jim Vale, Charlie Filler -> Charlie Hale).",
        ],
        "manuscript_inconsistency": "zh_md 08 describes the new pods as 'upright egg-shaped capsules' (竖立的蛋形胶囊) yet in 09 Jim lies fully flat inside one; 03 floods the pod with black liquid while 08 says the new pods no longer need it (possibly intentional if 03 is an earlier session).",
    },
    "whale-fall": {
        "publication": "Not formally published. Reading draft on the website.",
        "website_comparison": [
            "Website pages were built from v1-reading; all 49 chapters match paragraph for paragraph in both languages.",
            "Website adds the shared series 作者序 page (not part of this manuscript folder) and replaces 00 writing notes with a copyright page.",
            "English manuscript and reader spell the planet 'Phaeton'; the homepage now uses the same spelling.",
        ],
    },
    "crimson-cruise": {
        "publication": "UNPUBLISHED. Chapter framework seeds only (each chapter is marked 状态：框架种子). Website shows a 'coming soon' page.",
        "title_note": "Working title in the manuscript is 血色游轮 / The Blood-Red Cruise; covers and website use 血色邮轮 / The Crimson Cruise. Author to decide.",
        "series_order_note": "The series bible lists it as the chronological prequel (book 1); the website archive numbers it IV.",
    },
    "spacetime-labyrinth": {"publication": "UNPUBLISHED planning notes only; no prose."},
    "mystic-cat": {"publication": "No manuscript found in the Novels workspace."},
    "where-souls-return": {"publication": "No manuscript found in the Novels workspace."},
    "series-bible": {"publication": "UNPUBLISHED reference material containing plot plans and reveals for unwritten books."},
}

# Things in the workspace that are deliberately not archived.
EXCLUDED = [
    ("*/html, */zh_html, */en_html, *.html", "Generated HTML exports of the Markdown sources."),
    ("*_Overleaf_PDF/, 月球暗面_V2_Overleaf_PDF.zip, *.pdf", "LaTeX/PDF typesetting builds generated from the Markdown chapters."),
    ("Chinese_Novel_Overleaf_Template/", "Typesetting template (tooling)."),
    ("chinese-novelist-skill-master/", "Third-party writing skill; not author-owned."),
    (".codex/, AGENTS.md", "AI-assistant configuration and project instructions."),
    ("*.py (build_*, expand_whale_chapters_*, revise_*, render_docx, split_*)", "Generation/revision scripts. Some embed draft prose used to produce the chapter files; the resulting chapter files are archived instead."),
    ("render_check/", "Rendering previews."),
    ("._*, .DS_Store", "macOS metadata files."),
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def write_if_changed(path, text):
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    path.write_text(text, encoding="utf-8")


def collect(base, patterns):
    files = []
    for pattern in patterns:
        matches = sorted(base.glob(pattern))
        if not matches:
            raise SystemExit(f"Missing expected source: {base / pattern}")
        files += [m for m in matches if m.is_file() and m.name not in SKIP_NAMES and not m.name.startswith("._")]
    return files


def text_stats(path):
    if path.suffix != ".md":
        return {}
    text = path.read_text(encoding="utf-8")
    return {"characters": len(re.sub(r"\s", "", text))}


def build(workspace):
    today = datetime.date.today().isoformat()
    manifest = {
        "schema": 1,
        "generated": today,
        "source_workspace": str(workspace),
        "publication": "LOCAL ONLY. This directory is gitignored; review INVENTORY.md before publishing any of it.",
        "works": {},
        "excluded_from_archive": [{"pattern": p, "reason": r} for p, r in EXCLUDED],
    }
    for slug, meta in WORKS.items():
        manifest["works"][slug] = {**meta, **NOTES.get(slug, {}), "versions": [], "editions": []}

    for slug, vid, label, status, rel, patterns, langs in VERSIONS:
        base = workspace / rel
        dest_root = OUT / slug / "source" / vid
        entries = []
        for src in collect(base, patterns):
            rel_src = src.relative_to(base)
            dest = dest_root / rel_src
            dest.parent.mkdir(parents=True, exist_ok=True)
            digest = sha256(src)
            # Skip unchanged files: rewriting them is pointless and, in a
            # cloud-synced folder, can spawn "name 2.md" conflict copies.
            if not dest.exists() or sha256(dest) != digest:
                shutil.copy2(src, dest)
            if sha256(dest) != digest:
                raise SystemExit(f"Checksum mismatch after copy: {src}")
            entries.append({
                "path": str(dest.relative_to(OUT)),
                "source": str(src.relative_to(workspace)),
                "bytes": src.stat().st_size,
                "modified": datetime.datetime.fromtimestamp(src.stat().st_mtime).isoformat(timespec="seconds"),
                "sha256": digest,
                **text_stats(src),
            })
        chapters = {}
        for e in entries:
            folder = Path(e["path"]).parent.name
            if e["path"].endswith(".md") and folder in ("md", "zh_md", "en_md"):
                chapters[folder] = chapters.get(folder, 0) + 1
        manifest["works"][slug]["versions"].append({
            "id": vid,
            "label": label,
            "status": status,
            "languages": langs,
            "formats": sorted({Path(e["path"]).suffix.lstrip(".") for e in entries}),
            "chapter_files": chapters,
            "files": entries,
        })

    for slug, vid, folder, name in EDITIONS:
        chapter_dir = OUT / slug / "source" / vid / folder
        parts = sorted(chapter_dir.glob("*.md"))
        header = (
            f"<!-- Generated by tools/build_manuscript_archive.py on {today} by concatenating "
            f"{len(parts)} chapter files from source/{vid}/{folder}/ in file-name order. "
            "Text is unchanged; edit the chapter files, not this file. -->\n\n"
        )
        body = "\n\n".join(p.read_text(encoding="utf-8").lstrip("﻿").rstrip("\n") for p in parts)
        out = OUT / slug / name
        write_if_changed(out, header + body + "\n")
        manifest["works"][slug]["editions"].append({
            "path": str(out.relative_to(OUT)),
            "from": f"source/{vid}/{folder}/",
            "chapter_files": len(parts),
        })

    write_if_changed(OUT / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    return manifest


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    ws = Path(sys.argv[1]).expanduser()
    if not ws.is_dir():
        raise SystemExit(f"Workspace not found: {ws}")
    m = build(ws)
    total = sum(len(v["files"]) for w in m["works"].values() for v in w["versions"])
    print(f"Archived {total} files into {OUT}")
