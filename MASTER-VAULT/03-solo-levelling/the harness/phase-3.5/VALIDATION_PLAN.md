# Phase 3.5 — Empirical Validation Plan / Framework

> **Date:** 2026-09-01 | **Status:** DEPLOYING
> **Predecessor:** Phase 3 complete (Gate P3-31) — `harness-slice/HARNESS_SLICE.md` built
> **Mandate (plan.md):** Rankings are hypotheses until they survive real use. Run the harness slice against real tasks, record friction, feed back into Phase 2/3/1.

## Validation Method

1. **Materialize a real harness config** — apply `harness-slice/HARNESS_SLICE.md` → create actual `.harness/` in this repo (MCP config, hooks.py guards, permissions, skills index). This is *real work* that exposes whether the slice is coherent.
2. **Dogfood on real tasks in this repo** — use the materialized slice to execute genuine engineering tasks (e.g., implement the first concrete SKILL files, wire a working hook + run a real test loop). Record what worked/failed/friction.
3. **Capture SC friction** — per task: TTFUA-ish time, HIR (human interventions), cost tokens, permissions friction, context loss, autonomy misfit, tool conflicts.
4. **Feed back** — any S-tier element that under-delivered or B-tier that mattered gets logged → revise rankings.

## Validation Tasks (round 1)

| Task | What it exercises | Success criteria |
|------|-------------------|------------------|
| **V1 — Materialize `.harness/`** | CAP-37 AHG Gate, MCP config, hooks, permissions, 40-skill index | `.harness/` dir applies cleanly, hooks.py guard runs, no broken paths |
| **V2 — Author a real SKILL** | CAP-18 Skills, progressive disclosure, TDD SKILL template | A concrete new SKILL.md (from the 40) is authored + indexed |
| **V3 — Hook + test loop** | CAP-20 hooks, eval gate | pre_tool_guard.py + a real compile/test run executes end-to-end |

**Open:** real external tasks (the 2-3 from your actual projects) — pending user nomination. The dogfood rounds run now; external rounds slot in when nominated.

## Friction Log Schema

```
task, element, sc_expected, observation, friction_sev(0-3), fed_back_to (P2/P3/P1), status
```

## Next

Deploy VAL agents → write `.harness/` → run V1-V3 → friction log → feed back → VALIDATION_REPORT.md.