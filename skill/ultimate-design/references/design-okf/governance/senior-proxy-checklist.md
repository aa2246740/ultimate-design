---
type: Evaluation Rubric
title: Senior Proxy Checklist
description: Observable proxy checks for professional design quality and final verification.
tags: [quality-gate, senior-proxy, verification, design-review]
---

# Purpose

Use this concept before claiming professional quality. It does not prove a designer has ten years of experience; it checks observable behaviors associated with senior design work.

# Proxy Checks

- Brief is explicit.
- User and business goal are clear.
- Design direction is specific and non-generic.
- IA supports the primary user task.
- Visual hierarchy is intentional.
- Composition has a clear focal point and reading path.
- Color roles are defined and accessible.
- Typography is readable and handles overflow.
- Accessibility target is met or gaps are named.
- Responsive behavior is checked or specified.
- Interaction states are covered where relevant.
- Tokens/components are updated when persistence matters.
- Data visualization, i18n, and legal risks are checked when relevant.
- Automated checks or their absence are reported honestly.
- Print, licensing, or asset risks are flagged when relevant.
- Contract records decisions, assumptions, open questions, and review evidence.

# Evidence Levels

Use honest labels:

- Verified: checked with a tool, renderer, browser, export, or direct inspection.
- Assumed: safe default chosen and recorded.
- Not run: not checked, with reason.

# Runtime Boundary

This checklist is descriptive. It does not override:

- Browser rendering.
- Accessibility tools.
- Code tests.
- Print vendor specifications.
- CI or VCS status.
- User feedback.

# Done Check

The senior proxy pass is done when every relevant check is verified, assumed, or explicitly marked not run.
