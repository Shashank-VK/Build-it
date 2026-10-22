# Execution & Agency — Per-Element Knowledge Base (Phase 4, Batch D-1)

> **Date:** 2026-09-01 | **Sources:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-3/TOOL_SELECTION_INDEX.md`
> **Template:** 18-section per element (plan.md §Phase 4). Consolidated for the Execution layer.

---

## CAP-01 — Delegated Subagent Execution
1. **Overview:** Spawn isolated agent instances with bounded context, role prompts, scoped tool allowlists to execute decomposed subproblems.
2. **Why matters:** Prevents context-rot, main-agent overload; enables task parallelism (SC-09 CSP, SC-05 cost).
3. **How works:** Main orchestrator delegates via `description`-triggered subagent; subagents return summaries; isolated context windows.
4. **When use:** Long multi-step tasks, parallel exploration, expertise partitioning, research/agentic archetypes (C4/C6).
5. **When NOT:** Trivial single-tool tasks, bootstrapping, where delegation overhead > benefit.
6. **Importance:** S-tier. Freq 4, Harm 4, Benefit 5. Archetypes: C1=S, C2=S, C3=B, C4=S, C5=A, C6=S.
7. **Essential:** Claude Agent SDK, OpenAI Agents SDK (optional).
8. **Optional:** Codex `.codex/agents/*.toml` custom agents.
9. **Rules:** Keep parent context lean; return concise summaries; isolate tool scopes; cap fan-out.
10. **Deps:** CAP-03 orchestration, CAP-05 background, CAP-06 isolation.
11. **Integration:** Consumes orchestration layer; subagents run in isolated workspaces (E6).
12. **Failure modes:** Subagent context loss, tool over-permission, summary thrash.
13. **Security:** Tool allowlist per subagent (least-privilege); injection-scope subagent outputs.
14. **Maintenance:** Rotate role prompts; prune unused subagent types.
15. **Sources:** Master Taxonomy CAP-01; Batch-1 E1.
16. **Links:** https://code.claude.com/docs/en/sub-agents; OpenAI Agents SDK.
17. **Last verified:** 2026-09-01.
18. **Re-check:** New major subagent API version; harness archetype change.

---

## CAP-03 — Dynamic Orchestration & Control Flow
1. **Overview:** Architectural layer managing state machines, dynamic DAG sequencing, dependency resolution, failure recovery, non-deterministic branching.
2. **Why matters:** Central nervous system of autonomous runtime — recovers from tool errors, keeps SC-02/SC-03 healthy.
3. **How works:** State graph (nodes/edges), supervisor pattern, retry/replan loops.
4. **When use:** Any multi-step agent workflow with branching/retry.
5. **When NOT:** Deterministic single-path scripts (use CAP-04 workflows).
6. **Importance:** S-tier. Rank #1. Archetypes: C1-C4,C6=S; C5=A.
7. **Essential:** LangGraph, Temporal.
8. **Optional:** Durable workflows (n8n/Temporal for background).
9. **Rules:** Define explicit state transitions; checkpoint; bound retries (SC-03 ≤3).
10. **Deps:** CAP-01, CAP-04, CAP-05, CAP-06.
11. **Integration:** Subagents + workflows composed by orchestrator.
12. **Failure modes:** Infinite loops, state loss, unhandled exceptions (SC-02 <50%).
13. **Security:** Strict transition boundaries; prevent unconstrained recursion.
14. **Maintenance:** Runtime abstraction keeps per-project maintenance low.
15. **Sources:** Batch-1 E3; LangGraph docs.
16. **Links:** https://langchain-ai.github.io/langgraph/; https://temporal.io.
17. **Last verified:** 2026-09-01.
18. **Re-check:** New orchestration runtime major version.

---

## CAP-04 — Deterministic Workflows & Blueprints
1. **Overview:** Predefined reusable multi-step execution graphs (trigger → steps → gates) without unnecessary LLM routing.
2. **Why matters:** Repeatability + compliance; deterministic paths avoid LLM cost/flake.
3. **How works:** YAML/DSL blueprints; gates/checksums; re-runnable idempotent steps.
4. **When use:** Known repeatable processes (build-verify, refactor-safely, migration-safe).
5. **When NOT:** Novel/non-deterministic exploratory tasks.
6. **Importance:** S-tier. C2/C3/C5/C6=S; C1=A; C4=B.
7. **Essential:** Workflow YAML blueprints (in `.harness/workflows/`).
8. **Optional:** Taskfile/n8n.
9. **Rules:** Idempotent steps; deterministic triggers; version blueprints.
10. **Deps:** CAP-03 orchestration for dynamic parts.
11. **Integration:** Blueprints invoked by orchestrator/background.
12. **Failure modes:** Drift (SC-10), stale schema.
13. **Security:** Gate destructive steps behind HITL (CAP-29).
14. **Maintenance:** Keep blueprints in version control.
15. **Sources:** Batch-1 E4.
16. **Links:** `.harness/workflows/*.yaml` (in repo).
17. **Last verified:** 2026-09-01.
18. **Re-check:** New workflow engine; blueprint drift.

---

## CAP-05 — Background & Async Queued Execution
1. **Overview:** Decoupled async lifecycle (queued → running → completed/failed), survives client disconnect.
2. **Why matters:** Long-running tasks without blocking (compile/test/lint); fleet scale.
3. **How works:** Queue/poll/SSE/webhook patterns.
4. **When use:** Long jobs, CI, fleet automation (C3).
5. **When NOT:** Interactive short tasks.
6. **Importance:** A-tier. C2/C3=S; rest A.
7. **Essential:** Temporal; (Optional: n8n/Trigger.dev).
8. **Optional:** Cloud queues.
9. **Rules:** Return `202` early; persist state; dead-letter.
10. **Deps:** CAP-06 isolation; hooks for status.
11. **Integration:** Subagents/workflows run in background.
12. **Failure modes:** Orphaned jobs; state loss on crash.
13. **Security:** Scoped credentials in isolated env.
14. **Maintenance:** Drain/retry policies.
15. **Sources:** Batch-1 E5.
16. **Links:** https://temporal.io.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Queue/SDK major changes.

---

## CAP-06 — Isolated Workspace Management
1. **Overview:** Per-agent/per-task filesystem isolation via git worktree/containers to prevent clobbering/race/drift.
2. **Why matters:** Enables safe parallel agents + deterministic state (SC-06, SC-10).
3. **How works:** `git worktree` per agent branch; optional container overlay.
4. **When use:** Parallel agents, migrations, IaC blast-radius.
5. **When NOT:** Single-sequential tasks.
6. **Importance:** S-tier. C1/C5/C6=S; C2/A; C3/B.
7. **Essential:** `git worktree` CLI.
8. **Optional:** gwq/Vibora wrappers.
9. **Rules:** Idempotent create/diff/merge/remove; branch naming `.agents/*`.
10. **Deps:** git; CAP-24 hermetic boundary.
11. **Integration:** Subagent/workflow execution substrate.
12. **Failure modes:** Uncommitted drift, branch pollution.
13. **Security:** Boundary + sandboxing separate (batch-4 V-D).
14. **Maintenance:** Prune stale worktrees.
15. **Sources:** Batch-1 M1/E6; 5 harness impls.
16. **Links:** https://git-scm.com/docs/git-worktree.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Worktree tooling changes.

---

## CAP-07 — Parallel Execution & Fan-Out
1. **Overview:** Bounded concurrent execution of decomposed subtasks with rate-limiting + fan-in.
2. **Why matters:** Speed (SC-01); parallelization cost/benefit Pareto (SC-05).
3. **How works:** Concurrency pool; thread/container fan-out; fan-in aggregation.
4. **When use:** Search/exploration, deep research, batch jobs.
5. **When NOT:** Low-width tasks, sequential deps.
6. **Importance:** A-tier. C2/C4/C6=S; C1/C3=A; C5=C.
7. **Essential:** Orchestrator-native (LangGraph/parallel).
8. **Optional:** Thread pools.
9. **Rules:** Bound concurrency; weight vs cost; aggregate carefully.
10. **Deps:** CAP-03, CAP-06 isolation.
11. **Integration:** Fan-out workers within workspaces.
12. **Failure modes:** Rate-limit, resource exhaustion.
13. **Security:** Scoped per-worker tokens.
14. **Maintenance:** Tune pool sizes.
15. **Sources:** Batch-1 E9.
16. **Links:** LangGraph `Send`/parallel; opencode/agy threads.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Concurrency behavior change.

---

## MEC-01 — Git Worktree Isolation Primitive
1. **Overview:** Git filesystem branching creating isolated checkouts (`.agents/*`) for concurrent subagents.
2. **Why matters:** Cheap native isolation substrate for CAP-06/CAP-01.
3. **How works:** `git worktree add` per branch; idempotent lifecycle.
4. **When use:** Parallel edits; migration dual-writes.
5. **When NOT:** Where container isolation needed (CAP-24).
6. **Importance:** Foundational mechanism (S-tier impl).
7. **Essential:** `git worktree`.
8. **Optional:** Custom CLIs.
9. **Rules:** Idempotent create/diff/merge/remove.
10. **Deps:** git.
11. **Integration:** Backs CAP-06; hook `WorktreeCreate`.
12. **Failure modes:** Branch conflicts, stale worktrees.
13. **Security:** Non-sandbox (VCS-level only).
14. **Maintenance:** Prune.
15. **Sources:** Batch-1 M1.
16. **Links:** git-worktree(1).
17. **Last verified:** 2026-09-01.
18. **Re-check:** git changes.

---

*End of D-1 (Execution). See also `.harness/workflows/` + `.harness/agents/` for materialized forms.*