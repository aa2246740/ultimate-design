---
type: Governance Concept
title: OKF Taxonomy And Digestion Map
description: Maintainer-facing map of the existing OKF bundle by runtime layer, branch role, digestion status, and single-source-of-truth boundary.
tags: [okf, taxonomy, digestion, governance, single-source-of-truth]
---

# Purpose

Use this concept when auditing whether the existing OKF bundle has been digested, classified, and kept out of duplicate wiki/runtime forms.

This is a maintainer view. Ordinary design runs should use `index.md`, `principles.md`, branch references, and selected OKF concepts instead of loading this file.

# Digestion Status

The existing OKF bundle is already promoted runtime knowledge, not raw research. Treat it as the current curated output of prior research digestion.

Do not create duplicate LLM Wiki pages for every existing OKF concept. That would create two competing sources of truth. If retrospective analysis is needed, create source summaries, gap notes, or synthesis notes outside runtime, then update the relevant OKF concept in place.

# Runtime Taxonomy

| Layer | Runtime role | Current concepts | Load pattern |
|---|---|---|---|
| Methods | Task approach and senior/product judgment | `methods/senior-design-process.md`, `methods/product-sense.md` | Load when the work needs process, product framing, or senior design rationale. |
| Foundations | General visual communication principles | `foundations/visual-communication-hierarchy.md`, `foundations/layout-typography-composition.md`, `foundations/information-architecture.md`, `foundations/gestalt-composition.md`, `foundations/visual-hierarchy.md` | Load when the artifact depends on hierarchy, layout, reading path, composition, IA, or typography. |
| Content | Meaning, UX writing, state language, semantic binding | `content/message-model.md`, `content/ux-writing.md`, `content/state-language.md`, `content/semantic-binding.md` | Load before styling when words, report logic, forms, states, localization, or semantic frontend behavior matter. |
| Systems | Durable design systems and visual identity mechanics | `systems/brand-identity-media-production.md`, `systems/visual-language-style-system.md`, `systems/taste-engine.md`, `systems/motion-language.md`, `systems/color-system.md`, `systems/typography-system.md`, `systems/type-personality.md`, `systems/tokens-components.md` | Load when creating or changing reusable visual language, taste constraints, motion language, brand identity, color/type/tokens, font personality, or cross-media systems. |
| Digital | Web/app implementation quality | `digital/accessibility-usability.md`, `digital/responsive-interaction.md` | Load for frontend/product UI, responsive behavior, interaction states, accessibility, and usability checks. |
| Production | Medium-specific output and delivery constraints | `production/presentation-deck.md`, `production/graphic-print.md`, `production/data-viz-i18n-legal.md` | Load for decks, print/graphic assets, data visualization, localization, legal, licensing, and export/production caveats. |
| Governance | Runtime integrity, contracts, verification, research ingestion, and coverage | `governance/request-integrity.md`, `governance/design-md-standard.md`, `governance/design-md-agent-governance.md`, `governance/design-to-code-governance.md`, `governance/machine-verification-ci.md`, `governance/senior-proxy-checklist.md`, `governance/research-digestion-llm-wiki.md`, `governance/research-coverage-map.md`, `governance/okf-taxonomy-digestion-map.md` | Load for contract rules, validation, skill development, research absorption, flow proof, and coverage audits. |

# Source-Of-Truth Rules

- `SKILL.md` is the execution loop and branch router into references.
- `references/principles.md` is the high-level OKF router for professional/senior rationale and from-zero contracts.
- `references/design-okf/index.md` is the OKF bundle table of contents.
- Each OKF concept owns its own rules, caveats, and Done Check.
- Branch references own surface routing and practical task behavior.
- `quality-gates.md` owns final delivery checks.
- `research-coverage-map.md` owns research-to-OKF traceability.
- `research-digestion-llm-wiki.md` owns future raw-research digestion workflow.
- This file owns only the taxonomy and existing-OKF digestion status.

# Existing OKF Audit

The current OKF bundle is considered digested when:

1. Every concept has front matter with `type`.
2. Every concept belongs to one runtime layer.
3. The concept appears in `index.md`.
4. Relevant branch references or `principles.md` can route to it.
5. The concept has a clear purpose and operational boundary.
6. Major research areas appear in `research-coverage-map.md`.
7. Flow proof checks the concept when it is central to the skill's promised behavior.
8. Volatile claims are caveated or delegated to current official/vendor/legal sources.

# Gap Handling

When a gap appears:

- Missing concept: create a new OKF concept only if the knowledge is reusable, operational, checkable, and branch-relevant.
- Duplicate concept: merge into the stronger source of truth and update routers.
- Weak routing: sharpen `principles.md` or the branch reference before adding more files.
- Overloaded concept: split only when a branch needs to load part of it without the rest.
- Raw research residue: move examples, source archaeology, and weak-confidence notes to wiki digestion instead of runtime OKF.

# Done Check

This taxonomy pass is done when another maintainer can answer:

1. Which runtime layer owns each OKF concept?
2. Which file is the single source of truth for each kind of rule?
3. Which OKF concepts are runtime knowledge and which files are development-only governance?
4. Where should a new research finding be promoted, routed, or left as wiki-only?
5. Which validation proves the taxonomy, routing, and coverage did not drift?
