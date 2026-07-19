---
description: "Use when renaming, creating, or reviewing Markdown post filenames in this repo; generate short slugs from content, not literal title translations"
---

# Markdown 命名规则

## 适用范围

当任务涉及 `_posts/*.md`、`_posts/*/` 形式的文件或目录重命名时，优先读取并遵守本指令。

## 核心目标

- 文件名要短。
- 文件名要能概括内容，但不必直译标题。
- 优先使用英文或拼音短 slug，必要时允许混合，但不要做完整句翻译。
- 保留现有日期前缀，例如 `2026-07-20-xxx.md`。
- 目录型文章仅修改目录名，保持目录内的 `doc.md` 不变。

## 命名流程

1. 先读取 YAML front matter，再看正文首段、`<!--more-->` 前后的内容、标题、标签和分类。
2. 从内容中提炼 1 到 2 个最核心的概念，不优先照搬标题措辞。
3. 将概念压缩为短 slug，优先 2 到 4 个词以内，避免冗长短语。
4. 避免过于抽象的词、重复信息和无意义连接词。
5. 如果内容主题明确但标题很花哨，仍以内容主题为准。
6. 如果主题存在歧义，先给出最稳妥的候选名，再请求确认，不要擅自扩写。

## 具体规则

- 不要把中文标题整句翻译成英文文件名。
- 不要为了“完整”牺牲简短性。
- 不要在文件名里加入多余的副标题、情绪词或装饰性标点。
- 仅在原文件或目录名含有 `new-post` 时无需要确认直接执行。

