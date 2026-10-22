# OpenAI — product engineering case study

Workstream: cases-product · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Public evidence on OpenAI skews toward AI-model infrastructure and agent tooling (the company's actual public engineering disclosures). Little is publicly documented about OpenAI's product discovery, requirements, or design-system practice; those sections are marked Unknown rather than inferred from generic startup norms.

## Findings

### Product discovery
- Claim: Unknown. No public OpenAI engineering or product doc found in this pass describing how OpenAI discovers or validates product ideas (interviews, betas, experiments). Label: **Unknown** (methodology gap, not absence).

### Requirements / prioritisation
- Claim: Codex product lead Alexander Embiricos describes engineers assigning work to Codex via the same systems used for humans (Linear for issue tracking, Slack for discussion). Label: **Corroborated** (secondary report; see § Sources).

### Design systems / polish
- Claim: Unknown — no public design-system disclosure found. Label: **Unknown**.

### Architecture
- Claim: ChatGPT + OpenAI API run on Azure PostgreSQL with a single-primary write architecture: one Azure PostgreSQL Flexible Server for all writes, ~50 read replicas across regions, millions of queries/second, double-digit-ms p99, ~99.999% availability. Label: **Verified** — OpenAI engineer Bohan Zhang, OpenAI engineering disclosure (Jan 2026), via VentureBeat/Medium reporting.
- Claim: Optimisations included connection pooling (PgBouncer-class; 50ms→5ms connection setup) and cache locking/leasing against thundering-herd. Label: **Verified** (same disclosure).
- Claim: One SEV-0 PostgreSQL incident in the ~12-month window: ChatGPT ImageGen launch, ~10× write traffic spike from 100M+ signups in a week. Label: **Verified** (same disclosure). Cascading-replication testing underway. Label: **Verified**.

### Implementation
- Claim: codex-1 (the model behind Codex) is a version of OpenAI's o3 fine-tuned with reinforcement learning on real software tasks; sandboxed cloud containers with no internet during task execution; AGENTS.md as machine-readable repo instructions. Label: **Corroborated** (OpenAI launch announcements via DeepLearning.ai/ZDNet, May 2025; Medium architecture write-up).
- Claim: Codex agents verify work by running tests inside the sandbox; reward is test-suite outcome rather than human preference rating. Label: **Corroborated** (same sources).

### AI usage
- Claim: OpenAI runs an "agentic software factory" around Codex: engineer/PM defines outcome → Codex gathers context (Git, GitHub, Slack, Notion, Databricks, Datadog, internal logs) → implements → builds/tests/fixes CI → PRs stay agent-babysat until green → parallel domain-specialist agent reviews. PRs per engineer growing ~10×; roughly 10× load increase on build-test-deploy systems in ~6 months. Label: **Corroborated** — Gergely Orosz (Pragmatic Engineer) interview with Venkat Venkataramani, VP Engineering, Applied Infra (Sep 2026). Single journalistic source; OpenAI has not published a first-party engineering post on this. Treat load figures as vendor-adjacent claims.
- Claim: All internal documentation moved into source code so agents can consume it; new engineers are directed to ask Codex onboarding questions; some internal Codex skills are maintained by Codex itself. Label: **Corroborated** (same source).
- Claim: A dedicated performance harness routes PRs with suspected regressions to a Synthetics A/B evaluation framework. Label: **Corroborated** (same source).
- Claim: OpenAI uses the same open-source Codex CLI internally that external developers use — "no private version." Label: **Corroborated** (report via secondary press, quoting product lead).

### Automation
- Claim: Same as agentic factory above. Label: **Corroborated**.
- Claim: CI/CD load is the scaling bottleneck OpenAI infra is "heads-down" on as of Sep 2026. Label: **Corroborated** (same interview).

### Testing / reviews
- Claim: Domain-specialist agent review (multiple agents configured per infra domain, reviewing in parallel) is used instead of one generic AI reviewer. Label: **Corroborated** (same source; the journalist notes healthy skepticism about how distinct specialist configs really are).
- Claim: Humans can no longer review every generated line; agents sort changes by risk. Label: **Corroborated** (same source).

### Security
- Claim: Codex cloud tasks run in isolated sandboxes with no internet access. Label: **Corroborated** (launch reporting).
- Claim: Dec 2025 Codex product deliberation weighed forking VS Code (after "Antigravity" launched as a VS Code fork) and decided against it — bet that agents make IDEs matter less. Label: **Corroborated** (Pragmatic Engineer interview).

### Deployment
- Claim: Write-heavy/shardable workloads are being migrated from the single-primary PostgreSQL setup to Azure Cosmos DB. Label: **Inferred** (single LinkedIn system-design post summarising the OpenAI disclosure; not directly attributed to the OpenAI post text seen).

### Monitoring
- Claim: Dec 11, 2024 incident (3:16–7:38 PM Pacific, 4h22m): a newly deployed monitoring service overloaded OpenAI's cluster control plane, took down internal service discovery, and locked engineers out of the controls needed to revert. Label: **Corroborated** (secondary postmortem compilation; Beehiiv). OpenAI did not publish a first-party write-up found in this pass — flag official-vs-unofficial gap.
- Claim: Jun 9–10, 2025: routine OS update knocked GPU servers off the network; API availability ~75% at worst; ~13h to full recovery. Label: **Corroborated** (same compilation).

### User feedback
- Claim: Engineers increasingly act as product managers (judgment, prioritisation, taste over raw code-writing). Label: **Corroborated** (VP quote via Pragmatic Engineer).

### Business outcomes
- Claim: Codex desktop app launched after internal debate (the "iPad" worry — users might treat it as a misfit between CLI and IDE). Label: **Corroborated** (same interview).
- Claim: IDE usage declining internally since Jan 2026; the bet appears vindicated. Label: **Inferred** (single interviewee observation; no metrics published).

### Documented failures
1. Dec 2024 monitoring-service outage (4h22m, control-plane cascade, locked-out operators).
2. Jun 2025 OS-update outage (~13h, API at 75%).
3. ImageGen SEV-0 on PostgreSQL (~10× write spike, cache-miss storms, CPU saturation).
4. Codex desktop-app launch hesitation (product uncertainty, not a technical incident).

### Transferable lessons
- Optimise deeply before re-architecting: proven systems stretch further than scale-panic suggests (PostgreSQL at 800M users). Label: **Verified** as OpenAI's stated lesson; applicability varies.
- Make documentation machine-consumable (docs in code) once agents are primary consumers. Label: **Corroborated**.
- Agent-generated code load lands on CI first: plan build-test-deploy capacity for ~10× PR growth. Label: **Corroborated** (single source).
- Monitoring systems are part of the blast radius: a bad telemetry rollout can remove both observability and remediation. Label: **Corroborated**.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| OA-01 | Postgres scaling | https://openai.com/index/scaling-postgresql/ (cited via https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users) | Primary (original: eng blog); secondary (reporting) | Bohan Zhang / OpenAI; VentureBeat | Jan 2026 | 2026-10-10 | High |
| OA-02 | Agentic factory, PR load, perf harness, docs-in-code | https://newsletter.pragmaticengineer.com/p/openai-software-factory | Secondary (journalism) | Gergely Orosz | ~Sep 2026 | 2026-10-10 | Medium (single source, quotes named VP) |
| OA-03 | Factory summary mirror | https://github.com/steel-experiments/internal-agents-map/blob/HEAD/archive/sources/openai-factory-article/content.md | Tertiary (archive of OA-02) | steel-experiments | 2026 | 2026-10-10 | Low (repost) |
| OA-04 | Codex CLI internal use, builds itself | https://50000c16.com/openai-codex-ai-coding-agent/ | Secondary (press) | 50000c16 | ~Dec 2025 | 2026-10-10 | Medium-low |
| OA-05 | codex-1 training, sandbox, AGENTS.md | https://www.deeplearning.ai/the-batch/openai-introduces-codex-a-multi-agent-cloud-based-software-engineering-tool-in-chatgpt | Secondary (trade press) | DeepLearning.ai | May 2025 | 2026-10-10 | Medium |
| OA-06 | Dec 2024 + Jun 2025 incidents | https://rapidflowautomation.beehiiv.com/p/your-saas-s-core-feature-runs-on-someone-else-s-uptime-the-9-a-day-ai-outage-plan-most-founders-don | Tertiary (compiled postmortems) | rapidflowautomation | Oct 2026 | 2026-10-10 | Low-medium (no official write-up located) |
| OA-07 | ImageGen 10× spike detail, Cosmos DB migration | https://www.linkedin.com/posts/bahaasaeed_openai-chatgpt-systemdesign-activity-7469070836000493572-0BgM | Secondary (analysis post) | Bahaa Saeed | ~Jun 2026 | 2026-10-10 | Low-medium |
