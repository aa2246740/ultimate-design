# Ultimate Design 官网内容定稿

## 内容目标

这是一版从中文出发的官网首页，不再使用英译中的表达。中文页面先把话说顺、说具体；英文页面不是逐字翻译，而是面向英文读者的平行表达。

页面要让第一次接触 Ultimate Design 的人明白：

1. 它不是模板库，也不是“做高级点”的提示词。
2. 它是一套面向 AI Agent 的设计工作流。
3. 它是自洽的 skill：不依赖旧工具链，也不要求外部设计 skill 才能工作。
4. 它用 DESIGN.md 把需求、内容、方向、质量门和复盘记录下来。
5. 它能做网页、PPT、产品 UI、平面、品牌和审查打磨。
6. 它会先 critique and repair，再用真实截图验证。
7. 参考图是可选输入：有就吸收，没有也继续，不默认生成。

## 中文主线

### 第一屏

品牌：Ultimate Design

主张：让 AI 设计从生成，升级成交付。

说明：它不是模板包，也不是一句“高级一点”，更不是依赖旧工具链的拼装器。它把模糊需求变成 DESIGN.md 合同、内容结构、设计方向、真实产物、批判修复和渲染验证。

按钮：

- 看完整流程
- 复制官网 Prompt

模式提示：

- YOLO mode：默认少打扰，先交付一版完整结果。
- --pro mode：需要精细把关时，先把关键选择谈清楚。

### 为什么需要它

标题：AI 设计常翻车，不是因为不会画，而是因为没有过程。

说明：很多页面看上去完整，其实没有回答需求；看上去热闹，其实信息层级乱了。Ultimate Design 先管住问题，再开始做视觉。

问题一：没有合同，设计会一路漂移。

- 任务越长，越容易忘记用户到底要什么。
- 页面做完了，却说不清每一块为什么存在。
- 下个 agent 接手时，只能重新猜风格和规则。

问题二：没有自评，默认审美会自动接管。

- 居中大标题、三张卡片、紫蓝渐变、假截图。
- 文字像翻译，按钮像占位，证据像装饰。
- 最后才看一眼，重叠、贴边和怪换行已经混进成品。

### 它是什么

标题：它不是一个模板库，而是一条设计生产线。

说明：Ultimate Design 把设计拆成四件事：把需求说清楚，把知识按需调出来，把品味和必要性落成规则，把成品拿去验证。它自带这套纪律，不要求用户再安装另一套设计 skill。

四个系统：

- 合同：记录用户诉求、内容模型、视觉系统、组件规则、假设和风险。
- 知识：网页、产品、PPT、平面、品牌和内容策略按任务分支读取，并绑定到具体设计决策和验证方法。
- 品味判断：用 taste dials、必要性判断、反默认锁和版式家族检查，避免 AI 套路感。
- 验证：用真实截图、语义区检查、遮挡采样、动效证据和二次自评，把低级问题拦在交付前。

### 工作流

1. Anchor：把原始需求、最新调整、目标受众、成功标准和非目标写下来，防止越做越偏。
2. Content：先回答用户为什么来、第一屏要懂什么、行动意味着什么，再谈版式。
3. Contract：没有 DESIGN.md 也没关系，agent 会根据上下文建立第一版合同。
4. Direction：确定品牌姿态、色彩承诺、字体性格、信息密度、图像策略、版式模型和必要性判断。
5. Optional References：参考图是可选输入。有图就吸收结构、气质和反参考；没图就继续，不默认生成。
6. Build：做出页面、PPT、图形资产、产品 UI 或品牌系统，而不是只写一段说明。
7. Critique and Repair：交付前先自查有没有跑题、翻译腔、卡片套路、错位、拥挤、奇怪换行、假证明和不必要的装饰。
8. Verify and Govern：保存截图，跑验证，更新合同，让下一位 agent 能接着做。

### 使用 Prompt

普通页面：

```text
$ultimate-design 从零开始帮我设计这个页面。请先定内容和 DESIGN.md；如果我提供参考图，就作为可选输入吸收；没有参考图也继续选择方向。然后实现、critique、修复并验证。
```

专业确认模式：

```text
$ultimate-design --pro
我要设计一个面向投资人的产品官网。请先跟我确认受众、信息层级、品牌姿态、颜色、字体、版式、参考图和验收标准，再开始实现。
```

带参考图：

```text
$ultimate-design
我会提供一张参考图。请只提取它的结构、氛围、色彩和节奏，不要照抄文字或坏排版；如果我没发图，就按内容和上下文继续设计。
```

## English Page

The English page is a parallel version, not a word-for-word translation.

Hero claim: Turn AI design from generation into delivery.

Lead: Ultimate Design is not a template pack, a style preset, or a wrapper around another design skill. It turns a design request into a contract: clarify the message, choose a direction, build the artifact, critique it, repair it, and verify the rendered result.

Core sections:

- Why it exists: AI design fails less from lack of drawing skill, and more from lack of process.
- What it is: It is not a template library. It is a design production line.
- Workflow: Anchor, Content, Contract, Direction, Optional References, Build, Critique and Repair, Verify and Govern.
- New in 0.4: decision-bound OKF, hardened Pro mode, calibrated semantic-zone checks, proof freshness, and purpose-led motion evidence.
- Capabilities: Marketing Sites, Product UI, PPT / Deck, Graphics / Social, Brand Systems, Audit / Polish.
- Proof: DESIGN.md, Reference Assets, Rendered Screenshots, Visual Validation, Review Log.

## 交互要求

- 顶部提供中 / EN 切换。
- 默认中文。
- `index-en.html` 打开英文版本。
- 复制按钮按当前语言复制对应 prompt。
- 参考图只作为可选输入，不绑定生成图流程。
- 页面必须通过桌面和移动端渲染验证。
