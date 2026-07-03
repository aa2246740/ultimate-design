# Content Model

Use this reference when the artifact contains meaningful text, UX writing, report visualization, dense content, forms, component states, localization, or a new `DESIGN.md`.

Content is the meaning authority. It defines what the user must understand and what each state means. UI is the interaction authority. Visual design is the attention authority. Frontend is the semantic and accessibility authority.

## Content Contract

Before layout and styling, define:

- User intent: why the user is here.
- Business intent: what the product or artifact needs to accomplish.
- Message hierarchy: the order in which the user must understand things.
- Primary action meaning: the action, result, and consequence.
- Voice and tone: stable brand voice plus scenario-specific tone.
- Terminology: canonical terms and words to avoid.
- State language: loading, empty, error, success, disabled, confirmation, and undo patterns when relevant.
- Content risks: legal, compliance, pricing, medical, financial, localization, or claims risk.

Do not let the content contract directly prescribe layout mechanics. It may require a module, state, warning, proof point, or hierarchy; the branch reference decides the interaction and visual form.

## Required Checks

- First screen answers what this is, why it matters, and what the user can do next.
- CTAs use action plus result, not vague labels such as "OK", "Submit", or "Click here" unless the result is obvious.
- Error text explains the problem and the fix.
- Empty text explains the current state and next step.
- Labels are visible; placeholders do not replace labels.
- Same concept uses the same term across the artifact.
- Critical meaning is not carried only by color, image, tooltip, hover, or truncated text.
- Long text, mixed language, dates, numbers, currencies, and localization expansion have a handling strategy.

## OKF Routing

Open `design-okf/index.md` first, then load only the content concepts needed:

- `design-okf/content/message-model.md` for user intent, first-screen clarity, content order, and decision paths.
- `design-okf/content/ux-writing.md` for CTAs, labels, helper text, errors, empty states, terminology, and voice/tone.
- `design-okf/content/state-language.md` for loading, empty, error, success, disabled, confirmation, and undo copy.
- `design-okf/content/semantic-binding.md` for component content, semantic HTML, labels, `aria-describedby`, i18n, long text, and text-state accessibility.

Use `design-okf/systems/typography-system.md` for type scale, line height, line length, mixed Chinese/English behavior, and responsive text.
