---
type: Coverage Map
title: Research Coverage Map
description: Traceability map from the original design research report to this OKF bundle.
tags: [coverage, research, traceability, confidence]
---

# Purpose

Use this concept to audit whether the research packet is represented in the skill and to find the right concept for a rule.

# Coverage Map

| Research area | OKF concept or skill reference | Coverage |
|---|---|---|
| Senior-designer goal and design priority | `methods/senior-design-process.md`, `governance/senior-proxy-checklist.md` | Covered |
| LLM Wiki digestion layer for raw research before OKF promotion | `governance/research-digestion-llm-wiki.md`, `SKILL.md`, `flow_check.py` | Covered as build-time governance |
| Raw research, source summaries, wiki synthesis, OKF candidates, and runtime OKF boundary | `governance/research-digestion-llm-wiki.md`, `design-okf/index.md`, `principles.md` | Covered |
| OKF promotion criteria, do-not-promote rules, coverage protocol, and validation path | `governance/research-digestion-llm-wiki.md`, `governance/research-coverage-map.md`, `flow_check.py` | Covered |
| Existing OKF taxonomy, runtime-layer classification, and single-source-of-truth boundaries | `governance/okf-taxonomy-digestion-map.md`, `design-okf/index.md`, `flow_check.py` | Covered |
| Product problem framing, PM judgment, JTBD, and "problem before solution" | `methods/product-sense.md`, `governance/request-integrity.md` | Covered as conditional product-design lens |
| Product metrics, success signals, guardrails, and validation methods | `methods/product-sense.md`, `quality-gates.md` | Covered for product-oriented design tasks |
| MVP scope, hypothesis testing, and prototype/landing/fake-door validation | `methods/product-sense.md`, `branch-marketing-site.md`, `branch-web-product.md` | Covered as design scope and validation guidance |
| AI product UX risks, trust, fallback, cost, and uncertainty | `methods/product-sense.md`, `production/data-viz-i18n-legal.md`, `digital/accessibility-usability.md` | Covered as conditional AI-product checks |
| Business/user value tradeoffs and deliberate non-goals | `methods/product-sense.md`, `quality-gates.md`, `audit-polish.md` | Covered as critique and quality-gate criteria |
| Commercial PPT and business presentation design | `production/presentation-deck.md`, `branch-presentation.md`, `quality-gates.md` | Covered as conditional presentation branch |
| Deck narrative, conclusion titles, and claim/evidence/action slide model | `production/presentation-deck.md`, `branch-presentation.md` | Covered |
| PPT master/template, font embedding, PDF export, accessibility, and approval package | `production/presentation-deck.md`, `quality-gates.md`, `design-contract.md` | Covered with delivery caveats |
| Design Thinking, Double Diamond, HCD/UCD, Lean UX | `methods/senior-design-process.md` | Covered as operational lenses |
| Visual communication chain: intent, priority, attention, reading, understanding, action | `foundations/visual-communication-hierarchy.md`, `quality-gates.md` | Covered as a foundation coordination layer |
| Information priority: user goal, business goal, decision value, risk, urgency, frequency, context | `foundations/visual-communication-hierarchy.md`, `content/message-model.md` | Covered |
| Message hierarchy vs visual hierarchy | `foundations/visual-communication-hierarchy.md`, `content/message-model.md`, `foundations/visual-hierarchy.md` | Covered with source-of-truth boundaries |
| Attention and reading path: top-down/bottom-up, F/Z/layer-cake/spotted/modular/task-flow patterns | `foundations/visual-communication-hierarchy.md`, `foundations/gestalt-composition.md` | Covered as context-sensitive heuristics |
| Understanding and action: perception, grouping, decoding, mapping, CTA, signifiers, feedback, risk reducers | `foundations/visual-communication-hierarchy.md`, `content/ux-writing.md`, `digital/responsive-interaction.md` | Covered |
| Ethical hierarchy and dark-pattern rejection | `foundations/visual-communication-hierarchy.md`, `quality-gates.md` | Covered |
| Layout, typography, and composition system | `foundations/layout-typography-composition.md`, `quality-gates.md` | Covered as a foundation coordination layer |
| Grid, type area, margins, columns, gutters, baseline, and spacing rhythm | `foundations/layout-typography-composition.md`, `systems/tokens-components.md` | Covered |
| Alignment, optical alignment, visual weight, focal path, and grayscale structure | `foundations/layout-typography-composition.md`, `foundations/gestalt-composition.md`, `foundations/visual-hierarchy.md` | Covered |
| Typography hierarchy, legibility, readability, line height, line length, and type tone | `foundations/layout-typography-composition.md`, `systems/typography-system.md`, `systems/type-personality.md` | Covered |
| Font personality, type art direction, conservative-vs-expressive type decisions, and type roles | `systems/type-personality.md`, `systems/taste-engine.md`, `quality-gates.md`, `design-contract.md` | Covered |
| Chinese typography and mixed Chinese-English typesetting | `foundations/layout-typography-composition.md`, `systems/typography-system.md`, `systems/type-personality.md`, `production/data-viz-i18n-legal.md` | Covered |
| CJK/Latin voice maps, optical pairing, baseline/weight/size checks, numerals, punctuation, and real-content type testing | `systems/type-personality.md`, `systems/typography-system.md`, `quality-gates.md` | Covered |
| Editorial layout and multi-page rhythm | `foundations/layout-typography-composition.md`, `production/graphic-print.md`, `production/presentation-deck.md` | Covered |
| Swiss Style as grid-led method, not style costume | `foundations/layout-typography-composition.md`, `quality-gates.md` | Covered |
| Visual language and style system | `systems/visual-language-style-system.md`, `branch-brand-system.md`, `quality-gates.md` | Covered as system coordination layer |
| Style versus decoration and anti-template aesthetics | `systems/visual-language-style-system.md`, `audit-polish.md`, `quality-gates.md` | Covered |
| Taste Skill operational mechanisms: design read, dials, anti-defaults, layout-family audit, asset credibility, and taste critique | `systems/taste-engine.md`, `quality-gates.md`, `audit-polish.md`, branch references | Covered as adapted runtime OKF, not copied template content |
| Layout variety against card-heavy AI output | `systems/taste-engine.md`, `branch-marketing-site.md`, `branch-presentation.md`, `graphic-print.md`, `quality-gates.md` | Covered |
| Photography, illustration, iconography, symbols, and texture rules | `systems/visual-language-style-system.md`, `branch-brand-system.md`, `graphic-print.md` | Covered |
| Art direction, moodboard-to-rules, do/do-not examples, and cross-medium style guide | `systems/visual-language-style-system.md`, `design-contract.md` | Covered |
| Contextual color/symbol meaning and visual-language ethics | `systems/visual-language-style-system.md`, `systems/color-system.md`, `production/data-viz-i18n-legal.md` | Covered |
| Brand identity, brand image, brand equity, and recognition mechanisms | `systems/brand-identity-media-production.md`, `branch-brand-system.md`, `quality-gates.md` | Covered |
| Logo variants, clear space, minimum size, color/background rules, and misuse examples | `systems/brand-identity-media-production.md`, `branch-brand-system.md`, `quality-gates.md` | Covered |
| Brand guidelines: core, application, production, governance, and do/do-not rules | `systems/brand-identity-media-production.md`, `design-contract.md`, `quality-gates.md` | Covered |
| Design tokens, asset library, naming, delivery package, and DAM-style governance | `systems/brand-identity-media-production.md`, `systems/tokens-components.md`, `design-contract.md` | Covered |
| Screen, print, social, deck, and packaging media delivery | `systems/brand-identity-media-production.md`, `production/graphic-print.md`, `production/presentation-deck.md`, `digital/accessibility-usability.md` | Covered with current-source caveats |
| Packaging dieline, barcode, regulatory, supplier, and proofing checks | `systems/brand-identity-media-production.md`, `production/graphic-print.md`, `production/data-viz-i18n-legal.md` | Covered as production/legal caveat |
| Licensing, asset rights, copyright, trademark, commissioned work, and rights register | `systems/brand-identity-media-production.md`, `production/data-viz-i18n-legal.md`, `quality-gates.md` | Covered as flag-and-record guidance |
| Gestalt principles | `foundations/gestalt-composition.md` | Covered |
| Visual hierarchy | `foundations/visual-hierarchy.md` | Covered |
| Content strategy, user need, and message hierarchy | `content/message-model.md`, `content-model.md` | Covered |
| UX writing, microcopy, voice and tone | `content/ux-writing.md`, `content-model.md` | Covered |
| Component state language | `content/state-language.md`, `content/semantic-binding.md` | Covered |
| Semantic HTML, long text, i18n, and frontend text binding | `content/semantic-binding.md`, `digital/accessibility-usability.md` | Covered |
| Layout, composition, graphic design | `foundations/gestalt-composition.md`, `production/graphic-print.md` | Covered |
| Print caveats | `production/graphic-print.md` | Covered with caveats |
| Color theory and semantic colors | `systems/color-system.md` | Covered; deep palette generation should use project evidence and the selected color posture |
| Typography and responsive readability | `systems/typography-system.md`, `systems/type-personality.md` | Covered |
| WebFont performance, CJK fallback, font loading, font licensing, and deliverable portability | `systems/type-personality.md`, `systems/brand-identity-media-production.md`, `quality-gates.md` | Covered with current-source caveats for licensing/vendor rules |
| Web IA | `foundations/information-architecture.md` | Covered |
| Usability heuristics | `digital/accessibility-usability.md` | Covered |
| Responsive design | `digital/responsive-interaction.md` | Covered |
| WCAG/accessibility | `digital/accessibility-usability.md`, `quality-gates.md` | Covered |
| Token hierarchy | `systems/tokens-components.md`, `tokens-components.md` | Covered |
| Component specification | `systems/tokens-components.md`, `tokens-components.md` | Covered |
| Coding-agent execution rules | `SKILL.md`, `design-contract.md`, branch references | Covered |
| Low-interruption clarification | `SKILL.md` | Covered |
| Requirement drift prevention | `governance/request-integrity.md`, `design-contract.md`, `quality-gates.md`, `audit-polish.md` | Covered |
| Request Anchor runtime state | `governance/request-integrity.md`, `design-contract.md`, `scripts/validate_design_contract.py` | Covered as runtime contract, not temporary OKF |
| Senior proxy metrics | `governance/senior-proxy-checklist.md`, `quality-gates.md` | Covered |
| Design review and QA | `audit-polish.md`, `quality-gates.md` | Covered and now part of the build loop |
| DESIGN.md official definition and Google-compatible core schema | `governance/design-md-standard.md`, `design-contract.md` | Covered |
| DESIGN.md template | `design-contract.md`, `governance/design-md-standard.md` | Covered |
| DESIGN.md agent execution rules and AGENTS.md integration | `governance/design-md-agent-governance.md` | Covered |
| Official token reference syntax and component properties | `governance/design-md-standard.md`, `systems/tokens-components.md` | Covered |
| Machine-verifiable schema and CI | `governance/machine-verification-ci.md`, `scripts/validate_design_contract.py` | Covered |
| Design-to-code governance | `governance/design-to-code-governance.md` | Covered |
| Data visualization, i18n, legal extensions | `production/data-viz-i18n-legal.md` | Covered |

# Known Limits

- The bundle does not prove aesthetic excellence by itself.
- Some standards, framework APIs, and product guidelines may change and require current official sources.
- Print production remains vendor-specific.
- Brand originality and market fit still require user or stakeholder judgment.
- Full confidence requires running real design tasks and reviewing outputs.
