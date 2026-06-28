# Git Sync

## 策略

- Obsidian 启动时自动 Pull。
- 每 15 分钟自动 Pull。
- 停止编辑后按 15 分钟周期 Commit and Sync。
- Push 前先 Pull，使用 merge 模式。
- 工作区布局等设备本地状态不提交。

## 人工验证

在 Obsidian 命令面板运行 `Git: Commit-and-sync`，确认右上角无错误通知。

