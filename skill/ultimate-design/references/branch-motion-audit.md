# Motion Audit Branch

Use this branch for repo- or product-area-wide audits of existing animation: inventory, consistency, accessibility, performance, standardization, or repair. Keep one new animation, static design, and ordinary final polish on their normal creation branches.

This branch is the single source of truth for the project motion-audit process and **Evidence Gate**. Load `design-okf/systems/motion-language.md` for purpose, exposure, choreography, accessibility, and performance judgment. Load `design-okf/systems/motion-contract.md` only after a repair is selected or an existing interaction contract must be browser-validated. Keep duration, easing, and spring rules in those motion sources.

## Modes

- **YOLO:** define a bounded scope, audit it, repair confirmed P0/P1 and easy P2 findings, replay changed interactions, and record the remainder. Keep repository-wide improvement bounded by the agreed scope.
- **Pro:** present vetted findings and proposed scope before changing high-impact motion behavior, shared tokens, navigation transitions, or brand motion.
- **Audit only:** keep source unchanged and produce a compact report. Create implementation plans only for user-selected deferred work or when persistence materially helps handoff.

## Evidence Gate

Use one status per claim and promote it only when the required evidence exists:

| Status | Required evidence | Allowed conclusion |
|---|---|---|
| **Candidate** | Static inventory or source match with `file:line` | Inspect this location; assign no severity. |
| **Vetted** | Candidate reread in code context and checked against documented intent or the design contract | Describe the mismatch and confidence; runtime-dependent claims remain unverified. |
| **Confirmed** | Code proves the defect, or representative runtime evidence proves perceptual behavior; performance claims include a trace, frame observation, or reproducible load condition | Enter the repair queue and assign severity. |
| **Unverified** | Relevant claim cannot reach its required runtime or measurement evidence | Record the blocker and risk without presenting the claim as fact. |

Classify interaction frequency as observed telemetry, documented product knowledge, or an assumption. Derive product personality from `DESIGN.md`, brand rules, representative UI, or user context. Use rendered or interaction evidence for feel, origin, continuity, interruption, and reduced-motion claims whenever they depend on perception.

## Workflow

| Step | Action | Completion criterion |
|---|---|---|
| 1. Scope | Name routes, components, platforms, input methods, states, exclusions, and YOLO, Pro, or audit-only mode. | Every in-scope surface and material exclusion is explicit. |
| 2. Recon | Read `DESIGN.md`, motion tokens, component primitives, animation libraries, representative interactions, prior decisions, and test/build commands. | The motion surface map names the stack, libraries, tokens, intent sources, and runnable commands. |
| 3. Inventory | Run `python3 scripts/inventory_motion.py <project-root>` when useful, then inspect the highest-signal files. | The inventory report exists, high-signal files were sampled, and every static match remains a Candidate without severity. |
| 4. Baseline | Replay representative high-frequency, occasional, gesture-driven, and expressive interactions at normal and reduced-motion settings. Capture slow-motion or frame evidence where timing matters. | Each representative interaction has baseline evidence or a named runtime blocker. |
| 5. Audit | Check the categories below against the contract and active OKF concepts. | Every scoped interaction maps to applicable categories and an Evidence Gate status. |
| 6. Vet | Reread each cited location, replay when required, remove duplicates and intentional exceptions, and separate repairs from opportunities. | Each reported claim is Vetted, Confirmed, or Unverified with evidence and confidence. |
| 7. Prioritize | Rank Confirmed findings by user/accessibility impact, exposure, confidence, implementation risk, and effort. | Severity, confidence, leverage, and effort are assigned; opportunities remain a separate list. |
| 8. Act | Repair the bounded YOLO scope, obtain Pro agreement, or finish the audit-only report. | The selected mode's promised output is complete, and only Confirmed findings enter repair. |
| 9. Replay | Run the same baseline interactions, reduced-motion setting, and relevant performance evidence before and after repair. | Changed interactions have comparable replay evidence; unresolved or unverified claims remain explicit. |
| 10. Govern | Update Motion Strategy, Motion Audit Summary, shared tokens, deliberate exceptions, review log, and unresolved risks in `DESIGN.md`. | The contract records decisions, evidence paths, accepted exceptions, and remaining risks. |

## Audit Categories

- **Purpose and exposure:** Does motion communicate feedback, continuity, hierarchy, navigation, story, or brand? Does repeated exposure add delay or fatigue?
- **Response and continuity:** Does feedback begin at the right response point? Do origin, destination, direction, and object identity remain coherent?
- **Interruption and input:** Can rapid, reversible, or gesture-driven motion retarget from its live presentation state without blocking input?
- **Timing and easing:** Do duration and curve fit distance, size, exposure, platform, and scene? Treat `ease-in`, durations above 300 ms, pure fades, `scale(0)`, and stagger values as context-dependent review signals, never automatic failures.
- **Accessibility and safety:** Does reduced motion remain useful? Are essential meaning, controls, focus, flashing, auto-motion, zoom, rotation, parallax, and depth effects handled safely?
- **Performance:** Are animated properties, concurrency, main-thread work, paint, layout, filters, media, and scroll handlers acceptable under representative load?
- **Cohesion and tokens:** Do shared durations, curves, springs, origins, and motion roles form one system rather than near-duplicate local values?
- **Opportunities:** List only a few evidence-backed places where motion would prevent a jarring change or explain spatial continuity. Keep these separate and lower priority than repairs by default.

## Finding And Plan Format

Use one row per reported claim:

| Status | Severity | Confidence | Category | Location | Evidence | Finding | Repair | Verification |
|---|---|---|---|---|---|---|---|---|

Assign severity only to Confirmed findings. Candidate and Unverified rows remain outside the repair queue; Vetted rows enter it only after the required confirmation evidence exists.

- **P0:** prevents operation, hides essential content, creates a serious accessibility/safety failure, or causes severe reproducible instability.
- **P1:** high-exposure sluggishness, broken continuity, non-interruptible direct manipulation, missing reduced-motion behavior, or measured performance failure.
- **P2:** noticeable inconsistency, local timing/origin weakness, token drift, or low-risk repair.
- **P3:** optional polish or additive opportunity.

When a separate plan is useful, include the source commit, exact scope, current code excerpt, target behavior, repo conventions, ordered edits, protected boundaries, mechanical checks, runtime replay, reduced-motion check, and done condition. Refresh the plan when source drift changes its assumptions.

## Persistence

- Keep the durable summary and selected decisions in `DESIGN.md` under `Motion Audit Summary`.
- Create `motion-audit/report.md` only for a large audit, audit-only delivery, or multi-agent handoff.
- Create `motion-plans/NNN-short-name.md` only for selected deferred work. Keep grep matches and work already repaired in the same run in the report or trace.
- Keep screenshots, recordings, traces, and machine reports in the project's existing evidence location when one exists; otherwise use a clearly named temporary or review directory and record the path.

## Done Criteria

A motion audit is done when scope and assumptions are explicit, the motion surface was inventoried, runnable interactions have a baseline or a recorded blocker, every claim passed the Evidence Gate or remains explicitly Unverified, performance claims have measured evidence, corrective findings are separated from opportunities, selected repairs were replayed in normal and reduced-motion states, no unresolved P0/P1 remains inside the agreed repair scope, and `DESIGN.md` records decisions and remaining risks.
