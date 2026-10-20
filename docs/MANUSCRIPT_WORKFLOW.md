# From original manuscript to reading page

How a chapter gets from the author's manuscript onto the website, and how later
changes should travel. Short version: **the manuscript is the source; the HTML is
generated output; the two never share a folder.**

## The three layers

| Layer | Where | Who edits it | Public? |
|---|---|---|---|
| Working manuscripts | `Novels` workspace (`/Volumes/Fulong SSD/1Mac/novels`), e.g. `月球暗面_V2/zh_md/`, `巨鲸陨落_V1/en_md/` | The author | No |
| Archived originals | `original-novel-texts/` in this repo (gitignored), rebuilt by `tools/build_manuscript_archive.py` | Nobody by hand: it is a verified copy plus `manifest.json` | No, until reviewed |
| Reading pages | `novels/<slug>/zh_html/`, `en_html/` | Generated from the manuscript, then cleaned per `novels/NOVEL_PAGE_GUIDE.md` | Yes |

Current mapping:

| Website book | Manuscript source (canonical reading edition) |
|---|---|
| `novels/dark-moon/` | `月球暗面_V2/zh_md/` + `en_md/` (Chinese master text: `月球暗面_V2/md/`) |
| `novels/whale-fall/` | `巨鲸陨落_V1/zh_md/` + `en_md/` |
| other four books | No published text yet; `novels/<slug>/index.html` is a "coming soon" page |

## Updating a published chapter

1. Edit the chapter in the Novels workspace (`zh_md/NN_标题.md`, and the matching
   `en_md/` file if the English changes too). Keep the file name; it links the two
   languages and the HTML page.
2. Regenerate that chapter's HTML with the workspace's build script, or write it by
   hand following `NOVEL_PAGE_GUIDE.md` §5: one `<h1>`, `<p>` paragraphs, one bottom
   nav, `../assets/reader.js`, no `*` left from Markdown emphasis.
3. Copy the page into `novels/<slug>/zh_html/` (or `en_html/`). **Do not overwrite a
   website page just because the manuscript differs:** some pages carry later fixes
   that were never back-ported (see `original-novel-texts/INVENTORY.md` §3). Diff
   first and back-port into the manuscript when the website wording is the one to keep.
4. If the chapter list changed, update `novels/<slug>/index.html` (catalog and
   display numbers) and the neighbouring pages' prev/next links.
5. Rebuild the local archive so `manifest.json` records the new checksums:
   `python3 tools/build_manuscript_archive.py "/Volumes/Fulong SSD/1Mac/novels"`.
6. Run `python3 tools/check_site.py` and preview locally (see README).

## Publishing a new book

1. Finish the chapters in the workspace (both languages, same file names).
2. Create `novels/<slug>/` from the whale-fall template and import the HTML
   (`NOVEL_PAGE_GUIDE.md` §7).
3. Update the book's entry in `app.js` (status, description, link). The array order
   is the archive numbering; don't reorder in code.
4. Copyright page: only verified bibliographic data. No placeholder ISBN.

## Publishing the original manuscripts themselves

Not done automatically. `original-novel-texts/` is in `.gitignore`. To publish part
of it, review `original-novel-texts/INVENTORY.md` §4, then copy the approved files
to a tracked location (or narrow the ignore rule) in a separate, deliberate commit.
Unpublished drafts, the series bible and planning notes should stay private.
