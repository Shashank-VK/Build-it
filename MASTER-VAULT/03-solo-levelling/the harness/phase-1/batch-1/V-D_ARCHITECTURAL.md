# VERIFIER D — P1-07 + P1-08 | Batch 1 EXECUTION & AGENCY LAYER

**Repo root:** `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness`
**Ground truth:** `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md` §2 Batch 1 P1-01..P1-08 · `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md` C1-C6, SC-01..SC-10, rubric wiring
**Inputs reviewed:** Researcher A payload (§1 truncated at OpenCodeOrchestra) · Phase-1 STATUS `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-1\STATUS.md`
**Truncation notice (required):** R-A payload truncated after ecosystem 7/12 (cut inside OpenCode section; ecosystems 8-12 LangGraph/CrewAI/AutoGen/MAF, git-worktree harnesses gwq/Vibora/AgentsMesh/Omegon, Agent SDK comparison not in payload). R-B payload absent (Challenger sweep via delegation/handoff/spawning/worktree/parallelism/autonomy vocabulary). Full files not on disk (`phase-1/` empty except `STATUS.md` per `ls -R`). Candidates 8-12 reconstructed from plan.md sub-areas + R-A search-angle list (angles 7-12) and flagged `INFERRED — verify against full R-B` below.

---

## P1-07 ABSTRACTION RE-TAG PASS

**Level definitions enforced:**
- **Capability** = what harness needs (vendor-agnostic need, testable via SC regression if omitted). Survives tool death.
- **Mechanism** = way to implement a Capability (pattern, file convention, isolation primitive, event).
- **Protocol/Standard** = cross-vendor contract/de facto spec (MCP, Git worktree primitive, AGENTS.md convention).
- **Framework/Runtime** = composable engine that orchestrates Mechanisms to deliver Capabilities.
- **Tool/Product/Repo** = shippable implementation (CLI, cloud service, harness repo).

**Lifecycle roles:** `build-time` (harness authoring/config), `run-time` (agent execution live), `review-time` (human approval/gate). Most span two — primary listed first.
**Tier tags:** `foundational` (omit → SC-02/03/07 FAIL across ≥4 archetypes, harm 5/4), `important` (major TSR/HIR/CPSR delta in ≥2 archetypes), `specialized` (archetype-specific, high harm within niche), `situational` (niche/emerging/legacy, low global harm).

### 1. Capabilities (what harness must do — R-A systematically listed Mechanisms as if Capabilities)

| # | Canonical Candidate | R-A Raw Label | Correct Level | Lifecycle | Tier + Rationale | Conflation Flag |
|---|---|---|---|---|---|---|
| C1 | **Subagent Delegation / Task Decomposition** | "Claude Code subagents", "OpenAI subagent workflows", "OpenCode agents (build+plan)" | **Capability** | run-time (definition is build-time) | **foundational** — SC-09 CSP (context survival >30k), SC-05 CPSR (anti-context-rot: main stays lean, subagents summarize), SC-04 HIR (scoped autonomy). Needed C4 (agent/memory), C6 (migration parallel strands), C2 (DAG fan-out). Harm 4 if absent: goal drift embedding <0.90 on long tasks. | **FLAGGED:** R-A lists `.claude/agents/*.md`, `.codex/agents/*.toml`, `.github/agents/*.agent.md` as the capability. File convention is Mechanism; capability is delegation itself. Split required. |
| C2 | **Multi-Agent Team Orchestration** | "agent teams", "OpenCodeOrchestra PM→Orchestrator→Investigator", "Cursor Agent Window parallel agents" | **Capability** | run-time + review-time (team plan approval) | **important** — distinct from C1: C1=one parent→N children; C2=N peers + shared state + turn-taking. SC-02 TSR (+10pp on crew tasks per AEGIS harness), SC-03 MTTR (peer recovery). Critical C4, C1-scale, C6 strangler; overkill for C3 glue fleet (solo-ideal). Not foundational because solo runs succeed without it. | **FLAGGED:** R-A presents `OpenCodeOrchestra hierarchy` and `manager spawns subagents after plan approval` as if hierarchy IS the capability. Hierarchy is one Mechanism (hierarchical); flat/shared, handoff, and crew are alternative Mechanisms under same Capability. R-A averaged them away. |
| C3 | **Workflow / Flow Orchestration** | "Windsurf Cascade flows / workflows / stages", "LangGraph / CrewAI workflows" | **Capability** | build-time (definition) → run-time | **foundational** — SC-02/SC-08 gate for C2 (DAG), C3 (glue fleet), C6 (codemod→dual-write→shadow→cutover). Without DAG/sensor/dependency, idempotency SC-10 fails 100% on C5/C2. | **FLAGGED:** R-A conflates three levels: `Workflow` (Capability) vs `.windsurf/workflows/*.md` + `stages/` (Resource/Mechanism: file convention) vs `visual flow editor` (Tool). Same hygiene as Skills example: "Workflow orchestration" is capability; individual `.md` is resource; `.windsurf/workflows/` is implementation. |
| C4 | **Background & Asynchronous Execution** | "Claude Code background agents (Ctrl+B)", "Cursor Background Agents (isolated Ubuntu VMs)", "GitHub Copilot coding agent (Actions infra)" | **Capability** | run-time | **important** — SC-01 TTFUA (non-blocking: preview deploy while chat continues), SC-03 MTTR (queued retry without human stall). Elevated C3 (fleet), C1 (preview branch), C4-research (long dossier). Not foundational: foreground-only harness still passes SC-02 albeit slower. | **FLAGGED:** R-A merges Capability (async execution) + Mechanism (VM/container isolation, queue, worktree-backed) + Tool (Cursor Cloud VM vs Claude push-notification) into one row. Must split: VM is one isolation Mechanism; queue/worktree is another. |
| C5 | **Isolated Workspace Management** | "git worktree isolation (isolation: worktree)", "workspace (parallel workspace per task)", "gwq / Vibora / AgentsMesh" | **Capability** | build-time (provision) + run-time + review-time (drift check) | **foundational** — SC-10 IDFR (100% no-op on frozen re-run), SC-06 DRR (determinism), SC-07 SSHC (sandbox boundary). Mandatory C5 (IaC blast-radius), C2 (Bronze→Gold), C6 (dual-write), C1 (parallel PRs). Harm 4: without isolation, parallel edits corrupt SC-08 AHG. | **FLAGGED:** R-A labels Mechanism `git worktree` / `isolation: worktree` as the Capability. Correct Capability is isolated-workspace; git worktree is one Mechanism (Protocol-backed), container/VM is another. Tool harnesses (gwq etc.) are Products. |
| C6 | **Autonomy Calibration** | "autonomy calibration L0-L5, Zones/Stages/Inbox" (angle 9) | **Capability** | run-time + review-time | **foundational** — SC-04 HIR (median 0→1 vs ≤2 correctly), SC-07 SSHC (harm 5 if no calibration: unsandboxed write), SC-03 (bounded retries ≤3). Zero-tolerance V-D rule: harm≥4 for SC-07 cannot rank below median. All archetypes but tolerance varies (C5/C6 very low, C3 high-compensated). | **FLAGGED if R-A listed "L0-L5" as capability:** L0-L5/Zones/Inbox are Mechanisms/graduated controls, not the capability itself. |
| C7 | **Human-in-the-Loop Governance & Trust Calibration** | "human-in-the-loop + trust calibration + adaptive/SOC/TCF" (angle 8) | **Capability** | review-time (primary) | **foundational** — SC-07 (injection block ≥90%, secret leak 0/100), SC-04 (calibrated escalation precision), SC-02 (human review gate for C4 groundedness). Distinct from C6: C6=what agent may do alone; C7=when/how human approves/intervenes. Kill-test: no HITL → SC-07 FAIL on C1/C3/C5 creds. | **FLAGGED:** R-A bundles SOC/adaptive/TCF (frameworks for trust calibration) as synonyms for HITL. They are Frameworks/Mechanisms implementing HITL, not HITL itself. Separate. |
| C8 | **Parallel Execution & Fan-out** | "parallel fan-out up to 6 threads", "up to 8 parallel Background Agents", "one agent per point" trigger phrases | **Capability** | run-time | **important** — SC-01 (P50 <90s C1), SC-05 (cost trade: parallelism × token cost). Sub-capability of orchestration but independently toggled (max_concurrent_threads). C2/C4 benefit most; C5 gated low parallelism. | **FLAGGED:** R-A lists `max_concurrent_threads_per_session=6` (config knob) as capability. Knob is Mechanism; fan-out is Capability. |
| C9 | **Lifecycle Interception / Hooks** | "hooks (25 lifecycle events: command/http/mcp_tool/prompt/agent)" | **Capability** (cross-cutting) | run-time | **important** — SC-07 (policy gate: block before tool exec), SC-03 (retry/compensation trigger), SC-08 (gate.sh injection). Without interception, SC-07 audit cannot enforce allowlist. Specialized if treated as optional DX; important when security-gated. V-D notes: harm 4 for C5/C2. | **FLAGGED:** R-A places hooks alongside subagents as "execution primitive" at same level. Hook *system* is Mechanism for interception Capability; individual event `PreToolUse` is hook point (Resource). 25 is Tool-specific count (Claude Code), not canonical. |
| C10 | **Reversibility / Compensation / Undo** | "side-effect safety, idempotency, undo/reversibility" (P1-05 missed) | **Capability** | run-time + review-time | **important** (C5/C6 foundational, others important) — SC-10 (drift-free), AWRR SRR (safe rollback), SC-03 (saga compensation). Merged by R-A into HITL/autonomy but is distinct: idempotency is property, compensation is action, undo is UX. | **FLAGGED (omission risk):** If R-A subsumed this under "HITL controls" it averages away C6 dual-write/shadow gating. Split recommended; verify R-B angle covers it. |

### 2. Mechanisms (how to implement — R-A often elevated these to Capabilities)

| # | Mechanism | Implements Capability | Lifecycle | Tier | Flag |
|---|---|---|---|---|---|
| M1 | **Git Worktree (`git worktree add/remove`, `isolation: worktree`)** | C5 Isolated Workspace | build-time + run-time | **important** — primary mechanism for C1/C2/C5/C6 parallel branches; cheap, native, reversible. Not foundational globally because VM/container alternative exists for browser-heavy C3. | Flagged above; Protocol-backed mechanism, not Capability. |
| M2 | **Container / VM / Sandbox Isolation (Docker, isolated Ubuntu VM, GitHub Actions VM)** | C5 + SC-07 sandbox boundary | run-time | **important** — C3 stealth fleet, C5 blast-radius. Mechanism choice trades cost (SC-05) vs fidelity. | R-A conflates Cursor VM with Background Capability. |
| M3 | **Agent Definition File Conventions (`.claude/agents/*.md` + YAML frontmatter `name/description/tools/model/permissionMode/hooks/isolation`; `.codex/agents/*.toml`; `.github/agents/*.agent.md`; `.gemini/agents/*.md`; `AGENTS.md` Operating Model)** | C1, C2 | build-time | **important** — enables portability vs vendor lock-in; P3 model routing. One spine + thin adapters pattern (SynaptixLabs). | R-A lists each path as separate primitive; they are isomorphic Mechanisms for same Capability — dedupe, do not multiply taxonomy. |
| M4 | **Delegation Patterns: Delegation vs Handoff vs Spawn vs Agent-Team (GoClaw 4-pattern)** | C1/C2 | run-time | **specialized** — C4-only nuance (when to transfer context vs clone). Important for harness-as-code but not for C3/C5 operators. | R-A angle 7 correctly distinguishes; keep as Mechanism cluster, not 4 Capabilities. |
| M5 | **Forked Subagent / Context Inheritance Toggle (`CLAUDE_CODE_FORK_SUBAGENT`, Codex sandbox policy inheritance + per-agent override, `default/worker/explorer` built-ins)** | C1 | run-time | **situational** — experimental flag, read-only Investigator/Auditor lacking shell. Useful for long-horizon C4 but adds complexity SC-05. | Flag: experimental flag is Tool config, not Capability. |
| M6 | **Hook Event System (PreToolUse/PostToolUse, command/http/mcp_tool/prompt/agent hooks, 25 events)** | C9 | run-time | **important** | Flagged: count 25 is Claude Code Tool detail; canonical Mechanism is lifecycle interception points. |
| M7 | **Slash Commands / Skills as Prompt-Pack Triggers (`/delegate`, `/multitask`, Skills repo)** | C3/C1 | build-time + run-time | **specialized** — invocation Mechanism for workflows; hygiene: "Skills" is Capability category; individual skill is Resource; GitHub Skills repo is Implementation. | R-A lists alongside subagents; must demote to Mechanism/Resource. |
| M8 | **Queue / Scheduler / Automations (Cursor Automations scheduled/event-triggered, Cloud Agent API `launch/follow-up/status/list/delete/fetch + MCP server`, `gh agent-task create/list`, OpenAI `max_concurrent_threads_per_session`)** | C4 Background | build-time + run-time | **important** — C3 fleet, C4 content-pipeline loop. | R-A mixes scheduler with background agents. |
| M9 | **Worktree-backed Background Task + Cloud Dispatch (`gh agent-task`, Cloud Agent API push to branch, `/delegate TASK` unstaged→new-branch→draft-PR)** | C4 + C5 | run-time | **specialized** — GitHub/cloud surface only; local harness uses different Mechanisms. | Flag as Mechanism variant, not separate Capability. |
| M10 | **Read-only Investigator / Auditor Constraints (OpenCodeOrchestra Depth 2+ read-only, no shell)** | C1/C2 (safety) | run-time | **specialized** — least-privilege subagent. SC-07 reducer. | Part of M4 pattern family. |

### 3. Protocols / Standards

| # | Protocol/Standard | Scope | Lifecycle | Tier | Note |
|---|---|---|---|---|---|
| S1 | **MCP (Model Context Protocol)** | Integration layer (Batch 3) referenced in angle 12 | run-time | foundational for Batch 3, **situational for Batch 1** — do not duplicate as Execution Capability. | R-A angle 12 includes it; correctly belongs to Batch 3 taxonomy. Tag as Protocol, not Capability. |
| S2 | **Git Worktree Primitive (`git worktree` CLI contract)** | C5 Mechanism S1 | build-time + run-time | **important** — de facto standard; underlying Protocol for M1. | Distinct from gwq/Vibora wrappers (Tools). |
| S3 | **AGENTS.md / `CLAUDE.md` / `.cursorrules` Operating Model Convention (caesar-harness-agent cross-platform mapping, zeoel-framework 23-agent team)** | C1 definition portability | build-time | **important** (emerging de facto standard) — enables one spine → thin adapter (SynaptixLabs) portability. Not yet formal standard; tag `emerging`. | Flag: R-A lists as "Orchestration Operating Model in AGENTS.md" alongside Claude Code config — hygiene: convention is Standard; file is Resource. |

### 4. Frameworks / Runtimes

| # | Framework/Runtime | Implements | Lifecycle | Tier |
|---|---|---|---|---|
| F1 | **LangGraph** | C2/C3 orchestration (stateful DAG, cycles, persistence) | build-time + run-time | important |
| F2 | **CrewAI** | C2 (role-based crew, sequential/parallel/loop) | build-time + run-time | important |
| F3 | **AutoGen / AG2** | C2 (conversational multi-agent) | run-time | specialized |
| F4 | **Microsoft Agent Framework** | C2/C6 (enterprise policy, review gates) | run-time + review-time | specialized |
| F5 | **Claude Agent SDK** | C1/C4/C9 (subagents + hooks as SDK primitives) | build-time + run-time | important (harness-as-code) |
| F6 | **OpenCodeOrchestra / OpenAgentsControl (7 subagents: task-manager, context-scout, context-manager, coder-agent, test-engineer, code-reviewer, external-scout)** | C1 hierarchy + safety constraints | run-time | situational — fix for flat `build+plan` shared-everything debt; not canonical. |
| F7 | **Windsurf Cascade Runtime (Flow engine + visual pipeline builder + Workspace-aware agents + CI hooks)** | C3 + C5 | build-time + run-time | specialized |

*Hygiene: Framework ≠ Capability. R-A row "LangGraph / CrewAI / AutoGen / MAF" as "Execution Primitives" conflates Framework coverage with Capability need. LangGraph is not "orchestration"; it implements orchestration.*

### 5. Tools / Products / Repos

| # | Tool/Product/Repo | Type | Lifecycle | Tier | Note |
|---|---|---|---|---|---|
| T1 | **Claude Code** (subagents, background agents, worktree isolation, hooks, forked subagents, slash/skills) | Product | build+run | important | Vendor implementation of C1/C4/C5/C9. |
| T2 | **OpenAI Codex CLI** (`config.toml [agents]`, `default/worker/explorer`, 6-thread fan-out, `codex exec --full-auto` headless) | Product | run-time | important | |
| T3 | **Cursor** (Background Agents on Ubuntu VMs, Cloud Agent API, Agent Window, SDK local/cloud, Automations) | Product | run-time | important | |
| T4 | **Windsurf (Cascade)** | Product | build+run | specialized | |
| T5 | **Gemini CLI** | Product | run-time | situational | |
| T6 | **GitHub Copilot Coding Agent** (cloud async on Actions, `gh agent-task`, `/delegate`, `.github/agents/*.agent.md` custom agents) | Product | run-time | important | Three layers: IDE session vs CLI local vs Cloud VM — do not collapse. |
| T7 | **OpenCode, Cline, Roo Code, Aider, OpenHands** | Product family | run-time | situational (each) | R-A lumps; keep separate rows in MASTER_TAXONOMY tool registry, not execution taxonomy. |
| T8 | **Git Worktree Harnesses: gwq, Vibora, AgentsMesh, Omegon** | Repo/Tool | build+run | specialized | Wrappers over S2 Protocol; implement M1. |

---

## P1-08 CONVERGENCE — TAXONOMY SLICE FOR BATCH 1 (canonical, deduped)

**Dedupe rule applied:** One Capability row survives per need; isomorphic Mechanisms from different vendors collapse to one Mechanism with cross-ecosystem translations; Frameworks and Tools are catalogued but not promoted to Capabilities.

| Canonical Element | Correct Level | Lifecycle Role | Tier | Related Concepts (parent/child/sibling) | Cross-Ecosystem Translations |
|---|---|---|---|---|---|
| **Subagent Delegation** | **Capability** | build (define) → run | foundational | Parent of C2; child Mechanisms M3/M4/M5; sibling to Parallelism; competes with context budget (CSP). | Claude `subagents (.claude/agents/*.md)` ≡ Codex `custom agents (.codex/agents/*.toml)` ≡ Copilot `custom agents (.github/agents/*.agent.md)` ≡ Gemini `agents (.gemini/agents/*.md)` ≡ OpenCode `build/plan → Orchestra Investigator` |
| **Multi-Agent Team Orchestration** | **Capability** | run → review (plan approval) | important | Extends C1 with peer coordination, shared state, turn-taking; uses M4 patterns; F1-F4 implement. | Claude "agent teams" ≡ Codex "agent threads" ≡ Cursor "Agent Window parallel agents" ≡ Windsurf "Cascade Flow agents" ≡ CrewAI "crew" |
| **Workflow Orchestration** | **Capability** | build → run | foundational | Owns DAG, stages, sensors; C5 workspaces are its execution substrate; M7/M8 are triggers. | Windsurf `cascade flows (.windsurf/workflows/stages/)` ≡ LangGraph `StateGraph` ≡ CrewAI `flows` ≡ OpenHands `micro-agents` |
| **Background & Async Execution** | **Capability** | run | important | Requires C5 isolation; managed via M8 queue; observed via hooks M6. | Claude `background agents (Ctrl+B, push notify)` ≡ Cursor `Background Agents (VM, Cloud Agent API)` ≡ Copilot `coding agent (Actions)` ≡ Codex `headless exec --full-auto` |
| **Isolated Workspace Management** | **Capability** | build → run → review | foundational | Supports C3/C4 parallelism; SC-10 gate; M1/M2 implement over S2. | Claude `isolation: worktree` ≡ Copilot `workspace (parallel per task, branch auto-create)` ≡ Cursor `worktree-backed tasks` ≡ harness `gwq/Vibora` |
| **Autonomy Calibration** | **Capability** | run → review | foundational | Governance parent of C7; Mechanisms L0-L5/Zones/Stages/Inbox; F4 policy. | Codex `permissionMode / sandbox policy` ≡ Claude `permissionMode` ≡ system `L0-L5` ≡ Framework "Inbox" |
| **Human-in-the-Loop Governance** | **Capability** | review | foundational | Child of trust calibration; uses M6 interception + M8 approval queue; distinct from Autonomy (what agent may do vs when human decides). | Clause `human approval` ≡ ` HITL adaptive/SOC/TCF` ≡ `Harness review gate / trace viewer` |
| **Parallel Fan-out** | **Capability** | run | important | Sub-capability of C2/C3; knob M8 `max_concurrent_threads_per_session` (6 default), Cursor up to 8 VMs. SC-01 vs SC-05 Pareto. | Codex `parallel fan-out (spawn two agents)` ≡ Cursor `up to 8 parallel` |
| **Lifecycle Interception** | **Capability** | run | important | Implemented by M6 hook events; used by C6/C7 for policy; F5 SDK exposes. | Claude `hooks (25 events)` ≡ Codex `hooks` ≡ Copilot `CI hooks` |
| **Reversibility & Compensation** | **Capability** | run → review | important (C5/C6 foundational) | Saga/compensation, idempotency, undo; AWRR RR/SRR; drift-detector `plan.json`. | `Saga compensation` ≡ `checkpoint/rewind` (Batch 5 boundary) ≡ `dual-write/shadow` (C6) |

**Mechanism / Protocol / Framework / Tool rows** are not re-emitted as Capability rows in the canonical taxonomy — they are linked as above. This is the hygiene fix: Researcher A's "at-a-glance" table is a **Tool×Mechanism inventory**, not a Capability taxonomy. Counting it as taxonomy would inflate Batch 1 from 10 capabilities to ~35 and guarantee level-conflation downstream (P1-42 re-tag would fail).

**Relationship tensions (not forced DAG):**
- **C1 vs context budget:** fan-out reduces per-agent context but multiplies total CPSR (SC-05) — Pareto frontier `pass@1 vs $/task` gate required.
- **C5 vs DRR:** worktree isolation improves SC-06/SC-10 but adds branch/provision complexity (SC-01 <90s pressure).
- **C6 vs C7 vs SC-04/SC-07:** over-autonomy without HITL → SC-07 leak 0-tolerance FAIL; over-HITL → SC-04 median >2 → abandons. L0-L5 must be per-archetype calibrated (C5/C6 very low, C3 high-compensated).
- **C9 vs sandbox:** hook interception must not bypass sandbox boundary — trust-boundary mapping for P1-30.
- **M3 portability risk:** file-convention fragmentation (`.claude` vs `.codex` vs `.github/agents`) anti-portable; `AGENTS.md` spine + adapter is emerging mitigation — Phase 3 portability decision.

**Open questions for P1-06/P1-42 + Phase 3:**
1. Verify INFERRED rows (F1-F4, T8) against full R-A angles 11-12 + full R-B handoff/autonomy vocabulary — 3 consecutive no-new-synonym stop-rule not observable in truncated payload.
2. Decide S3 promotion: `AGENTS.md` from emerging convention to formal Standard (adopt as harness spine?).
3. Resolve C10 boundary with Batch 5: checkpoint/rewind vs compensation — keep Capability here, Mechanism there.

**Files relevant to next gate:** `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md`, `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md`, `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-1\STATUS.md`. No `phase-1/batch-1-execution.md` or `MASTER_TAXONOMY.md` yet — this slice is the input to P1-08 synthesis.

