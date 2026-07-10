# Quality Gates

Read this before final delivery. Apply this core gate, the selected branch's Done Criteria, and the Done Checks of active OKF concepts. Branch files own medium-specific rules; this file owns the cross-branch delivery bar.

## Request Fit

- The artifact matches the Request Anchor's deliverable, audience, core job, success criteria, latest override, must-preserve constraints, and non-goals.
- The primary user-facing view supports the intended task or message.
- Source facts, data, copy, assets, brand constraints, and behavior are preserved unless a recorded decision changes them.
- A mismatch is fixed or reported with the reason. Requirement drift that changes the deliverable or core job is P0/P1.

## OKF Evidence

- Preflight happened before direction and artifact decisions, not as post-rationalization.
- Active references, constraints, deliberate exceptions, and verification hooks are recorded.
- Every active `design-okf/` concept has an `OKF Decision Bindings` row: `Reference | Decision | Artifact target | Verification`.
- A concept that changed no decision is removed from Active references.
- Major content, layout, visual-system, interaction, motion, and production choices trace to the Request Anchor, existing contract, or a binding.
- In monitored mode, `scripts/validate_okf_usage.py` passes.

## Content And Hierarchy

- The artifact makes clear what this is, why it matters, what the user can do next, and what happens after action.
- Message order follows the user's decision or task path rather than internal organization.
- Voice, terminology, CTAs, labels, states, trust, risk, and help content follow the content contract.
- Primary, secondary, and tertiary information are visually distinct through size, weight, position, spacing, contrast, or rhythm.
- Critical meaning is not carried only by color, image, motion, hover, tooltip, truncation, or hidden text.

## Necessary Taste

- The design read, type personality, layout-family budget, visual memory feature, and category defaults kept or rejected are explicit when style freedom exists.
- The artifact does not fall back to repeated generic cards, default gradients, vague premium styling, or decoration that cannot survive the Delete Test.
- Major choices pass necessity, replacement, move, justification, care, material honesty, and scene-fit tests when polished judgment matters.
- Delight emerges from clarity, agency, craft, and coherence; it is not an added flourish that competes with the task.
- At least one owned visual feature remains recognizable without the logo when distinction matters.

## Typography

- Body, UI, data, state, and legal text remain readable; Expressive type is reserved for places where memory or voice helps.
- Hierarchy uses deliberate size, weight, line-height, space, position, color, and family choices without stacking every emphasis lever.
- Letter spacing is `0` by default; nonzero or negative tracking requires a brand rule, optical-size need, logo/wordmark need, or recorded typographic reason.
- Mixed Chinese/English work checks optical size, weight, baseline, punctuation, numerals, spacing, coverage, fallback, and rights with real content.
- Text zoom, long words, long Chinese strings, localization expansion, and fallback fonts do not break layout.
- WebFont loading, CJK payload, `font-display`, portability, and license status are recorded when relevant.

## Accessibility And Interaction

- Semantic structure, keyboard access, visible focus, accessible names, labels, errors, status feedback, contrast, reflow, and reduced motion are checked where applicable.
- Touch and pointer targets are usable for the intended device and interaction frequency.
- Loading, empty, error, partial, permission, success, disabled, confirmation, and undo states are covered when the workflow can reach them.
- Frequent actions stay immediate and quiet. Direct-manipulation interactions track input continuously, remain interruptible, and preserve recovery or cancellation.
- Color, motion, sound, or haptics never carry the only copy of critical meaning.

## Rendered Integrity

- Every final page, slide, frame, export, or key responsive state practical to inspect has rendered evidence. Generated HTML also has Rendered UI Audit evidence when browser measurement is available.
- The full set was inspected for overlap, occlusion, clipping, awkward wraps, density, hidden controls, misleading depth, and first/last-frame problems.
- Generated HTML uses sparse `data-ud-check` markers at one intentional hierarchy level.
- `scripts/validate_html_visual.mjs` has no active fail findings when browser measurement is available.
- Intentional overlaps use documented `data-ud-allow` allowances with reason, owner, and expiry rather than disappearing from evidence.
- A passing DOM or bounds check never substitutes for screenshot/contact-sheet inspection of the final pixels.

## Motion

Apply this section only when meaningful motion is active:

- Static communication and operation work before animation.
- Every nontrivial animation has one primary purpose and a frequency-appropriate motion budget.
- Direction, origin, duration/easing, interruption, input mapping, and reduced-motion behavior fit the interaction and scene.
- Gesture-driven motion starts from the live presentation state, can be redirected, and hands off velocity or boundary resistance when physical continuity requires it.
- Scroll remains user-controlled; large zoom, rotation, parallax, pinning, blur, and cinematic sequences earn their attention cost.
- Transform/opacity are preferred for predictable performance; other properties require measured justification.
- `scripts/validate_motion_contract.mjs` passes for declared scroll-linked, SVG drawing, reveal no-flash, or reduced-motion claims, or the missing evidence is reported.

## Production Integrity

- Responsive behavior, performance risk, export stability, data meaning, localization, legal claims, confidentiality, and asset/font/image/icon rights are checked when relevant.
- Current platform, vendor, printer, supplier, legal, and license facts are verified from current authoritative sources rather than stale memorized values.
- Unknown production facts make the result a draft or preflight package, not a false production-ready claim.
- Mockups, generated assets, placeholders, inferred claims, and illustrative data remain materially honest.

## Branch Gates

Apply the selected branch's Done Criteria rather than loading unrelated medium rules:

- `branch-web-product.md`: task path, states, components/forms, accessibility, responsive behavior, design-to-code consistency.
- `branch-marketing-site.md`: first viewport, objection flow, proof, conversion, layout variety, performance.
- `branch-presentation.md`: title story, claim/evidence/action, density, charts, master, accessibility, export.
- `graphic-print.md`: output size, viewing distance, hierarchy, crop/safe area, production and rights preflight.
- `branch-brand-system.md`: distinctiveness, identity coherence, reusable rules, applications, governance and rights.
- `tokens-components.md`: token layers, component states, adoption, migration and regression coverage.
- `audit-polish.md`: severity-ranked findings, repair, second critique and accepted remaining risk.

## Contract And Delivery

- `DESIGN.md` matches the final artifact, stays lean, and records Request Anchor, content model, OKF Preflight, decision bindings, direction, assumptions, open questions, and review evidence.
- Reusable systems update tokens, components, agent rules, or review logs where continuity requires it.
- Critique 1 findings are severity-ranked; all P0/P1 and easy P2 findings are repaired.
- Critique 2 confirms no unresolved P0/P1, Request Anchor drift, active binding failure, or rendered-integrity failure.
- Verification failures are repaired or reported as `Not run`/blocked with a reason. The final response does not claim what evidence cannot support.

## Done Signal

Delivery passes only when Request Fit, active OKF bindings, selected branch Done Criteria, critique/repair, and relevant rendered/production checks pass. Remaining lower-severity risks are named, and another agent can continue from the governed contract without reverse-engineering the decisions.
