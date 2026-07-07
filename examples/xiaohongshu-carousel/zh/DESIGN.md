---
version: alpha
name: ultimate-design-xhs-chinese-carousel
description: 中文语境的小红书 9 图轮播，用于介绍 Ultimate Design skill。

colors:
  primary: "#101010"
  secondary: "#f7f0e6"
  tertiary: "#2457ff"
  neutral: "#fffaf0"
  surface: "#f7f0e6"
  on-surface: "#101010"
  error: "#ff3b30"

typography:
  headline-lg:
    fontFamily: "PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans CJK SC, Source Han Sans SC, sans-serif"
    fontSize: "76px-112px"
    fontWeight: "800-900"
    lineHeight: "1.02-1.08"
  body-md:
    fontFamily: "PingFang SC, Hiragino Sans GB, Microsoft YaHei, Noto Sans CJK SC, Source Han Sans SC, sans-serif"
    fontSize: "23px-36px"
    fontWeight: "560-900"
    lineHeight: "1.28-1.45"
  label-md:
    fontFamily: "SF Mono, Menlo, Consolas, Noto Sans Mono CJK SC, monospace"
    fontSize: "18px-23px"
    fontWeight: "800-900"
    lineHeight: "1.0-1.2"

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 8px
  full: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 54px

components:
  carousel-frame:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
---

# Design System

## Overview

这是 Ultimate Design skill 的中文语境小红书轮播版。它不是英文版直译，而是按中文内容消费习惯重写：封面先戳痛点，中间解释机制，最后给出适用场景和行动理由。

目标读者是中文 AI 工具、设计、产品、前端和 Agent 用户。他们需要快速判断：这个 skill 是什么、为什么不是模板、它到底靠什么让 AI 做出更稳定的设计结果。

## Colors

沿用 Ultimate Design 系列识别色：黑、暖纸、蓝、红、荧光绿、粉、青、紫、琥珀。每页保留底部九色条，保证系列感；每页主色和构图变化，避免九页同模板换字。

## Typography

中文优先。主体使用系统黑体族保证清晰度和跨设备可用性；部分页面用宋体作为观点型、知识型语气的显示字。等宽字体只用于标签、流程、页码和技术词。

规则：

- 标题可以强，但正文必须能读。
- 中文正文采用现代段落系统：不首行缩进，靠段距和模块分组。
- 中英文混排保留空格：如 `AI 设计`、`DESIGN.md`、`Taste Engine`。
- 字距保持 `0`，不靠负字距制造紧张感。
- 系统字体优先，不引入外部字体文件，避免授权和体积风险。

## Layout

输出规格为 1080 × 1440，3:4 竖版轮播。版心安全区 54px，底部预留 154px 放页脚和色条。

九页版式角色：

- 01 痛点封面：模板指纹。
- 02 核心公式：规则、品味、内容、证据。
- 03 设计合同：DESIGN.md 作为单一事实源。
- 04 内容先行：中文阅读路径。
- 05 反模板机制：先命名套路。
- 06 字体人格：中文字体选择。
- 07 OKF 路由：按需调用知识。
- 08 挑刺修复：验证不是走过场。
- 09 总结 CTA：适用场景与价值。

## Elevation & Depth

使用硬边框、硬阴影、斜色块、网格和色块制造图文海报感。避免柔和玻璃拟态、过度圆角和默认阴影。

## Shapes

主要容器圆角不超过 8px。胶囊只用于局部标签，不作为默认装饰。

## Components

- Topbar：主题标签和页码。
- Palette strip：系列识别和跨页连续性。
- Footer note：页脚元信息和概念说明。
- Panel / Node / Step：根据每页叙事任务变化，不形成单一模板。
- Fake stack / screen blocks：作为概念图解，不伪装真实产品截图。

## Do's and Don'ts

Do:

- 用中文语境表达，不做硬翻译。
- 每页只有一个主观点，但允许有足够解释。
- 保持中文标题的钩子感和正文的可读性。
- 让版式服务叙事角色。
- 导出后检查 9 张图的真实渲染。

Don't:

- 不把英文版逐句翻译回来。
- 不用同一张卡片模板刷 9 页。
- 不用假截图、假证据、假引用。
- 不让装饰压住正文和底部信息。
- 不宣称这是印刷级最终文件。

## Agent Execution Rules

- 编辑中文文案后必须重新渲染全部 9 张图。
- 任何新颜色、新字体、新组件都要写回本文件。
- 保持 1080 × 1440，除非用户明确更改平台规格。
- 修复 contact sheet 中发现的重叠、贴边、截断和阅读顺序问题。

## Request Anchor

- Original user request: 按照中文语境设计中文版。
- Latest user override: 中文语境，不是英文直译；延续小红书轮播版本。
- Deliverable: 9 张 1080 × 1440 中文 PNG，源 HTML，DESIGN.md，README，contact sheet，verification report，zip 包。
- Primary audience: 中文 AI 设计、Agent、前端、产品和内容创作者。
- Core job to be done: 让读者快速理解 Ultimate Design 是什么、解决什么问题、为什么不是模板型 skill、怎么保证设计质量。
- Success criteria: 中文表达自然；信息比纯口号更充分；9 页版式有变化但系列统一；导出尺寸正确；视觉检查通过；可发送飞书。
- Non-goals: 不做英文版逐句翻译；不做真实 PPTX；不做官网页面。
- Must preserve: DESIGN.md、Request Anchor、Content Model、Taste Engine、Type Personality、OKF 路由、挑刺修复、渲染验证这些真实机制。
- Validation must check against: 9 张图、1080 × 1440、中文可读、底部安全区、无明显重叠裁切。

## Content Model

- User intent: 看完知道 Ultimate Design 是一套让 AI 做设计更稳定、更少模板感的工作流。
- Message hierarchy:
  1. AI 设计 Skill 很容易出现模板指纹。
  2. 规则只能兜底，品味、内容和证据决定上限。
  3. Ultimate Design 用 DESIGN.md 和 Request Anchor 锚定需求。
  4. 它把内容、中文排版、字体人格、OKF 路由、挑刺修复、渲染验证串成流程。
  5. 它适合页面、PPT、海报、报告、产品 UI 和品牌系统。
- Voice and tone: 中文小红书知识帖，直接、有判断、不过度吹捧。
- Terminology rules: `DESIGN.md`、`Request Anchor`、`Taste Engine`、`OKF` 保留英文/缩写并解释语境。
- Content risks: 不夸大为“必然 10 年设计师水准”；强调流程和可验证质量。

## Taste Signature

- Design read: 中文 AI 工具/设计知识型轮播，手机阅读，目标是解释机制并建立信任。
- Taste dials: visual variance 8, information density 6, motion depth 0, brand distinction 8, type expressiveness 8, experiment risk 6.
- Category defaults avoided: 同模板卡片、泛 AI 渐变、玻璃高级感、假截图、只有大字没有机制。
- Layout families or slide archetypes: 痛点海报、四象限矩阵、设计合同蓝图、中文阅读路径、反模板规则墙、字体标本、知识路由图、验证面板、总结 CTA。
- Visual memory feature: 强中文标题 + 九色条 + 每页不同结构。
- Type personality: 黑体为主，理性清晰；宋体用于观点型显示；等宽用于系统感标签。
- Asset/reference policy: 纯 CSS 图形和文字，不使用第三方图片、字体文件、Logo 或假证明。
- Anti-default locks: 不默认圆角卡片，不默认玻璃渐变，不假装真实产品截图，不重复同一版式。
- Intentional exceptions: 第 9 页使用强渐变作为收束页的发布感，不作为全套默认风格。

## Graphic Or Print Specs

- Size: 1080 × 1440 px.
- Aspect ratio: 3:4 vertical.
- Color mode: screen RGB / sRGB-oriented export.
- Bleed: none.
- Safe area: 54 px frame plus 154 px bottom reservation.
- Resolution: exact pixel screenshots.
- Export format: PNG frames plus zip bundle.
- Font handling: system fonts only.
- Image/font/logo license notes: no external assets bundled.

## Review Log

- 2026-07-07: Bootstrapped Chinese-context carousel from the English version's intent, not its literal wording. Rewrote all page copy for Chinese social reading, added Chinese typography rules, and preserved Ultimate Design mechanism claims.
