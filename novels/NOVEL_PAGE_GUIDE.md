# 小说展示页面规则 / Novel Page Template Guide

本文件定义每一本小说在本站的标准页面结构与做法。新增一本小说时,**复制 `whale-fall`(巨鲸陨落)作为模板**,按本规则替换内容即可。`whale-fall` 与 `dark-moon` 是当前的参考实现。

---

## 1. 目录结构

每本小说放在 `novels/<slug>/` 下,结构固定如下:

```
novels/<slug>/
  index.html              展示首页(书名/简介/封面/章节目录/音乐播放器)
  assets/
    reader.js             交互逻辑(语言、主题、音乐播放器)——各本独立但同源
    style.css             样式——各本独立但同源
  zh_html/                中文章节,文件名:NN_中文标题.html
  en_html/                英文章节,文件名与 zh 同名(NN_中文标题.html)
  soundtrack/
    catalog.js            曲目目录(双语标题 + 时长 + src)
    track-name-map.md     音乐文件中英文件名对照(见第 6 节)
    audio/                音频文件(英文 ASCII 文件名)
```

- `<slug>` 用英文小写连字符,如 `whale-fall`、`dark-moon`、`mystic-cat`。
- 封面图放在仓库根 `assets/`,命名 `<XX>_cn.png` / `<XX>_en.png`(如 `WF_cn.png`、`DM_cn.png`)。

---

## 2. 双语机制(中/英切换)

整站为中英双语:**中文界面所有内容显示中文,英文界面所有内容显示英文**。

- `<body>` 上有 `data-lang="zh"`(默认)。顶部语言按钮切换时,`reader.js` 更新 `body[data-lang]` 并刷新所有文案。
- 首页所有需要翻译的文字加 `data-i18n="<key>"`,翻译写在 `reader.js` 顶部的 `copy.zh` / `copy.en` 对象里。
- 章节正文不用 i18n:中文正文在 `zh_html/`,英文正文在 `en_html/`,靠切换链接到对应语言的同名文件。
- `<html lang>` 也随之切换(`zh-CN` / `en`)。

新增小说时,务必把 `copy.zh` / `copy.en` 两套文案补全(书名、副标题、简介、按钮、目录标题、Soundtrack 标题、`playlist` 等)。

---

## 3. 封面切换(cover-stack)

首页 hero 右侧用两张叠放封面,**当前语言的封面在前**:

```html
<figure class="cover-stack" aria-label="<Book> covers">
  <img class="cover-zh" src="../../assets/web/XX_cn.jpg" alt="中文封面" />
  <img class="cover-en" src="../../assets/web/XX_en.jpg" alt="English cover" />
</figure>
```

网页一律引用 `assets/web/` 下的 1024px JPG(每张约 60–300 KB);`assets/XX_cn.png` 原图(每张 4–5 MB)只作母版保留。新增或替换封面后重新生成:

```bash
sips -s format jpeg -s formatOptions 82 -Z 1024 assets/XX_cn.png --out assets/web/XX_cn.jpg
```

层级由 CSS 按 `body[data-lang]` 控制(复制 whale-fall 的规则即可),无需 JS:

```css
body[data-lang="zh"] .cover-stack .cover-zh,
body[data-lang="en"] .cover-stack .cover-en { /* 前:top:0; right:74px; z-index:2; filter:none */ }
body[data-lang="zh"] .cover-stack .cover-en,
body[data-lang="en"] .cover-stack .cover-zh { /* 后:top:92px; right:0; z-index:1; 变暗 */ }
```

移动端(`max-width:760px`)需要重新排两张封面的位置与容器高度,避免后封面溢出压到下方文字,详见第 8 节。

---

## 4. 音乐播放器(位置 + 结构 + 行为)

### 位置
播放器放在 hero 左栏 **「开始阅读」按钮的正下方**(`.hero-copy` 内、`.hero-actions` 之后),进入页面即可见,无需下滚。**不要**放在章节目录下面。

### 结构(胶囊条 + 可折叠列表)
```html
<section class="soundtrack-panel" aria-labelledby="soundtrack-title">
  <div class="soundtrack-heading">
    <p class="eyebrow" data-i18n="soundtrackKicker">原声概念</p>
    <h2 id="soundtrack-title" data-i18n="soundtrackTitle"><书名> Soundtrack</h2>
  </div>
  <div class="soundtrack-player" data-soundtrack-player>
    <div class="sp-bar">
      <span class="sp-num" id="track-number">01</span>
      <div class="sp-name"><span id="track-title">…</span></div>
      <span class="sp-playwrap">
        <svg class="sp-ring" viewBox="0 0 44 44"><circle class="sp-ring-track" cx="22" cy="22" r="20"/><circle class="sp-ring-fill" id="track-ring" cx="22" cy="22" r="20"/></svg>
        <button id="track-play" class="sp-icon sp-play">▶ 图标</button>
      </span>
      <button id="track-toggle" class="sp-icon sp-listbtn">☰ 三条杠图标</button>
    </div>
    <ol class="sp-list" id="track-list"></ol>
    <audio id="soundtrack-audio" preload="metadata"></audio>
  </div>
</section>
```

### 外观要点
- 整条为**胶囊圆角**(`border-radius:999px`)。左:圆形序号 + 歌名(过长省略号)。右:播放键 + 列表键。
- **进度做成播放键外圈的圆环**(SVG ring,随播放填充,播完为整圈)。
- **播放键透明**(只留青色图标),让进度环更清楚。
- 列表键是**纯三条杠**图标;点击在下方展开/收起整张曲目列表(展开时高亮、超高可滚动),列表项也是圆角。

### 行为(`reader.js` 的 `setupSoundtrack`)
- 点播放键 = 播放/暂停;点列表项 = 播放该曲并高亮;一曲播完自动下一首(到末尾回到第一首)。
- 歌名、列表、`播放列表` 文案都随语言切换,**切语言不打断播放**(靠 `player.dataset.bound` 守卫:已绑定时只刷新文字)。
- 持久状态用 IIFE 作用域变量 `stIndex` / `stLang`。
- 每本小说用各自的全局曲目变量:`window.<camelCaseSlug>Soundtrack`(如 `whaleFallSoundtrack`、`darkMoonSoundtrack`)。移植时记得改这一处。

---

## 5. 阅读页(zh_html / en_html)

- 每个章节是独立 HTML:`<body><main>` → `<h1>标题</h1>` → 正文 `<p>` → 底部一个导航。
- **导航只保留底部一个**,不要在标题上方再放一个顶部导航。
- 导航文案必须跟随页面语言,不要中英混排:
  - 中文页只用 `上一章` / `目录` / `下一章`;
  - 英文页只用 `Previous` / `Index` / `Next`;
  - 禁止使用 `上一章 / Previous`、`目录 / Index`、`下一章 / Next` 这种混合写法。
- 中英文章节文件**同名**(都用 `NN_中文标题.html`),正文分别为中文 / 英文,方便语言切换时一一对应跳转。
- Markdown 强调要完整转换,页面上不能残留 `*`:原稿里 `***系统提示***` 这类整行粗斜体写成 `<p class="system-line"><strong>…</strong></p>`,行内的写成 `<em><strong>…</strong></em>`。

### 5.1 版权信息页(第一页)

- 每本书的**第一页(`00_…` 文件)固定为「版权信息」页**:`<h1>` 与 `<title>` 中文为「版权信息」、英文为「Copyright」。原来的"书名页/写作说明"等工程内容不对外展示,直接被版权信息替换。
- 内容模板(中文,书名按本书替换):

  ```
  书名：<本书中文名>     作者：李富龙
  出版：<仅填写已核实的出版信息，例如「独立出版」；未出版的书写「版本：网络阅读稿（尚未正式出版）」>
  出版年份：<仅已出版的书填写，以实际上架日期为准>
  © <首次发表年份> 李富龙     版权所有，侵权必究。
  未经作者书面许可，不得以任何形式复制、转载或传播本书内容。
  ```
  英文页同义翻译,书名用英文名、作者写 Fulong Li(出版写 `Publisher: Independently published` 或 `Edition: online reading draft (not yet formally published)`)。
- **不要填写占位或推测的书目信息**:没有正式分配的 ISBN 就整行不写(不要写 `978-1-xxxxxx-xx`);出版社、出版日期只写能核实的内容。
- 已核实信息(2026-10-20):《月球暗面》英文电子版在 Apple Books 上架,标注 Independently published,发行日期 2025-12-31,页面未显示 ISBN。《巨鲸陨落》尚未正式出版。
- **不要**保留「灵接科技 / 书名 / 作者 著」这类标题页抬头三行,只留版权信息正文。

### 5.2 章节编号规则

- 版权信息页、**作者序、前言**等前置内容**不加序号**(目录里序号栏留空,章节页 `<h1>`/`<title>` 不带数字)。
- **正文从 01 开始连续编号**。目录 `<span>` 与章节页 `<h1>`/`<title>` 的显示序号要一致。
- 注意:显示序号与 `NN_…` 文件名可以不一致(文件名保持历史编号即可,不必重命名);以**显示序号**为准。

### 5.3 共用「作者序」

- **每本小说都放同一篇《作者序》**(关于《灵接科技》系列、梦境与意识的开篇自述,署名「——李富龙 / — Fulong Li」)。这是**全系列共用的固定内容**,中英双语都要一致,新书直接复用,不要逐本另写。
- 位置:排在「版权信息」之后、正文第一章之前;**不加序号**。
- 文件:中文 `zh_html/作者序.html`、英文 `en_html/作者序.html`(文件名一致以支持语言切换);导航 上一章=版权信息页、下一章=正文第一章。
- 「前言」则可以是**各书专属**(如月球暗面的「前言：吉姆的自述」),不强制共用。
- 参考实现:`whale-fall` 与 `dark-moon` 的 `作者序`,内容完全相同,可直接拷贝。

---

## 6. 音乐文件命名与对照

- 音频文件名统一用**英文 ASCII**(避免中文文件名在服务器/URL 上的编码问题)。
- 中英显示名由 `catalog.js` 的 `title.zh` / `title.en` 控制,**不靠文件名**。
- 每本 `soundtrack/track-name-map.md` 维护:文件名 ↔ English title ↔ 中文名称 ↔ 章节 ↔ 时长。

### catalog.js 条目格式
```js
window.<camelCaseSlug>Soundtrack = [
  {
    id: "shadows-above-the-ruins",
    number: "01",
    title: { zh: "废墟之上的阴影", en: "Shadows Above the Ruins" },
    mood:  { zh: "…", en: "…" },          // 现在 UI 不显示,可留作备注
    duration: "3:29",
    chapter: "01",
    src: "audio/shadows-above-the-ruins.mp3",  // 留空 "" 表示概念曲、暂不可播
    file: "audio/shadows-above-the-ruins.mp3"
  },
  // …
];
```

---

## 7. 新增一本小说的步骤

1. 复制 `novels/whale-fall/` 为 `novels/<slug>/`。
2. 改 `index.html`:书名、副标题、简介、章节目录、Soundtrack 标题、封面图路径(`../../assets/web/XX_cn/en.jpg`)、aria-label。
3. 改 `assets/reader.js`:`copy.zh` / `copy.en` 全部文案;`storagePrefix`;`setupSoundtrack` 里的全局变量名 `window.<camelCaseSlug>Soundtrack`。
4. 放入 `zh_html/` 与 `en_html/` 同名章节文件(底部单导航)。
5. 写 `soundtrack/catalog.js` 与 `soundtrack/track-name-map.md`,音频放 `audio/`(英文文件名)。
6. 准备封面 `assets/<XX>_cn.png` / `<XX>_en.png`,并按第 3 节生成 `assets/web/` 下的 JPG。
7. 在根目录 `app.js` 的 `books` 数组里登记这本书。**数组顺序就是档案编号**(档案 I、II…、镜头经过灵接舱的顺序、书卷总览顺序都由它决定),不要再用额外代码调整顺序;`tagline` 只写「档案 N ·」后面的部分。
8. 正文来源:章节 HTML 由原稿 Markdown 生成,原稿与网页的对应关系、更新流程见 `docs/MANUSCRIPT_WORKFLOW.md`。
9. 自检:`node --check assets/reader.js`;首页中英切换、封面切换、音乐播放/列表展开均正常;章节页仅底部导航;运行 README 中的链接检查。

> 说明:四本占位小说(mystic-cat、crimson-cruise、spacetime-labyrinth、where-souls-return)目前仍是「创作中」单页,正式制作时按本规则套用即可;它们的中英封面图已在 `assets/` 备好。

---

## 8. 移动端(响应式,`@media (max-width: 760px)`)

新书复制模板即可继承这些规则,无需重写。

### 8.1 章节底部导航

- **保持一行三个**:上一章/Previous(左) · 目录/Index(中) · 下一章/Next(右),沿用桌面的 `grid-template-columns: 1fr auto 1fr`。**不要**在手机端压成单列(会出现按钮错位的"阶梯"状)。
- 文案仍按页面语言单语显示:中文页显示 `上一章` / `目录` / `下一章`;英文页显示 `Previous` / `Index` / `Next`。
- 手机端只收紧间距与字号即可:

  ```css
  .chapter-nav, .nav { gap: 8px; margin-top: 40px; padding-top: 18px; }
  .chapter-nav a, .nav a { padding: 0 14px; font-size: 12px; }
  ```

### 8.2 封面叠放(cover-stack)

- 封面图比例约 **高:宽 = 1.6**。两张图绝对定位叠放,手机端容器高度必须能容下"靠后那张"的偏移,否则它会溢出压到下方文字。
- 用一个随宽度缩放的变量统一控制,避免固定 `min-height` 在不同屏宽下溢出或留大空隙:

  ```css
  .cover-stack {
    --cw: min(210px, 52vw);          /* 封面宽度 */
    min-height: calc(var(--cw) * 1.94);  /* 容纳后封面:0.34 偏移 + 1.6 高度 */
    margin-bottom: 6px;
    order: -1;                       /* 手机端封面排到文字上方 */
  }
  .cover-stack img { width: var(--cw); }
  /* 前(当前语言):top:0; left:6% */
  /* 后(另一语言):top: calc(var(--cw) * 0.34); right:6% */
  ```
- 前/后由 `body[data-lang]` 决定(见第 3 节),手机端只改 `top` / `left` / `right` 偏移,层级与变暗规则不变。
