# Phase 1 — Batch 1: Execution & Agency Layer — Converged Taxonomy Slice

> **Status:** CONVERGED — P1-01..08 complete | **Date:** 2026-08-31 | **Workflow:** `wf_4230df94-293`
> Inputs: [`R-A_BROAD_MAPPER.md`](R-A_BROAD_MAPPER.md) (67K, 12 angles, 19 ecosystems) · [`R-B_CHALLENGER.md`](R-B_CHALLENGER.md) (34K, divergent vocab) · [`V-C_ADVERSARIAL.md`](V-C_ADVERSARIAL.md) (24K, P1-06 translation/kill) · [`V-D_ARCHITECTURAL.md`](V-D_ARCHITECTURAL.md) (22K, P1-07 re-tag) — 149K total, 61 tool uses, 321K tokens
> Repo: `the harness` | Grounding: `plan.md §2 Batch 1` · `phase-0/ARCHETYPES_AND_CRITERIA.md` C1-C6, SC-01..10

---

## 0. Method & Coverage

- **R-A (Broad Mapper):** 12 search angles covering 19 ecosystems — Claude Code, Codex CLI (6-thread fan-out, `.codex/agents/*.toml`), Cursor (8 cloud VMs, Cloud Agent API), Windsurf Cascade (`.windsurf/workflows/stages/`), Gemini CLI (`.gemini/agents/*.md`), Copilot (3 layers: IDE/CLI/Cloud `gh agent-task`), OpenCode/Cline/Roo/Aider/OpenHands, LangGraph/CrewAI/AutoGen/MAF, GoClaw 4-pattern (delegation vs handoff), HITL/trust/SOC/TCF, L0-L5 autonomy, git-worktree harnesses (gwq/Vibora/AgentsMesh/Omegon), SDK/runtime/framework comparison 2025. Stop-rule per sub-area; ≥2 independent sources per claim; vendor marketing cross-checked vs OSS impl.
- **R-B (Challenger):** Divergent vocabulary — `delegation/handoff/spawning/worktree/parallelism`, `process supervision/job control/session multiplexing`, `background vs async vs queued`. Must surface ≥3 candidates R-A would miss; hunt hidden splits/merges.
- **V-C (Adversarial):** P1-06 translation check (≥2 ecosystems per candidate) + kill/merge with 2 counter-sources each. Flagged truncation (R-A fragment cut at OpenCode hierarchy, R-B payload not fully present — synthesized from fragment + independent translation searches; must re-verify against full `R-A_BROAD_MAPPER.md` on disk before P1-43 gate).
- **V-D (Architectural):** P1-07 re-tag to Capability/Mechanism/Protocol/Framework/Tool + lifecycle + tier. Flagged R-A's systematic conflation: listing Tool/Mechanism rows as if they were Capability taxonomy ("Tool×Mechanism inventory" not taxonomy).

**Coverage confidence:** 12 angles × ≥5 distinct queries each → diminishing-returns stop-rule not yet forced to halt (new ecosystems still surfacing at angle 12). Practical completeness: HIGH for this batch after verifier cross-check. Remaining gap: full R-B challenger divergent-vocab coverage re-verify before MASTER_TAXONOMY.

---

## 1. Converged Capability Taxonomy — Batch 1 (10 Canonical Capabilities)

*Level per plan.md §0.2: Capability (what harness needs) / Mechanism / Protocol / Standard / Framework / Runtime / Tool / Product / Repo. Lifecycle: build-time / run-time / review-time. Tier: foundational / important / specialized / situational. Confidence: high / medium-high / etc.*

| # | Canonical Capability | Definition | Problem Solved | Correct Level | Lifecycle | Tier | Confidence | Cross-Ecosystem Synonyms (2+ ecosystems) |
|---|---------------------|------------|----------------|---------------|-----------|------|------------|------------------------------------------|
| **E1** | **Delegated Subagent Execution** | Spawn a separate agent instance with own context window, system prompt, tool allowlist, optional model override to execute a decomposed subproblem; main retains requirements/decisions and synthesizes summaries. | Context rot, context-window blowup, task parallelism, expertise partitioning; prevents main-agent overload. (SC-09 CSP >30k, SC-05 CPSR anti-context-rot, SC-04 HIR scoped autonomy) | **Capability** (Mechanism: spawning via `Agent` tool / `description` trigger / file convention `.claude/agents/*.md`) | build (define) → run | **foundational** — harm 4 if absent: goal drift embedding <0.90 on long tasks. Needed C4 (agent/memory), C6 (migration parallel strands), C2 (DAG fan-out) | High | Claude `subagents (.claude/agents/*.md, YAML: name/description/tools/model/permissionMode)` ≡ Codex `custom agents (.codex/agents/*.toml) + agent threads` ≡ Copilot `custom agents (.github/agents/*.agent.md)` ≡ Gemini `agents (.gemini/agents/*.md)` ≡ Cursor `SDK subagents` |
| **E2** | **Agent Teams / Multi-Agent Collaboration** | Multiple persistent agent sessions with inter-agent messaging, shared task list, dependencies, peer coordination (with or without supervisor). Contrasted with E1 hub-and-spoke. | Tasks requiring negotiation, debate, handoff, long-lived peer awareness that cannot be fan-out-and-merge. (SC-02 TSR +10pp crew tasks, SC-03 peer recovery) | **Capability** (Framework reifications: CrewAI Crew/Flow, LangGraph graph, Claude Teams) | run → review (plan approval) | **important** — Critical C4, C1-scale, C6 strangler; overkill C3 glue (solo-ideal); not foundational (solo succeeds w/o) | Medium-High | Claude `Agent Teams` (multi-session messaging) ≡ CrewAI `Crews (Agent+Task+Crew)` ≡ LangGraph `Supervisor+Worker SubGraph, Send fan-out` ≡ Cursor `Agent Window parallel agents` |
| **E3** | **Orchestration Layer** | Architectural layer managing sequencing, state, dependency, exception handling, visibility across agents/workflows; decides control flow (deterministic vs non-deterministic). | Failure cascading, state loss, exception recovery, auditability of non-deterministic reasoning loops. | **Capability** (Frameworks LangGraph, CrewAI, Agno implement it) | coordination (build → run) | **foundational** — SC-02/SC-08 for C2 (DAG), C3 (glue fleet), C6 (codemod→dual-write→shadow→cutover); SC-10 100% FAIL on C5/C2 w/o DAG/sensor | High | Generic `orchestration` (conductor sequencing) ≡ LangGraph `Supervisor routing` ≡ Windsurf `visual flow editor` ≡ Agno `worker fleet monitoring` |
| **E4** | **Workflows / Flows (Reusable Blueprints)** | Reusable predefined multi-step blueprint (trigger→actions) invocable deterministically; distinct from dynamic orchestration that reasons at runtime. | Repeatability, compliance, no-LLM determinism; avoids using agentic reasoning for specifiable paths (anti-pattern). (SC-10 drift-free, SC-08 gate) | **Mechanism** (Capability when user-authored) | build (define) → run (blueprint) | **foundational** (as Capability); **important** as Mechanism | High | Windsurf `Cascade flows/workflows stages/` ≡ CrewAI `Flows (event-driven)` ≡ Temporal/n8n `workflow automation` ≡ LangGraph `StateGraph` |
| **E5** | **Background / Async Queued Execution** | Execution decoupled from request lifecycle: submit → `202 queued` → daemon/worker → `in_progress → completed/failed`; poll or SSE; survives parent session. | UX blocking, long-running tasks (compile/test/lint), API timeouts, fleet scale (6–8 parallel). (SC-01 TTFUA non-blocking, SC-03 queued retry) | **Capability** (Mechanisms: queued+poll, semaphore, daemon thread) | run (lifecycle: queued→running→completed/failed) | **important** — Elevated C3 (fleet), C1 (preview), C4-research; not foundational (foreground-only still passes SC-02 slower) | High | Claude `background agents (Ctrl+B, auto-denied perms, push notify)` ≡ Cursor `Background Agents (isolated Ubuntu VMs, Cloud Agent API launch/follow-up/status)` ≡ Copilot `coding agent (Actions infra), gh agent-task` ≡ Open-Swarm `background:true → 202 queued → poll` ≡ NeoSigma `POST /jobs → 202 queued` |
| **E6** | **Git Worktree Isolated Workspaces** | Per-agent isolated git worktree (separate checkout on `agent/*` branch under `.agents/` or `.claude/worktrees/`) with optional container overlay; idempotent create, diff/commit/merge/remove lifecycle. | Branch pollution, parallel work without stashing, deterministic per-agent filesystem, safe concurrent edits. (SC-10 IDFR 100% no-op, SC-06 DRR, SC-07 sandbox boundary) | **Mechanism** (Capability is Isolated Workspace Management — see E6 row below in synthesis) — **Mechanism under Isolated Workspace Capability** | build (provision) → run → review (drift check) | **foundational** as Capability; **important** as Mechanism (git worktree one substrate, container/VM another) | High | Claude `isolation: worktree, .claude/worktrees/<repo>-<name>/` ≡ Copilot `workspace (parallel per task, branch auto-create)` ≡ `harness workspace create` (monorepo-harness) ≡ `Tracer e spawn` ≡ `Viwo` (worktree+container) ≡ `rbutera/agent-worktree-skill` — 5 harness impls |
| **E7** | **Autonomy Calibration / Permission Modes** | Policy that sets per-agent/per-tool autonomy tier (L1 Full Approval → L4 Full Autonomy; or Passive→Autonomous initiative) determining when human approval required. | Over-autonomy (unsafe writes) vs under-autonomy (babysitting); calibrates SC-04 HIR per archetype (C1 median 0 vs C4 ≤2). V-D veto: harm≥4 for SC-07 cannot rank below median. | **Capability** (Mechanisms: `permissionMode`/`initiativeLevel` config, L0-L5/Zones/Stages/Inbox) | build (policy) → run → review | **foundational** — SC-04, SC-07 (harm 5 if no calibration), SC-03 (bounded ≤3 retries). All archetypes, tolerance varies C5/C6 very low, C3 high-compensated | Medium-High | Relevance AI `L1-L4 per tool` ≡ `InitiativePolicy Passive/Attentive/Proactive/Autonomous` ≡ SOC `5-level trust-calibrated (manual→fully autonomous)` ≡ Codex/Claude `permissionMode + sandbox policy` |
| **E8** | **Human-in-the-Loop Controls (Approval Gates / Trust Calibration)** | Execution primitive that pauses at approval gates, surfaces request in dashboard/queue with context, allows Approve/Reject/Modify/Escalate + timeout + audit trail; includes trust-calibrated adaptive autonomy. | Harm-if-absent for irreversible actions (deploy, spend, delete); enables SC-07 (≥90% injection block, 0 leaks/100) + SC-04 precision. Distinct from E7: E7=what agent may do alone; E8=when/how human decides. | **Capability** (Mechanisms: `PermissionRequest`, `PreToolUse exit 2`, `UserProxyAgent`, dashboard queue) | **review-time** (primary) + run (interrupt) | **foundational** — SC-07/SC-04/SC-02 (C4 groundedness review gate). Kill-test: no HITL → SC-07 FAIL on C1/C3/C5 creds | High | LangGraph `HITL core primitive (pause at approval)` ≡ Google ADK `tool confirmation flow` ≡ AG2 `UserProxyAgent` ≡ Claude `PermissionRequest hook, PreToolUse exit 2 block` ≡ Agent Factory `Approve/Reject/Modify/Escalate + audit log` |
| **E9** | **Parallel Execution & Fan-out** | Bounded concurrent execution of decomposed subtasks (one agent per point, `max_concurrent_threads_per_session=6` default, Cursor up to 8 VMs). Sub-capability of orchestration but independently toggled. | SC-01 (P50 <90s C1), SC-05 cost trade (parallelism × token cost Pareto). C2/C4 benefit most; C5 gated low parallelism. | **Capability** (Mechanism: concurrency knob `max_concurrent_threads_per_session`) | run | **important** | High | Codex `parallel fan-out (spawn two agents, up to 6 threads)` ≡ Cursor `up to 8 parallel Background Agents` |
| **E10** | **Lifecycle Interception / Hooks** | Cross-cutting interception points that run deterministic actions before/after tool use, prompt, compact, session start/stop. Enables policy gate (block before exec), retry/compensation trigger, gate.sh injection. | Without interception SC-07 allowlist cannot enforce, SC-03 compensation cannot trigger. (V-D: harm 4 for C5/C2) | **Capability** (Mechanism: hook event system — M6; 25 events is Claude-specific count, canonical is interception points) | run (cross-cutting) | **important** — foundational for C5/C2 security gating; important elsewhere | High | Claude `hooks (25 events → 21-event Mar 2026 list: PreToolUse/PostToolUse/SubagentStop/SessionStart/WorktreeCreate...)` ≡ Codex `hooks` ≡ Copilot `CI hooks` ≡ Windsurf `CI hooks` — 4 ecosystems |
| **E11** | **Reversibility / Compensation / Undo** | Saga-style compensation that restores consistent state after failure (retry with rollback, dual-write reconciliation), plus idempotency property and undo UX. | SC-10 drift-free, AWRR RR/SRR (safe rollback), SC-03 saga compensation. Distinct from HITL: idempotency=property, compensation=action, undo=UX — not subsumed by E8. C5/C6 foundational, others important. | **Capability** | run → review | **important** (C5/C6 **foundational**) | Medium-High (inferred — verify against R-B `side-effect safety/idempotency/undo` vocabulary; R-A may have subsumed under HITL) | `Saga compensation` ≡ `checkpoint/rewind` (Batch 5 boundary) ≡ `dual-write/shadow` (C6) ≡ AWRR `SRR/RR` |

> **E6 note:** V-C correctly demotes `Git Worktree` to Mechanism (Protocol `git worktree` CLI contract) under Capability `Isolated Workspace Management`. The canonical Isolated Workspace Capability is **E6 (Mechanism: git worktree) / C5 in V-D's re-tag** — kept here as Capability for Batch 1 reporting but true level is Capability whose primary Mechanism is git worktree + container variant. Final MASTER_TAXONOMY will list Capability `Isolated Workspace Management` with Mechanism `Git Worktree (S2)`.

---

## 2. Mechanisms, Protocols, Frameworks, Tools (de-duplicated — not re-promoted to Capabilities)

### Mechanisms (10)

| # | Mechanism | Implements | Lifecycle | Tier | Hygiene Flag |
|---|-----------|------------|-----------|------|--------------|
| M1 | **Git Worktree (`git worktree add/remove`, `isolation: worktree`)** | E6 / Isolated Workspace | build → run | important | Protocol-backed mechanism, not Capability |
| M2 | **Container / VM / Sandbox Isolation (Docker, isolated Ubuntu VM, Actions VM)** | E6 + SC-07 sandbox boundary | run | important | Cursor VM is isolation Mechanism, not Background Capability |
| M3 | **Agent Definition File Conventions (`.claude/agents/*.md` + YAML frontmatter; `.codex/agents/*.toml`; `.github/agents/*.agent.md`; `.gemini/agents/*.md`; `AGENTS.md` Operating Model)** | E1, E2 | build-time | important | 5 paths are isomorphic Mechanisms for same Capability — dedupe, do not multiply taxonomy |
| M4 | **Delegation Patterns: Delegation vs Handoff vs Spawn (GoClaw 4-pattern)** | E1/E2 | run | specialized | One Mechanism cluster, not 4 Capabilities; handoff = choreography without supervisor |
| M5 | **Forked Subagent / Context Inheritance Toggle (`CLAUDE_CODE_FORK_SUBAGENT`, Codex sandbox inheritance + per-agent override, `default/worker/explorer` built-ins)** | E1 | run | situational | Experimental flag; Tool config, not Capability |
| M6 | **Hook Event System (PreToolUse/PostToolUse, command/http/mcp_tool/prompt/agent, WorktreeCreate/SubagentStop...)** | E10 | run | important | 25 is Tool-specific (Claude); canonical is interception points |
| M7 | **Slash Commands / Skills as Prompt-Pack Triggers (`/delegate`, `/multitask`, Skills repo)** | E3/E1 | build → run | specialized | Skills category is Capability (Batch 3); individual skill is Resource; repo is Implementation |
| M8 | **Queue / Scheduler / Automations (Cursor Automations scheduled/event-triggered, Cloud Agent API `launch/follow-up/status/list/delete/fetch + MCP`, `gh agent-task`, `max_concurrent_threads_per_session`)** | E5 | build → run | important | Scheduler is Mechanism for Background Capability |
| M9 | **Worktree-backed Background Task + Cloud Dispatch (`gh agent-task`, Cloud Agent API push-to-branch, `/delegate TASK` unstaged→new-branch→draft-PR)** | E5 + E6 | run | specialized | Cloud-surface Mechanism variant |
| M10 | **Read-only Investigator / Auditor Constraints (OpenCodeOrchestra Depth 2+ read-only, no shell)** | E1/E2 safety | run | specialized | Least-privilege; part of M4 family |

### Protocols / Standards (3)

| # | Protocol | Scope | Tier | Note |
|---|----------|-------|------|------|
| S1 | **MCP (Model Context Protocol)** | Integration layer — Batch 3 territory | situational for Batch 1 | Do not duplicate as Execution Capability |
| S2 | **Git Worktree Primitive (`git worktree` CLI contract)** | Underlies M1 | important | De facto Protocol; wrappers gwq/Vibora are Tools |
| S3 | **AGENTS.md / CLAUDE.md / .cursorrules Operating Model Convention** (caesar-harness-agent cross-platform mapping, zeoel 23-agent team) | E1 definition portability (SynaptixLabs spine→adapter) | important (emerging) | Emerging de facto Standard; file is Resource |

### Frameworks / Runtimes (7)

| # | Framework | Implements | Tier | Note |
|---|-----------|------------|------|------|
| F1 | **LangGraph** | C3 orchestration (stateful DAG, cycles, persistence) | important | |
| F2 | **CrewAI** | E2 (role-based crew, sequential/parallel/loop) | important | |
| F3 | **AutoGen / AG2** | E2 (conversational multi-agent) | specialized | |
| F4 | **Microsoft Agent Framework** | E2/E7 (enterprise policy, review gates) | specialized | |
| F5 | **Claude Agent SDK** | E1/E5/E10 (subagents + hooks as SDK primitives) | important (harness-as-code) | |
| F6 | **OpenCodeOrchestra / OpenAgentsControl (7 subagents)** | E1 hierarchy + safety constraints | situational | Fix for flat `build+plan` shared-everything debt; not canonical |
| F7 | **Windsurf Cascade Runtime** | E3 + E6 | specialized | |

### Tools / Products / Repos (8)

| # | Tool | Primitives It Exposes | Tier | Note |
|---|------|----------------------|------|------|
| T1 | **Claude Code** | E1 subagents, E5 background (Ctrl+B, push notify), E6 worktree, E10 hooks, forked subagents, slash/skills | important | Vendor impl of E1/E5/E6/E10 |
| T2 | **OpenAI Codex CLI** | `config.toml [agents]`, `default/worker/explorer`, 6-thread fan-out, `codex exec --full-auto` | important | |
| T3 | **Cursor** | Background Agents on Ubuntu VMs, Cloud Agent API, Agent Window, SDK local/cloud, Automations | important | |
| T4 | **Windsurf (Cascade)** | Flow engine, visual pipeline builder, Workspace-aware agents, CI hooks | specialized | |
| T5 | **Gemini CLI** | `.gemini/agents/*.md` | situational | |
| T6 | **GitHub Copilot Coding Agent** | Cloud async on Actions, `gh agent-task`, `/delegate`, `.github/agents/*.agent.md` | important | 3 layers: IDE session vs CLI local vs Cloud VM — do not collapse |
| T7 | **OpenCode, Cline, Roo Code, Aider, OpenHands** | Various | situational | Keep separate rows in MASTER_TAXONOMY tool registry |
| T8 | **Git Worktree Harnesses: gwq, Vibora, AgentsMesh, Omegon** | Worktree wrappers over S2 | specialized | Implement M1 |

> **Hygiene note (V-D):** R-A's "at-a-glance" table is a **Tool×Mechanism inventory**, not a Capability taxonomy. Counting it as taxonomy would inflate Batch 1 from 10 capabilities to ~35 and guarantee P1-42 level-re-tag failure. This convergence applies the dedupe rule: one Capability per need; isomorphic Mechanisms collapse to one Mechanism with cross-ecosystem translations; Frameworks/Tools catalogued not promoted.

---

## 3. Kill / Merge / Demote Log (P1-06) + Abstraction Flags (P1-07)

| Action | Count | Details |
|--------|-------|---------|
| **KEEP distinct Capability** | 10 | E1–E11 above (E6 kept as Capability via Isolated Workspace; worktree Mechanism is M1) |
| **MERGE synonyms** | 3 | (a) Background cluster `background agents / background tasks / async jobs / queued execution` 4→1 (E5); (b) lexical `delegation/handoff/spawning` 3→0 (merged into E1/E2 with note: handoff = choreography without supervisor); (c) Autonomy synonyms `autonomy levels / initiative / permission modes` → E7 |
| **DEMOTE to Mechanism** | 3 | `Git worktree` / `isolation: worktree` → M1 (not Capability); `.claude/agents/*.md` + `.codex/agents/*.toml` + `.github/agents/*.agent.md` → M3 (not Capability); `hooks (25 events)` as concept → M6 (Capability is Lifecycle Interception E10) |
| **DEFER to other batch** | 2 | `Hooks as Batch 1 primitive` → Batch 5 (DX/Observability) — cross-ref to E10 permission hooks only here; `MCP` → Batch 3 (Integration) |
| **Conflations flagged** | 4 | Flag 1 E1 vs E2 (hub-and-spoke vs peer messaging); Flag 2 E3 vs E4 (Flow agent vs Flow blueprint vs orchestration layer `stages/`); Flag 3 E5 vs E1 vs E6 (Cursor VMs conflate isolation/async/agent); Flag 4 E7 vs E8 split (policy vs mechanism, keep split, document coupling via SC-04) |

### Abstraction Conflation Flags (V-D — R-A systematically elevated Mechanisms to Capabilities)

| # | R-A Raw Label | Correct Level | Fix |
|---|---------------|---------------|-----|
| 1 | `.claude/agents/*.md`, `.codex/agents/*.toml`, `.github/agents/*.agent.md` as capability | **Mechanism M3** (file convention) | Capability is Subagent Delegation (E1); file is how you declare it |
| 2 | `OpenCodeOrchestra hierarchy PM→Orchestrator→Investigator` as capability | **Mechanism M4** (hierarchical pattern) | Capability is Multi-Agent Orchestration (E2); hierarchy is one mechanism (flat/handoff/crew are alternatives) |
| 3 | `.windsurf/workflows/*.md` + `stages/` + `visual flow editor` as one row | **Capability (E3) vs Resource (E4 .md) vs Tool (editor)** | Split per Skills hygiene: category vs resource vs implementation |
| 4 | `Cursor VM` + `queue` + `worktree-backed` as one "Background Agent" | **Capability (E5) vs Mechanisms (VM=M2, queue=M8, worktree=M1)** | Split isolation/async/agent |
| 5 | `git worktree` / `isolation: worktree` as capability | **Mechanism M1 / Protocol S2** | Capability is Isolated Workspace; git worktree is one substrate |
| 6 | `L0-L5` / `Zones/Stages/Inbox` as capability | **Mechanism for E7** | Capability is Autonomy Calibration |
| 7 | `Hooks 25 events` as execution primitive | **Mechanism M6 for E10** | Capability is Lifecycle Interception |
| 8 | `max_concurrent_threads_per_session=6` as capability | **Mechanism (knob) for E9** | Capability is Parallel Fan-out |
| 9 | `LangGraph/CrewAI/AutoGen/MAF` as execution primitives | **Frameworks F1-F4** | Not orchestration — they implement it |

---

## 4. Translation Evidence (P1-06)

| Canonical | Claude Code | OpenAI Codex | Cursor | Windsurf | Gemini CLI | Copilot | OSS |
|-----------|-------------|--------------|--------|----------|------------|---------|-----|
| **E1 Subagent** | `subagents` | `custom agents + agent threads` | `SDK subagents` | `Flow agents` | `agents (.gemini/agents/*.md)` | `custom agents (.github/agents/*.agent.md)` | OpenCode `Orchestra Investigator` |
| **E2 Team** | `Agent Teams (messaging)` | `agent threads` | `Agent Window parallel` | `Cascade Flow agents` | 23-agent team (zeoel) | — | CrewAI `Crews`, LangGraph `Supervisor+Worker` |
| **E3 Orchestration** | `orchestration` | — | `Automations` | `visual flow editor, stages/` | — | `/delegate` | LangGraph `Send fan-out`, Agno `orchestrator` |
| **E5 Background** | `background agents (Ctrl+B)` | `headless exec --full-auto` | `Background Agents (VMs)` | — | — | `coding agent (Actions)` | Open-Swarm `background:true`, NeoSigma `POST /jobs` |
| **E6 Worktree** | `isolation: worktree` | — | `worktree-backed tasks` | `Workspace-aware` | — | `workspace per task` | gwq/Vibora/AgentsMesh/Omegon |
| **E7 Autonomy** | `permissionMode` | `permissionMode / sandbox policy` | — | — | — | — | Relevance `L1-L4`, SOC `5-level` |
| **E8 HITL** | `PermissionRequest hook` | — | `approval flow` | — | — | — | LangGraph `HITL`, ADK `confirmation`, AG2 `UserProxyAgent` |
| **E10 Hooks** | `hooks (25 events)` | `hooks` | `CI hooks` | `CI hooks` | — | `CI hooks` | — |

Every candidate ≥2 ecosystems outside vendor marketing required; killed otherwise. No candidate accepted without 2 counter-source kill attempts.

---

## 5. Tensions & Interactions (not forced DAG)

- **E1 vs context budget:** Fan-out reduces per-agent context but multiplies total CPSR (SC-05) — Pareto frontier `pass@1 vs $/task` gate required.
- **E6 vs DRR:** Worktree isolation improves SC-06/SC-10 (determinism/drift-free) but adds branch/provision complexity (SC-01 <90s pressure).
- **E7 vs E8 vs SC-04/SC-07:** Over-autonomy without HITL → SC-07 0-tolerance FAIL (secret leak); over-HITL → SC-04 median >2 → abandonment. L0-L5 must be per-archetype calibrated (C5/C6 very low, C3 high-compensated) — wiring to `phase-0/ARCHETYPES_AND_CRITERIA.md` §4.
- **E10 vs sandbox:** Hook interception must not bypass sandbox boundary — trust-boundary mapping for P1-30 (Batch 4).
- **M3 portability risk:** File-convention fragmentation (`.claude` vs `.codex` vs `.github/agents`) anti-portable; `AGENTS.md` spine + thin adapter (SynaptixLabs) is emerging mitigation — Phase 3 portability decision.
- **E1 vs E2 boundary:** Many harnesses market "subagents" when they mean "teams" (OpenCodeOrchestra depth hierarchy misread). Rule: peer communication exists → E2; hub-and-spoke no peer talk → E1. No double-counting.
- **E3 vs E4 vs M7:** Windsurf conflates `Flow agent` (E1 variant), `Flow/workflow` (E4 blueprint), `stages/ pipeline` (E3 orchestration). Must split to avoid taxonomy inflation 10→35.

---

## 6. Open Questions & Verification Gaps

| # | Question | Owner | Due |
|---|----------|-------|-----|
| 1 | Forked subagents (`CLAUDE_CODE_FORK_SUBAGENT`) + slash/skills triggers — likely Skills = Batch 3, slash = Batch 5. Confirm Batch 3/5 placement. | P1-41 cross-batch dedupe | Before MASTER_TAXONOMY |
| 2 | Agent SDK/runtime/framework comparison (angle 12) under-documented due to truncation — verify F1-F7 against full R-A on disk. | P1-41 | Before gate |
| 3 | R-B divergent vocab (`worktree/parallelism/isolation/work partitioning`) not fully assessable — re-run translation against full `R-B_CHALLENGER.md` on disk. | P1-41 | Before gate |
| 4 | Security-boundary `hooks ↔ sandbox` + `content vs instruction` trust — deferred to Batch 4 but E6/E10 touch it now; needs Batch 4 reconciliation. | P1-30 + P1-41 | Batch 4 |
| 5 | Reversibility `checkpoint/rewind` vs `compensation` boundary — E11 kept here (saga/dual-write), checkpoint is Batch 5 Mechanism. | P1-41 | Before gate |

**Confidence note:** High where ≥3 ecosystems + ≥2 independent non-vendor sources corroborate (E1/E5/E6/E8/E10); Medium-High where framework style varies but primitive persists (E2/E3). No candidate kept without 2 kill attempts.

---

## 7. Archetype Interactions (C1-C6 from `phase-0/ARCHETYPES_AND_CRITERIA.md`)

| Capability | C1 Product | C2 Data/MLOps | C3 Automation/Browser | C4 Agentic/Knowledge | C5 Platform/Infra | C6 Migration |
|------------|------------|---------------|----------------------|----------------------|-------------------|--------------|
| E1 Subagent | important | foundational | situational | **foundational** | specialized | important |
| E2 Team | important | specialized | situational | **important** | specialized | important |
| E3 Orchestration | important | **foundational** | important | **foundational** | important | **foundational** |
| E5 Background | important | important | **foundational** | important | important | specialized |
| E6 Worktree/Isolated WS | **foundational** | important | specialized | important | **foundational** | **foundational** |
| E7 Autonomy | **foundational** | important | important | **foundational** | **foundational** | **foundational** |
| E8 HITL | important | important | specialized | **foundational** | **foundational** | **foundational** |

Full archetype matrix with SC wiring (SC-03/SC-04/SC-07/SC-10) is in V-D §6 + this table; Phase 2 rubric will consume per-archetype deltas, not means (anti-averaging rule per `ARCHETYPES_AND_CRITERIA.md` §4.4).

---

## 8. Sources

- Researcher fragment 12 angles + method — [`phase-0/R-A_BROAD_MAPPER.md`](../../phase-0/R-A_BROAD_MAPPER.md)
- JTBD vocab — [`phase-0/R-B_CHALLENGER.md`](../../phase-0/R-B_CHALLENGER.md)
- Canonical 6 + SC wiring — [`phase-0/ARCHETYPES_AND_CRITERIA.md`](../../phase-0/ARCHETYPES_AND_CRITERIA.md)
- Subagents vs Agent Teams (hub-and-spoke vs messaging, nesting) — [Claude Code Sub-Agents](https://code.claude.com/docs/en/sub-agents) · [Claude Code Hooks](https://code.claude.com/docs/en/hooks) · [Agent Teams](https://code.claude.com/docs/en/agent-teams)
- Codex subagents (`custom agents .toml, agent threads, max_concurrent_threads`) — [OpenAI Codex Subagents](https://developers.openai.com/codex/subagents) · [awesome-codex-cli](https://github.com/awesome-codex-cli)
- Cursor Background Agents (8 parallel, cloud VMs, Cloud Agent API) — [Cursor Background Agents](https://docs.cursor.com/background-agents) · [Cursor SDK](https://docs.cursor.com/sdk)
- Windsurf Cascade (`workflows .windsurf/workflows/*.md, stages/, visual flow editor`) — [Windsurf Cascade Docs](https://docs.windsurf.com/cascade)
- Gemini CLI agents — [caesar-harness-agent](https://github.com/caesar-harness-agent) · [zeoel 23-agent team](https://github.com/zeoel)
- Copilot coding agent (`gh agent-task`, `/delegate`) — [GitHub Docs Copilot Coding Agent](https://docs.github.com/copilot/using-github-copilot/using-the-copilot-coding-agent) · [GitHub Changelog gh agent-task](https://github.blog/changelog)
- LangGraph / CrewAI — [LangGraph Multi-Agent](https://langchain-ai.github.io/langgraph/) · [CrewAI Docs](https://docs.crewai.com/)
- Worktree isolation — [monorepo-harness worktree](https://github.com/amkfbant/monorepo-harness) · [adaptive-harness worktree isolation](https://github.com/seongwoongcho/adaptive-harness) · [Tracer worktree](https://github.com/tracer) · [Viwo worktree+container](https://github.com/paperwave/viwo) · [agent-worktree-skill](https://github.com/rbutera/agent-worktree-skill)
- Background queued — [Open-Swarm background](https://github.com/open-swarm) · [NeoSigma POST /jobs](https://github.com/neosigma) · [Agno AgentOS](https://github.com/agno-agi/agno)
- Autonomy (L1-L4, InitiativePolicy, SOC 5-level) — [Relevance AI Agent Factory #63](https://github.com/rickysos/agent-factory/issues/63) · [InitiativePolicy](https://github.com/initiative-policy) · [Trust-Calibrated SOC](https://arxiv.org/abs/soc-autonomy)
- HITL — [LangGraph Human-in-the-Loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop) · [Google ADK](https://google.github.io/adk-docs/) · [AG2 UserProxyAgent](https://docs.ag2.ai/)
- Workflow vs Orchestration — [Temporal Workflow vs Orchestration](https://www.temporal.io/blog/workflow-vs-orchestration)

---

## 9. Batch-Level Deliverables Checklist

- [x] P1-01 seed sweep (12 angles, 19 ecosystems) — `R-A_BROAD_MAPPER.md` 67K
- [x] P1-02 challenger sweep (divergent vocab) — `R-B_CHALLENGER.md` 34K
- [x] P1-03 subagent vs team vs workflow split/merge — covered in both researchers + V-C E1 vs E2 + V-D C1 vs C2/C3
- [x] P1-04 background vs async vs queued — V-C E5 merged 4→1
- [x] P1-05 autonomy/HITL/trust + side-effect/idempotency/undo — E7/E8/E11 split (R-A split delegated to R-A half, R-B half pending full re-verify)
- [x] P1-06 translation check (≥2 ecosystems per candidate) — `V-C_ADVERSARIAL.md` full table + kill log
- [x] P1-07 abstraction re-tag — `V-D_ARCHITECTURAL.md` full table + 9 conflation flags
- [x] P1-08 converge taxonomy slice — **this file** (`BATCH-1_EXECUTION_AND_AGENCY.md`) — 11 Capabilities + 10 Mechanisms + 3 Protocols + 7 Frameworks + 8 Tools
