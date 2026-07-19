# 月球暗面 / Darkside of the Moon — 音乐文件名中英对照
# Soundtrack Track Name Map (English ↔ 中文)

文件名统一用英文 ASCII(避免空格/中文名在网页/服务器上的编码问题),
中英文显示名由 `catalog.js` 的 `title.en` / `title.zh` 控制:英文页面显示英文名,中文页面显示中文名。

Filenames are kept in English ASCII (no spaces). Bilingual display names are driven by
`title.en` / `title.zh` in `catalog.js`.

| # | 文件名 (filename) | English title | 中文名称 | 章节 Chapter | 时长 Duration |
|---|-------------------|---------------|----------|--------------|---------------|
| 01 | `audio/city-that-ages-with-my-steps.mp3` | The City That Ages With My Steps | 随我脚步老去的城市 | 07 新世纪与双生 / The New Century and the Dual-Born | 2:43 |
| 02 | `audio/moon-kingdom.mp3` | Moon Kingdom | 月之国 | 21 罗斯威尔遗产 / The Roswell Inheritance | 3:00 |
| 03 | `audio/terasha-record.mp3` | Terasha Record | 泰拉撒记录 | 32 泰拉撒第一层门 / The First Gate of Terasha | 3:13 |
| 04 | `audio/moon-landing.mp3` | Moon Landing | 登月 | 33 下一本入口 / The Door to the Next Book | 4:15 |

## 重命名记录 / Rename log
- `Terasha record.mp3` → `terasha-record.mp3`(去空格 / remove spaces）
- `The City That Ages With My Steps.mp3` → `city-that-ages-with-my-steps.mp3`
- `The Gate Before Dawn.mp3` → `gate-before-dawn.mp3` → `moon-landing.mp3`(改名为「登月」/ renamed to "Moon Landing"）
- `echoes-of-a-fallen-empire.mp3` → `moon-kingdom.mp3`(改名为「月之国」/ renamed to "Moon Kingdom"）

## 新增音乐的步骤 / How to add a new track
1. 把音频放进 `audio/`,文件名用英文 ASCII(如 `my-new-track.mp3`)。
2. 在本表加一行:文件名 / English title / 中文名称 / 章节 / 时长。
3. 在 `catalog.js` 新增条目,`title` 填 `{ zh, en }` 双语,`src` 指向该文件。
