# Contributing

Contributions should preserve the core premise: Ultimate Design is an OKF-based design skill, not a monolithic prompt.

## Good Contributions

- Improve routing clarity in `SKILL.md`.
- Add or sharpen OKF concept files when a design branch needs missing knowledge.
- Improve validators without making ordinary design work heavier.
- Add benchmark prompts, rubrics, or result fixtures.
- Fix portability, installation, or documentation issues.

## Guardrails

- Keep the installable skill lean. Put release docs in the repository root, not inside `skill/ultimate-design`.
- Do not add raw private research dumps to the skill. Distill them into typed OKF concepts.
- Do not add mandatory monitoring to ordinary design work.
- Do not claim benchmark wins without reproducible runs.

## Validation Before PR

```bash
npm run flow-check
npm run scan-release
```

If you changed `validate_html_visual.mjs`, also run it on a small HTML artifact that includes `data-ud-check` zones.
