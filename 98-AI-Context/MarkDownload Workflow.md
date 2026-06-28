# MarkDownload Workflow

```mermaid
flowchart LR
  A[浏览器 MarkDownload] --> B[00-Inbox/Downloaded]
  B --> C[research_cleaner.py]
  C --> D[00-Inbox/Cleaned]
  D --> E[人工确认主分类]
  E --> F[04-Research]
```

## MarkDownload 设置

- 下载目录：Vault 的 `00-Inbox/Downloaded`。
- 文件名：优先 `{date:YYYY-MM-DD} {pageTitle}`。
- Frontmatter 至少保留 `title`、`source`、`author`、`published`、`captured`。
- 不启用会改写正文或自动摘要的选项。

## 清洗

在 Vault 根目录运行：

```bash
python3 98-AI-Context/Tools/research_cleaner.py
```

原始文件留在 `Downloaded`；清洗稿进入 `Cleaned`，便于核对后归档。

