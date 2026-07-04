---
type: Design System Concept
title: Taste Engine
description: Turns design taste into operational choices: design read, taste dials, anti-default bans, layout-family audit, asset credibility, and final taste critique.
tags: [taste, anti-slop, art-direction, layout-variety, visual-assets, critique]
---

# Purpose

Use this concept when an artifact has visible style freedom and could otherwise become generic: marketing sites, portfolios, campaign pages, presentation decks, social graphics, posters, report visualizations, brand systems, redesigns, and any critique where the result feels stiff, templated, or "AI-generated."

This concept does not define one house style. It converts taste into repeatable operating constraints. The output may be Swiss, editorial, brutalist, quiet, playful, institutional, luxury, dense, or restrained, but the direction must be chosen from the brief and then enforced.

# Core Model

Taste is not a template. Treat it as a chain of commitments:

```text
design read
-> taste dials
-> anti-default locks
-> layout-family budget
-> asset credibility
-> taste critique
-> contract record
```

The design may be surprising, but the process should be predictable.

# Design Read

Before choosing style, read the brief through these questions:

- Artifact: page, app surface, deck, social frame, poster, report, brand system, or audit.
- Audience: buyer, executive, operator, investor, reader, fan, student, internal team, or public.
- Scene: where and how it is consumed: phone, meeting room, desktop work session, print, feed, kiosk, outdoor, email, or deck review.
- Job: sell, explain, reassure, persuade, compare, teach, align, announce, signal identity, or drive action.
- Brand posture: established, experimental, institutional, premium, technical, handmade, urgent, playful, editorial, or utilitarian.
- Category defaults: the common look this artifact must avoid or intentionally use.
- Evidence assets: real screenshots, product photos, charts, copy, brand assets, data, quotes, or generated assets.
- Risk tolerance: conservative, memorable, campaign-only, prototype, or experimental.

If the brief is weak, infer safe defaults and record them. Ask only when the wrong scene, audience, or rights assumption would invalidate the deliverable.

# Taste Dials

Set dials after the design read. Record them in `DESIGN.md` or the run trace when taste is a major part of the work.

| Dial | 1 | 5 | 10 |
|---|---|---|---|
| Visual variance | Symmetric, conventional, low surprise | Offset rhythm, varied section shapes | Asymmetric, editorial, risky composition |
| Information density | Airy, one idea per view | Balanced scanning and detail | Dense, cockpit, analyst/report mode |
| Motion depth | Static | Purposeful entry/hover/scroll feedback | Cinematic or physics-led, with reduced-motion fallback |
| Brand distinction | Generic category fit | Recognizable motif or system rule | Ownable visual behavior across media |
| Experiment risk | Safe production | Memorable but controlled | Prototype/campaign-level exploration |

Dial guidance:

- Keep product/admin UI lower variance and higher clarity unless the brand or context demands expression.
- Let marketing, brand, campaign, social, and pitch surfaces use more variance when the message needs memory.
- Decks can vary slide archetypes without making every slide theatrical.
- Motion above a modest level must actually be implemented and must honor reduced motion.
- High variance must collapse to simple, stable mobile structures.

# Branch Presets

Use these as starting points, then adjust to the brief:

| Branch | Visual variance | Information density | Motion depth | Brand distinction | Experiment risk |
|---|---:|---:|---:|---:|---:|
| Product UI/dashboard | 2-5 | 5-9 | 1-4 | 2-6 | 1-4 |
| Marketing/portfolio site | 5-8 | 3-6 | 2-7 | 5-9 | 3-7 |
| Executive/business deck | 3-6 | 4-8 | 0-2 | 3-7 | 1-4 |
| Pitch/campaign deck | 5-8 | 3-6 | 0-3 | 6-9 | 3-7 |
| Social/poster/key visual | 6-9 | 2-6 | 0-5 | 6-10 | 4-8 |
| Report visualization | 3-6 | 6-9 | 0-3 | 3-7 | 2-5 |
| Brand system | 5-9 | 3-7 | 1-5 | 8-10 | 4-8 |

# Anti-Default Locks

Name the defaults being rejected. Do not merely say "make it premium" or "make it creative."

Common defaults to reject unless the brief explicitly justifies them:

- One centered hero followed by repeated equal card grids.
- AI-purple or category-blue gradients used as generic excitement.
- Glass panels, soft glows, or oversized rounded cards on every section.
- Fake product screenshots built from decorative rectangles.
- Text-only "minimalism" when the artifact needs evidence, product truth, or atmosphere.
- Decorative pills, dots, badges, and labels that carry no semantic state.
- Stock-like images that could represent any competitor.
- Beige/brass/espresso luxury defaults for every premium consumer brief.
- Endless split-image/text zigzags.
- Identical slide or social-frame compositions repeated with new words only.
- Generic names, fake quotes, fake logos, and invented proof when real proof is absent.

Anti-defaults are not universal bans. They are locks against lazy first choices. If a locked pattern fits the brief, record the reason and execute it deliberately.

# Layout-Family Audit

A layout family is a recognizable composition pattern: centered hero, split hero, asymmetric editorial grid, bento, timeline, comparison table, quote wall, full-bleed image, chart-led slide, process diagram, statement slide, matrix, annotated screenshot, modular list, map, or typographic poster.

Use the audit before final delivery:

- Multi-section pages with six or more sections should use at least four layout families unless the design intentionally needs strict repetition.
- Do not repeat the same family in adjacent sections more than twice.
- Avoid using cards as the default container for every idea; use scale, alignment, dividers, image, table, chart, or whitespace when elevation does not carry meaning.
- Decks should vary slide archetypes by narrative job: claim, evidence, comparison, process, decision, quote, data, appendix, transition.
- Social nine-frame or carousel work should vary composition by message role, not only swap text inside the same frame.
- Reports should combine diagrams, tables, callouts, charts, annotations, and editorial text blocks instead of only card stacks.
- If the artifact is intentionally systematic, record the repetition rule and the one place where the rhythm breaks for emphasis.

# Asset Credibility

Visual assets must either prove, clarify, or create the world of the artifact.

Prefer in this order:

1. Real product, user, place, data, screenshot, diagram, or brand asset when truth matters.
2. Generated bitmap image or illustration when the brief needs mood, campaign world, abstraction, or a missing scene.
3. Purpose-built SVG, icon, chart, or diagram when precision or system reuse matters.
4. Explicit placeholder slots only when no truthful asset can be created or used in scope.

Do not fill missing assets with decorative SVG blobs, fake UI panels, random stock, or CSS-only "screenshots." If assets are missing, leave named slots and explain what assets are needed.

# Reference Extraction

References should change rules, not be copied as surface.

When using references, extract:

- Composition behavior.
- Color posture and surface-area ratio.
- Type personality and spacing rhythm.
- Image crop, light, and material logic.
- Interaction or motion principle.
- What not to copy.

Do not imitate a reference's logo, protected identity, exact layout, trademarked assets, or signature work unless the user owns or supplied it.

# Taste Critique

Ask these before delivery or after a user says the work feels stiff:

1. What category default did this avoid?
2. What is the strongest visual memory after removing the logo?
3. Which layout families were used, and where did the rhythm intentionally change?
4. Which dial choices explain the color, type, density, imagery, and motion?
5. Which asset proves or expresses the idea rather than decorating it?
6. What still looks like AI filler: equal cards, fake screenshots, generic badges, vague proof, stock imagery, over-rounded panels, or default gradients?
7. Does the design still solve the Request Anchor, or did taste drift away from the user's core job?

Fix failed answers before final delivery when the artifact is meant to be polished or public-facing.

# Contract Fields

For durable work, record a compact Taste Signature:

- Design read:
- Taste dials:
- Category defaults avoided:
- Layout families or slide archetypes:
- Visual memory feature:
- Asset/reference policy:
- Anti-default locks:
- Intentional exceptions:

Keep this compact. It is a continuation aid, not a manifesto.

# Done Check

This concept is applied when another agent can answer:

1. Which taste dials were chosen and why?
2. Which defaults were rejected, and which were intentionally allowed?
3. Which layout families or slide archetypes are present?
4. Which visual asset or system rule gives the artifact memory?
5. Which checks prevent the result from becoming generic card-based AI output?
6. Where are the decisions recorded so the next agent can continue?

# Source Notes

This concept generalizes public anti-slop and design-direction patterns observed in Taste Skill's docs and skill files, plus this bundle's existing visual-language, layout, brand, presentation, and audit concepts. It is an adapted operating model, not copied template content.
