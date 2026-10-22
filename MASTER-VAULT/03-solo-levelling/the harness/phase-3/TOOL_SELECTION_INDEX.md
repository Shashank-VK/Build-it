# Phase 3 — Tool Selection Index (P3-30) — Essential / Optional / Avoid

> **Status:** CONVERGED — ALL 8 tool batches + verification + overlap + slice build | **Date:** 2026-09-01
> **Fleet:** 26-agent Phase 3 operation — 8 selectors (T-A..T-H, via agy) + 2 verifiers + overlap sweep + slice build
> **Sources on disk:** `phase-3/tools/T-*.md` (8 files, 262K) · `phase-3/verify/VERIFICATION_PASS1.md` + `VERIFICATION_PASS2.md` · `phase-3/verify/CROSS_TOOL_OVERLAP.md` · `harness-slice/HARNESS_SLICE.md` (38K)
> **Input:** `phase-1/MASTER_TAXONOMY.md` + `phase-2/RANKINGS.md` (21 S / 12 A / 4 B)

---

## 1. Verification Gate Summary

- **Pass 1** (15.7K): audited T-B (Context), T-D (Safety), T-F (A-tier), T-H (B-tier) — link valid, maintenance <6mo, adoption, relevance, compatibility, license.
- **Pass 2** (27.4K): audited T-A (Execution), T-C (Integration/Skills), T-E (DX/Meta), T-G (A-tier2).
- **Cross-tool overlap** (33K): KEEP/SPLIT/REMOVE resolved — e.g., LiteLLM SPLIT (Gateway vs Budget Governor), RouteLLM REMOVED (gate fail), gVisor KEPT at PRIMARY (Hermetic Exec).

## 2. Final Essential Toolset (deduplicated, verified)

### Execution (CAP-01/03/04/05/06/07)
| Tool | Type | Serves | Tier | Verified |
|------|------|--------|------|----------|
| **Claude Agent SDK** | SDK | CAP-01 Subagent | **Essential** | ✅ |
| **LangGraph** | Framework | CAP-03 Orchestration | **Essential** | ✅ |
| **Temporal** | Workflow engine | CAP-03/04 | **Essential** | ✅ |
| **git worktree** (`git worktree` CLI) | CLI | CAP-06 Isolation | **Essential** | ✅ |
| **n8n / Trigger.dev** | Background flows | CAP-05 | Optional | ✅ |
| **OpenAI Agents SDK** | SDK | CAP-01 | Optional | ✅ |

### Context & Memory (CAP-08/09/13/15/10/14/16)
| Tool | Type | Serves | Tier | Verified |
|------|------|--------|------|----------|
| **Qdrant / pgvector** | Vector DB | CAP-13 RAG | **Essential** | ✅ |
| **LlamaIndex / Haystack** | RAG stack | CAP-13 | **Essential** | ✅ |
| **Letta (MemGPT)** | Memory | CAP-09/10/14 | **Essential** (long-horizon C4) | ✅ |
| **Mem0 / Zep** | Memory | CAP-10/14 | Optional | ✅ |
| **tiktoken** | Token counter | CAP-08/16 | **Essential** | ✅ |

### Integration & Skills (CAP-17/18/19/20/22/23)
| Tool | Type | Serves | Tier | Verified |
|------|------|--------|------|----------|
| **MCP (modelcontextprotocol/servers)** | Protocol+servers | CAP-17 | **Essential** | ✅ |
| **40-Skill catalog** (from T-C) | Skills | CAP-18 | **Essential** — see `harness-slice` for implemented TDD skill + full index | ✅ |
| **LiteLLM** | Model Gateway+budget | CAP-22/35 | **Essential** (SPLIT: gateway + budget governor) | ✅ |
| **mcp.so / Glama** | MCP registries | CAP-17 | Optional | ✅ |
| **Claude/AGENTS.md rules files** | Rules | CAP-19 | **Essential** | ✅ |

### Safety (CAP-24/25/26/27/29/30)
| Tool | Type | Serves | Tier | Verified |
|------|------|--------|------|----------|
| **gVisor / Docker ephemeral sandbox** | Sandbox | CAP-24 | **Essential** | ✅ |
| **OPA / Cedar** | Policy engine | CAP-25 | **Essential** (Cedar in slice) | ✅ |
| **HashiCorp Vault** | Secrets | CAP-26 | **Essential** | ✅ |
| **PromptInjectionDefender / trust fencing** | Injection defense | CAP-27 | **Essential** | ✅ |
| **LangGraph HITL / ADK confirmation** | HITL | CAP-29 | **Essential** | ✅ |
| **git rollback + saga frameworks** | Reversibility | CAP-30 | **Essential** | ✅ |

### DX / Meta (CAP-32/35/37)
| Tool | Type | Serves | Tier | Verified |
|------|------|--------|------|----------|
| **Inspect AI** | Eval harness | CAP-32 | **Essential** | ✅ |
| **SWE-bench runner / Terminal-Bench** | Benchmark | CAP-32 | **Essential** | ✅ |
| **Promptfoo** | Eval assertions | CAP-32/33 | **Essential** | ✅ |
| **Langfuse** | Cost/telemetry | CAP-35 | **Essential** | ✅ |
| **gitleaks / pre-commit / Ruff** | AHG gate | CAP-37 | **Essential** | ✅ |
| **agy lifecycle hooks (pre/post-tool)** | Hooks | CAP-37 | **Essential** | ✅ |

### A-tier (verified)
| Tool | Type | Serves | Tier |
|------|------|--------|------|
| **Temporal** | Background | CAP-05 | Optional |
| **OpenRouter** | Routing | CAP-23 | Optional |
| **OpenTelemetry / Arize Phoenix** | Provenance | CAP-28 | **Essential** |
| **Sigstore / SLSA** | Supply-chain | CAP-31 | **Essential** |
| **LangSmith** | Self-improvement | CAP-34 | Optional |

### B-tier (verified)
| Tool | Type | Serves | Tier |
|------|------|--------|------|
| **CrewAI / AutoGen** | Agent Teams | CAP-02 | Optional |
| **Neo4j / Graphiti** | KG Memory | CAP-11 | Optional |
| **RedisVL / LangCache** | Semantic cache | CAP-12 | Optional |

## 3. Explicit Avoid (gate-failed)
- **RouteLLM** — failed verification gate (REMOVED)
- **Lakera Guard** — gate failure (REMOVED)
- Overweight SaaS-only MCP servers — lock-in risk

## 4. Harness Slice (build-as-you-go result)
`harness-slice/HARNESS_SLICE.md` (38K) — real working skeleton: `AGENTS.md` manifest, dir structure, MCP config, hooks.json + Python pre/post-tool guards + lefthook.yml, Cedar ABAC policy + per-archetype permission presets, 40-skill index + TDD SKILL.md, LiteLLM budget router. This is the **start of the actual versioned harness** (`.harness/`).

## 5. Gate P3-31 — Recommendation
**PASS.** All tools verified; overlaps deduplicated; harness slice built. **Ready for Phase 3.5 empirical validation** — run the slice against 2-3 real tasks.

**NEEDED FROM YOU (before P3.5):** nominate 2-3 real tasks/projects to validate the harness against (real work, not toys).