---
type: guide
status: active
tags:
  - system/inbox
---
# Research Import Guide

## 入口

- 网页：使用 Obsidian Web Clipper 的 `Research Capture` 模板。
- MarkDownload：保存到 `00-Inbox/Downloaded`，保留原始 Markdown。
- PDF、图片及附件：放入 `00-Inbox/Attachments`，在对应笔记中链接。
- 其他文本：先保存为 UTF-8 Markdown，再进入 `Downloaded`。

## 文件要求

- 一篇资料一个文件。
- 优先保留原始标题、作者、来源 URL 和发布时间。
- 不在 `Downloaded` 中直接改写原文。
- 文件名可暂时粗糙，Research Cleaner 会生成安全文件名。

## 下一步

进入 [[Research Triage Guide]]，或运行 `python3 98-AI-Context/Tools/research_cleaner.py`。

