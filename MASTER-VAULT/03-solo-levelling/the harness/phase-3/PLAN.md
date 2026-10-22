# Phase 3 — Tool/Resource Selection — Deployment Plan (20-30 agents, agy + opencode)

> **Date:** 2026-09-01 | **Predecessor:** Phase 1 (48-element MASTER_TAXONOMY) + Phase 2 (21 S / 12 A / 4 B rankings) → Gate P2-18 APPROVED
> **Input:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-2/RUBRIC.md`, `phase-2/verify/MECH_PROT_AGY.md` (mech→tool mapping)
> **Repos on disk:** `phase-3/tools/*.md` per element batch

## Objective

Select actual tools/resources/Skills/MCP servers/frameworks for the harness — Essential / Optional / Avoid per element — with the verification gate (link valid, maintained, adopted, relevant, compatible, licensed). Build minimal working harness slices **as we go** (anti-bloat, integration-friction exposure).

## Agent Fleet (26 agents — mix of agy + opencode)

| Batch | Agents | Tool | Element Scope | Deliverable |
|-------|--------|------|---------------|-------------|
| **T-A** | A1, A2 (open) | opencode | S-tier Execution (CAP-01,03,04,05,06,07): orchestration frameworks (LangGraph/Temporal/LangChain), worktree CLIs, subagent SDKs | `tools/T-A_EXECUTION.md` |
| **T-B** | B1, B2 (agy) | agy | S-tier Context (CAP-08,09,13,15): compaction libs, vector DBs (Qdrant/Pinecone/Chroma), RAG stacks, memory stores | `tools/T-B_CONTEXT.md` |
| **T-C** | C1, C2, C3 (open) | opencode | S-tier Integration (CAP-17,18,19,20,22,23): MCP servers + registries, Skills (Anthropic+community), rules tools, hooks CLIs, LiteLLM/Portkey | `tools/T-C_INTEGRATION.md` |
| **T-D** | D1, D2 (agy) | agy | S-tier Safety (CAP-24,25,26,27,29,30): sandboxes (gVisor/Firecracker), policy engines (OPA/Cedar), secret tools (Vault), injection defense, HITL tooling | `tools/T-D_SAFETY.md` |
| **T-E** | E1, E2 (open) | opencode | S-tier DX/Meta (CAP-32,35,37): eval harnesses (SWE-bench/Terminal-Bench), cost trackers, harness-config tools | `tools/T-E_DX_META.md` |
| **T-F** | F1, F2 (agy) | agy | A-tier: Background (Temporal/n8n), Memory (Mem0/Zep/Letta), Semantic Cache, Routing (OpenRouter) | `tools/T-F_A_TIER.md` |
| **T-G** | G1, G2, G3 (open) | opencode | A-tier: Provenance, Supply-Chain (Sigstore/SLSA), Deprecation, Self-Improvement, HITL | `tools/T-G_A_TIER_2.md` |
| **T-H** | H1, H2 (agy) | agy | B-tier + niche: Agent Teams, KG Memory, Semantic Cache, Meta-Eval | `tools/T-H_B_TIER.md` |
| **Verify** | V-A, V-B (open) | opencode | **Verify gate on ALL Essential selections**: link validity (fetch URLs), maintenance (recent commits), adoption (stars/usage), licensing | `verify/TOOL_VERIFICATION.md` |
| **Build** | BU-A, BU-B, BU-C (agy) | agy | **Build minimal slice**: assemble selected S-tier tools into a working harness skeleton, expose integration conflicts | `harness-slice/` |
| **Cross** | X-A (agon) | opencode | Cross-element overlap sweep — dedupe tools selected under multiple elements | `verify/CROSS_TOOL_OVERLAP.md` |

**Total: 26 agents** (9 batches × 2-3 agents each) — ~14 agy + ~12 opencode. Parallel per batch; quality enforced (each reads Master Taxonomy + RANKINGS + applies verification gate).

## Verification Gate (from plan.md §PHASE 3 — applied to every Essential tool)

- **Link validity** — repo/site exists (fetch resolves)
- **Maintenance** — meaningful commit/release within 6-month window
- **Independent corroboration** — evidence beyond project's own README
- **Real adoption** — usage/star evidence
- **Functional relevance** — solves the stated problem
- **Compatibility** — fits harness architecture
- **License** — clean, non-viral preferred

## Anti-bloat guard (applied every batch close)

Each tool that reaches Essential must answer: materially improves? actually used? benefit > complexity? redundant? removable?

## Known tooling constraint

- **agy** — `-dangerously-skip-permissions` needed (headless permission auto-deny); reliable output via `tee`
- **opencode** — emit with plain `opencode run "..." 2>/dev/null | tee` (NOT `--print-logs` which pollutes stdout); long prompts cause truncation — keep prompts focused

## Next

Execute batches T-A..T-H in parallel (8 full batches), then verify (V-A/V-B), cross-overlap (X-A), build slice (BU-A..C), converge `phase-3/TOOL_SELECTION_INDEX.md`, gate → Phase 3.5.