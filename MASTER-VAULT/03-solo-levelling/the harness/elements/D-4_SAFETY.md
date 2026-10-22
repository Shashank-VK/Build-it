# Safety, Governance & Trust — Per-Element Knowledge Base (Phase 4, Batch D-4)

> **Date:** 2026-09-01 | **Sources:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md`
> **Template:** 18-section per element. Consolidated.

---

## CAP-24 — Hermetic Isolated Execution Boundary
1. **Overview:** Host OS/network containment — untrusted agent actions in sandboxes (containers/microVMs).
2. **Why matters:** SC-07 zero-host-leak invariant; regex is NOT enough (validated).
3. **How works:** gVisor/Bubblewrap/Docker ephemeral sandbox; seccomp/namespaces.
4. **When use:** All tool/shell execution (esp untrusted code, C5/C6).
5. **When NOT:** (core, always).
6. **Importance:** S-tier (universal, veto).
7. **Essential:** gVisor/Docker ephemeral; `.harness/sandbox/gate.sh`.
8. **Optional:** Firecracker/Wasmtime.
9. **Rules:** Ephemeral; no host FS writes; network egress allowlist.
10. **Deps:** MEC-01/02 isolation mechanisms.
11. **Integration:** Execution substrate for all tools.
12. **Failure modes:** Escape, false sandbox confidence.
13. **Security:** THE security boundary.
14. **Maintenance:** Keep runtime patched.
15. **Sources:** Batch-4 B4-01..03.
16. **Links:** gVisor; Bubblewrap.
17. **Last verified:** 2026-09-01.
18. **Re-check:** sandbox runtime CVEs.

---

## CAP-25 — Authorization & Least-Privilege Governance
1. **Overview:** CapBAC + declarative policy engine enforcing minimal tool/FS/network perms.
2. **Why matters:** Least privilege; SC-07/04.
3. **How works:** OPA/Cedar policy evaluation; role presets (C1-C6).
4. **When use:** All tool authorization.
5. **When NOT:** (core).
6. **Importance:** S-tier (universal, veto).
7. **Essential:** OPA or Cedar; `.harness/permissions/policies.cedar` + `presets.json`.
8. **Optional:** OPA/Cedar engine.
9. **Rules:** Deny-by-default; per-archetype presets; externalize policy.
10. **Deps:** —.
11. **Integration:** Gate tool execution via hooks.
12. **Failure modes:** Over-broad grants.
13. **Security:** Core authz.
14. **Maintenance:** Policy as code.
15. **Sources:** Batch-4 B4-04..07.
16. **Links:** https://www.openpolicyagent.org; Cedar.
17. **Last verified:** 2026-09-01.
18. **Re-check:** policy engine.

---

## CAP-26 — Zero-Trust Secret Governance
1. **Overview:** End-to-end credential isolation — plaintext secrets never in LLM context/logs/disk.
2. **Why matters:** SC-07 0-leaks; JIT brokering + DLP redaction.
3. **How works:** JIT ephemeral tokens into process env; DLP masks output streams.
4. **When use:** All secrets-using tasks.
5. **When NOT:** (core).
6. **Importance:** S-tier (universal, veto).
7. **Essential:** Vault; `.harness/pre_tool_guard.py` secret patterns.
8. **Optional:** AWS Secrets Manager/KMS.
9. **Rules:** Never plaintext in prompt; JIT+TTL; DLP before flight recorder.
10. **Deps:** MEC-06/07.
11. **Integration:** Pre-tool guard + DLP + vault.
12. **Failure modes:** Secret leak, false-positive redaction.
13. **Security:** Zero-tolerance.
14. **Maintenance:** Rotation; pattern updates.
15. **Sources:** Batch-4 B4-08..11.
16. **Links:** Hashicorp Vault.
17. **Last verified:** 2026-09-01.
18. **Re-check:** secret patterns.

---

## CAP-27 — Indirect Prompt Injection Defense & Fencing
1. **Overview:** Separate trusted instructions from untrusted data (delimiter fencing, sanitizer, span-taint, canary).
2. **Why matters:** Agent-era XSS; SC-07 ≥90% blocked, 0 leaks.
3. **How works:** `[BEGIN UNTRUSTED REF]` fences; pre-model scan; dual-LLM.
4. **When use:** Web/repo/tool-output ingestion (all agents).
5. **When NOT:** (core).
6. **Importance:** S-tier (universal, veto).
7. **Essential:** PromptInjectionDefender/trust-boundary libs.
8. **Optional:** AGENTS.md trust classes.
9. **Rules:** Provenance stamp; scan every tool result; fences survive compaction.
10. **Deps:** B6 fencing + G-X governance (batch 4).
11. **Integration:** Pre-tool + pre-prompt hooks.
12. **Failure modes:** Novel-phrasing evasion (hook semantic), sandwich attacks.
13. **Security:** Core defense.
14. **Maintenance:** Red-team suites.
15. **Sources:** Batch-4 B4-12/13; Batch-2 B6.
16. **Links:** pydantic-ai-harness; faion.
17. **Last verified:** 2026-09-01.
18. **Re-check:** new attack vectors.

---

## CAP-28 — Execution Provenance & Non-Repudiation
1. **Overview:** Tamper-evident append-only flight recorder (WAL, SHA-256 hash chain).
2. **Why matters:** Audit, reproducibility (SC-10).
3. **How works:** WAL — flush event+hash to `transcript.jsonl` BEFORE tool dispatch.
4. **When use:** All actions (esp autonomous C4/C6).
5. **When NOT:** (should always).
6. **Importance:** A-tier. C5/C6=S; rest A.
7. **Essential:** Flight-recorder script + OTel/JSONL.
8. **Optional:** Arize Phoenix/OpenLineage.
9. **Rules:** WAL ordering; hash chain; non-bypassable.
10. **Deps:** CAP-37 gate.
11. **Integration:** Hooks write events.
12. **Failure modes:** Log gap, hash break.
13. **Security:** Integrity.
14. **Maintenance:** Retention policy.
15. **Sources:** Batch-4 B4-14/15.
16. **Links:** (flight_recorder.py in `.harness/telemetry/`).
17. **Last verified:** 2026-09-01.
18. **Re-check:** format changes.

---

## CAP-29 — HITL Escalation Gateway
1. **Overview:** Non-bypassable human approval primitive (approve/reject/modify, audit trail).
2. **Why matters:** Irreversible actions; SC-04 / SC-07.
3. **How works:** Approval queue at risk threshold; timeouts; calibrate per archetype.
4. **When use:** Irreversible (deploy/spend/delete), C5/C6 low-autonomy.
5. **When NOT:** High-autonomy C3 (compensated).
6. **Importance:** S-tier. C1/C5/C6=S; C3=A; C4=B.
7. **Essential:** harness HITL hooks (approval gate).
8. **Optional:** LangGraph/ADK human-in-loop.
9. **Rules:** Risk-class-based; audit trail; timeout.
10. **Deps:** CAP-25/30.
11. **Integration:** Escalation path on risk.
12. **Failure modes:** Over-babysit, missed risk.
13. **Security:** Human review is barrier.
14. **Maintenance:** Calibration.
15. **Sources:** Batch-4 B4-19.
16. **Links:** (hooks.json in `.harness/`).
17. **Last verified:** 2026-09-01.
18. **Re-check:** risk taxonomy.

---

## CAP-30 — Side-Effect Containment & State Reversibility
1. **Overview:** Isolate/checkpoint/undo/compensate state mutations (FS, context, external APIs).
2. **Why matters:** SC-03 recovery, safe rollback.
3. **How works:** Tripartite: FS snapshots + trajectory rewind + compensating inversion/sagas.
4. **When use:** Mutating tasks (all), esp migrations/ops.
5. **When NOT:** Read-only.
6. **Importance:** S-tier. C1/C5/C6=S.
7. **Essential:** git snapshot + saga patterns.
8. **Optional:** Temporal saga.
9. **Rules:** Idempotent; rollback contract; classify side-effects.
10. **Deps:** MEC-05.
11. **Integration:** Undo hooks (E11).
12. **Failure modes:** Partial rollback.
13. **Security:** Reversibility reduces blast.
14. **Maintenance:** Compensation registry.
15. **Sources:** Batch-4 B4-20/21/22.
16. **Links:** (workflows in `.harness/`).
17. **Last verified:** 2026-09-01.
18. **Re-check:** saga tooling.

---

## CAP-31 — Supply-Chain Integrity & Manifest Verification
1. **Overview:** Verify provenance/signatures of skills/plugins/hooks/tools before execution.
2. **Why matters:** Prevent supply-chain poisoning (SC-07).
3. **How works:** Sigstore/Cosign/SLSA attestation; static AST scan (Semgrep/TruffleHog).
4. **When use:** Loading any third-party component.
5. **When NOT:** Built-in trusted.
6. **Importance:** A-tier. C4/C5=S.
7. **Essential:** Sigstore/SLSA + static scanners.
8. **Optional:** Dependabot.
9. **Rules:** Verify before load; signed manifests; scan secrets.
10. **Deps:** —.
11. **Integration:** Harness loader.
12. **Failure modes:** Unverified component.
13. **Security:** Supply-chain gate.
14. **Maintenance:** Verify cadence.
15. **Sources:** Batch-4 B4-23..26.
16. **Links:** https://slsa.dev.
17. **Last verified:** 2026-09-01.
18. **Re-check:** SLSA changes.

---

*End of D-4 (Safety).*