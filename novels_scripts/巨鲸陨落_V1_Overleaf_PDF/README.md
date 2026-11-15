# 中文小说 Overleaf 模板

## Overleaf 使用方法

1. 将整个 ZIP 上传到 Overleaf。
2. 打开 **Menu → Compiler**，选择 **XeLaTeX**。
3. 修改 `novel-config.tex` 中的书名、作者等信息。
4. 在 `chapters/` 中按顺序添加章节文件，例如：
   - `03-second-chapter.tex`
   - `04-third-chapter.tex`
5. 在 `chapters/chapters-list.tex` 中加入对应的 `\input{...}`。
6. 若需要图片封面，将图片命名为 `cover.jpg`，放入 `assets/`。

## 章节写法

```tex
\chapter{章节标题}

第一段正文。

第二段正文。

\SceneBreak

场景切换后的正文。
```

序章、楔子、番外等不参与自动编号时：

```tex
\chapter*{序章}
\addcontentsline{toc}{chapter}{序章}
```

## 简单自动化

Overleaf 本身通常不会自动运行 Python 脚本。本模板提供 `tools/build_chapters.py`，适合在本地或 GitHub 工作流中使用。运行后，它会扫描所有数字开头的章节文件，并自动更新 `chapters/chapters-list.tex`。

```bash
python tools/build_chapters.py
```

若只在 Overleaf 编辑，直接维护 `chapters/chapters-list.tex` 即可。

## 推荐命名规则

使用两位或三位数字作为章节前缀：

```text
01-prologue.tex
02-awakening.tex
03-departure.tex
```

这样章节会始终按正确顺序排列。
