# Phase 1 — Batch 4: Safety, Governance & Trust — Converged Taxonomy Slice

> **Status:** CONVERGED — P1-25..32 | **Date:** 2026-09-01 | **Dispatch:** WSL `agy` (plan §8.1)
> Inputs: [`R-A_SAFETY_AGY.md`](R-A_SAFETY_AGY.md) (29.7K Broad) · [`R-B_SAFETY_AGY.md`](R-B_SAFETY_AGY.md) (25.3K Challenger) · [`V-C_SAFETY_AGY.md`](V-C_SAFETY_AGY.md) (39.8K Adversarial) · [`V-D_SAFETY_AGY.md`](V-D_SAFETY_AGY.md) (12.8K Architectural)
> Repo: `the harness` | Grounding: `plan.md §2 Batch 4` · `phase-0/ARCHETYPES_AND_CRITERIA.md` SC-01..10 · merged with Batch 1 (E7 auto/E8 HITL/E11 undo) + Batch 2 (B6 fencing, G-X)

---

## 0. Method & Coverage

- **R-A (Broad, via agy):** 6 angles — Execution Sandboxing, Permission Gateways, Prompt-Injection Defenses (G-X), Credential/Data Governance, Config Scanning + Skill Supply Chain, Auditability/Reversibility/Provenance — all SC-07/04/10 wired. Ecosystems: Claude Code, OpenAI, LangChain/LangGraph, AutoGen/SK, Bedrock Guardrails, NeMo Guardrails, OpenHands, MCP.
- **R-B (Challenger, via agy):** least-privilege allow/deny, policy-as-code, guardrail taxonomy, sandbox boundary, credential vault + rotation, data vs privacy vs licensing/IP, side-effect reversibility classes, injection governance. Divergent vocab.
- **V-C (Adversarial, via agy):** mapped every candidate against ≥2 mature non-agent ecosystems (POSIX/OS, Distributed Systems, Cloud-Native/K8s, IAM/Zero-Trust, W3C, DB Engines, MITRE/NIST). **Dual-boundary security**: hooks/instruction-trust (orchestration layer) vs sandbox/syscall-trust (OS/hypervisor). Resolved triads: guardrails/safety-nets/permission-modes → 2 distinct + 1 KILLED; audit vs observability vs reproducibility → Batch 4 / Batch 5 / Batch 6.
- **V-D (Architectural, via agy):** 6-layer ontology (CAP/MEC/STD/RUN/ART/TLS). **26-row converged master table**. Fixed systematic conflation: sandbox/gVisor/JIT/DLP/Vault/audit/cosign all were Mechanism/Tool/Resource mislabeled as Capability.

**Dispatch note:** first agy dispatch hit headless permission auto-deny (0 bytes) → **resolved with `--dangerously-skip-permissions`** (correct for headless research; see `ISSUES.md` #7-10).

---

## 1. Converged Batch 4 Master Table (26 rows, V-D)

| # | Candidate | Level | Lifecycle | Tier | SC Wiring | Conflation Fix |
|---|---|--------|-----------|------|-----------|----------------|
| 01 | **Hermetic Isolated Execution** | **Capability** | run | Foundational | SC-01, SC-07 | Pure cap — agent actions cannot compromise host OS |
| 02 | Ephemeral Container/MicroVM Sandbox | Mechanism | run | Foundational | SC-01, SC-07 | R-A called it Capability; it's a Mechanism |
| 03 | gVisor / Bubblewrap / Wasmtime | Framework/Runtime | run | Important | SC-01, SC-07 | Concrete executable substrate |
| 04 | **Authorization & Least-Privilege Governance** | **Capability** | run | Foundational | SC-02, SC-04 | Pure cap — restrict to minimal viable set |
| 05 | Capability-Based Access Control (CapBAC) | Mechanism | build/run | Foundational | SC-02, SC-07 | Permission model is CapBAC mechanism |
| 06 | Declarative Policy Engine (Policy-as-Code) | Mechanism | build/run | Important | SC-02, SC-04 | Decouples rules from agent prompts |
| 07 | OPA / Cedar Engine | Framework/Runtime | run | Important | SC-02 | Policy evaluation runtime |
| 08 | **Zero-Trust Secret Governance** | **Capability** | run | Foundational | SC-07 | Zero plaintext secret exposure |
| 09 | JIT Ephemeral Credential Brokering | Mechanism | run | Foundational | SC-07 | Dynamic short-lived token injection |
| 10 | HashiCorp Vault / AWS Secrets Manager / KMS | Tool/Product/Repo | run | Important | SC-07 | Vendor product, not capability |
| 11 | Data Loss Prevention (DLP) & Stream Masking | Mechanism | run | Foundational | SC-07 | Redacts secrets before logs/LLM context |
| 12 | **Indirect Prompt Injection Defense Gateway** | **Capability** | run | Foundational | SC-02, SC-07 | Extends B6 fencing to tool-data ingestion |
| 13 | Dual-LLM / Delimiter-Isolated Sanitizer | Mechanism | run | Important | SC-02 | Pattern separating untrusted parsing |
| 14 | **Execution Provenance & Non-Repudiation** | **Capability** | run/review | Foundational | SC-10 | Proves chain-of-custody, causality |
| 15 | Cryptographic Append-Only Flight Recorder | Mechanism | run | Foundational | SC-10 | Audit trail is Mechanism, not Capability |
| 16 | Transcript & Trajectory Log `transcript.jsonl` | Resource/Artifact | review | Foundational | SC-10 | Data artifact |
| 17 | **Deterministic Execution Replayability** | **Capability** | run/review | Specialized | SC-01, SC-10 | Separate from Observability (goes Batch 5/6) |
| 18 | Virtual Clock & Syscall Network Interception | Mechanism | run/review | Specialized | SC-01, SC-10 | Enables deterministic replay |
| 19 | **HITL Escalation & Override Gateway** | **Capability** | run | Foundational | SC-04 | Non-bypassable human gate; governs E8 |
| 20 | **Side-Effect Containment & State Reversibility** | **Capability** | run | Foundational | SC-04, SC-01 | Classify/isolate/checkpoint/rollback |
| 21 | Git Worktree / Snapshot Rollback Engine | Mechanism | run | Foundational | SC-04, SC-01 | Branching/overlayfs = snapshot mechanism |
| 22 | Compensating Transaction Saga Coordinator | Mechanism | run | Important | SC-04 | Distributed rollback for external side effects |
| 23 | **Supply-Chain Integrity & Manifest Verification** | **Capability** | build | Important | SC-02, SC-07 | Validated provenance for skills/plugins/hooks |
| 24 | Sigstore / Cosign / SLSA Attestation | Protocol/Standard & Tool | build | Important | SC-02 | Signing tool + SLSA framework |
| 25 | Signed Skill Manifest (`skill.json`/`manifest.sig`) | Resource/Artifact | build | Important | SC-02, SC-07 | Static data resource |
| 26 | Static AST & Secret Leakage Scanner | Mechanism | build/review | Important | SC-07, SC-02 | Semgrep/TruffleHog = static analysis |

---

## 2. V-C Semantic Resolutions

### 2.1 Guardrails vs Safety Nets vs Permission Modes — the triad collapses

| Former Triad | Verdict | Resolution |
|---|---|---|
| Semantic Guardrails | **DISTINCT** | Runtime semantic policy interceptor (NeMo/Bedrock-style rails) — check model I/O against constraints |
| Deterministic Capability Authorization | **DISTINCT** | Hard allow/deny gate at tool boundary (CapBAC / OPA) |
| "Safety Nets" (colloquial) | **KILLED** | Umbrella term, not an architectural primitive — absorbed into the two above |

### 2.2 Audit Trail vs Observability vs Reproducibility — XOR split

- **Tamper-Evident Audit Trail & Cryptographic Provenance** → **Batch 4** (governance) — immutable, non-repudiable.
- **Runtime Observability / Telemetry** → **Batch 5** (DX/observability owner) — what's happening now (OTel traces).
- **Deterministic State Replay** → **Batch 6 / Reproducibility** — can we reconstruct the exact run (hermetic env freeze).

### 2.3 Dual-Boundary Security (the key structural insight)

```
Orchestration Layer (Semantic Policy)     OS/Hypervisor Layer (Capability Containment)
──────────────────────────────────────    ─────────────────────────────────────────
Hooks / PreToolUse interception          Sandbox / seccomp / namespaces / microVM
Instruction Trust (content vs instruction)   Syscall Trust (kernel-level capability)
   → scopes with Batch 2 (B6 fencing)        → scopes with Batch 4 (rows 01-03)
```
**Boundary rule:** hooks are semantic (can be fooled by novel phrasing); sandboxing is mechanical (cannot be fooled by content). Both required — never substitute.

---

## 3. Kill / Merge / Demote Log + Abstraction Flags

| Action | Count | Details |
|--------|-------|---------|
| **KEEP Capability** | **9** | Hermetic Execution, Authorization/Least-Privilege, Zero-Trust Secrets, Injection Defense Gateway, Execution Provenance, Deterministic Replay, HITL Escalation, Side-Effect Reversibility, Supply-Chain Integrity |
| **DEMOTE to Mechanism/Framework/Tool/Resource** | **17** | Sandbox, gVisor, CapBAC, Policy Engine, OPA, JIT Brokering, Vault, DLP, Dual-LLM, Flight Recorder, transcript, Virtual Clock, Worktree, Saga, Cosign, Skill Manifest, AST Scanner |
| **KILL** | 1 | "Safety Nets" (colloquial umbrella) |
| **RE-ROUTE** | 2 | Observability → Batch 5; Deterministic Replay → Reproducibility (Batch 6); Hooks↔sandbox dual-boundary |
| **Conflation theme** | — | R-A/R-B consistently labeled Mechanism/Tool/Resource as Capability (sandbox, JIT, DLP, audit, cosign all fixed) |

**Level-hygiene (V-D):** *Hermetic Execution* (CAP) vs *Ephemeral Sandbox* (MEC) vs *gVisor* (RUN); *Secret Governance* (CAP) vs *Vault* (TLS); *Provenance* (CAP) vs *Flight Recorder* (MEC) vs *transcript.jsonl* (ART); *Reversibility* (CAP) vs *Git Worktree* (MEC) vs *Saga* (MEC).

---

## 4. Architectural Directives (V-D §6)

1. **Terminology invariant:** never call "Sandboxing"/"Permission Modes"/"Audit Trails" Capabilities — use **Isolated Execution Boundary (CAP)**, **Capability-Based Access Control (MEC)**, **Execution Provenance (CAP)/Flight Recorder (MEC)**.
2. **Policy/core decoupling:** all authorization externalized to Policy-as-Code Engine (MEC) against Signed Policy Manifest (ART); no hardcoded security heuristics in the agent loop.
3. **Hermetic secret invariant (SC-07):** plaintext long-lived secrets never touch LLM context/workspace; JIT ephemeral tokens into isolated process env, scrubbed by DLP before flight recorder.
4. **Non-bypassable flight recording (SC-10):** WAL pattern — flush+sync event record to disk *before* subprocess/API trigger.

---

## 5. Sources

R-A/R-B disk files (in this dir) · V-C/V-D verifier files · NIST SP 800-207 Zero Trust · Linux namespaces/cgroups/seccomp · OPA (CNCF) · Cedar (AWS) · SLSA v1.0 (OpenSSF/Google) · SPDX/CycloneDX/Sigstore/Cosign · OpenTelemetry · HashiCorp Vault · Semgrep/TruffleHog · internal SC contracts.

**Last verified:** 2026-09-01.