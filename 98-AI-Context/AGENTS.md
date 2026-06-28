# AGENTS

## Agent 行为规范

- 默认先执行安全、可逆、任务范围内的操作。
- 修改前检查已有文件，保留用户内容和未提交改动。
- 新研究笔记必须有唯一 `primary_domain`，可有多个 `topic/...` 标签。
- 来源型内容必须保留标题、来源、作者、时间、URL 与完整原文。
- 不把聊天记录存入 Memory。
- 任何自动分类低置信度内容留在 `00-Inbox/Cleaned`，标记 `status/needs-review`。
- 文件命名使用可读标题，避免控制字符、URL 参数和重复日期。
- 新项目必须包含 `Project-Status.md` 并维护下一步、风险与决策。

## 系统工具

- 清洗：`python3 98-AI-Context/Tools/research_cleaner.py`
- 巡检：`python3 98-AI-Context/Tools/kb_audit.py`
- 工作流说明：[[MarkDownload Workflow]]、[[Web Clipper Setup]]

