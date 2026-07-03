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
| Product problem framing, PM judgment, JTBD, and "problem before solution" | `methods/product-sense.md`, `governance/request-integrity.md` | Covered as conditional product-design lens |
| Product metrics, success signals, guardrails, and validation methods | `methods/product-sense.md`, `quality-gates.md` | Covered for product-oriented design tasks |
| MVP scope, hypothesis testing, and prototype/landing/fake-door validation | `methods/product-sense.md`, `branch-marketing-site.md`, `branch-web-product.md` | Covered as design scope and validation guidance |
| AI product UX risks, trust, fallback, cost, and uncertainty | `methods/product-sense.md`, `production/data-viz-i18n-legal.md`, `digital/accessibility-usability.md` | Covered as conditional AI-product checks |
| Business/user value tradeoffs and deliberate non-goals | `methods/product-sense.md`, `quality-gates.md`, `audit-polish.md` | Covered as critique and quality-gate criteria |
| Commercial PPT and business presentation design | `production/presentation-deck.md`, `branch-presentation.md`, `quality-gates.md` | Covered as conditional presentation branch |
| Deck narrative, conclusion titles, and claim/evidence/action slide model | `production/presentation-deck.md`, `branch-presentation.md` | Covered |
| PPT master/template, font embedding, PDF export, accessibility, and approval package | `production/presentation-deck.md`, `quality-gates.md`, `design-contract.md` | Covered with delivery caveats |
| Design Thinking, Double Diamond, HCD/UCD, Lean UX | `methods/senior-design-process.md` | Covered as operational lenses |
| Gestalt principles | `foundations/gestalt-composition.md` | Covered |
| Visual hierarchy | `foundations/visual-hierarchy.md` | Covered |
| Content strategy, user need, and message hierarchy | `content/message-model.md`, `content-model.md` | Covered |
| UX writing, microcopy, voice and tone | `content/ux-writing.md`, `content-model.md` | Covered |
| Component state language | `content/state-language.md`, `content/semantic-binding.md` | Covered |
| Semantic HTML, long text, i18n, and frontend text binding | `content/semantic-binding.md`, `digital/accessibility-usability.md` | Covered |
| Layout, composition, graphic design | `foundations/gestalt-composition.md`, `production/graphic-print.md` | Covered |
| Print caveats | `production/graphic-print.md` | Covered with caveats |
| Color theory and semantic colors | `systems/color-system.md` | Covered, but deep palette generation may still use `ui-ux-pro-max` or project evidence |
| Typography and responsive readability | `systems/typography-system.md` | Covered |
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
