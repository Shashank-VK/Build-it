# Domain A — Area 8: CI/CD and Deployment (AI-assisted)

*How AI assists with building CI/CD pipelines and deploying software — pipeline generation, agents running in CI, and deployment automation.*

> Read-only research. No installation, ranking, or recommendations. Accessed 2026-10-10 unless noted.

## 1. What teams demonstrably do

### Agents authoring CI/CD pipelines
- **Claim (Corroborated):** Teams use coding agents with dedicated CI skills to generate production-grade GitHub Actions workflows: analyzing repo language/project type/deployment targets, then emitting workflows with security hardening (pin actions to SHA, OIDC), caching, and optimization. Skills trigger on phrases like "set up CI," "harden this pipeline," or when files under `.github/workflows/` are touched; they also handle migration from GitLab CI/CircleCI/Travis/Jenkins/Drone.
- Source: https://github.com/mohammaddaoudfarooqi/agent-engineering-skills/blob/HEAD/skills/github-actions/SKILL.md (evidence class: primary technical; ~Jul 2026)

### CI as the enforcement layer for agentic work
- **Claim (Corroborated):** Mature agent workflows treat CI as the non-negotiable gate: **on every PR** — build verification, full test suite (unit/integration/e2e), static analysis + lint, security scanning (dependency CVEs, SAST); **on merge to main** — re-run checks, produce a versioned snapshot artifact, CD to staging, continuous testing, flag artifact `releasable`/`non-releasable`. "The harness codified in the pipeline is identical regardless of who or what authored the change" — i.e., agent-authored and human-authored code face the same gates.
- Source: https://github.com/deors/agent-skills (evidence class: primary technical; ~Jul 2026)
- **Anthropic's own posture (Corroborated):** Anthropic's hard gate sits at test/CI, not at the agent prompt — in-session review is advisory; CI is the enforcement point.
- Source: https://github.com/uygnoey/skills-from-claude-blog/blob/HEAD/2026.07.21_how-anthropic-secures-its-ai-native-software-development-lifecycle/description.en.md

### Agents running inside CI (issue→PR automation)
- **Claim (Corroborated):** Open-source coding-agent bots (e.g. tmseidel/ai-git-bot) run in CI-style loops: webhook on issue assignment → agent works on a branch (`ai-agent/issue-{n}`) → pushes commits → opens PRs → posts progress/error comments. Documented limitations: best for focused issues (broad refactors may be incomplete); large repos/discussions can exceed context; validation retries are budget-capped; the agent can edit dependency files but can't guarantee external package availability.
- Source: https://github.com/tmseidel/ai-git-bot/blob/HEAD/doc/CODING_AGENT.md (evidence class: primary technical; Sep 2026)

### Full "AI scrum team" delivery pipelines
- **Claim (Proposed-to-Corroborated):** Community frameworks package "Scrum Team as Code": PO/scrum-master/dev/QA/security/DevOps agents with sprint workflows, Definition of Done templates, story→test→commit→release traceability, and GitHub Actions/Azure Pipelines quality gates. These are real repos with real pipeline files (e.g. `quality-gates.yml`, `azure-pipelines.yml`), but evidence of production adoption at scale was not found — treat as Proposed with working implementations.
- Source: https://github.com/flexnetos/ai-coding-factory (GitHub; ~Apr 2026)

### CI/CD for AI workloads themselves (adjacent, note the boundary)
- **Claim (Verified — official docs):** AWS's prescriptive guidance documents CI/CD for serverless AI *applications*: code+prompt commit → build/lint (incl. prompt validators) → unit tests + prompt regression (promptfoo, golden tests) → IaC validation → staging integration test → manual/auto approval (model cost impact) → production deploy → post-deploy smoke tests → monitoring (token usage, cost alerts). This is Domain A (building/deploying software) applied to AI workloads — distinct from Domain B (the AI feature in the product).
- Source: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html (AWS official docs; evidence class: primary technical)

## 2. Tools and workflows
| Tool/pattern | Role |
|---|---|
| github-actions agent skill | Generate/harden/audit workflows; migrate from other CI systems |
| quality-gates.yml pattern | PR: build+test+lint+SAST; merge: snapshot+staging+releasable flag |
| Issue-assigned coding bots | Issue → branch → PR automation with bounded retries |
| Cloud agent harnesses (GitHub.com agents, Claude Code web) | Run spec/plan/build/review from IDE, CLI, or cloud |
| Prompt-regression in CI (promptfoo, golden tests) | For repos containing prompts/AI behavior |

## 3. Failure modes
1. **Agent-authored pipeline misconfiguration.** Agents can generate plausible-but-wrong workflow YAML (wrong OIDC trust, unpinned actions, cache poisoning surface) — the skill exists to *harden*, implying the default output needs hardening. **Inferred from skill design.**
2. **Silent CI budget exhaustion.** Validation retries are budget-capped; exhausted budgets report failure rather than continuing — by design, but teams must notice the failure. **Verified (bot docs).**
3. **Broad refactors incomplete.** Issue-bots handle focused issues; multi-system changes come back partial. **Verified (bot docs).**
4. **"Scrum team as code" overreach.** Full autonomous delivery pipelines exist as repos, not as evidenced production practice — the gap between demo and deployment is the known 70–95% agent failure pattern (Fiddler AI 2026 analysis, vendor-adjacent — treat cautiously). **Proposed; negative evidence: no scaled adoption found.**
5. **Prompt/config drift in AI workloads.** Prompt changes need regression gates like code changes; without them, behavior drifts silently. **Corroborated (AWS guidance).**

## 4. Costs / latency / reliability
- CI minutes + agent inference per PR: agent-driven PRs multiply CI load (full suite per iteration, ~1.2–1.8 review iterations per autonomous PR per Presenc). **Inferred.**
- Pipeline-generation itself is cheap (single-digit dollars per workflow); the cost is in running heavier gates on more, bigger PRs. **Inferred.**

## 5. Human correction burden
- Pipeline YAML still needs human security review (OIDC, secrets, environment scoping) — agents generate the 80% but the trust-critical 20% is human. Deployment approvals (manual/auto gates on cost impact) remain human or policy-driven. **Corroborated.**

## 6. Where AI genuinely helps vs where it creates rework
- **Genuinely helps:** scaffolding standard pipelines fast; migrating between CI systems; enforcing identical gates for agent- and human-authored code; prompt-regression testing for AI-bearing repos.
- **Creates rework:** subtly wrong pipeline security config; over-ambitious "full autopilot" delivery repos that don't survive contact with real release processes.

## 7. Boundary notes (A vs B vs C)
- **Domain A:** using AI to build/deploy *your* software (pipeline generation, CI gates, deploy automation). **Domain B:** CI/CD *for* an AI product's model/prompt lifecycle is still A (it's the build process), but the *shipped AI feature* is B — AWS's "CI/CD for serverless AI" doc is A-process for B-products; keep the two roles explicit. **Domain C:** AI automating business deployments (e.g., auto-provisioning employee SaaS) — organizational, not product-building.

## Evidence register (this file)
| # | Claim | URL | Source type | Author/org | Pub date | Confidence | Class |
|---|---|---|---|---|---|---|---|
| 8.1 | GitHub Actions agent skill: generate/harden/migrate workflows | https://github.com/mohammaddaoudfarooqi/agent-engineering-skills/blob/HEAD/skills/github-actions/SKILL.md | Skill repo | mohammaddaoudfarooqi | ~Jul 2026 | Medium | primary technical |
| 8.2 | CI as enforcement layer; identical harness for agent/human code | https://github.com/deors/agent-skills | Skill pack | deors | ~Jul 2026 | Medium | primary technical |
| 8.3 | Issue→branch→PR bot with bounded retries; documented limits | https://github.com/tmseidel/ai-git-bot/blob/HEAD/doc/CODING_AGENT.md | Repo docs | tmseidel | Sep 2026 | Medium–High | primary technical |
| 8.4 | Scrum-team-as-code with traceability + quality gates | https://github.com/flexnetos/ai-coding-factory | Repo | flexnetos | ~Apr 2026 | Low (no adoption evidence) | primary technical |
| 8.5 | AWS CI/CD guidance for serverless AI workloads | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html | Official docs | AWS | 2026 | High | primary technical |
| 8.6 | 70–95% enterprise agent pilot failure (Fiddler AI 2026, via vendor blog) | https://coasty.ai/blog/ai-agent-workflow-automation-patterns-2026-20261003 | Vendor blog | Coasty | Oct 2026 | Low | unverified |
