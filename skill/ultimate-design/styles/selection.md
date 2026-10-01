# Choosing a style

Read the row for the scene, pick one option per dimension from **Use**, and never pick from **Avoid** without a written reason in `DESIGN.md`. When two scenes overlap (a bakery's social card), take the voice from the subject (bakery) and the canvas from the medium (xhs). Presets named in a row are the nearest worked examples.

## Scenes

| Scene | Type | Color | Surface | Density | Layout | Presets | Centerpiece options | Avoid |
|-------|------|-------|---------|---------|--------|---------|---------------------|-------|
| **Local shop, food, café, bakery** 本地小店·餐饮 | T02, T18, T05, T14 | C01, C06, C07 | S01, S02 | regular | L03, L04 | P01, P13 | Today's menu as a price ledger; bake or opening schedule; booking windows; how-to-find-us with real landmarks | C05 dark console, gradients, stat strips, stock-photo hero |
| **Developer tool, infrastructure, API** 开发者工具 | T03, T13, T06 | C02, C05 | S01, S04 | regular | L03 | P02, P04 | Real request/response pair; config diff; log excerpt with the failure it catches; latency chart with the before/after | purple/blue gradient, glowing orbs, three icon feature cards, fake logo wall |
| **SaaS product UI, settings, admin** 产品界面·后台 | T12, T06, T20 | C02 | S03, S01 | dense | L05 | P08 | The working table, form, or queue itself, with real states (empty, error, loading, selected) | sticky phone action bars (`.cta-bar` is for pitch pages only), marketing hero, display type, decorative color, cards inside cards |
| **Data report, dashboard, weekly review** 报告·看板·周报 | T13, T15, T17 | C09, C02 (C05 for night ops) | S01, S02 | regular, dense | L01, L05 | P07, P04 | The conclusion sentence, then the chart that proves it with the story series highlighted; a decision list | KPI tiles without comparison, rainbow series, dual axes, 3D, donut for more than three parts |
| **Editorial, long read, newsletter** 内容·长文 | T01, T17, T05, T15 | C01, C09, C10 | S01, S05 | regular, airy | L01, L02 | P03, P07 | The lede and one key figure or pull quote; margin notes; a real table | card grids of articles with identical thumbnails, eyebrow on every section |
| **Event, launch, exhibition, conference** 活动·发布·展览 | T04, T16, T07, T11 | C03, C08, C06 | S02, S04 | airy, regular | L06, L03 | P09, P14, P06 | Date and venue as the second-largest thing; agenda timeline; ticket tiers with what each includes | countdown clocks as decoration, speaker grids without roles, confetti |
| **Culture, tea, heritage, Chinese brand** 文化·茶·非遗 | T09, T05 | C07, C01 | S05, S01 | airy | L02, L01 | P05 | The process in its real steps and times; a single object described closely; a seasonal calendar | pop colors, rounded pills, emoji, gold gradients as "premium" |
| **Hotel, beauty, jewelry, studio** 精品·静奢 | T19, T10 | C10, C01, C07 | S05 | airy | L02 | P12 | Real photography when supplied; the offer in one sentence with price and dates; a room or product spec sheet | glassmorphism, busy grids, discount badges |
| **Kids, pets, desserts, family services** 亲子·宠物·社区服务 | T08, T14, T06 | C04, C08, C06 | S06, S02 | regular | L03, L04 | P11 | Schedule or booking slots; what to bring checklist; price list per size or age | dark themes, clinical blue, tiny type |
| **Fintech, mobility, marketplace** 消费科技 | T20, T06 | C02, C03 | S03 | regular | L03 | P08 | The calculator or quote with real inputs; fee table; timeline of a transaction | 3D coins, gradient cards, hero phone mockups with fake UI |
| **Public institution, education, NGO** 公共机构·教育 | T04, T01, T15 | C03, C02, C09 | S01 | regular | L01 | P14, P07 | Who is eligible, what to bring, where and when; a step list with the office hours | stock smiling-people photos, vague mission statements |
| **Sports, outdoor, logistics, industry** 运动·户外·工业 | T11, T01, T04 | C07, C03 | S02, S01 | regular | L06, L03 | P10 | Route, schedule, or capacity table; conditions right now; a spec sheet | neon gradients, glossy 3D |
| **Portfolio, personal site** 作品集·个人 | T19, T10, T02, T14 | C01, C10 | S05 | airy | L01, L02 | P12, P03 | The work itself, large, with one line on the problem each solved | skill bars, percentage circles, testimonials carousel |
| **Social cards, carousel (xhs, square, story)** 社交卡片·小红书 | from the subject's row; T07, T08, T14, T09 are common | C08, C04, C06, C01 | S02, S04, S06 | canvas | canvas | P06, P11 | Cover: one promise + one anchor (number, photo, shape). Inner cards: one idea each. Last card: the part people save | more than one idea per card, text under the canvas minimum, emoji bullets, stock icons |
| **Digital poster** 电子海报 | from the subject's row | C03, C08, C01 | S02, S04 | canvas | canvas | P14, P06 | Title from across the room, date second-largest, facts in rows | long prose, four font sizes of equal weight |
| **Slides (HTML deck)** 幻灯片 | T01, T04, T13, T17 | C01, C02, C09, C03 | S01, S02 | canvas | canvas | P03, P07, P09 | Each title is the slide's conclusion as a sentence; the body is the evidence; one highlighted series per chart | bullet walls, topic-label titles ("Background", "Results"), clip art |

## Layouts

| Id | Name | Shape | Kit |
|----|------|-------|-----|
| L01 | 编辑长栏 Editorial column | One reading column at `--measure` with a side column for notes, figures, and metadata; sections divided by rules | `.grid-edit`, `.prose`, `.note` |
| L02 | 居中留白 Quiet center | Narrow centered column, generous vertical rhythm, few elements per screen | `.wrap` + `max-width: var(--measure)` |
| L03 | 左文右物 Claim and artifact | Claim, facts, and action on one side; the centerpiece artifact on the other; stacks on phones with the claim first | `.hero`, `.grid-split`, `.artifact` |
| L04 | 目录网格 Index grid | A catalog of real items (menu, products, rooms, people) where each cell carries its own facts, not an icon and a slogan | `.grid-cols`, `.price-list`, `.plans` |
| L05 | 工作台 Workbench | Side navigation plus a dense work area; tables and forms are the page | `.shell`, `.side-nav`, `.grid-dash`, `.table` |
| L06 | 大字色带 Poster bands | Full-width bands of oversized type and alternating grounds; one message per band | `.section--band`, `.t-display` |

Fixed canvases (xhs, square, story, poster, slide) use `kit/canvas.css`: `.cv-head` / `.cv-body` / `.cv-foot` regions, with `--low`, `--center`, `--spread`, `--fill` bodies.

## Moves

A move is a signature detail. Pick two or three that come from the subject; a move that could appear on any page is decoration.

| Id | Move | Use when | How |
|----|------|----------|-----|
| M01 | Mono metadata | Versions, timestamps, IDs, specs are real content | `var(--font-mono)`, `.num`, small size |
| M02 | Rule-led sections | Editorial or civic pages that need order without boxes | heavy top rule + small label per section |
| M03 | Price ledger | Anything sold by item | `.price-list` with leader dots and tabular prices |
| M04 | Oversized type | One word or number carries the message | `.t-display`, crop at the container edge on purpose |
| M05 | Live data artifact | The product produces data | real chart or table in `.artifact`, `UDChart` |
| M06 | Wayfinding numerals | A real sequence exists: agenda, floors, steps | numbers that match the sequence; never decorative 01/02/03 |
| M07 | Handwritten note | A person runs the place | one annotation in `var(--font-accent)` beside the centerpiece |
| M08 | Margin notes | Explanations that should not interrupt reading | `.note` in the L01 side column |
| M09 | Status semantics | States matter (orders, incidents, availability) | `--positive/--warning/--danger` with `-soft` fills, only on states |
| M10 | Stamp or sticker | One offer or deadline needs to jump | `.cv-stamp` or `.tag--accent`, once per page |
| M11 | Pull quote | One sentence carries the argument | `.quote`, display font |
| M12 | Time bar | Hours, bake times, booking windows | `.windows`, `.week`, `UDChart.windows` |
| M13 | Vertical label | Chinese heritage or literary voice | one `writing-mode: vertical-rl` label, never body text |
| M14 | Color-block alternation | Committed brand or campaign color | alternate `.section` and `.section--band` |
| M15 | Footnoted evidence | Claims need sources | numbered notes, captions with source and date |
| M16 | Dense table | Comparison or operations data | `.table`, sticky header, tabular numbers, `.table--stack` on phones |
| M17 | Designed states | Product UI | empty, loading, error, and success states written and styled |
| M18 | Photography lead | Real photos are supplied | full-bleed photo, text in its quiet area; never a placeholder hero |
| M19 | Spec sheet | Hardware, rooms, products with measurable facts | two-column definition list with units |
| M20 | Hairline frame | Quiet luxury, galleries | thin inset frame and small caps labels, lots of air |

## Checks before you generate

- Could the page belong to a different business if you swapped the name? Then the seed, the type, or the centerpiece is generic; change the one that came from habit.
- Is the seed color the default blue, indigo, or purple? Only keep it if the brand or subject genuinely is that color.
- Does the density match the reader's task? Dashboards and admin are dense; culture and luxury are airy; everything else starts regular.
- Is the canvas right for where it will be seen? A phone feed needs xhs or square with large type, not a web page screenshot.
