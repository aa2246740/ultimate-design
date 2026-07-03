---
type: Content Design Concept
title: Semantic Binding
description: Binding content rules to components, semantic HTML, accessibility, long text, and localization.
tags: [semantic-html, accessibility, i18n, component-content]
---

# Purpose

Use this concept when content must survive implementation: forms, components, frontend UI, localization, long text, generated reports, and accessibility checks.

# Rules

- Prefer semantic HTML before ARIA: native controls first, ARIA only to supplement.
- Use visible labels for inputs; placeholders do not replace labels.
- Associate helper and error text with controls through `aria-describedby` when implemented in HTML.
- Use `aria-invalid` and useful error text for invalid fields.
- Critical content should wrap before it truncates.
- Truncated critical text needs a full-view path and should not depend only on `title`.
- Avoid sentence concatenation that breaks localization.
- Use locale-aware formatting for dates, numbers, and currencies when implemented dynamically.
- Use logical CSS properties when RTL or localization matters.
- Images, color, icons, and hover-only surfaces must not carry the only copy of critical meaning.

# Component Binding

Every reusable component should define:

- Default content.
- State content.
- Content slots.
- Accessible name and description.
- Long-text behavior.
- Localization behavior.
- Do and do-not examples when the component is reused across teams.

# Contract Fields

Record:

- Component content rules.
- Semantic HTML requirements.
- Long text and truncation rules.
- Localization and RTL assumptions.
- Accessibility implementation notes.
