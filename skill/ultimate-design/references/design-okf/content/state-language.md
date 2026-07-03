---
type: Content Design Concept
title: State Language
description: Copy patterns for loading, empty, error, success, disabled, confirmation, and undo states.
tags: [states, forms, feedback, microcopy]
---

# Purpose

Use this concept for product UI, forms, dashboards, workflows, async actions, destructive actions, and components with state changes.

# State Patterns

- Loading: what is happening now.
- Empty: what is missing, why it may be missing, and how to start.
- Error: what failed, impact if useful, and how to recover.
- Success: what completed and what can happen next.
- Disabled: why the action is unavailable and what would enable it.
- Confirmation: what will happen and the consequence.
- Undo: what changed and how long or how to reverse it.
- Permission: what access is missing and how to request or switch context.
- Partial data: what is shown, what is missing, and whether action is safe.

# Rules

- States are part of the design, not afterthoughts.
- Do not rely on color alone for state.
- Disabled controls need a discoverable explanation; do not hide the only explanation in hover-only tooltip.
- Loading and error states need accessible announcements when they change important status.
- Destructive actions need confirmation or undo when practical.

# Contract Fields

Record:

- Required states by component or page.
- State copy patterns.
- Recovery paths.
- Accessibility notes for state changes.
