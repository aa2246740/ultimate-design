---
type: Digital Design Concept
title: Responsive And Interaction
description: Mobile-first layout, content breakpoints, interaction states, motion, and feedback.
tags: [responsive, interaction, motion, states]
---

# Purpose

Use this concept for websites, product UI, dashboards, and any digital artifact that must adapt across devices.

# Responsive Rules

- Start with mobile behavior.
- Expand for tablet and desktop.
- No page-level horizontal scroll at 320 px.
- Images and media scale predictably.
- Tables need a mobile strategy.
- Fixed or sticky UI must not cover content.
- Use content breakpoints where layout starts to fail.

Common breakpoints such as 640, 768, 1024, 1280, and 1536 px are defaults, not proof.

# Interaction Rules

- Every user action needs feedback.
- Async actions need loading, success, and failure states.
- Disabled controls need semantic disabled behavior and visible distinction.
- Popovers, menus, dialogs, and sheets need focus and escape behavior.
- Gesture-only actions need visible alternatives for critical tasks.

# Direct Manipulation

- Acknowledge press at input start when immediate feedback helps; commit the action at the appropriate semantic event.
- Dragged content follows input continuously after a small intent threshold and preserves the user's grab offset.
- Capture the active pointer or use an equivalent mechanism so tracking does not break when input leaves the element.
- Keep settling animation interruptible and start retargeting from the live rendered state.
- Use velocity, momentum projection, snap points, friction, or rubber-banding only when the interaction represents physical movement and the platform supports the behavior.
- Provide cancel, reverse, undo, keyboard, and reduced-motion alternatives in proportion to consequence.
- Verify consequential touch/gesture interactions on a real target device when browser or simulator evidence cannot represent feel and latency.

# Motion Rules

- Motion should express cause, hierarchy, continuity, feedback, navigation, story, or brand behavior.
- For nontrivial motion, animated decks, page transitions, scroll storytelling, or motion depth above static, read `../systems/motion-language.md`.
- For animation that must be implemented and verified, especially scroll-linked, SVG drawing, timeline, or reveal no-flash behavior, read `../systems/motion-contract.md`.
- Prefer transform and opacity for performance.
- Avoid content hidden behind reveal animations that might not fire.
- Support reduced motion and keep animations interruptible.

# Citations

[1] MDN Responsive Design: https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design
