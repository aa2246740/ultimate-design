# Ultimate Design

[中文](README.md) · [English](README.en.md)

[![npm](https://img.shields.io/npm/v/ultimate-design-skill)](https://www.npmjs.com/package/ultimate-design-skill)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![OKF BundleDex](https://bundledex.net/static-badge.svg)](https://bundledex.net)

**Build the design. Keep the judgment.**

An OKF design workflow skill for coding agents: pin the request, write a `DESIGN.md` contract, build the artifact, critique it, and check the rendered result in a browser before handoff.

## Look at the work first

The public face is the showcase the skill built:

**https://aa2246740.github.io/ultimate-design/**

Twelve complete demos. Each one opens its own `DESIGN.md`.

![Official homepage](docs/screenshots/site-home.png)

*https://aa2246740.github.io/ultimate-design/ — the live homepage in Chrome. The bar says Ultimate Design; below it are the title, hero, and five-stage card.*

![Demo gallery](docs/screenshots/site-gallery.png)

*The same live site, scrolled to `#gallery`. The first row is the real Finlytics, 山声茶事, and TaskFlow cards — not a second site.*

![Demo plus contract](docs/screenshots/demo-plus-contract.png)

*Left: the 山声茶事 page at `…/demos/teahouse/`. Right: that demo's `DESIGN.md` (what the gallery "看契约" / contract link opens). `…/demos/teahouse/DESIGN.md` is 404 on GitHub Pages, so the contract is the repo file, not another site.*

![Contract close-up](docs/screenshots/demo-contract.png)

*The same `DESIGN.md` close-up: `docs/demos/teahouse/DESIGN.md`, tokens next to the work.*

![Home to demo](docs/screenshots/site-to-demo.gif)

*From the official homepage, click 山声茶事 → 查看页面, and land on `…/demos/teahouse/`. Same origin: `aa2246740.github.io`.*

## Install

```bash
npx ultimate-design-skill@latest --target codex
npx ultimate-design-skill@latest --target claude-code
npx ultimate-design-skill@latest --target pi-agent
```

Project-scoped, shared, and manual installation: [integrations/README.md](integrations/README.md).

## The twelve demos

Every demo below is a complete, self-contained page. Open it, copy the prompt that produced it, and read its contract — [all twelve in the gallery](https://aa2246740.github.io/ultimate-design/#gallery).

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

All brands are fictional. The newer styles come from the skill's Study route, which extracts transferable mechanisms from strong reference work without copying any site's signature.

## What a run leaves behind

- **Request Anchor** — what this run must solve, for whom, and what must not be lost.
- **`DESIGN.md` contract** — tokens, direction, assumptions, and open questions, written so the next agent (or human) can continue without reverse-engineering.
- **Rendered review** — the real page, screenshots, and browser-measured audits.

## What's inside

| Capability | Details |
|---|---|
| **Operational design knowledge** | 35 concept files across 7 domains — layout, typography, color systems, motion language, content models, accessibility, governance. A concept is loaded on demand and stays active only while it changes a concrete decision. |
| **19 branch playbooks** | Marketing sites, product UI, presentation decks, graphic/print, brand systems, motion audits, reference study, audit & polish, and more. |
| **11 bundled validators & tools** | Contract validation, OKF-usage validation, a pinned-Chromium **rendered UI audit** (overflow, clipping, occlusion, target sizes), motion-contract validation, agent-handoff checks. |
| **4 task routes** | Build / Audit / Redesign / Study. Audit and Study stop at findings instead of rebuilding what already works. |
| **Multi-agent native** | Portable Specialist mode: an Integrator routes work orders, specialists return packets, one writer owns the final artifact. Ships with the templates. |
| **12 complete demos** | Twelve pages in twelve deliberately different design languages, each designed end-to-end by an agent running this skill, each with its own contract. |

## Use

Describe the outcome you want:

```text
Use $ultimate-design to turn this report into a clear visual web page. Create DESIGN.md if needed, make the page, critique it, repair it, and verify the rendered result.
```

To settle the important choices together before it builds, add `--pro`:

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

## Built-in verification

Visual work gets rendered and reviewed before delivery. The skill ships deterministic tools for it:

```bash
npm run flow-check            # skill flow integrity
npm run okf-graph-check       # knowledge graph consistency
npm run agent-handoff-check   # multi-agent handoff schema
npm run check-integrations    # host integration health
```

The rendered UI audit (`validate_html_visual.mjs`) measures marked semantic zones in a pinned Chromium: horizontal overflow, clipping, occlusion, spacing, and interactive target sizes. The showcase site and all twelve demos pass it with zero failures.

## License

[MIT](LICENSE)
