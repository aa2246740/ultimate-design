# Ultimate Design

**Turn your coding agent into a disciplined designer-builder.** Contract first. Real artifact. Rendered proof.

[![npm](https://img.shields.io/npm/v/ultimate-design-skill)](https://www.npmjs.com/package/ultimate-design-skill)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![OKF BundleDex](https://bundledex.net/static-badge.svg)](https://bundledex.net)

Most AI "design" ends at a screenshot that looks finished and falls apart the moment requirements shift. Ultimate Design keeps the judgment attached to the pixels: it anchors the request, writes the design contract, builds the real thing, critiques it, and verifies the rendered result in a browser before it ships.

**[See it prove itself → aa2246740.github.io/ultimate-design](https://aa2246740.github.io/ultimate-design/)**
The showcase site was designed and built by agents running this skill — and every demo on it publishes its own `DESIGN.md` contract next to the page. No other design skill shows you its receipts.

## What a run leaves behind

Every run produces three things you can keep using:

- **Request Anchor** — what this run must solve, for whom, and what must not be lost.
- **`DESIGN.md` contract** — tokens, direction, assumptions, and open questions, written so the next agent (or human) can continue without reverse-engineering.
- **Rendered review** — the real page, screenshots, and browser-measured audits, not a promise.

## What's inside

| Capability | The receipts |
|---|---|
| **Operational design knowledge** | 35 concept files across 7 domains — layout, typography, color systems, motion language, content models, accessibility, governance. Loaded on demand and **bound to concrete decisions**, never dumped as vibes. |
| **19 branch playbooks** | Marketing sites, product UI, presentation decks, graphic/print, brand systems, motion audits, reference study, audit & polish, and more. |
| **11 bundled validators & tools** | Contract validation, OKF-usage validation, a pinned-Chromium **rendered UI audit** (overflow, clipping, occlusion, target sizes), motion-contract validation, agent-handoff checks. Machine-checkable design. |
| **4 task routes** | Build / Audit / Redesign / Study — it knows when *not* to redesign your product. |
| **Multi-agent native** | Portable Specialist mode: an Integrator routes work orders, specialists return packets, one writer owns the final artifact. Ships with the templates. |
| **12 complete demos** | Twelve pages in twelve deliberately different design languages, each designed end-to-end by an agent running this skill — contract included. |

## The demo gallery

Every demo below is a complete, self-contained page. Click through, copy the prompt that produced it, and read its contract — [all twelve in the gallery](https://aa2246740.github.io/ultimate-design/#gallery).

| Demo | Surface | Design language |
|---|---|---|
| [Finlytics](https://aa2246740.github.io/ultimate-design/demos/finlytics/) | SaaS marketing page | Dark data console |
| [山声茶事](https://aa2246740.github.io/ultimate-design/demos/teahouse/) | Brand site | Eastern editorial paper |
| [TaskFlow](https://aa2246740.github.io/ultimate-design/demos/taskflow/) | Product dashboard | Quiet daylight system UI |
| [毛茸茸研究所](https://aa2246740.github.io/ultimate-design/demos/petcare/) | Booking landing page | Cream-lab playful |
| [墨记 Q2 复盘](https://aa2246740.github.io/ultimate-design/demos/deck-q2/) | HTML slide deck | Mineral-paper report |
| [GRID&NOISE](https://aa2246740.github.io/ultimate-design/demos/gridnoise/) | Studio portfolio | Neo-brutalism |
| [SYSTEMA 2026](https://aa2246740.github.io/ultimate-design/demos/systema/) | Conference site | Swiss International Style |
| [Maison Ombre](https://aa2246740.github.io/ultimate-design/demos/maison/) | E-commerce product page | Quiet luxury |
| [FIELD-7](https://aa2246740.github.io/ultimate-design/demos/field7/) | Hardware product page | Industrial functionalism |
| [街巷](https://aa2246740.github.io/ultimate-design/demos/jiexiang/) | Independent publication | Newsprint editorial |
| [拾光书房](https://aa2246740.github.io/ultimate-design/demos/shuguang/) | Annual data report | Data storytelling |
| [新厅美术馆](https://aa2246740.github.io/ultimate-design/demos/neuehalle/) | Exhibition page | Bauhaus geometry |

All brands are fictional. New style directions come from **mechanism extraction** (the skill's Study route) — transferable craft, never cloned signatures.

## Install

```bash
npx ultimate-design-skill@latest --target codex
npx ultimate-design-skill@latest --target claude-code
npx ultimate-design-skill@latest --target pi-agent
```

Project-scoped, shared, and manual installation: [integrations/README.md](integrations/README.md).

## Use

Describe the outcome, not the process:

```text
Use $ultimate-design to turn this report into a clear visual web page. Create DESIGN.md if needed, make the page, critique it, repair it, and verify the rendered result.
```

Want to lock the important choices together before it builds? Add `--pro`:

```text
$ultimate-design --pro
I need a product site for investors. Align with me on audience, message hierarchy, brand posture, and acceptance criteria before implementing.
```

For multi-domain, high-risk work, ask for **Portable Specialist mode**: an Integrator routes Narrative / Visual / Interaction work orders on a file blackboard and stays the sole final writer. Details: `skill/ultimate-design/references/multi-agent-mode.md`.

## How a run moves

1. **Anchor the request** — original ask, latest overrides, acceptance criteria.
2. **Shape the content** — message hierarchy before layout.
3. **Load only relevant knowledge** — every active concept must change a real decision.
4. **Choose a direction and build** — taste dials, anti-default locks, semantic zone markers.
5. **Critique, repair, verify** — rendered UI audit in a real browser; fix what fails.
6. **Govern** — leave a contract the next agent can continue from.

## Verification is a feature, not a footnote

Visual work gets rendered and reviewed before delivery — the skill ships deterministic tools for it:

```bash
npm run flow-check            # skill flow integrity
npm run okf-graph-check       # knowledge graph consistency
npm run agent-handoff-check   # multi-agent handoff schema
npm run check-integrations    # host integration health
```

The rendered UI audit (`validate_html_visual.mjs`) measures marked semantic zones in a pinned Chromium: horizontal overflow, clipping, occlusion, spacing, and interactive target sizes. The showcase site and all twelve demos pass it with zero failures.

---

## 中文简介

**Ultimate Design 是给 AI Agent 用的设计工作流技能:把设计做出来,也把判断留下来。**

大多数 AI 设计止步于一张"看起来完成"的截图。Ultimate Design 让 Agent 像职业设计师一样工作:先理顺需求和内容,再落成真实制品,对着浏览器渲染结果批判、修复、验证,最后把 `DESIGN.md` 契约留给下一位接手的人。

每次运行留下三件东西:**Request Anchor**(这次要解决什么、给谁用、什么不能丢)、**`DESIGN.md` 契约**(内容顺序、视觉方向、假设与待确认项)、**渲染复查**(真实页面、截图与浏览器实测审计)。

随包携带:35 个知识概念文件(7 大知识域,按需加载、绑定到具体决策)、19 份分支参考(官网、产品界面、Deck、图形印刷、品牌系统、动效审计……)、11 个内置校验脚本(契约校验、知识使用校验、固定版 Chromium 渲染审计、动效契约校验),以及多 Agent 协作的 Portable Specialist 模式。

**[官网展示站](https://aa2246740.github.io/ultimate-design/)由本技能自举完成**:12 个完整案例覆盖 12 种设计语言(瑞士国际主义、静奢极简、工业功能主义、新闻纸编辑、数据叙事、包豪斯几何、新粗野主义、东方编辑感……),每个案例都附带自己的设计契约和可复现的 Prompt,全部通过渲染审计。

安装(三选一):

```bash
npx ultimate-design-skill@latest --target codex
npx ultimate-design-skill@latest --target claude-code
npx ultimate-design-skill@latest --target pi-agent
```

普通用法(说结果,不用背流程):

```text
$ultimate-design 帮我把这份研究做成一个便于阅读的网页。先处理内容和设计方向,再实现、复查并修掉明显问题。
```

关键选择想先对齐再动手,用 `--pro`;多域高风险工作可要求 Portable Specialist 模式。

## License

[MIT](LICENSE)
