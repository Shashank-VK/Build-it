# Superior OS v2.0

A single-developer AI product-engineering OS. Superset of the deve v1.0 template:
same loop rails, 6 gates, ABAC, sandbox — plus engineering-depth skills (21),
subagents (coder/explorer/planner/reviewer), executable workflows (15),
a real MCP layer with security rules, eval + evidence gates, 6 product
disciplines, 34 rules / 19 anti-patterns, 16 lifecycle templates, and
domain playbooks.

## Start
1. Read `AGENTS.md` (operating contract), then `os/lifecycle.md`.
2. `task new-project -- <name>`; follow Gates 1-6 in `os/gates.md`.
3. `task verify` must exit 0 before any merge or deploy.

## Behavior contract
`../how-to-use/` (707 cards) is the authority behind every skill, workflow,
gate, discipline, and template here. Each file cites its card sources.
`../how-to-use/` is read-only; this OS never copies raw corpus.

## Map
- `.harness/` — executable contract: config, skills+index, agents, workflows, MCP, hooks, permissions, sandbox, telemetry.
- `os/` — readable contract: lifecycle, gates, rubric, rules, evidence, disciplines, templates, domains, third-party registries (skills/MCP/agents + machine index).
- `scripts/` — verification: secret-scan, scope-check, tests, coverage-gate, claim-check, spend-log, verify.sh.
