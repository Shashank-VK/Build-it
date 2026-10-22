# §27 — End-to-end Workflow Reconstructions

**The Omniscient Resource Atlas · product_engineering / automation · Built 2026-10-10**
**Read-only research only.** Discover, inspect, categorize, record sources. No building or recommending.

## Method note — VERIFIED vs PROPOSED

- **VERIFIED — <Company> (<source>)**: the company documents this as its own practice in official docs or its engineering blog. Every element below the tag comes from that source unless otherwise labeled.
- **PROPOSED**: the author's reference design — a synthesis of verified patterns into a complete workflow. Grounded elements cite their sources; the *assembly* is mine. Never presented as anyone's actual practice.

Each workflow carries the same ten-part anatomy: **triggers · inputs · decisions · tool calls · state changes · validation · outputs · failure handling · permissions · approvals**.

---

## W1. Idea → validated concept

**PROPOSED** reference design. Grounded in Amazon's Working Backwards PR/FAQ practice (**Corroborated** — described in *Working Backwards*, Bryar & Carr; PR/FAQ template and usage corroborated across multiple practitioner skill docs) and Linear-style triage states (**Corroborated** — practitioner best-practices doc citing linear.app/docs).

### Overview
A raw idea becomes a *validated concept*: a written, debated, explicitly-killed-or-funded proposition — before any build commitment. The workflow's product is a decision, not code.

### Anatomy

| Part | Detail |
|---|---|
| **Triggers** | Idea submitted (form, doc, meeting note); recurring discovery review (weekly/monthly); a production signal routed from W8 |
| **Inputs** | One-pager: opportunity, desired outcome (not deliverables), assumptions, unknowns, risks. For launch-shaped bets: PR/FAQ — a ≤1-page mock press release written *as if shipped* + FAQ answering the hardest customer and internal questions (pricing, scope, dependencies, metrics, rollback, security) |
| **Decisions** | D1: Is this a one-way-door (hard to reverse) or two-way-door decision? → chooses artifact weight (one-pager vs PR/FAQ vs six-pager). D2: FUND / KILL / REVISE after debate. D3: who owns it (single-threaded owner named — Amazon's operating mechanism, **Corroborated**) |
| **Tool calls** | Doc collaboration; customer-evidence lookup (interview notes, analytics, support tickets); lightweight LLM assistance *optional* for drafting — the thinking is the human's |
| **State changes** | `submitted → triaged → in-debate → funded | killed | parked`. Killed ideas stay recorded with rationale (prevents zombie revival) |
| **Validation** | The press-release test: *"if you can't write an exciting press release, the value proposition doesn't hold — go back and re-position"* (**Corroborated**, practitioner summary of Working Backwards). Pre-mortem: assume it failed, explain why. FAQ must include the questions the author wishes wouldn't be asked |
| **Outputs** | Decision record (FUND/KILL/REVISE + rationale + owner + kill criteria); funded concepts feed W2 |
| **Failure handling** | Vague PR/FAQ → REVISE, not FUND (Amazon teams reportedly iterate 10+ drafts — **Corroborated**, single practitioner source, treat as illustrative). Parked ideas get a revisit date or are archived; no silent limbo |
| **Permissions** | Anyone can submit; debate is open; the FUND decision sits with the named owner + stakeholders |
| **Approvals** | Human-only. No automation approves a bet. The workflow *prepares* the decision; a person makes it |

### Why this shape
Writing is the validation mechanism: *"Iterating on a press release is a lot less expensive than iterating on the product itself"* (**Corroborated**). The automation here is deliberately thin — templates, routing, records. Judgment stays human because the cost of a wrong FUND dwarfs the cost of slow triage.

---

## W2. Concept → specification

**PROPOSED** reference design. Grounded in Amazon's narrative-memo/six-pager shape (**Corroborated** — context → customer/problem → proposal → mechanism → metrics → risks → appendix) and RFC-style public review norms (**Inferred** as standard practice; IETF process not re-verified this pass).

### Overview
A funded concept becomes a *buildable specification*: scope, behavior, interfaces, acceptance criteria, and explicit non-goals — reviewed until the team agrees on what "done" means.

### Anatomy

| Part | Detail |
|---|---|
| **Triggers** | FUND decision from W1; or a defect trend from W8 that needs design (not just a patch) |
| **Inputs** | The concept record + kill criteria; existing system docs/architecture; constraints (compliance, platform limits, budgets) |
| **Decisions** | D1: build vs buy vs don't (revisit). D2: scope cuts — what is explicitly *out*. D3: interface contracts (API shapes, data schemas, event names) frozen before build. D4: acceptance criteria — the tests that will prove it in W4 |
| **Tool calls** | Spec template (narrative sections, not bullet decks — Amazon's "narratives over slides," **Corroborated**); API design linting; dependency/security review of new components; optional LLM drafting with human authorship of decisions |
| **State changes** | `drafting → in-review → approved | revise`. Review comments are first-class state, not hallway chat |
| **Validation** | Review by engineering + design + affected stakeholders; every open question resolved or explicitly deferred with an owner; acceptance criteria traceable to the concept's kill criteria |
| **Outputs** | Approved spec (versioned, immutable once approved — changes go through revision); work items for W3/W4; test plan skeleton |
| **Failure handling** | Spec churn after approval → formal revision, never silent edits; unresolved interface disputes escalate to the owner (W1's single-threaded owner persists) |
| **Permissions** | Spec repo: write access for the owning team; comment access for stakeholders; approval rights for tech lead + product owner |
| **Approvals** | Human sign-off required (tech lead + product). For high-risk surfaces (payments, identity, data export): security review as a required check |

---

## W3. Specification → prototype

**PROPOSED** reference design. Grounded in the evaluator-optimizer pattern and human-in-the-loop interrupts (**Corroborated** — Anthropic patterns; LangGraph interrupt mechanics).

### Overview
A spec becomes a *throwaway-or-evolvable prototype* that proves the riskiest assumption — the demo that answers "can this work at all?" rather than "is this shippable?"

### Anatomy

| Part | Detail |
|---|---|
| **Triggers** | Approved spec (W2); time-boxed spike request ("we don't know if X is feasible") |
| **Inputs** | Spec; riskiest-assumption statement (the one thing the prototype must prove); time box (days, not weeks); throwaway-vs-evolvable flag |
| **Decisions** | D1: what is *not* built (auth, scale, polish — named explicitly). D2: throwaway (learn and discard) vs evolvable (will harden in W4). D3: which assumption gets the demo |
| **Tool calls** | Scaffolding generators; a coding agent in a sandbox (human reviews output); notebook/scratch environments; feature flags to hide the prototype from users |
| **State changes** | `spiking → demo-ready → accepted | rejected`. Demo is a checkpoint, not a merge |
| **Validation** | Demo against the riskiest assumption *only*; explicit list of what was faked; if evolvable, a hardening backlog is filed before acceptance |
| **Outputs** | Working prototype behind a flag; learnings doc (what broke, what surprised); go/no-go for W4; hardening backlog if evolvable |
| **Failure handling** | Assumption disproved → back to W2 (revise spec) or W1 (kill concept) — a *successful* prototype workflow includes kills. Time box expires → demo what exists, decide, don't extend silently |
| **Permissions** | Prototype lives in a scratch repo/branch; cannot touch production data or production infrastructure |
| **Approvals** | Human demo review. If an agent built it: human reviews the diff before it leaves the sandbox (mirrors the Copilot coding-agent rule — no merge on an AI's word alone) |

---

## W4. Prototype → production implementation

**PROPOSED** reference design. Grounded in CI gates, evaluator-optimizer loops, and progressive delivery (**Corroborated** for CI mechanics via GitHub Docs; progressive rollout **Inferred** as standard practice).

### Overview
The validated approach becomes production code: hardened, tested, observed, and rolled out gradually — with the prototype's shortcuts explicitly paid down.

### Anatomy

| Part | Detail |
|---|---|
| **Triggers** | Accepted prototype (W3); hardening backlog complete enough to start |
| **Inputs** | Prototype + learnings doc + hardening backlog; production standards (testing, observability, security baselines); rollout plan |
| **Decisions** | D1: strangler vs rewrite vs new-service (how the new code meets the old). D2: rollout shape (flag → 1% → 10% → 100%, or blue/green). D3: rollback trigger thresholds defined *before* rollout |
| **Tool calls** | Issue tracker → branches → PRs (W5 per task); CI (lint, typecheck, unit/integration tests); load tests for hot paths; migration tooling; feature-flag service; dashboards/alerts wired *before* traffic |
| **State changes** | `hardening → in-review → merged → flag-off → rolling-out → fully-live`. Each stage is a gate, not a notification |
| **Validation** | Required status checks per PR; hardening backlog items closed or explicitly deferred; dashboards show the new path healthy at each rollout step; rollback drill (can we actually roll back?) |
| **Outputs** | Production code behind flags; runbooks; dashboards + alerts; rollout record; prototype retired or deleted |
| **Failure handling** | Rollout metric breaches threshold → automatic halt + rollback to last good state (flag flip, not a redeploy); flaky tests quarantine, never silently skipped; a failed rollout routes to W6 (defect) with the rollout context attached |
| **Permissions** | Merge rights per branch protection; flag-flip rights restricted to owning team; production data access only via audited paths |
| **Approvals** | Human code review per PR; human approval to begin rollout and to pass each rollout stage (can be encoded as GitHub environment required reviewers — **Verified** mechanics, W7) |

---

## W5. Task → verified pull request

**VERIFIED — GitHub (GitHub Docs: Copilot coding agent overview; Dependabot version/security update docs; InfoWorld reporting GitHub CEO's launch announcement, 2025-05-19).** Two documented company workflows are reconstructed: (a) the Copilot coding agent, (b) Dependabot.

### (a) Copilot coding agent — issue to PR

| Part | Detail (**Verified** unless noted) |
|---|---|
| **Triggers** | A GitHub issue is *assigned to Copilot*; or a developer asks in Copilot Chat to create a PR; or (via Jira integration) a Jira automation fires |
| **Inputs** | The issue description / chat prompt as the task spec; repo's `.github/copilot-instructions.md` as standing rules; the repository itself |
| **Decisions** | Agent evaluates the task from the prompt, plans the change set, and works like a human developer would |
| **Tool calls** | Ephemeral development environment **powered by GitHub Actions**: explores code, edits, runs automated tests and linters |
| **State changes** | `issue assigned → draft PR opened (tracks progress) → branch commits pushed → ready for review → review requested from the human` |
| **Validation** | Existing repo policies apply unchanged: **branch protections still apply; the agent's PRs require human approval before CI/CD workflows run**; required status checks gate merge |
| **Outputs** | Pull request with description of the change; session logs viewable via "View session"; the human can leave PR comments asking the agent to iterate |
| **Failure handling** | Agent's limits: excels at low-to-medium complexity tasks in well-tested codebases (GitHub's own scoping); iteration happens through PR review comments; session logs expose what it did |
| **Permissions** | Requires a paid Copilot plan; agent enabled per repository by admin policy; the agent works within the repo's permission model |
| **Approvals** | **Human review is mandatory** — the agent requests review on completion and *never merges on its own* (**Corroborated**: third-party comparison notes "it never merges") |

### (b) Dependabot — scheduled scan to PR

| Part | Detail (**Verified**, GitHub Docs) |
|---|---|
| **Triggers** | Schedule (`daily`/`weekly`/`monthly` per `dependabot.yml`); immediate scan when the config file changes; security advisories for the ecosystem |
| **Inputs** | `.github/dependabot.yml` (ecosystems, directories, schedules, labels, reviewers, ignore rules, open-PR limits); manifest/lockfile contents; semver metadata from registries |
| **Decisions** | Deterministic: compare manifest versions against registry semver → decide whether an update is warranted; group updates per configuration (grouped security updates never mix ecosystems, and never mix security with version updates) |
| **Tool calls** | Manifest parsing; registry lookups; PR creation with changelog/release-note summaries; commits are signed by Dependabot by default |
| **State changes** | `scan → update available → PR opened (max 5 open by default; configurable via open-pull-requests-limit) → CI runs → human merges or closes` |
| **Validation** | Dependabot PRs **trigger the repo's normal CI workflows** (GitHub Actions runs on them like any PR); branch protection and required checks apply |
| **Outputs** | One PR per dependency (or per group); version-bump diff; compatibility metadata |
| **Failure handling** | PR limits prevent floods (first 5, rest after merges); failed CI is visible on the PR like any other; grouped updates reduce PR volume |
| **Permissions** | Runs as the Dependabot app identity; configured entirely through the checked-in `dependabot.yml` — the config *is* the permission |
| **Approvals** | Human merge (unless the repo configures auto-merge — **Inferred** as a common extension, not in the verified docs excerpt) |

### Cross-note
Both workflows share the load-bearing property: **the automation proposes; humans and CI dispose.** The PR — with its checks, reviews, and protections — is the trust boundary, not the agent.

---

## W6. Defect report → validated fix

**VERIFIED — Sentry (Sentry Docs: Seer / Autofix, docs.sentry.io).** Second verified instance: **GitHub — Dependabot security updates** (GitHub Docs).

### Sentry Seer Autofix — production error to PR

| Part | Detail (**Verified**, Sentry Docs) |
|---|---|
| **Triggers** | Manual: "Autofix" from the Issue Details page. Automatic (if enabled): issues meeting criteria — including **10 or more events** (Sentry waits to ensure the issue is worth investigating) |
| **Inputs** | Sentry context (issue details, tracing data, logs, profiles); connected codebases (GitHub/GitLab integration required); natural-language guidance from the engineer |
| **Decisions** | D1: root-cause analysis judges whether the issue is auto-fixable. D2: solution identification. D3: generate code directly vs **hand off to an external coding agent** (supported: Claude Code, Cursor Cloud Agents, GitHub Copilot) |
| **Tool calls** | Seer's internal tools over Sentry telemetry; repo access via the Seer GitHub/GitLab app; code generation; optional external coding-agent handoff at the final step |
| **State changes** | `root cause analysis → solution identification → code generation (+ optional PR) → PR iteration`. Seer's documented model is a **new branch / draft PR — never writing to main or merging without review** (**Corroborated**, practitioner research citing Sentry docs) |
| **Validation** | **PR iteration step refines the PR using CI failures and engineer feedback**; the fix is validated against the repo's CI like any PR |
| **Outputs** | Root-cause write-up on the issue; proposed code fix; optionally an opened PR; or a handoff package for an external coding agent |
| **Failure handling** | Low actionability → analysis only, no code; CI failures feed back into iteration; engineer can add context in natural language at any step |
| **Permissions** | Requires the Seer GitHub/GitLab app installed; repo selection in Seer SCM settings; project↔repo mapping in Seer project settings; PR creation is opt-in |
| **Approvals** | **Merging remains a human decision**; configurable stopping points cap automation at scan / diagnose / draft / handoff (**Corroborated**, practitioner FAQ citing Sentry) |

**Security caveat — VERIFIED pattern, Corroborated incident:** a CERT advisory described an attack chain in which attacker-submitted exception events flowed through Seer's analysis into a coding agent's prompt, and the agent **downloaded and executed an attacker-controlled package before any human reviewed a PR** (**Corroborated**, practitioner report citing CERT, 2026). Implication: defect-intake pipelines must treat incoming reports as *untrusted input* (OWASP LLM01/LLM05) — sandbox the agent, pin dependencies, and never let pre-review execution touch secrets or production.

### Dependabot security updates — advisory to PR (second verified instance)

Trigger: a new advisory in the GitHub Advisory Database matching the dependency graph → Dependabot opens a PR bumping to the minimum patched version (also covers vulnerable GitHub Actions in workflows). Grouped security updates batch per ecosystem. Validation/approvals/permissions: identical to W5(b) — normal CI, branch protections, human merge. **Verified** (GitHub Docs).

---

## W7. Pull request → deployment

**VERIFIED — GitHub (GitHub Docs: "Deployments and environments," GitHub Actions).**

| Part | Detail (**Verified** unless noted) |
|---|---|
| **Triggers** | PR merged to a deployable branch (commonly `main`); tag pushed (`v*`); manual dispatch |
| **Inputs** | The merged commit SHA; the workflow file (`.github/workflows/*.yml`); environment configuration (Settings → Environments) |
| **Decisions** | D1: which environment (`dev`/`staging`/`production`) the job targets — declared in YAML via `environment:`. D2: whether protection rules pass. D3: human approve/reject at each gate |
| **Tool calls** | Build, test, artifact publish, and deploy steps on runners; OIDC-minted cloud credentials scoped to the environment |
| **State changes** | `merged → build → deploy-dev (auto) → deploy-staging (gate) → deploy-production (gate) → live`. A job referencing an environment **must satisfy that environment's protection rules before it runs or can access its secrets** |
| **Validation** | Required status checks and branch protections on the PR *before* merge (**Corroborated**, practitioner study guides quoting docs); deployment branch rules (e.g. only `main`/`v*` may reach production); optional custom protection rules via GitHub Apps (max 6 per environment) — observability, change-management, or code-quality systems can gate a deploy |
| **Outputs** | Deployment record; environment URL; audit trail of who approved what |
| **Failure handling** | Rejected approval → run stops, no secrets exposed. Wait timer (1 min–30 days, non-billable) gives a cancellation window for mistaken triggers. Failed deploy → previous revision stays live; rollback is a new deployment, not an undo |
| **Permissions** | **Environment-scoped secrets/variables are visible only to jobs referencing that environment**; reviewers need ≥ read access; OIDC trust policies can require `environment: production` in token claims so even a bypassed gate can't mint production credentials (**Corroborated**, practitioner implementation) |
| **Approvals** | **Required reviewers**: up to 6 people/teams, only one approval needed to proceed; optional **prevent self-review** — whoever triggered the deploy cannot approve it. This is the human-approval mechanism of §26 Part B(10), implemented as platform policy rather than agent prompt |

### Standard promotion shape (**Corroborated**, practitioner repos)
`dev`: auto, all branches, no reviewers → `staging`: 1 reviewer, `main` only → `production`: 2 reviewers + wait timer + version tags only. The YAML *declares* the environment; the *protection lives in repo settings* — a separation worth preserving (declarative intent vs enforced policy).

---

## W8. Production signals → new improvements

**PROPOSED** reference design. Grounded elements: Sentry's issue model (**Verified** — events grouped into issues with actionability scoring); error-budget thinking (**Corroborated** — Google SRE workbook, published); auto-triage rules (**Corroborated** — Sentry documents "archive recurring issues with no events in 30 days" as a Seer capability).

### Overview
Telemetry becomes backlog: signals (errors, latency, saturation, user reports) are triaged into either *fixes* (route to W6) or *improvements* (route to W1/W2) — with explicit anti-noise defenses, because the failure mode of this workflow is alert fatigue, not missed signals.

### Anatomy

| Part | Detail |
|---|---|
| **Triggers** | Error-rate / latency / saturation alerts; new Sentry issues crossing actionability thresholds; user-reported incidents; periodic review (weekly signal triage) |
| **Inputs** | The signal (alert payload, issue link, dashboard); error-budget state (how much unreliability is "spent"); recent deploy history (what changed?) |
| **Decisions** | D1: real user impact or noise? D2: fix (→ W6) vs improve (→ W1/W2) vs accept/monitor. D3: priority — P0 (page now) through P3 (backlog). D4: does this burn error budget faster than policy allows? If yes, feature work pauses until reliability recovers (the SRE bargain, **Corroborated** as published practice) |
| **Tool calls** | Alerting/monitoring; issue tracker (Sentry → Linear/GitHub issue with context attached); on-call paging; dashboards; optional Seer-style investigation (W6) for the diagnostic half |
| **State changes** | `firing → triaged → accepted-as-defect | accepted-as-improvement | archived-as-noise`. Archived signals keep their evidence (reopen if they recur) |
| **Validation** | Every accepted item has a reproduction or a metric to move; noise verdicts require a reason (flaky probe, known third-party blip); weekly review audits the triage queue age |
| **Outputs** | Defect tickets (→ W6) with frozen evidence packets; improvement proposals (→ W1) with the signal as customer evidence; updated runbooks; error-budget accounting |
| **Failure handling** | Alert fatigue: auto-archive rules for recurring no-event issues; alert thresholds tuned from false-positive history; paging storms → incident commander declared, mitigation before diagnosis. Duplicate signals dedupe on issue identity (W6's evidence-packet pattern) |
| **Permissions** | Anyone can file a signal; triage rights with the on-call + owning team; paging policy per severity |
| **Approvals** | Human triage — no auto-filing of P0s without a human in the loop; error-budget policy exceptions need tech-lead sign-off |

### The loop this closes
W8 is the flywheel: production teaches, the backlog learns. Its discipline is *selective* automation — auto-collect and auto-group signals, but keep the *judgment* (real? whose? how urgent?) human, because mis-triaged automation either pages people at 3am or silently archives real outages.

---

## W9. Parallel agents collaborating on isolated tasks

**VERIFIED — Anthropic ("How we built our multi-agent research system," anthropic.com engineering blog).** Guardrails from **VERIFIED — Cognition ("Don't Build Multi-Agents" + 2026 follow-up "Multi-Agents: What's Actually Working," cognition.ai/cognition.com).**

### What Anthropic actually built (their words, paraphrased)
An **orchestrator-worker** system behind the Research feature: a lead agent analyzes the query, develops a strategy, and spawns subagents that **search for information simultaneously**, each in its **own context window**; the lead synthesizes; a separate **CitationAgent** attributes claims. The lead **saves its plan to memory** because long sessions exceed context limits.

### Anatomy

| Part | Detail (**Verified** from Anthropic unless noted) |
|---|---|
| **Triggers** | A user query needing breadth-first investigation (many independent directions, information exceeding one context window) |
| **Inputs** | The query; the lead agent's strategy; available tools (search, integrations, MCP servers) |
| **Decisions** | D1 (lead): decompose into subagent briefs — each brief carries **objective + output format + tool/source guidance + clear task boundaries** (vague briefs caused duplicated work and gaps in early versions). D2 (lead): how many subagents — **effort scaled to query complexity**: simple fact-finding = 1 agent with 3–10 tool calls; comparisons = 2–4 subagents × 10–15 calls; complex research = 10+ subagents with divided responsibilities. D3 (lead): synthesize now or spawn another round |
| **Tool calls** | Subagents iteratively use search tools with **interleaved thinking** (evaluate tool results, identify gaps, refine queries); lead uses **parallel tool calling** (3–5 subagents at once; 3+ parallel tools per subagent) — this cut research time up to **90%** for complex queries |
| **State changes** | `query → plan (persisted to memory) → subagent batch N running → findings returned → synthesize → more research? → citations → done`. The lead **waits for each batch synchronously** — Anthropic calls this a bottleneck they ship anyway because it simplifies coordination (**Corroborated**) |
| **Validation** | Outcome-based evals (agents may take different valid paths — step-matching doesn't work); **start evaluating immediately with small samples** (early prompt tweaks moved success 30%→80%); heuristics over rigid rules; guardrails against spiraling (explicit anti-runaway rules in prompts) |
| **Outputs** | Synthesized research report with citations placed by the CitationAgent |
| **Failure handling** | Observed early failures: **50 subagents spawned for simple queries**; endless scouring for nonexistent sources; subagents distracting each other with excessive updates — all fixed primarily through **prompt engineering** (the highest-leverage lever) and effort-scaling rules. Infrastructure retries + checkpointing so failures *resume rather than restart* (**Corroborated**) |
| **Permissions** | Subagents get distinct tools/prompts per concern (separation of concerns reduces path dependency); tool access scoped to the investigation |
| **Approvals** | None mid-run in the Research product (read-only work); the *economic* approval is the task-value test: multi-agent burns ~**15× the tokens of chat** (~4× for single agents) — *"for economic viability, multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance"* |

### Measured results (**Verified**, Anthropic's internal evals — vendor-published, no independent replication found)
- Opus 4 lead + Sonnet 4 subagents **outperformed single-agent Opus 4 by 90.2%** on the internal research eval (breadth-first queries especially).
- Token usage alone explained **80%** of performance variance on BrowseComp (three factors — tokens, tool calls, model choice — explained 95%).
- Anthropic's own caveat: this shape fits tasks with heavy parallelization and information exceeding single context windows; **"most coding tasks involve fewer truly parallelizable tasks than research."**

### Cognition's guardrails on this workflow (**Verified**, cognition.ai)
Apply W9 only where these hold: (1) **share context** — subagents need full traces, not just messages, or they misread subtasks (the Flappy Bird case: one subagent built a Mario-style background, another an incompatible bird); (2) **actions carry implicit decisions** — parallel *writers* make conflicting assumptions no composer can reconcile. Cognition's converged rule (2026 follow-up): use multi-agent only where *"multiple agents contribute intelligence to a task while writes stay single-threaded."* Claude Code's embodiment of this: subagents answer questions, they don't write code in parallel with the parent.

---

## Cross-workflow notes

1. **The PR is the universal trust boundary.** W5, W6, and W4 all terminate at a pull request with CI + human review. Automation proposes; the PR disposes. (Verified across GitHub and Sentry docs.)
2. **Kill paths are first-class.** W1 kills concepts, W3 kills on disproved assumptions, W6 declines low-actionability issues, W8 archives noise. A workflow without an explicit "no" just accumulates.
3. **Human approvals cluster at irreversibility.** Money, production, merges, pages — every workflow puts the person at the step that can't be undone, and automation everywhere else. (Verified: GitHub environments, Sentry merge policy, LangGraph interrupts.)
4. **Evidence packets, not screenshots.** W6 and W8 freeze structured evidence (IDs, event counts, deploy links, suspected commits) at triage time — because production state keeps moving after the signal fires. (Corroborated practitioner pattern.)
5. **Cost is a design input.** W9's 15× token cost and W5's per-run compute are budgeted like infrastructure, with caps and kill-switches. (Verified Anthropic; Corroborated incident analysis.)
