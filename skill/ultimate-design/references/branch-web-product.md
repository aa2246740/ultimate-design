# Web Product Branch

Use this branch for dashboards, app UI, product flows, settings, onboarding, forms, tables, components, and design-to-code for task-oriented products.

Read `design-okf/digital/accessibility-usability.md` when the surface includes forms, keyboard work, consequential actions, complex status, or accessibility review. Read `design-okf/digital/responsive-interaction.md` when layouts, tables, sticky/fixed UI, gestures, or interaction states must adapt across devices. Read `design-okf/governance/design-to-code-governance.md` when tokens/components must survive implementation, Storybook, regression tests, or CI.

When the OKF budget is tight and the user, task, outcome, and scope are already clear, prefer the concrete accessibility, responsive, interaction, motion, typography, data, or implementation concept over `product-sense.md`. Load product sense only when a product decision can still change what should be built or how success should be judged.

For product UI, taste is usually quiet: clarity, density, recovery, and trust beat spectacle. Read `design-okf/systems/typography-system.md` for scale, long or mixed-script labels, tabular figures, text zoom, wrapping, and overflow. Read `design-okf/systems/type-personality.md` only when introducing/changing font families, onboarding or empty states need a distinct voice, the CJK/Latin family pairing is itself an art-direction decision, or WebFont/fallback/licensing affects the product.

Read `design-okf/systems/motion-language.md` when product work includes nontrivial state transitions, microinteractions, drag/reorder, list update/delete/undo, modal/drawer choreography, route transitions, or loading/success/error motion. For dashboards, forms, payment, compliance, and high-frequency tools, keep the motion budget quiet unless the brief proves a stronger need.

Read `design-okf/systems/motion-contract.md` when product work includes animation that must be implemented and verified, especially SVG drawing, scroll-linked behavior, timeline sequencing, or no-flash reveal states.

## First Decisions

Before visual styling, settle:

- User: who is here and in what work context.
- Task: what they came to complete.
- Content contract: what the screen must communicate, what terms are canonical, and what each state means.
- State: what data, permission, loading, or error condition may appear.
- Navigation: how users move, return, recover, and preserve state.
- Content priority: what appears first on mobile.
- Density: compact, comfortable, or spacious.
- Type posture: usually utility-first, with any expressive display type limited to onboarding, empty-state illustration captions, marketing-adjacent surfaces, or brand moments.

Product surfaces help users repeatedly complete tasks. Favor clarity, predictability, and recovery over spectacle.

## Information Architecture

- The primary task path must be obvious.
- Users should know where they are, what they can do, and what happens next.
- Navigation labels use user language, not internal taxonomy.
- One screen or section should have one primary action unless the workflow truly has two peers.
- Loading, empty, error, success, disabled, permission-denied, and partial-data states are part of the design.
- Favor recognition over recall: expose choices when hiding them creates memory burden.

## Layout And Density

- Use spacing and alignment for grouping before adding borders.
- Use grid for two-dimensional layout; use flex for one-dimensional flows.
- Use stable dimensions for fixed-format UI such as boards, toolbars, counters, thumbnails, and icon buttons.
- No page-level horizontal scroll at 320 px.
- Use content breakpoints when the layout starts to fail, not only framework defaults.
- Do not put cards inside cards. Cards are for repeated items, modals, and genuinely framed tools.

## Components And Forms

- Prefer existing components, helpers, tokens, and framework idioms.
- Every interactive component needs relevant states: default, hover, focus, active, disabled, loading, and error.
- Forms need visible labels, helper text where useful, inline errors, recovery paths, and focus management.
- Component copy follows the content contract: labels name the thing, helper text explains format or consequence, errors explain fix, and empty states provide the next step.
- Destructive actions need confirmation or undo.
- Tables need sorting, empty/error/loading states, responsive strategy, and tabular figures.

## Accessibility And Interaction

- Use semantic HTML: `button` for actions, `a` for navigation, labels for inputs.
- Icon-only buttons need accessible names.
- Keyboard navigation must match visual order.
- Focus states must be visible.
- Do not rely on color alone.
- Every action needs visible feedback.
- Motion should explain cause, hierarchy, or continuity.
- Provide a reduced-motion path.
- Browser validation must prove any motion contract that affects state, sequence, SVG progress, or reduced-motion behavior.
- Give press feedback at input start when it improves directness; do not wait for a completed click to acknowledge the user.
- Direct-manipulation controls track the pointer or touch continuously, preserve the grab offset, and keep cancellation/recovery available.
- Gesture-driven animation starts from the live presentation value, remains interruptible, and does not lock input while settling.
- Use pointer capture, a small intent threshold, velocity handoff, momentum, or progressive boundary resistance only when the physical interaction needs them; verify important gestures on a real target device when practical.

## Frontend Implementation

- Do not hard-code color, spacing, radius, shadow, z-index, or motion values if the project has tokens.
- Images need dimensions or aspect ratios to avoid layout shift.
- Avoid unnecessary client-side JavaScript for static surfaces.
- Preserve existing project conventions unless the design goal justifies changing them.

## Done Criteria

Product UI is ready when the primary task path and return/recovery paths are clear, reachable states have useful content and feedback, components/forms are semantic and keyboard-safe, responsive behavior is verified, consequential interaction remains predictable and interruptible, implementation follows the contract/tokens, and unresolved product, accessibility, performance, or data risks are named.
