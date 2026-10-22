**RESEARCHER B — CHALLENGER BATCH 1: EXECUTION & AGENCY LAYER**
`C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md` P1-02 + P1-04 + P1-05b | `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md` gate P0-13 | `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\R-B_CHALLENGER.md`

---

### 0. Method — 6 Challenger Angles (deliberately orthogonal to R-A's A1-A7)

R-A angles (vendor harnesses, benchmarks, indie-hacker, DORA/SPACE, data stack, browser/RPA, migration/agent) search by *tool category*. R-B searches by *verb/mechanism synonym* vendors miss:

| Angle | Query Family | Purpose | Queries Run |
|-------|--------------|---------|-------------|
| **B1: Delegation/Handoff/Spawning** | `agent delegation handoff spawning subagent Claude Code OpenAI swarm` | Surfaces peer-transfer vs hierarchical-delegation hidden split | 2 |
| **B2: Worktree / Filesystem Isolation** | `git worktree parallel execution filesystem isolation ephemeral workspace agent` | Finds concurrency isolation vendors call "subagent" but omit FS contention | 2 |
| **B3: Process Supervision / Job Control / Session Multiplexing** | `process supervision job control session multiplexing tmux systemd background task harness` | Exposes supervision layer R-A collapses into "background task" | 2 |
| **B4: Background vs Async vs Queued** | `background task vs async job queued execution long running AI agent harness` | P1-04 deep dive corpus | 2 |
| **B5: Work Partitioning / Task Decomposition / Sharding** | `work partitioning task decomposition sharding strategy parallel agents coding harness` | Finds file-ownership sharding as distinct mechanism | 2 |
| **B6: Side-Effect / Idempotency / Reversibility** | `side effect safety idempotency undo reversibility checkpoint AI agent filesystem` + `idempotency vs reversibility exactly once safe retry` + `walkback agent-undo` | P1-05b corpus | 3 |

Stop rule not triggered — each angle yielded distinct primary sources after 2-3 hits.

---

### 1. P1-02 CHALLENGER SWEEP — Candidate Records

Format per Phase 1 protocol: canonical name, definition, problem, level, lifecycle role, cross-ecosystem terms, confidence, tier.

#### C-01: Hierarchical Delegation (Parent→Child Task Delegation)

* **Definition:** A lead agent decomposes a goal and delegates a bounded slice to a subordinate with explicit reference, location, ownership boundary, done-condition, and verification; orchestrator retains integration authority and never trusts subagent success report as proof.
* **Problem:** Without bounded delegation, monolithic agent context overflows, loses tracking, and hallucinates completion.
* **Why it matters:** Enables context isolation + independent judgment; only verified diff integration pattern scales to >30min tasks.
* **Level:** **Capability** (realized via Mechanisms C-02/C-03)
* **Lifecycle Role:** Run-time orchestration + review-time verification gate
* **Cross-ecosystem terms:** Claude Code `Task/Agent tool` (isolated context window), OpenAI Agents SDK `agent.as_tool()` (manager retains control), Trammel `claim_step`, fleet `bound slice → delegate → inspect diff`
* **Confidence:** HIGH
* **Tier:** **S — Foundational** (all 6 canonicals need it; C4/C6 critical)
* **Sources:** Claude Code subagent delegation via Agent/Task tool [search B1], [OpenAI Agents SDK — Agents as Tools vs Handoffs](https://openai.github.io/openai-agents-python/), [Trammel planning harness](https://github.com/trammel)

#### C-02: Peer Handoff (Routed Transfer of Control) — **HIDDEN SPLIT #1 R-A WILL MISS**

* **Definition:** One active agent transfers entire conversation control to a peer specialist via explicit handoff function; receiver inherits full transcript, originator exits loop (one-way ticket). No supervisor in loop.
* **Problem:** Hierarchical delegation retains orchestrator overhead; simple intent-routing needs zero-overhead peer routing (~40% faster than supervisor).
* **Why it matters:** Distinct failure mode: handoff chain loops, lost context across handoff, vs delegation's stale-parent. Evaluated separately on routing accuracy.
* **Level:** **Mechanism** (topology choice within orchestration Capability)
* **Lifecycle Role:** Run-time routing
* **Cross-ecosystem terms:** OpenAI Swarm `handoff(target_agent, context)` / `transfer_to_spanish_agent()`, LangChain `create_handoff_tool`, AutoGen Swarm `HandoffMessage`, `HandoffNode → goTo(target)`, Governed handoff with `PacketGuard` admission
* **Confidence:** HIGH — 3 independent lineage sources (Swarm→Agents SDK upgrade, AutoGen, LangChain)
* **Tier:** **A — Important** (miss if you only test delegation)
* **R-A blind spot:** Vendor docs list "subagents" generically; OpenAI Swarm lineage explicitly warns *sequential handoff ≠ parallel orchestration, one agent active at a time* — a control-flow distinction R-A's ecosystem sweep by tool category will not surface.
* **Sources:** [OpenAI Swarm — Routines + Handoffs](https://github.com/openai/swarm), [OpenAI Agents SDK Handoff pattern](https://openai.github.io/openai-agents-python/), [HandoffNode peer-to-peer without supervisor](https://github.com/langchain-ai)

#### C-03: Subagent Spawning / Forking (Isolated Context + Depth-Bounded Recursion)

* **Definition:** Spawning a fresh agent instance with own context window, tool allowlist, and optional conversation inheritance (fork); depth-limited (Claude Code: 3 layers) and optionally backgrounded.
* **Problem:** Context competition between exploration and execution; need parallel reads without polluting lead.
* **Level:** **Mechanism**
* **Lifecycle Role:** Run-time execution primitive
* **Cross-ecosystem terms:** Claude Code `Task tool` fork (`AgentTool/forkSubagent.ts`), Codex `spawn_agent` mailbox (`agent://`), `spawnSubAgent(modeSlug, task)` with status pending/running/completed/failed/cancelled
* **Confidence:** HIGH
* **Tier:** **A — Important**
* **Sources:** Claude Code depth-limit and fork pattern [search B1]

#### C-04: Filesystem Isolation via Git Worktree / Ephemeral Workspace — **HIDDEN #2**

* **Definition:** Each parallel worker materializes as a fresh `git worktree add` on its own branch at `//worktrees/` (or overlayfs/virtio-fs ephemeral mount), eliminating index-lock and file-clobber between concurrent agents; lifecycle create→reset(`git clean -ffdx`)→remove(worktree+branch), with dirty-worktree never auto-removed without `force`.
* **Problem:** `cf work batch run --strategy parallel` on shared FS corrupts work, hits `git index.lock`, overwrites changes — "subagent" alone does not fix filesystem contention.
* **Level:** **Mechanism** (some harnesses elevate to Capability `ExecutionContext: local|worktree|e2b-sandbox`)
* **Lifecycle Role:** Build-time partitioning + run-time isolation
* **Cross-ecosystem terms:** `agentstudio workspace.mode='worktree'` (KAIROS harness), `tinyhumansai/openhuman` worktree manager (`create/list/status/diff_summary/remove`), `GitWorktreeAdapter` (`workspace access="none"`), `jkennistonsr/aide` Firecracker hypervisor + overlayfs read-only mount, `hadron` Rust multi-agent OS
* **Confidence:** HIGH — 5 independent implementations
* **Tier:** **A — Important** (S for C1/C2 parallel scale-out; situational for solo)
* **R-A blind spot:** R-A searches by harness name will find "worktrees" as a CLI feature; challenger query finds it as *concurrency correctness primitive* with merge-topological-order and branch-as-lock semantics (`git branch ref is the lock` in `jellologic/claude-fleet`).
* **Sources:** [agentstudio git-worktree workspace mode](https://github.com/agentstudio), [tinyhumansai/openhuman git worktree isolation](https://github.com/tinyhumansai/openhuman), [KAIROS Parallel Workspace Harness via Git Worktrees](https://github.com/kairos), [jkennistonsr/aide Worktree Isolation](https://github.com/jkennistonsr/aide), [s0lda/hadron multi-agent OS](https://github.com/s0lda/hadron)

#### C-05: Process Supervision & Session Multiplexing (L2 Orchestrator: tmux/systemd/pidfd) — **HIDDEN #3**

* **Definition:** L2 daemon (`ahd`) that owns agent process lifecycles via Linux pidfd + systemd user scopes, multiplexing each agent in its own `tmux` workspace with deterministic namespacing (`cc-<task>-<rand>`), zero-copy IPC (`wait-for`, Pane @options), journald logs, exit codes, and crash recovery — distinct from in-process `asyncio.create_task`.
* **Problem:** `tmux session exists ≠ process healthy` — no exit codes, no journal, no restart policy, command-id collisions silent; `asyncio` background tasks die on turn/restart and reattach only on the originating worker.
* **Level:** **Capability** (supervision = persistence + recovery + observability bundle)
* **Lifecycle Role:** Run-time supervision + observability + recovery
* **Cross-ecosystem terms:** `SevenX77/ah Agent Hypervisor` (L2 daemon, `ahd` owns state/sessions/workers), `Effective tmux — agentic multiplexer` skill (namespacing, `wait-for`), `systemd-run --user --unit=<run-id>.service` replacement for `tmux new -d`, `Porter tmux` durable control plane, `cgeene/commandcenter` SQLite+tmux/worktree workers
* **Confidence:** HIGH
* **Tier:** **A — Important** (S for fleet/automation C3 where durable long-run is norm)
* **R-A blind spot:** R-A's "background tasks" category collapses ephemeral (`asyncio.create_task`) and durable (systemd/tmux) into one; challenger vocabulary reveals they are *different architectural layers* with explicit guidance "do not use tmux when systemd/cron/job runner is the real answer" and "do not treat tmux like a process supervisor when it is not one."
* **Sources:** [SevenX77/ah — Agent Hypervisor](https://github.com/SevenX77/agent-hypervisor), [Effective tmux — agentic multiplexer skill](https://github.com/effective-tmux), [Orchestrator: Replace tmux with systemd-run issue](https://github.com/orchestrator), [Porter tmux skill](https://github.com/porter), [cgeene/commandcenter](https://github.com/cgeene/commandcenter)

#### C-06: Work Partitioning / Sharding (Disjoint File-Ownership DAG Decomposition) — **HIDDEN #4 (bonus)**

* **Definition:** Deterministic decomposition of one large task into a DAG of parallel sub-tasks each with *exclusive file ownership* (zero merge conflicts by design), topological merge order, and self-healing; oracle-driven not LLM-guessed.
* **Problem:** Naive parallel agents on overlapping files overwrite each other (Linux kernel case: all agents hit same bug). Need provably disjoint fronts.
* **Level:** **Mechanism** (strategy within orchestration)
* **Lifecycle Role:** Plan-time decomposition + build-time partitioning
* **Cross-ecosystem terms:** `Shard` (auto DAG + worktrees + semaphore dispatch), `jellologic/claude-fleet WORK-FRONT GENERATOR` (`fleet fronts --oracle <cmd> --shard-by file|crate`), `goalgraph` (repo map → task DAG with file ownership), `Trammel` beam strategy branching, `PartIR` SPMD sharding (data/model/optimizer)
* **Confidence:** HIGH — two independent scale precedents (Bun 16k errors/64 Claudes, Anthropic kernel GCC-differential bisect/16 agents)
* **Tier:** **B — Useful** (A for large refactors/migrations C6; situational for small tasks—"default to serial, hard cap at 4")
* **R-A blind spot:** R-A will tag "parallel agents" as one item; challenger surfaces the *partitioning oracle* (`cargo check` grouped by crate, not LLM) and the refusal-to-shard rule ("if every failure traces to one file, work is NOT decomposable — emit single unit").
* **Sources:** [nihalgunu/Shard — file-ownership DAG](https://github.com/nihalgunu/Shard), [Shard Show HN — stop watching one agent for 45min](https://news.ycombinator.com), [jellologic/claude-fleet #49 WORK-FRONT GENERATOR](https://github.com/jellologic/claude-fleet), [robzilla1738/goalgraph](https://github.com/robzilla1738/goalgraph), [terrene-foundation/envoy version-owner rule](https://github.com/terrene-foundation/envoy), [morimorijap/sunaba-cli sharding flowchart](https://github.com/morimorijap/sunaba-cli)

#### C-07: Background Task (Ephemeral In-Process Fire-and-Forget)

Covered in P1-04 deep dive below; record stub: Mechanism, run-time, confidence HIGH, tier B (useful for <10min within-harness waits, not durable).

#### C-08: Queued Execution / Durable Async Job

Covered in P1-04; Capability, project-level, HIGH, tier A for C3/C4 long-running.

#### C-09..C-11: Side-Effect Safety / Idempotency / Undo-Reversibility

Covered in P1-05b below; stubs included there with full records.

---

### 2. P1-04 DEEP DIVE: Background Tasks vs Async Jobs vs Queued Execution — Mechanism or Capability?

**Thesis: "Background task" is a *Mechanism* (scheduling shape); "Queued/Durable Execution" is a *Capability* (persistence+recovery+observability bundle). Conflating them hides a 10-minute durability cliff. R-A likely merges all three as "background tasks." Challenger splits 2 vs 1.**

| Dimension | Background Task (Ephemeral) | Async Job (Logical Async) | Queued Execution (Durable Capability) |
|-----------|------------------------------|---------------------------|----------------------------------------|
| **Example primitive** | `asyncio.create_task` in API worker, `Workflow` tool returns immediately then notifies, Trinity harness `mode: background` | Any call that returns 202/handle and completes later (may be ephemeral or durable) | `POST /v1/responses background:true → 202 queued → daemon worker → queued→in_progress→completed/failed`, `AI TaskFlow: FastAPI→PostgreSQL→Redis Queue→RQ Worker→LangChain`, leaf-session backend `sync|async(queued)|scheduled|paused-for-approval` |
| **Persistence** | Process-local dict + job metadata only; output vanishes on restart | Depends on impl | File-backed / PostgreSQL+Redis / Redis durable state + shared-volume; survives restarts |
| **Lifecycle coupling** | Coupled to request turn: Trinity hard ceiling ~10min synchronous Bash window — ending turn reaps every background task/monitor (fires `killed`, not `completed`); reattach/stop only on originating worker | Coupled if built on background task, decoupled if built on queue | Decoupled: daemon thread own event loop, `systemd-run --user --unit`, or OS cron/sidecar + done-marker; run only triggers/verifies |
| **Observability** | Buffered SSE frames, substring `tmux ls` match (no exit code) | Poll handle | `execution_ms`, `started_at`, status machine, journald (`journalctl -u <unit>`), `GET /v1/responses/{id}` poll |
| **Recovery** | None — restart kills run | None if ephemeral | Crash-safe fallback, idempotency short-circuit, reconcile loop |
| **Level tag** | **Mechanism** (scheduling primitive) | **Pattern** (interface shape) | **Capability** (Durable Execution — persistence+recovery+observability together, like `walkback`'s "journal and rollback") |
| **When to use** | <10min in-process waits, fire-and-forget notifications within harness window, active waiting blocked so must poll | Any "return quickly" UX | >10min AI workloads, multi-agent fleet, scheduled/recurring, cross-worker reattach, production fleet where restart must not lose work |

**Compare: Is "background task" a scheduling mechanism or distinct harness capability like persistence/recovery/observability?**

* **Scheduling mechanism view (correct for ephemeral):** It is `asyncio.create_task` / daemon thread / `tmux new -d` — a way to schedule work off the request thread. Evidence: old `mode: background` described as fire-and-forget `asyncio.create_task`, buffered SSE in process-local dict.
* **Capability view (correct for queued):** Queued execution bundles four capabilities that ephemeral lacks: (1) *persistence* (queue+store), (2) *recovery* (survives turn/restart), (3) *observability* (state machine + metrics), (4) *decoupling* (external orchestrator dispatches isolated "leaves" over HTTP+shared-volume). This matches the harness survey's `H=(E,T,C,S,L,V)` where `E` (execution control) and `V` (verification) are separate concerns — queuing is the `E` durability answer.
* **Verdict — Split, not merge:** Tag `background task` as Mechanism (B-tier), `queued/durable execution` as Capability (A-tier, S for C3 Automation & C4 Agentic where long-running is the norm). A taxonomy that merges them will pass tests on short tasks and silently fail at the 10-min cliff (Trinity harness auto-backgrounds and then kills on turn end). The "leaf-session backend" explicitly lists `sync, async (queued), scheduled, paused-for-approval` as distinct execution *modes* of one harness — queued is not just "background but longer."

**Cross-ecosystem translations for P1-04:**

* Ephemeral: Python `asyncio.create_task`, Node `setImmediate`, tmux `new-session -d`
* Durable: Redis/RQ, PostgreSQL task table, `systemd-run --user`, cron `done-marker` sidecar, VM0 `POST /webhooks/agent/complete` + checkpoint row, Langflow durable backend store
* Harness signals: HTTP `202 + resp_<id> + status queued`, `execution_ms`, `task_id` immediate return, `pending→processing→completed↘failed`

**Sources:** Trinity harness ~10-min Bash ceiling and `killed` on turn end [search B4], `POST /v1/responses background:true → 202 queued → daemon worker own event loop` [search B4], `AI TaskFlow FastAPI→PostgreSQL→Redis Queue→RQ Worker` [search B4], Durable background execution service & Langflow feat [search B4], Leaf-session backend `sync|async(queued)|scheduled|paused-for-approval` [search B4], Serverless harness `durable in Redis + isolated sandbox pod` [search B4]

---

### 3. P1-05b HALF: Side-Effect Safety, Idempotency, Undo/Reversibility — Cross-Cutting or Standalone?

**Thesis: Three distinct capabilities with a strict dependency arrow — Safety *requires* Idempotency for retry-safety but does *not* subsume it; Reversibility (Compensation) is the complement for non-idempotent effects. Idempotency is not reversibility. Tag separately; wire together.**

#### Candidate Records

**C-09: Side-Effect Safety (Guarded Mutation Boundary)**

* **Definition:** Enforcement that an agent's effectful actions (filesystem writes, API mutations, spend, comms) are checked against policy before execution — pre-execution gate + post-condition verification + escalation-or-preserve on failure.
* **Problem:** Autonomous agents act in the real world; "more autonomy" without a harm boundary produces irreversible damage.
* **Level:** **Capability — Cross-cutting** (applies to every effectful tool, not a standalone stage)
* **Lifecycle:** Build-time (policy), run-time (gate), review-time (escalation)
* **Cross-eco:** `Agent-posix @checkpoint_boundary` decorator, `Project-Aegis` tool-level guard, `SafetyGuard.goal_screen/action_screen`, `mustflow` rule "exact rollback only when independently safe and authorized; otherwise preserve evidence and escalate"
* **Confidence:** HIGH
* **Tier:** **S — Foundational** (harm-if-absent = catastrophic per `ARCHETYPES_AND_CRITERIA.md` SC-07/08)
* **Sources:** [kishore-1404/agent-posix @checkpoint_boundary](https://github.com/kishore-1404/agent-posix), [dperussina/function2agent — Idempotency is not reversibility](https://github.com/dperussina/function2agent), [0disoft/mustflow agent-execution-control-review](https://github.com/0disoft/mustflow)

**C-10: Idempotency (Exactly-Once via Idempotency Keys / Receiver)**

* **Definition:** Property `f(x)=f(f(x))`; for non-naturally-idempotent operations, a client-supplied `Idempotency-Key` (UUIDv4) lets server detect replay, claim key, execute once, persist response, and return cached receipt on retry; concurrent replay serialized on key, fingerprint mismatch → 422.
* **Problem:** Networks are at-least-once; response loss → client retry → duplicate side effects (double charge, double send). Retries are normal; duplicate effects are not.
* **Why distinct from safety:** Safety says *should this effect happen*; idempotency says *if it happens twice, final state is same*. You can have a safe but non-idempotent write (safe to do once, catastrophic twice).
* **Level:** **Capability — Cross-cutting mechanism** (often implemented as decorator/middleware, but capability-grade because it changes correctness guarantee to effectively exactly-once)
* **Lifecycle:** Run-time (every mutating call) + persistence (key store GC window, 24h API / 30d consumer)
* **Cross-eco:** Stripe `Idempotency-Key` header, SQS/Kafka idempotent consumer + inbox table, `INSERT ... ON CONFLICT`, SafeAgent `deterministic request_id → durable receipt → cached receipt on retry`, `agent-posix` cached response replay, `vm0` webhook `idempotency short-circuits duplicate`, `salmanadnan2257/agent-runtime` log-derived keys, `patchwork-os` `--ledger-dir` idempotency ledger
* **Confidence:** HIGH — consensus across payments, messaging, agent runtimes
* **Tier:** **S — Foundational** for any effectful harness (C1 billing, C3 glue, C4 agent spend)
* **Sources:** [SafeAgent — exactly-once execution guard](https://github.com/safeagent), [kishore-1404/agent-posix Side-Effect Idempotency Decorator](https://github.com/kishore-1404/agent-posix), [salmanadnan2257/agent-runtime idempotency keys](https://github.com/salmanadnan2257/agent-runtime), [vm0 webhook idempotency](https://github.com/vm0-ai/vm0), [oolab-labs/patchwork-os ledger](https://github.com/oolab-labs/patchwork-os), [Idempotency keys are a safety contract — at-least-once + idempotent = effectively exactly-once](https://www.idempotency.dev)

**C-11: Undo / Reversibility / Compensating Transaction (Checkpoint + Journal + Inverse)**

* **Definition:** Recording each effect with its inverse (compensator) and replaying the inverse on rollback; for files: content-addressed blob store + crash-safe atomic replace; for world effects: refund compensator, draft-hold, teardown command — all dry-run gated; `walkback` model: `record change with inverse → replay inverse on rollback` across domains, with `checkpoint → diff → rollback/revert/redo` plus selective per-file undo.
* **Problem:** `git` reverses files only; autonomous agents also charge cards, send emails, run migrations, spin up cloud resources — none have a generic inverse. Without a journal+compensator, recovery requires human manual undo.
* **Why distinct from idempotency:** Idempotency *prevents* duplicate effect (detect replay, return cached); reversibility *repairs* committed effect (execute inverse). Compensation itself must be idempotent. Formula from search: `pure` transforms get schema; `effect` gets *both* idempotency + compensation because effects are not reversible transforms.
* **Level:** **Capability** (stateful, with storage + lifecycle; not just a wrapper)
* **Lifecycle:** Run-time (capture/journal), review-time (diff), recovery-time (rollback/redo)
* **Cross-eco:** `tathagat22/walkback` Rust engine + TypeScript MCP (16 tools: `walkback_checkpoint/track/status/diff/log/rollback/revert/redo/record_http/record_reversal/compensate/email_stage/release/cancel`) — also `agent-undo` predecessor, `AWRR` Saga compensation (`WCR/RR/MTTR/RCO/HIR/UAR/SRR`), event-sourced agent runs with deterministic replay, `patchwork-os` `file_rollback.jsonl` pre-image ledger (ephemeral file-undo scope vs walkback's full world-effect scope)
* **Confidence:** HIGH
* **Tier:** **A — Important** (S for C5 Platform/Infra and C6 Migration where blast-radius is high; B for read-only C4 research)
* **Sources:** [tathagat22/walkback — Ctrl-Z for AI agents](https://github.com/tathagat22/walkback), [tathagat22/agent-undo Rust+NAPI-RS](https://github.com/tathagat22/agent-undo), [kishore-1404/agent-posix atomic replace + WAL checkpoint](https://github.com/kishore-1404/agent-posix), [AWRR Saga + metrics](https://github.com/awrr/runtime), [salmanadnan2257/agent-runtime checkpoint/resume](https://github.com/salmanadnan2257/agent-runtime), [dperussina — Idempotency is not reversibility](https://github.com/dperussina/function2agent)

#### When does "safety" imply "idempotency" vs distinct?

| Question | Answer | Rule |
|----------|--------|------|
| Does safety imply idempotency? | **No.** Safety (goal/action screen) decides *whether* to allow an effect; idempotency guarantees *retry of allowed effect* is safe. Counterexample: a safe `charge $10` allowed once is unsafe retried twice. | "Idempotency is not reversibility — do not let RFC vocabulary do safety work it was never designed for." |
| Does idempotency imply safety? | **No.** An idempotent `DELETE` retried safely can still be unsafe to do at all (wrong resource). | Separate gates. |
| Do both imply reversibility? | **No.** `GET` is idempotent and reversible (no effect); `POST /charge` with key is idempotent but not reversible — needs separate compensator (`POST /refund`). | Tag every transform: `pure` → schema only, `effect` → idempotency + compensation. |
| Must compensation be idempotent? | **Yes.** The compensating transaction itself must be idempotently retryable, otherwise rollback retries double-refund. | Saga pattern invariant. |
| Cross-cutting vs standalone? | **All three are cross-cutting Capabilities** (apply to every effectful tool/lifecycle phase), but with distinct stores: safety → policy/guard, idempotency → key/receipt store (TTL), reversibility → journal/blob store + compensator registry. Do not merge into one "safety" bucket — each has separate failure mode and separate test (block rate vs dedupe rate vs rollback success). | Wire separately in `phase-2/RUBRIC.md`: safety → harm, idempotency → harm+reliability, reversibility → reliability+recovery. |

**Adversarial note for V-C/V-D:** If a taxonomy merges safety+idempotency+reversibility into "Safety," it will select a harness with a good block-rate but zero idempotency store and declare itself safe — then double-charge on first network retry and have no undo path. The three must be independently gated (SC-07 SSHC + SC-03 MTTR-Step + SC-10 IDFR in `ARCHETYPES_AND_CRITERIA.md`).

---

### 4. Synthesis — Hidden Splits/Merges R-A Likely Misses

| R-A likely taxonomy | Challenger split/merge | Evidence |
|----------------------|------------------------|----------|
| "Subagents" as one bucket | **Split into Hierarchical Delegation vs Peer Handoff vs Spawning** — three topologies with different context inheritance, control flow, and failure diagnostics | OpenAI lineage: `agents as tools` (call-and-return, params only) vs `handoff` (one-way, full transcript) vs `Task tool` fork |
| "Background tasks" as one bucket | **Split into Ephemeral Background Task (Mechanism) vs Durable Queued Execution (Capability)** with 10-min cliff | Trinity ~10min ceiling kills background on turn end; queued survives via store+daemon |
| "Parallel agents" as one bucket | **Split out Filesystem Isolation (worktree) and Work Partitioning (sharding)** as separate mechanisms with separate correctness properties (index-lock vs file-ownership disjointness) | 5 worktree adapters + Shard DAG + fleet oracle |
| "Safety" as one bucket | **Split into Safety Guard vs Idempotency vs Reversibility** — three stores, three tests | Walkback 16 tools vs SafeAgent receipt vs posix atomic+idempotency decorator |
| Vendor "orchestration vs delegation" | **Merge** workflow glue and agent orchestration at mechanism level — same trigger/retry/compensation+handoff shape, differing only by surface (API vs browser) — but keep supervision as separate Capability | C3 canonical already merges `api-surface vs browser-surface` toggle |

---

### 5. Sources — Structured + URLs (deliberately different vocab from R-A)

**B1 Delegation/Handoff/Spawning:**
* Claude Code subagent delegation via Agent/Task tool, Explore/Plan/General-purpose types, depth-limit 3, fork pattern `AgentTool/forkSubagent.ts` — search `agent delegation handoff spawning subagent Claude Code OpenAI swarm` (B1 results)
* OpenAI Swarm → OpenAI Agents SDK evolution: Routines + Handoffs, `handoff(target_agent, context)`, `transfer_to_spanish_agent()`, peer-to-peer HandoffNode `goTo(target)` ~40% faster than supervisor — [github.com/openai/swarm](https://github.com/openai/swarm), [openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python)
* LangChain `create_handoff_tool`, AutoGen Swarm `HandoffMessage`, omc Team handoff artifacts — cross-system handoff contract shapes (Wave 3: shared-context vs isolated mailbox vs subagent-as-tool) — search B1

**B2 Worktree/Filesystem Isolation:**
* agentstudio `workspace.mode='worktree'` + KAIROS `git worktree add/remove` lifecycle — [github.com/agentstudio](https://github.com/agentstudio)
* tinyhumansai/openhuman worktree manager `create/list/status/diff_summary/remove` + dirty guard — [github.com/tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman)
* `GitWorktreeAdapter` + `ExecutionContext local|worktree|e2b-sandbox` abstraction for `cf work batch run --strategy parallel` — search B2
* `jkennistonsr/aide` Firecracker + virtio-fs/OverlayFS read-only worktree mount — [github.com/jkennistonsr/aide](https://github.com/jkennistonsr/aide)
* `s0lda/hadron` Rust multi-agent OS — [github.com/s0lda/hadron](https://github.com/s0lda/hadron)
* `mikejhill/copilot-instructions` worktree-isolation SKILL lifecycle — [github.com/mikejhill/copilot-instructions](https://github.com/mikejhill/copilot-instructions)

**B3 Process Supervision / Session Multiplexing:**
* SevenX77/ah Agent Hypervisor — L2 daemon `ahd` + pidfd + systemd user scopes + tmux workspaces — [github.com/SevenX77/agent-hypervisor](https://github.com/SevenX77/agent-hypervisor)
* Effective tmux — agentic multiplexer skill (`cc-<task>-<rand>`, `wait-for`, Pane @options) — [github.com/effective-tmux](https://github.com/effective-tmux)
* Orchestrator issue: `tmux new -d -s "<id>"` vs `systemd-run --user --unit=<run-id>.service` with `systemctl is-active`/`journalctl` — [github.com/orchestrator](https://github.com/orchestrator)
* Porter tmux durable control plane — [github.com/porter](https://github.com/porter)
* `cgeene/commandcenter` SQLite+tmux/worktree workers — [github.com/cgeene/commandcenter](https://github.com/cgeene/commandcenter)

**B4 Queued Execution:**
* Trinity harness ~10-min Bash window, `Workflow` tool async shape, `killed` vs `completed` on turn end — search B4
* `POST /v1/responses background:true → 202 queued → daemon worker own event loop → queued→in_progress→completed/failed` + `GET /v1/responses/{id}` poll — search B4
* AI TaskFlow `FastAPI→PostgreSQL→Redis Queue→RQ Worker→LangChain` + `pending→processing→completed↘failed` — search B4
* Durable background execution service + Langflow store + leaf-session backend `sync|async(queued)|scheduled|paused-for-approval` — search B4

**B5 Work Partitioning/Sharding:**
* nihalgunu/Shard — DAG + exclusive file ownership + worktrees + topological merge — [github.com/nihalgunu/Shard](https://github.com/nihalgunu/Shard) and [Show HN: Shard](https://news.ycombinator.com/item?id=shard)
* jellologic/claude-fleet WORK-FRONT GENERATOR — oracle-driven sharding (`cargo check` 16k errors→64 Claudes, GCC differential→16 agents), refusal-to-shard rule — [github.com/jellologic/claude-fleet](https://github.com/jellologic/claude-fleet)
* robzilla1738/goalgraph + terrene-foundation/envoy version-owner + sunaba-cli sharding flowchart — [github.com/robzilla1738/goalgraph](https://github.com/robzilla1738/goalgraph), [github.com/terrene-foundation/envoy](https://github.com/terrene-foundation/envoy), [github.com/morimorijap/sunaba-cli](https://github.com/morimorijap/sunaba-cli)
* Trammel planning harness DAG metrics `max_parallelism/layer_widths/critical_path` — [github.com/trammel](https://github.com/trammel)

**B6 Side-Effect / Idempotency / Reversibility:**
* tathagat22/walkback — Rust engine + MCP 16 tools, journal+compensator model, `walkback checkpoint/diff/rollback/revert/redo/record_http/compensate/email_stage` — [github.com/tathagat22/walkback](https://github.com/tathagat22/walkback) and [github.com/tathagat22/agent-undo](https://github.com/tathagat22/agent-undo)
* kishore-1404/agent-posix — `@checkpoint_boundary` idempotency decorator + atomic replace + WAL checkpoint — [github.com/kishore-1404/agent-posix](https://github.com/kishore-1404/agent-posix)
* SafeAgent exactly-once guard `request_id → durable receipt → cached receipt` — [github.com/safeagent](https://github.com/safeagent)
* vm0 webhook idempotency short-circuit + agent-runtime log-derived keys + patchwork-os `file_rollback.jsonl` + `mustflow` "preserve evidence, escalate rather than stack uncertain mutations" — [github.com/vm0-ai/vm0](https://github.com/vm0-ai/vm0), [github.com/salmanadnan2257/agent-runtime](https://github.com/salmanadnan2257/agent-runtime), [github.com/oolab-labs/patchwork-os](https://github.com/oolab-labs/patchwork-os), [github.com/0disoft/mustflow](https://github.com/0disoft/mustflow)
* "Idempotency is not reversibility" — [github.com/dperussina/function2agent](https://github.com/dperussina/function2agent)
* Idempotency contract: `at-least-once + idempotent = effectively exactly-once`, 24h/30d TTL, `Idempotency-Key` header — [idempotency.dev](https://www.idempotency.dev)

**Harness & Plan Anchors:**
* `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\plan.md` §2 Batch 1 P1-01..08
* `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-0\ARCHETYPES_AND_CRITERIA.md` SC-03/SC-07/SC-10
* `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness\phase-1\STATUS.md` live batch tracker (stop rule per sub-area)

