# 巨鲸陨落 / Whale Fall — 音乐文件名中英对照
# Soundtrack Track Name Map (English ↔ 中文)

这是音乐文件的"中间对照文档"。文件名统一用英文 ASCII(避免中文文件名在网页/服务器上的编码问题),
中英文显示名称由 `catalog.js` 的 `title.en` / `title.zh` 控制:英文页面显示英文名,中文页面显示中文名。

This is the intermediate map for soundtrack files. Filenames are kept in English ASCII (to avoid
encoding issues with Chinese filenames on the web/server). The bilingual display names are driven by
`title.en` / `title.zh` in `catalog.js` — the English page shows English, the Chinese page shows Chinese.

| # | 文件名 (filename) | English title | 中文名称 | 章节 Chapter | 时长 Duration |
|---|-------------------|---------------|----------|--------------|---------------|
| 01 | `audio/lost-ancient-empire.mp3` | Solar Empire | 太阳帝国 | 30 法厄同开始下沉 / Phaeton Begins to Sink | 3:00 |
| 02 | `audio/shadows-above-the-ruins.mp3` | Shadows Above the Ruins | 废墟之上的阴影 | 01 尸山之上 / On the Mountain of Dead | 3:29 |
| 03 | `audio/phaethon-in-memory.mp3` | Phaethon in Memory | 记忆中的法厄同 | 05 法厄同的天空裂开 / Phaethon's Sky Cracks | 2:55 |
| 04 | `audio/requiem-grieving-sky.mp3` | Requiem for the Grieving Sky | 回溯恸天 | 08 五族残骸 / The Remains of Five Peoples | 2:54 |
| 05 | `audio/phaethon-hymn.mp3` | Hymn of Phaethon | 法厄同圣歌 | 09 日辉族的律令 / The Decrees of the Sunbright | 2:46 |
| 06 | `audio/phaethon-holy-war.mp3` | The Holy War of Phaethon | 法厄同圣战 | 16 第五行星 / The Fifth Planet | 3:40 |
| 07 | `audio/last-sunbright-heir.mp3` | The Last Sunbright Heir | 最后的太阳裔 | 18 日辉族想要人类跪拜 / The Sunbright Wanted Kneeling Humans | 3:13 |
| 08 | `audio/moment-of-rising.mp3` | The Moment of Rising | 起身之刻 | 47 醒来之前 / Before Waking | 2:45 |
| 09 | `audio/ancient-lament-of-return.mp3` | Ancient Lament of Return | 古老的归来挽歌 | 48 蓝鲸在地球歌唱 / Blue Whales Sing on Earth | 1:52 |

## 重命名记录 / Rename log
- `记忆中的法厄同.mp3` → `phaethon-in-memory.mp3`(中文文件名 → 英文 ASCII / Chinese filename → English ASCII)
- `回溯恸天（instrumental-requiem）.mp3` → `requiem-grieving-sky.mp3`
- `法厄同圣歌.mp3` → `phaethon-hymn.mp3`
- `法厄同圣战.mp3` → `phaethon-holy-war.mp3`
- `起身之刻.mp3` → `moment-of-rising.mp3`
- `失落的远古帝国.mp3` → `lost-ancient-empire.mp3`（显示名改为「太阳帝国」/ now displayed as "Solar Empire"）
- `最后的太阳裔.mp3` → `last-sunbright-heir.mp3`

## 新增音乐的步骤 / How to add a new track
1. 把音频放进 `audio/`,文件名用英文 ASCII(如 `my-new-track.mp3`)。
   Drop the audio into `audio/` with an English ASCII filename.
2. 在本表加一行:文件名 / English title / 中文名称 / 章节 / 时长。
   Add a row here: filename / English title / 中文名称 / chapter / duration.
3. 在 `catalog.js` 新增一个条目,`title` 填 `{ zh, en }` 双语,`src` 指向该文件。
   Add an entry in `catalog.js` with bilingual `title { zh, en }` and `src` pointing to the file.
