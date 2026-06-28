#!/usr/bin/env python3
"""Conservatively clean imported Markdown while preserving the downloaded original."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
INPUT_DIR = VAULT / "00-Inbox" / "Downloaded"
CLEAN_DIR = VAULT / "00-Inbox" / "Cleaned"
ORIGINAL_DIR = CLEAN_DIR / "_Originals"
RESEARCH_DIR = VAULT / "04-Research"

CLASSIFIERS = {
    "01-世界/宏观经济": ["宏观", "经济", "通胀", "利率", "汇率", "货币政策", "财政", "gdp"],
    "01-世界/国家政策": ["国家政策", "监管", "政策", "法规", "国务院", "央行"],
    "01-世界/国际关系": ["国际关系", "地缘", "外交", "贸易战", "制裁"],
    "01-世界/时政热点": ["时政", "选举", "政府", "政治", "热点事件"],
    "01-世界/科技与AI发展": ["科技发展", "技术革命", "人工智能发展", "ai发展"],
    "01-世界/能源格局": ["能源", "石油", "天然气", "光伏", "电力", "新能源"],
    "01-世界/全球产业趋势": ["全球产业", "产业趋势", "制造业转移", "全球化"],
    "02-产业/行业研究": ["行业研究", "行业规模", "市场规模", "行业报告"],
    "02-产业/产业链与供应链": ["产业链", "供应链", "上游", "下游", "供应商"],
    "02-产业/商业模式": ["商业模式", "收入模式", "成本结构", "单位经济"],
    "02-产业/龙头企业": ["龙头企业", "市场份额", "头部企业"],
    "02-产业/竞争格局": ["竞争格局", "竞争对手", "集中度", "壁垒"],
    "02-产业/行业数据": ["行业数据", "统计数据", "数据库"],
    "02-产业/行业案例": ["行业案例", "案例研究"],
    "03-企业/企业战略": ["企业战略", "战略规划", "组织战略"],
    "03-企业/管理与运营": ["企业管理", "企业运营", "组织管理", "绩效管理"],
    "03-企业/采购生产销售": ["采购", "生产", "销售", "产销"],
    "03-企业/仓储物流": ["仓储", "物流", "库存", "运输"],
    "03-企业/财务税务资金": ["财务管理", "税务", "资金管理", "财务分析"],
    "03-企业/企业融资": ["企业融资", "股权融资", "债权融资"],
    "03-企业/数字化": ["企业数字化", "数字化转型", "erp", "数字运营"],
    "03-企业/企业案例": ["企业案例", "公司案例"],
    "04-金融/对公业务": ["对公业务", "公司银行", "企业银行"],
    "04-金融/票据业务": ["票据", "承兑汇票", "贴现"],
    "04-金融/贸易融资": ["贸易融资", "福费廷", "押汇"],
    "04-金融/供应链金融": ["供应链金融", "应收账款融资", "存货融资"],
    "04-金融/国内信用证与保理": ["信用证", "保理", "应收账款"],
    "04-金融/财资与现金管理": ["财资", "现金管理", "资金池", "结算"],
    "04-金融/授信与风险识别": ["授信", "信用风险", "风险识别", "风控"],
    "05-AI/AI基础与模型": ["大模型", "llm", "模型训练", "推理模型", "机器学习"],
    "05-AI/AI工具": ["ai工具", "工具调用", "copilot"],
    "05-AI/AI-Agent": ["agent", "智能体", "多智能体"],
    "05-AI/Codex": ["codex", "openai codex"],
    "05-AI/自动化工作流": ["工作流", "automation", "自动化", "n8n", "zapier"],
    "05-AI/Prompt工程": ["prompt", "提示词", "上下文工程"],
    "05-AI/AI商业化": ["ai商业化", "ai创业", "ai产品", "ai变现"],
    "05-AI/大众AI应用": ["普通人", "效率工具", "ai应用"],
    "06-人/心理学与认知科学": ["心理学", "认知科学", "认知偏差", "行为科学"],
    "06-人/哲学与历史": ["哲学", "历史", "思想史"],
    "06-人/周易与术数": ["周易", "梅花易数", "紫微斗数", "术数"],
    "06-人/思维模型": ["思维模型", "第一性原理", "系统思维"],
    "06-人/博弈论": ["博弈论", "纳什均衡", "策略互动"],
    "07-个人/我的知识与经验": ["我的知识", "我的经验", "复盘"],
    "07-个人/案例与思考": ["我的案例", "我的思考", "个人思考"],
    "07-个人/方法论与决策": ["方法论", "我的决策", "决策记录"],
    "07-个人/提示词": ["我的提示词", "个人prompt"],
    "07-个人/成长记录": ["成长记录", "个人成长"],
    "08-每日更新/AI资讯": ["ai资讯", "ai新闻"],
    "08-每日更新/财经新闻": ["财经新闻", "市场快讯"],
    "08-每日更新/时政新闻": ["时政新闻"],
    "08-每日更新/产业动态": ["产业动态", "行业动态"],
    "08-每日更新/银行业资讯": ["银行业资讯", "银行新闻"],
    "08-每日更新/政策更新": ["政策更新", "新规"],
    "08-每日更新/重大事件": ["重大事件", "突发事件"],
}

TOPICS = {
    "ai": ("AI Hub", ["人工智能", " ai ", "ai工具", "大模型", "llm"]),
    "agent": ("Agent Hub", ["agent", "智能体"]),
    "codex": ("Codex Hub", ["codex"]),
    "claude-code": ("Claude Code Hub", ["claude code"]),
    "mcp": ("MCP Hub", ["mcp", "model context protocol"]),
    "prompt": ("Prompt Hub", ["prompt", "提示词", "上下文工程"]),
    "workflow": ("Workflow Hub", ["工作流", "workflow"]),
    "automation": ("Automation Hub", ["自动化", "automation", "n8n", "zapier"]),
    "obsidian": ("Obsidian Hub", ["obsidian"]),
    "github": ("GitHub Hub", ["github", "git "] ),
    "macro": ("Macro Hub", ["宏观", "通胀", "利率", "汇率", "gdp"]),
    "policy": ("Policy Hub", ["政策", "监管", "法规"]),
    "supply-chain": ("Supply Chain Hub", ["供应链", "产业链", "上下游"]),
    "business-model": ("Business Model Hub", ["商业模式", "收入模式", "成本结构"]),
    "enterprise-operations": ("Enterprise Operations Hub", ["企业运营", "企业管理", "采购", "生产", "销售"]),
    "banking": ("Banking Hub", ["银行", "对公业务", "授信"]),
    "supply-chain-finance": ("Supply Chain Finance Hub", ["供应链金融", "贸易融资", "保理", "信用证"]),
    "decision-making": ("Decision Making Hub", ["决策", "心理学", "认知", "博弈"]),
    "knowledge-management": ("Knowledge Management Hub", ["知识管理", "知识库"]),
    "content-creation": ("Content Creation Hub", ["内容创作", "公众号", "小红书", "播客", "课程"]),
    "monetization": ("Monetization Hub", ["商业化", "变现", "货币化"]),
}

URL_RE = re.compile(r"https?://[^\s)>\]}]+")
YAML_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.S)


@dataclass
class CleanResult:
    source: str
    output: str
    classification: str
    topics: list[str]
    confidence: int


def scalar(frontmatter: str, key: str) -> str:
    match = re.search(rf"(?mi)^\s*{re.escape(key)}\s*:\s*[\"']?(.*?)[\"']?\s*$", frontmatter)
    return match.group(1).strip() if match else ""


def safe_name(value: str) -> str:
    value = re.sub(r"[\\/:*?\"<>|#\[\]]", "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .-")
    return (value[:120] or "Untitled Research").strip()


def unique_path(directory: Path, stem: str) -> Path:
    candidate = directory / f"{stem}.md"
    counter = 2
    while candidate.exists():
        candidate = directory / f"{stem} ({counter}).md"
        counter += 1
    return candidate


def extract_title(frontmatter: str, body: str, fallback: str) -> str:
    title = scalar(frontmatter, "title")
    if title:
        return title
    match = re.search(r"(?m)^#\s+(.+?)\s*$", body)
    return match.group(1).strip() if match else fallback


def classify(text: str) -> tuple[str, int]:
    lowered = f" {text.lower()} "
    scored = []
    for path, words in CLASSIFIERS.items():
        score = sum(lowered.count(word.lower()) for word in words)
        if score:
            scored.append((score, path))
    if not scored:
        return "05-AI/AI工具", 0
    scored.sort(key=lambda item: (-item[0], item[1]))
    return scored[0][1], scored[0][0]


def detect_topics(text: str) -> list[tuple[str, str]]:
    lowered = f" {text.lower()} "
    found = []
    for slug, (hub, terms) in TOPICS.items():
        if any(term.lower() in lowered for term in terms):
            found.append((slug, hub))
    return found


def normalize_body(body: str, title: str) -> str:
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    lines = body.splitlines()
    output: list[str] = []
    seen_h1 = False
    in_fence = False
    for raw in lines:
        line = raw.rstrip()
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence:
            heading = re.match(r"^(#{1,6})\s*(.+)$", line)
            if heading:
                level, text = len(heading.group(1)), heading.group(2).strip()
                if level == 1:
                    if seen_h1 or text.casefold() != title.casefold():
                        level = 2
                    else:
                        seen_h1 = True
                line = f"{'#' * level} {text}"
            elif re.match(r"^\d+(?:\.\d+)*[、.]\s*\S.{0,80}$", line) and output and output[-1] == "":
                line = f"## {line}"
            elif re.match(r"^\d+[.)、]\s+\S", line) and output and output[-1] != "":
                output.append("")
        output.append(line)
    if not seen_h1:
        output.insert(0, f"# {title}")
        output.insert(1, "")
    normalized = "\n".join(output).strip()
    normalized = re.sub(r"\n{4,}", "\n\n\n", normalized)
    return normalized + "\n"


def clean_file(path: Path, promote: bool) -> CleanResult:
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    yaml_match = YAML_RE.match(raw)
    frontmatter = yaml_match.group(1) if yaml_match else ""
    body = raw[yaml_match.end():] if yaml_match else raw
    title = extract_title(frontmatter, body, path.stem)
    source_url = scalar(frontmatter, "source_url") or scalar(frontmatter, "url") or scalar(frontmatter, "source")
    if not source_url.startswith("http"):
        url_match = URL_RE.search(raw)
        source_url = url_match.group(0).rstrip(".,;") if url_match else ""
    author = scalar(frontmatter, "author")
    published = scalar(frontmatter, "published") or scalar(frontmatter, "date")
    captured = scalar(frontmatter, "captured") or datetime.fromtimestamp(path.stat().st_mtime).isoformat(timespec="minutes")
    classification, confidence = classify(f"{title}\n{body}")
    topics = detect_topics(f"{title}\n{body}")
    topic_tags = [f"topic/{slug}" for slug, _ in topics]
    status = "processed" if confidence >= 2 else "needs-review"
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    metadata = [
        "---", "type: source", f'title: "{title.replace(chr(34), chr(39))}"',
        f'primary_domain: "{classification}"', f'source_url: "{source_url}"',
        f'author: "{author.replace(chr(34), chr(39))}"', f'published: "{published}"',
        f'captured: "{captured}"', f'original_file: "{path.relative_to(VAULT).as_posix()}"',
        f'original_sha256: "{digest}"', "tags:", f"  - status/{status}", "  - source/imported",
    ]
    metadata.extend(f"  - {tag}" for tag in topic_tags)
    metadata.extend(["topics:"] + [f'  - "[[04-Research/Topic Hubs/{hub}]]"' for _, hub in topics] + ["---", ""])
    source_block = [
        "> [!source] 来源与保真信息",
        f"> 原文链接：{source_url or '未识别'}  ",
        f"> 作者：{author or '未识别'}  ",
        f"> 发布时间：{published or '未识别'}  ",
        f"> 原始文件：`{path.relative_to(VAULT).as_posix()}`  ",
        "> 本文件仅做结构与排版清理；下载原文保持不变。",
        "",
    ]
    related = ["", "## 关联主题", ""] + [f"- [[04-Research/Topic Hubs/{hub}]]" for _, hub in topics]
    if not topics:
        related.append("- 待人工建立或关联 Topic Hub")
    cleaned_text = "\n".join(metadata + source_block) + normalize_body(body, title) + "\n".join(related) + "\n"
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    original_copy = ORIGINAL_DIR / path.name
    if not original_copy.exists():
        shutil.copy2(path, original_copy)
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    output = unique_path(CLEAN_DIR, safe_name(title))
    output.write_text(cleaned_text, encoding="utf-8")
    if promote:
        target_dir = RESEARCH_DIR / classification
        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(output, unique_path(target_dir, output.stem))
    return CleanResult(str(path.relative_to(VAULT)), str(output.relative_to(VAULT)), classification, topic_tags, confidence)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Markdown files; defaults to 00-Inbox/Downloaded")
    parser.add_argument("--promote", action="store_true", help="Also copy cleaned files into the predicted Research directory")
    args = parser.parse_args()
    paths = [Path(item).expanduser().resolve() for item in args.paths]
    if not paths:
        paths = sorted(INPUT_DIR.rglob("*.md")) if INPUT_DIR.exists() else []
    results = [clean_file(path, args.promote) for path in paths if path.is_file()]
    print(json.dumps([result.__dict__ for result in results], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

