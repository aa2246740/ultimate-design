# Ultimate Design 官网内容

## 这页要完成什么

让第一次见到 Ultimate Design 的人，在一两分钟内知道三件事：

1. 它不只生成一个看起来完整的页面；它把需求、内容、设计判断和复核过程留下来。
2. 用户不需要先准备 `DESIGN.md`；Agent 会从已有材料和上下文做出第一版。
3. 默认可以直接做；想共同决定关键选择时，再使用 `--pro`。

不把它写成“万能设计师”或“高级提示词”。不拿其他 skill 当陪衬。不承诺不可验证的设计水平。

## 叙事顺序

### 第一屏

品牌：Ultimate Design

主张：把设计做出来，也把判断留下来。

说明：收到一段模糊需求时，先把目标和内容理顺；页面做完后，再看真实结果，修掉跑题、错位和含糊的表达。最后留下下一位 Agent 能接着用的记录。

动作：

- 看它怎么工作
- 复制起步 Prompt

模式：

- 默认：先做出一版完整结果。
- `--pro`：关键选择先对齐，再开始做。

### 为什么需要它

标题：一张页面，常常只完成了一半。

说明：画面做出来以后，真正的问题才露出来：需求在中途变了，内容没讲清，下一位接手的人不知道哪些是刻意选择。

三个具体问题：

- 原始诉求被后续细节盖住了。
- 内容和版式一起开工，重要的话没有位置。
- 交付只剩截图，没人知道为什么这样取舍。

### 它留下什么

标题：每一次设计，都留下能继续使用的东西。

三个对象：

- `Request Anchor`：这次到底要解决什么，谁来用，什么不能丢。
- `DESIGN.md`：内容顺序、视觉方向、假设和待确认项。
- Rendered review：真实页面、截图和复核结果。

### 工作方式

标题：先把事情说清，再把画面做对。

五步：

1. 读需求：保留原始诉求、最新调整和验收标准。
2. 理内容：确定先让人看懂什么，哪些话必须准确。
3. 定方向：选择合适的色彩、字体、密度、版式和参考策略。
4. 做成品：落到网页、产品界面、PPT、图形或品牌材料。
5. 回看交付：检查真实输出，修问题，补上下一位能读懂的记录。

### 适用的工作

- 官网、营销页和内容页
- 产品界面、表单、Dashboard、流程
- HTML Deck、汇报和培训材料
- 海报、社媒图、报告封面、信息图
- 品牌规则与已有页面的审查打磨

### 怎么开始

普通模式的提示词要短，表达结果，不要把流程背给用户：

```text
$ultimate-design 帮我把这份研究做成一个便于阅读的网页。先处理内容和设计方向，再实现、复查并修掉明显问题。
```

`--pro` 只用于关键选择确实需要共同决定的工作：

```text
$ultimate-design --pro
我要做一个面向投资人的产品官网。先和我确定受众、信息重点、品牌气质和验收标准，再开始实现。
```

### 交付时看什么

标题：交出去的，不只有一个链接。

- 需求和取舍写在 `DESIGN.md`。
- 参考资料有来源和用途。
- 页面、幻灯片或图形按实际尺寸检查过。
- 未解决的风险被如实写下。

## 文案规则

- 中文从中文的判断顺序出发；英文是独立的平行表达，不逐句翻译。
- 用具体对象和动作替代“体系、赋能、升级、重要、专业、品质”等抽象评价。
- 不使用“不是……而是……”作为整页骨架；不用“首先、其次、最后、综上所述”撑结构。
- 每段至少交代一个事实、动作、限制或可见结果；没有新增信息的句子删掉。
- 不编造案例、数字、客户或结果。没有证据的主张就缩小。
- 保留正常的句长和语气变化，但不为了“去 AI 味”故意写得散乱。

## English Page

The English page is a parallel expression, not a sentence-by-sentence translation.

Hero claim: Build the design. Keep the judgment.

Lead: Ultimate Design helps an Agent turn a vague ask into a clear brief, a real artifact, and a record another person or Agent can continue from. It checks the rendered result before handoff.

The English version should be plain, specific, and useful. Avoid “transform,” “elevate,” “empower,” “seamless,” “world-class,” and generic contrast formulas.

## Interaction Requirements

- Chinese is the default; the top switch changes the whole page to English.
- The copy button copies the prompt in the active language.
- The reference image remains optional and is not presented as a mandatory step.
- Desktop and mobile must both show a clean reading path; no section should compete with the hero for attention.
