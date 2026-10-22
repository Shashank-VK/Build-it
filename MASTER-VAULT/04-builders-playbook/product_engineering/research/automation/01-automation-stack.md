# §26 — The Complete Automation Stack: 12 Layers

**The Omniscient Resource Atlas · product_engineering / automation · Built 2026-10-10**
**Read-only research only.** This file discovers, inspects, and categorizes. It does not install, build, configure, rank, or recommend.

## How to read the labels

Every factual claim carries one of five labels:

- **Verified** — read directly in the primary source (official docs, company engineering blog) during this pass.
- **Corroborated** — reported consistently by ≥2 independent secondary sources, or once in a primary source not directly fetched this pass.
- **Inferred** — standard industry practice the author is confident about but did not re-verify against a primary source in this pass.
- **Proposed** — the author's synthesis or recommendation; not a report of anyone's practice.
- **Unknown** — could not be established; listed as a gap.

**Evidence classes:** `official-docs` (vendor/company documentation), `eng-blog` (company engineering blog), `paper`, `repo` (public repository), `practitioner` (blog post, talk, or write-up by a practitioner), `forum` (HN/Reddit/X/discussion), `standard` (OWASP, IETF, published book), `mirror` (third-party mirror/summary of a primary source).

Terms are explained in three parts: **plain English** (what it is, no jargon), **example** (a concrete instance), **mechanics** (how it actually works).

---

# PART A — The 12 layers

## Layer 1 — Triggers and events

**Plain English.** The "what starts it" layer. Something in the world changes — a timer fires, a webhook arrives, a developer pushes code, an alert goes off — and the automation layer turns that occurrence into a unit of work.

**Mechanics.** Event sources emit occurrences; a delivery mechanism (scheduler, event bus, webhook endpoint, VCS event payload) carries them to the orchestration layer. Two properties matter more than the source list: (a) **delivery guarantees** — at-least-once is the norm (the event may arrive twice), so consumers must tolerate duplicates; (b) **deduplication identity** — a stable event ID lets the consumer ignore repeats (see Layer 2/8 on idempotency). Scheduled triggers deserve jitter (randomized offset) so thousands of jobs don't stampede at the top of the hour — **Verified**, AWS Builder's Library: *"add jitter to all timers, periodic jobs or delayed work."*

**Real examples (grounded).**
- Dependabot's schedule: `schedule.interval` of `daily`, `weekly`, or `monthly` in `dependabot.yml` triggers a manifest scan. **Verified**, GitHub Docs.
- Temporal **Schedules** as a cron replacement with overlap policies, pause/resume, and backfill. **Corroborated** (practitioner gap-analysis of Temporal docs; not fetched from docs.temporal.io this pass).
- GitHub Actions workflow triggers on `push` / `pull_request` events: the Copilot coding agent itself runs *inside* GitHub Actions on an ephemeral runner after being assigned an issue. **Verified**, GitHub Docs (Copilot coding agent overview).

**Design note.** Triggers are the cheapest layer to build and the most common source of thundering-herd outages. When many consumers retry or wake on the same schedule, the trigger layer becomes the failure (see Part B, jitter).

## Layer 2 — Workflow orchestration

**Plain English.** The conductor: it decides *what runs, in what order, and what happens when a step fails* — and it remembers where it was, so a crash doesn't mean starting over.

**Two schools, both real:**

**A. Workflows-as-code / durable execution (Temporal).** You write an ordinary function; the platform persists its progress. **Verified** from docs.temporal.io:
- **Workflows** are pure orchestration code (no network/file I/O inside — that lives in **activities**). **Corroborated** (practitioner skill doc summarizing Temporal rules).
- **Activities** carry a **RetryPolicy** (defaults: initial interval 1s, backoff coefficient 2.0, max interval 100× initial, unlimited attempts, all errors retried unless marked non-retryable) and four **timeouts**: schedule-to-start (queue wait), start-to-close (one attempt's runtime), schedule-to-close (total across attempts), heartbeat (max gap between heartbeats for long activities).
- **Durable timers**: `workflow.sleep(30 days)` consumes no resources while waiting and fires reliably. **Heartbeats** double as progress checkpoints — the last heartbeat's details are handed to the next retry attempt so work isn't repeated from zero.
- **Deduplication vs idempotency are different problems and you need both** (Temporal's own framing): the Activity ID stops you *submitting* the same job twice; idempotent activity code stops one job's side effects *happening* twice when retried.
- Workers long-poll **task queues**; scaling means adding workers; the server never runs user code. Workflow state survives crashes via **event-history replay**; **signals/queries/updates** push data into, read from, or mutate running workflows; **versioning/patching** lets new code deploy while old executions finish on old logic. **Corroborated** (practitioner summary of Temporal docs).

**B. JSON-defined orchestration (Netflix Conductor).** Workflows are declared as JSON task graphs; language-agnostic workers poll for tasks over HTTP. Originally built at **Netflix**, open-sourced under Apache 2.0, now maintained as **Conductor OSS** by Orkes with SDKs for Java, Python, JavaScript, Go, C#. **Corroborated** (project FAQ mirrors, api-evangelist index; docs at `docs.conductor-oss.org`). Built-in retries, error handling, observability; event-driven via queues (SQS/Kafka/AMQP). The trade: declarative and polyglot, but orchestration logic lives outside the type system of your code.

**Also in this layer (Inferred, standard):** DAG schedulers (Airflow/Prefect-style) for batch/data pipelines and step-function services for cloud-native glue. Chosen when the work is a fixed graph of batch steps rather than long-lived, human-interactive processes — where Temporal/Conductor win.

## Layer 3 — Models and reasoning

**Plain English.** The "thinking" layer: which model does the judging, and in what shape — one call, a chain, or a loop.

**The building block.** Anthropic's framing (**Verified**, "Building effective agents," Dec 2024): the foundation is the **augmented LLM** — a model enhanced with **retrieval** (it can look things up), **tools** (it can act), and **memory** (it can retain state). Modern models can generate their own search queries, select tools, and decide what to retain — which is exactly why this layer needs engineering, not just prompting.

**Five workflow shapes** (**Verified**, same source) — LLM capability embedded in *predefined code paths* (these are workflows, not agents):
1. **Prompt chaining** — step A's output feeds step B, with gates between.
2. **Routing** — classify the input, send it down the specialized path.
3. **Parallelization** — *sectioning* (split independent subtasks) and *voting* (run the same task N times, take the best/majority).
4. **Orchestrator-workers** — a central LLM decomposes dynamically, delegates to worker LLMs, synthesizes.
5. **Evaluator-optimizer** — generate ↔ critique loop until criteria are met.

**Model selection discipline** (**Corroborated**, OpenAI's "A practical guide to building agents," 2025): prototype with the most capable model to establish the performance baseline, set accuracy targets with eval metrics, then swap in smaller models wherever accuracy holds — matching model to task complexity, latency, and cost. OpenAI's three signals that an *agent* (not a script) is warranted: complex judgment-based decisions, rulesets grown too brittle to maintain, heavy reliance on unstructured data — *"if none apply a deterministic solution may suffice."*

**Reasoning hygiene** (**Corroborated**, Anthropic "Effective context engineering for AI agents," Sep 2025): treat context as a finite, degradable resource ("context rot" — recall degrades as windows grow). The guiding question is *what is the smallest set of high-signal tokens that maximizes the chance of the desired outcome at each step*. Practical moves: progressive disclosure, compaction near window limits, structured notes outside the window, subagents for deep dives that return distilled summaries.

## Layer 4 — Agent runtimes

**Plain English.** The harness around the model: the loop that feeds tool results back in, the state it carries, the pause button for humans.

**LangGraph (the graph runtime).** **Corroborated** across official-docs mirrors and practitioner write-ups (official docs at docs.langchain.com not re-fetched this pass):
- Agents are **state graphs**: nodes with a typed, shared state; conditional edges are the control flow.
- **Checkpointing**: after each step the runtime serializes state to a checkpointer (SQLite, Postgres, Redis). Crash at step N → resume at step N+1 with exact state. Enables time-travel debugging and multi-turn continuity.
- **Durability modes** (`exit` / `async` / `sync`): a performance–durability dial — persist only on exit, persist asynchronously, or persist synchronously before each step.
- **Human-in-the-loop**: `interrupt()` pauses execution and checkpoints; a human reviews/edits; `Command(resume=...)` on the same `thread_id` continues exactly where it paused. Threads are the persistent cursor.
- **Topologies**: supervisor (central router), swarm/peer-to-peer (handoff via shared tools), hierarchical (nested subgraphs); dynamic fan-out via `Send` for map-reduce shapes.
- One 2026 practitioner note: the LangChain team reportedly recommends implementing supervisor routing through plain tool calls rather than the supervisor helper, for tighter context control (**Corroborated**, single source — treat as evolving guidance).

**Claude Code subagents** (as described by Cognition's engineering essay, **Corroborated** practitioner account): subagents are spawned for subtasks but *never work in parallel with the parent*, and are usually tasked with *answering a question, not writing code* — because the subtask agent lacks the parent's context for anything more. The benefit is context hygiene: investigative work doesn't pollute the main agent's history.

**OpenAI Agents SDK**: handoffs (control transfer modeled as a tool), guardrails, session tracing. **Corroborated** (official SDK docs via reading-list citations).

**Cautionary entry**: Microsoft **AutoGen** is in maintenance mode (README banner; successors AG2 / Microsoft Agent Framework) — recorded in Atlas deliverable H §H5. Framework churn is real; the runtime decision should assume migration.

## Layer 5 — Tool execution

**Plain English.** How the model touches the world: the uniform plug shape between "I want to search the docs" and the docs actually being searched.

**MCP (Model Context Protocol).** Introduced by **Anthropic, November 2024**, open specification. **Corroborated** (Anthropic's own engineering blog references MCP servers as the tool-integration approach; spec at modelcontextprotocol.io):
- An **MCP server** exposes three primitives: **tools** (callable functions, e.g. `search_docs`), **resources** (read-only context, e.g. a file's contents), **prompts** (reusable templates).
- An **MCP client** (Claude Desktop, Cursor, ChatGPT, automation platforms) discovers and calls them over one JSON-RPC dialect. Write the server once; every compatible client can use it — *"LSP for AI tools"* (practitioner shorthand, **Inferred** as community framing).
- Under the hood the model still uses function calling; MCP standardizes discovery, invocation, auth, and description around it.

**Why tool design is the reliability lever.** **Verified** (Anthropic, "How we built our multi-agent research system"): *"Tool design and selection are critical… Bad tool descriptions can send agents down completely wrong paths."* Each tool needs a distinct purpose and a clear description; agents got explicit heuristics (examine all tools first, prefer specialized over generic). In one documented case, an agent that *tested* a flawed MCP tool and rewrote its description cut future agents' task completion time by **40%**.

**Tool safeguards** (**Corroborated**, OpenAI guide): rate every tool low/medium/high risk on read-only vs write access, reversibility, required permissions, and financial impact — then gate accordingly.

## Layer 6 — Retrieval and context

**Plain English.** Getting the right information *into* the model's working memory at the right moment — and keeping the wrong stuff out.

**Mechanics.** Classical **RAG** (retrieval-augmented generation): chunk documents, embed into vectors, fetch the top-k most similar chunks for a query, stuff them into context. Anthropic's research system explicitly contrasts this *static* retrieval with **multi-step agentic search**: the agent issues searches, reads results, adapts queries to new findings, and evaluates quality as it goes. **Verified** (Anthropic multi-agent blog).

**Context assembly patterns** (**Corroborated**, Anthropic context-engineering summaries):
- **Just-in-time retrieval** — fetch when the agent asks, not upfront.
- **Progressive disclosure** — load summaries first, details on demand (Claude Code's 2026 system-prompt work moved verification/review into separately-loaded skills; some tools use deferred loading via search-before-use).
- **Compaction** — near window limits, summarize history preserving decisions, TODOs, and constraints.
- **Structured note-taking** — durable state (`NOTES.md`-style) outside the window with explicit write/read policies.

**Failure mode to know**: "lost in the middle" — models under-attend to information buried mid-context (Liu et al., 2023, cited in practitioner reading lists, **Corroborated**). The practical consequence: retrieval ranking and placement are load-bearing, not cosmetic.

## Layer 7 — Memory and state

**Plain English.** What the system remembers *between* steps and *between* runs — and how it survives a crash in the middle of remembering.

**Three distinct things people conflate:**
1. **Conversation/working state** — the current run's messages and scratchpad. Lives in the runtime's state object (LangGraph) or workflow variables (Temporal).
2. **Durable execution state** — checkpoints that survive process death. LangGraph's checkpointer (per-step snapshots, resume by `thread_id`); Temporal's event history (replay reconstructs state; heartbeats carry progress details into retries). **Verified** (Temporal docs) / **Corroborated** (LangGraph mirrors).
3. **Long-term memory** — facts that persist across runs: user preferences, project conventions, accumulated learnings. LangGraph's cross-session memory store; Anthropic's prescribed pattern of external memory (their research lead agent *saves its plan to memory* because long sessions exceed/truncate context). **Verified** (Anthropic: plan persisted to memory past ~200K tokens).

**Design rule** (**Corroborated**, Anthropic context-engineering): persist durable state *outside* the context window with explicit write/read policies; never rely on the window as a database. Temporal's version of the same rule: workflow code holds orchestration variables; all side effects and their results live in activities and the event log.

## Layer 8 — API and system integrations

**Plain English.** The boring, load-bearing layer: talking to Stripe, GitHub, Slack, and your own services without double-charging anyone or melting down when they hiccup.

**Idempotency — the keystone pattern.** **Plain English:** make repeating a request safe, so "did that go through?" never becomes a double-charge. **Example:** a user clicks Pay, the network drops, the client retries. **Mechanics** (**Corroborated**, Stripe's idempotency design via official API docs and SDK docs): the client generates one key per *logical operation* (UUID v4, ≤255 chars, generated *before* the retry loop) and sends it as `Idempotency-Key`. The server saves the first request's status code and body against the key — *including failures* — and replays the saved result on repeats. Stripe honors keys for 24 hours; same key with a *different* body is rejected (400); never use sensitive data (emails, PII) as keys. Apply at three layers: API requests (header), webhook events (store `event.id` with a unique constraint — Stripe redelivers on failure, so the same event can arrive twice), and business state (DB unique constraints + state-machine guards so fulfillment can't run twice).

**Retry behavior of SDKs** (**Corroborated**, AWS Builder's Library summaries): AWS SDKs implement automatic retry with exponential backoff out of the box; a token-bucket mechanism (in the SDK since 2016) throttles retry storms client-side. For rate limits, Stripe's guidance is exponential backoff *with randomness* to avoid thundering herds (**Corroborated**).

**Integration hygiene for agents** (**Inferred**, standard practice): every external call gets a timeout, a retry policy, an idempotency key, and a circuit breaker; tool descriptions declare which calls are read-only vs mutating (ties to Layer 5's risk ratings).

## Layer 9 — Testing and evaluations

**Plain English.** How you know the thing works — twice: once for the code (tests), once for the judgment (evals).

**Classical tests still apply.** The Copilot coding agent runs in an ephemeral GitHub Actions environment where it can *execute automated tests and linters* — the same gates humans face. **Verified** (GitHub Docs). Branch protections and required status checks apply to agent PRs exactly as to human PRs (**Corroborated**, InfoWorld quoting GitHub's CEO at launch).

**Evals are the new test suite for judgment.** **Verified** (Anthropic multi-agent blog): multi-agent systems defeat step-based testing — two agents can take completely different valid paths to the same answer — so evals must judge *outcomes plus reasonable process*, not prescribed steps. Start evaluating *immediately* with *small samples*: early changes have huge effect sizes (a prompt tweak moving success 30%→80% is visible in a handful of cases). **Corroborated** (OpenAI's evaluation best-practices guide): design task-specific evals with explicit criteria, set accuracy targets, iterate.

**Practitioner reality check** (**Corroborated**, dev.to practitioner, 2026): LLM judges are unreliable graders (14 fluent-but-wrong answers scored 4–5/5 in one 100-question study) — pin behavior with exact-match or oracle-scored regression tests, because agent failures are "invisible in normal use: the system keeps answering, it just answers wrong." Also: **every agent loop needs a hard iteration cap** or a stuck agent runs forever (**Corroborated**, practitioner audit citing Addy Osmani).

## Layer 10 — Deployment infrastructure

**Plain English.** How a change gets from a merged PR to production — and the gates that can stop it.

**Verified reference implementation: GitHub Actions environments** (GitHub Docs):
- A job that references an environment *must satisfy the environment's protection rules before it runs or can read its secrets*.
- **Required reviewers**: up to 6 people/teams; only one approval needed to proceed; optional **prevent self-review** (the person who triggered the deploy can't approve it).
- **Wait timer**: 1 minute to 30 days of delay — a cancellation window for mistaken triggers. Doesn't count as billable time.
- **Deployment branch/tag rules**: e.g. only `main` (or `v*` tags) may reach `production`.
- **Custom protection rules** via GitHub Apps (max 6 per environment): third-party systems — observability, change management, code quality — can gate deployments.
- **Environment-scoped secrets/variables**: visible only to jobs referencing that environment.

**Standard promotion shape** (**Corroborated**, multiple practitioner repos): `dev` (auto, all branches) → `staging` (1 reviewer, `main` only) → `production` (2 reviewers + wait timer + version tags only). Secrets and OIDC trust policies are scoped per environment so a staging credential can never mint production access.

## Layer 11 — Observability

**Plain English.** Seeing what the automation did, why, and what it cost — while it's running and after.

**Three telemetry levels, all needed:**
1. **Execution traces** — every workflow run's step history. Temporal's Web UI renders the full event history with stack traces; LangGraph streams per-node state deltas and checkpoints. **Verified** (Temporal docs) / **Corroborated** (LangGraph).
2. **LLM-specific traces** — per-call inputs, outputs, tool calls, token counts, latency. The OpenAI Agents SDK ships tracing (spans for agent steps); dedicated LLM-observability tools (Langfuse, LangSmith, Braintrust) aggregate this across runs. **Corroborated** (SDK docs citations); vendor tooling details **Unknown** this pass (not re-verified).
3. **Cost metering** — token usage per run/agent/workflow, with budgets and alerts. The "$50K runaway agent" incident report argues for orchestration-layer budgets, circuit breakers, and kill-switches as *deployment requirements*, not nice-to-haves (**Corroborated**, practitioner incident write-up, single report — treat the incident as anecdotal, the pattern as standard).

**Debugging multi-agent systems** (**Verified**, Anthropic): failures hide in the orchestrator's plan, the subagent's interpretation, its tool use, the summarization, or the integration of summaries — without strong observability "debugging gets very hard very fast" (practitioner gloss, **Corroborated**). Anthropic's own method: simulations with exact prompts+tools, watching agents step by step.

## Layer 12 — Security and governance

**Plain English.** Keeping the automation from being tricked, from leaking, and from doing things nobody approved.

**The threat list: OWASP Top 10 for LLM Applications (2025)** (**Corroborated**, genai.owasp.org; list confirmed across 3 sources): LLM01 Prompt Injection · LLM02 Sensitive Information Disclosure · LLM03 Supply Chain · LLM04 Data and Model Poisoning · LLM05 Improper Output Handling · LLM06 Excessive Agency · LLM07 System Prompt Leakage · LLM08 Vector and Embedding Weaknesses · LLM09 Misinformation · LLM10 Unbounded Consumption.

**What the field has learned (all Corroborated unless noted):**
- **Prompt injection (LLM01) has no reliable fix.** It topped the list in both the 2023 and 2025 editions. The cause is structural: the model reads instructions and untrusted content through the same channel, so hidden commands in a webpage/email/PDF/tool output are indistinguishable from legitimate ones. OWASP's position is that fool-proof prevention is not established.
- **Design for containment, not filtering.** Practitioner consensus (Simon Willison's "lethal trifecta," Jun 2025): an agent with *private data access* + *untrusted content* + *external communication* is exploitable by design — remove one leg rather than perfecting a filter. Documented indirect-injection incidents span Bard (2023), Amazon Q (2024), NotebookLM (2024), GitHub's MCP server and GitLab Duo (May 2025), Microsoft 365 Copilot (Jun 2025) (single practitioner source — treat incident list as reported).
- **The Sentry/Seer case** — why this layer is load-bearing for automation: a CERT advisory described an attack chain where attacker-submitted exception events flowed through Seer's root-cause analysis into a coding agent's prompt, and the agent *downloaded and executed an attacker-controlled package before any human reviewed a PR* (**Corroborated**, practitioner report citing CERT). Every automated defect→fix pipeline (see §27 W6) must treat incoming reports as untrusted input.
- **Guardrail layering** (OpenAI guide, **Corroborated**): relevance classifier, safety classifier, PII filter, moderation, tool safeguards (risk-rated), rules-based protections (blocklists, input limits), output validation — plus failure thresholds and high-risk triggers for **human escalation**.
- **Governance mechanics** (**Verified**, GitHub Docs): prevent self-review on deployments; branch protections and required checks apply to agent-created PRs; environment secrets are scoped so a compromised job can't read what it shouldn't. Least-privilege tool permissions map directly to OWASP LLM06 (Excessive Agency): give the agent the smallest tool set that can do the job.
- **Supply chain** (LLM03): MCP servers are now a software supply chain — a malicious or compromised server sits inside the agent's tool boundary. Pin versions, review server code, treat community servers like dependencies (**Inferred**, standard reasoning from LLM03).

---

# PART B — Cross-cutting reliability mechanics

The §26 brief names ten mechanisms. Each: plain English, example, mechanics.

**1. Queues.** *Plain English:* a waiting line between "work arrived" and "work gets done," so bursts don't crush the worker. *Example:* Temporal task queues; SQS/Kafka feeding Conductor workers. *Mechanics:* producers enqueue; workers long-poll; backpressure is natural (the queue grows instead of the worker dying); ordering and dedup are queue properties you choose, not free. **Corroborated** (Temporal docs: workers pull from task queues; scaling = add workers).

**2. State machines.** *Plain English:* the work is always in exactly one named state (queued → running → awaiting-approval → done), and only legal transitions can happen. *Example:* a Dependabot PR's lifecycle; LangGraph's graph with conditional edges. *Mechanics:* transitions are explicit and logged; illegal jumps are impossible by construction; the current state is queryable (Temporal queries; LangGraph thread checkpoints). **Inferred** (standard pattern; instances verified).

**3. Durable execution.** *Plain English:* the automation remembers where it was across crashes, deploys, and even days of waiting. *Example:* Temporal workflow that sleeps 3 days between onboarding emails, then continues. *Mechanics:* every state transition is appended to an event log; on recovery the runtime *replays* the log to rebuild state instead of re-running side effects (which live in activities, retried by policy). **Verified** (docs.temporal.io).

**4. Retries.** *Plain English:* try again when failure looks temporary. *Example:* a flaky LLM API call retried with backoff. *Mechanics:* retry at **one** layer of the stack, not every layer (five layers × three retries can multiply load 243× against the database — AWS's memorable arithmetic, **Corroborated**); exponential backoff with a cap; never retry 4xx/client errors; mark non-retryable error types explicitly (validation, auth). **Verified** (AWS Builder's Library; Temporal default policy).

**5. Timeouts.** *Plain English:* a deadline that turns "is it slow or dead?" into a decision. *Example:* Temporal's start-to-close timeout on one LLM call attempt. *Mechanics:* set from latency percentiles (p99.9 forces the "how many false positives are OK?" conversation — AWS); distinguish queue-wait from run-time from total-deadline (Temporal's four timeouts, **Verified**). A timeout proves nothing about the remote side — the operation may have succeeded (see idempotency).

**6. Idempotency.** *Plain English:* doing it twice has the same effect as doing it once. *Example:* Stripe's `Idempotency-Key` header; Temporal's activity-ID uniqueness. *Mechanics:* the server stores (key → result) and replays instead of re-executing; generate one key per *logical operation* before the retry loop; remember Temporal's distinction — dedup keys stop *resubmission*, idempotent code stops *double side effects* (**Verified**, docs.temporal.io). Retries without idempotency on side-effecting calls are how you double-charge customers (**Verified**, AWS: "APIs with side effects aren't safe to retry unless they provide idempotency").

**7. Checkpoints.** *Plain English:* saved progress you can resume from instead of restarting. *Example:* LangGraph checkpoint after each node; Temporal heartbeat details handed to the next attempt. *Mechanics:* serialize state (and partial progress) at step boundaries; resume reads the checkpoint, skips completed work; time-travel debugging falls out for free. **Verified** (Temporal) / **Corroborated** (LangGraph).

**8. Parallel execution.** *Plain English:* do independent things at the same time. *Example:* Anthropic's lead agent spinning up 3–5 subagents in parallel, each using 3+ tools in parallel — cutting research time up to 90% (**Verified**). *Mechanics:* fan-out/fan-in with a join; the orchestrator waits for the batch (Anthropic calls the synchronous wait a "bottleneck" they ship anyway because it simplifies coordination — **Corroborated**); parallelism is only safe over *independent* work (see Part C).

**9. Recovery.** *Plain English:* what happens after something breaks — automatically. *Example:* worker dies mid-activity → Temporal redispatches; saga compensation (step C fails → run compensations for B then A in reverse, each idempotent). *Mechanics:* replay + redispatch for crash recovery; **saga pattern** (compensating transactions) for multi-service writes since there's no distributed transaction; dead-letter queues for poison messages (**Corroborated** for saga via practitioner Temporal guide; DLQ **Inferred** standard).

**10. Human approvals.** *Plain English:* a person says "go" before the irreversible step. *Example:* GitHub environment required reviewer before production deploy (**Verified**); LangGraph `interrupt()` pausing before a destructive tool call (**Corroborated**); Temporal `workflow.condition()` waiting on a signal for days (**Corroborated**). *Mechanics:* the run checkpoints and suspends with zero compute burn; approval/denial arrives as an external event (signal, API call, UI click); denial routes to a safe terminal state, never to silent continuation. Approvals are the backstop for LLM06 (excessive agency) and LLM10 (unbounded consumption).

---

# PART C — Decision guide: script vs LLM call vs workflow vs agent vs multi-agent

## The ladder (cheapest first)

| Approach | Use when… | Concrete example |
|---|---|---|
| **Deterministic script** | Steps are fixed and enumerable; correctness must be provable; inputs are structured; cost/latency budget is tight | Dependabot's version scan: parse manifest → compare semver → open templated PR (**Verified**, GitHub Docs) |
| **Single LLM call (+ retrieval)** | One judgment on unstructured input; no multi-step tool use needed | Classify a support ticket; summarize a thread. "For many apps, a single optimized LLM call with retrieval is enough" (**Corroborated**, Anthropic) |
| **Workflow** (LLM steps on predefined paths) | Steps are known but individual steps need judgment; predictability and consistency matter; you want gates and evals per step | Prompt chain: extract → validate → format, with a human gate before publish (**Verified** pattern catalog, Anthropic) |
| **Agent** (LLM directs its own loop) | Open-ended; step count unpredictable; needs ground truth from the environment each step | "Research this outage": search logs, follow leads, pivot on findings (**Verified** definition, Anthropic; OpenAI's three signals) |
| **Multi-agent** (orchestrator + workers) | Work is *genuinely parallelizable* AND exceeds one context window AND the value justifies ~15× token cost | Breadth-first research across many independent sources (**Verified**, Anthropic: 90.2% lift on internal research eval) |

## Rules of thumb (each labeled)

1. **Start simple; add complexity only when it earns its keep.** Agentic systems trade latency and cost for capability. (**Verified**, Anthropic: "start with the simplest solution possible.")
2. **If none of OpenAI's three signals apply, a deterministic solution may suffice.** Complex judgment-based decisions? Brittle, unmaintainable rulesets? Heavy unstructured-data dependence? No → script it. (**Corroborated**, OpenAI guide.)
3. **"A well-designed single agent with appropriate tools can accomplish far more than many developers expect."** (**Verified**, Anthropic multi-agent blog.) Before adding a second agent, try: better tools, better prompts, more context budget.
4. **Redesign the tools before adding agents.** In a worked five-agent support pipeline, 64% of tokens went to duplicated context and handoff notes; collapsing to one agent didn't cut the bill (the loop re-reads context each turn) — but *rewriting the tools* around what the agent actually needs to decide cut cost below half. (**Corroborated**, practitioner analysis, single study — treat numbers as illustrative.)
5. **The one-agent test:** "Can you say what each agent would be evaluated on *by itself*?" Parallel research, context isolation, separate permissions, verification passes this test. Splitting by job title (planner/coder/tester/reviewer) usually doesn't. (**Corroborated**, practitioner essay synthesizing the debate.)
6. **Parallel reads are safe; parallel writes must be serialized.** Research fan-out is naturally idempotent (many agents reading the web can't corrupt each other); parallel code-writers make conflicting implicit decisions that no composer can reconcile (Cognition's Flappy Bird case, **Verified**). Cognition's 2026 follow-up: the multi-agent setups that actually work are ones where *"multiple agents contribute intelligence to a task while writes stay single-threaded."* (**Verified**, cognition.com.)
7. **Budget the 15×.** Multi-agent uses ~15× the tokens of chat (~4× for single agents) (**Verified**, Anthropic). One practitioner reports ~20K tokens of overhead per subagent invocation regardless of task size (**Corroborated**, single source — treat as rough). Set per-run budgets, iteration caps, and kill-switches as deployment requirements (**Corroborated**, incident write-up).
8. **Most coding tasks are *not* parallelizable.** Anthropic's own caveat: "most coding tasks involve fewer truly parallelizable tasks than research, and current agents are not yet great at coordinating and delegating to other agents in real time." (**Verified**.)

## When multi-agent introduces unnecessary complexity (negative evidence)

- **Cognition (Devin team), Jun 2025, "Don't Build Multi-Agents"** (**Verified**): parallel subagents make implicit, conflicting choices about style, edge cases, and code patterns; the composer inherits "the undesirable task of combining these two miscommunications." Principles: share context (full traces, not messages); actions carry implicit decisions. Default: single-threaded linear agent with context compression. Cognition explicitly criticized OpenAI Swarm and Microsoft AutoGen for pushing multi-agent as the default.
- **The telephone game**: dividing work by phase ("planning agent + implementation agent + testing agent") degrades information at every handoff; Anthropic hit this as an anti-pattern in early versions (**Verified**).
- **Role proliferation**: agents "spawning 50 subagents for simple queries," "scouring the web endlessly for nonexistent sources," "distracting each other with excessive updates" — all observed in Anthropic's early builds (**Verified**).
- **Matched-budget studies** (practitioner synthesis, **Corroborated**): most published multi-agent wins compare a team against a *single agent given far less compute*; budget-matched comparisons shrink or erase the advantage (one cited study: auto-generated multi-agent underperformed a self-consistency baseline at up to 10× the cost).
- **Practitioner skepticism** (**Corroborated**, HN "Ask HN: Is anybody getting value from AI Agents?"): production value clusters in *tightly constrained* agents (one prompt + context + a few functions per subtask) integrated with traditional engineering — not in general-purpose swarms. The recurring quote: don't trust AI with anything you wouldn't trust a high-schooler to do.
- **Framework churn as complexity tax**: AutoGen — once the default multi-agent framework — is in maintenance mode (Atlas H §H5). Betting the architecture on a fast-moving framework is its own risk.

---

# PART D — Gaps and unknowns (this pass)

- **Unknown**: current maintenance status and versioning of Airflow/Prefect/Dagster; AWS Step Functions feature set — not re-verified; orchestration-layer comparison beyond Temporal/Conductor is **Inferred**.
- **Unknown**: Langfuse/LangSmith/Braintrust current features and pricing — named only as the category; not verified.
- **Unknown**: OpenTelemetry's current agent-observability conventions (GenAI semantic conventions) — not verified this pass.
- **Unknown**: exact Dependabot compute backend (how GitHub runs the update jobs) — GitHub Docs describes behavior, not internals.
- **Unknown**: whether Anthropic's 90.2% / 15× figures replicate outside Anthropic's internal eval — vendor-published, uncorroborated by independent replication found this pass.
- **Corroborated-low**: the "$50K runaway agent" incident (single practitioner report); Simon Willison's "lethal trifecta" incident list (single source); ~20K tokens subagent overhead (single source).
- Suggested follow-ups live in `03-evidence-register.md` §Gaps.
