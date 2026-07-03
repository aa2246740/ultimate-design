# Web Product Branch

Use this branch for dashboards, app UI, product flows, settings, onboarding, forms, tables, components, and design-to-code for task-oriented products.

## First Decisions

Before visual styling, settle:

- User: who is here and in what work context.
- Task: what they came to complete.
- Content contract: what the screen must communicate, what terms are canonical, and what each state means.
- State: what data, permission, loading, or error condition may appear.
- Navigation: how users move, return, recover, and preserve state.
- Content priority: what appears first on mobile.
- Density: compact, comfortable, or spacious.

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

## Frontend Implementation

- Do not hard-code color, spacing, radius, shadow, z-index, or motion values if the project has tokens.
- Images need dimensions or aspect ratios to avoid layout shift.
- Avoid unnecessary client-side JavaScript for static surfaces.
- Preserve existing project conventions unless the design goal justifies changing them.
