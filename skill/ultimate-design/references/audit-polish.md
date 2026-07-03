# Audit And Polish Branch

Use this branch for critiques, redesign diagnosis, final polish, visual QA, anti-AI-slop passes, and improving an existing design without starting over.

## Audit Flow

1. Identify the surface, audience, primary task, and current design intent.
2. Inspect the artifact or code before making recommendations.
3. Score or rank findings by user impact, business impact, accessibility risk, and implementation effort.
4. Separate quick wins from structural changes.
5. Propose concrete fixes.
6. Verify changed work when you implement fixes.

## Build Critique Loop

Use this loop after creating a design and before final delivery:

1. Compare the artifact to the Request Anchor, user brief, and `DESIGN.md`.
2. Check content contract: user intent, message hierarchy, first-screen answers, CTA meaning, terminology, and state language.
3. Check product fit when relevant: problem statement, target user, core job, success signal, deliberate non-goals, validation path, and whether the artifact is the smallest useful version for the learning or user outcome.
4. Check presentation fit when relevant: audience, delivery mode, decision request, title-story coherence, slide claim/evidence/action, density, charts, master consistency, accessibility, and export stability.
5. Check requirement fit: deliverable, core job to be done, success criteria, non-goals, must-preserve constraints, and latest user override.
6. Check theme fit: color, typography, imagery, and tone match the audience, product, and desired emotion.
7. Check IA: primary message, primary task, first-screen clarity, navigation, and content hierarchy.
8. Check craft: composition, visual hierarchy, spacing, alignment, component states, motion, and anti-slop issues.
9. Check production: accessibility, responsive behavior, performance risk, slide/PDF export, print/export, i18n, legal/licensing, and data-viz rules when relevant.
10. For screenshotable visual artifacts, render every final page/slide/state practical to inspect; do not rely on a single sampled screenshot or bounds-only check.
11. Write findings as P0/P1/P2/P3.
12. Fix all P0/P1 and easy P2 issues, including any mismatch with the Request Anchor.
13. Run one more critique pass on the changed artifact.

Do not ship after the first critique if it found unresolved P0 or P1 issues, including requirement drift from the Request Anchor.

## Finding Format

For reviews, lead with findings:

- Severity.
- Location.
- Problem.
- Why it matters.
- Concrete fix.

Avoid vague feedback such as "make it cleaner" or "improve hierarchy" without naming the elements and changes.

## Polish Sequence

Apply polish in this order:

1. Clarity: message, task, IA, labels, CTA.
2. Content: voice/tone, terminology, state language, help/risk/trust copy.
3. Product fit when relevant: problem, user outcome, success signal, scope, and validation path.
4. Presentation fit when relevant: decision path, title story, claim/evidence/action, density, chart trust, and delivery package.
5. Request fit: deliverable, core job, success criteria, non-goals, and must-preserve constraints.
6. Accessibility: contrast, focus, semantics, keyboard, reduced motion.
7. Layout: alignment, grouping, spacing rhythm, responsive behavior.
8. Typography: scale, weight, line length, wrapping, overflow.
9. Color: roles, contrast, state parity, palette coherence, visual personality.
10. Interaction: states, feedback, recovery, loading/empty/error.
11. Craft: motion, imagery, details, anti-slop cleanup.

## Anti-Slop Checks

Reject and rewrite:

- Gradient text used as decoration.
- Generic glass cards.
- Identical icon-card grids.
- Decorative side stripes.
- Over-rounded cards or inputs.
- Huge soft shadows paired with borders.
- Generic blobs, orbs, stripes, or stock-like placeholders.
- Tiny uppercase eyebrows repeated above every section.
- Numbered section markers where order carries no meaning.
- Copy that sounds impressive but says nothing specific.

## Done Criteria

An audit or polish pass is done when:

- Findings are severity-ranked.
- Recommendations map to user, business, accessibility, or design-system impact.
- Implemented fixes are verified.
- A second pass confirms no unresolved P0/P1 findings remain.
- The artifact still matches the Request Anchor or any mismatch is explicitly accepted as a follow-up risk.
- Remaining risks are named.
- Contract assumptions or design-system changes are recorded when persistence matters.
