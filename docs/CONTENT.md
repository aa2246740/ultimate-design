# Ultimate Design 官网内容(展示版)

## 这页要完成什么

让第一次见到 Ultimate Design 的人,在六十秒内知道三件事:

1. 这是一个给 AI Agent 用的设计工作流技能:先理顺需求和内容,再落成真实制品,渲染复查后交付,并留下 `DESIGN.md` 契约。
2. 它随包携带一套可检索的设计知识框架(OKF):35 个概念文件、7 个知识域、19 份分支参考,按需加载并绑定到具体决策。
3. 一条命令就能装进 Codex、Claude Code 或 Pi Agent;想共同决定关键选择时用 `--pro`。

页面本身就是能力证明:它由本仓库的方法自举完成——契约在 `docs/DESIGN.md`,内容源在本文件,交付前经过渲染复查。页面上出现的每一个数字都必须能在仓库里数出来。

## 真实库存(页面统计数的唯一来源)

| 数据 | 值 | 核对方式 |
|---|---|---|
| OKF 概念文件 | 35 | `ls skill/ultimate-design/references/design-okf/*/*.md \| wc -l` |
| 知识域 | 7 | design-okf 下的子目录:foundations / systems / content / digital / methods / production / governance |
| 分支参考(playbook) | 19 | `ls skill/ultimate-design/references/*.md \| wc -l` |
| 内置脚本(校验与工具) | 11 | `ls skill/ultimate-design/scripts/ \| wc -l` |
| 任务路线 | 4 | SKILL.md:Build / Audit / Redesign / Study |
| 宿主集成 | 3 | Codex / Claude Code / Pi Agent |
| 协作模板 | 4 | templates/:work-order 等 |
| 完整案例 | 12 | `ls docs/demos/*/index.html \| wc -l`,由安装本技能的 Agent 按完整工作流设计,每个附带自己的 DESIGN.md |
| 版本 | 0.6.0 | package.json |

不得出现:用户数、星标数、成功率、案例数等仓库内无法核对的数字。

## 叙事顺序

### 第一屏(hero)

顶栏:品牌 Ultimate Design;锚点导航——方法、知识库、案例、上手;语言切换(中/EN);GitHub 链接。

Kicker 徽标:`Agent Skill · v0.6.0 · MIT`

主张(沿用品牌句):把设计做出来,也把判断留下来。

导语:Ultimate Design 是给 AI Agent 用的设计工作流:收到模糊需求时先理顺目标和内容,做完后对着真实渲染结果复查,最后把 `DESIGN.md` 契约留给下一位接手的人。

动作:

- 复制安装命令(主 CTA,复制 `npx ultimate-design-skill@latest --target claude-code`)
- 看它怎么工作(锚点跳转)

右侧运行记录卡:一张深色桌面上的"纸样",循环展示一次运行的五个阶段(需求锚点 → 内容契约 → 方向 → 制品 → 渲染复查),配红色批注记号。可点击切换,自动轮播,尊重 reduced motion。

统计条(全部真实,见上表):

- 35 个知识概念
- 7 个知识域
- 19 份分支参考
- 11 个内置脚本
- 12 个完整案例
- 3 个宿主

### 为什么需要它

标题:一张"看起来完成"的页面,往往只完成了一半。

说明:画面做出来以后,真正的问题才露出来。

三个具体问题(沿用现有版本,文案已被验证):

- 原始诉求被后续细节盖住了。
- 内容和版式一起开工,重要的话没有位置。
- 交付只剩截图,没人知道为什么这样取舍。

### 它留下什么(三件产物)

标题:每一次运行,留下三件能继续用的东西。

三张"纸面制品",各配一段真实样例片段:

- `Request Anchor`:这次到底要解决什么,谁来用,什么不能丢。样例片段:三行锚点记录。
- `DESIGN.md`:内容顺序、视觉方向、假设和待确认项。样例片段:契约 front matter 节选。
- `Rendered review`:真实页面、截图和复核结果。样例片段:一条已修复的批判发现。

### 工作方式(五步,可交互)

标题:先把事情说清,再把画面做对。

交互:五个步骤可点击,当前步骤展开一个真实的微型制品;默认停在第 1 步,不自动跳动。

1. 读需求 —— 保留原始诉求、最新调整和验收标准。微型制品:需求锚点条目。
2. 理内容 —— 确定先让人看懂什么,哪些话必须准确。微型制品:信息层级清单。
3. 定方向 —— 选择色彩、字体、密度、版式和参考策略。微型制品:taste dials 摘要。
4. 做成品 —— 落到网页、产品界面、Deck、图形或品牌材料。微型制品:带 `data-ud-check` 的代码片段。
5. 回看交付 —— 对着渲染结果修问题,补上下一位能读懂的记录。微型制品:验证清单(契约校验、渲染复查、双语核对)。

### 知识库(OKF 浏览器,可交互)

标题:35 个概念,按需加载,绑定到决策。

说明:OKF 不是装饰性的背景知识。每个被激活的概念,都必须绑定一条具体决策、一个制品目标和一条验证钩子;贡献结束就退场。

交互:搜索框(占位符:搜索概念、文件名或关键词…)+ 域筛选片(全部 / 基础 / 系统 / 内容 / 数字 / 方法 / 生产 / 治理 / 分支参考)+ 结果计数(如"54 项中的 9 项")。

数据:35 个 OKF 概念 + 19 份分支参考,共 54 条。每条含:文件路径、域、中英文标题、中英文一句话摘要、关键词。摘要必须忠实于源文件,不得虚构。

空态文案:没有匹配的条目。换个关键词,或清除筛选。

### 案例画廊(完整页面,可点开体验)

标题:十二个完整页面,十二种设计语言。

说明:每个案例都由安装了本技能的 Agent 按完整工作流设计——契约、实现、批判、渲染复查。缩略图是案例页的实时渲染(缩放的 iframe),不是截图;点开就是真实页面,旁边是能复现它的 Prompt 和它自己的 `DESIGN.md` 契约。所有品牌均为虚构。

卡片动作:查看页面(新标签打开)· 复制 Prompt · 看契约(链接到该案例的 DESIGN.md)。

十二个案例(slug · 类目 · 风格 · 语言 · 复现 Prompt):

1. `finlytics` · 营销页 · 深色数据感 · EN —— Prompt:`$ultimate-design Design a marketing landing page for Finlytics, a fictional real-time revenue analytics platform for subscription businesses. Dark, data-forward, credible; charts drawn in CSS/SVG; pricing and a demo CTA.`
2. `teahouse` · 品牌官网 · 东方编辑感 · 中文 —— Prompt:`$ultimate-design 为虚构茶馆品牌「山声茶事」设计品牌官网首页:山泉煮茶的门店故事、三款招牌茶、茶席预约。东方编辑感、纸感底色、宋体标题、竖排点缀。`
3. `taskflow` · 产品界面 · 冷静系统感 · EN —— Prompt:`$ultimate-design Design the main dashboard screen for TaskFlow, a fictional project management tool: sidebar, project board with task cards, activity feed, summary row. Light, calm, production-quality states.`
4. `petcare` · 预约落地页 · 活泼圆润 · 中文 —— Prompt:`$ultimate-design 为虚构宠物洗护品牌「毛茸茸研究所」设计预约落地页:服务套餐、价格、门店预约表单。活泼、圆角、奶油色系,但专业可信。`
5. `deck-q2` · HTML Deck · 汇报叙事 · 中文 —— Prompt:`$ultimate-design 把「2026 Q2 增长复盘」做成 HTML 演示 deck:8–10 页,封面、议程、3 个数据页(CSS/SVG 图表)、结论页;键盘翻页、页码、可打印。数据虚构。`
6. `gridnoise` · 作品集 · 新粗野主义 · EN —— Prompt:`$ultimate-design Design a one-page portfolio for GRID&NOISE, a fictional independent design studio: manifesto, text-based selected works, services, contact. Neo-brutalist - hard borders, offset shadows, aggressive type - but readable and accessible.`
7. `systema` · 会议活动 · 瑞士国际主义 · EN —— Prompt:`$ultimate-design Design the landing page for SYSTEMA 2026, a fictional one-day conference on design systems. Swiss International Style: strict modular grid, oversized flush-left type, one red accent, the schedule set as a designed table. English.`
8. `maison` · 电商产品页 · 静奢极简 · EN —— Prompt:`$ultimate-design Design a product detail page for Maison Ombre Eau de Parfum No.04, a fictional fragrance house. Quiet luxury: muted warm neutrals, generous whitespace, serif with humanist sans, a CSS/SVG still-life instead of photography, ingredients accordion, sticky add-to-cart. English.`
9. `field7` · 硬件产品页 · 工业功能主义 · EN —— Prompt:`$ultimate-design Design the product page for FIELD-7, a fictional pocket synthesizer. Industrial functionalism: a detailed inline-SVG schematic as the hero, a knolling grid of accessories, mono spec tables, functional gray with industrial orange. English.`
10. `jiexiang` · 独立刊物 · 新闻纸编辑 · 中文 —— Prompt:`$ultimate-design 为虚构独立城市观察刊物「街巷」设计创刊号页面:报头、本期目录、三篇文章的多栏报纸排版、订阅栏。新闻纸编辑风:多栏网格、首字下沉、细规则线、黑白加一个专色蓝。中文。`
11. `shuguang` · 数据报告 · 数据叙事 · 中文 —— Prompt:`$ultimate-design 为虚构阅读 App「拾光书房」设计 2026 年度阅读报告页:巨号数字开场,每屏一个数据结论配一张 SVG 图表(时长分布、类目偏好、夜读热力、年度书单),浅底高饱和数据色。数据虚构。中文。`
12. `neuehalle` · 展览海报 · 包豪斯几何 · 中文 —— Prompt:`$ultimate-design 为虚构美术馆「新厅美术馆」设计展览页「形式与功能:包豪斯百年」:海报式几何 hero(三原色、圆三角方构成)、展览介绍、三个展区、参观信息与票务。中文。`

画廊卡片标注格式:名称 + 类目片 + 风格一句话 + 语言标签;底部一行说明「由安装本技能的 Agent 设计,契约随附」。

### 模式与路线

标题:默认直接做;要对齐时再对齐。

三种协作模式:

- 默认(YOLO):不盘问用户,从现有材料推断,先交出完整的第一版。
- `--pro`:受众、信息重点、品牌气质、验收标准先对齐,再开始做。
- Portable Specialist:多域高风险工作时,Integrator 分发工单,专家返回结果包,最终制品只有一个执笔人。

四条任务路线(横向片):Build 做出来 · Audit 只诊断 · Redesign 保内容换结构 · Study 提取可迁移机制。

### 怎么开始

宿主选择(三个标签页,各配复制按钮):

```bash
npx ultimate-design-skill@latest --target codex
npx ultimate-design-skill@latest --target claude-code
npx ultimate-design-skill@latest --target pi-agent
```

普通模式提示词(短,表达结果):

```text
$ultimate-design 帮我把这份研究做成一个便于阅读的网页。先处理内容和设计方向,再实现、复查并修掉明显问题。
```

`--pro` 提示词(关键选择需要共同决定时):

```text
$ultimate-design --pro
我要做一个面向投资人的产品官网。先和我确定受众、信息重点、品牌气质和验收标准,再开始实现。
```

### 交付时看什么

标题:交出去的,不只有一个链接。

- 需求和取舍写在 `DESIGN.md`。
- 参考资料有来源和用途。
- 页面、幻灯片或图形按实际尺寸检查过。
- 未解决的风险被如实写下。

CTA:去 GitHub 看仓库。

### 自举声明(meta 条)

本页由 Ultimate Design 的方法自举完成:契约在 `docs/DESIGN.md`,内容源在 `docs/CONTENT.md`,交付前经过契约校验与浏览器渲染复查。两个文件都有 GitHub 链接,读者可以核对。

### 页脚

MIT 许可 · GitHub 仓库 · npm 包 · 集成说明(integrations/README.md)· 语言切换。

## 文案规则

- 中文从中文的判断顺序出发;英文是独立的平行表达,不逐句翻译。
- 用具体对象和动作替代"体系、赋能、升级、重要、专业、品质"等抽象评价。
- 不使用"不是……而是……"作为整页骨架;不用"首先、其次、最后"撑结构。
- 每段至少交代一个事实、动作、限制或可见结果;没有新增信息的句子删掉。
- 不编造案例、数字、客户或结果。页面统计数只允许来自"真实库存"表。
- 样张必须如实标注"渲染在本页",不得暗示是客户项目或产品截图。
- 保留正常的句长和语气变化,不为了风格牺牲准确。

## English Page

The English page is a parallel expression, not a sentence-by-sentence translation.

Hero claim: Build the design. Keep the judgment.

Lead: Ultimate Design is a design workflow skill for AI agents. It turns a vague ask into a clear brief and a real artifact, reviews the rendered result before handoff, and leaves a `DESIGN.md` contract the next agent can continue from.

Stat labels: 35 knowledge concepts · 7 domains · 19 branch playbooks · 11 bundled scripts · 12 complete demos · 3 hosts.

Section titles (parallel, not literal):

- Why: A page that looks finished is often half done.
- Outputs: Every run leaves three things you can keep using.
- Workflow: Say it clearly first, then get the picture right.
- Knowledge: 35 concepts, loaded on demand, bound to decisions.
- Gallery: Twelve complete pages, twelve design languages. (Card note: each demo was designed by an agent running this skill and ships with its own `DESIGN.md`; thumbnails are live renders, not screenshots; all brands fictional.)
- Modes: Ship by default. Align when it matters.
- Start: Install, then describe the outcome you want.
- Delivery: What you hand over is more than a link.
- Meta strip: This page bootstraps itself with Ultimate Design — its contract lives in `docs/DESIGN.md`, its content source in `docs/CONTENT.md`, and it was render-reviewed before delivery.

Avoid "transform", "elevate", "empower", "seamless", "world-class", "supercharge", and generic contrast formulas. Keep sentences plain and specific.

## 交互要求

- 中文为默认语言;顶部切换会替换整页文案并更新 `<html lang>`;`?lang=en` 直接打开英文态;`index-en.html` 保持跳转。
- 所有复制按钮复制当前语言的内容,成功/失败以当前语言短暂提示。
- OKF 浏览器为纯客户端过滤,数据内联在页面里;无网络请求。
- 案例画廊缩略图用缩放 iframe 实时渲染案例页:`loading="lazy"`、`aria-hidden="true"`、`tabindex="-1"`、`pointer-events: none`;「查看页面」新标签打开 `demos/<slug>/`;「复制 Prompt」复制 CONTENT.md 里对应的 Prompt 原文;「看契约」打开该案例的 DESIGN.md。
- 五步工作流手动切换,不劫持滚动。
- 所有进场动效用 transform/opacity,时长 ≤ 400ms;`prefers-reduced-motion: reduce` 时全部退化为静态。
- 桌面与移动端都要有干净的阅读路径;知识库是唯一允许的高密度区。
