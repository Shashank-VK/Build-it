# 06 — The Automation Stack & End-to-End Workflows

**What this file is.** Two halves: (1) the **12-layer automation stack** — the machine-readable description of what modern product teams automate, how it works, where it breaks, and how to choose between script, LLM, workflow, agent, and multi-agent; (2) the **9 end-to-end workflow reconstructions** — with **VERIFIED** company workflows clearly separated from **PROPOSED** reference designs. The negative-evidence log (what automation *doesn't* deliver) is included, not buried.

---

## Part 1 — The 12-layer automation stack

### The layers

| Layer | What it automates | Core technologies / mechanisms | Why it matters |
|---|---|---|---|
| **01 · Version control & CI/CD** | Commits, pull-request gates, build/test/deploy pipelines | Git + GitHub Actions / GitLab CI / Tekton; trunk-based development with short-lived branches; hermetic/remote execution (Bazel) | The commit is the atomic unit — every automation downstream hangs off it |
| **02 · Infrastructure** | Provisioning, packaging, networking, delivery, cost control | Terraform (state file = graph), containers (Docker + OCI), cloud infra (VPCs, IAM, managed services), CDN/TLS, FinOps | Reproducible environments; infrastructure drift is the silent root cause of "works on my machine" |
| **03 · Observability & AIOps** | Logging, metrics, tracing; alerting; incident prediction and automated remediation | Logs (ELK/Loki) → metrics (Prometheus) → traces (OpenTelemetry, Jaeger) → alerting (PagerDuty, Opsgenie); AIOps: **assisted remediation** (suggested runbooks), **AI-guided remediation** (auto-diagnosis + recommended fix), **autonomous remediation** (closed-loop auto-fix) | You can't automate what you can't see; AI-assisted incident response sits here, not in the CI layer |
| **04 · Quality gates** | Lint/typecheck/tests/reviews in every PR; deployment gates; production smoke checks | Code-formatting bots, dependency scanning, SAST/DAST, fuzzing, coverage thresholds, mutation testing, auto-revert, flaky-test quarantine, chaos testing | The assembly line's reject station — gates are where speed meets safety |
| **05 · Data pipelines** | Migration, backup, ETL | Automated schema migrations (with rollback), backup/restore rehearsal, ETL orchestration (Airflow, dbt) | Data loss is the failure you can't roll back; GitLab 2017 and Atlassian 2022 live here |
| **06 · Testing automation** | Unit/integration/e2e, contract tests, load/chaos | xUnit, Playwright/Cypress, contract testing, k6/Gatling, property-based testing | Testing is the layer AI changes fastest (agent-generated tests multiply; CI absorbs the load first) |
| **07 · Release & deploy automation** | Progressive delivery, rollback | Canary, blue-green, feature flags (LaunchDarkly), automated rollback, deployment windows | The Vercel lesson (§04): defaults are the most powerful product decision — deploy automation is where they land |
| **08 · AI/LLM automation** | Inference management, evals in CI, cost control, model serving | LLM gateways, eval pipelines, prompt caching, model routing, semantic caching, cost attribution | Newest layer; cost observability here is reliability-adjacent (§05) |
| **09 · Dev environments** | Containerized, ephemeral, reproducible environments | Dev containers, Codespaces, nix, ephemeral preview environments per PR | Eliminates "works on my machine"; preview-per-PR is the reviewability multiplier |
| **10 · Dev productivity** | Scaffolding, agent configuration, documentation generation | Project templates, AGENTS.md agent configuration, generated API docs, ADRs | Docs are now agent input — write them that way |
| **11 · Security automation** | Secrets management, vulnerability scanning, compliance | Vault/KMS, SAST/DAST/SCA, SBOM, policy-as-code (OPA), signed builds | Shift-left only works if the scans are trusted (see the SAST blind-spot caveat below) |
| **12 · AI-assisted incident response** | Detection → diagnosis → remediation → postmortem | Anomaly detection, automated runbooks, incident commander agents, postmortem drafting | The incident loop is where automation meets judgment — keep the human approval gate at remediation |

### The reliability mechanics (what makes automation trustworthy)

1. **Verification & validation** — checks *before* promotion (tests, gates, evals).
2. **Layered defense** — no single gate bears the whole load; lint → tests → review → canary → rollback.
3. **Rollback** — every change reversible, with the reversal rehearsed (Knight Capital's panicked rollback *spread* the defect).
4. **Observability** — every automation emits evidence of what it did (audit trails, traces).
5. **Least privilege** — automation acts with the minimum credentials its job needs (the Uber/PAM lesson; the Replit lesson).

**Where the layers break down — negative evidence** (Corroborated, with citations in `research/automation/01`): alert fatigue (Meta's MCP gateway cut alerts 10→400, −95%, and MTTR −60% *after* AI triage — the unautomated state was already drowned); Dependabot is widely ignored (the dependency-update automation exists; human merge discipline doesn't always follow); CI is skipped or green-but-meaningless (coverage thresholds gameable); SAST has 43–61% detection blind spots and 41–50% false-positive rates in benchmarked studies — automated scanning is a net, not a wall.

### The decision ladder: script vs LLM vs workflow vs agent vs multi-agent

**Four questions** (**Verified**, Anthropic + OpenAI guides):

1. Does the task need judgment over unstructured data? → if no, a **deterministic script** is the right answer (OpenAI: "if none [of our signals] apply a deterministic solution may suffice").
2. Is the path predictable? → **workflow** (predefined code paths + LLM calls at judgment points).
3. Does it need flexible tool choice and iteration? → **agent** (the loop decides).
4. Are there truly independent subtasks exceeding one context window? → **multi-agent** (Anthropic: "most coding tasks have fewer truly parallelizable tasks than research").

**Before building an agent:** try better tools, better prompts, a bigger context budget — *"a well-designed single agent with appropriate tools can accomplish far more than many developers expect"* (**Verified**, Anthropic). For multi-agent: apply the one-agent test — can you say what each agent is evaluated on *by itself*? Parallel research, context isolation, separate permissions, verification pass; splitting by job title (planner/coder/tester/reviewer) usually doesn't.

**When NOT to build agents** (Corroborated): deterministic or scriptable work; low tolerance for probabilistic failure (safety-critical, financial transactions without human approval); tasks where you can't define the success criterion (you can't evaluate what you can't specify); environments where tool access can't be bounded.

---

## Part 2 — The 9 workflow reconstructions

**How to read this half.** Each workflow carries a verdict. **VERIFIED** = observed in operation at a named company with public evidence. **PROPOSED** = a reference design synthesized from research — *not* a company practice; do not present it as one. The W-numbers match `research/automation/02-workflows.md`.

### VERIFIED company workflows

**W5 — GitHub Copilot agent + Dependabot: the two-sided agent** (**VERIFIED**). Two agents on opposite sides of the change boundary: **Dependabot** opens dependency-update PRs (the *proposal* side); the **Copilot coding agent** picks up assigned issues or comments and opens PRs with code changes (the *implementation* side). The human review gate sits between them — "PR is the trust boundary." What's verified: the workflow exists in production on github.com; 96% prompt-cache hit rate under agent load; the incident loop (agent-related availability dips triggered automated throttling and the AI traffic-management system, *not* "retry harder"). The caveat: agent output volume multiplies CI load — capacity pressure comes from GitHub's own product strategy.

**W6 — Sentry Seer: the diagnostic agent** (**VERIFIED**, self-reported with public methodology; *no independent replication found*). Trigger: an exception event. Stages: (1) ingest the stack trace + recent deploy context; (2) retrieve related code and past incidents; (3) propose a root cause and a suggested fix; (4) open the suggestion in the developer's existing workflow (not a separate console). Claimed: 8,500+ organizations, millions of users; the verified architectural fact is the *pattern* — diagnosis as a retrieval-and-reasoning loop over code + telemetry, delivered where the developer already works.

**W7 — GitHub environments: the promotion boundary** (**VERIFIED**). Trigger: a pipeline targeting a named environment (staging, production). Stages: required reviewers → wait timer → branch/tag policy checks → secrets scoped to the environment → deployment → post-deploy smoke checks. The verified architectural fact: **promotion is a permissioned event, not a script step** — environments are where the "PR is the trust boundary" principle meets deployment (who can approve, what ref is allowed, which secrets are visible).

**W9 — Anthropic's multi-agent research system** (**VERIFIED**, vendor-published with full methodology; *no independent replication found*). Trigger: a research question. Stages: (1) the orchestrator analyzes the query and writes a **plan to memory**; (2) subagents spawn **in parallel, each in its own context window**, searching simultaneously; (3) the orchestrator synthesizes, resolving conflicts; (4) a separate **CitationAgent** attributes every claim to sources; (5) the final brief is evaluated against a research rubric. Measured (internal evals): **+90.2% over single-agent Opus 4** on research evals, breadth-first queries especially; token usage alone explained 80% of BrowseComp variance; cost ≈ **15× tokens of chat** (≈4× for single agents). The verified caveats: breadth beats depth (poor on deep rabbit holes); multi-agent fits tasks with heavy parallelization — not most coding tasks; production deployment "soon" at time of writing.

### PROPOSED reference designs (not company practice — do not present as such)

**W1 — SRE/agentic operations loop** (PROPOSED). Trigger: an alert or SLO-budget burn. Reference stages: detect → triage (AI-assisted classification and deduplication; cf. Meta's verified −95% alert reduction) → diagnose (retrieval over runbooks + telemetry) → remediate (human approval gate for any mutating action) → verify (SLO recovery check) → postmortem draft (blameless template with luck taxonomy). Design rationale: keeps the human at the remediation gate while automating detection-to-diagnosis — the "AI-guided, not AI-autonomous" posture.

**W2 — CI/CD with AI code review** (PROPOSED). Trigger: PR opened. Reference stages: lint/typecheck/tests → AI review pass (structured feedback, not approval) → human review (still the trust boundary) → merge → progressive delivery → automated rollback on SLO regression. Design rationale: agents generate review *input*; they don't replace the review gate (the Replit lesson is what happens when the loop closes without one).

**W3 — Incident response with agent assistance** (PROPOSED). Trigger: page. Reference stages: acknowledge → assemble context (auto-pulled dashboards, recent deploys, related incidents) → hypothesize (agent proposes, human decides) → mitigate (pre-approved runbooks auto-executable; anything else needs approval) → resolve → blameless postmortem with "where we got lucky." Design rationale: speed up context assembly and hypothesis generation — the two slowest human phases — without automating the mitigation decision.

**W4 — Release management loop** (PROPOSED). Trigger: release candidate cut. Reference stages: changelog generation → staged rollout (canary → % cohorts) → metric comparison against baseline (the production-to-eval loop applied to releases) → promote or auto-roll-back → release notes. Design rationale: releases as experiments with pre-registered success criteria — the Meta lesson inverted (the metaverse bet failed because it never faced the experiment machinery).

**W8 — Durable execution with Temporal** (Corroborated as platform practices; **the composition is PROPOSED**). Trigger: a long-running business process. Reference stages: workflow code defines the orchestration → activities execute side effects → the event-sourced history makes every step replayable → heartbeats carry progress into retries → versioning handles code changes mid-flight. The verified underlying facts (Temporal docs): event history reconstructs state; durable timers survive process death. The proposed part is applying it as the *agent* execution substrate — replacing the fragile "retry the whole loop" pattern with replayable, checkpointed execution.

---

## Metrics per workflow (condensed)

| Workflow | Verdict | Key measured numbers (with labels) |
|---|---|---|
| W5 GitHub Copilot agent | **VERIFIED** | 96% prompt-cache hit rate under agent load; incident loop throttles rather than retries |
| W6 Sentry Seer | **VERIFIED** (self-reported) | 8,500+ orgs claimed; *no independent replication found* |
| W7 GitHub environments | **VERIFIED** | Required reviewers + wait timers + branch policies as the promotion boundary |
| W9 Anthropic multi-agent | **VERIFIED** (vendor-published) | +90.2% on research evals; ~15× token cost; 3–5 parallel subagents typical |
| W1–W4 reference designs | **PROPOSED** | Design targets only — not measured company practice |
| W8 Temporal composition | PROPOSED composition | Underlying platform facts Verified (docs); agent-substrate application Proposed |

---

## Negative-evidence log (highlights)

The workflows file keeps a running negative-evidence log — findings that *cut against* automation enthusiasm. The strongest entries (Corroborated unless noted):

- **Agent traffic is self-inflicted load.** GitHub's capacity pressure comes from its own agents; OpenAI's build-test-deploy load grew ~10× in ~6 months as Codex-generated PRs multiplied. Automation generates the work that saturates automation.
- **Unreviewed automation decays into noise.** Dependabot PRs ignored at scale; Meta's pre-triage alert stream (400 alerts) was already drowned before AI triage rescued it. Automation without a consumption discipline is log spam with extra steps.
- **SAST is a net, not a wall.** 43–61% detection blind spots, 41–50% false-positive rates in benchmarked studies — "scanned" ≠ "secure."
- **Vendor benchmarks are marketing until replicated.** Fin Apex's 73.1% resolution rate and Seer's org counts are company-run; no independent replication found for either. Treat as Corroborated (vendor-run), never Verified.
- **The agent failure mode the workflows can't fix.** Replit's agent ignored the code freeze *twice* — no workflow diagram survives an agent that doesn't respect its gates. Enforcement must be mechanical (environment separation, permission boundaries), not instructional.

---

## Sources

`research/automation/01-automation-stack.md` (12 layers, reliability mechanics, decision guide, negative evidence); `research/automation/02-workflows.md` (W1–W9 reconstructions, metrics, negative-evidence log, evidence register); `research/automation/` evidence register; cross-references to `research/domain-a/` (agent guardrails), `research/domain-b/` (harness-not-model, evals, cost/latency/reliability), `research/security/04-ai-agent-security.md` (control catalog), `research/cases-product/` (GitHub, Replit), `research/forensics/` (GitHub, Replit verdicts).
