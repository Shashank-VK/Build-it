# Superior OS v2.0 — Design

Superset of deve v1.0. Same layout so deve users are at home; new capabilities are additive files, never rewrites of deve semantics.

## Layout (new files marked +)
```
superior-os/
  README.md                  OS overview + how-to-use wiring map
  AGENTS.md                  v2 registry: deve C1-C4 + C5-Verification (coder/explorer/planner/reviewer, eval-runner, coverage-keeper)
  CLAUDE.md                  runtime bridge (deve + subagent invocation + evidence rules)
  Taskfile.yml               deve tasks + council/review, eval-gate, coverage-gate, doctor, skills-list-15
  lefthook.yml               deve hooks + ruff-ast post-write check
  .cursorrules               deve rules + evidence/claim discipline pointers
  .env.template              deve keys + langfuse + eval flags
  .harness/config/harness.yaml   v2: loop rails + tier router + evidence gates + fetch caps
  .harness/skills/           9 deve skills + 15 verbatim the-harness runbooks (SKILL.md each)
  .harness/skills/index.json + progressive-disclosure registry (40-entry pattern, 24 local)
  .harness/agents/           + coder.md explorer.md planner.md reviewer.md
  .harness/workflows/        10 deve YAML + 5 new (build-verify, test-and-verify, migration-safeguard, refactor-safely, eval-gate)
  .harness/mcp/tools.yaml    deve 5 tools + servers block (filesystem/playwright/context7/github)
  .harness/mcp/MCP_SECURITY.md + transports/auth/poisoning/inspector
  .harness/hooks/hooks.json  deve 4 hooks + post-tool-linter
  .harness/hooks/post_tool_linter.py + ruff+AST auto-format/validate
  .harness/hooks/pre_tool_guard.py   (from deve, unchanged semantics)
  .harness/permissions/      deve cedar/check/presets (unchanged) + reviewer preset
  .harness/sandbox/gate.sh   (deve, unchanged)
  .harness/telemetry/        litellm-config.yaml (tiers) + langfuse-config.json + spend-log.sh
  os/                        deve 9 docs + 6 templates + disciplines/ (finops, notifications, mobile-release, trust-safety, api-product, billing)
  os/RULES-34.md             + 34-rule digest (card refs)
  os/ANTI-PATTERNS-19.md     + 19-AP digest + forensics notes pointer
  os/EVIDENCE.md             + change-coverage + claim-evidence + quarantine discipline
  os/templates/              + 10 lifecycle templates
  os/domains/                + A/B/C checklists
  scripts/                   deve 6 + coverage_gate.py + claim_check.py + tests
  scripts/verify.sh          v2: secret-scan + lint + pytest + coverage-gate + claim-check
```

## Key mechanisms
- Tier router (harness.yaml tiers.*): tiny → small model, gates 4/6 N/A; default → standard; high-stakes → big model + FCAR + independent re-implementation + eval-gate.
- Evidence gates: coverage_gate.py fails a change with no test receipt; claim_check.py fails unverified external claims (no URL+HTTP+date row in build-log evidence table).
- Worker discipline (docs): 40-cap fanout, idempotent rerun, checkpoint-per-receipt, quarantine-with-approval (adapted Phase 1 manager pattern for migrations/evals).
- Skills index.json: progressive disclosure (name/description/trigger, 24 local entries).
- No raw corpus copies: skills/workflows are distilled runbooks with `Ref: files/...` + card category, max 60 lines each.

## Build order
1. Config + registry + Taskfile + verify (this doc set).
2. Skills (12) + index.
3. Agents (4) + workflows (5).
4. MCP + security + hooks + telemetry.
5. OS docs + templates + domains.
6. Scripts + tests; run verify; fix; report.
