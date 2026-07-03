# Tokens And Components

Use this reference when creating or changing reusable design systems, tokens, components, themes, UI kits, or implementation rules.

Read `design-okf/systems/tokens-components.md` for the source-of-truth model: token layers, token families, component spec fields, and interaction states. Use this branch file for implementation coverage and governance checks.

## Implementation Tasks

- Inventory existing token sources before adding new ones.
- Map raw values to primitive, semantic, or component tokens.
- Update the design contract when token or component behavior changes.
- Keep component code consuming semantic or component tokens, not raw primitives.
- Add or update state examples when a reusable component changes.

## Naming Check

Prefer stable names over appearance names:

- Good: `color.text.primary`, `color.background.surface`, `color.action.primary`.
- Bad: `blue1`, `gray2`, `bigFont`, `newButtonColor`, `random13px`.

If a name describes appearance but the role is semantic, rename or record why the appearance name is intentionally local.

## Required Component Coverage

For a mature web product, check whether the system covers:

- Button.
- Link.
- Input.
- Textarea.
- Select.
- Checkbox.
- Radio.
- Switch.
- Form field.
- Label.
- Helper text.
- Error message.
- Card.
- Dialog or modal.
- Drawer.
- Tooltip.
- Dropdown or menu.
- Tabs.
- Accordion.
- Breadcrumb.
- Pagination.
- Navbar.
- Sidebar.
- Table.
- Badge or tag.
- Alert.
- Toast.
- Empty state.
- Skeleton.
- Spinner.
- Avatar.
- Icon.

Do not build the entire list if the project does not need it. Use it as a gap check.

## Governance

- New tokens need a purpose and role.
- Changed tokens need impact notes.
- Removed tokens should be deprecated first when existing code may consume them.
- New component variants need state and edge-case examples.
- Significant visual changes update the contract review log.
- If Storybook, visual regression, or CI exists, update it with the changed states.
