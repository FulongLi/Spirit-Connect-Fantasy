# Spirit Connect Fantasy Archives

**Spirit Connect Fantasy / 灵接幻想** 是李富龙的长篇科幻小说系列。本仓库是它的线上档案馆：
一个可滚动的 Three.js 3D 档案大厅，六座灵接舱各对应一卷书，并接入中英双语阅读页、
原声音乐、故事线与人物关系图。

- Website: <https://fulongli.github.io/Spirit-Connect-Fantasy/>
- Story Lines view: <https://fulongli.github.io/Spirit-Connect-Fantasy/#storylines>
- Relation Graph view: <https://fulongli.github.io/Spirit-Connect-Fantasy/#relations>

## 原稿与阅读页 / Manuscripts vs. reading pages

| | 原稿 Manuscripts | 阅读页 Reading pages |
|---|---|---|
| 内容 | 作者的 Markdown / Word / Pages 原稿、修订稿、设定文档 | 从原稿生成并按规范整理的章节 HTML |
| 位置 | `Novels` 工作区；本地归档在 `original-novel-texts/`（**gitignored，不公开**） | `novels/<slug>/zh_html/`、`en_html/` |
| 修改方式 | 作者在工作区编辑 | 由原稿重新生成，不在 HTML 里改写正文 |

完整流程见 [`docs/MANUSCRIPT_WORKFLOW.md`](docs/MANUSCRIPT_WORKFLOW.md)。

## 仓库结构 / Repository layout

```
index.html, styles.css, app.js     档案大厅：场景、镜头、书卷数据、故事线、关系图
src/scene/SpiritConnectionPod.js   灵接舱 3D 模型（程序化几何）
assets/                            封面母版 PNG、logo
assets/web/                        网页用封面 JPG（1024px）
novels/<slug>/                     每本书：index.html、assets/、zh_html/、en_html/、soundtrack/
novels/NOVEL_PAGE_GUIDE.md         阅读页制作规范
docs/MANUSCRIPT_WORKFLOW.md        原稿 → 阅读页流程
tools/check_site.py                链接 / 章节导航 / 占位信息检查
tools/build_manuscript_archive.py  生成本地原稿归档 original-novel-texts/
original-novel-texts/              本地原稿归档（gitignored）
```

## 灵接舱 3D 模型 / The Spirit Connection Pod

`src/scene/SpiritConnectionPod.js` 按《月球暗面》V2 原稿对第六代灵接舱的描写建模（括号内为 `zh_md` 文件名）：

- 光滑白色复合材料、“没有多余线条”的**蛋形舱体**（08_第二次数字矫正），银白色外壳（25_再见小女孩、27_三天失败）；
- 人平躺其中的**人体工学躺椅**，压力均匀分散，蛋形舱盖合拢（09_数字吉姆的空房间）；
- **半透明舱盖**，缓缓开合（03_黑水与苏醒、06_蓝黑球体与时间井）——以头端为铰链，镜头停在某一卷时对应舱盖打开；
- 舱内柔和而冰冷的光、边沿有节律闪烁的**状态指示灯**（03_黑水与苏醒），
  外壳上像呼吸一样流动的**接口光纹**（18_童年的另一个世界、20_月暗副本）；
- 舱侧的**监测立柱**显示实时波形（06_蓝黑球体与时间井，卢博士的控制台与状态曲线）；
- 新一代不再注入黑水（08_第二次数字矫正），所以模型没有液体管路。

所有几何体只生成一次、六座舱共享；外壳、躺椅、底座等为 PBR 材质，所有发光部分合并为一个着色器、
每舱一次绘制。主题切换走 `podKit.setTheme()`，动画走 `podKit.update()`。

## 场景性能 / Performance

- 设备分级（high / medium / low）：像素比上限、阴影、抗锯齿、粒子数量随档位调整；
- 自适应分辨率：帧时间持续偏高时降低像素比，恢复后再升回；
- 页面隐藏时暂停渲染；档案总览遮住场景且镜头静止时跳过渲染；
- 支持 `prefers-reduced-motion`：关闭视差与环境动画；
- 无 WebGL 时退化为 2D 页面，书卷面板、总览、故事线、关系图照常可用；
- 封面贴图上传前缩到 1024px，切换语言时释放另一语言的封面贴图。

## 新增或更新一本书 / Adding or updating a novel

1. 书卷数据在 `app.js` 的 `books` 数组：标题、`tagline`、状态、简介、封面、链接。
   **数组顺序就是档案编号**（档案 I…VI、镜头经过的灵接舱、总览顺序），不要另写排序逻辑。
2. 阅读页按 [`novels/NOVEL_PAGE_GUIDE.md`](novels/NOVEL_PAGE_GUIDE.md) 制作，正文来自原稿。
3. 故事线在 `storyBooks`（用 `bookId` 关联书卷），关系图在 `graphNodes` / `graphLinks`。
4. 版权页只写已核实的书目信息；没有 ISBN 就不写 ISBN。

## 双语内容 / Bilingual content

- 首页界面文案在 `app.js` 的 `uiText.zh` / `uiText.en`；书卷与故事线数据每个字段都有 `zh` / `en`。
- 阅读页首页文案在各书 `assets/reader.js` 的 `copy.zh` / `copy.en`。
- 章节正文不做 i18n：中英章节**同名**放在 `zh_html/` 与 `en_html/`，切换语言即跳到同名文件。
- 语言、主题选择保存在 `localStorage`；`?lang=en` 可直接指定语言。

## 本地预览与检查 / Preview and validate locally

页面使用 ES modules 和 import map，需要通过 HTTP 访问：

```bash
python3 -m http.server 8790
```

然后打开 <http://127.0.0.1:8790/>。

```bash
python3 tools/check_site.py
```

检查所有本地链接、中英章节配对、上一章/下一章顺序、音频文件、占位 ISBN 与未转换的 Markdown 强调。

```bash
node --check app.js
```

调试参数：

- `?debug=1` 暴露 `window.spiritConnectDebug`（`jump(0.135)` 跳到第一座舱、`step()`、`look()`、`info()`）
- `?quality=low|medium|high` 强制设备档位
- `?nowebgl` 模拟无 WebGL 设备
- `#archive-grid` / `#storylines` / `#relations` 直接打开对应总览视图
