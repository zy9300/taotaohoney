---
type: source
title: "我把 Codex 接进 Obsidian，做了一个会自动整理资料的 AI 知识库"
primary_domain: "05-AI/Codex"
source_url: "https://mp.weixin.qq.com/s/Q4THoKbQmpdFg2EyjU9oDg?token=1170307989&clicktag=bar_share&scene=294&clickpos=25369&from_safari=1"
author: "KK"
published: "2026-06-21 12:51"
captured: "2026-06-28T17:13"
original_file: "00-Inbox/Downloaded/2026-06-28T171336+0800我把 Codex 接进 Obsidian，做了一个会自动整理资料的 AI 知识库.md"
original_sha256: "703738917797d0c109ed8b5b57cfc1206cfd8451c332c6d163e70122af80ac59"
tags:
  - status/processed
  - source/imported
  - topic/ai
  - topic/agent
  - topic/codex
  - topic/prompt
  - topic/workflow
  - topic/automation
  - topic/obsidian
  - topic/github
  - topic/knowledge-management
  - topic/content-creation
topics:
  - "[[04-Research/Topic Hubs/AI Hub]]"
  - "[[04-Research/Topic Hubs/Agent Hub]]"
  - "[[04-Research/Topic Hubs/Codex Hub]]"
  - "[[04-Research/Topic Hubs/Prompt Hub]]"
  - "[[04-Research/Topic Hubs/Workflow Hub]]"
  - "[[04-Research/Topic Hubs/Automation Hub]]"
  - "[[04-Research/Topic Hubs/Obsidian Hub]]"
  - "[[04-Research/Topic Hubs/GitHub Hub]]"
  - "[[04-Research/Topic Hubs/Knowledge Management Hub]]"
  - "[[04-Research/Topic Hubs/Content Creation Hub]]"
---

> [!source] 来源与保真信息
> 原文链接：https://mp.weixin.qq.com/s/Q4THoKbQmpdFg2EyjU9oDg?token=1170307989&clicktag=bar_share&scene=294&clickpos=25369&from_safari=1  
> 作者：KK  
> 发布时间：2026-06-21 12:51  
> 原始文件：`00-Inbox/Downloaded/2026-06-28T171336+0800我把 Codex 接进 Obsidian，做了一个会自动整理资料的 AI 知识库.md`  
> 本文件仅做结构与排版清理；下载原文保持不变。
# 我把 Codex 接进 Obsidian，做了一个会自动整理资料的 AI 知识库
来源：
https://mp.weixin.qq.com/s/Q4THoKbQmpdFg2EyjU9oDg?token=1170307989&clicktag=bar_share&scene=294&clickpos=25369&from_safari=1
作者：
KK
抓取时间：
2026-06-28T17:13:36+08:00
---
KK KK的AI笔记 *2026年6月21日 12:51*

👆点击 **KK的Ai笔记** >点击右上角“···”>设为星标🌟

看到一篇好内容，先收藏；看到一个 Prompt，先保存；看到一个工具教程，先丢进文件夹。东西越攒越多，真正要写文章、做视频、找资料时，又要从截图、链接和聊天记录里重新翻。

现在我把 Obsidian 当成长期资料库，把 Codex 当成整理资料的人。网页、推文和教程先统一收进去，Codex 再负责清洗、改标题、归类、打标签、挂到对应主题上。等我要写公众号、X、小红书或者视频脚本时，AI 可以先读我的长期规则和写作偏好，知道我是谁、我做什么内容、哪些东西已经验证过。

## 00｜先看搭好之后长什么样

我现在的 Obsidian 不是一个散乱笔记本，它更像一个本地工作台。左侧是一套已经分好用途的资料入口，收集、研究、内容、项目和 Prompt 都有各自的位置。给 AI 读取的长期规则也单独放着，后面让 Codex 写文章、整理资料时，它不用每次从零猜我的偏好。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2ML04Aj4ay8PI4MQia3rKbhGV1NvwDjjIwyGSk6yFxsIaguKspea0y22iaWcXe6zXc9xeSWbaR6wSkUiafVHZZ6pLQXuHNx1bHXHtw/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=0)

关系图谱打开后，主题之间会连起来。比如我点 Codex 这个主题 Hub，和 Codex 相关的教程、工具、工作流、插件、内容创作案例都会展开。这个感觉和普通文件夹不太一样。普通文件夹只能告诉你文件放在哪里，图谱会告诉你资料之间怎么互相连接。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MIfiaZk98bic4ehPibzPticC00oa6jLkNn0YF4AJljh8bYv4XovuSO6JxgITc1LV1FBHtgwviao7nuX9AbhsILbR1qK2D1DBia8JibAIs/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=1)

我看重的是后面的复用能力。比如我后面要写一篇 Codex 文章，只要让 Codex 找出知识库里和 Codex 相关的资料，它就能沿着主题 Hub 和标签把旧资料翻出来。以前我靠记忆找，现在我让系统找。

## 01｜先在 Obsidian 里建一个本地仓库

Obsidian 的仓库可以理解成一个本地文件夹。你的每一篇笔记，本质上都是电脑里的 Markdown 文件。这个设计很适合和 Codex 配合，因为 Codex 可以直接读取、修改、整理这些文件。打开 Obsidian 后，右下角进入管理仓库。新手刚打开时，界面会很空，甚至有点不知道该点哪里。正常，这一步只需要先把仓库建出来。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MIPJ5WLABPf0QblmYY5n6jdHQc2Fpl0xSMiaw2q8FiaMEbSBbAoVnicGSW6Xicqe5mEe6XO7n9bRRPdSUFrGtBfoyVOPiaicqWefpOQY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=2)

新建仓库时，仓库名称按自己的项目来起。我的叫 `KK-AI-Knowledge-Base。` 仓库位置我更建议放到 D 盘，别放在桌面，也别放在系统盘太深的位置。后面 Codex 要读取这个路径，路径越清楚，越不容易出错。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2MI3yU5Kl6Pzt4apRY83JibjMMkjrEIIDXEUkrFagIOCT0kdyUIos8BmNjLq7xXpZPnrdl0U7uSymmnVh7OyqHwjAlQA0qBbNkUY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=3)

这里有两个信息要记下来：

## 1. 仓库名称。

2. 本地路径。后面写给 Codex 的提示词会用到它们。路径不要凭感觉写，直接从资源管理器复制更稳。
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MJfypfU0jXAZs5jFDjd2mQ01wll8ZiaerVwT5JdxficSaEBHzHR613KEK4oRCv0vSgs3sk4CYwzpfXwGw8x7PBJIVviacvqcZqcE0/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=4)

## 02｜给这个知识库建一个 GitHub 私有仓库

只做本地版也能跑起来，但我不太建议长期这么用。知识库一旦用起来，里面会有你长期积累的资料、Prompt、内容复盘和项目状态。

电脑坏一次，或者换电脑时忘了迁移，损失会很大。我的做法是给 Obsidian 仓库配一个 GitHub 私有仓库。

平时资料保存在本地，同时同步到 GitHub。这样有版本记录，也有一份云端备份。进入 GitHub 后，点击右上角头像旁边的菜单，新建仓库。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2ML8AMs0rIG838KxE6FN0ZBmayPqad3qyxSqwWchZaNwySRCTAtSsaobiaBL3Ihk0KCLmufO7SlfibWK3tblucd2G8niaVKwnJ3icPI/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=5)

仓库名称最好和 Obsidian 仓库保持一致。权限选择 Private。公开仓库不适合放个人知识库，里面可能会有私密笔记、未发布选题、账号使用记录、工作流和 Prompt。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MJafQ3J5DZyicls47j782iaOhBd9DdGCJGtTJghdibDY03LbOABlcczMP5tgNkX0hLibFxNZvxoFCb6qvH3SF3XngJOywpypSpx8mc/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=6)

这一步做完，把 GitHub 仓库地址保存下来。后面交给 Codex 时，它需要知道这个本地仓库要同步到哪里。

## 03｜提前准备 GitHub Token

Codex 要把本地 Obsidian 仓库同步到 GitHub，电脑需要获得 GitHub 的授权。这里用的是 GitHub Personal access token。进入 GitHub 设置页面。右上角头像打开菜单，选择 Settings。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MKGuZWIpjJibAibVPIuXxMsibic0UIcaxnv7mZHtRPK8iaO8GHVAH8HHaclZMM3dx488hI2ibH21KNibh4BibSdL262sEd0GDfibR8vtIRk/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=7)

设置页面左侧往下找到 Developer settings。这个入口有点深，很多人第一次会找半天。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MJ3AWstniaIhUOzBatbkyhPbth2bWSem7FXLRTIOIQUoELtMPCzPnXvnHyC6YFhtluBxVscgFU7j5xaWo2nRXRJ3mqqXf3faHxQ/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=8)

进入 Developer settings 后，选择 Personal access tokens。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MKbib0gt4yGdKZ4cvDMEj5sy0qZwSEIVMoJYIOHAzr8hXG5eiafh4xC4x3pX6LPbYmkqruvZVHxEHnrlibHHTN5pubZUB4xjTtUn8/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=9)

再点 Generate new token。GitHub 会让你确认权限和验证码。Token 生成后只出现一次，自己保存好。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MK1W3VTAhup8jugVW3sMfmz0iaICFdu4el6KDDkhH2bPia3KicEvTE6xuPKN1IZIpKXbT9r05aeiaU0Khq03v4UzsdylmN9tqmIP0U/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=10)

这里我多说一句：Token 不要直接粘贴到 AI 聊天窗口里。等 Git 或 GitHub 授权窗口需要时，再粘贴到对应输入框。权限能少给就少给，别为了省事把所有权限全打开。

## 04｜把仓库规则交给 Codex

Obsidian 仓库、GitHub 私有仓库、Token 都准备好后，就可以让 Codex 去做底层搭建了。这一步不要只说“帮我建一个知识库”。

这句话太泛。你要把自己的长期方向、平台、内容类型、文件夹规则、AI 记忆规则一次性讲清楚。

Codex 才知道它要建的是一个长期内容系统，不是随便生成几个文件夹。我这套提示词里，最重要的是 AI 记忆系统。

它规定 Codex、Claude Code、Cursor 这类 Agent 以后怎么读取我的上下文，哪些内容该写进长期记忆，哪些内容不能乱存。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MIVKPFlxpluTkSE5lkKwc4pazbGYDw7DprtML7pTQHVJb8nRcHmOrZdhhzkJrmeaAEbxTASnRCEQGH418vpsmknvzE073bwMlg/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=11)

你可以按这个结构写给 Codex。完整模板放在文末附录，复制时把路径、仓库地址和研究方向换成自己的信息。比如你不是做 AI、Crypto、US Stocks，那就把研究方向换成自己的领域。做职场、投资、设计、运营、跨境、电商都可以，重点是让 Codex 知道你长期关注什么。

## 05｜把AI的记忆目录放进系统底层

我这套知识库里，\`97-AI-Memory\` 和 \`98-AI-Context\` 很重要。

\`97-AI-Memory\` 更像经验本。它记录已经发生过、以后还要用的信息，比如成功项目、踩坑经验、长期决策、工作流、待办和最佳实践。

\`98-AI-Context\` 更像个人说明书。它告诉 AI：我是谁，我做什么内容，我的读者是谁，我讨厌什么文风，我的公众号、X、小红书、YouTube 分别怎么写。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2ML6K6icfcKib2Eics7crTMibCdf9695A37BdicW2RahIyIcAb1Tc2BgG3udjdzCbKJKEvxRt56JyAP2h5fzAHgOUhKuiawwYHJH5P3dE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=12)

这个设计解决了一个很烦的问题：每次开新对话，不用反复告诉 AI “我是谁、我做什么、我要什么风格”。Codex 直接读这些文件，就能按你的长期规则工作。我现在写公众号文章、做 X Article、整理研究资料，都会让 AI 先读这些上下文。它至少不会一上来就写成官方说明，也不会把我的内容方向搞错。

## 06｜用 Obsidian Web Clipper 收集网页

知识库搭好后，最麻烦的地方变成资料入口。手动复制网页、粘贴正文、改标题、放文件夹，这种事做几次还行，长期做一定会烦。我用的是 Obsidian Web Clipper。它是浏览器扩展，可以把网页、X 文章、教程页面直接保存到 Obsidian。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MIj8epdhhibrN0dgeBxE3t7r819pfhxF8YT5sK65aEiaUJ96W0bicH9OPoj4AMvSK2yED6ficL2MOovtSGM6rkaSUZmjjKWh2icoYGA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=13)

装好后，重点是配置模板。我的模板叫 `Research Capture，` 默认保存到：

> 00-Inbox/Downloaded

也就是所有新资料先进入 Inbox，不急着分类。这个习惯很重要。收集阶段别逼自己马上判断，它会把保存成本拉高。先收进来，后面再让 Codex 统一处理。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2MJmIibtYiaq1hibNONpjJ2CICcgIAbB5ic8aKNLI7iaDJbY9Eicv7gqlFVeSU4bW4hLpKUMhfXBGoAc1uVA2l1ShwHZdrkEwNNRHEaSE/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=14)

模板不用写得很花。我的版本只保留标题、来源、作者、抓取时间和正文，够用，也不容易乱。

笔记内容按下面填：

`# {{title}}`

来源：

`{{url}}`

作者：

`{{author}}`

抓取时间：

`{{date}}`

`---`

`{{content}}`

不用一开始就把模板搞得很复杂。先保证它能稳定保存网页，能留下来源，能进入正确文件夹。

## 07｜实际保存一篇文章

比如我看到一篇关于 Claude 做 YouTube 视频的文章，打开 Web Clipper，点击添加到 Obsidian。网页内容会被保存成一篇 Markdown 笔记。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2MJCnyWMiakBYBta1WHFib3owzY5tAV9XgCvTwjML3TQSZlyPgIw5bvthJyyXmwMvZ4VO79nhyhEppf1T9oEGFKe3icDicgY8YzYibHY/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=15)

回到 Obsidian 后，这篇文章会出现在 `00-Inbox/Downloaded。` 它还没有正式进入研究目录，只是一个刚收进来的原始资料。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/nmC3ics2A2MJUWm0zJLYeAajQyzuWZ5BzMs6uKibM6jokdlMXQ7iaMaxHiadMapP9ZnicI8uw2icJXRQJZwQAwt4XUqyUZ3HWs0BPFxQlD5ibQE120/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=16)

有些页面会保存失败。比如本地页面、特殊页面、非 http 或 https 页面，Web Clipper 可能会提示无法剪藏。这个不是配置坏了，换成正常网页链接再试。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2MKHoV4SibW23XOtI9ORTDbuQ36QPUwBEAFA4Yx3icUpiaaVR61zknjy1YyJPFh4cSK84S3cscdzY9Z3lrpat4jpd4cclibSQGp4BfA/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=17)

当 `Downloaded` 里的资料越来越多，就别手动整理了。这个阶段交给 Codex。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2MKhGPDMVLNumXQ9X8iapTiaw2taG1SKU3vsBVj9AD6xM3olYqz4MAFX0jEm2O91jTPogsLtqybpqRufzB6KpGGMPfyUMFico8krgc/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=18)

## 08｜让 Codex 自动清洗和归类

我给 Codex 的清洗指令也放在文末附录里。Codex 处理完后，会告诉我哪些文章进入了哪个目录，哪些旧稿已经归档，Downloaded 是否清空，GitHub 是否同步成功。它还会检查文件名、标题、frontmatter 和正文标题是否一致。

![图片](https://mmbiz.qpic.cn/mmbiz_png/nmC3ics2A2MLpb4iapb4Vhianaic3CnHjfB1fyapuTa4XD7BvZrcHoonI9RGAgdfjjTcVlS74nWhZJudv732fplyAEAcImLevaziaicXOtM0hBv3Y/640?wx_fmt=png&from=appmsg&watermark=1#imgIndex=19)

这一步做完，网页收藏才算真正进入知识库。否则它只是一堆“以后再看”的材料。

## 09｜最容易卡住的几个地方

## 1. 路径写错。Obsidian 仓库路径建议直接从资源管理器复制，别手打。路径一错，Codex 后面会直接找不到文件。

2. GitHub 权限混在一起。私有仓库、Git 凭证、Token 容易搞混。Token 不要粘到 AI 聊天窗口里，需要授权时再粘到 GitHub 或 Git 的输入框。

3. 目录一开始建太复杂。刚开始别做几十层目录，先用 `00-Inbox、` `04-Research、` `05-Content、` `89-Prompts、` `97-AI-Memory、` `98-AI-Context` 这几个主入口跑通。

4. 把收藏当整理。保存到 `Downloaded` 只是把资料收进来，真正有用的是后面的清洗、归类、主题标签和 Hub 链接。

5. 写文章前忘了读上下文。已经建了 `97-AI-Memory` 和 `98-AI-Context，` 写公众号、脚本、标题前就让 Codex 先读。这样它更像接着你的长期工作写，不会每次从零猜。

## 10｜写在最后

我现在更愿意把 Obsidian 理解成一个长期资料底座。Codex 负责处理那些我不想手动做的部分：改标题、分类、补标签、同步 GitHub、读取上下文、从旧资料里找线索。

这套系统刚开始搭会有点麻烦。建仓库、配 GitHub、写规则、调 Web Clipper，每一步都不算难，但堆在一起会让人想偷懒。

可一旦跑通，后面会轻很多。看到好资料，先收进来；一段时间后，让 Codex 清洗；需要写某个主题，再从知识库里把相关资料拉出来。

这个流程更慢一点，但资料会留下来，判断也会留下来。Obsidian 负责保存，Codex 负责整理，\`97-AI-Memory\` 和 \`98-AI-Context\` 负责让 AI 记住你的长期方向。

---

### 附录：万能提示词模板

下面这段可以直接复制到 Codex 里。把 Vault 路径、GitHub 仓库、研究领域和内容输出平台换成自己的信息。

你现在是我的 Obsidian Knowledge Base Architect（知识库架构师）兼系统管理员。

目标：

从零开始搭建一套 AI Native Obsidian Knowledge Base。

不要只提供建议。

优先直接执行。

无法自动执行的部分，请明确告诉我需要准备什么资料。

最终目标：

搭建一套长期可扩展、支持 AI Agent 使用、支持 GitHub 同步、支持知识图谱、支持内容创作的 Obsidian 知识库。

我的信息：

Vault 路径：

【填写你的 Obsidian Vault 路径】

GitHub 仓库：

【填写 GitHub 仓库地址】

主要研究领域：

【填写】例如：

AI

Crypto

US Stocks

Programming

Design

Marketing

Finance

Law

Medicine

Photography

主要内容输出：

【填写】例如：

公众号

YouTube

B站

小红书

抖音

TikTok

Newsletter

博客

课程

是否已经安装 Git：

【是 / 否】

是否已经创建 GitHub 私有仓库：

【是 / 否】

第一步：检查环境

检查：

## 1. Obsidian 是否安装

2. 当前 Vault 是否存在

3. Git 是否安装

4. GitHub 是否连接

5. GitHub 是否可 Push

6. GitHub CLI 状态

7. Obsidian 插件状态

8. 当前目录结构

9. 当前权限状态

输出：

已完成

未完成

需要我补充的资料

不要跳过检查。

第二步：建立知识库基础架构

必须创建：

00-Inbox

04-Research

05-Content

06-Projects

89-Prompts

90-Templates

97-AI-Memory

98-AI-Context

99-Archive

不要创建无意义目录。

第三步：建立 Inbox 收集系统

创建：

00-Inbox

├─ Attachments

├─ Downloaded

├─ Cleaned

创建：

Research Import Guide

Research Triage Guide

Research Collection Workflow

第四步：建立 Research 系统

根据我的研究领域自动生成目录。

不要硬编码目录。

根据实际方向自动生成。

例如：

AI

Models

Workflow

Automation

Tools

MCP

Business

Design

Information-Sources

Crypto

Market

Research

Onchain

Protocols

US Stocks

Portfolio

Macro

Valuation

Global Finance

Banking

Cards

Credit System

自动决定。

第五步：建立 Content 系统

创建：

Ideas

Scripts

Published

用于内容生产。

第六步：建立 Projects 系统

创建：

Project Status

并规范：

每个项目自动包含 Project-Status.md。

记录：

当前状态

已完成事项

待办事项

下一步

风险

决策

第七步：建立 Prompt Library

创建：

89-Prompts

并建立：

Prompt Index

Prompt Library Guide

自动分类：

Research

Workflow

Automation

Business

Content

Video Script

Cover Design

第八步：建立 Templates

创建：

Research Template

Daily Note Template

Project Template

Prompt Template

Source Template

Content Brief Template

第九步：建立 AI Memory

创建：

97-AI-Memory

并建立：

TODO

Ideas

Decisions

Best Practices

Lessons Learned

Workflows

Knowledge Summary

Current Trends

Successful Projects

Future Ideas

User Preferences

第十步：建立 AI Context

创建：

98-AI-Context

并建立：

About Me

Current Focus

Channel Positioning

Platform Strategy

Content Strategy

Writing Style

Prompt Rules

Knowledge Map

AI Operating Context

AGENTS

第十一步：配置 GitHub 自动同步

检查：

Git

GitHub

GitHub CLI

Obsidian Git

自动配置：

Pull

Push

自动备份

同步验证

输出验证结果。

第十二步：配置 Web Clipper

创建：

Research Capture

模板要求：

自动保存标题、来源、作者、时间、正文。

进入：

00-Inbox/Downloaded

第十三步：配置 MarkDownload 工作流

建立：

MarkDownload

↓

Downloaded

↓

Research Cleaner

↓

Research

形成完整流程。

第十四步：建立 Research Cleaner

要求：

自动处理 Markdown。

功能：

自动分类

自动命名

自动提取来源

自动提取链接

自动识别标题层级

自动识别编号列表

自动分段

提高可读性

保留全部原文

不删减

不总结

不改写观点

第十五步：建立 Knowledge Base Audit

用于：

检查重复内容

检查分类冲突

检查异常文件名

检查空目录

检查垃圾文件

检查孤立文件

生成巡检报告

第十六步：建立 Knowledge Graph（知识图谱）

重要：

不要只依赖文件夹分类。

知识库必须同时支持：

## 1. 文件夹分类

2. 标签系统

3. Topic Hub

4. 内部链接

请扫描 04-Research 中的全部内容。

分析：

高频主题

高频工具

高频工作流

高频商业模式

高频平台

建立 Topic Hub 系统。

例如：

Codex

Claude Code

Prompt

Workflow

Agent

MCP

Obsidian

GitHub

Content Creation

Monetization

SEO

Crypto

US Stocks

自动决定。

规则：

一个文件只能有一个主分类目录，但可以拥有多个主题标签。

例如：

主目录：

AI / Workflow

标签：

topic/codex

topic/agent-workflow

topic/github-open-source

topic/claude-code

创建：

Topic Index.md

Topic Hub Template

并建立：

Codex Hub

Claude Code Hub

Prompt Hub

Workflow Hub

Obsidian Hub

GitHub Hub

等主题中心页。

升级 Research Cleaner，使其支持：

自动主题标签

自动 Topic Hub 引用

自动内部链接

不要只做文件夹分类。

第十七步：建立 AI Agent 记忆系统

适用于：

Codex

Claude Code

Cursor

等 Agent

规则：

不要保存聊天记录。

只保存长期有价值的信息。

当形成经验、决策、工作流，或者推进项目、发现最佳实践时，自动更新：

97-AI-Memory

98-AI-Context

06-Projects

最终输出：

## 1. 完整目录结构

2. 已完成配置

3. 未完成配置

4. 需要我手动操作的步骤

5. 当前知识库评分

6. 当前知识地图

7. 当前薄弱领域

8. 下一步建议

优先执行。

不要只输出方案。

---

收录于Obsidian教程

## 关联主题

- [[04-Research/Topic Hubs/AI Hub]]
- [[04-Research/Topic Hubs/Agent Hub]]
- [[04-Research/Topic Hubs/Codex Hub]]
- [[04-Research/Topic Hubs/Claude Code Hub]]
- [[04-Research/Topic Hubs/MCP Hub]]
- [[04-Research/Topic Hubs/Prompt Hub]]
- [[04-Research/Topic Hubs/Workflow Hub]]
- [[04-Research/Topic Hubs/Automation Hub]]
- [[04-Research/Topic Hubs/Obsidian Hub]]
- [[04-Research/Topic Hubs/GitHub Hub]]
- [[04-Research/Topic Hubs/Business Model Hub]]
- [[04-Research/Topic Hubs/Enterprise Operations Hub]]
- [[04-Research/Topic Hubs/Decision Making Hub]]
- [[04-Research/Topic Hubs/Knowledge Management Hub]]
- [[04-Research/Topic Hubs/Content Creation Hub]]
