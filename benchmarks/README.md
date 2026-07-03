# Benchmarking Ultimate Design

There is no single public benchmark that fully measures a professional design skill. The available benchmarks are useful, but each covers a slice of the work.

Ultimate Design should be measured on two layers:

1. **Public comparability:** run against existing web/UI/design benchmarks where the task matches.
2. **OKF workflow quality:** measure what makes this skill different: request integrity, contract quality, routed knowledge, critique/repair, rendered verification, and reusable governance.

## Public Benchmarks To Consider

| Benchmark | Best For | Notes |
| --- | --- | --- |
| [Design2Code](https://github.com/NoviScl/Design2Code) | Screenshot-to-HTML visual fidelity | 484 real-world webpages plus an 80-case hard set; includes automatic evaluation code and metrics such as block/text/position/color/CLIP-style measures. |
| [DesignBench](https://github.com/WebPAI/DesignBench) | Frontend generation, edit, and repair | Multi-framework benchmark for React, Vue, Angular, and vanilla HTML/CSS; 900 samples across generation, edit, repair, and compile repair. |
| [WebGen-Bench](https://arxiv.org/html/2505.03733v1) | Natural-language website generation | Tests website generation from scratch with functional and appearance requirements. |
| [UI-Bench](https://uibench.ai/leaderboard) | Text-to-app design preference | Expert blinded pairwise comparison, TrueSkill ranking, and confidence intervals. |
| [Design Arena](https://www.designarena.ai/) | Crowdsourced design preference | Useful for public taste/preference comparison across categories such as website, UI component, data visualization, slides, logo, and more. |
| [VisualWebBench](https://github.com/VisualWebBench/VisualWebBench) | Web understanding and grounding | Good for testing whether an agent/model can parse visual web context, OCR, ground elements, and predict actions. |
| [WebSight](https://arxiv.org/html/2403.09029v1) / [WebCode2M](https://webcode2m.github.io/) | Data for screenshot-to-code and visual fidelity research | Useful for training/eval context, less directly aligned with contract-driven design workflow. |
| [AesthetiQ-style layout judging](https://arxiv.org/html/2503.00591v1) | Layout aesthetics | Useful inspiration for MLLM-as-judge and win-rate scoring of rendered layout quality. |

## Why Public Benchmarks Are Not Enough

Ultimate Design is not only a frontend generator. It also decides whether to create a `DESIGN.md`, preserves the user request across long work, routes OKF knowledge by branch, critiques its own work, and verifies rendered output. A screenshot-to-code benchmark can score fidelity, but it will not tell you whether the agent:

- remembered the original user need after a long task,
- avoided loading irrelevant research,
- chose a style with a design reason,
- repaired issues found during critique,
- left a usable contract for the next agent.

## OKF Workflow Rubric

Score each run out of 100:

| Dimension | Points | Measurement |
| --- | ---: | --- |
| Request integrity | 15 | Request Anchor exists; original request, latest override, deliverable, success criteria, non-goals, and validation checks are preserved and used in final critique. |
| Contract quality | 15 | `DESIGN.md` or equivalent captures tokens, content model, IA, visual system, quality gates, assumptions, open questions, and review log at the right depth. |
| OKF routing | 15 | Loaded references match the task branch; irrelevant branches are not loaded; selected OKF concepts are reflected in decisions. |
| Content strategy | 10 | Message hierarchy, terminology, UX writing, state language, and copy density fit the audience and medium. |
| Visual craft | 15 | Hierarchy, typography, color posture, spacing, composition, density, and theme fit are deliberate rather than generic. |
| Accessibility and responsiveness | 10 | Contrast, semantic structure, focus/keyboard needs, responsive checks, and text reflow are addressed where relevant. |
| Verification evidence | 15 | Rendered screenshots/previews exist for every final page/slide/frame; DOM or visual checks catch overlap, clipping, tight spacing, and line issues. |
| Governance and reuse | 5 | Contract updates, assumptions, and review notes let another agent continue without reverse engineering. |

## Recommended Eval Protocol

1. Pick 10 to 30 prompts across surfaces: web page, dashboard, marketing page, deck, social carousel, report visualization, brand system, and audit/repair.
2. Run each prompt with and without Ultimate Design while holding model, tools, and time budget constant.
3. Save artifacts, `DESIGN.md`, screenshots, validation reports, and trace notes.
4. Run automated checks:
   - `flow_check.py` on the skill bundle,
   - `validate_design_contract.py --strict-ultimate` on generated contracts,
   - `validate_html_visual.mjs` on screenshotable HTML outputs,
   - accessibility/performance checks when the artifact is a real web surface.
5. Run blinded pairwise human judging for final artifacts. Use a TrueSkill or Bradley-Terry style model if enough comparisons exist.
6. Report both:
   - public benchmark numbers where applicable,
   - OKF workflow score with evidence paths.

## Minimum Quantitative Metrics

- `contract_pass_rate`: percent of runs whose `DESIGN.md` passes strict contract validation.
- `visual_check_pass_rate`: percent of final screenshotable artifacts with zero high-severity visual validation failures.
- `request_anchor_coverage`: percent of runs with all Request Anchor fields present and referenced in final critique.
- `okf_routing_precision`: loaded relevant references divided by all loaded references.
- `p0_p1_repair_rate`: high-severity critique findings fixed before delivery.
- `human_preference_win_rate`: blinded preference win rate versus a baseline skill or no-skill run.

## Benchmark Files

- [okf-rubric.json](okf-rubric.json): machine-readable rubric.
- [prompt-suite.jsonl](prompt-suite.jsonl): starter prompt set.
- [score-okf-run.mjs](score-okf-run.mjs): simple scorer for rubric result JSON.

## Claiming Results

Do not claim "best design skill" from automated checks alone. A strong claim needs:

- repeated runs across prompt categories,
- blinded human preference or expert scoring,
- rendered artifact evidence,
- failure analysis,
- versioned prompts, model names, dates, and tool constraints.
