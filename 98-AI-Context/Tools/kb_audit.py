#!/usr/bin/env python3
"""Audit the vault and write a human-readable Markdown report."""

from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
REPORT = VAULT / "98-AI-Context" / "Knowledge Base Audit Report.md"
IGNORE_PARTS = {".git", ".trash", "node_modules", "_Originals"}
GARBAGE_NAMES = {".DS_Store", "Thumbs.db", "desktop.ini"}
BAD_NAME = re.compile(r"[\\:*?\"<>|]|\s{2,}|^\.|\.$")
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
TAG = re.compile(r"(?<![\w/])#([\w\-/\u4e00-\u9fff]+)")


def wanted(path: Path) -> bool:
    return not any(part in IGNORE_PARTS for part in path.relative_to(VAULT).parts)


def normalized_hash(text: str) -> str:
    text = re.sub(r"(?s)\A---.*?---\s*", "", text)
    text = re.sub(r"\s+", " ", text).strip().casefold()
    return hashlib.sha256(text.encode()).hexdigest()


def yaml_value(text: str, key: str) -> str:
    match = re.search(rf"(?mi)^\s*{re.escape(key)}\s*:\s*[\"']?(.*?)[\"']?\s*$", text)
    return match.group(1).strip() if match else ""


def main() -> int:
    files = sorted(path for path in VAULT.rglob("*") if path.is_file() and wanted(path))
    notes = [path for path in files if path.suffix.lower() == ".md" and path != REPORT]
    note_by_stem = defaultdict(list)
    note_by_rel = {}
    file_by_rel = {}
    contents = {}
    for note in notes:
        rel = note.relative_to(VAULT).with_suffix("").as_posix()
        note_by_rel[rel] = note
        note_by_stem[note.stem].append(note)
        contents[note] = note.read_text(encoding="utf-8", errors="replace")
    for file in files:
        file_by_rel[file.relative_to(VAULT).as_posix()] = file

    hashes = defaultdict(list)
    for note, text in contents.items():
        if len(text.strip()) > 80:
            hashes[normalized_hash(text)].append(note)
    duplicates = [group for group in hashes.values() if len(group) > 1]

    bad_names = [path for path in files if not path.name.startswith(".") and BAD_NAME.search(path.name)]
    garbage = [path for path in files if path.name in GARBAGE_NAMES or path.suffix.lower() in {".tmp", ".bak", ".swp"}]
    empty_dirs = [path for path in VAULT.rglob("*") if path.is_dir() and wanted(path) and not any(path.iterdir())]

    incoming = Counter()
    broken = []
    outgoing = Counter()
    for note, text in contents.items():
        for raw_target in WIKILINK.findall(text):
            target = raw_target.strip().replace("\\", "/")
            outgoing[note] += 1
            candidates = []
            try:
                relative_target = (note.parent / target).resolve().relative_to(VAULT).as_posix()
            except ValueError:
                relative_target = ""
            if relative_target in note_by_rel:
                candidates = [note_by_rel[relative_target]]
            elif target in note_by_rel:
                candidates = [note_by_rel[target]]
            elif relative_target in file_by_rel or target in file_by_rel:
                candidates = [file_by_rel.get(relative_target, file_by_rel.get(target))]
            elif f"{relative_target}.md" in file_by_rel or f"{target}.md" in file_by_rel:
                candidates = [file_by_rel.get(f"{relative_target}.md", file_by_rel.get(f"{target}.md"))]
            else:
                candidates = note_by_stem.get(Path(target).name, [])
            if candidates:
                for candidate in candidates:
                    incoming[candidate] += 1
            else:
                broken.append((note, target))

    exempt_orphans = {"README", "欢迎", "Topic Hub Template"}
    orphans = [
        note for note in notes
        if incoming[note] == 0
        and outgoing[note] == 0
        and note.stem not in exempt_orphans
        and "00-Inbox/Downloaded" not in note.relative_to(VAULT).as_posix()
    ]

    conflicts = []
    for note, text in contents.items():
        if "04-Research" not in note.parts or "Topic Hubs" in note.parts:
            continue
        primary = yaml_value(text, "primary_domain")
        if primary and primary not in note.relative_to(VAULT).as_posix():
            conflicts.append((note, primary))

    tag_counts = Counter()
    word_groups = {
        "高频工具": ["Codex", "Claude Code", "Obsidian", "GitHub", "MCP", "n8n", "MarkDownload"],
        "高频工作流": ["Workflow", "自动化", "Research Cleaner", "内容创作", "知识管理"],
        "高频商业模式": ["商业模式", "供应链金融", "变现", "订阅", "平台"],
        "高频平台": ["公众号", "小红书", "播客", "课程", "GitHub", "Obsidian"],
    }
    research_text = "\n".join(text for note, text in contents.items() if "04-Research" in note.parts)
    for text in contents.values():
        tag_counts.update(TAG.findall(text))
        yaml_tags = re.findall(r"(?m)^\s*-\s+((?:topic|domain|status|hub)/[^\s]+)\s*$", text)
        tag_counts.update(yaml_tags)
        tag_counts.update(re.findall(r"\b((?:topic|domain|status|hub)/[a-z0-9-]+)\b", text, re.I))

    lines = [
        "---", "type: audit-report", f'generated: "{datetime.now().isoformat(timespec="seconds")}"', "tags: [system/audit]", "---",
        "# Knowledge Base Audit Report", "",
        "## 摘要", "",
        f"- 文件：{len(files)}", f"- Markdown 笔记：{len(notes)}", f"- 重复内容组：{len(duplicates)}",
        f"- 分类冲突：{len(conflicts)}", f"- 异常文件名：{len(bad_names)}", f"- 空目录：{len(empty_dirs)}",
        f"- 垃圾文件：{len(garbage)}", f"- 孤立笔记：{len(orphans)}", f"- 断裂链接：{len(broken)}", "",
        "## 重复内容", "",
    ]
    lines += [f"- " + " ↔ ".join(f"`{p.relative_to(VAULT)}`" for p in group) for group in duplicates] or ["- 无"]
    lines += ["", "## 分类冲突", ""]
    lines += [f"- `{p.relative_to(VAULT)}` 声明 `{primary}`" for p, primary in conflicts] or ["- 无"]
    lines += ["", "## 异常文件名", ""]
    lines += [f"- `{p.relative_to(VAULT)}`" for p in bad_names] or ["- 无"]
    lines += ["", "## 空目录", ""]
    lines += [f"- `{p.relative_to(VAULT)}`" for p in empty_dirs] or ["- 无"]
    lines += ["", "## 垃圾文件", ""]
    lines += [f"- `{p.relative_to(VAULT)}`" for p in garbage] or ["- 无"]
    lines += ["", "## 孤立笔记", ""]
    lines += [f"- `{p.relative_to(VAULT)}`" for p in orphans] or ["- 无"]
    lines += ["", "## 断裂链接", ""]
    lines += [f"- `{p.relative_to(VAULT)}` → `[[{target}]]`" for p, target in broken] or ["- 无"]
    lines += ["", "## 高频主题标签", ""]
    lines += [f"- `{tag}`：{count}" for tag, count in tag_counts.most_common(20)] or ["- 暂无"]
    lines += ["", "## Research 内容扫描", ""]
    for label, terms in word_groups.items():
        counts = sorted(((research_text.casefold().count(term.casefold()), term) for term in terms), reverse=True)
        visible = [f"{term}（{count}）" for count, term in counts if count]
        lines.append(f"- {label}：{'、'.join(visible) if visible else '尚无足够内容'}")
    lines += ["", "## 建议", "", "- 优先修复断裂链接和分类冲突。", "- 孤立的来源型笔记应至少连接一个 Topic Hub。", "- 空研究目录会在加入真实资料后自然消失；Git 使用 `.gitkeep` 保留必要结构。", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(REPORT.relative_to(VAULT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
