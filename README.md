# Ultimate Design

OKF-based design skill for contract-driven AI design.

Ultimate Design is a Codex skill that turns vague design requests into governed design work: a brief, a `DESIGN.md` contract when persistence matters, routed OKF knowledge, a concrete artifact, critique/repair, rendered verification, and reusable design memory for the next agent.

Most frontend design skills optimize for styling or code generation. Ultimate Design optimizes the full professional design loop:

1. Preserve the original user request with a Request Anchor.
2. Convert intent, content, visual rules, accessibility, and quality gates into a design contract.
3. Load only the relevant OKF concept files instead of dumping all research into context.
4. Make the artifact across web, product UI, decks, graphics, brand systems, content design, or audits.
5. Critique and repair before final delivery.
6. Verify rendered output, not just source code.
7. Govern the contract so later agents do not have to reverse-engineer the design.

## Why OKF

OKF means the design knowledge is split into small, typed concept files with an index and routing rules. The skill can load product sense for a dashboard, commercial deck knowledge for a PPT, print caveats for a poster, content strategy for dense copy, or visual verification rules for screenshotable artifacts.

That is the core selling point: **the skill behaves like an indexed design operating system, not a giant prompt.**

## Repository Layout

```text
.
├── skill/ultimate-design/        # Installable Codex skill
│   ├── SKILL.md                  # Core operating loop and routing rules
│   ├── agents/openai.yaml        # UI metadata
│   ├── references/               # Branch references and OKF bundle
│   └── scripts/                  # Flow, contract, and visual validators
├── benchmarks/                   # Benchmark landscape and OKF eval proposal
└── examples/                     # Example prompts
```

## Install

Copy the installable skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skill/ultimate-design ~/.codex/skills/ultimate-design
```

Then invoke it in Codex:

```text
Use $ultimate-design to turn this report into a visual page. Create or update DESIGN.md if needed, keep the original request anchored, and verify the rendered output.
```

## Example Prompts

```text
Use $ultimate-design to redesign this dense validation report as a visual web page for executives.
```

```text
Use $ultimate-design to create a 10-slide HTML PPT deck from this research memo. Make it board-room credible and run deck-level validation before delivery.
```

```text
Use $ultimate-design to audit this landing page. Find requirement drift, visual slop, copy issues, accessibility issues, and fix the high-severity problems.
```

More examples live in [examples/prompts.md](examples/prompts.md).

## Validation

Run the static flow proof:

```bash
python3 skill/ultimate-design/scripts/flow_check.py skill/ultimate-design
```

Validate a generated `DESIGN.md` contract:

```bash
python3 skill/ultimate-design/scripts/validate_design_contract.py path/to/DESIGN.md --strict-ultimate
```

Validate screenshotable HTML artifacts:

```bash
node skill/ultimate-design/scripts/validate_html_visual.mjs \
  --input path/to/artifact.html \
  --out benchmark-runs/visual-check \
  --viewports desktop=1440x900,mobile=390x844 \
  --spacing 36
```

The visual validator uses Playwright when available. Set `PLAYWRIGHT_MODULE` or install `playwright` in the project if your runtime does not provide it.

## Benchmarks

There is no single public benchmark that fully measures a design skill like this. Existing benchmarks usually test one slice: screenshot-to-code fidelity, text-to-app preference, frontend repair, web grounding, or layout aesthetics. See [benchmarks/README.md](benchmarks/README.md) for the current benchmark landscape and an OKF-specific scoring plan.

The recommended benchmark story is:

- Use public web/UI benchmarks for external comparability.
- Use the OKF workflow rubric for what makes Ultimate Design different: request integrity, contract quality, routed knowledge, critique/repair, rendered verification, and reusable governance.

## License

Apache-2.0. This is a default open-source release choice; change it before publishing if your project needs MIT, CC-BY, or a proprietary dual-license.

## Non-Affiliation

This project is not an official Google, OpenAI, Anthropic, Figma, or Codex product. OKF references are an implementation pattern for indexed knowledge in agent workflows.
