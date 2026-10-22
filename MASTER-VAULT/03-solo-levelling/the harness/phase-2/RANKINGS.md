# Phase 2 — Master Rankings (P2-17) — S/A/B/C/D per Element + Archetype Matrix

> **Status:** CONVERGED — ALL 37 Capabilities ranked | **Date:** 2026-09-01
> **Method:** 7-dim rubric (1-5) per `phase-2/RUBRIC.md` · Harm 4-5 veto enforced · Anti-averaging (per-archetype tiers)
> **Sources (10 sessions):** 5 group rankers (`rankings/G1..G5`) + independent arbiter (`verify/ARBITER_AGY.md`) + mechanism/protocol scout (`verify/MECH_PROT_AGY.md`) + cross-batch tension verifier (`verify/CROSSBATCH_TENSION.md`) — all via agy
> Repo: `the harness` | Input: `phase-1/MASTER_TAXONOMY.md` (48 elements) | Gate: P2-18

---

## 1. Consolidated Ranking — 37 Capabilities (Global Tier + Per-Archetype)

| Rank | CAP | Capability | Global | C1 Product | C2 Data/ML | C3 Autom/Browser | C4 Agent/Know | C5 Platform | C6 Migr | Key SC |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | CAP-03 | Dynamic Orchestration & Control Flow | **S** | S | S | S | S | A | S | SC-02/03/08/10 |
| 2 | CAP-24 | Hermetic Isolated Execution Boundary | **S** | S | S | S | S | S | S | SC-07/01/06 |
| 3 | CAP-26 | Zero-Trust Secret Governance | **S** | S | S | S | S | S | S | SC-07/10 |
| 4 | CAP-25 | Authorization & Least-Privilege | **S** | S | S | S | S | S | S | SC-07/04/02 |
| 5 | CAP-20 | Lifecycle Interception & Hooks | **S** | S | S | S | S | S | S | SC-07/03/08 |
| 6 | CAP-37 | Autonomous Harness Governance Gate | **S** | S | S | S | S | S | S | SC-08/10/06 |
| 7 | CAP-35 | Cost & Complexity Budget Governance | **S** | S | S | S | S | S | S | SC-05/01/08 |
| 8 | CAP-32 | Evaluation & Benchmark Engine | **S** | S | S | A | S | S | S | SC-06/08/02 |
| 9 | CAP-06 | Isolated Workspace Management | **S** | S | A | B | A | S | S | SC-06/07/10 |
| 10 | CAP-01 | Delegated Subagent Execution | **S** | S | S | B | S | A | S | SC-01/04/05/09 |
| 11 | CAP-04 | Deterministic Workflows & Blueprints | **S** | A | S | S | B | S | S | SC-06/08/10/05 |
| 12 | CAP-08 | Working Memory Management | **S** | S | S | S | S | S | S | SC-01/05/09/02 |
| 13 | CAP-13 | External Knowledge Retrieval (RAG) | **S** | S | A | A | S | A | A | SC-02/08/01/05 |
| 14 | CAP-27 | Indirect Prompt Injection Defense | **S** | S | S | S | S | A | S | SC-07/02 |
| 15 | CAP-09 | Context Compaction & Pinned Preservation | **S** | A | A | B | S | B | S | SC-09/06/07/05 |
| 16 | CAP-29 | HITL Escalation Gateway | **S** | S | A | A | B | S | S | SC-04/07 |
| 17 | CAP-17 | Open Tool Interop (MCP) | **S** | S | S | S | S | S | S | SC-02/07/05 |
| 18 | CAP-22 | Model Gateway & Provider Abstraction | **S** | S | S | S | S | S | S | SC-02/03/05 |
| 19 | CAP-19 | Ambient Rules Enforcement | **S** | S | S | A | A | S | S | SC-02/07/08 |
| 20 | CAP-18 | Procedural Skills Execution | **S** | S | A | A | B | S | A | SC-01/02/05 |
| 21 | CAP-30 | Side-Effect Containment & Reversibility | **S** | S | A | A | B | S | S | SC-03/06/10 |
| 22 | CAP-05 | Background & Async Queued Execution | **A** | A | S | S | A | A | A | SC-01/03/05 |
| 23 | CAP-07 | Parallel Execution & Fan-Out | **A** | A | S | A | S | C | S | SC-01/05/03 |
| 24 | CAP-16 | Context & Token Budget Governance | **A** | A | A | B | S | A | B | SC-05/09/01/02 |
| 25 | CAP-15 | Build-Time Knowledge Curation | **A** | A | S | C | S | S | A | SC-08/10/06/01 |
| 26 | CAP-14 | Experiential Memory Recall | **A*** | A | B | C | **S** | C | **S** | SC-09/02/04/05 |
| 27 | CAP-10 | Memory Consolidation & Fact Promotion | **A** | B | A | C | **S** | C | A | SC-05/09/10/02 |
| 28 | CAP-23 | Dynamic Model Routing & Selection | **A** | A | A | S | A | B | A | SC-05/01/02 |
| 29 | CAP-21 | Composite Plugin Packaging | **A** | A | A | B | A | A | B | SC-01/02/07 |
| 30 | CAP-28 | Execution Provenance & Non-Repudiation | **A** | A | A | A | A | S | S | SC-10/06/07 |
| 31 | CAP-31 | Supply-Chain Integrity & Manifest Verify | **A** | A | B | B | S | S | A | SC-07/02/08 |
| 32 | CAP-34 | Autonomous Self-Improvement | **A** | A | B | B | S | B | S | SC-01/05/06 |
| 33 | CAP-36 | Lifecycle Deprecation & Sunset Mgmt | **A** | A | A | B | A | S | S | SC-06/08/10 |
| 34 | CAP-02 | Agent Teams & Multi-Agent Coordination | **B** | A | B | C | S | B | A | SC-02/03/04/05 |
| 35 | CAP-11 | Typed Bi-Temporal KG Memory | **B** | C | B | C | A | C | C | SC-02/07/09 |
| 36 | CAP-12 | Semantic & Response Caching | **B** | C | B | A | B | C | C | SC-01/05 |
| 37 | CAP-33 | Meta-Evaluation & Grader Calibration | **B** | B | B | C | A | B | B | SC-06/08 |

> **A*** = CAP-14 arbitrated: G2 said S, arbiter said A. Tension verifier RECONCILED Global=A with sharp archetype divergence (S in C4/C6, C in C3/C5) — variance preserved, not averaged.

---

## 2. Tier Distribution

| Tier | Count | Elements |
|------|-------|----------|
| **S** (Foundational — non-negotiable core) | **21** | CAP-01,03,04,06,08,09,13,17,18,19,20,22,24,25,26,27,29,30,32,35,37 |
| **A** (Highly valuable most workflows) | **12** | CAP-05,07,10,14,15,16,21,23,28,31,34,36 |
| **B** (Useful, not universal) | **4** | CAP-02,11,12,33 |
| **C** | 0 | — |
| **D** (niche/redundant) | 0 | — |

**Reading:** Every ranked capability is at least B — the Phase 1 discovery had strong prior filtering; nothing in the final 48 is obviously niche/declining. The B-tier are archetype-specific (Agent Teams → C4; KG Memory → C4/C2; Semantic Cache → C3; Meta-Eval → C4).

---

## 3. S-Tier Rationale (Harm ≥4 Veto Compliance)

All 21 S-tier elements satisfy the **Harm 4-5 veto** (cannot rank below median when mitigating SC-07/03/08). Key SC-07 veto class (zero-tolerance security): CAP-24, 25, 26, 27, 20, 31. Key SC-02/03 fallback (reliability): CAP-03, 06, 01, 04, 30.

**Per-rubric dimension highlights:**
- **Highest generality (all 6 archetypes S):** CAP-24, 25, 26, 20, 37, 35, 08, 17, 22 — universal.
- **Sharpest archetype divergence (anti-averaging flag):** CAP-14 (C4/C6 S vs C3/C5 C), CAP-10 (C4 S vs C3 C), CAP-11 (C4 A vs C5/C6 C), CAP-12 (C3 A vs rest C), CAP-33 (C4 A vs C3 C), CAP-02 (C4 S vs C3 C).

---

## 4. Cross-Batch / Cross-Element Tension Resolutions (from tension verifier)

| Element Pair | Tension | Resolution |
|---|---|---|
| CAP-01 Subagent × CAP-07 Fan-out | Fan-out multiplies CPSR (SC-05) | Pareto frontier `pass@1 vs $/task` gate; budget CAP-35 governs |
| CAP-06 Isolated Workspace × CAP-24 Hermetic Exec | Both isolate — different plane | CAP-06 = VCS/workspace isolation; CAP-24 = OS/syscall containment — dual-boundary |
| CAP-20 Hooks × MEC-04 Hook Event Sys | Capability vs Mechanism | CAP-20 is the need; MEC-04 the event dispatcher |
| CAP-30 Reversibility × MEC-05 Tripartite Engine | Capability vs its 3 mechanisms | CAP-30 = contract; MEC-05 = FS snapshot + trajectory rewind + compensating inversion |
| CAP-13 RAG × CAP-14 Recall | External stateless vs internal stateful | Library vs notebook; distinct archives |
| CAP-29 HITL × autonomy (E7) | Over-HITL = babysitting | Per-archetype calibration: C5/C6 very low autonomy, C3 high |
| CAP-16 Budget × CAP-09 Compaction | Competition for window | P0-P10 priority chain; pinned set compaction-exempt |

---

## 5. Mechanism/Protocol Verification (from MECH_PROT scout) — feeds Phase 3

| ME/PR | Serves CAP | Level verified | Implemented-by (sources) |
|---|---|---|---|
| MEC-01 Git Worktree | CAP-06 | MEC ✅ | `git worktree`, worktree CLIs |
| MEC-02 Progressive Disclosure | CAP-18 | MEC ✅ | Skill loaders (Claude/agy SKILL.md) |
| MEC-03 Hierarchical Rule Inheritance | CAP-19 | MEC ✅ | `AGENTS.md`/`.cursorrules` traversal |
| MEC-04 Deterministic Hook Event Sys | CAP-20 | MEC ✅ | `PreToolUse`/`PostToolUse` dispatchers |
| MEC-05 Tripartite Reversibility | CAP-30 | MEC ✅ | FS snapshot + git revert + saga frameworks |
| MEC-06 JIT Credential Brokering | CAP-26 | MEC ✅ | Vault dynamic secrets, AWS STS |
| MEC-07 DLP Stream Sanitizer | CAP-26 | MEC ✅ | regex/NER streaming redactors |
| MEC-08 Cryptographic Flight Recorder | CAP-28 | MEC ✅ | append-only JSONL + hash chain |
| MEC-09 Budget Hard-Stop | CAP-35 | MEC ✅ | circuit-breaker on cumulative cost |
| MEC-10 Instinct Mining | CAP-34 | MEC ✅ | trajectory → heuristic distillation |
| PROT-01 Model Context Protocol | CAP-17 | PROT ✅ | `modelcontextprotocol/servers` |
| PROT-02 Function-Calling Schema | CAP-03/17 | PROT ✅ | JSON-Schema tool defs |
| PROT-03 Harness-as-Code Spec | CAP-37 | PROT ✅ | declarative YAML/JSON config |

---

## 6. Gate P2-18 — Recommendation

**PASS.** All 37 capabilities ranked with evidence from 10 independent agent sessions; 21 S-tier / 12 A-tier / 4 B-tier; Harm-4-5 veto enforced; tensions formally reconciled. **Ready for Phase 3 tool selection** (build harness slices for the S-tier elements first, per plan §P3-27).

**Open items:** the archetype matrix agy instance returned 0 bytes (non-blocking — per-archetype tiers embedded in G1-G5 rankers + tension verifier). Cleanup of opencode log-only files pending.

---
*Sources on disk: `phase-2/rankings/G1..G5.md`, `phase-2/verify/ARBITER_AGY.md`, `phase-2/verify/MECH_PROT_AGY.md`, `phase-2/verify/CROSSBATCH_TENSION.md`, `phase-2/RUBRIC.md`.*