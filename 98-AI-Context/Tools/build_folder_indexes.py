#!/usr/bin/env python3
"""Create lightweight category index notes from the actual Research directory tree."""

from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
RESEARCH = VAULT / "04-Research"


def main() -> int:
    count = 0
    for domain in sorted(RESEARCH.iterdir()):
        if not domain.is_dir() or domain.name == "Topic Hubs":
            continue
        domain_indexes = list(domain.glob("* Index.md"))
        domain_index = domain_indexes[0].stem if domain_indexes else "../Research Index"
        for category in sorted(path for path in domain.iterdir() if path.is_dir()):
            index = category / "_Index.md"
            if index.exists():
                continue
            text = (
                "---\n"
                "type: category-index\n"
                f'category: "{category.name}"\n'
                "status: active\n"
                "tags:\n"
                "  - system/category\n"
                "---\n"
                f"# {category.name}\n\n"
                f"上级领域：[[../{domain_index}]]。\n\n"
                "本目录存放以此分类为主要研究问题的资料。跨领域关系使用 `topic/...` 标签、Topic Hub 和内部链接。\n"
            )
            index.write_text(text, encoding="utf-8")
            count += 1
    print(f"created {count} category indexes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

