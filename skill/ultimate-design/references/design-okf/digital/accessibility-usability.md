---
type: Digital Design Concept
title: Accessibility And Usability
description: WCAG target, semantic HTML, keyboard, focus, labels, errors, and usability heuristics.
tags: [accessibility, usability, wcag, forms, keyboard]
---

# Purpose

Use this concept for digital surfaces, forms, product UI, marketing sites with interaction, and design QA.

# Accessibility Default

Default target for digital work: WCAG 2.2 AA unless the user specifies otherwise.

# Minimum Checks

- Semantic structure.
- Keyboard access.
- Visible focus.
- Text contrast.
- UI/non-text contrast.
- Labels for inputs.
- Alt text for meaningful images.
- Empty alt for decorative images.
- Reduced motion.
- Reflow at narrow widths.
- Error identification and recovery.

# Usability Heuristics

Check:

- System status is visible.
- Language matches the user's world.
- Users can recover from mistakes.
- Interfaces are consistent.
- Recognition is preferred over recall.
- Errors are prevented where practical.
- Help is close to the problem.

# Forms And Feedback

- Inputs need labels, not placeholder-only labels.
- Errors explain what happened and how to fix it.
- Submit actions need loading and failure states.
- Destructive actions need confirmation or undo.
- Toasts and status messages should not steal focus unnecessarily.

# Touch Targets

Use 44 by 44 CSS px as a comfortable mobile target when practical, while remembering WCAG AA has a smaller target-size minimum with exceptions.

# Citations

[1] WCAG 2.2 Quick Reference: https://www.w3.org/WAI/WCAG22/quickref/
[2] NN/g 10 Usability Heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/
