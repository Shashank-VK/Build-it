# DX, Observability & Meta — Per-Element Knowledge Base (Phase 4, Batch D-5)

> **Date:** 2026-09-01 | **Sources:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-1/batch-5/BATCH-5_DX_OBSERVABILITY.md`
> **Template:** 18-section per element. Consolidated.

---

## CAP-32 — Evaluation & Benchmark Engine
1. **Overview:** Empirical harness scoring (SWE-bench, Terminal-Bench, Inspect AI, Promptfoo, unit/e2e gates).
2. **Why matters:** Objectively measures task success (SC-02/06/08) — the harness's own dashboard.
3. **How works:** versioned task suites → agent → gold-patch/assertion verdict.
4. **When use:** Harness development, regression gates, feature validation.
5. **When NOT:** (core DX; always in CI).
6. **Importance:** S-tier. C1/C2/C4/C5/C6=S; C3=A.
7. **Essential:** Inspect AI, SWE-bench runner, Promptfoo.
8. **Optional:** Terminal-Bench, deep-eval.
9. **Rules:** Version suites; hidden tests; no eval leakage.
10. **Deps:** CAP-37 gate.
11. **Integration:** Post-run grading.
12. **Failure modes:** Leakage, overfit suites.
13. **Security:** Sanitize tasks.
14. **Maintenance:** Refresh suites.
15. **Sources:** Batch-5 B5-16/17/18.
16. **Links:** https://inspect.aisi.org.uk; promptfoo.
17. **Last verified:** 2026-09-01.
18. **Re-check:** benchmark changes.

---

## CAP-33 — Meta-Evaluation & Grader Calibration
1. **Overview:** Validate accuracy/variance/calibration/bias of LLM-judges.
2. **Why matters:** Trustworthy grading (SC-06/08).
3. **How works:** Reference-set evaluation of the judge.
4. **When use:** LLM-as-judge workflows (C4 research), eval harness itself.
5. **When NOT:** Deterministic assertions.
6. **Importance:** B-tier (specialized). C4=A; rest B/C.
7. **Essential:** (optional) judge-calibration libs.
8. **Optional:** Promptfoo calibration.
9. **Rules:** Calibrate judges; report variance; human spot-check.
10. **Deps:** CAP-32.
11. **Integration:** Audits eval.
12. **Failure modes:** Judge bias.
13. **Security:** N/A.
14. **Maintenance:** Recalibrate.
15. **Sources:** Batch-5 B5-19.
16. **Links:** (as sources).
17. **Last verified:** 2026-09-01.
18. **Re-check:** judge models.

---

## CAP-34 — Autonomous Self-Improvement & Adaptation
1. **Overview:** Offline loop mining history → refine prompts/tools/routing.
2. **Why matters:** Long-term capability growth (SC-06/08) — instinct-mining + auto-tuning.
3. **How works:** Trajectory analysis → heuristics/rule bank; hyperparam tuning.
4. **When use:** Mature harnesses seeking improvement (C4/C6).
5. **When NOT:** Early/brittle harness — complexity risk.
6. **Importance:** A-tier. C4/C6=S; rest B.
7. **Essential:** (optional) LangSmith / evals-driven tuning.
8. **Optional:** instinct-mining engines.
9. **Rules:** Guardrail against feedback loop corruption; A/B validate changes.
10. **Deps:** CAP-32 eval.
11. **Integration:** Uses friction logs.
12. **Failure modes:** Self-reinforcing errors.
13. **Security:** Validation gate.
14. **Maintenance:** Monitor drift.
15. **Sources:** Batch-5 B5-21..24.
16. **Links:** https://www.langchain.com/langsmith.
17. **Last verified:** 2026-09-01.
18. **Re-check:** self-improve tooling.

---

## CAP-35 — Cost & Complexity Budget Governance
1. **Overview:** Global quotas on spend/tokens/tools/hooks/rules (anti-bloat).
2. **Why matters:** SC-05 hard cap; prevents harness bloat.
3. **How works:** Budget circuit-breaker (LiteLLM $5 cap); complexity budgets; stale-rule pruner.
4. **When use:** Every run (esp C4 long).
5. **When NOT:** (core).
6. **Importance:** S-tier (universal).
7. **Essential:** LiteLLM proxy budget + Langfuse; `.harness/telemetry/litellm-config.yaml`.
8. **Optional:** tiktoken pre-flight.
9. **Rules:** Hard-stops; per-session attribution; prune dead rules.
10. **Deps:** CAP-16.
11. **Integration:** Governs all model/tool usage.
12. **Failure modes:** Over-budget, bloat.
13. **Security:** N/A.
14. **Maintenance:** Tune limits.
15. **Sources:** Batch-5 B5-08/09/25/26.
16. **Links:** docs.litellm.ai; langfuse.com.
17. **Last verified:** 2026-09-01.
18. **Re-check:** budget config.

---

## CAP-36 — Lifecycle Deprecation & Sunset Management
1. **Overview:** Formal protocol to mark/alert/migrate/tombstone obsolete skills/tools/schemas.
2. **Why matters:** Safe evolution; SC-06/08.
3. **How works:** `deprecated` schema + migration path + sunset deadline; tombstone engine.
4. **When use:** Harness evolution, tooling changes.
5. **When NOT:** (should run continuously).
6. **Importance:** A-tier. C5/C6=S.
7. **Essential:** deprecation protocol in HaC.
8. **Optional:** —.
9. **Rules:** Migration before sunset; deterministic failure post-deadline.
10. **Deps:** PROT-03 HaC.
11. **Integration:** Config changes.
12. **Failure modes:** Abrupt breakage.
13. **Security:** N/A.
14. **Maintenance:** Sunset audit.
15. **Sources:** Batch-5 B5-27/28.
16. **Links:** (in repo).
17. **Last verified:** 2026-09-01.
18. **Re-check:** —.

---

## CAP-37 — Autonomous Harness Governance (AHG) Gate
1. **Overview:** Top-level governor running pre/in/post-flight quality gates across harness lifecycle.
2. **Why matters:** Integrates eval+budget+deprecation+verification (SC-08).
3. **How works:** `gate.sh` + lefthook + pre/post hooks; CI harness validation.
4. **When use:** Every harness run (CI + local).
5. **When NOT:** (core).
6. **Importance:** S-tier (universal).
7. **Essential:** gate.sh + lefthook + gitleaks + pre_tool_guard.
8. **Optional:** —.
9. **Rules:** Zero unlinted/secret code; gates in CI.
10. **Deps:** CAP-20/32/35/36.
11. **Integration:** Top-level orchestration.
12. **Failure modes:** Gate gaps, slow gates.
13. **Security:** Enforcement hub.
14. **Maintenance:** Keep gates fast.
15. **Sources:** Batch-5 B5-30.
16. **Links:** `.harness/` (lefthook, gate).
17. **Last verified:** 2026-09-01.
18. **Re-check:** gate tooling.

---

*End of D-5 (DX/Meta).*