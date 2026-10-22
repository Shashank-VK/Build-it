# Phase 3.5 — Validation Report (P3.5-12)

> **Date:** 2026-09-01 | **Status:** LOOP COMPLETE — findings fed back into Phases 2/3
> **Input:** harness slice (`harness-slice/` + `.harness/`), 26-agent Phase 3 fleet
> **Method:** V1 hook gate test → V2 skill authoring → V3 coherence audit → materialization sprint → V4 re-validation

---

## 1. Validation Rounds Executed

| Round | What ran | Result | Empirical finding |
|-------|----------|--------|-------------------|
| **V1** | `pre_tool_guard.py` gate | ✅ PASS | Blocks `rm -rf`, secrets; passes benign. Regex guard is brittle vs true sandbox. |
| **V2** | Skill authoring + index | ✅ PASS | repo-surveyor-map + TDD skill materialized; progressive-disclosure index + functional `survey_repo.py`. |
| **V3** | Coherence audit (spec vs disk) | ⚠️ GAP | Only 2/21 S-tier ops on disk — slice was a blueprint. 15 caps unmaterialized. |
| **Sprint** | Materialization (M-A/M-B/M-C) | ✅ PASS | Converted blueprint → working `.harness/` — **2 → 15+ operational**. |
| **V4** | Re-validate materialized artifacts | ✅ PASS + fixed 1 bug | JSON valid; rm/secrets/AWS-key blocked. **Found real security regression**: force-push regex missed `--force` after branch → **FIXED** + re-verified. |

## 2. What Worked (validated strengths)

1. **S-tier security guard works in practice** — `pre_tool_guard.py` blocks destructive commands (rm -rf, mkfs, chmod 777, fork bomb, curl|sh) AND real secret patterns (AWS AKIA, GitHub PAT/Fine-grained, GitLab, private keys, JWTs, hardcoded keys). Empirically confirmed.
2. **Progressive disclosure (skills) is functional** — skills index + frontmatter + on-demand load works; `survey_repo.py` is real working code.
3. **Materialization sprint proved the loop** — coherence audit → identified gap → agents closed it → re-validated. The spiral is real, not theoretical.
4. **JSON configs all valid**, subagent prompts/workflows/Cedar policy/LiteLLM budget all materialized cleanly.

## 3. What Failed / Friction (the valuable part)

| # | Friction | Element | Fed back to | Status |
|---|----------|---------|-------------|--------|
| 1 | Spec-vs-code gap: 2/21 S-tier ops on disk | all S-tier | **P3 → materialization sprint** | ✅ RESOLVED (15+ ops) |
| 2 | Regex guard brittle, false-positives | CAP-24/26 | P2: CAP-24 impl bar = real OS sandbox; P3 | sandbox/gate.sh added |
| 3 | `hooks.json` missing / post-linter absent / gate.sh absent | CAP-20/37 | P3 | ✅ materialized |
| 4 | No agents/, workflows/, Taskfile | CAP-01/04 | P3 | ✅ materialized |
| 5 | MCP stripped 7→2 servers | CAP-13/17 | P3 | ✅ expanded |
| 6 | Cedar policy not wired | CAP-25 | P3 | policies.cedar + presets ✅ |
| 7 | LiteLLM $5 cap not active | CAP-35/22 | P3 | litellm-config ✅ |
| 8 | No flight recorder | CAP-28 | P3 | langfuse + flight recorder config |
| 9 | HITL only hard-exits, no interactive modal | CAP-29 | P3 | presets wire HITL triggers |
| 10 | **force-push regex missed `--force` after branch** | CAP-37 | **P3 immediate fix** | ✅ FIXED + re-tested |

## 4. Feedback Loop Results (rankings/tools/taxonomy revisions)

- **P3 revised:** materialization sprint added real `.harness/` artifacts (agents, workflows, hooks, Cedar, LiteLLM, sandbox, 3 more skills, provenance) — the harness is now buildable, not just documented.
- **P2 note:** CAP-24 Hermetic Exec stays S-tier, but the implementation bar is now explicit (real OS sandbox via bwrap/docker, not regex).
- **P3 anti-bloat:** 40 skills indexed; top ~5 materialized; rest stay as index entries (avoid 40-file bloat).
- **Body of knowledge:** the validation findings are the "friction tax" that separates a real harness from a doc.

## 5. Real-task validation (outstanding)

Dogfood rounds (V1-V4) validated the harness internals on our own repo. **The remaining Phase 3.5 requirement is running the harness against 2-3 tasks from your actual projects** (not this repo) — pending user nomination. The slice is now functional enough to do that.

## 6. Gate P3.5-13 — Recommendation

**CONDITIONAL PASS for internal validation.** The harness slice now works end-to-end (guards, skills, workflows, agent defs, configs) and the feedback loop caught + fixed a real bug. **Final pass on external real-task validation** — nominate 2-3 real projects/tasks and I'll run the harness against them, then close out Phase 3.5 and proceed to **Phase 4 (documentation `.md` knowledge base + interaction map)**.

---
*"Rankings are hypotheses until they survive real use." — this report is the evidence they've started to.*