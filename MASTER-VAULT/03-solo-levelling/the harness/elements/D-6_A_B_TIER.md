# A/B-Tier & Interaction Map — Knowledge Base (Phase 4, Batch D-6)

> **Date:** 2026-09-01 | **Sources:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-3/TOOL_SELECTION_INDEX.md`
> **Contents:** (1) A/B-tier element briefs, (2) MASTER INTERACTION / CONFLICT MAP.

---

## Part 1 — A/B-Tier Element Briefs (anti-bloat, concise)

### CAP-02 — Agent Teams & Multi-Agent Coordination (A→B global)
- **Overview:** Persistent peer/supervisor multi-agent topologies with messaging, task-lists, negotiation.
- **Why:** Debate/handoff/long-lived peer awareness beyond fan-out-and-merge.
- **When use:** C4 agentic (S); complex refactors.
- **When NOT:** Solo/simple tasks (C3=C).
- **Tier:** B global (S in C4). Tools: CrewAI/AutoGen/LangGraph supervisor (Optional).
- **Rules:** Peer messaging vs hub-and-spoke (E1 boundary); shared task deps.
- **Deps:** CAP-01/03. **Failure:** Coordination overhead. **Security:** Peer scope.
- **Sources:** Batch-1 E2. **Verified:** 2026-09-01.

### CAP-11 — Typed Bi-Temporal KG Memory → see D-2 CAP-11 (B-tier). Tools: Neo4j/Graphiti.
### CAP-12 — Semantic & Response Caching → see D-2 CAP-12 (B-tier). Tools: Redis LangCache.
### CAP-23 — Dynamic Model Routing → see D-3 CAP-23 (A-tier). Tools: OpenRouter / LiteLLM Router (RouteLLM removed — maintenance stall).
### CAP-28 — Execution Provenance → see D-4 CAP-28 (A-tier). Tools: flight recorder/OTel.
### CAP-31 — Supply-Chain → see D-4 CAP-31 (A-tier). Tools: Sigstore/SLSA.
### CAP-33 — Meta-Evaluation → see D-5 CAP-33 (B-tier).
### CAP-34 — Self-Improvement → see D-5 CAP-34 (A-tier). Tools: LangSmith.
### CAP-36 — Deprecation → see D-5 CAP-36 (A-tier).
All referenced in their layer files to avoid duplication (anti-bloat).

---

## Part 2 — MASTER INTERACTION / CONFLICT MAP

> Purpose: cross-element dependencies, conflicts, overlaps, resource competition, security-boundary interactions, context competition, lifecycle conflicts, failure propagation. **Tensions are explicit, not forced into a DAG.**

### 1. Dependency Graph (MUST-HAVE-ON)

```
CAP-01 Subagent ──(needs)──▶ CAP-03 Orchestration, CAP-06 Isolation, CAP-16 Budget
CAP-03 Orchestration ──▶ CAP-04 (workflows), CAP-05 (background), CAP-07 (fan-out)
CAP-08 Working Memory ──▶ CAP-16 Budget ──▶ CAP-09 Compaction
CAP-09 Compaction ──(hook)──▶ CAP-20 Lifecycle Hooks
CAP-13 RAG ──▶ CAP-15 Curation (build); CAP-16 (augment)
CAP-17 MCP ──(tool)──▶ CAP-03; PROT-01 (protocol)
CAP-18 Skills ──▶ MEC-02 Progressive Disclosure
CAP-20 Hooks ──▶ MEC-04 Event Sys ──wraps──▶ all tool exec
CAP-22 Gateway ──▶ PROT-02 (schemas); CAP-23 routing
CAP-24 Hermetic Exec ──▶ MEC-01 isolation (container/bwrap drivers)
CAP-25 Authorization ──▶ CAP-20 hooks gate
CAP-26 Secrets ──▶ MEC-06/07; CAP-37 gate
CAP-27 Injection Def ──▶ CAP-20 pre-prompt; Batch-2 B6 fencing
CAP-29 HITL ──▶ CAP-25 authorization, CAP-30 reversibility
CAP-30 Reversibility ──▶ MEC-05; CAP-03 recovery
CAP-32 Eval ──▶ CAP-37 gate
CAP-35 Budget ──▶ CAP-16, CAP-22, CAP-23
CAP-37 AHG Gate ──▶ CAP-20/32/35/36
```

### 2. Conflicts & Tensions (the interesting part)

| Tension | Parties | Nature | Resolution |
|---------|---------|--------|------------|
| **Memory ↔ Context budget** | CAP-08/09/14 ↔ CAP-16 | Both compete for window | P0-P10 priority chain; pinned set non-evictable; compaction preserves pins |
| **Hooks ↔ Sandboxing** | CAP-20 ↔ CAP-24 | Hook runs inside or outside sandbox? | Dual-boundary: semantic (hooks) at orchestration; mechanical (sandbox) at OS — never substitute |
| **Subagents ↔ Cost** | CAP-01/07 ↔ CAP-35 | Fan-out multiplies tokens | Pareto `pass@1 vs $/task` gate; per-agent budget |
| **Autonomy ↔ Human review** | CAP-07/34 ↔ CAP-29 | More autonomy needs stronger verify | Per-archetype autonomy calibration (C5/C6 very low, C3 high-compensated) |
| **Skills ↔ Complexity budget** | CAP-18 ↔ CAP-35 | More skills = more ambiguity/maintenance | Index not 40 files; prune unused; top-10 materialized |
| **Compaction ↔ Fencing survival** | CAP-09 ↔ CAP-27 | Hardening decays if compactable | Trust labels + pinned set compaction-exempt (SC-09 probe must test) |
| **Consolidation ↔ Poisoning** | CAP-10 ↔ CAP-27/31 | Episodic→semantic promotion is injection point | Provenance `informed_by` + validation before promotion |
| **Graph vs Vector substrate** | CAP-11 ↔ CAP-13 | Provenance vs cheap | Choose per archetype: C4-research graph; C1/C3 vector |
| **Cache ↔ Staleness** | CAP-12 ↔ CAP-14 | Reuse vs stale hits | TTL/namespace; invalidate on supersede |
| **Isolation ↔ Overhead** | CAP-06/24 ↔ CAP-01 TTFWS | Sandbox/worktree add latency | Overlay only where risk demands (SC-01 pressure) |
| **Eval ↔ Leakage** | CAP-32 ↔ CAP-28 | Benchmark leakage distorts | Hidden tests; no leakage; versioned suites |
| **Self-improvement ↔ Corruption** | CAP-34 ↔ CAP-32 | Feedback loop can self-reinforce | A/B validate; guardrail; human spot-check |
| **Authorization ↔ Velocity** | CAP-25 ↔ CAP-07 SC-01 | Least-privilege adds friction | Presets per archetype; deny-by-default with fast allow path |
| **Rollback ↔ External Side-Effects** | CAP-30 ↔ CAP-17/CAP-03 | Git rollback cannot undo remote mutations (DB writes, cloud infra, API calls) | Tripartite state engine enforces compensating saga transactions for non-idempotent MCP tools (V-KB-3 §5.1) |
| **Telemetry ↔ Secret Isolation** | SUB-01/CAP-28 ↔ CAP-26 | Full-fidelity OTel traces and WAL flight recorders log raw command I/O — primary secret leakage vector | Synchronous, non-bypassable DLP redactor (MEC-07) upstream of all telemetry emitters and disk flushes (V-KB-3 §5.2) |
| **Multi-agent concurrency ↔ Git index lock** | CAP-07/CAP-02 ↔ CAP-06/MEC-01 | Parallel subagents sharing `.git` object store collide on `index.lock` / ref-updates during simultaneous commits | Mutex/queue lock manager around git ref ops across worktree pool (V-KB-3 §5.3) |
| **Dynamic routing ↔ Prompt cache invalidation** | CAP-23 ↔ CAP-08/CAP-12/PROT-02 | Cross-provider turn routing (Claude→GPT-4o→Gemini) voids prefix cache and causes JSON-schema dial-drift → parsing errors | Sticky session affinity per sub-task; strict schema normalization at Gateway (CAP-22) (V-KB-3 §5.4) |
| **Injection defense ↔ Skill ingestion** | CAP-27 ↔ CAP-18 | Rigid sanitizers false-positive on legitimate bash runbooks and regex patterns in `SKILL.md` files | Cryptographic trust provenance (CAP-31/PROT-04) allows verified local skills to bypass external-data sanitizers (V-KB-3 §5.5) |

### 3. Resource Competition (zero-sum)

- **Context window:** CAP-08/09/13/16 + tools + prompts all compete — budget governor arbitrates.
- **Model budget ($/tokens):** CAP-23 routing × CAP-35 caps × CAP-07 fan-out — Pareto frontier.
- **CPU/container:** CAP-07 fan-out × CAP-24 sandbox × CAP-05 background — pool limits.
- **Developer attention:** HITL (CAP-29) × autonomy (CAP-07) — calibrated not maximized.

### 4. Security-Boundary Interactions

```
ORCHESTRATION LAYER (semantic)      OS/HYPERVISOR (mechanical)
  CAP-20 hooks, CAP-27 fencing,      CAP-24 sandbox, CAP-26 secrets(JIT/DLP)
  CAP-25 policy, CAP-29 HITL         CAP-28 flight recorder (WAL)
  ── instruction trust ──            ── syscall trust ──
  hooks can be fooled by novel phrasing; sandbox cannot by content. Both required.
```

### 5. Lifecycle Conflicts

- **Build-time (CAP-15 curation, CAP-31 supply-chain, CAP-36 deprecation)** must not gate run-time velocity (CAP-01 TTFWS).
- **Review-time (CAP-29 HITL, CAP-33 meta-eval, CAP-37 gate)** adds latency — calibrate.
- **Self-improvement (CAP-34)** runs review→build — must not rewrite production prompts without eval.

### 6. Failure Propagation Paths

```
Tool error ──▶ CAP-03 recover ──▶ CAP-28 record ──▶ CAP-35 budget check ──▶ CAP-37 gate
Context overflow ──▶ CAP-09 compact (pinned) ──▶ CAP-16 re-allocate
Poisoned input ──▶ CAP-27 block ──▶ CAP-28 log ──▶ CAP-25 scope
Irreversible action ──▶ CAP-29 HITL ──▶ CAP-30 checkpoint/saga ──▶ CAP-28 audit
Hook failure ──▶ CAP-20 non-bypassable fallback ──▶ CAP-37 gate
```

### 7. Top-level anti-bloat check (plan §HARNESS COMPLEXITY)
The 37 caps + 10 MEC + 3 PROT are the *capability* set — most are Mechanisms/Protocols, only ~21 are load-bearing Capabilities. Each addition must answer: materially improves? actually used? benefit>complexity? redundant? removable? — enforced at every gate (the harness's own CAP-35/37 discipline).

---

*End of D-6 (A/B + Interaction Map).*