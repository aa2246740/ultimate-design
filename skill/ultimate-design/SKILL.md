---
name: ultimate-design
description: "Contract-driven design workflow for durable visual work. Use for: DESIGN.md contracts, product UI, marketing pages, presentation decks, graphic/print assets, brand systems, content/UX writing, design critique, and rendered verification."
---

# Ultimate Design

Work like a professional designer-builder: frame the problem, shape the content, choose a visual system with reasons, make the artifact, critique the result, verify rendered output, and preserve the design contract for the next agent. Do not use this skill for purely functional frontend changes with no visual, UX, brand, layout, or design-system impact unless the user asks for design judgment.

The leading word for this skill is **contract**: every design choice should either come from the existing design contract or create/update it. The contract is usually `DESIGN.md`; for larger projects it may include `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, or equivalent files. A missing `DESIGN.md` is normal, not a blocker.

Treat content as the meaning layer of the contract. Content decides what the artifact must communicate; UI decides how users act; visual design directs attention; frontend implementation preserves semantics, accessibility, responsiveness, and consistency.

## Interaction Modes

Default to **YOLO mode**: do not interview the user by default. Infer from the prompt, existing files, screenshots, brand assets, code, and product context first. Ask only for blockers, make safe assumptions, and produce a complete first pass with contract, artifact, critique, repair, and verification.

Use **Pro mode** when the user includes `--pro`, asks to work "like a real pro", or explicitly wants to confirm details before execution. In Pro mode, build consensus before making high-impact choices: audience, deliverable, message hierarchy, content scope, brand posture, taste dials, color commitment, type personality, layout model, imagery/assets, interaction/export constraints, and acceptance criteria. Ask in compact batches, avoid open-ended interviews, skip harmless details, update the Request Anchor after each decision, and proceed only when the next design choice is sufficiently agreed.

After the user answers Pro mode questions or supplies a clear decision bundle, the next turn is a delivery turn, not another discovery turn. Freeze a **Decision Snapshot** in the Request Anchor and move into bounded execution. Do not re-open agreed choices, ask more questions, or expand into broad research unless a true blocker appears.

### Pro Post-Consensus Delivery Gate

When Pro mode has reached consensus, follow this order:

1. Record a compact Request Anchor and Decision Snapshot. In monitored eval mode, create or update `.ultimate-design/runs/<timestamp>-<slug>.md` immediately with every phase listed as `pending`, then update statuses as work proceeds.
2. If the requested deliverable is a screenshotable artifact, write the visible artifact skeleton as the next major file operation after the initial trace: `index.html` for an HTML page, `deck.html` for an HTML deck, an SVG/HTML/CSS graphic for a graphic, or the requested project file for app UI. The skeleton must already contain real user-facing content, responsive structure, and `data-ud-check` semantic zones for major regions. Do this before reading optional references, writing a long `DESIGN.md`, or doing extended internal planning. A rough but real skeleton is better than no artifact; refine it after it exists.
3. Load only the selected branch reference, `content-model.md`, `design-contract.md`, `visual-verification.md`, `quality-gates.md`, and at most two directly relevant OKF concept files. Do not open the OKF index, broad foundation files, or adjacent concepts unless the artifact cannot be made without them.
4. Create or update a compact `DESIGN.md` contract after the visible artifact exists, then refine both. Do not spend the turn producing only a long `DESIGN.md`.
5. Critique, repair, second-critique, verify, govern, and deliver. In monitored eval mode, a pass requires artifact, trace, critique/repair evidence, rendered verification evidence, and a governed contract.

Hard stop: in monitored eval mode, a run that creates only `DESIGN.md` is a failed run. When a visible artifact is requested, writing `DESIGN.md` before any artifact file is also a failed execution order. If time or context becomes tight, prioritize the visible artifact, trace, critique/repair, and verification over a longer contract. Run validators against existing artifacts; do not run validator help or read validator source unless debugging the validator itself.

For monitored evals, update the run trace after each completed phase instead of leaving the table for the end. Before final delivery, no applicable phase may remain `pending`; use `pass`, `blocked`, or `not-run` with evidence. Run only one visual verification path unless it fails. For HTML work, prefer `scripts/validate_html_visual.mjs` when available; do not run duplicate screenshot or static validators after it passes. If `DESIGN.md` exists, run `scripts/validate_design_contract.py` with strict options when practical and fix reported errors. Scan CSS for forbidden typography such as negative `letter-spacing` and repair it unless an explicit brand rule justifies it. After Govern passes, stop expanding and send a short final response immediately.

In monitored eval mode, write a machine-readable completion seal before the final chat response:

```text
.ultimate-design/runs/<timestamp>-<slug>.complete.json
```

The seal contains `status`, `trace`, `artifacts`, `verification`, `remaining_risks`, and `final_summary`. Write it only after all applicable phases are non-`pending`, the visible artifact exists, validators have run or are marked `not-run` with reasons, the contract has been governed, and the final summary is ready. If a development watchdog terminates the run after this seal appears, that still counts as a completed monitored workflow because the evidence is already on disk.

Classify missing information before asking:

- **Blocker:** proceeding would make the result unsafe, legally risky, production-invalid, or pointed at the wrong audience. Ask once.
- **Risky but defaultable:** choose a conservative default, proceed, and record the assumption.
- **Harmless:** proceed without mentioning it unless it affects the final artifact.

Typical blockers:

- The business/user goal cannot be inferred.
- The user asks for print-ready output but print size, bleed, color mode, or printer specs are missing.
- Brand assets, logo usage, likeness rights, image rights, or font licensing matter.
- The requested platform, stack, or deliverable format is impossible to infer.
- The user asks for an exact redesign of an unknown existing brand/product without source material.

If the missing detail is not a blocker, do not interrupt the user in YOLO mode. Record it under `Open Questions` or `Assumptions` when persistence matters.

## Operating Loop

1. **Orient.** Determine the surface: product UI, marketing website, presentation/PPT deck, graphic/print collateral, brand system, audit/polish, or design-system work. Read any existing `DESIGN.md`, design-system files, CSS/theme/tokens, representative components, screenshots, slide masters/templates, and relevant assets.
   Completion: you can state the user, task, surface, constraints, existing visual language, and what artifact you are expected to change or create.

2. **Complete the brief.** Fill the smallest useful design brief: audience, primary task, success criteria, brand tone, platform, accessibility target, technical stack, assets, optional user-supplied reference images, and output format. For presentation decks, also state audience role, meeting or reading mode, decision or action requested, duration, delivery format, brand/template constraints, and compliance risks. For product, feature, flow, dashboard, onboarding, pricing, or validation-page work, also state the product problem, user situation, desired behavior or outcome, success signal, and main tradeoff. Reference images are optional input: use them when supplied; in Pro mode ask once in a compact way whether the user has any; in YOLO mode do not block or generate one by default when none is supplied. Create a compact **Request Anchor** with the original user request, latest user override, deliverable, primary audience, core job to be done, success criteria, non-goals, must-preserve constraints, and validation checks. Use existing evidence before asking.
   Completion: blockers were asked once, assumptions were written down and safe enough to proceed, and the Request Anchor is available in `DESIGN.md`, a compact review note, or the run trace.

3. **Build the content contract.** Define the user intent, message hierarchy, primary action meaning, voice/tone, terminology rules, state-language rules, and content risks before choosing layout or styling. Content may shape IA and component needs, but it should not directly prescribe layout mechanics.
   Completion: the artifact can answer what this is, why it matters, what the user can do next, what happens after action, and which words/states must stay consistent.

4. **Bootstrap the contract.** For any non-trivial design artifact, create or update `DESIGN.md` by default. Use a compact contract or review note only for one-off, low-risk artifacts such as a tiny copy, color, or spacing adjustment. Create the contract from the user's prompt, repository context, product copy, existing UI/code, assets, and safe defaults. For UI/web work, make root `DESIGN.md` Google-compatible when practical: YAML front matter holds official token fields and Markdown holds rationale and agent-readable constraints. Do not ask the user to supply `DESIGN.md`. Mark inferred items as assumptions and unresolved items as open questions. In Pro post-consensus or monitored eval mode, bootstrap only the minimum contract needed to build and verify the artifact; when a visible artifact is requested, create the artifact skeleton before expanding or polishing `DESIGN.md`.
   Completion: the contract contains enough Google-compatible token, project, user, content-model, IA, visual-system, component, quality-gate, assumption, and review-log material for another agent to continue.

5. **Load the branch reference.** Read only the references that match the work:
   - `references/principles.md` when bootstrapping `DESIGN.md` from zero, when no existing design system exists, when the user asks for senior/professional design judgment, or when the design direction lacks a clear rationale. This is a router into `references/design-okf/index.md`; read the OKF index, then only the relevant concept files.
   - `references/design-okf/methods/product-sense.md` when the task is product UI, feature design, dashboard, onboarding, pricing, AI product UX, PRD/MVP/prototype, growth or validation landing page, or when the design depends on product strategy, metrics, prioritization, business/user outcome, or whether the requested solution solves the right problem.
   - `references/design-okf/governance/request-integrity.md` when the task is long, content-heavy, multi-file, likely to exceed short-term attention, or when final validation must prove the artifact still answers the user's original request.
   - `references/design-okf/systems/taste-engine.md` when creating a visible artifact with style freedom, when the user asks for taste, originality, anti-AI-slop, stronger color/type/layout personality, or when marketing/PPT/graphic/brand work risks becoming generic cards and default gradients.
   - `references/content-model.md` when the artifact has meaningful text, UX writing, report visualization, dense content, forms, component states, localization, or when bootstrapping `DESIGN.md`.
   - `references/branch-presentation.md` for PowerPoint, Keynote, Google Slides, business presentations, investor/board/executive decks, sales or pitch decks, training decks, read-alone decks, slide redesigns, and PPTX/PDF deck delivery.
   - `references/branch-web-product.md` for dashboards, app UI, product flows, components, forms, tables, and frontend implementation.
   - `references/branch-marketing-site.md` for landing pages, marketing sites, content sites, portfolios, campaign pages, and website redesigns.
   - `references/graphic-print.md` for posters, social graphics, banners, brand collateral, packaging, brochures, print, and image-generation art direction.
   - `references/branch-brand-system.md` for brand systems, visual identity, logo usage rules, art direction, palette/type systems, and reusable brand guidance.
   - `references/audit-polish.md` for critique, redesign diagnosis, visual polish, anti-AI-slop passes, and design QA without building a new artifact.
   - `references/tokens-components.md` when creating or changing tokens, component systems, UI kits, or shared design rules.
   - `references/design-contract.md` when creating or updating `DESIGN.md`. It routes to `references/design-okf/governance/design-md-standard.md` and `references/design-okf/governance/design-md-agent-governance.md` for Google-compatible schema, token references, official section order, agent rules, and extension boundaries.
   - `references/visual-verification.md` before final delivery for screenshotable visual artifacts: HTML pages/decks, product UI, dashboards, presentation previews, PDFs, graphics, and exported images. It defines the required rendered-output pass and optional HTML semantic-zone checks.
   - `references/monitoring.md` only for development/testing evidence: when the user asks for proof, evals, repeatability, traceability, or monitoring. Do not load it during ordinary design work.
   - `references/quality-gates.md` before final delivery, always.
   Completion: every active branch reference has been applied to the design decisions, not merely skimmed. Do not expand into adjacent OKF concepts once the branch decision is already supported unless the artifact depends on that concept. In Pro post-consensus or monitored eval mode, extra OKF reading is a failure mode when it delays the artifact.

6. **Choose a direction.** Commit to one primary design strategy. Produce alternatives only when the user asked for variants or when two directions are genuinely plausible and cheap to compare. Name the chosen strategy in practical terms: message hierarchy, information density, taste dials, color commitment, color posture, type personality, layout model, layout-family budget, imagery style, motion level, interaction model, anti-default locks, and the intended visual memory feature.
   Completion: the design direction explains why this solution fits this user and task better than common category reflexes, and which defaults it rejects or intentionally keeps.

7. **Make the artifact.** Depending on the request, implement the UI, create the graphic asset, create or redesign the presentation deck, write the design spec, produce the prompt/art direction, or update the design system. Reuse existing project patterns and tokens first. For generated HTML or app UI, mark major semantic zones during implementation with `data-ud-check`, such as navigation, hero, primary content, card grid, chart area, slide, modal, form, and footer, so verification can inspect layout intent rather than raw DOM boxes only. For one-off graphics or quick audits, a compact assumptions/review note may be enough. In Pro post-consensus or monitored eval mode, create a minimum complete artifact before optional research, long rationale, or polish; for HTML this means `index.html` exists before a full contract draft.
   Completion: the artifact is usable without the user filling in obvious missing states, breakpoints, labels, or component behavior.

8. **Critique and repair.** Before final delivery, critique the artifact against the Request Anchor, brief, product/problem framing when relevant, content contract, design contract, taste dials and anti-default locks when relevant, selected OKF concepts, branch reference, and quality gates. Score or rank findings by user impact, business impact, accessibility risk, brand/theme fit, requirement drift, taste drift, and implementation effort. Fix all P0/P1 findings and easy P2 findings before proceeding; if a finding cannot be fixed in scope, record it with the reason. Treat failed contract validation, negative default tracking, un-updated monitoring trace, missing rendered evidence, and obvious generic card/default-gradient output as repair items when they apply.
   Completion: a second pass finds no unresolved P0/P1 issues, no unresolved mismatch with the Request Anchor, and remaining P2/P3 issues are either fixed or explicitly accepted as follow-up risk.

9. **Verify.** Run the relevant quality gates: Request Anchor fit, content clarity, UX writing, visual hierarchy, contrast, responsive behavior, keyboard/focus, reduced motion, content states, text zoom/reflow, performance risk, slide title/reading order, export stability, print preflight, licensing notes, and contract consistency. For visual artifacts, do not rely only on DOM/canvas bounds or one sampled screenshot. Render every final page, slide, frame, or key responsive state; save screenshots/previews; inspect the full set for overlaps, cramped semantic spacing, hidden controls, clipping, awkward wraps, and density mismatch. For generated HTML, run `scripts/validate_html_visual.mjs` against the semantic zones created during implementation when Playwright/Chrome is available.
   Completion: failures are fixed, or explicitly reported as not run with the reason; user-specific success criteria from the Request Anchor were checked; visual artifacts have rendered evidence for every user-visible page/slide/state that was practical to inspect. Run bundled validators by path when possible, after the artifact exists; read validator source or run validator help only when editing or debugging the validator itself. Do not run multiple equivalent visual validators after one has produced passing rendered evidence.

10. **Govern.** Update the contract with changed content model, tokens, component rules, page/screen specs, assumptions, open questions, and review log entries. Keep the contract lean. Create `design-system/AGENT-RULES.md`, `TOKENS.md`, `COMPONENTS.md`, or similar files only for reusable systems, multi-screen products, brand systems, or multi-agent continuity.
   Completion: the next agent can continue from the contract without reverse-engineering your design choices. In monitored eval mode, the run trace has no applicable `pending` statuses before final response.

## Defaults

Use these defaults when evidence is absent and the assumption is low risk:

- Accessibility: WCAG 2.2 AA for web; prefer 44 by 44 CSS px touch targets for comfort even though WCAG AA has a smaller minimum with exceptions.
- Responsive checks: 320, 375, 768, 1024, 1280, and 1440 px when practical.
- Type: start body text at 16 px or equivalent; cap long-form English lines around 65 to 75 characters and Chinese around 25 to 40 characters.
- Spacing: use a 4 or 8 point scale; avoid undocumented one-off values.
- Tokens: primitive, semantic, then component tokens. Components should consume semantic or component tokens, not raw primitives.
- Motion: purposeful, interruptible, transform/opacity first, with `prefers-reduced-motion` support.
- Theme: choose light/dark from the physical use scene, not category habit.
- Print: treat 3 mm bleed and 300 PPI as common placeholders, never as final production specs without printer confirmation.

## Professional Bar

Do not claim the artifact proves "10 years of design experience." Professional quality is observable behavior, not an identity claim:

- Frame the real problem before styling the surface.
- Shape content structure, message hierarchy, and state language before layout.
- Choose color, type, density, imagery, and motion from the audience, medium, scene, and brand posture.
- Preserve accessibility, responsiveness, production constraints, rights, and export stability.
- Critique and repair requirement drift, visual hierarchy, copy clarity, theme fit, spacing, overlaps, awkward wraps, and AI-default aesthetics before delivery.
- Leave a contract that explains what changed, why it changed, what assumptions remain, and how the next agent should continue.

The bundled OKF knowledge is descriptive context, not runtime truth. It can guide decisions and contract writing, but it does not override rendered output, accessibility tools, tests, print/vendor requirements, or user review.

## Development/Eval Monitoring

Monitoring is an optional add-on, not part of normal design execution. Use it only when the user asks to prove the workflow, run evals, debug the skill, or collect repeatable evidence. In that mode, read `references/monitoring.md` and use the bundled scripts before or after a test run. For ordinary page, UI, graphic, or polish requests, keep the workflow lightweight and do not create a trace unless it materially helps the deliverable.

## Research Ingestion

Research ingestion is a development task, not ordinary design execution. When absorbing deep research, building a wiki-like synthesis layer, auditing coverage, or promoting knowledge into OKF, read `references/design-okf/governance/research-digestion-llm-wiki.md`. Keep raw sources and long wiki notes out of runtime references; promote only stable, operational, checkable knowledge into OKF, then update the index, router, quality gates, coverage map, and flow proof when affected.

## Use Of Other Design Skills

If `ui-ux-pro-max` is available and the project is new, ambiguous, or needs style/color/type/stack recommendations, query its design-system or domain search before choosing the direction. Treat its output as evidence, not as a substitute for judgment.

If `impeccable` is available and the work touches frontend craft, apply its register split, anti-slop checks, accessibility discipline, typography limits, motion guidance, and browser verification expectations.

If a real `.pptx`, `.ppt`, Google Slides, or PowerPoint-compatible file must be created or edited, use the available Presentations capability for file operations and use this skill for deck strategy, visual system, slide-level critique, and delivery quality gates.

Use current official sources when a standard, browser behavior, framework API, platform guideline, or legal/printing requirement could have changed.

## Final Response

Keep the user-facing closeout short. Include:

- What was created or changed.
- The main design direction and any important assumptions.
- How the result maps back to the user's original request when the task was long, content-heavy, or drift-prone.
- What verification ran, and what could not be verified.
- Where the deliverable or contract lives.
- If development/eval monitoring was explicitly used, where the evidence report or run trace lives.

Do not dump the full checklist unless the user asks for it.
