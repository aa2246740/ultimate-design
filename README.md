# Ultimate Design

A design workflow skill for AI agents.

It turns a design request into a usable result: clarify the brief, create a `DESIGN.md` when needed, load relevant design knowledge, make the artifact, critique and repair it, then verify what users will see.

Works with Codex, Claude Code, Pi Agent, and other compatible Agent Skill hosts.

## Install

```bash
npx ultimate-design-skill@latest --target codex
npx ultimate-design-skill@latest --target claude-code
npx ultimate-design-skill@latest --target pi-agent
```

See [integrations/README.md](integrations/README.md) for project-scoped, shared, and manual installation.

## Use

```text
Use $ultimate-design to turn this report into a clear visual web page. Create DESIGN.md if needed, make the page, critique it, repair it, and verify the rendered result.
```

Use `--pro` when you want to agree on the important design choices before implementation.

## What It Covers

- Websites and marketing pages
- Product UI, dashboards, and flows
- HTML decks and presentation strategy
- Posters, social graphics, and print direction
- Brand systems, design audits, and content design
- Project-wide motion audits and evidence-backed repair

## How It Works

1. Keep the user's request anchored.
2. Build a content and design contract.
3. Load only the relevant OKF knowledge.
4. Choose a direction and make the artifact.
5. Critique, repair, and verify it.
6. Leave enough context for the next Agent to continue.

## Verification

Visual work should be rendered and reviewed before delivery. Use the host Agent's available browser, renderer, screenshot, and accessibility tools; record what was checked and any limits. The bundled HTML validators are optional deterministic tools for environments that provide their compatible runtime.

For development checks:

```bash
npm run flow-check
npm run okf-graph-check
npm run check-integrations
```

## License

[MIT](LICENSE)
