# 05 — AI/Agent Architecture: The Product Is the Harness, Not the Model

**Organizing thesis:** the model is a commodity reasoning component; the *product* is everything around it — prompts, context assembly, tool design, validation, execution, evals, observability, cost controls, and security. Teams that treat "call the API" as the feature ship the failure modes in §4 of `domain-b/01`; teams that engineer the harness ship products. This section synthesizes how agent systems are architected: the anatomy, the patterns, context engineering, tool design, memory/state, eval methodology, cost/latency/reliability engineering, and the agent security control catalog.

---

## 1. The anatomy of an agent system

**The building block** (**Verified**, Anthropic, "Building effective agents," Dec 2024): the **augmented LLM** — a model enhanced with **retrieval** (it can look things up), **tools** (it can act), and **memory** (it can retain state). Modern models generate their own search queries, select tools, and decide what to retain — which is exactly why this layer needs engineering, not just prompting.

**The agent loop** (Corroborated): model reasons → emits a structured tool call (function name + JSON arguments) → harness validates → executes against the real API → returns the result as a message → model continues. Every step can fail — and reliability multiplies *down*: an agent with 85% per-step accuracy completes a 10-step task only ~20% of the time (0.85¹⁰). This compounding is why tool-use benchmarks look so much worse than single-call benchmarks (tau-bench: 61% single-trial → ~25% across 8 trials; MCP-Universe best 43.7%; **Corroborated**).

**The five workflow shapes** (**Verified**, Anthropic) — LLM capability embedded in *predefined code paths* (these are workflows, not agents): (1) **prompt chaining** — step A's output feeds step B, with gates between; (2) **routing** — classify the input, send it down the specialized path; (3) **parallelization** — *sectioning* (split independent subtasks) and *voting* (run N times, take best/majority); (4) **orchestrator-workers** — a central LLM decomposes dynamically, delegates, synthesizes; (5) **evaluator-optimizer** — generate ↔ critique loop until criteria are met.

**Model selection discipline** (**Corroborated**, OpenAI, "A practical guide to building agents," 2025): prototype with the most capable model to establish the baseline, set accuracy targets with eval metrics, then swap in smaller models wherever accuracy holds — matching model to task complexity, latency, and cost. OpenAI's three signals that an *agent* (not a script) is warranted: complex judgment-based decisions, rulesets grown too brittle to maintain, heavy reliance on unstructured data — *"if none apply a deterministic solution may suffice."*

## 2. The architecture patterns (what works, what doesn't)

**Orchestrator-workers — the verified reference build** (**Verified**, Anthropic, "How we built our multi-agent research system"): a lead agent analyzes the query, develops a strategy, and spawns subagents that search **simultaneously**, each in its **own context window**; the lead synthesizes; a separate **CitationAgent** attributes claims; the lead **saves its plan to memory** because long sessions exceed context limits. Measured results (vendor-published internal evals, no independent replication found): Opus 4 lead + Sonnet 4 subagents outperformed single-agent Opus 4 by **90.2%** on research evals (breadth-first queries especially); token usage alone explained **80%** of performance variance on BrowseComp. Cost: ~**15× the tokens of chat** (~4× for single agents). Anthropic's own caveat: this shape fits tasks with heavy parallelization and information exceeding single context windows — *"most coding tasks involve fewer truly parallelizable tasks than research."*

**The counterweight — Cognition's doctrine** (**Verified**, cognition.ai, 2025–2026): default to a **single-threaded linear agent with context compression**. Parallel subagents make implicit, conflicting choices about style, edge cases, and code patterns; the composer inherits "the undesirable task of combining these two miscommunications" (the Flappy Bird case: one subagent built a Mario-style background, another an incompatible bird). The converged rule (2026): use multi-agent only where *"multiple agents contribute intelligence to a task while writes stay single-threaded."* The **one-agent test** (**Corroborated**, practitioner essay): "Can you say what each agent would be evaluated on *by itself*?" Parallel research, context isolation, separate permissions, verification — pass. Splitting by job title (planner/coder/tester/reviewer) — usually doesn't.

**The practical synthesis** (Corroborated): **parallelize reading, serialize writing.** Claude Code's embodiment: subagents answer questions; they don't write code in parallel with the parent. Anthropic's early-build failures fixed by prompt engineering, not infrastructure: 50 subagents spawned for simple queries; endless scouring for nonexistent sources; subagents distracting each other with excessive updates. LangGraph topologies (supervisor / swarm peer-to-peer / hierarchical; **Corroborated**) exist, but the topology decision is secondary to the read/write discipline. And before adding a second agent: try better tools, better prompts, more context budget — *"A well-designed single agent with appropriate tools can accomplish far more than many developers expect"* (**Verified**, Anthropic).

**Hybrid systems need layered playbooks** (Proposed synthesis, `domain-c/09`): read-only coordination under Domain C rules, mutation under Domain A rules — the eng-agent-os "read-only, always" mechanical enforcement is the cleanest expression found in the research.

## 3. Context engineering — the finite, degradable resource

**The doctrine** (**Corroborated**, Anthropic, "Effective context engineering for AI agents," Sep 2025): treat context as a finite, degradable resource — "context rot": recall degrades as windows grow. The guiding question is ***what is the smallest set of high-signal tokens that maximizes the chance of the desired outcome at each step***.

**Practical moves** (Corroborated): **just-in-time retrieval** (fetch when the agent asks, not upfront); **progressive disclosure** (summaries first, details on demand — Claude Code's 2026 system-prompt work moved verification/review into separately-loaded skills); **compaction** near window limits (summarize history preserving decisions, TODOs, constraints); **structured note-taking** (durable `NOTES.md`-style state outside the window with explicit write/read policies); **subagents for deep dives** that return distilled summaries (context hygiene — investigative work doesn't pollute the main agent's history).

**The load-bearing failure mode**: "lost in the middle" — models under-attend to information buried mid-context (Liu et al., 2023; **Corroborated**). Retrieval ranking and placement are load-bearing, not cosmetic.

## 4. Tool design — the reliability lever

**The verified claim** (**Verified**, Anthropic, multi-agent blog): *"Tool design and selection are critical… Bad tool descriptions can send agents down completely wrong paths."* Each tool needs a distinct purpose and a clear description; in one documented case, an agent that *tested* a flawed MCP tool and rewrote its description cut future agents' task completion time by **40%**.

**MCP (Model Context Protocol)** — Anthropic, Nov 2024, open specification (**Corroborated**): a server exposes three primitives — **tools** (callable functions), **resources** (read-only context), **prompts** (reusable templates); a client discovers and calls them over one JSON-RPC dialect. Practitioner shorthand: *"LSP for AI tools"* (**Inferred** as community framing). Under the hood the model still uses function calling; MCP standardizes discovery, invocation, auth, and description.

**Tool safeguards** (**Corroborated**, OpenAI guide): rate every tool low/medium/high risk on read-only vs write access, reversibility, required permissions, and financial impact — then gate accordingly. **The boundary-layer principle** (**Corroborated**): auth, timeouts, retries, and response shaping live in the API-client layer — never exposed to or handled by the model. Secrets are injected by the client layer; the model never sees keys. Simple flat schemas beat clever nested ones (malformed arguments are one of the five predictable tool-call failure modes; validated with Pydantic/Instructor *before* execution).

**The five tool-call failure modes** and their fixes (Corroborated): (1) tool execution failure → return a descriptive error *to the model* as a structured message, never crash the loop; (2) malformed arguments → validate before execution; (3) hallucinated function names → allow-list check; (4) timeouts → explicit timeouts with retries/backoff/circuit breaking *outside* the model; (5) unexpected results → size limits, response translation into minimal model-shaped schemas, sanitization.

## 5. Memory and state — three distinct things, persistently conflated

1. **Conversation/working state** — the current run's messages and scratchpad (LangGraph's state object; Temporal's workflow variables).
2. **Durable execution state** — checkpoints surviving process death: LangGraph's checkpointer (per-step snapshots, resume by `thread_id`, enabling time-travel debugging); Temporal's event history (replay reconstructs state; heartbeats carry progress details into retries). **Verified** (Temporal docs) / **Corroborated** (LangGraph mirrors).
3. **Long-term memory** — facts persisting across runs: preferences, conventions, accumulated learnings (LangGraph's cross-session memory store; Anthropic's lead agent *saves its plan to memory* past ~200K tokens — **Verified**).

**Design rule** (**Corroborated**, Anthropic): persist durable state *outside* the context window with explicit write/read policies; **never rely on the window as a database**. Temporal's version of the same rule: workflow code holds orchestration variables; all side effects and their results live in activities and the event log.

## 6. Eval methodology — the test suite for judgment

**Why evals exist** (Corroborated): AI features are non-deterministic — the same input gives different outputs on different days — so you can't assert exact strings. Evals are the replacement: a curated set of test cases with known-good answers, run automatically every time anything changes, scored by rules, models, or humans. Without them, silent regressions are the norm: the AKR case (a 15% regression discovered *weeks later* from user complaints, ~$200K+ self-reported impact; **Corroborated**) and the healthcare RAG case (94% → 38% failure) both trace to "no systematic quality measurement."

**The eval stack** (Corroborated, practitioner consensus):

| Layer | What it is | Notes |
|---|---|---|
| **Golden datasets** | 50–1,000+ curated input/output pairs with validated correct answers, versioned like code | Built from production logs → expert-validated answers → edge cases, failure modes, adversarial examples. Size guidance: 50–100 minimum viable; 200–500 good coverage; 1,000+ comprehensive with holdout splits. **The rule: your eval is only as good as your golden dataset.** Never silently change expected outputs. Keep a 20–30% holdout you never look at during development, or you overfit the prompt to the test. |
| **Deterministic checks (~60%)** | Exact match, schema validation, regex/keyword assertions, refusal-rate and format-violation rates | Cheap, fast, non-noisy — use wherever the criterion is checkable without judgment. |
| **LLM-as-judge (~30%)** | A strong model scores outputs against rubrics (faithfulness, relevance, tone) — correlating with human judgment 80–85% | Cost ≈ $0.02–0.05/call; a 100-question suite ≈ $3 — "the cheapest insurance against a catastrophic prompt regression." **Mandatory calibration:** run the judge against human-scored examples first; if it disagrees >20% of the time, fix the judge prompt. Countermeasures: swap positions, multiple judges, diverse models. **Never rely on LLM-as-judge alone.** |
| **Human evaluation (~10%, but load-bearing)** | Judge calibration, final acceptance before major deploys, nuanced criteria (tone, empathy), 1–5% weekly random-sample audit of production | User feedback (thumbs) is sparse and expectation-biased; only deliberate human review establishes the reference standard. |

**The production-to-eval loop** (Corroborated): mine failed/low-rated production traces → add to the golden dataset → LLM-as-judge in CI on every PR. This is how evals stay representative of real traffic instead of fossilizing. For RAG: measure retrieval recall *separately* from generation faithfulness (RAGAS-style metrics), or you'll "fix" the wrong layer.

**Evals in CI** (Corroborated): run the golden suite on every prompt/model/retrieval/tool change; block deployment beyond threshold (practitioner norms: 5% tolerance on quality, zero tolerance on safety and format compliance; statistical significance for noisy evals, n>30). Shadow/canary: run new prompt versions on live traffic without returning results; compare behind a flag. **Benchmarks vs product evals:** public benchmarks (tau-bench, MCP-Universe) are for model/tool *selection*; vendor benchmarks (Fin Apex's 73.1%) are company-run — treat as *corroborating*, not *verified*, until independently reproduced. Always build the domain-specific benchmark for the actual task.

**Negative evidence about evals themselves** (Corroborated): judge bias (position, verbosity, self-preference) *creates* false confidence in uncalibrated judges; eval rot (datasets fossilize while traffic shifts); metric gaming (optimizing a vendor-defined "resolution rate" produces Goodhart failures — see Klarna).

## 7. Cost, latency, and reliability engineering

**Inference economics.** Every LLM call costs per token — input (the whole conversation history re-sent each turn) and output (usually priced higher). Costs compound because usage grows faster than per-token prices fall, history re-sends every turn, agent loops multiply calls, and long contexts inflate inputs (**Corroborated**). Agentic tasks consume roughly **1,000× the tokens of a standard query** (Corroborated). Andreessen Horowitz's widely-cited framing: AI inference is the single largest line item in the AI application stack past prototype.

**The cost-optimization stack, ordered by effort** (Corroborated on techniques; exact percentages **Inferred**, workload-dependent):

| Technique | Typical saving | Complexity |
|---|---|---|
| Prompt caching (prefix) | 60–90% on cached tokens | Low |
| Batch APIs | 50% flat (for anything tolerating delay) | Low |
| Output length control | 15–30% on output | Low |
| Model routing (small-first, escalate) | 40–70% on routed requests | Medium |
| Semantic caching | 31–47% fewer LLM calls | Medium |
| Context compression | 20–40% on input | Medium |
| Quantization (self-host) | 30–60% on compute | High |
| OSS models for narrow tasks | 70–95% on targeted workloads | High |

**The sequencing rule:** instrument first (cost attribution per team/feature is the prerequisite — you can't cut what you can't see), then caching, then routing, then model substitution. Every optimization risks quality — evaluate before/after each change; never trade correctness for cents blind. "The cheapest token of all is the one you never send — some features are better served by plain software than a model call."

**Latency** (Corroborated): users feel *time to first token* (TTFT) more than total time — streaming changes *perceived* latency, not cost. Tail latencies *add*: one LLM call's p95 of 2s → a three-step agent chain's p95 of 6–8s; track span hierarchies (per-call averages hide the session that fanned out into 40 calls). Practitioner norms: voice turn <800ms–1s; chat 2–4s (Fin Apex: 3.7s); RAG Q&A p99 <2s; recommender funnel 50–200ms total; agent multi-step task 10s–minutes with legible progress.

**The reliability stack** (Corroborated): (1) **deterministic first** — validate everything; never let unvalidated model output into a privileged operation; (2) **defined failure paths** — retry once with a repair instruction → fall back to a deterministic path → surface an honest error (and answer the extra question every LLM call needs: *what happens when it returns successfully but wrongly?*); (3) **fallback chains** — primary → smaller model → cached response → rule-based fallback → honest "unavailable"; (4) **timeouts, retries with backoff, circuit breakers** at the API-client layer; (5) **iteration caps** on every agent loop (the single most important agent reliability measure); (6) **idempotency and state rollbacks** for multi-step mutations. **Monitor four pillars simultaneously** (quality, performance, cost, reliability) per prompt/model version; alert norms: cost >2× baseline, p95 >3× p50, error rate >2%, format violations >0.5%, sudden content-policy spikes (possible attack). Weekly: manually review a 1–5% random sample of production outputs. Quarterly: red-team.

## 8. The agent security control catalog

**The threat landscape, current editions** (Corroborated): **OWASP Top 10 for LLM Applications 2026** (3 Aug 2026, supersedes the 2025 edition): LLM01 Prompt Injection · LLM02 Sensitive Information Disclosure · LLM03 Excessive Agency · LLM04 Supply Chain · LLM05 Data and Model Poisoning · LLM06 Unbounded Consumption · LLM07 Misinformation · LLM08 Hidden Context Exposure · LLM09 Vector and Embedding Weaknesses · LLM10 Improper Output Handling. **OWASP Top 10 for Agentic Applications (ASI) 2026**: ASI01 Agent Goal Hijack · ASI02 Tool Misuse & Exploitation · ASI03 Identity & Privilege Abuse · ASI04 Agentic Supply Chain · ASI05 Unexpected Code Execution · ASI06 Memory & Context Poisoning · ASI07 Insecure Inter-Agent Communication · ASI08 Cascading Failures · ASI09 Human-Agent Trust Exploitation · ASI10 Rogue Agents/Uncontrolled Autonomy. **OWASP MCP Top 10 (2025)**: tool poisoning codified as **MCP03:2025**, alongside rug pulls and tool shadowing.

**Foundational finding** (**Corroborated**, Greshake et al., 2023): processing untrusted retrieved data is *analogous to executing arbitrary code* — retrieval merges data and instructions into one undifferentiated channel; there is no parameterised prompt. The attacker never enters the session — they place text where the agent will read it. Economics worsen it: the attacker states only the *goal*; the model invents the *method*. **Prompt injection has no patch-style fix; mitigations are architectural.**

**MCP-era attack surface** (Corroborated): **tool poisoning** — malicious instructions inside tool `description` fields (loaded into context at session init); models cannot reliably distinguish operational intent from embedded instruction (MCPTox benchmark: most agents vulnerable; more capable models often *more* vulnerable — instruction-following is the exploit surface; Claude 3.7 Sonnet highest refusal rate at under 3%). **Rug pulls** — tool approved once, definitions silently changed later (fix: pin/hash `tools/list`, re-prompt on change). **Tool shadowing** — one server's description steers another's tools. **Confused deputy** — servers forwarding upstream tokens without audience validation; MCP spec mandates servers MUST NOT accept tokens not issued for them. **Supply chain** — malicious MCP packages on public registries (Sep 2025); CVE-2025-49596 (CVSS 9.4, RCE via unauthenticated MCP Inspector). **Credential aggregation** — one MCP server holding Slack+GitHub+Postgres+Salesforce creds = single-point breach.

**The control catalog** (Corroborated; per-control evidence in `research/security/04`):

| Control | Threat addressed | Notes |
|---|---|---|
| **Sandboxing** (hardware-enforced, zero-access where feasible) | ASI05 unexpected code execution | **Critical** when agents execute code; n/a for text-only agents. Mandatory for code interpreters per 2026 guidance. |
| **Tool allowlists + signed/pinned tool manifests** | ASI02 tool misuse, ASI04 supply chain, tool poisoning | Granular just-in-time permissions; pin/hash definitions; re-approve on change; treat tool descriptions and annotations (`readOnlyHint`) as untrusted. |
| **Permission boundaries / least-privilege identities** | ASI03 identity & privilege abuse, excessive agency | Unique, short-lived, per-task/per-tool scoped credentials; the agent never inherits the user's full credentials; no shared service accounts. One injection = the blast radius of the broadest credential. |
| **Human approval for consequential ops** | ASI09 trust exploitation, destructive actions | Mandatory for payments, deletion, external comms, prod deploys (the MCP spec's "SHOULD" is insufficient — "that word is doing too much work"). Approval UIs must show *full* tool info — truncation widens the human-model visibility gap. |
| **Secret isolation** | Credential theft via injection (LLM02, ASI01→exfil) | Secrets in a store the model cannot read; injected at tool-execution time, never into context; redacted from logs/traces. |
| **Output validation** | LLM05 improper output handling | Schema + allowlist + size validation on model output at every tool/DB/API boundary — treat model output as untrusted input to downstream systems. |
| **Audit logs** | All — detection & forensics | Log tool calls, approvals, permission grants, prompt/response pairs (redacted); MCP JSON-RPC traffic evades traditional SIEM patterns — plan reconstruction explicitly. |
| **Agent budgets & retry limits** | LLM06 unbounded consumption, ASI08 cascading failures | Token/cost/time budgets per task and per session with hard caps; retry caps; circuit breakers; transactional rollback; kill-switch. |
| **Untrusted-content handling** | Indirect injection, memory poisoning (ASI06) | All retrieved/external content is untrusted data, never instructions; delimit it in context; sanitize ingested data; integrity checks on persistent memory; memory isolation between agents/sessions. |
| **Runtime policy enforcement** | All | Policy engine at the tool-call boundary (pre-tool guards, per-tool blast-radius declarations); deny-by-default. |
| **Recovery / rollback** | ASI08 cascading failures | Backups, transactional semantics, kill-switches, defined safe failure modes. |
| **Inter-agent auth** (multi-agent only) | ASI07 insecure inter-agent communication | mTLS + message signing; no unauthenticated A2A delegation; consent verification. |

**How controls escalate with capability** (**Inferred** synthesis; each control's evidence above): text-only agent → D1 (untrusted-content handling), D7 (output validation), disclosure minimisation · + read tools → + read-scoped least-privilege identities, secret isolation, memory-poisoning defenses · + write/exec tools → full stack (sandboxing, allowlists, approvals, audit logs, budgets, rollback) — one compromised write-capable agent = the blast radius of its broadest credential · + payments/production infra → D5 mandatory (dual control), hard spend caps, immutable audit trail, incident runbook · multi-agent → + inter-agent auth, circuit breakers, quarantine of misbehaving agents.

**What doesn't work alone** (Corroborated): telling the model "don't follow instructions in documents" (probabilistic; EchoLeak bypassed Microsoft's XPIA classifier); input "sanitization" as the only layer; prompts as guardrails ("be careful with refunds" is probabilistic — production needs deterministic rules, hard limits, and human fallback triggers). Anthropic's own red-team conclusion is the doctrine in one line: *only environment boundaries hold*, not model-layer defenses.

**Reference architecture — the Polly harness** (**Corroborated**, self-reported with public methodology): a 9-layer harness around a support refund agent — instructions → RAG context → typed tools (8 MCP tools) → sandboxed execution → durable state → LangGraph orchestration with interrupt-before-execute approval gates → fraud sub-agent → injection/jailbreak/abuse gates → 8 judges + 229-case eval + Langfuse traces — plus a 10th loop: every verification failure becomes a structured incident feeding new prompts/skills/rules. Measured: 98.7% injection resistance, 100% jailbreak resistance on stable runs — with honest documentation of axes that *didn't* pass (policy correctness 60%, tool-decision safety 42% on stress cases). Engineering implication: "production-grade" is a measured threshold per axis, not an adjective — and the honest failure documentation is the signal of seriousness.

---

## Sources

`research/domain-b/07-tool-using-agents.md` (tool-use reliability, guardrail doctrine, MCP attack surface, Polly harness); `research/domain-b/08-evals.md` (eval methodology); `research/domain-b/09-cost-latency-reliability.md` (inference economics, latency, reliability stack); `research/domain-b/10-security-ops.md` (prompt-injection threat model, incident chronology, defense stack, LLMOps); `research/domain-b/02-rag.md` (retrieval architecture, Glean, Perplexity Photon); `research/security/04-ai-agent-security.md` (OWASP landscape, MCP attack research, control catalog, escalation ladder); `research/security/06-classification-index.md` (D1–D11 classifications with context sensitivity); `research/automation/01-automation-stack.md` (agent runtimes, tool execution, memory/state, observability, decision guide); `research/domain-a/` boundary notes (A-side agent guardrails).
