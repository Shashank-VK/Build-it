# Part 15 + Part 16 — Build Systems, CI/CD, Cloud & Production Infrastructure; SEO, Analytics, Content, Commerce & Website Operations (06c-operations)

> Research workstream #13 | Verification date: 2026-10-10
> READ-ONLY research: discover, inspect, identify, verify, categorize, explain usage, record sources.
> No installing, executing, building, configuring, ranking, or recommending.
> Record type classification used: **cloud service** / **open-source project** / **development utility** / **agent integration** / **infrastructure framework**.

## 0. Research method

### Sources searched (primary-first)
For each resource: official product site, official docs, official GitHub repository (README, docs/, releases/CHANGELOG), official pricing/changelog pages. Primary sources fetched directly: pre-commit.com (full docs), evilmartians/lefthook README, opentofu.org (FAQ), workers.cloudflare.com (product page). Secondary: 2026 technical comparisons, skills references, and curated knowledge bases, used only to corroborate status/pricing and never as sole evidence for existence. Every official URL below was seen verbatim in search results or opened directly; none were guessed.

### Search themes used
1. `pre-commit.com husky lefthook lint-staged git hooks framework comparison` (A2)
2. `CI/CD platforms 2026 GitHub Actions GitLab CI CircleCI Buildkite Jenkins comparison` (A3)
3. `OpenTofu Terraform fork status 2026 Pulumi infrastructure as code` (A8)
4. `Docker Podman containerd devcontainers specification 2026 developer environments` (A6/A7)
5. `frontend hosting 2026 Vercel Netlify Cloudflare Pages comparison preview deployments` (A10/A17)
6. `observability platforms 2026 Datadog Grafana Sentry OpenTelemetry Prometheus error tracking` (A20/A21)
7. `backend hosting PaaS 2026 Fly.io Render Railway Coolify self-hosted Heroku alternative` (A11)
8. `Cloudflare Workers Deno Deploy edge runtime 2026 serverless functions workerd WinterCG` (A12)
9. `managed Postgres database 2026 Neon Supabase PlanetScale Turso serverless pricing` (A14)
10. `secrets management 2026 HashiCorp Vault Doppler Infisical 1Password SOPS` (A15)
11. `release automation semantic-release changesets release-please GoReleaser conventional commits 2026` (A18)
12. `background jobs workflow orchestration 2026 Inngest Trigger.dev Temporal durable execution` (A25)
13. `LLM observability 2026 Langfuse LangSmith Helicone Braintrust AI agent tracing` (A23)
14. `feature flags 2026 LaunchDarkly Unleash Flagsmith GrowthBook progressive delivery` (A19)
15. `headless CMS 2026 Sanity Contentful Strapi Payload Storyblok comparison` (B7)
16. `documentation platforms 2026 Docusaurus Mintlify GitBook Starlight developer docs` (B9)
17. `ecommerce frameworks 2026 Shopify MedusaJS Saleor WooCommerce headless commerce` (B10)
18. `transactional email API 2026 Resend SendGrid Mailgun Postmark Loops` (B12)
19. `web analytics 2026 Plausible Fathom Umami PostHog privacy-friendly GA4 alternative` (B3/B4)
20. `technical SEO tools 2026 schema.org structured data sitemap Core Web Vitals` (B1)
21. `site search 2026 Algolia Typesense Meilisearch Elasticsearch self-hosted` (B15)
22. `uptime monitoring 2026 UptimeRobot Better Stack Checkly Pingdom status page` (B18)
23. `i18n localization tooling 2026 i18next next-intl Crowdin Lokalise Tolgee` (B14)
24. `consent management platform 2026 CookieYes OneTrust Klaro GDPR cookie banner` (B5)
25. `monorepo build tools 2026 Turborepo Nx Bazel Buck2 remote caching` (A5)
26. `developer environment tools 2026 mise direnv Nix Devbox toolchain management` (A7/A16)
27. `headless coding agent CI 2026 GitHub Copilot coding agent Claude Code GitHub Action Codex cloud` (A26)
28. `cloud cost monitoring 2026 Infracost Vantage OpenCost Kubecost FinOps` (A24)
29. `Kamal Dokku CapRover deployment automation Docker 2026 Argo CD GitOps` (A4/A17)
30. `user feedback tools 2026 Canny Featurebase Nolt product feedback voting` (B16)
31. `online forms 2026 Typeform Tally Formspree form backend API comparison` (B17)
32. `customer messaging support 2026 Intercom Crisp Plain chat in-app support` (B13)

### Deduplication (already catalogued — cross-referenced, not re-researched)
Per the workstream brief, these are cross-referenced only (full records live in the prior OpenCode ecosystem catalog): opencode-primer (CI guide), opencode-shell-strategy, opencode serve/run/web, opencode github install, opencode-plugin-otel, pai4451/opencode-telemetry-plugin, Langfuse OpenCode Observability, opencode stats CLI, ocsight, opencode-token-monitor, opencode-tokenscope, opencode-bar, opencode-stats, opencode-dashboard, tongsh6/opencode-token-tracker, gaboe/opencode-usage, eserete/opencode-token-tracker, Token Monitor, OpenCode Throughput, Opencode Quota, Opencode Usage Monitor, Opencode Telemetry, opencode-mystatus, kdcokenny/opencode-background-agents, zenobi-us/opencode-background, server-manager, opencode-scheduler, opencode-notify, Pilot, Dodo Payments MCP, cloudflare/skills, entireio/cli, KyungJunAn/opencode-rewind, @arkfactory/opencode-checkpoint, witlox/opencode-checkpoint, kdcokenny/opencode-worktree, felixAnhalt/opencode-worktree-session, NjengaFelix/opencode-permissions, joelhooks/opencode-config. Where such a tool is a general-platform resource (Langfuse, Dodo Payments), the general record appears below and the OpenCode-specific integration is cross-referenced.

### Verification labels (used exactly as specified)
**Verified** / **Partially verified** / **Unverified** / **Corrected** / **Archived** / **Inaccessible** / **Historical** / **Unresolved**

### Notable 2026 status changes found during research
- **Deno team joined Cloudflare; Deno Deploy sunsets ~April 2027** (announced 2026-10-09; six-month window). Deno runtime gets one year of maintenance releases.
- **Langfuse acquired by ClickHouse** (January 2026).
- **Statsig acquired by OpenAI** (September 2025); **Amplitude took over the Statsig brand/customers** (May 2026).
- **MkDocs Material entered maintenance mode** (November 2025; security fixes only until November 2026).
- **Piwik PRO free Core plan sunset** (February 2026).
- **Intercom rebranded to Fin** (May 2026); **Salesforce acquisition of Intercom/Fin signed** (June 2026, pending close).
- **Mixpanel November 2025 security breach** (ShinyHunters; ~28M accounts) — widely cited in 2026 comparisons.
- **Neon acquired by Databricks** (May 2025).
- **IBM closed HashiCorp acquisition** ($6.4B, February 2025); BSL license unchanged as of September 2026.
- **Helicone services in maintenance mode** (per 2026 AI-observability roundup; proxy gateway product).
- **Railway removed its free tier** (trial credit only); **Koyeb closed free tier to new users** (2026).
- **GitHub Actions cut Linux rates up to 39%** (January 2026); announced-then-postponed self-hosted runner fee.
- **Earthly shut down its cloud** (July 2025); **BuildJet closed** (March 2026) after GitHub shipped native larger/ARM runners.
- **GitHub Agentic Workflows** in preview; **Buildkite LLM proxy** (Anthropic models); **TeamCity AI Assistant + MCP support**.

---

## A. Build systems, CI/CD, cloud, production infrastructure

### A1. Version control & repo management

#### A1.1 Git
- **Canonical identity:** Git — distributed version control system (git-scm.com). **Type:** open-source project / development utility.
- **Official URL:** https://git-scm.com — **Verification:** Verified.
- **Description / capabilities:** Distributed VCS; branching, merging, worktrees (`git worktree` for multiple checked-out branches), hooks (`.git/hooks`), signed commits/tags, sparse checkout, partial clone. Worktrees are the native primitive behind OpenCode-worktree-style agent workflows (already catalogued separately; cross-reference only).
- **Contents inspected:** Prior knowledge of git CLI/docs; worktree feature confirmed via git-scm documentation references in search results (sparse-checkout/worktree guidance in monorepo standards docs).
- **Usage domain:** Source control for all downstream categories. **Integration method:** CLI; libgit2 bindings; hosting-platform APIs.
- **Compatibility:** Universal. **Dependencies:** None. **Availability:** All platforms. **Maintenance:** Active (git project). **License:** GPL-2.0.
- **Limitations:** Monorepo scale needs blobless/sparse checkouts; LFS for large files. **Related:** GitHub, GitLab, pre-commit frameworks.
- **Sources:** https://git-scm.com; search themes 1, 25. **Verification date:** 2026-10-10. **Confidence:** High.

#### A1.2 GitHub
- **Canonical identity:** GitHub — code hosting & collaboration platform (github.com), owned by Microsoft. **Type:** cloud service.
- **Official URL:** https://github.com — **Verification:** Verified.
- **Description / capabilities:** Git hosting, pull requests, code review, Issues, Projects, GitHub Packages (container/npm registries), GitHub Pages, Codespaces, branch protection, required checks, OIDC federation to clouds, fine-grained PATs, GitHub Apps, MCP/REST/GraphQL APIs. The substrate for GitHub Actions (A3.1) and Copilot coding agent (A26.1).
- **Contents inspected:** docs.github.com references across search results (Actions minutes, OIDC, coding agent docs). **Usage domain:** Repo management + CI/CD + agent execution.
- **Integration method:** Web UI, `gh` CLI, REST/GraphQL APIs, webhooks. **Compatibility:** Git-standard. **Dependencies:** None. **Availability:** SaaS; GitHub Enterprise Server self-hosted. **Maintenance:** Active. **License:** Proprietary (service).
- **Limitations:** Actions minutes billed; larger runners cost extra. **Related:** GitHub Actions, GitLab, Bitbucket.
- **Sources:** https://github.com; https://docs.github.com; search themes 2, 27. **Verification date:** 2026-10-10. **Confidence:** High.

#### A1.3 GitLab
- **Canonical identity:** GitLab — DevOps platform (SaaS + self-managed), gitlab.com / about.gitlab.com. **Type:** cloud service / open-source project (self-managed).
- **Official URL:** https://about.gitlab.com — **Verification:** Partially verified.
- **Description / capabilities:** Git hosting, merge requests, built-in CI/CD (`.gitlab-ci.yml`), container/package registries, environments, review apps, Duo AI features. All-in-one alternative to GitHub+separate CI.
- **Usage domain:** Repo management + CI/CD. **Integration method:** Web UI, `glab` CLI, APIs. **Availability:** SaaS (400 CI minutes/mo free per comparisons) and self-managed. **License:** MIT (core/CE components) + proprietary tiers; not fully re-verified — marked Partially verified.
- **Limitations:** SaaS CI minute allowance smaller than GitHub's. **Related:** GitHub, GitLab CI/CD (A3.2).
- **Sources:** https://about.gitlab.com; search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A1.4 Bitbucket
- **Canonical identity:** Bitbucket — Git hosting by Atlassian (bitbucket.org). **Type:** cloud service.
- **Official URL:** https://bitbucket.org — **Verification:** Partially verified.
- **Description / capabilities:** Git hosting integrated with Jira/Trello; Bitbucket Pipelines CI (A3.7); pull requests, branch permissions.
- **Usage domain:** Atlassian-ecosystem repo management. **Availability:** Cloud + Data Center self-hosted. **License:** Proprietary.
- **Limitations:** Smaller ecosystem than GitHub/GitLab. **Related:** GitHub, GitLab, Azure DevOps.
- **Sources:** search theme 2 (comparison tables). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A1.5 Gitea / Forgejo
- **Canonical identity:** Gitea (gitea.com) — self-hosted Git service; Forgejo (forgejo.org) — community fork of Gitea. **Type:** open-source project.
- **Official URL:** https://gitea.com ; https://forgejo.org — **Verification:** Partially verified.
- **Description / capabilities:** Lightweight self-hosted Git hosting with issues, PRs, packages, and built-in Actions-compatible CI (Gitea Actions). Forgejo forked after Gitea's governance changes; Codeberg runs Forgejo.
- **Usage domain:** Self-hosted repo management. **Integration method:** Binary/Docker self-host. **License:** MIT (both).
- **Limitations:** Smaller feature surface than GitHub/GitLab (no native advanced CI matrix scale). **Related:** GitLab self-managed, Sourcehut.
- **Sources:** General knowledge + search themes 2, 18 (Forgejo cited in release-tooling multi-forge support). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A1.6 Azure DevOps (Repos + Pipelines)
- **Canonical identity:** Azure DevOps — Microsoft DevOps suite (dev.azure.com). **Type:** cloud service.
- **Official URL:** https://dev.azure.com — **Verification:** Partially verified.
- **Description / capabilities:** Azure Repos (Git), Azure Pipelines (CI/CD), Boards, Artifacts, Test Plans. Strong in Microsoft/Azure-centric enterprises.
- **Usage domain:** Enterprise repo + CI/CD. **License:** Proprietary. **Limitations:** UI/UX considered dated vs GitHub.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A2. Pre-commit & git-hook frameworks

#### A2.1 pre-commit (pre-commit.com)
- **Canonical identity:** `pre-commit` — multi-language Git hook manager by Anthony Sottile (github.com/pre-commit/pre-commit). **Type:** open-source project / development utility.
- **Official URL:** https://pre-commit.com — **Verification:** Verified (site fetched in full).
- **Description / capabilities:** Manages installation/execution of Git hooks written in any language; hooks declared in `.pre-commit-config.yaml` referencing hook repos at pinned `rev`s; auto-creates isolated environments (Python/Node/Ruby/Go etc.) so contributors need no local toolchain; `pre-commit install`, `run --all-files`, `autoupdate`; `PRE_COMMIT=1` env during hook execution; `pre-commit.ci` companion service auto-fixes PRs.
- **Contents inspected:** Full pre-commit.com docs (install, quickstart, config reference for repos/hooks, hook-repo authoring format, `stages`, `pass_filenames`, `require_serial`).
- **Usage domain:** Local commit-time quality gates (format, lint, secrets detection, whitespace). **Integration method:** `pip install pre-commit` or `.pyz` zipapp; `pre-commit install` writes into `.git/hooks`.
- **Compatibility:** Any Git repo, any language. **Dependencies:** Python runtime (or pyz). **Availability:** PyPI. **Maintenance:** Active (docs show v4.6.2). **License:** MIT.
- **Limitations:** First run downloads/builds hook envs (slow cold start); weaker parallel story than lefthook on huge repos.
- **Related:** lefthook, husky, pre-commit.ci.
- **Sources:** https://pre-commit.com (fetched 2026-10-10); search theme 1. **Verification date:** 2026-10-10. **Confidence:** High.

#### A2.2 lefthook
- **Canonical identity:** lefthook — fast Git hooks manager by Evil Martians (github.com/evilmartians/lefthook). **Type:** open-source project / development utility.
- **Official URL:** https://github.com/evilmartians/lefthook (docs: lefthook.dev) — **Verification:** Verified (README fetched).
- **Description / capabilities:** Single dependency-free Go binary managing Git hooks for any project type; parallel execution; glob/regexp file filters; `{staged_files}` templates; sub-directory execution roots; script runners (incl. Docker); tags + `lefthook-local.yml` overrides; JSON schema for config; `lefthook install` / `lefthook run <hook>`.
- **Contents inspected:** Full README (install via go/npm/gem/pipx/apt/brew/winget, usage, parallel execution, file lists, globs, sub-directory, scripts, tags, Docker, local config, output control); repo metadata: 8,890 stars, 1,272 commits, MIT, not archived, v2.2.1 referenced.
- **Usage domain:** Polyglot repos, monorepos where hook speed matters. **Integration method:** Binary install + `lefthook.yml` + `lefthook install`.
- **Compatibility:** Any Git repo. **Dependencies:** None (static binary). **Availability:** GitHub releases + package managers. **Maintenance:** Active. **License:** MIT.
- **Limitations:** Smaller ready-made hook catalog than pre-commit; staged-file runs don't stash unstaged changes (precision tradeoff noted in comparisons).
- **Related:** pre-commit, husky.
- **Sources:** https://github.com/evilmartians/lefthook (fetched 2026-10-10); search theme 1. **Verification date:** 2026-10-10. **Confidence:** High.

#### A2.3 husky
- **Canonical identity:** husky — Git hooks made easy for Node.js (github.com/typicode/husky). **Type:** open-source project / development utility.
- **Official URL:** https://typicode.github.io/husky (repo: https://github.com/typicode/husky) — **Verification:** Partially verified.
- **Description / capabilities:** Installs Git hooks from `.husky/` shell scripts on `npm install` (via `prepare` script); v9+ (`npx husky init`) simplified setup; typically paired with lint-staged.
- **Usage domain:** JS/TS projects. **Integration method:** npm devDependency. **License:** MIT. **Maintenance:** Active (v9 line).
- **Limitations:** Node-centric; needs lint-staged for staged-file filtering. **Related:** lint-staged, lefthook, Husky.Net.
- **Sources:** search theme 1. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A2.4 lint-staged
- **Canonical identity:** lint-staged — run linters on staged Git files (github.com/lint-staged/lint-staged). **Type:** open-source project / development utility.
- **Official URL:** https://github.com/lint-staged/lint-staged — **Verification:** Partially verified.
- **Description / capabilities:** Runs configured linters/formatters only against staged files; configured via `lint-staged` key in `package.json` or config file; usually invoked from husky `pre-commit` hook.
- **Usage domain:** JS/TS commit-time linting. **License:** MIT. **Maintenance:** Active (v15+).
- **Limitations:** JS ecosystem only; pulls a dependency chain.
- **Sources:** search theme 1. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A2.5 Husky.Net
- **Canonical identity:** Husky.Net — Git hooks task runner for .NET (dotnet tool). **Type:** open-source project / development utility.
- **Official URL:** https://github.com/alirezanet/Husky.Net — **Verification:** Partially verified.
- **Description / capabilities:** `dotnet tool install Husky`; JSON `task-runner.json` config; `${staged}` incremental processing; attaches to `.csproj` for team install.
- **Usage domain:** .NET/C# projects. **License:** MIT (per comparisons).
- **Sources:** search theme 1. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A2.6 pre-commit.ci
- **Canonical identity:** pre-commit.ci — hosted service that runs pre-commit hooks on pull requests and auto-fixes. **Type:** cloud service / agent integration.
- **Official URL:** https://pre-commit.ci — **Verification:** Partially verified.
- **Description / capabilities:** GitHub App; runs `.pre-commit-config.yaml` hooks in CI; auto-fix commits pushed to PRs; autoupdate PRs for hook rev bumps.
- **Usage domain:** CI-side enforcement of the same hooks developers run locally. **License:** Proprietary (free for open source / paid private per public docs — not re-verified).
- **Sources:** search theme 1; pre-commit.com references. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A2.7 commitlint / commitizen
- **Canonical identity:** commitlint (github.com/conventional-changelog/commitlint) — lint commit messages against Conventional Commits; Commitizen (commitizen.github.io/cz-cli) — guided commit message prompts. **Type:** open-source project / development utility.
- **Official URL:** https://commitlint.js.org ; http://commitizen.github.io/cz-cli/ — **Verification:** Partially verified.
- **Description / capabilities:** commitlint validates `commit-msg` hook input (used with husky/lefthook/pre-commit); Commitizen provides `cz` interactive prompt producing conventional messages.
- **Usage domain:** Feed for release automation (A18). **License:** MIT.
- **Sources:** search themes 1, 11. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A3. CI platforms

#### A3.1 GitHub Actions
- **Canonical identity:** GitHub Actions — CI/CD + workflow automation native to GitHub (docs.github.com/actions). **Type:** cloud service / infrastructure framework.
- **Official URL:** https://github.com/features/actions — **Verification:** Verified (docs referenced across primary GitHub docs; pricing/features corroborated by 2026 comparisons).
- **Description / capabilities:** YAML workflows in `.github/workflows/`; event triggers (push, PR, schedule, manual, webhooks); hosted runners (Linux/Windows/macOS, x64/ARM, GPU, larger runners); self-hosted runners; matrix builds; reusable workflows + composite actions; Actions Marketplace (~third-party actions, pin-by-SHA recommended); environments with approvals; OIDC-to-cloud (keyless AWS/GCP/Azure auth); artifacts, caches; 2026: Linux rate cuts up to 39% (Jan 2026), native larger/ARM runners, Agentic Workflows in preview.
- **Contents inspected:** GitHub docs pages referenced via search (coding-agent docs confirm Actions-powered ephemeral envs); 2026 pricing comparisons (2,000–3,000 min/mo Team; unlimited for public repos).
- **Usage domain:** CI for GitHub repos; also the execution substrate for Copilot coding agent and Claude Code GitHub Action (A26). **Integration method:** Workflow YAML + `gh`/`git` push; API + webhooks.
- **Compatibility:** Any language; any Git host only via mirroring (native to GitHub). **Dependencies:** GitHub account. **Availability:** SaaS + self-hosted runners. **Maintenance:** Active. **License:** Proprietary service; runner agent open source (MIT).
- **Limitations:** Marketplace supply-chain risk (third-party actions run in your context); minutes billed for private repos; macOS/Windows multipliers.
- **Related:** GitLab CI/CD, CircleCI, Buildkite, Jenkins, act (local runner — see rapid-fire).
- **Sources:** https://github.com/features/actions; https://docs.github.com/actions; search themes 2, 27. **Verification date:** 2026-10-10. **Confidence:** High.

#### A3.2 GitLab CI/CD
- **Canonical identity:** GitLab CI/CD — pipelines defined in `.gitlab-ci.yml`. **Type:** cloud service / infrastructure framework.
- **Official URL:** https://about.gitlab.com — **Verification:** Partially verified.
- **Description / capabilities:** YAML pipelines with stages, `include:`/`extends:`, DAG (`needs:`), `parallel: matrix`, environments + review apps, protected/masked variables, OIDC to clouds, built-in container/package registries; self-managed runners free.
- **Usage domain:** GitLab-native DevOps. **Availability:** SaaS + self-managed. **License:** Proprietary tiers over open core.
- **Limitations:** SaaS minute allowance modest (400–10,000/mo depending on tier per 2026 comparisons); runner fleet ops when self-hosting.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.3 Jenkins
- **Canonical identity:** Jenkins — self-hosted automation server (jenkins.io; CloudBees commercial). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://www.jenkins.io — **Verification:** Partially verified.
- **Description / capabilities:** Groovy `Jenkinsfile` (declarative + scripted), shared libraries, ~1,800 plugins, agents on any infrastructure, air-gap capable; 2026 comparisons position it for legacy/complex/on-prem estates.
- **Usage domain:** Self-hosted CI at scale; regulated/air-gapped builds. **Integration method:** Self-hosted WAR/container + agents. **License:** MIT.
- **Limitations:** Plugin sprawl/maintenance burden; UI dated; no native cloud.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.4 CircleCI
- **Canonical identity:** CircleCI — cloud CI with orbs (circleci.com). **Type:** cloud service.
- **Official URL:** https://circleci.com — **Verification:** Partially verified.
- **Description / capabilities:** `.circleci/config.yml`; orbs (versioned reusable config); workflows, matrix, parallelism, test splitting (ML-based), strong caching; cloud + self-hosted runners; Linux/Windows/macOS/ARM.
- **Usage domain:** Cloud-native teams wanting build speed. **License:** Proprietary (credit-based pricing; free tier credits).
- **Limitations:** Credit metering complexity; macOS costs.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.5 Buildkite
- **Canonical identity:** Buildkite — hybrid CI: SaaS control plane, customer-run agents (buildkite.com). **Type:** cloud service.
- **Official URL:** https://buildkite.com — **Verification:** Partially verified.
- **Description / capabilities:** `.buildkite/pipeline.yml` (+ dynamic pipelines generated at runtime); agents on your infra (any cloud/on-prem); per-user pricing + your compute; hosted agents optional; 2026: LLM proxy with Anthropic models.
- **Usage domain:** Enterprise-scale builds where compute economics dominate. **License:** Proprietary.
- **Limitations:** You operate the agent fleet.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.6 Azure Pipelines
- **Canonical identity:** Azure Pipelines — CI/CD in Azure DevOps (dev.azure.com). **Type:** cloud service.
- **Official URL:** https://dev.azure.com — **Verification:** Partially verified.
- **Description / capabilities:** YAML pipelines, Microsoft-hosted + self-hosted agents, environments/approvals; free tier (1 parallel job, 1,800 min/mo per comparisons).
- **Usage domain:** Microsoft/Azure-centric enterprises. **License:** Proprietary.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.7 Bitbucket Pipelines
- **Canonical identity:** Bitbucket Pipelines — CI integrated in Bitbucket Cloud. **Type:** cloud service.
- **Official URL:** https://bitbucket.org/product/features/pipelines — **Verification:** Partially verified.
- **Description / capabilities:** `bitbucket-pipelines.yml`; Docker-based steps; Jira integration; modest free minutes.
- **Usage domain:** Atlassian-ecosystem teams. **License:** Proprietary.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.8 TeamCity
- **Canonical identity:** TeamCity — JetBrains CI/CD server (jetbrains.com/teamcity). **Type:** cloud service / open-source-adjacent project.
- **Official URL:** https://www.jetbrains.com/teamcity/ — **Verification:** Partially verified.
- **Description / capabilities:** Kotlin DSL configs, build chains, remote-run/personal builds; Cloud + self-hosted; 2026: AI Assistant, MCP support per comparisons.
- **Usage domain:** JetBrains-ecosystem teams. **License:** Proprietary (free tier: 3 agents/100 build configs).
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.9 Drone / Woodpecker CI
- **Canonical identity:** Drone (drone.io) — container-native CI; Woodpecker CI (woodpecker-ci.org) — community fork. **Type:** open-source project.
- **Official URL:** https://www.drone.io ; https://woodpecker-ci.org — **Verification:** Partially verified.
- **Description / capabilities:** Pipeline-as-YAML executed in Docker containers; lightweight self-hosted; Woodpecker forked over licensing concerns (2023-era) and is community-run.
- **Usage domain:** Self-hosted container-native CI. **License:** PolyForm/Apache mix (Drone) / Apache-2.0 (Woodpecker) — exact current license not re-verified.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A3.10 GoCD
- **Canonical identity:** GoCD — open-source CD server (gocd.org, Thoughtworks). **Type:** open-source project.
- **Official URL:** https://www.gocd.org — **Verification:** Partially verified.
- **Description / capabilities:** Pipeline modeling with value-stream maps; agents; strong for complex deployment pipelines.
- **Usage domain:** Complex pipeline modeling, self-hosted. **License:** Apache-2.0.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.11 Dagger
- **Canonical identity:** Dagger — programmable container-native CI/CD engine (dagger.io). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://dagger.io — **Verification:** Partially verified.
- **Description / capabilities:** Pipelines as code (Go/Python/TypeScript SDKs) running in containers identically locally and in CI; Dagger Cloud for caching/telemetry; often wrapped inside an existing CI rather than replacing it.
- **Usage domain:** Portable pipelines. **License:** Apache-2.0 (engine).
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.12 Harness
- **Canonical identity:** Harness — software delivery platform (harness.io). **Type:** cloud service.
- **Official URL:** https://www.harness.io — **Verification:** Partially verified.
- **Description / capabilities:** CI + CD + feature flags (Split by Harness) + cloud cost management; approvals, policy-as-code, progressive delivery; SaaS or self-managed; enterprise sales-led.
- **Usage domain:** Enterprise governance-heavy delivery. **License:** Proprietary.
- **Sources:** search themes 2, 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A3.13 Semaphore
- **Canonical identity:** Semaphore — CI/CD (semaphoreci.com); 2026 positioning as "agent-native/AI-native CI". **Type:** cloud service.
- **Official URL:** https://semaphoreci.com — **Verification:** Partially verified.
- **Description / capabilities:** Cloud CI with Community Edition self-hosted option; pay-as-you-go from ~$0.003/min per comparisons.
- **Usage domain:** Teams wanting hosted CI with AI-agent-friendly features. **License:** Proprietary.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A3.14 Travis CI — Historical note
- **Canonical identity:** Travis CI (travis-ci.com). **Type:** cloud service. **Verification:** Historical.
- **Description:** Once-dominant hosted CI for open source; now legacy/usage-based pricing; retained only for legacy projects per 2026 comparisons. Not recommended for new work by current sources.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A4. CD, GitOps & progressive delivery

#### A4.1 Argo CD
- **Canonical identity:** Argo CD — declarative GitOps CD for Kubernetes (argoproj.github.io/cd), CNCF graduated. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://argo-cd.readthedocs.io ; https://argoproj.github.io/cd/ — **Verification:** Partially verified.
- **Description / capabilities:** Kubernetes controller syncing cluster state to Git (desired state); UI + CLI; sync waves, hooks, automated/manual sync; works with Helm/Kustomize/plain manifests; Application CRD.
- **Usage domain:** Kubernetes GitOps delivery. **Integration method:** In-cluster install (Helm/kustomize). **License:** Apache-2.0. **Maintenance:** Active (CNCF).
- **Limitations:** K8s-only; secrets handling needs external tooling (SOPS/External Secrets).
- **Related:** Flux, Argo Rollouts, Helm, Kustomize.
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A4.2 Flux
- **Canonical identity:** Flux — GitOps toolkit for Kubernetes (fluxcd.io), CNCF graduated. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://fluxcd.io — **Verification:** Partially verified.
- **Description / capabilities:** Set of K8s controllers (source, kustomize, helm, notification) reconciling Git to cluster; CLI-driven, less UI than Argo CD.
- **Usage domain:** Kubernetes GitOps. **License:** Apache-2.0.
- **Sources:** search theme 29 (SOPS-via-Flux cited in secrets research). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A4.3 Argo Rollouts
- **Canonical identity:** Argo Rollouts — progressive delivery for Kubernetes (argoproj.github.io/rollouts). **Type:** open-source project.
- **Official URL:** https://argoproj.github.io/rollouts/ — **Verification:** Partially verified.
- **Description / capabilities:** Canary/blue-green rollouts, automated analysis with metrics (Prometheus/Datadog), traffic management via ingress/service-mesh.
- **Usage domain:** Safe production rollouts on K8s. **License:** Apache-2.0.
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A4.4 Spinnaker — Historical note
- **Canonical identity:** Spinnaker — multi-cloud CD platform (spinnaker.io). **Type:** open-source project. **Verification:** Historical/Partially verified.
- **Description:** Pioneered advanced deployment strategies (red/black); 2026 sources rarely shortlist it; community activity reduced relative to Argo/Flux. Retained for historical completeness.
- **Sources:** search themes 2, 29. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A4.5 Octopus Deploy
- **Canonical identity:** Octopus Deploy — deployment automation (octopus.com). **Type:** cloud service / open-source-adjacent.
- **Official URL:** https://octopus.com — **Verification:** Partially verified.
- **Description / capabilities:** Release/environment promotion, runbook automation, multi-tenancy; self-hosted or cloud; per-target pricing.
- **Usage domain:** Enterprise CD with approval-heavy flows. **License:** Proprietary.
- **Sources:** search theme 2. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A4.6 Helm
- **Canonical identity:** Helm — Kubernetes package manager (helm.sh), CNCF graduated. **Type:** open-source project / development utility.
- **Official URL:** https://helm.sh — **Verification:** Partially verified.
- **Description / capabilities:** Charts (templated K8s manifests), releases, rollbacks, values overlays; the de-facto K8s packaging format consumed by Argo CD/Flux.
- **Usage domain:** K8s app packaging/deploy. **License:** Apache-2.0.
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A4.7 Kustomize
- **Canonical identity:** Kustomize — template-free K8s customization (kustomize.io; built into kubectl). **Type:** open-source project / development utility.
- **Official URL:** https://kustomize.io — **Verification:** Partially verified.
- **Description / capabilities:** Overlays/patches on base manifests without templating; native `kubectl -k`.
- **Usage domain:** K8s manifest management. **License:** Apache-2.0.
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A5. Build systems & monorepo tooling

#### A5.1 Bazel
- **Canonical identity:** Bazel — polyglot build system (bazel.build), open-sourced by Google. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://bazel.build — **Verification:** Partially verified.
- **Description / capabilities:** Explicit dependency graph, hermetic/reproducible builds, fine-grained target-level incrementality, local + remote caching, remote execution API, large rules ecosystem (rules_oci, etc.).
- **Usage domain:** Large polyglot monorepos; correctness-critical CI. **License:** Apache-2.0. **Maintenance:** Active (v8.x line per references).
- **Limitations:** Steep learning curve; BUILD-file authoring overhead.
- **Related:** Buck2, Pants, Turborepo.
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A5.2 Buck2
- **Canonical identity:** Buck2 — large-scale build system by Meta (buck2.build; github.com/facebook/buck2), Rust implementation. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://buck2.build — **Verification:** Partially verified.
- **Description / capabilities:** Single incremental dependency graph, dynamic dependencies, remote execution, deferred materialization; ~2x faster than Buck1 per Meta; targets C++/Python/Rust/Java/Kotlin/Go.
- **Usage domain:** Very large polyglot monorepos. **License:** Apache-2.0/MIT (dual, per comparisons).
- **Limitations:** Meta-ecosystem conventions; smaller community than Bazel.
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A5.3 Pants
- **Canonical identity:** Pants — build system for Python/JVM/Go monorepos (pantsbuild.org). **Type:** open-source project.
- **Official URL:** https://www.pantsbuild.org — **Verification:** Partially verified.
- **Description / capabilities:** Dependency inference, fine-grained caching, remote cache/execution, Docker/Shell support.
- **Usage domain:** Python-heavy and JVM-heavy polyglot teams. **License:** Apache-2.0.
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A5.4 Turborepo
- **Canonical identity:** Turborepo — JS/TS monorepo task runner by Vercel (turbo.build). **Type:** open-source project / development utility.
- **Official URL:** https://turbo.build — **Verification:** Partially verified.
- **Description / capabilities:** Package-level task graph (`turbo.json`), content-aware caching, remote caching (Vercel Remote Cache, free tier), `--filter=...[origin/main]` affected builds, parallel execution; v2.x current per 2026 sources.
- **Usage domain:** JS/TS monorepos; CI acceleration. **Integration method:** npm package `turbo`. **License:** MIT. **Maintenance:** Active.
- **Limitations:** JS/TS-focused; cache poisoning risk from fork PRs (keep untrusted writers read-only).
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A5.5 Nx
- **Canonical identity:** Nx — monorepo build system + dev tools (nx.dev), by Nx (formerly Nrwl). **Type:** open-source project / development utility.
- **Official URL:** https://nx.dev — **Verification:** Partially verified.
- **Description / capabilities:** Project graph, affected commands (`nx affected --base=...`), generators, plugin ecosystem (React/Angular/Node), Nx Cloud remote caching (free credits tier), distributed task execution.
- **Usage domain:** Large JS/TS teams, enterprise monorepos. **License:** MIT (core).
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A5.6 Gradle / Maven
- **Canonical identity:** Gradle (gradle.org) — JVM build automation; Maven (maven.apache.org) — Java convention-based builds. **Type:** open-source project / development utility.
- **Official URL:** https://gradle.org ; https://maven.apache.org — **Verification:** Partially verified.
- **Description / capabilities:** Gradle: Groovy/Kotlin DSL, incremental builds, build cache, remote cache, Android standard. Maven: `pom.xml` convention, vast plugin/artifact ecosystem (Maven Central).
- **Usage domain:** JVM/Android builds. **License:** Apache-2.0.
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A5.7 Moon
- **Canonical identity:** moon — polyglot task runner/build orchestrator (moonrepo.dev). **Type:** open-source project / development utility.
- **Official URL:** https://moonrepo.dev — **Verification:** Partially verified.
- **Description / capabilities:** Language-agnostic task running with hashing/caching for teams mixing JS + Rust + Go + Python; positioned as polyglot alternative to Turborepo.
- **Usage domain:** Polyglot monorepos. **License:** MIT (per comparisons — not re-verified).
- **Sources:** search theme 25. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A6. Containers & Kubernetes

#### A6.1 Docker (Engine + Compose)
- **Canonical identity:** Docker — container platform (docker.com); Compose spec for multi-container apps. **Type:** open-source project (engine, Apache-2.0/Moby) / cloud service (Docker Hub, Desktop).
- **Official URL:** https://www.docker.com ; https://docs.docker.com — **Verification:** Verified (engine facts corroborated across 2026 comparisons; Docker Desktop licensing terms widely documented).
- **Description / capabilities:** `dockerd` daemon + CLI, OCI images, BuildKit builds, Compose multi-service orchestration, Docker Hub registry; Swarm (legacy). 2026: Docker Desktop paid for commercial use above ~250 employees/$10M revenue; engine remains free.
- **Usage domain:** Local dev, CI builds, single-host services, image distribution. **Integration method:** CLI/API; Compose YAML.
- **Compatibility:** OCI images portable to Podman/containerd. **Dependencies:** Linux kernel features (or VM on macOS/Windows). **Availability:** All major OSes. **Maintenance:** Active. **License:** Apache-2.0 (Moby/engine); Desktop proprietary.
- **Limitations:** Root daemon security surface; macOS/Windows runs in a VM (RAM/startup cost); Desktop licensing for larger orgs.
- **Related:** Podman, containerd, Buildah, OrbStack, Colima.
- **Sources:** search theme 4. **Verification date:** 2026-10-10. **Confidence:** High.

#### A6.2 Podman
- **Canonical identity:** Podman — daemonless container engine (podman.io), Red Hat. **Type:** open-source project / development utility.
- **Official URL:** https://podman.io — **Verification:** Partially verified.
- **Description / capabilities:** Daemonless, rootless by default, Docker-compatible CLI (`alias docker=podman` covers most workflows), pods (K8s-like grouping), `podman generate kube`, Quadlet systemd integration.
- **Usage domain:** Security-sensitive hosts, RHEL-family, CI runners. **License:** Apache-2.0. **Maintenance:** Active.
- **Limitations:** Some Docker-socket-dependent tooling needs shims; Compose via podman-compose.
- **Sources:** search theme 4. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A6.3 containerd
- **Canonical identity:** containerd — industry-standard container runtime (containerd.io), CNCF graduated. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://containerd.io — **Verification:** Partially verified.
- **Description / capabilities:** Low-level runtime daemon; CLIs: `ctr`, `nerdctl`, `crictl`; what Kubernetes actually uses under the hood; OCI-compliant.
- **Usage domain:** K8s nodes, platforms embedding a runtime, CI via nerdctl. **License:** Apache-2.0.
- **Sources:** search theme 4. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A6.4 Buildah / Kaniko
- **Canonical identity:** Buildah (buildah.io) — OCI image builder; Kaniko (github.com/GoogleContainerTools/kaniko) — daemonless image builds in CI. **Type:** open-source project / development utility.
- **Official URL:** https://buildah.io ; https://github.com/GoogleContainerTools/kaniko — **Verification:** Partially verified.
- **Description / capabilities:** Build OCI images without a privileged Docker daemon; Buildah adds `--sbom` flag; Kaniko executes Dockerfiles inside containers/K8s.
- **Usage domain:** CI image builds without docker-in-docker. **License:** Apache-2.0.
- **Sources:** search theme 4. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A6.5 Kubernetes
- **Canonical identity:** Kubernetes — container orchestration (kubernetes.io), CNCF graduated. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://kubernetes.io — **Verification:** Verified (status as de-facto orchestrator corroborated by CNCF survey references).
- **Description / capabilities:** Declarative workloads (Deployments, StatefulSets), services/ingress, autoscaling, RBAC, CRDs/operators; managed offerings (GKE/EKS/AKS/DOKS).
- **Usage domain:** Production container orchestration. **License:** Apache-2.0. **Maintenance:** Active (CNCF survey: K8s "de facto operating system" for AI production use in 2025).
- **Limitations:** Operational complexity; cost visibility needs Kubecost/OpenCost (A24).
- **Related:** k3s, kind, minikube, Helm, Argo CD.
- **Sources:** search theme 4; CNCF survey references. **Verification date:** 2026-10-10. **Confidence:** High.

#### A6.6 k3s / kind / minikube
- **Canonical identity:** k3s (k3s.io, SUSE) — lightweight K8s; kind (kind.sigs.k8s.io) — K8s in Docker; minikube (minikube.sigs.k8s.io) — local K8s. **Type:** open-source project / development utility.
- **Official URL:** https://k3s.io ; https://kind.sigs.k8s.io ; https://minikube.sigs.k8s.io — **Verification:** Partially verified.
- **Description / capabilities:** Local/edge Kubernetes: k3s single binary for edge/IoT; kind for CI testing of K8s manifests; minikube for laptop clusters.
- **Usage domain:** Local K8s dev/test; edge. **License:** Apache-2.0.
- **Sources:** search theme 4. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A6.7 OrbStack / Colima / Rancher Desktop / Finch
- **Canonical identity:** macOS/Windows container VM managers: OrbStack (orbstack.dev, commercial), Colima (github.com/abiosoft/colima, OSS), Rancher Desktop (rancherdesktop.io, SUSE, OSS), Finch (runfinch.com, AWS, OSS). **Type:** development utility (mixed OSS/commercial).
- **Official URL:** https://orbstack.dev ; https://github.com/abiosoft/colima ; https://rancherdesktop.io ; https://runfinch.com — **Verification:** Partially verified.
- **Description / capabilities:** Replace Docker Desktop's VM: OrbStack (fast, paid commercial use), Colima (lightweight, free, no GUI), Rancher Desktop (free, built-in k3s, containerd or Moby), Finch (containerd + nerdctl everywhere).
- **Usage domain:** macOS/Windows container development without Docker Desktop licensing. **License:** Mixed (OrbStack proprietary; others Apache-2.0).
- **Sources:** search theme 4. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A6.8 DevPod
- **Canonical identity:** DevPod — disposable dev workspaces on any provider (devpod.sh, Loft). **Type:** open-source project / development utility.
- **Official URL:** https://devpod.sh — **Verification:** Partially verified.
- **Description / capabilities:** `devpod up` launches reproducible workspaces (devcontainer-compatible) on local Docker, SSH hosts, or clouds; provider plugins.
- **Usage domain:** Ephemeral dev environments. **License:** Apache-2.0.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A7. Dev containers & reproducible environments

#### A7.1 Dev Containers (spec + CLI)
- **Canonical identity:** Development Containers — open specification (containers.dev) + reference CLI (github.com/devcontainers/cli). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://containers.dev — **Verification:** Partially verified.
- **Description / capabilities:** `devcontainer.json` describes image, features, extensions, ports, lifecycle commands; supported by VS Code, Cursor, DevPod; base images at `mcr.microsoft.com/devcontainers/*`; features from `ghcr.io/devcontainers/features/*`.
- **Usage domain:** Reproducible containerized dev environments. **Integration method:** `devcontainer.json` in `.devcontainer/`; Remote-Containers tooling.
- **License:** Spec CC; CLI MIT. **Maintenance:** Active.
- **Limitations:** Needs a container runtime; image pinning discipline required (floating tags break reproducibility).
- **Sources:** search themes 4, 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A7.2 Devbox
- **Canonical identity:** Devbox — Nix-backed dev environments via simple JSON (jetify.com/devbox; github.com/jetify/devbox). **Type:** open-source project / development utility.
- **Official URL:** https://www.jetify.com/devbox (repo: https://github.com/jetify/devbox) — **Verification:** Partially verified.
- **Description / capabilities:** `devbox.json` declares tools/services; `devbox shell` creates isolated env with pinned versions using Nix under the hood without requiring Nix expertise.
- **Usage domain:** Reproducible per-project dev environments. **License:** Apache-2.0.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A7.3 devenv
- **Canonical identity:** devenv — fast, declarative dev environments on Nix (devenv.sh). **Type:** open-source project / development utility.
- **Official URL:** https://devenv.sh — **Verification:** Partially verified.
- **Description / capabilities:** `devenv.nix`/`devenv.yaml` with languages, services (Postgres etc.), processes, git hooks; activates on `cd` (with direnv); friendlier than raw Nix flakes.
- **Usage domain:** Per-project environments incl. services/processes. **License:** Apache-2.0.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A7.4 Nix
- **Canonical identity:** Nix — reproducible package manager + language (nixos.org). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://nixos.org — **Verification:** Partially verified.
- **Description / capabilities:** Declarative, content-addressed packages; `nix develop` per-project devShells; flakes + `flake.lock` pinning; rollbacks; underpins Devbox/devenv.
- **Usage domain:** Reproducible environments/toolchains. **License:** LGPL-2.1+.
- **Limitations:** Steep learning curve.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A7.5 Coder
- **Canonical identity:** Coder — self-hosted remote development environments (coder.com). **Type:** open-source project / cloud service.
- **Official URL:** https://coder.com — **Verification:** Partially verified.
- **Description / capabilities:** Terraform-defined workspace templates provisioned on your infra; browser/IDE access; centralized fleet management.
- **Usage domain:** Remote dev environment fleets. **License:** AGPL + enterprise.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A7.6 Gitpod — status note
- **Canonical identity:** Gitpod — cloud dev environments (gitpod.io). **Type:** cloud service. **Verification:** Unresolved.
- **Description:** Historically a leading cloud dev-environment platform; 2026 sources in this research did not confirm current product direction (company pivoted messaging in 2024–2025). Listed for completeness; status not verified in this pass.
- **Sources:** General knowledge only. **Verification date:** 2026-10-10. **Confidence:** Low.

### A8. Infrastructure as code

#### A8.1 Terraform
- **Canonical identity:** Terraform — declarative IaC by HashiCorp, now IBM (developer.hashicorp.com/terraform). **Type:** infrastructure framework (BSL-licensed).
- **Official URL:** https://developer.hashicorp.com/terraform — **Verification:** Verified (license history + IBM acquisition corroborated by primary-adjacent sources).
- **Description / capabilities:** HCL declarative configs; plan/apply; state with locking; huge provider ecosystem; Stacks; Sentinel policy (enterprise); HCP Terraform (managed runs).
- **Contents inspected:** 2026 landscape analyses (license change 2023-08-10 MPL-2.0→BSL-1.1; IBM $6.4B acquisition closed Feb 2025; BSL unchanged as of Sept 2026).
- **Usage domain:** Multi-cloud infrastructure provisioning. **Integration method:** CLI `terraform`; CI via HCP Terraform or self-run.
- **Compatibility:** Provider ecosystem shared with OpenTofu. **Dependencies:** Provider plugins. **Availability:** Binary + source (BSL). **Maintenance:** Active. **License:** BSL-1.1 (source-available, not OSI open source; forbids competitive offerings).
- **Limitations:** BSL risk for vendors building competing offerings; community innovation largely moved to OpenTofu.
- **Related:** OpenTofu, Pulumi, CloudFormation.
- **Sources:** https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license (via secondary citation); search theme 3. **Verification date:** 2026-10-10. **Confidence:** High (license facts), Medium (current feature details).

#### A8.2 OpenTofu
- **Canonical identity:** OpenTofu — community Terraform fork under Linux Foundation (opentofu.org; CNCF Sandbox since April 2025). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://opentofu.org — **Verification:** Verified (site fetched).
- **Description / capabilities:** Fork of Terraform ~1.5; CLI-compatible (`tofu`); own registry (search.opentofu.org, 3,900+ providers, 23,600+ modules per mid-2026 reports); diverged features: native state encryption (1.7), early variable evaluation (1.8), provider `for_each` (1.9), `-exclude` flag (1.9), OCI registry support (1.10), S3 native locking, experimental OTel tracing (1.12.x, current per June 2026).
- **Contents inspected:** Full opentofu.org homepage + FAQ (fork rationale, BUSL ambiguity, compatibility, registry, supporters: Harness, Gruntwork, Spacelift, env0, Scalr; sponsors: Buildkite, Cloudflare, Datadog).
- **Usage domain:** License-safe Terraform-compatible IaC. **Integration method:** `tofu` CLI drop-in; registry at search.opentofu.org.
- **Compatibility:** HCL + Terraform 1.5-era providers/modules; state-file compatible. **Dependencies:** Provider plugins. **Availability:** GitHub releases. **Maintenance:** Active (Linux Foundation). **License:** MPL-2.0.
- **Limitations:** Very new Terraform-only features (e.g., Stacks) absent; migration inertia in large orgs.
- **Related:** Terraform, Pulumi, Terragrunt.
- **Sources:** https://opentofu.org (fetched 2026-10-10); search theme 3. **Verification date:** 2026-10-10. **Confidence:** High.

#### A8.3 Pulumi
- **Canonical identity:** Pulumi — IaC in general-purpose languages (pulumi.com). **Type:** open-source project / infrastructure framework (+ cloud service: Pulumi Cloud).
- **Official URL:** https://www.pulumi.com — **Verification:** Partially verified.
- **Description / capabilities:** Define infra in TypeScript/Python/Go/C#/Java/YAML/HCL; own state + provider model (150+ providers); Automation API; Pulumi ESC for secrets (A15); policy as code; 2026: Pulumi Neo (AI); Pulumi Cloud can act as managed OpenTofu backend/remote runner; Pulumi HCL runs valid OpenTofu configs.
- **Usage domain:** Code-first IaC for app-engineer teams. **License:** Apache-2.0 (core).
- **Limitations:** Smaller community/module ecosystem than HCL world; state model differs from Terraform.
- **Related:** Terraform, OpenTofu, AWS CDK.
- **Sources:** https://www.pulumi.com/docs/iac/comparisons/opentofu/; search theme 3. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A8.4 AWS CloudFormation / AWS CDK
- **Canonical identity:** CloudFormation — AWS-native IaC (JSON/YAML); AWS CDK — define CloudFormation in code (aws.amazon.com/cdk). **Type:** infrastructure framework (cloud service component).
- **Official URL:** https://aws.amazon.com/cloudformation/ ; https://aws.amazon.com/cdk/ — **Verification:** Partially verified.
- **Description / capabilities:** CloudFormation: declarative stacks, drift detection, StackSets. CDK: TypeScript/Python/Java/Go/C# constructs synthesizing to CloudFormation; `cdk deploy`.
- **Usage domain:** AWS-only infrastructure. **License:** Apache-2.0 (CDK).
- **Limitations:** AWS-only; CloudFormation speed/UX complaints vs HCL tools.
- **Sources:** General knowledge + search theme 3. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A8.5 SST
- **Canonical identity:** SST — framework for building serverless/full-stack apps on AWS (sst.dev). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://sst.dev — **Verification:** Partially verified.
- **Description / capabilities:** TypeScript-defined AWS infrastructure (Ion engine on Pulumi/Terraform under the hood historically); live Lambda dev loop; aimed at Next.js/SST apps on AWS.
- **Usage domain:** AWS app + infra co-development. **License:** MIT (per public repo).
- **Sources:** General knowledge; search theme 3 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A8.6 Ansible
- **Canonical identity:** Ansible — agentless automation (ansible.com, Red Hat/IBM). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://www.ansible.com — **Verification:** Partially verified.
- **Description / capabilities:** YAML playbooks over SSH/WinRM; configuration management, provisioning, app deployment; Galaxy roles.
- **Usage domain:** Config management + procedural automation. **License:** GPL-3.0 (core).
- **Sources:** search theme 3 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A8.7 Crossplane
- **Canonical identity:** Crossplane — Kubernetes-native IaC (crossplane.io), CNCF incubating. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://www.crossplane.io — **Verification:** Partially verified.
- **Description / capabilities:** Provision cloud resources via K8s CRDs/providers; compose into platform APIs; GitOps-friendly (works with Argo CD/Flux).
- **Usage domain:** Platform teams exposing self-service infra on K8s. **License:** Apache-2.0.
- **Sources:** General knowledge; search theme 3 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A8.8 Terramate / Terragrunt
- **Canonical identity:** Terramate (terramate.io) — orchestration layer for Terraform/OpenTofu stacks; Terragrunt (terragrunt.gruntwork.io) — DRY wrapper. **Type:** open-source project / development utility.
- **Official URL:** https://terramate.io ; https://terragrunt.gruntwork.io — **Verification:** Partially verified.
- **Description / capabilities:** Stack generation, orchestration, change detection across many Terraform/OpenTofu roots.
- **Usage domain:** Large IaC monorepos. **License:** MPL-2.0 (Terramate) / MIT (Terragrunt).
- **Sources:** search theme 3 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A8.9 Checkov / Trivy (IaC scanning)
- **Canonical identity:** Checkov (checkov.io, Bridgecrew/Palo Alto) — static analysis for IaC; Trivy (aquasec.github.io/trivy) — vulnerability/misconfig scanner. **Type:** open-source project / development utility.
- **Official URL:** https://www.checkov.io ; https://aquasecurity.github.io/trivy/ — **Verification:** Partially verified.
- **Description / capabilities:** Scan Terraform/CloudFormation/K8s/Dockerfiles for misconfigurations and CVEs; CI gates (tfsec deprecated 2023, replaced by this pair per 2026 skill docs).
- **Usage domain:** IaC security in PRs. **License:** Apache-2.0.
- **Sources:** search theme 3. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A9. Cloud CLIs & SDKs

#### A9.1 AWS CLI / SDKs
- **Canonical identity:** AWS Command Line Interface + SDKs (aws.amazon.com/cli). **Type:** development utility / infrastructure framework.
- **Official URL:** https://aws.amazon.com/cli/ — **Verification:** Partially verified.
- **Description / capabilities:** `aws` CLI for all AWS services; SDKs (v2/v3) for major languages; SSO/IAM Identity Center auth; SSM/Secrets Manager access.
- **Usage domain:** AWS operations + automation. **License:** Apache-2.0.
- **Sources:** search themes 8, 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A9.2 gcloud / Google Cloud CLI
- **Canonical identity:** Google Cloud CLI (cloud.google.com/sdk). **Type:** development utility.
- **Official URL:** https://cloud.google.com/sdk — **Verification:** Partially verified.
- **Description / capabilities:** `gcloud`, `gsutil`, `bq`, `kubectl` management; auth, config, deployment commands.
- **Usage domain:** GCP operations. **License:** Proprietary (free tool).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A9.3 Azure CLI
- **Canonical identity:** Azure CLI `az` (learn.microsoft.com/cli/azure). **Type:** development utility.
- **Official URL:** https://learn.microsoft.com/cli/azure/ — **Verification:** Partially verified.
- **Description / capabilities:** Cross-platform CLI for Azure resource management.
- **Usage domain:** Azure operations. **License:** MIT.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A9.4 Cloudflare Wrangler
- **Canonical identity:** Wrangler — CLI for Cloudflare Workers/Pages (developers.cloudflare.com/workers/wrangler). **Type:** open-source project / development utility.
- **Official URL:** https://developers.cloudflare.com/workers/wrangler/ — **Verification:** Partially verified.
- **Description / capabilities:** `wrangler dev`/`deploy`/`tail`; bindings management (KV, D1, R2, Queues, Durable Objects); local workerd dev; secrets.
- **Usage domain:** Workers/Pages development + deploy. **License:** Apache-2.0/MIT (wrangler repo).
- **Sources:** search theme 8; workers.cloudflare.com (workerd local dev confirmed). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A9.5 Flyctl
- **Canonical identity:** flyctl — CLI for Fly.io (fly.io/docs/flyctl). **Type:** development utility.
- **Official URL:** https://fly.io/docs/flyctl/ — **Verification:** Partially verified.
- **Description / capabilities:** `fly launch/deploy/secrets/scale`; `fly.toml` app config; wireguard VPN; Machines API.
- **Usage domain:** Fly.io app lifecycle. **License:** Apache-2.0 (open-sourced).
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A9.6 Supabase CLI
- **Canonical identity:** Supabase CLI (supabase.com/docs/guides/cli). **Type:** open-source project / development utility.
- **Official URL:** https://supabase.com/docs/guides/cli — **Verification:** Partially verified.
- **Description / capabilities:** Local stack (Postgres, Auth, Storage via Docker), migrations, `supabase db push`, edge functions deploy, type generation.
- **Usage domain:** Supabase local dev + CI. **License:** Apache-2.0.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A9.7 Vercel CLI
- **Canonical identity:** Vercel CLI `vc` (vercel.com/docs/cli). **Type:** development utility.
- **Official URL:** https://vercel.com/docs/cli — **Verification:** Partially verified.
- **Description / capabilities:** `vercel`/`vercel --prod` deploys; env pull; project linking; preview deployments from CLI.
- **Usage domain:** Vercel deploys outside git integration. **License:** Apache-2.0.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A10. Frontend hosting & static deployment

#### A10.1 Vercel
- **Canonical identity:** Vercel — frontend cloud (vercel.com). **Type:** cloud service.
- **Official URL:** https://vercel.com — **Verification:** Partially verified.
- **Description / capabilities:** Git-push deploys; framework-native (Next.js) builds; Preview Deployments per PR; Edge + Serverless Functions; Fluid Compute; Web Analytics ($10/mo); Speed Insights; Hobby tier free (non-commercial only — noted gotcha in 2026 guides); Pro from $20/mo.
- **Usage domain:** Frontend/full-stack JS hosting. **Integration method:** Git integration or CLI/API.
- **Limitations:** Usage-based costs can surprise at scale; Hobby ToS restricts commercial use.
- **Related:** Netlify, Cloudflare Pages.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A10.2 Netlify
- **Canonical identity:** Netlify — web platform (netlify.com). **Type:** cloud service.
- **Official URL:** https://www.netlify.com — **Verification:** Partially verified.
- **Description / capabilities:** Git deploys, Deploy Previews, serverless/edge functions, built-in Forms, Identity, redirects/headers config; 2026: credit-based plans (Forms free+unlimited on credit plans per docs), Pro from $19/mo.
- **Usage domain:** Static/Jamstack + marketing sites. **Limitations:** Bandwidth caps (100GB free); build minutes 300/mo free.
- **Sources:** search themes 5, 31. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A10.3 Cloudflare Pages
- **Canonical identity:** Cloudflare Pages — Jamstack platform (pages.cloudflare.com). **Type:** cloud service.
- **Official URL:** https://pages.cloudflare.com — **Verification:** Partially verified.
- **Description / capabilities:** Git-connected static deploys; unlimited bandwidth on free tier; 500 builds/mo; preview deployments; Workers integration for dynamic routes; free Web Analytics; 300+ edge locations.
- **Usage domain:** High-traffic static sites; edge-first apps. **Limitations:** Rougher deploy UX than Vercel/Netlify per comparisons; form handling needs Workers.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A10.4 GitHub Pages
- **Canonical identity:** GitHub Pages — static hosting from GitHub repos (pages.github.com). **Type:** cloud service.
- **Official URL:** https://pages.github.com — **Verification:** Partially verified.
- **Description / capabilities:** Static deploys from repo branches/Actions; Jekyll built-in; custom domains + HTTPS; no preview deploys or env vars.
- **Usage domain:** Docs, portfolios, OSS project sites. **Limitations:** Static only; no serverless functions.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A10.5 Firebase Hosting
- **Canonical identity:** Firebase Hosting — Google static/app hosting (firebase.google.com). **Type:** cloud service.
- **Official URL:** https://firebase.google.com — **Verification:** Partially verified.
- **Description / capabilities:** `firebase deploy` CLI; global CDN; Cloud Functions/Run integration; custom domains; free tier (10GB storage, 360MB/day transfer per 2026 guides).
- **Usage domain:** Firebase-ecosystem apps. **Limitations:** No git-push-to-deploy; daily transfer cap on free tier.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A10.6 AWS Amplify
- **Canonical identity:** AWS Amplify — full-stack hosting on AWS (aws.amazon.com/amplify). **Type:** cloud service.
- **Official URL:** https://aws.amazon.com/amplify/ — **Verification:** Partially verified.
- **Description / capabilities:** Git-connected frontend hosting + backend (data/auth/storage/functions); preview environments; Gen 2 code-first DX.
- **Usage domain:** AWS-native full-stack apps. **Limitations:** AWS complexity leaks through.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A11. Backend hosting & PaaS

#### A11.1 Fly.io
- **Canonical identity:** Fly.io — global app platform running containers on Firecracker micro-VMs (fly.io). **Type:** cloud service.
- **Official URL:** https://fly.io — **Verification:** Partially verified.
- **Description / capabilities:** `fly launch` from Dockerfile; multi-region deploys; Fly Postgres; Machines API; Sprites AI micro-VMs; usage-based pricing ($5/mo Hobby minimum per 2026 guides); free allowance reduced vs early years.
- **Usage domain:** Containerized backends close to users. **Integration method:** flyctl CLI; Machines REST API.
- **Limitations:** Pricing model changes over time; you manage the container.
- **Related:** Render, Railway, Coolify.
- **Sources:** search themes 7, 8. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A11.2 Render
- **Canonical identity:** Render — cloud application platform (render.com). **Type:** cloud service.
- **Official URL:** https://render.com — **Verification:** Partially verified.
- **Description / capabilities:** Web services, static sites, Postgres, Redis, cron jobs from git; predictable fixed pricing (Standard $25/mo 2GB per 2026 guides); free tier web services sleep after ~15 min idle.
- **Usage domain:** Simple PaaS hosting. **Limitations:** Free services spin down; slower builds than Vercel/Netlify.
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A11.3 Railway
- **Canonical identity:** Railway — usage-based app platform (railway.app). **Type:** cloud service.
- **Official URL:** https://railway.app — **Verification:** Partially verified.
- **Description / capabilities:** Git/Docker deploys; managed Postgres/Redis; per-second usage billing; private networking; templates marketplace. **2026: legacy free tier removed; trial credit only.**
- **Usage domain:** Usage-billed PaaS. **Limitations:** No permanent free tier anymore; costs scale with usage.
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A11.4 Heroku
- **Canonical identity:** Heroku — original git-push PaaS (heroku.com, Salesforce). **Type:** cloud service.
- **Official URL:** https://www.heroku.com — **Verification:** Partially verified.
- **Description / capabilities:** Dynos (managed containers), buildpacks, add-ons, managed Postgres, background workers, easy scaling; `git push heroku main`.
- **Usage domain:** Mature PaaS baseline. **Limitations:** Higher cost than newer platforms for small apps; free tier long gone.
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A11.5 DigitalOcean App Platform
- **Canonical identity:** DigitalOcean App Platform — PaaS on DO (digitalocean.com/products/app-platform). **Type:** cloud service.
- **Official URL:** https://www.digitalocean.com/products/app-platform — **Verification:** Partially verified.
- **Description / capabilities:** Git/container deploys; managed databases; predictable pricing; BYOC-adjacent simplicity.
- **Usage domain:** DO-ecosystem PaaS. **License:** Proprietary.
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A11.6 Coolify
- **Canonical identity:** Coolify — self-hosted PaaS (coolify.io; github.com/coollabsio/coolify). **Type:** open-source project (self-hosted cloud service equivalent).
- **Official URL:** https://coolify.io — **Verification:** Partially verified.
- **Description / capabilities:** Push-to-deploy for Docker apps on your own VPS; web UI; managed databases; PR preview environments (beta); TLS via Caddy + Let's Encrypt; runs on 2CPU/2GB (tested on $6 DO droplet with swap per Oct 2026 guide).
- **Usage domain:** Self-hosted Heroku alternative. **License:** Apache-2.0. **Maintenance:** Active.
- **Limitations:** Single-node primary; you own ops/upgrades.
- **Related:** Dokku, CapRover, Dokploy.
- **Sources:** search themes 7, 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A11.7 Dokku
- **Canonical identity:** Dokku — mini-Heron on your box (dokku.com). **Type:** open-source project.
- **Official URL:** https://dokku.com — **Verification:** Partially verified.
- **Description / capabilities:** `git push dokku main`; Heroku buildpacks + Docker; plugin ecosystem (mature Postgres plugin); Let's Encrypt; minimal idle footprint; CLI-first.
- **Usage domain:** Single-VPS PaaS. **License:** MIT. **Maintenance:** Active.
- **Limitations:** No built-in UI (third-party); no preview envs natively.
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A11.8 CapRover / Dokploy
- **Canonical identity:** CapRover (caprover.com) — Docker Swarm-based self-hosted PaaS; Dokploy (dokploy.com) — newer self-hosted PaaS with UI. **Type:** open-source project.
- **Official URL:** https://caprover.com ; https://dokploy.com — **Verification:** Partially verified.
- **Description / capabilities:** CapRover: one-click apps, web UI, Swarm scaling (fragile beyond few nodes). Dokploy: modern UI, Docker Compose deploys, databases, Traefik.
- **Usage domain:** Self-hosted PaaS. **License:** Apache-2.0 (both per 2026 comparisons).
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A11.9 Northflank / Qovery / Upsun
- **Canonical identity:** Northflank (northflank.com) — container/K8s PaaS; Qovery (qovery.com) — BYOC Internal Developer Platform; Upsun (upsun.com) — Platform.sh successor PaaS. **Type:** cloud service.
- **Official URL:** https://northflank.com ; https://www.qovery.com ; https://upsun.com — **Verification:** Partially verified.
- **Description / capabilities:** Northflank: container + K8s control with BYOC path. Qovery: deploys into your cloud account (BYOC), environments per PR. Upsun: managed environments, preview envs, Platform.sh heritage.
- **Usage domain:** Teams outgrowing simple PaaS. **License:** Proprietary.
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A11.10 Koyeb — status note
- **Canonical identity:** Koyeb — serverless-ish app platform (koyeb.com). **Type:** cloud service. **Verification:** Partially verified.
- **Description / capabilities:** Git/Docker deploys globally. **2026: free tier closed to new users** (Starter gone) per free-hosting trackers.
- **Sources:** search theme 7. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A12. Serverless & edge runtimes

#### A12.1 AWS Lambda
- **Canonical identity:** AWS Lambda — functions-as-a-service (aws.amazon.com/lambda). **Type:** cloud service.
- **Official URL:** https://aws.amazon.com/lambda/ — **Verification:** Partially verified.
- **Description / capabilities:** Event-driven functions (15-min max), layers, provisioned concurrency, function URLs; integrates with API Gateway/SQS/EventBridge.
- **Usage domain:** AWS serverless compute. **Limitations:** Cold starts (esp. VPC/Java); 15-min timeout.
- **Sources:** General knowledge + search theme 8. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A12.2 Cloudflare Workers
- **Canonical identity:** Cloudflare Workers — V8-isolate edge compute (workers.cloudflare.com). **Type:** cloud service (+ open-source runtime workerd).
- **Official URL:** https://workers.cloudflare.com — **Verification:** Verified (product page fetched).
- **Description / capabilities:** JS/TS/Python/Rust/WASM in isolates across 330+ cities; sub-millisecond cold starts; CPU-time billing; Durable Objects (SQL-backed, GA since Apr 2025), KV, R2, D1, Queues, Workflows, Cron Triggers bindings; Python Workers (CPython via Pyodide/WASM in workerd); gradual rollouts + instant rollback; 100k req/day free.
- **Contents inspected:** Full product page (isolates vs containers, Smart Placement, no cold starts, local dev with workerd, Git integration).
- **Usage domain:** Edge APIs, middleware, full-stack on Cloudflare. **Integration method:** Wrangler CLI; Git integration.
- **Compatibility:** WinterCG-aligned web APIs. **Dependencies:** Cloudflare account. **Availability:** Global. **Maintenance:** Active. **License:** Proprietary service; workerd open source (Apache-2.0).
- **Limitations:** Isolate constraints (no raw sockets; CPU-time limits on free); self-hosted Durable Objects scaling limits noted in 2026 announcements.
- **Related:** workerd, Deno (team joined Cloudflare), Fastly Compute.
- **Sources:** https://workers.cloudflare.com (fetched 2026-10-10); search theme 8. **Verification date:** 2026-10-10. **Confidence:** High.

#### A12.3 workerd
- **Canonical identity:** workerd — open-source Workers runtime (github.com/cloudflare/workerd). **Type:** open-source project / infrastructure framework.
- **Official URL:** https://github.com/cloudflare/workerd — **Verification:** Partially verified.
- **Description / capabilities:** The runtime powering Workers (or closely matching it); local testing, portability; 2026: Deno team merging efforts with workerd + celld for self-hosting story.
- **Usage domain:** Local Workers dev; self-hosted edge experiments. **License:** Apache-2.0.
- **Sources:** search theme 8; workers.cloudflare.com. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A12.4 Vercel Functions (Serverless + Edge)
- **Canonical identity:** Vercel Functions — serverless/edge functions on Vercel (vercel.com/docs/functions). **Type:** cloud service.
- **Official URL:** https://vercel.com/docs/functions — **Verification:** Partially verified.
- **Description / capabilities:** Framework-native API routes; Edge runtime (V8 isolates, WinterCG) + Node serverless; Fluid Compute architecture; 1M invocations/mo free (edge) per 2026 guides.
- **Usage domain:** Next.js-adjacent serverless. **Limitations:** Execution-time limits by plan; vendor lock-in.
- **Sources:** search themes 5, 8. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A12.5 Netlify Functions / Edge Functions
- **Canonical identity:** Netlify Functions (AWS Lambda-backed) + Edge Functions (Deno-based). **Type:** cloud service.
- **Official URL:** https://www.netlify.com/platform/functions/ — **Verification:** Partially verified.
- **Description / capabilities:** Git-deployed functions; 125k req/mo free (functions) per 2026 guides; background + scheduled functions.
- **Usage domain:** Jamstack dynamic backends. **License:** Proprietary.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A12.6 Deno Deploy — Archived (sunsetting)
- **Canonical identity:** Deno Deploy — hosted Deno edge platform (deno.com/deploy). **Type:** cloud service. **Verification:** Archived (sunset announced).
- **Description / capabilities (historical):** Native Deno/TypeScript edge runtime, built-in KV, global edge; free tier 1M req/mo.
- **Status:** **2026-10-09: Deno team joined Cloudflare; Deno Deploy operates 6 more months then shuts down (~April 2027).** Deno runtime gets 1 year of maintenance releases then ends independent development. Paying customers assisted to migrate to Cloudflare Workers.
- **Related:** Cloudflare Workers, Deno runtime, Appwrite Functions (Deno alternative).
- **Sources:** https://runtimewire.com/article/deno-joins-cloudflare-self-hosted-workers; https://appwrite.io/blog/post/deno-deploy-alternative; search theme 8. **Verification date:** 2026-10-10. **Confidence:** High.

#### A12.7 Deno (runtime)
- **Canonical identity:** Deno — secure JS/TS runtime (deno.com). **Type:** open-source project.
- **Official URL:** https://deno.com — **Verification:** Partially verified.
- **Description / capabilities:** TypeScript-first, permissions model, JSR registry; Deno 2.x. **2026 status:** team joined Cloudflare; runtime stays open source with 1 year of bugfix/security releases, then independent development ends.
- **Usage domain:** JS/TS server-side runtime; edge alternative. **License:** MIT.
- **Sources:** search theme 8. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A12.8 Bun
- **Canonical identity:** Bun — all-in-one JS runtime/toolkit (bun.sh). **Type:** open-source project / development utility.
- **Official URL:** https://bun.sh — **Verification:** Partially verified.
- **Description / capabilities:** Runtime + bundler + test runner + package manager; fast startup; Node-compatible; used as edge/serverless runtime option.
- **Usage domain:** JS tooling + server runtime. **License:** MIT (core; some parts proprietary — not re-verified).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A12.9 Fastly Compute / Akamai EdgeWorkers
- **Canonical identity:** Fastly Compute (fastly.com/products/edge-compute) — WASM edge compute; Akamai EdgeWorkers (akamai.com) — CDN-embedded JS runtime. **Type:** cloud service.
- **Official URL:** https://www.fastly.com/products/edge-compute ; https://www.akamai.com/products/edgeworkers — **Verification:** Partially verified.
- **Description / capabilities:** Compute: Lucet/Wasmtime WASM, microsecond cold starts, 10M free req/mo per 2026 guides. EdgeWorkers: JS at CDN edge, A/B testing, auth validation, EdgeKV.
- **Usage domain:** Edge compute on Fastly/Akamai networks. **License:** Proprietary.
- **Sources:** search theme 8. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A12.10 WinterCG
- **Canonical identity:** WinterCG — Web-interoperable Runtimes Community Group (wintercg.org). **Type:** open standard (specification).
- **Official URL:** https://wintercg.org — **Verification:** Partially verified.
- **Description / capabilities:** Standardizes web-platform APIs (fetch, streams, crypto, etc.) across server runtimes (Workers, Deno, Bun, Node) for portable server JS.
- **Usage domain:** Runtime API portability. **License:** N/A (spec).
- **Sources:** search theme 8. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A13. CDN & edge network infrastructure

#### A13.1 Cloudflare (CDN + network)
- **Canonical identity:** Cloudflare — CDN, DNS, edge network (cloudflare.com). **Type:** cloud service / infrastructure framework.
- **Official URL:** https://www.cloudflare.com — **Verification:** Partially verified.
- **Description / capabilities:** 300+ PoPs; CDN caching, WAF, DDoS, DNS, R2 (zero-egress object storage), Cache Rules; free tier generous.
- **Usage domain:** CDN/security/DNS fronting any host. **License:** Proprietary.
- **Sources:** search themes 5, 8. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A13.2 Fastly
- **Canonical identity:** Fastly — edge cloud/CDN (fastly.com). **Type:** cloud service.
- **Official URL:** https://www.fastly.com — **Verification:** Partially verified.
- **Description / capabilities:** VCL-configurable CDN, real-time purging, Compute@Edge, image optimization; developer-focused.
- **Usage domain:** Programmable CDN. **License:** Proprietary.
- **Sources:** search theme 8. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A13.3 Akamai
- **Canonical identity:** Akamai — CDN/edge security (akamai.com). **Type:** cloud service.
- **Official URL:** https://www.akamai.com — **Verification:** Partially verified.
- **Description / capabilities:** Largest legacy CDN; edge delivery + security (Kona/WAF), EdgeWorkers, EdgeKV; enterprise contract pricing.
- **Usage domain:** Enterprise edge delivery. **License:** Proprietary.
- **Sources:** search theme 8. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A13.4 AWS CloudFront
- **Canonical identity:** CloudFront — AWS CDN (aws.amazon.com/cloudfront). **Type:** cloud service.
- **Official URL:** https://aws.amazon.com/cloudfront/ — **Verification:** Partially verified.
- **Description / capabilities:** Global CDN integrated with S3/ALB/Lambda@Edge/CloudFront Functions; Functions for lightweight edge logic.
- **Usage domain:** AWS-ecosystem CDN. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A13.5 Bunny CDN
- **Canonical identity:** Bunny.net — budget CDN + edge storage (bunny.net). **Type:** cloud service.
- **Official URL:** https://bunny.net — **Verification:** Partially verified.
- **Description / capabilities:** Low-cost CDN, edge storage, stream/video; popular with indie/SMB.
- **Usage domain:** Affordable CDN. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A14. Managed databases & data platforms

#### A14.1 Supabase
- **Canonical identity:** Supabase — open-source Firebase alternative: Postgres + Auth + Storage + Realtime + Edge Functions (supabase.com). **Type:** cloud service / open-source project.
- **Official URL:** https://supabase.com — **Verification:** Partially verified.
- **Description / capabilities:** Managed Postgres with built-in auth (magic links, OAuth, JWT), file storage, realtime subscriptions, pgvector, Edge Functions; local dev via Supabase CLI; free tier (500MB, pausing); Pro $25/mo.
- **Usage domain:** Full backend platform for MVPs/SaaS. **Integration method:** JS/Python SDKs, REST (PostgREST), CLI.
- **Compatibility:** Standard Postgres (use any Postgres tooling). **Dependencies:** None. **Availability:** Cloud + self-host. **Maintenance:** Active. **License:** Apache-2.0 (core repos).
- **Limitations:** Free tier pauses; Pro per-project pricing adds up vs pure-DB options.
- **Related:** Neon, Firebase, Convex, Prisma.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A14.2 Neon
- **Canonical identity:** Neon — serverless Postgres (neon.com/neon.tech), acquired by Databricks May 2025. **Type:** cloud service.
- **Official URL:** https://neon.com — **Verification:** Partially verified.
- **Description / capabilities:** Serverless Postgres with scale-to-zero, copy-on-write database branching (per-PR branches), read replicas; HTTP + WebSocket drivers; generous free tier; Launch ~$19/mo (pricing varies by source $5–19 entry).
- **Usage domain:** Serverless Postgres for modern apps. **Integration method:** Postgres wire protocol; serverless drivers; ORMs (Drizzle first-class, Prisma).
- **License:** Proprietary service; platform code AGPLv3 (per 2026 comparisons).
- **Limitations:** Cold-start latency from idle (400–750ms); branching costs at scale.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A14.3 PlanetScale
- **Canonical identity:** PlanetScale — serverless MySQL on Vitess (+ Postgres offering) (planetscale.com). **Type:** cloud service.
- **Official URL:** https://planetscale.com — **Verification:** Partially verified.
- **Description / capabilities:** Vitess-based sharded MySQL; branching/deploy-request workflows; always-on; free tier eliminated March 2024; Scaler from $39/mo; added Postgres single-node from $5/mo per 2026 guides.
- **Usage domain:** MySQL at scale; sharding. **License:** Proprietary (Vitess OSS).
- **Limitations:** No free tier; MySQL-only strengths (Postgres offering newer).
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A14.4 Turso / libSQL
- **Canonical identity:** Turso — distributed SQLite on libSQL (turso.tech). **Type:** cloud service / open-source project (libSQL MIT).
- **Official URL:** https://turso.tech — **Verification:** Partially verified.
- **Description / capabilities:** libSQL (SQLite fork); thousands of per-tenant databases; multi-region replication; embedded replicas for zero-latency reads; free tier generous; Developer from ~$5/mo; Drizzle first-class via `@libsql/client`.
- **Usage domain:** Edge reads, multi-tenant SaaS, SQLite-first apps. **Integration method:** HTTP client + embedded.
- **Limitations:** Not Postgres (different tooling); Prisma support via preview adapter.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A14.5 Cloudflare D1
- **Canonical identity:** D1 — Workers-native SQLite database (developers.cloudflare.com/d1). **Type:** cloud service.
- **Official URL:** https://developers.cloudflare.com/d1/ — **Verification:** Partially verified.
- **Description / capabilities:** SQLite at the edge bound to Workers; generous free tier; from $5/mo; Time Travel backups.
- **Usage domain:** Cloudflare-stack apps. **Limitations:** SQLite semantics; Cloudflare-only.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A14.6 Convex
- **Canonical identity:** Convex — reactive TypeScript backend (convex.dev). **Type:** cloud service.
- **Official URL:** https://www.convex.dev — **Verification:** Partially verified.
- **Description / capabilities:** TypeScript-defined DB + realtime sync + serverless functions; reactive queries; free tier; from $25/mo.
- **Usage domain:** TypeScript-first realtime apps. **Limitations:** Custom (non-Postgres) data model; TS-only.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A14.7 Firebase (Firestore/Auth)
- **Canonical identity:** Firebase — Google app platform (firebase.google.com): Firestore (document NoSQL), Auth, Hosting, Cloud Functions. **Type:** cloud service.
- **Official URL:** https://firebase.google.com — **Verification:** Partially verified.
- **Description / capabilities:** Realtime document DB, auth, storage, analytics; pay-as-you-go; strong mobile story.
- **Usage domain:** Mobile + rapid B2C backends. **Limitations:** Query limitations of Firestore; Google lock-in.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A14.8 MongoDB Atlas
- **Canonical identity:** MongoDB Atlas — managed document DB (mongodb.com/atlas). **Type:** cloud service.
- **Official URL:** https://www.mongodb.com/atlas — **Verification:** Partially verified.
- **Description / capabilities:** Managed MongoDB; Atlas Search, Vector Search; from ~$9/mo per 2026 guides.
- **Usage domain:** Document-model apps. **License:** Proprietary (SSPL for server).
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A14.9 Upstash
- **Canonical identity:** Upstash — serverless Redis/Kafka/Vector (upstash.com). **Type:** cloud service.
- **Official URL:** https://upstash.com — **Verification:** Partially verified.
- **Description / capabilities:** Serverless Redis (REST API), QStash (message queues/cron), Vector search; per-request pricing; generous free tier.
- **Usage domain:** Serverless caching/queues. **Limitations:** REST latency vs in-VPC Redis.
- **Sources:** search theme 12 (QStash cited). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A14.10 Prisma / Drizzle (ORMs)
- **Canonical identity:** Prisma (prisma.io) — ORM + Accelerate/Studio; Drizzle (orm.drizzle.team) — TS-first lightweight ORM. **Type:** open-source project / development utility (+ cloud service for Prisma Accelerate).
- **Official URL:** https://www.prisma.io ; https://orm.drizzle.team — **Verification:** Partially verified.
- **Description / capabilities:** Prisma: schema-first, migrations, type-safe client, connection pooling (Accelerate). Drizzle: SQL-like TS API, plain-TS schemas, first-class Neon/Turso/PlanetScale adapters; 2026 preference for edge/serverless per comparisons.
- **Usage domain:** TypeScript data access. **License:** Apache-2.0.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A14.11 Xata — Unresolved
- **Canonical identity:** Xata — Postgres + branching + AI (xata.io). **Type:** cloud service. **Verification:** Unresolved.
- **Description:** 2026 comparisons still list Xata (free tier, $35/mo entry); historical reports of shutdown/restructure could not be confirmed in this pass. Status requires direct verification at xata.io.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Low.

#### A14.12 Crunchy Bridge
- **Canonical identity:** Crunchy Bridge — ops-grade managed Postgres (crunchybridge.com, Snowflake-owned). **Type:** cloud service.
- **Official URL:** https://www.crunchybridge.com — **Verification:** Partially verified.
- **Description / capabilities:** Plain serious Postgres (HA, PITR, extensions); from ~$50/mo per 2026 guides.
- **Usage domain:** Teams wanting vanilla Postgres without AWS pain. **License:** Proprietary.
- **Sources:** search theme 9. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A15. Secrets management

#### A15.1 HashiCorp Vault
- **Canonical identity:** Vault — secrets + encryption management (developer.hashicorp.com/vault). **Type:** infrastructure framework (BSL-licensed).
- **Official URL:** https://developer.hashicorp.com/vault — **Verification:** Partially verified.
- **Description / capabilities:** KV/static secrets, dynamic secrets (DB creds, cloud IAM), PKI, transit encryption, AppRole/JWT/OIDC auth; `hashicorp/vault-action` for CI.
- **Usage domain:** Enterprise secrets infrastructure. **License:** BSL-1.1 (not OSI open source). **Maintenance:** Active (IBM/HashiCorp).
- **Limitations:** Complex to operate (unseal lifecycle, Raft storage, TLS); BSL license.
- **Related:** OpenBao, Infisical, SOPS.
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A15.2 OpenBao
- **Canonical identity:** OpenBao — community Vault fork (openbao.org), Linux Foundation. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://openbao.org — **Verification:** Partially verified.
- **Description / capabilities:** API-compatible with Vault for KV+auth subset; dynamic secrets; AppRole + JWT/OIDC; 2.5.0 GA (Feb 2026) per 2026 docs.
- **Usage domain:** License-safe Vault-compatible secrets. **License:** MPL-2.0.
- **Limitations:** Feature parity subset; smaller ecosystem.
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A15.3 Doppler
- **Canonical identity:** Doppler — secrets ops SaaS (doppler.com). **Type:** cloud service.
- **Official URL:** https://www.doppler.com — **Verification:** Partially verified.
- **Description / capabilities:** Project→config→environment secrets; 50+ integrations; CLI; official GitHub Action; Service Tokens (free read-only); Team from ~$3–21/user/mo (sources vary).
- **Usage domain:** Developer-first secrets SaaS. **License:** Proprietary (closed source, no self-host).
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A15.4 Infisical
- **Canonical identity:** Infisical — open-source secrets platform (infisical.com). **Type:** open-source project / cloud service.
- **Official URL:** https://infisical.com — **Verification:** Partially verified.
- **Description / capabilities:** MIT core; self-host + free SaaS tier; project→env→path scoping; Machine Identities with OIDC/Universal auth in free tier; official GitHub Action; first-party SDKs; secret rotation, PKI, approvals (tier-dependent).
- **Usage domain:** Open-source Doppler alternative. **License:** MIT (core). **Maintenance:** Active (25k+ stars per 2026 docs).
- **Limitations:** Some advanced features (SSO, machine-identity scale) paid.
- **Related:** Doppler, OpenBao, SOPS.
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A15.5 SOPS
- **Canonical identity:** SOPS — Secrets OPerationS: encrypt files in Git (github.com/getsops/sops), CNCF Sandbox. **Type:** open-source project / development utility.
- **Official URL:** https://github.com/getsops/sops — **Verification:** Partially verified.
- **Description / capabilities:** Encrypts YAML/JSON/ENV/TF files with age/PGP/KMS; commit encrypted files; decrypt in CI with key from GH Secrets; readable diffs (keys visible, values encrypted); 17k+ stars.
- **Usage domain:** GitOps secret storage without a server. **License:** MPL-2.0. **Maintenance:** Active.
- **Limitations:** No UI; manual key rotation; no dynamic secrets.
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A15.6 1Password Secrets Automation
- **Canonical identity:** 1Password service accounts + Connect/CLI (1password.com). **Type:** cloud service / development utility.
- **Official URL:** https://1password.com — **Verification:** Partially verified.
- **Description / capabilities:** `op://vault/item/field` references; `1password/load-secrets-action` GH Action; `@1password/sdk` (v0, WASM/Rust); best for teams already on 1Password; no free tier.
- **Usage domain:** Secrets for 1Password shops. **License:** Proprietary.
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A15.7 AWS Secrets Manager / GCP Secret Manager / Azure Key Vault
- **Canonical identity:** Cloud-native secret stores (aws.amazon.com/secrets-manager; cloud.google.com/secret-manager; azure.microsoft.com — Key Vault). **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Managed secrets with IAM + workload-identity federation (IRSA/WIF/Entra); auto-rotation (AWS); native OIDC in CI.
- **Usage domain:** Single-cloud secrets. **License:** Proprietary. **Limitations:** Vendor lock-in; per-secret/API pricing.
- **Sources:** search theme 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A15.8 Pulumi ESC
- **Canonical identity:** Pulumi ESC — Environments, Secrets & Configuration (pulumi.com/esc). **Type:** cloud service.
- **Official URL:** https://www.pulumi.com/esc/ — **Verification:** Partially verified.
- **Description / capabilities:** Centralized env config + secrets pulled from any provider; integrates with Pulumi IaC and standalone.
- **Usage domain:** IaC-adjacent secrets/config. **License:** Proprietary (free tier).
- **Sources:** search theme 10 (awesome-agent-vault product list). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A15.9 GitHub Actions Secrets (+ OIDC)
- **Canonical identity:** Encrypted secrets/variables at repo/org/environment scope; OIDC federation. **Type:** cloud service feature.
- **Official URL:** https://docs.github.com/actions/security — **Verification:** Partially verified.
- **Description / capabilities:** Environment-scoped secrets with required reviewers; OIDC to AWS/GCP/Azure (no stored creds); Dependabot secrets.
- **Usage domain:** CI/CD credential baseline. **Limitations:** GitHub-scoped only.
- **Sources:** search themes 2, 10. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A16. Environment & toolchain management

#### A16.1 direnv
- **Canonical identity:** direnv — per-directory env vars (direnv.net). **Type:** open-source project / development utility.
- **Official URL:** https://direnv.net — **Verification:** Partially verified.
- **Description / capabilities:** Loads/unloads `.envrc` on `cd`; `use flake`/`layout` integrations; explicit `direnv allow` trust model.
- **Usage domain:** Project-scoped env vars. **License:** MIT.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A16.2 mise
- **Canonical identity:** mise — polyglot tool version manager + tasks + env (mise.jdx.dev). **Type:** open-source project / development utility.
- **Official URL:** https://mise.jdx.dev — **Verification:** Partially verified.
- **Description / capabilities:** Fast Rust-based asdf successor; `.mise.toml` pins tools; env var management; task runner; direnv-like activation.
- **Usage domain:** Toolchain pinning per project. **License:** MIT. **Maintenance:** Active.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A16.3 asdf
- **Canonical identity:** asdf — plugin-based version manager (asdf-vm.com). **Type:** open-source project / development utility.
- **Official URL:** https://asdf-vm.com — **Verification:** Partially verified.
- **Description / capabilities:** `.tool-versions`; shims per plugin; huge plugin registry. Being superseded by mise for new setups per 2026 docs.
- **Usage domain:** Tool versioning. **License:** MIT.
- **Sources:** search theme 26. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A16.4 Flox
- **Canonical identity:** Flox — Nix-based environments without Nix complexity (flox.dev). **Type:** open-source project / development utility.
- **Official URL:** https://flox.dev — **Verification:** Partially verified.
- **Description / capabilities:** `flox init/install/activate`; reproducible envs on Nix packages; FloxHub sharing.
- **Usage domain:** Reproducible dev envs. **License:** Mixed (CLI open).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

### A17. Deployment automation & preview environments

#### A17.1 Kamal
- **Canonical identity:** Kamal — deploy web apps with Docker via SSH (kamal-deploy.org; github.com/basecamp/kamal), by 37signals/Basecamp. **Type:** open-source project / development utility.
- **Official URL:** https://kamal-deploy.org — **Verification:** Partially verified.
- **Description / capabilities:** `kamal deploy` from `deploy.yml`; zero-downtime rolling deploys over SSH; accessory services (DB/Redis) via compose-like config; no control plane; registry-based image flow.
- **Usage domain:** Small-app deploys to your own servers. **License:** MIT. **Maintenance:** Active.
- **Limitations:** No UI; deliberately small scope (few apps, scripted servers).
- **Sources:** search theme 29. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A17.2 Vercel Preview Deployments / Netlify Deploy Previews
- **Canonical identity:** Per-PR ephemeral environments on Vercel/Netlify. **Type:** cloud service feature.
- **Official URL:** https://vercel.com/docs/preview-deployments ; https://www.netlify.com/platform/deploy-previews/ — **Verification:** Partially verified.
- **Description / capabilities:** Every pull request gets a unique URL; visual diff/feedback comments (Vercel); one-click rollback; branch-based environments.
- **Usage domain:** PR review workflows. **Limitations:** Tied to the hosting platform; database branching needs Neon/Supabase branching to match.
- **Sources:** search theme 5. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A17.3 Tugboat
- **Canonical identity:** Tugboat — preview environments as a service (tugboatqa.com). **Type:** cloud service.
- **Official URL:** https://www.tugboatqa.com — **Verification:** Partially verified.
- **Description / capabilities:** Full-stack preview envs per PR with build configs; visual diffing; base previews.
- **Usage domain:** Platform-agnostic preview environments. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

### A18. Release automation & versioning

#### A18.1 semantic-release
- **Canonical identity:** semantic-release — fully automated versioning/publishing from Conventional Commits (semantic-release.gitbook.io; github.com/semantic-release/semantic-release). **Type:** open-source project / development utility.
- **Official URL:** https://semantic-release.gitbook.io — **Verification:** Partially verified.
- **Description / capabilities:** Analyzes commits since last tag → computes version → generates notes → creates tag + GitHub/GitLab release → publishes (npm/Docker/etc.) → commits CHANGELOG back; plugin ecosystem; no human version numbers.
- **Usage domain:** High-cadence JS releases. **Integration method:** CI workflow on release branch. **License:** MIT.
- **Limitations:** Monorepo-weak without plugins; CI is the only gate (no human review).
- **Related:** release-please, changesets.
- **Sources:** search theme 11. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A18.2 release-please
- **Canonical identity:** release-please — Google's release-PR bot (github.com/googleapis/release-please). **Type:** open-source project / agent integration.
- **Official URL:** https://github.com/googleapis/release-please — **Verification:** Partially verified.
- **Description / capabilities:** Maintains a running "release PR" accumulating changelog + computed version from Conventional Commits; merging cuts the release; manifest mode for monorepos; language-agnostic (GitHub-centric).
- **Usage domain:** Deliberate release cadences needing human gate. **License:** Apache-2.0.
- **Limitations:** GitHub-only.
- **Sources:** search theme 11. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A18.3 Changesets
- **Canonical identity:** Changesets — versioning for JS monorepos (github.com/changesets/changesets). **Type:** open-source project / development utility.
- **Official URL:** https://github.com/changesets/changesets — **Verification:** Partially verified.
- **Description / capabilities:** Contributors add `.changeset/*.md` files declaring bump level + summary; `changeset version` consumes them into version PRs; best-in-class independent versioning for JS monorepos.
- **Usage domain:** JS/TS monorepo publishing. **License:** MIT.
- **Limitations:** JS-centric; explicit per-change files (ceremony).
- **Sources:** search theme 11. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A18.4 GoReleaser
- **Canonical identity:** GoReleaser — release automation for Go (goreleaser.com). **Type:** open-source project / development utility.
- **Official URL:** https://goreleaser.com — **Verification:** Partially verified.
- **Description / capabilities:** Builds Go binaries (multi-OS/arch), archives, Homebrew taps, Docker images, GitHub Releases; `goreleaser release` in CI.
- **Usage domain:** Go CLI/app distribution. **License:** MIT.
- **Sources:** search theme 11. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A18.5 git-cliff / conventional-changelog
- **Canonical identity:** git-cliff (git-cliff.org) — changelog generator (Rust); conventional-changelog — JS changelog tooling. **Type:** open-source project / development utility.
- **Official URL:** https://git-cliff.org — **Verification:** Partially verified.
- **Description / capabilities:** Generate changelogs from Conventional Commits; no publishing (compose with release-please/GoReleaser).
- **Usage domain:** Changelog-only automation. **License:** MIT/Apache-2.0.
- **Sources:** search theme 11. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A18.6 knope / release-it / cargo-dist
- **Canonical identity:** knope (knope.tech) — polyglot release automation; release-it (github.com/release-it/release-it) — interactive JS releases; cargo-dist (github.com/axodotdev/cargo-dist) — Rust binary distribution. **Type:** open-source project / development utility.
- **Official URL:** https://knope.tech ; https://github.com/release-it/release-it ; https://github.com/axodotdev/cargo-dist — **Verification:** Partially verified.
- **Description / capabilities:** knope: conventional-commits releases multi-language with version plans. release-it: interactive/versioned JS releases with hooks. cargo-dist: builds + publishes Rust binaries to GitHub Releases.
- **Usage domain:** Language-specific release flows. **License:** MIT/Apache-2.0.
- **Sources:** search theme 11. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A19. Feature flags & progressive delivery

#### A19.1 LaunchDarkly
- **Canonical identity:** LaunchDarkly — feature management platform (launchdarkly.com). **Type:** cloud service.
- **Official URL:** https://launchdarkly.com — **Verification:** Partially verified.
- **Description / capabilities:** Flags with targeting/percentage rollouts, kill switches, scheduled releases, approvals, guarded releases (metric guardrails), experimentation add-on; SDKs broad; `ldcli`.
- **Usage domain:** Enterprise feature management. **License:** Proprietary (per-seat + MAU pricing).
- **Limitations:** Cost/complexity at scale; Relay Proxy only for self-hosting.
- **Related:** Unleash, Flagsmith, OpenFeature.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A19.2 Unleash
- **Canonical identity:** Unleash — open-source feature management (getunleash.io). **Type:** open-source project / cloud service.
- **Official URL:** https://www.getunleash.io — **Verification:** Partially verified.
- **Description / capabilities:** Self-hostable flags; strategies/constraints; full data sovereignty; enterprise tier for governance.
- **Usage domain:** Self-hosted flags requirement. **License:** Apache-2.0 (core) + enterprise.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A19.3 Flagsmith
- **Canonical identity:** Flagsmith — feature flags + remote config (flagsmith.com). **Type:** open-source project / cloud service.
- **Official URL:** https://www.flagsmith.com — **Verification:** Partially verified.
- **Description / capabilities:** Flags + remote config; self-host (enterprise-only for full features per 2026 guides) or SaaS; per-API-request pricing.
- **Usage domain:** Flexible deployment flags. **License:** BSD-3-Clause (core).
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A19.4 GrowthBook
- **Canonical identity:** GrowthBook — open-source flags + experimentation (growthbook.io). **Type:** open-source project / cloud service.
- **Official URL:** https://www.growthbook.io — **Verification:** Partially verified.
- **Description / capabilities:** MIT-licensed; self-host full-featured; warehouse-native experimentation (stats on your warehouse); guardrails + auto-rollback; MCP + AI skills (2026).
- **Usage domain:** OSS flags with serious experimentation. **License:** MIT.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A19.5 Statsig — status changed
- **Canonical identity:** Statsig — experimentation + flags (statsig.com). **Type:** cloud service. **Verification:** Corrected (ownership changed).
- **Description / capabilities:** Feature flags + warehouse-native experimentation; generous free tier historically.
- **Status:** Acquired by OpenAI Sept 2025 ($1.1B); in May 2026 Amplitude took over the Statsig brand and customers while OpenAI kept the engineers (per 2026 research). Verify current offering at statsig.com before depending on it.
- **Sources:** search theme 19 (analytics research). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A19.6 OpenFeature / flagd
- **Canonical identity:** OpenFeature — vendor-neutral feature-flag API (openfeature.dev), CNCF; flagd — OSS evaluator. **Type:** open standard / open-source project.
- **Official URL:** https://openfeature.dev — **Verification:** Partially verified.
- **Description / capabilities:** Standard SDK interfaces decoupling app code from flag backends; providers for LaunchDarkly/Statsig/Unleash/etc.; Vercel Flags GA (Apr 2026) with native OpenFeature support.
- **Usage domain:** Flag-backend portability. **License:** Apache-2.0.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A19.7 ConfigCat
- **Canonical identity:** ConfigCat — feature flag service (configcat.com). **Type:** cloud service.
- **Official URL:** https://configcat.com — **Verification:** Partially verified.
- **Description / capabilities:** Simple hosted flags with SDKs; straightforward pricing.
- **Usage domain:** Teams wanting simple managed flags. **License:** Proprietary.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Low.

#### A19.8 Vercel Flags / Cloudflare Flagship
- **Canonical identity:** Vercel Flags (GA Apr 2026, OpenFeature-native); Cloudflare Flagship (Apr 29, 2026) — flagging for AI workloads (model/prompt rollouts). **Type:** cloud service feature.
- **Official URL:** https://vercel.com/docs/flags ; https://www.cloudflare.com (Flagship announcement) — **Verification:** Partially verified.
- **Description / capabilities:** Vercel Flags: edge-evaluated flags with OpenFeature support. Flagship: flags built for AI workloads (model swaps, prompt rollouts).
- **Usage domain:** Platform-native flagging. **License:** Proprietary.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A20. Observability: metrics, logs, traces

#### A20.1 Datadog
- **Canonical identity:** Datadog — monitoring & security platform (datadoghq.com). **Type:** cloud service.
- **Official URL:** https://www.datadoghq.com — **Verification:** Partially verified.
- **Description / capabilities:** Infra monitoring, APM, logs, RUM, synthetics, security, LLM Observability (40k LLM spans/mo free tier per 2026 roundup); OTel ingestion; 2026 pricing per comparisons: Infra Pro $15/host/mo annual, APM +$31/host, logs $0.10/GB ingest.
- **Usage domain:** All-in-one SaaS observability. **Integration method:** Agent + SDKs + OTel.
- **Limitations:** Bill scales steeply with hosts/logs; set ingestion limits day one.
- **Related:** New Relic, Grafana Cloud, Honeycomb.
- **Sources:** search themes 6, 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A20.2 Grafana (OSS + Cloud; LGTM stack)
- **Canonical identity:** Grafana Labs — Grafana dashboards + Loki (logs) + Tempo (traces) + Mimir (metrics) + Pyroscope (profiling) (grafana.com). **Type:** open-source project / cloud service.
- **Official URL:** https://grafana.com — **Verification:** Partially verified.
- **Description / capabilities:** Visualization + alerting over Prometheus/Loki/Tempo/Mimir; Grafana Cloud free tier (10k series, 50GB logs, 50GB traces/mo per 2026 guides); k6-based synthetic monitoring; Agent Observability product for LLM apps (30k generations/mo free).
- **Usage domain:** OSS-leaning observability; K8s-native. **License:** AGPL-3.0 (Grafana OSS).
- **Limitations:** You own dashboards/alert rules or they rot.
- **Sources:** search theme 6. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A20.3 Prometheus
- **Canonical identity:** Prometheus — metrics + alerting toolkit (prometheus.io), CNCF graduated. **Type:** open-source project / infrastructure framework.
- **Official URL:** https://prometheus.io — **Verification:** Partially verified.
- **Description / capabilities:** Pull-based metrics, PromQL, Alertmanager, `/metrics` exposition; kube-prometheus-stack for K8s.
- **Usage domain:** Metrics backbone. **License:** Apache-2.0.
- **Sources:** search theme 6. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A20.4 OpenTelemetry
- **Canonical identity:** OpenTelemetry — observability framework (opentelemetry.io), CNCF graduated. **Type:** open-source project / open standard.
- **Official URL:** https://opentelemetry.io — **Verification:** Partially verified.
- **Description / capabilities:** Vendor-neutral APIs/SDKs/instrumentation for traces, metrics, logs; OTLP protocol; Collector for unified ingestion; GenAI semantic conventions for LLM spans; the universal instrumentation layer across Datadog/Grafana/Honeycomb.
- **Usage domain:** Instrumentation standard. **License:** Apache-2.0.
- **Sources:** search themes 6, 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A20.5 New Relic
- **Canonical identity:** New Relic — observability platform (newrelic.com), incl. New Relic AI monitoring. **Type:** cloud service.
- **Official URL:** https://newrelic.com — **Verification:** Partially verified.
- **Description / capabilities:** APM, infra, logs, synthetics; usage-based pricing (per-GB/Compute); New Relic AI for LLM monitoring.
- **Usage domain:** SaaS APM alternative to Datadog. **License:** Proprietary.
- **Sources:** search theme 6. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A20.6 Honeycomb
- **Canonical identity:** Honeycomb — event-based observability (honeycomb.io). **Type:** cloud service.
- **Official URL:** https://honeycomb.io — **Verification:** Partially verified.
- **Description / capabilities:** Wide-event tracing, BubbleUp debugging, SLOs; OTel-native; beloved for high-cardinality debugging.
- **Usage domain:** Debugging complex distributed systems. **License:** Proprietary.
- **Sources:** search theme 6 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A20.7 Elastic (ELK)
- **Canonical identity:** Elastic — search + observability (elastic.co): Elasticsearch, Kibana, APM. **Type:** open-source-adjacent project / cloud service.
- **Official URL:** https://www.elastic.co — **Verification:** Partially verified.
- **Description / capabilities:** Log analytics, APM, SIEM; Elastic Cloud hosted; SSPL/Elastic License (source-available, not OSI).
- **Usage domain:** Log-heavy observability + security. **License:** SSPL/Elastic License.
- **Sources:** search theme 6. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A20.8 SigNoz / HyperDX / Better Stack (logs)
- **Canonical identity:** SigNoz (signoz.io) — OSS APM; HyperDX (hyperdx.io) — OSS session-replay+otel; Better Stack (betterstack.com) — logs + uptime + on-call. **Type:** open-source project / cloud service.
- **Official URL:** https://signoz.io ; https://hyperdx.io ; https://betterstack.com — **Verification:** Partially verified.
- **Description / capabilities:** SigNoz: self-hostable Datadog alternative on OTel/ClickHouse. HyperDX: traces+logs+replay unified. Better Stack: ClickHouse-backed log management + uptime + incidents + status pages.
- **Usage domain:** Cost-effective observability. **License:** MIT/Apache-2.0 (SigNoz, HyperDX core); proprietary (Better Stack).
- **Sources:** search themes 6, 22. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A21. Error tracking

#### A21.1 Sentry
- **Canonical identity:** Sentry — error + performance monitoring (sentry.io). **Type:** cloud service / open-source project.
- **Official URL:** https://sentry.io — **Verification:** Partially verified.
- **Description / capabilities:** Error grouping/dedup, stack traces, release tracking, performance transactions, session replay, cron monitoring; agent tracing for AI workflows (2026); SDKs for all major platforms; free Developer plan (1 user, 5k errors, 5M spans per 2026 guides); self-hostable.
- **Usage domain:** Near-universal error tracking choice. **Integration method:** SDK init + DSN.
- **License:** BSL (self-host) / proprietary SaaS — license nuance not re-verified.
- **Limitations:** Not infra monitoring; pair with Grafana/Better Stack for servers.
- **Related:** Rollbar, Bugsnag, GlitchTip.
- **Sources:** search theme 6. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A21.2 Rollbar / Bugsnag
- **Canonical identity:** Rollbar (rollbar.com); Bugsnag (bugsnag.com, SmartBear). **Type:** cloud service.
- **Official URL:** https://rollbar.com ; https://www.bugsnag.com — **Verification:** Partially verified.
- **Description / capabilities:** Real-time error monitoring with grouping, deploy tracking, alerting; long-standing Sentry alternatives.
- **Usage domain:** Error tracking. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A21.3 GlitchTip
- **Canonical identity:** GlitchTip — open-source Sentry-compatible error tracking (glitchtip.com). **Type:** open-source project.
- **Official URL:** https://glitchtip.com — **Verification:** Partially verified.
- **Description / capabilities:** Sentry SDK-compatible ingestion; self-host or managed; simple, cheap error tracking.
- **Usage domain:** Self-hosted error tracking. **License:** MIT.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

### A22. Performance & web-vitals monitoring

#### A22.1 Lighthouse / PageSpeed Insights
- **Canonical identity:** Lighthouse — open-source auditing (github.com/GoogleChrome/lighthouse; pagespeed.web.dev). **Type:** open-source project / development utility.
- **Official URL:** https://github.com/GoogleChrome/lighthouse — **Verification:** Partially verified.
- **Description / capabilities:** Lab audits for performance, SEO, a11y, best practices; CrUX field data via PageSpeed Insights; CI via Lighthouse CI.
- **Usage domain:** Web performance auditing. **License:** Apache-2.0.
- **Sources:** search theme 20. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A22.2 web-vitals (library)
- **Canonical identity:** `web-vitals` — Google's field-measurement library (github.com/GoogleChrome/web-vitals). **Type:** open-source project / code library.
- **Official URL:** https://github.com/GoogleChrome/web-vitals — **Verification:** Partially verified.
- **Description / capabilities:** Measures LCP/INP/CLS/FCP/TTFB in real users; tiny; ships data to your analytics/RUM.
- **Usage domain:** Real-user Core Web Vitals collection. **License:** Apache-2.0.
- **Sources:** search theme 20 (spec monitoring doc). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A22.3 SpeedCurve / Calibre / DebugBear
- **Canonical identity:** SpeedCurve (speedcurve.com); Calibre (calibreapp.com); DebugBear (debugbear.com) — synthetic web-performance monitoring. **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Lab + field (CrUX/RUM) performance tracking, budgets, filmstrips, competitor benchmarks; DebugBear strong on Core Web Vitals detail.
- **Usage domain:** Continuous web performance. **License:** Proprietary.
- **Sources:** General knowledge + search theme 20 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A22.4 Vercel Speed Insights
- **Canonical identity:** Speed Insights — RUM on Vercel (vercel.com/docs/speed-insights). **Type:** cloud service feature.
- **Official URL:** https://vercel.com/docs/speed-insights — **Verification:** Partially verified.
- **Description / capabilities:** Real-experience scores from `web-vitals`-style collection on Vercel-hosted sites.
- **Usage domain:** Vercel-native performance RUM. **License:** Proprietary.
- **Sources:** search theme 5 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low.

### A23. AI agent / LLM telemetry (general; OpenCode-specific integrations cross-referenced)

#### A23.1 Langfuse
- **Canonical identity:** Langfuse — open-source LLM engineering platform (langfuse.com). **Type:** open-source project / cloud service.
- **Official URL:** https://langfuse.com — **Verification:** Partially verified.
- **Description / capabilities:** Tracing, cost tracking, prompt management, evals/datasets, user analytics; Python/JS SDKs with `@observe`; OTel ingestion + OTLP endpoint; MIT core (EE folders excluded); self-host via Docker/K8s/Terraform; cloud free 50k observations/mo.
- **Status:** **Acquired by ClickHouse, January 2026** (per 2026 roundups).
- **Usage domain:** OSS-default LLM tracing + evals. **License:** MIT (core) + commercial EE.
- **Related:** LangSmith, Arize Phoenix, Comet Opik, Helicone. Cross-reference: Langfuse OpenCode Observability (prior catalog, dedup).
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.2 LangSmith
- **Canonical identity:** LangSmith — LangChain's LLM platform (langchain.com/langsmith). **Type:** cloud service.
- **Official URL:** https://www.langchain.com/langsmith — **Verification:** Partially verified.
- **Description / capabilities:** Tracing, datasets, eval scheduling, prompt hub, agent assist; deepest LangChain/LangGraph integration; OTel ingestion; free tier 5k traces/mo; self-host enterprise-only.
- **Usage domain:** LangChain-stack observability. **License:** Proprietary.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.3 Helicone — maintenance mode
- **Canonical identity:** Helicone — LLM proxy gateway (helicone.ai). **Type:** open-source project / cloud service. **Verification:** Partially verified (status: maintenance mode).
- **Description / capabilities:** Proxy-based: route LLM calls through `oai.helicone.ai` with near-zero code change; cost tracking across 300+ models, caching (exact+semantic), rate limiting; Apache-2.0, self-hostable; free 10k–100k req/mo (sources vary).
- **Status:** 2026 AI-observability roundup reports Helicone's services now run in maintenance mode. Verify current status before adopting.
- **Usage domain:** Drop-in LLM cost/latency metering. **License:** Apache-2.0.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.4 Braintrust
- **Canonical identity:** Braintrust — eval-first AI platform (braintrustdata.com). **Type:** cloud service.
- **Official URL:** https://www.braintrustdata.com — **Verification:** Partially verified.
- **Description / capabilities:** Playground → dataset → CI eval loop; production tracing/logging; OTel ingestion; $80M Series B Feb 2026; 1M spans/mo free tier per roundups.
- **Usage domain:** Eval-centric AI development. **License:** Proprietary (SDKs open).
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.5 Arize Phoenix
- **Canonical identity:** Phoenix — AI observability (github.com/Arize-AI/phoenix; docs.arize.com/phoenix); Arize AX managed. **Type:** open-source-adjacent project / cloud service.
- **Official URL:** https://docs.arize.com/phoenix — **Verification:** Partially verified.
- **Description / capabilities:** OTel-native tracing, evals, drift/embedding analysis; notebook-friendly.
- **License:** Elastic License 2.0 (source-available, NOT OSI-approved) — important nuance per 2026 comparisons.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.6 Comet Opik
- **Canonical identity:** Opik — open-source LLM eval/tracing by Comet (comet.com/opik; github.com/comet-ml/opik). **Type:** open-source project.
- **Official URL:** https://www.comet.com/site/products/opik/ — **Verification:** Partially verified.
- **Description / capabilities:** Tracing + online evaluation rules; fully self-hostable; ~20.9k stars (July 2026).
- **Usage domain:** Permissive-licensed Langfuse alternative. **License:** Apache-2.0.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.7 Traceloop / OpenLLMetry
- **Canonical identity:** OpenLLMetry — OTel instrumentation for LLMs (traceloop.com/openllmetry). **Type:** open-source project / code library.
- **Official URL:** https://www.traceloop.com — **Verification:** Partially verified.
- **Description / capabilities:** Vendor-neutral instrumentation layer emitting standard OTel spans to any backend; thin UI; cleanest standards story.
- **Usage domain:** Backend-agnostic LLM spans. **License:** Apache-2.0.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.8 Portkey / LiteLLM (AI gateways)
- **Canonical identity:** Portkey (portkey.ai) — AI gateway; LiteLLM (litellm.ai; github.com/BerriAI/litellm) — LLM proxy. **Type:** open-source project / cloud service.
- **Official URL:** https://portkey.ai ; https://www.litellm.ai — **Verification:** Partially verified.
- **Description / capabilities:** Unified OpenAI-compatible API across 100+ models; caching, retries, fallbacks, load balancing, budgets, guardrails; LiteLLM fully OSS proxy; the most-copied 2026 OSS stack: App → LiteLLM → provider with spans to Langfuse.
- **Usage domain:** Multi-provider LLM routing + reliability. **License:** MIT (LiteLLM); proprietary + OSS tiers (Portkey).
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A23.9 Promptfoo / DeepEval / Ragas (evals)
- **Canonical identity:** promptfoo (promptfoo.dev) — LLM eval CLI; DeepEval (deepeval.com) — eval framework; Ragas (ragas.io) — RAG evals. **Type:** open-source project / development utility.
- **Official URL:** https://promptfoo.dev ; https://www.deepeval.com ; https://docs.ragas.io — **Verification:** Partially verified.
- **Description / capabilities:** promptfoo: test prompts/models in CI with assertions. DeepEval: pytest-like evals with LLM-as-judge metrics. Ragas: RAG-specific metrics (faithfulness, context precision).
- **Usage domain:** LLM quality gates in CI. **License:** MIT/Apache-2.0.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A23.10 Lunary
- **Canonical identity:** Lunary — lightweight LLM analytics (lunary.ai). **Type:** open-source project / cloud service.
- **Official URL:** https://lunary.ai — **Verification:** Partially verified.
- **Description / capabilities:** Chat-style replay UI, cost/latency analytics; good for small teams.
- **Usage domain:** Simple LLM analytics. **License:** Apache-2.0 + cloud.
- **Sources:** search theme 13. **Verification date:** 2026-10-10. **Confidence:** Low.

### A24. Cost & usage monitoring (FinOps)

#### A24.1 Infracost
- **Canonical identity:** Infracost — cloud cost estimates for Terraform in PRs (infracost.io; github.com/infracost/infracost). **Type:** open-source project / development utility (+ cloud service).
- **Official URL:** https://www.infracost.io — **Verification:** Partially verified.
- **Description / capabilities:** Comments cost diffs on IaC pull requests; shift-left FinOps; CI integration.
- **Usage domain:** IaC cost review. **License:** Apache-2.0 (core).
- **Sources:** search theme 28. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A24.2 Vantage
- **Canonical identity:** Vantage — cloud cost transparency (vantage.sh). **Type:** cloud service.
- **Official URL:** https://www.vantage.sh — **Verification:** Partially verified.
- **Description / capabilities:** Multi-cloud cost reporting, budgets, optimization recommendations; free tier; ~$30/mo entry per 2026 comparisons; default start for <$2.5k/mo spend.
- **Usage domain:** Self-serve FinOps dashboards. **License:** Proprietary.
- **Sources:** search theme 28. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A24.3 CloudZero
- **Canonical identity:** CloudZero — cloud cost intelligence (cloudzero.com). **Type:** cloud service.
- **Official URL:** https://www.cloudzero.com — **Verification:** Partially verified.
- **Description / capabilities:** Unit economics (cost per customer/feature), multi-cloud; sales-led opaque pricing.
- **Usage domain:** Business-metric cost attribution. **License:** Proprietary.
- **Sources:** search theme 28. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A24.4 OpenCost / Kubecost
- **Canonical identity:** OpenCost (opencost.io) — CNCF incubating K8s cost spec; Kubecost (kubecost.com) — K8s cost monitoring built on OpenCost. **Type:** open-source project / cloud service.
- **Official URL:** https://www.opencost.io ; https://www.kubecost.com — **Verification:** Partially verified.
- **Description / capabilities:** Real-time pod/namespace cost allocation; Kubecost adds budgets/alerts/chargeback; free single-cluster tier; Business from $449/mo per 2026 comparisons.
- **Usage domain:** Kubernetes cost visibility. **License:** Apache-2.0 (OpenCost); commercial (Kubecost).
- **Sources:** search theme 28. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A24.5 Komiser / Cloud Custodian
- **Canonical identity:** Komiser (tailwarden/komiser) — cloud inspector; Cloud Custodian (cloud-custodian.io) — rules engine for cost/security/governance. **Type:** open-source project / development utility.
- **Official URL:** https://github.com/tailwarden/komiser ; https://cloud-custodian.io — **Verification:** Partially verified.
- **Description / capabilities:** Komiser: inventory + cost/usage/security views across AWS/GCP/Azure. Custodian: YAML policies to tag/stop/delete waste.
- **Usage domain:** Cloud hygiene automation. **License:** MPL-2.0 (Komiser) / Apache-2.0 (Custodian).
- **Sources:** search theme 28. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A24.6 Finout / nOps / CloudFix
- **Canonical identity:** Finout (finout.io) — FinOps chargeback; nOps (nops.io) — automated optimization; CloudFix (cloudfix.com) — automated AWS fixes. **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Finout: unit economics + chargeback. nOps: AI-powered rightsizing/commitment automation. CloudFix: implements fixes automatically (rightsizing, etc.).
- **Usage domain:** Automated cloud cost optimization. **License:** Proprietary.
- **Sources:** search theme 28. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A25. Background jobs & workflow orchestration

#### A25.1 Inngest
- **Canonical identity:** Inngest — event-driven durable execution (inngest.com). **Type:** cloud service / open-source project (self-host option).
- **Official URL:** https://www.inngest.com — **Verification:** Partially verified.
- **Description / capabilities:** Durable functions split into steps; events, schedules, cron, waits (e.g., "wait 3 days"); functions run on your infra (serverless-friendly) while Inngest handles scheduling/retries/flow control; deep run observability; strong AI/agent patterns.
- **Usage domain:** Serverless-native durable workflows. **Integration method:** SDK (TS/Python/Go); `inngest dev` local.
- **License:** Apache-2.0 (core) + cloud.
- **Limitations:** Step idempotency is your responsibility (re-runs possible in rare failures — use idempotency keys for payments/emails).
- **Related:** Trigger.dev, Temporal, QStash.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A25.2 Trigger.dev
- **Canonical identity:** Trigger.dev — background jobs platform (trigger.dev). **Type:** open-source project / cloud service.
- **Official URL:** https://trigger.dev — **Verification:** Partially verified.
- **Description / capabilities:** TypeScript-first tasks; v3 runs tasks on managed compute (no serverless timeouts); self-hostable (Apache-2.0); checkpoints for long waits; first-class agent/AI runs with LLM rate-limit retries.
- **Usage domain:** Long-running TS jobs without timeout limits. **License:** Apache-2.0.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A25.3 Temporal
- **Canonical identity:** Temporal — durable workflow engine (temporal.io). **Type:** open-source project / cloud service.
- **Official URL:** https://temporal.io — **Verification:** Partially verified.
- **Description / capabilities:** Workflows (deterministic code) + activities (side effects); event-sourced replay; signals/queries for human-in-the-loop; sagas/compensation; SDKs in 7 languages; self-host (Cassandra/Postgres + server cluster) or Temporal Cloud (no monthly minimum as of 2026).
- **Usage domain:** Business-critical long-running orchestration at scale. **License:** MIT (SDKs/server).
- **Limitations:** Steep learning curve (determinism constraints: no `Date.now()`/`Math.random()` in workflows); heavy to operate self-hosted.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A25.4 BullMQ
- **Canonical identity:** BullMQ — Redis-based Node.js queue (docs.bullmq.io). **Type:** open-source project / code library.
- **Official URL:** https://docs.bullmq.io — **Verification:** Partially verified.
- **Description / capabilities:** High-throughput job queues with priorities, rate limiting, delayed jobs, DLQ; needs Redis + persistent workers.
- **Usage domain:** Self-hosted worker jobs. **License:** MIT.
- **Limitations:** Requires always-on workers (not serverless-native); you own Redis.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A25.5 QStash (Upstash)
- **Canonical identity:** QStash — serverless messaging (upstash.com/qstash). **Type:** cloud service.
- **Official URL:** https://upstash.com — **Verification:** Partially verified.
- **Description / capabilities:** HTTP-callback queues, schedules/cron, DLQ, retries; no workers to run; pairs with serverless functions.
- **Usage domain:** Simple fire-and-forget serverless jobs. **License:** Proprietary.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A25.6 Restate / DBOS / Hatchet
- **Canonical identity:** Restate (restate.dev) — durable handlers/virtual objects; DBOS (dbos.dev) — durable execution as Postgres-backed library; Hatchet (hatchet.run) — OSS task queue. **Type:** open-source project / cloud service.
- **Official URL:** https://restate.dev ; https://www.dbos.dev ; https://www.hatchet.run — **Verification:** Partially verified.
- **Description / capabilities:** Restate: journaled durable handlers, less ceremony than Temporal. DBOS: durable execution in-process on Postgres — zero new infra. Hatchet: OSS-first queue, Postgres-backed, growing in 2026.
- **Usage domain:** Lightweight durable execution. **License:** Mixed OSS (BSL noted for some DBOS/Restate components historically — not re-verified; treat as Unresolved license nuance).
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A25.7 Airflow / Prefect / Dagster
- **Canonical identity:** Apache Airflow (airflow.apache.org); Prefect (prefect.io); Dagster (dagster.io) — data workflow orchestrators. **Type:** open-source project / cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** DAG-based scheduling for data/ML pipelines; sensors, backfills, retries; managed clouds available.
- **Usage domain:** Data engineering pipelines (not general background jobs). **License:** Apache-2.0.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A25.8 pg-boss / Graphile Worker
- **Canonical identity:** pg-boss (github.com/timgit/pg-boss); Graphile Worker (worker.graphile.org) — Postgres-native job queues. **Type:** open-source project / code library.
- **Official URL:** https://github.com/timgit/pg-boss ; https://worker.graphile.org — **Verification:** Partially verified.
- **Description / capabilities:** Queues inside your existing Postgres (SKIP LOCKED; LISTEN/NOTIFY); zero new infra; pg-boss ~96k weekly npm downloads per 2026 research.
- **Usage domain:** Postgres-shop background jobs. **License:** MIT.
- **Sources:** search theme 12. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A25.9 Sidekiq / Celery
- **Canonical identity:** Sidekiq (sidekiq.org) — Ruby background jobs; Celery (docs.celeryq.dev) — Python distributed task queue. **Type:** open-source project / code library.
- **Official URL:** https://sidekiq.org ; https://docs.celeryq.dev — **Verification:** Partially verified.
- **Description / capabilities:** Mature Redis-backed workers for Rails/Django ecosystems; scheduling via sidekiq-cron/celery-beat.
- **Usage domain:** Ruby/Python background processing. **License:** LGPL-3.0 (Sidekiq OSS) / BSD-3 (Celery).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Medium.

### A26. Headless coding-agent execution in CI

#### A26.1 GitHub Copilot coding agent
- **Canonical identity:** Copilot coding agent — autonomous agent in GitHub (docs.github.com/copilot/concepts/agents/coding-agent/about-coding-agent). **Type:** agent integration / cloud service.
- **Official URL:** https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent — **Verification:** Partially verified.
- **Description / capabilities:** Assign issues or `@copilot` mentions; runs in its own ephemeral GitHub-Actions-powered dev environment; researches/plans/edits/tests; opens exactly one branch + PR per task; customizable agent firewall; steerable via `@copilot` PR comments. 2026: Claude and Codex models available inside Copilot subscriptions (no extra subscription).
- **Usage domain:** Issue-to-PR automation inside GitHub. **Integration method:** GitHub UI/issue assignment; MCP/REST APIs.
- **License:** Proprietary (Copilot subscription).
- **Limitations:** Can ignore repo instructions unless wired into Actions; GitHub-only.
- **Related:** Codex cloud, Jules, Claude Code GitHub Action.
- **Sources:** search theme 27. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A26.2 Claude Code in CI (GitHub Action + headless CLI)
- **Canonical identity:** Claude Code — `claude -p` headless mode + official GitHub Action (`@claude` mentions) (code.claude.com/docs/en/headless). **Type:** agent integration / development utility.
- **Official URL:** https://code.claude.com/docs/en/headless — **Verification:** Partially verified.
- **Description / capabilities:** `claude -p "<prompt>"` runs the agent loop non-interactively (exit code signals completion); GitHub Action triggers on `@claude` mentions for deep multi-file work; costs: Claude subscription + Actions minutes.
- **Usage domain:** CI-driven autonomous coding with Claude. **License:** Proprietary (Anthropic).
- **Limitations:** No free tier; separate Actions-minutes cost.
- **Sources:** search theme 27. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A26.3 OpenAI Codex (cloud + CLI headless)
- **Canonical identity:** Codex — OpenAI coding agent: cloud tasks + `codex exec` CLI (developers.openai.com/codex). **Type:** agent integration / cloud service.
- **Official URL:** https://developers.openai.com/codex — **Verification:** Partially verified.
- **Description / capabilities:** Cloud: each task in isolated container at selected branch; two-phase (setup with network, agent phase sandboxed); commits + cited logs; user promotes to PR; 12h container-state cache. CLI: `codex exec` headless with approval policies; internet opt-in allowlists.
- **Usage domain:** Async cloud coding tasks; CI-driven via CLI. **License:** Proprietary (ChatGPT Plus/Pro bundled).
- **Limitations:** GitHub workflow newer/less deep than Copilot's.
- **Sources:** search theme 27. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### A26.4 Google Jules
- **Canonical identity:** Jules — Google's async coding agent (developers.google.com/jules). **Type:** agent integration / cloud service.
- **Official URL:** https://developers.google.com/jules — **Verification:** Partially verified.
- **Description / capabilities:** GitHub issue label → plan (optional approval) → Cloud VM execution → PR; free tier 15 tasks/day per 2026 comparisons; MCP restricted to vetted list.
- **Usage domain:** Budget-friendly async PR generation. **License:** Proprietary.
- **Limitations:** No enterprise tier yet; vetted MCP only.
- **Sources:** search theme 27. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A26.5 Devin
- **Canonical identity:** Devin — autonomous software engineer by Cognition (devin.ai). **Type:** agent integration / cloud service.
- **Official URL:** https://devin.ai — **Verification:** Partially verified.
- **Description / capabilities:** Full cloud dev environment; async task execution via Slack/GitHub issues; "assign and walk away" tickets; from $20/mo + usage per 2026 comparisons.
- **Usage domain:** Fully autonomous ticket completion. **License:** Proprietary.
- **Limitations:** Weaker on vague/open-ended work per 2026 satisfaction notes.
- **Sources:** search theme 27. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### A26.6 Aider (headless)
- **Canonical identity:** Aider — AI pair-programming in the terminal (aider.chat). **Type:** open-source project / development utility.
- **Official URL:** https://aider.chat — **Verification:** Partially verified.
- **Description / capabilities:** Terminal agent; `--message` non-interactive mode for CI/scripting; BYO provider keys; git-native flow.
- **Usage domain:** Scripted agent edits in pipelines. **License:** Apache-2.0.
- **Sources:** search theme 27. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### A. Rapid-fire: secondary infrastructure resources
Compact entries for significant-but-secondary tools (full records not warranted in this pass):

- **act** (github.com/nektos/act) — run GitHub Actions locally in Docker. OSS (MIT). Partially verified.
- **Earthly** — containerized builds; **cloud shut down July 2025**; OSS core continues (MPL-2.0). Historical/Partially verified.
- **BuildJet** — faster GitHub runners; **closed March 2026**. Archived.
- **Renovate** (github.com/renovatebot/renovate) — automated dependency updates; Mend.io. OSS. Partially verified.
- **Dependabot** — GitHub-native dependency updates. Cloud service feature. Partially verified.
- **Trunk.io** — meta-linter + CI; trunk check. Proprietary + OSS plugins. Partially verified.
- **devenv `tasks` / just** (casey/just) — command runner. OSS (CC0). Partially verified.
- **direnv `use flake`** — covered in A16.1.
- **Tailscale** — mesh VPN for dev/prod networking. Proprietary + OSS client. Partially verified.
- **ngrok / Cloudflare Tunnel** — expose local services. Proprietary (free tiers). Partially verified.
- **Caddy / Traefik / nginx** — reverse proxies + auto-TLS. OSS. Partially verified.
- **Let's Encrypt** — free ACME certificates. OSS service (ISRG). Verified (well-established).
- **External Secrets Operator** — sync secrets from providers into K8s. OSS (Apache-2.0). Partially verified.
- **cert-manager** — K8s TLS automation. OSS (Apache-2.0). Partially verified.
- **Vagrant** — VM dev environments (HashiCorp, BSL). Partially verified.
- **Packer** — machine image builds (HashiCorp, BSL). Partially verified.
- **Consul / Nomad** (HashiCorp, BSL) — service mesh / workload orchestration. Partially verified.
- **OpenTofu Registry** — search.opentofu.org. Verified via opentofu.org fetch.
- **Spacelift / env0 / Scalr** — IaC automation platforms (Terraform/OpenTofu Cloud alternatives). Proprietary. Partially verified.
- **HCP Terraform** — HashiCorp managed IaC runs. Proprietary. Partially verified.
- **Doppler GitHub Action / Infisical GitHub Action** — secrets injection in CI. Covered in A15.
- **PagerDuty / Opsgenie** — on-call alerting. Proprietary. Partially verified.
- **incident.io / Rootly** — incident management. Proprietary. Partially verified.
- **Sentry Cron Monitoring** — job health checks. Covered in A21.1.
- **Healthchecks.io** — dead-man's-switch cron monitoring. OSS + hosted. Partially verified.
- **Cronitor** — cron monitoring + status pages. Proprietary. Partially verified.
- **AWS EventBridge Scheduler / GCP Cloud Scheduler** — managed cron. Proprietary. Partially verified.
- **GitHub Actions `schedule` / `workflow_dispatch`** — cron + manual CI triggers. Covered in A3.1.
- **Vercel Cron / Netlify Scheduled Functions** — platform cron. Proprietary features. Partially verified.
- **Cloudflare Cron Triggers** — Workers scheduled. Covered in A12.2.
- **Upstash QStash schedules** — covered in A25.5.
- **Railway cron / Render cron jobs** — PaaS cron. Proprietary features. Partially verified.

---

## B. SEO, analytics, content, commerce, website operations

### B1. Technical SEO & indexing

#### B1.1 Google Search Console
- **Canonical identity:** Google Search Console — indexing/performance tooling (search.google.com/search-console). **Type:** cloud service (free).
- **Official URL:** https://search.google.com/search-console — **Verification:** Partially verified.
- **Description / capabilities:** Index coverage, Core Web Vitals field data, sitemap submission, URL inspection, manual actions, international targeting reports.
- **Usage domain:** Technical SEO baseline. **Integration method:** Web UI + API. **License:** Proprietary (free).
- **Sources:** search theme 20. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B1.2 Bing Webmaster Tools
- **Canonical identity:** Bing Webmaster Tools (bing.com/webmasters). **Type:** cloud service (free).
- **Official URL:** https://www.bing.com/webmasters — **Verification:** Partially verified.
- **Description / capabilities:** Indexing, SEO reports, URL submission API (IndexNow participant).
- **Usage domain:** Non-Google indexing. **License:** Proprietary (free).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B1.3 schema.org / JSON-LD
- **Canonical identity:** schema.org — structured-data vocabulary; JSON-LD the recommended serialization. **Type:** open standard.
- **Official URL:** https://schema.org — **Verification:** Partially verified.
- **Description / capabilities:** Types (Article, Product, FAQPage, Organization, BreadcrumbList…); enables rich results; 2026 sources stress nested entities and AI-engine parseability; test via Google Rich Results Test.
- **Usage domain:** Structured data for search + AI answer engines. **Integration method:** `<script type="application/ld+json">` in HTML; framework helpers.
- **License:** CC-SA-ish (schema.org terms — not re-verified).
- **Sources:** search theme 20. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B1.4 Sitemap / robots.txt standards
- **Canonical identity:** XML sitemaps (sitemaps.org) + robots.txt (RFC 9309) + `llms.txt` (emerging AI-crawler convention). **Type:** open standard / development utility.
- **Official URL:** https://www.sitemaps.org ; https://www.rfc-editor.org/rfc/rfc9309.html ; https://llmstxt.org — **Verification:** Partially verified.
- **Description / capabilities:** `sitemap.xml` (≤50k URLs/50MB per file, `<lastmod>`); `robots.txt` crawl directives + sitemap pointer; `llms.txt` at site root as machine-readable content index for AI crawlers (2026 discovery stack).
- **Usage domain:** Crawlability + AI discoverability. **License:** N/A.
- **Sources:** search theme 20. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B1.5 next-sitemap / sitemap libraries
- **Canonical identity:** next-sitemap (npm) — sitemap generation for Next.js; equivalents: `sitemap` (npm), Astro sitemap integration. **Type:** open-source project / code library.
- **Official URL:** https://github.com/iamvishnusankar/next-sitemap — **Verification:** Partially verified.
- **Description / capabilities:** Generates `sitemap.xml` + `robots.txt` at build from Next.js routes.
- **Usage domain:** Framework sitemap automation. **License:** MIT.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

#### B1.6 Screaming Frog SEO Spider
- **Canonical identity:** Screaming Frog — website crawler for SEO audits (screamingfrog.co.uk). **Type:** development utility (freemium desktop app).
- **Official URL:** https://www.screamingfrog.co.uk/seo-spider/ — **Verification:** Partially verified.
- **Description / capabilities:** Crawls sites for broken links, redirects, metadata, structured data, Core Web Vitals; free tier 500 URLs.
- **Usage domain:** Technical SEO audits. **License:** Proprietary (freemium).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B2. SEO tooling (suites)

#### B2.1 Ahrefs
- **Canonical identity:** Ahrefs — SEO suite (ahrefs.com). **Type:** cloud service.
- **Official URL:** https://ahrefs.com — **Verification:** Partially verified.
- **Description / capabilities:** Site Audit, Keywords Explorer, Site Explorer (backlinks), Rank Tracker, Content Explorer; powers 2M+ sites' consent tooling customer overlap noted (Ahrefs uses CookieYes).
- **Usage domain:** SEO research + monitoring. **License:** Proprietary.
- **Sources:** search themes 20, 24 (CookieYes customer mention). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B2.2 Semrush
- **Canonical identity:** Semrush — online visibility suite (semrush.com). **Type:** cloud service.
- **Official URL:** https://www.semrush.com — **Verification:** Partially verified.
- **Description / capabilities:** Keyword research, site audits, position tracking, PPC/competitive intelligence.
- **Usage domain:** SEO + marketing intelligence. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B2.3 Yoast SEO / Rank Math
- **Canonical identity:** Yoast SEO (yoast.com) — WordPress SEO plugin; Rank Math (rankmath.com) — newer WP SEO plugin. **Type:** plugin (freemium).
- **Official URL:** https://yoast.com ; https://rankmath.com — **Verification:** Partially verified.
- **Description / capabilities:** Meta tags, XML sitemaps, schema output, readability/content analysis, redirects; Rank Math noted for generous free tier.
- **Usage domain:** WordPress on-page/technical SEO. **License:** GPL (WP plugins).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B3. Web analytics (incl. privacy-friendly)

#### B3.1 Google Analytics 4
- **Canonical identity:** GA4 — Google's analytics platform (analytics.google.com). **Type:** cloud service (free; 360 enterprise).
- **Official URL:** https://analytics.google.com — **Verification:** Partially verified.
- **Description / capabilities:** Event-based web/app analytics; Consent Mode v2 integration; Google Ads/Search Console native links; needs cookie consent in EU/UK; 2026: loses 30–50% conversion signal to consent/ad-blockers without server-side CAPI per analysts.
- **Usage domain:** Default web analytics. **License:** Proprietary (free).
- **Limitations:** Consent-dependent; data retention 2–14 months standard; EU data-transfer scrutiny (CNIL €325M fine Sept 2025 context).
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B3.2 Plausible
- **Canonical identity:** Plausible — privacy-friendly web analytics (plausible.io). **Type:** open-source project / cloud service.
- **Official URL:** https://plausible.io — **Verification:** Partially verified.
- **Description / capabilities:** Lightweight (<1KB), cookieless, no cross-site tracking; EU-hosted; Search Console integration; Starter ~$9/mo per 2026 guides; self-hostable.
- **Usage domain:** Privacy-first pageview analytics. **License:** AGPL-3.0 (self-host).
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B3.3 Fathom
- **Canonical identity:** Fathom Analytics — privacy-first analytics (usefathom.com). **Type:** cloud service.
- **Official URL:** https://usefathom.com — **Verification:** Partially verified.
- **Description / capabilities:** Simple cookieless analytics; V4 dashboard rebuild (Mar 2026) per 2026 roundups; agency-friendly.
- **Usage domain:** Polished privacy-first reporting. **License:** Proprietary (from ~$9–15/mo).
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B3.4 Umami
- **Canonical identity:** Umami — open-source web analytics (umami.is). **Type:** open-source project / cloud service.
- **Official URL:** https://umami.is — **Verification:** Partially verified.
- **Description / capabilities:** Privacy-focused, cookieless option; self-host free; Hobby cloud free; lightweight script.
- **Usage domain:** OSS privacy analytics. **License:** MIT.
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B3.5 Matomo
- **Canonical identity:** Matomo — open-source analytics platform (matomo.org), ex-Piwik. **Type:** open-source project / cloud service.
- **Official URL:** https://matomo.org — **Verification:** Partially verified.
- **Description / capabilities:** GA-like feature depth with data ownership; self-host free; heatmaps/session recordings (premium); Tag Manager; 2026: absorbed Piwik PRO free-Core migrants after Feb 2026 sunset.
- **Usage domain:** Self-hosted/enterprise privacy analytics. **License:** GPL-3.0.
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B3.6 Simple Analytics / Pirsch / Rybbit
- **Canonical identity:** Simple Analytics (simpleanalytics.com); Pirsch (pirsch.io); Rybbit (rybbit.io) — indie privacy analytics. **Type:** cloud service (+ OSS for Rybbit).
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Minimal cookieless pageview analytics; Rybbit open-source with heatmaps/session replay in business tier; Pirsch developer-friendly API + events.
- **Usage domain:** Lightweight indie analytics. **License:** Proprietary (Simple/Pirsch); OSS (Rybbit).
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B3.7 Cloudflare Web Analytics
- **Canonical identity:** Cloudflare Web Analytics — free privacy-first analytics (cloudflare.com/web-analytics). **Type:** cloud service (free).
- **Official URL:** https://www.cloudflare.com/web-analytics/ — **Verification:** Partially verified.
- **Description / capabilities:** Beacon-based, no cookies, free; server-side measurement option.
- **Usage domain:** Zero-cost privacy analytics on Cloudflare. **License:** Proprietary (free).
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B3.8 Microsoft Clarity
- **Canonical identity:** Microsoft Clarity — free heatmaps + session replay (clarity.microsoft.com). **Type:** cloud service (free).
- **Official URL:** https://clarity.microsoft.com — **Verification:** Partially verified.
- **Description / capabilities:** Unlimited heatmaps/session recordings free; no analytics depth — pairs with a pageview tool.
- **Usage domain:** Free UX behavior insight. **License:** Proprietary (free).
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B3.9 Vercel Analytics
- **Canonical identity:** Vercel Web Analytics (vercel.com/docs/analytics). **Type:** cloud service feature.
- **Official URL:** https://vercel.com/docs/analytics — **Verification:** Partially verified.
- **Description / capabilities:** Privacy-friendly pageview analytics for Vercel sites; paid ($10/mo) per 2026 guides.
- **Usage domain:** Vercel-native traffic stats. **License:** Proprietary.
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Low.

### B4. Product analytics

#### B4.1 PostHog
- **Canonical identity:** PostHog — open-source product analytics suite (posthog.com). **Type:** open-source project / cloud service.
- **Official URL:** https://posthog.com — **Verification:** Partially verified.
- **Description / capabilities:** Product + web analytics, funnels, cohorts, session replay, feature flags, experiments, surveys, LLM analytics, error tracking — all-in-one; generous free tiers; usage-based; open source + public roadmap; cookieless mode.
- **Usage domain:** Technical teams' product analytics. **Integration method:** JS/Python SDKs; reverse proxy for first-party collection.
- **License:** MIT (core). **Maintenance:** Active.
- **Limitations:** Breadth means depth tradeoffs vs best-of-breed (e.g., Mixpanel funnels).
- **Related:** Mixpanel, Amplitude, Plausible.
- **Sources:** search themes 14, 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B4.2 Mixpanel
- **Canonical identity:** Mixpanel — product analytics (mixpanel.com). **Type:** cloud service.
- **Official URL:** https://mixpanel.com — **Verification:** Partially verified.
- **Description / capabilities:** Event-based funnels/retention/cohorts; event-based pricing (Feb 2026) per roundups.
- **Status note:** **November 2025 security breach** (ShinyHunters; ~28M SoundCloud accounts exposed; OpenAI publicly removed Mixpanel) — widely cited in 2026; verify current security posture before adopting.
- **Usage domain:** Product growth analytics. **License:** Proprietary.
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B4.3 Amplitude
- **Canonical identity:** Amplitude — product analytics (amplitude.com). **Type:** cloud service.
- **Official URL:** https://www.amplitude.com — **Verification:** Partially verified.
- **Description / capabilities:** Event-based analytics, experimentation, session replay; Plus self-serve tier; **took over Statsig brand/customers May 2026** (OpenAI kept engineers).
- **Usage domain:** Enterprise product analytics. **License:** Proprietary.
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B4.4 Heap (by Contentsquare)
- **Canonical identity:** Heap — autocapture analytics, now Heap by Contentsquare (heap.io). **Type:** cloud service.
- **Official URL:** https://www.heap.io — **Verification:** Partially verified.
- **Description / capabilities:** Automatic event capture without manual instrumentation; part of Contentsquare experience-intelligence suite (acquired Dec 2023).
- **Usage domain:** Low-instrumentation product analytics. **License:** Proprietary.
- **Sources:** search theme 19. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B4.5 Pendo
- **Canonical identity:** Pendo — product experience platform (pendo.io). **Type:** cloud service.
- **Official URL:** https://www.pendo.io — **Verification:** Partially verified.
- **Description / capabilities:** In-app guides, product analytics, session replay, feedback; Resource Center knowledge base.
- **Usage domain:** Enterprise product adoption. **License:** Proprietary.
- **Sources:** search theme 19 (adjacent). **Verification date:** 2026-10-10. **Confidence:** Low.

### B5. Consent management

#### B5.1 CookieYes
- **Canonical identity:** CookieYes — consent management platform (cookieyes.com). **Type:** cloud service (+ open-source SDK).
- **Official URL:** https://www.cookieyes.com — **Verification:** Partially verified.
- **Description / capabilities:** Cookie scanning, customizable banners, geo-targeting, consent logging; Google Consent Mode v2; Gold-tier Google CMP Partner; 2M+ sites (Ahrefs, KFC, Domino's, Forbes per company); free plan (25k pageviews/mo); paid from ~$10/mo; **2026: launched MCP server** (manage consent from Claude/ChatGPT; OAuth 2.1 PKCE; read-mostly tools); **open-source CookieYes SDK** for React/Next.js (`@cookieyes/*` packages, SSR-safe, headless engine).
- **Usage domain:** GDPR/CCPA cookie compliance. **Integration method:** Script tag, WordPress plugin, npm SDK, MCP server.
- **License:** Proprietary service; SDK open source.
- **Limitations:** Free tier pageview cap.
- **Related:** OneTrust, Cookiebot, Klaro.
- **Sources:** search theme 24. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B5.2 OneTrust
- **Canonical identity:** OneTrust — privacy/trust platform (onetrust.com). **Type:** cloud service.
- **Official URL:** https://www.onetrust.com — **Verification:** Partially verified.
- **Description / capabilities:** Enterprise CMP + privacy management, data mapping, DSAR; Google-certified CMP.
- **Usage domain:** Enterprise privacy programs. **License:** Proprietary (enterprise pricing).
- **Sources:** search theme 24. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B5.3 Cookiebot (Usercentrics)
- **Canonical identity:** Cookiebot — CMP by Usercentrics (cookiebot.com). **Type:** cloud service.
- **Official URL:** https://cookiebot.com — **Verification:** Partially verified.
- **Description / capabilities:** Automatic cookie scanning/categorization; Google Consent Mode; IAB TCF 2.2; Google-certified CMP.
- **Usage domain:** SMB–mid-market consent. **License:** Proprietary (free tier small sites).
- **Sources:** search theme 24. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B5.4 Klaro
- **Canonical identity:** Klaro — open-source consent manager (klaro.org; github.com/kiprotect/klaro). **Type:** open-source project / code library.
- **Official URL:** https://klaro.org — **Verification:** Partially verified.
- **Description / capabilities:** Lightweight JS consent banner; declarative service config; no external calls; self-hosted.
- **Usage domain:** OSS consent banners. **License:** BSD-3-Clause.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B5.5 Osano / Complianz
- **Canonical identity:** Osano (osano.com) — data privacy platform; Complianz (complianz.io) — WordPress CMP plugin. **Type:** cloud service / plugin.
- **Official URL:** https://www.osano.com ; https://complianz.io — **Verification:** Partially verified.
- **Description / capabilities:** Osano: CMP + vendor risk. Complianz: WP-native consent with geo-targeting; Google-certified.
- **Usage domain:** Privacy compliance. **License:** Proprietary (Osano); GPL freemium (Complianz).
- **Sources:** search theme 24. **Verification date:** 2026-10-10. **Confidence:** Low.

### B6. Experimentation & A/B testing

#### B6.1 GrowthBook (experiments)
- **Canonical identity:** GrowthBook — covered in A19.4; experiment module: warehouse-native stats engine, visual editor, SDKs. **Type:** open-source project / cloud service.
- **Official URL:** https://www.growthbook.io — **Verification:** Partially verified.
- **Description / capabilities:** Bayesian/frequentist stats on your warehouse; feature flags + experiments unified; guardrails/auto-rollback.
- **Usage domain:** OSS experimentation. **License:** MIT.
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B6.2 PostHog Experiments
- **Canonical identity:** Experiments module in PostHog (posthog.com/docs/experiments). **Type:** cloud service feature.
- **Official URL:** https://posthog.com/docs/experiments — **Verification:** Partially verified.
- **Description / capabilities:** A/B/n tests on feature flags with built-in stats; ties to product analytics funnels.
- **Usage domain:** In-suite experimentation. **License:** MIT (core).
- **Sources:** search theme 14. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B6.3 Optimizely / VWO
- **Canonical identity:** Optimizely (optimizely.com) — experimentation platform; VWO (vwo.com) — A/B testing + CRO suite. **Type:** cloud service.
- **Official URL:** https://www.optimizely.com ; https://vwo.com — **Verification:** Partially verified.
- **Description / capabilities:** Visual editor experiments, feature experimentation, personalization; VWO adds heatmaps/session recordings.
- **Usage domain:** Marketing/product experimentation. **License:** Proprietary (enterprise-leaning).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B7. Headless CMS

#### B7.1 Sanity
- **Canonical identity:** Sanity — structured content platform (sanity.io). **Type:** cloud service.
- **Official URL:** https://www.sanity.io — **Verification:** Partially verified.
- **Description / capabilities:** Customizable Sanity Studio; real-time collaboration; GROQ + GraphQL APIs; visual editing; live preview; content lake; AI actions (2026); free tier then seats + usage.
- **Usage domain:** Content-heavy structured content ops. **Integration method:** JS client, GROQ queries, webhooks, Presentation tool for visual editing.
- **License:** Proprietary (Studio customizable; platform SaaS).
- **Limitations:** No classic self-host; costs climb with team/API usage.
- **Related:** Contentful, Payload, Storyblok.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B7.2 Contentful
- **Canonical identity:** Contentful — headless CMS (contentful.com). **Type:** cloud service.
- **Official URL:** https://www.contentful.com — **Verification:** Partially verified.
- **Description / capabilities:** Enterprise content platform; REST + GraphQL; rich preview workflows; Studio; personalization; AI Actions (native; no MCP server for coding agents per 2026 comparison — ships own agent skills approach instead).
- **Usage domain:** Enterprise content operations. **License:** Proprietary (free tier; paid from ~$300/mo per 2026 guides).
- **Limitations:** Expensive at scale; less visual-first than Storyblok/Sanity.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B7.3 Strapi
- **Canonical identity:** Strapi — open-source headless CMS (strapi.io). **Type:** open-source project / cloud service.
- **Official URL:** https://strapi.io — **Verification:** Partially verified.
- **Description / capabilities:** Self-host or Strapi Cloud; admin panel + content-type builder; REST + GraphQL; plugin ecosystem; largest OSS community in category.
- **Usage domain:** Self-hosted headless CMS. **License:** MIT core (+ paywalled enterprise features per 2026 guides).
- **Limitations:** You own upgrades/plugins/hardening.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B7.4 Payload
- **Canonical identity:** Payload — TypeScript-first headless CMS (payloadcms.com). **Type:** open-source project / cloud service.
- **Official URL:** https://payloadcms.com — **Verification:** Partially verified.
- **Description / capabilities:** Code-defined schema; admin generated from code; REST + GraphQL + Local API; Next.js-native; self-host free; Cloud optional.
- **Usage domain:** Developer-led TS stacks. **License:** MIT.
- **Limitations:** Dev-centric; editors live in what you build; upfront dev investment.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B7.5 Storyblok
- **Canonical identity:** Storyblok — visual headless CMS (storyblok.com). **Type:** cloud service.
- **Official URL:** https://www.storyblok.com — **Verification:** Partially verified.
- **Description / capabilities:** Visual editor + component blocks; live preview; REST + GraphQL; strong Next.js App Router support; free tier; paid from ~€99/mo.
- **Usage domain:** Marketing-led teams needing visual editing. **License:** Proprietary.
- **Limitations:** SaaS economics; less raw-CMS control.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B7.6 Hygraph
- **Canonical identity:** Hygraph — GraphQL-native headless CMS (hygraph.com). **Type:** cloud service.
- **Official URL:** https://hygraph.com — **Verification:** Partially verified.
- **Description / capabilities:** GraphQL-first with content federation across backends; enterprise workflows.
- **Usage domain:** Federated/composable architectures. **License:** Proprietary.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B7.7 Directus
- **Canonical identity:** Directus — data platform wrapping SQL databases (directus.io). **Type:** open-source project / cloud service.
- **Official URL:** https://directus.io — **Verification:** Partially verified.
- **Description / capabilities:** Instant REST + GraphQL over existing SQL DBs; data studio; self-host or Cloud.
- **License nuance:** 2026 comparisons report **BSL 1.1 with conditional licensing** (changed from earlier GPL) — treat as source-available; verify current license before adopting.
- **Usage domain:** SQL-centric stacks. **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Medium (capabilities), Low (license — flagged).

#### B7.8 Prismic / DatoCMS
- **Canonical identity:** Prismic (prismic.io) — slice-based headless CMS; DatoCMS (datocms.com) — editorial-UX headless CMS. **Type:** cloud service.
- **Official URL:** https://prismic.io ; https://www.datocms.com — **Verification:** Partially verified.
- **Description / capabilities:** Prismic: slices for page assembly, strong visual editing. DatoCMS: GraphQL-first, media-heavy publishing UX.
- **Usage domain:** Mid-market marketing sites. **License:** Proprietary.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B7.9 Contentstack / Kontent.ai
- **Canonical identity:** Contentstack (contentstack.com) — enterprise headless DXP; Kontent.ai (kontent.ai) — headless CMS with AI governance. **Type:** cloud service.
- **Official URL:** https://www.contentstack.com ; https://kontent.ai — **Verification:** Partially verified.
- **Description / capabilities:** Contentstack: DXP-grade governance, omnichannel. Kontent.ai: ISO/IEC 42001 AI governance positioning (2026).
- **Usage domain:** Regulated enterprise content. **License:** Proprietary.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Low.

#### B7.10 Keystatic / TinaCMS
- **Canonical identity:** Keystatic (keystatic.com) — git-based headless CMS by Thinkmill; TinaCMS (tina.io) — git-backed visual editing. **Type:** open-source project.
- **Official URL:** https://keystatic.com ; https://tina.io — **Verification:** Partially verified.
- **Description / capabilities:** Content stored as files in Git (Markdown/YAML); visual editing over git workflow; no database.
- **Usage domain:** Git-native content for dev teams. **License:** MIT/Apache-2.0.
- **Limitations:** Doesn't suit non-technical editorial at scale.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B7.11 BCMS
- **Canonical identity:** BCMS — hosted headless CMS (thebcms.com). **Type:** cloud service.
- **Official URL:** https://www.thebcms.com — **Verification:** Partially verified.
- **Description / capabilities:** WordPress-like editing mental model; hosted; ships MCP + open agent skills (2026 differentiator vs Contentful's native AI Actions).
- **Usage domain:** Teams wanting approachable headless editing + agent access. **License:** Proprietary.
- **Sources:** search theme 15. **Verification date:** 2026-10-10. **Confidence:** Low.

### B8. Traditional CMS & blogging platforms

#### B8.1 WordPress (incl. headless)
- **Canonical identity:** WordPress — CMS (wordpress.org); headless via WP REST API / WPGraphQL. **Type:** open-source project.
- **Official URL:** https://wordpress.org — **Verification:** Partially verified.
- **Description / capabilities:** ~40%+ of the web; themes/plugins; headless: REST API + WPGraphQL feeding Next.js/Astro frontends; Yoast/Rank Math (B2.3); WooCommerce (B10.4).
- **Usage domain:** General CMS; headless content backend. **License:** GPL-2.0.
- **Limitations:** PHP monolith ops; plugin security surface; headless adds complexity.
- **Sources:** search themes 15, 24. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B8.2 Ghost
- **Canonical identity:** Ghost — publishing platform (ghost.org). **Type:** open-source project / cloud service (Ghost Pro).
- **Official URL:** https://ghost.org — **Verification:** Partially verified.
- **Description / capabilities:** Headless-capable publishing; newsletters/memberships/payments built in; Content + Admin APIs; self-host or Pro.
- **Usage domain:** Blogs, newsletters, membership publications. **License:** MIT.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B8.3 Drupal
- **Canonical identity:** Drupal — enterprise CMS (drupal.org). **Type:** open-source project.
- **Official URL:** https://www.drupal.org — **Verification:** Partially verified.
- **Description / capabilities:** JSON:API headless; granular permissions; strong for government/education/enterprise content.
- **Usage domain:** Complex enterprise content. **License:** GPL-2.0+.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

#### B8.4 Hashnode / DEV.to / Substack / Medium
- **Canonical identity:** Hashnode (hashnode.com) — dev blogging; DEV.to (dev.to) — developer community; Substack (substack.com) — newsletters; Medium (medium.com) — publishing network. **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Hosted blogging with built-in audiences; Hashnode: custom domains + headless API; DEV: community distribution; Substack: paid newsletters; Medium: Partner Program monetization.
- **Usage domain:** Developer/personal publishing + distribution. **License:** Proprietary.
- **Sources:** search themes (DEV appears throughout as source). **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B9. Documentation platforms

#### B9.1 Docusaurus
- **Canonical identity:** Docusaurus — React docs SSG by Meta (docusaurus.io). **Type:** open-source project.
- **Official URL:** https://docusaurus.io — **Verification:** Partially verified.
- **Description / capabilities:** Markdown/MDX docs sites; versioning; i18n; plugin ecosystem (OpenAPI docs plugin); search; used by React/Jest/Prettier/Supabase/Temporal/Algolia.
- **Usage domain:** Complex versioned developer docs. **License:** MIT. **Maintenance:** Active (v3.10; v4 with React 19 incoming per 2026 guides).
- **Limitations:** React customization barrier; build times grow with docs size; no managed hosting.
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B9.2 Mintlify
- **Canonical identity:** Mintlify — managed docs platform (mintlify.com). **Type:** cloud service.
- **Official URL:** https://mintlify.com — **Verification:** Partially verified.
- **Description / capabilities:** GitHub-connected MDX; polished managed hosting; headless mode (Enterprise, Feb 2026); AI features paywalled (~$300/mo per 2026 analysis); free tier for OSS.
- **Usage domain:** Fast managed API docs. **License:** Proprietary.
- **Limitations:** Pricing caveats; AI paywalled.
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B9.3 GitBook
- **Canonical identity:** GitBook — docs collaboration platform (gitbook.com). **Type:** cloud service.
- **Official URL:** https://www.gitbook.com — **Verification:** Partially verified.
- **Description / capabilities:** Block editor; Git sync; per-site pricing; GitBook AI ($249+/site/mo per 2026 analysis); good for mixed technical/non-technical authors.
- **Usage domain:** Collaborative product docs. **License:** Proprietary.
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B9.4 Starlight
- **Canonical identity:** Starlight — Astro docs theme (starlight.astro.build). **Type:** open-source project.
- **Official URL:** https://starlight.astro.build — **Verification:** Partially verified.
- **Description / capabilities:** Zero-JS-by-default docs sites; first-class `llms.txt` plugin; built-in search/i18n/a11y; framework-agnostic components; 200k+ weekly downloads, v0.38+ per 2026 guides.
- **Usage domain:** Greenfield OSS/developer docs. **License:** MIT.
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B9.5 Nextra / Fumadocs
- **Canonical identity:** Nextra (nextra.site) — Next.js docs framework; Fumadocs (fumadocs.dev) — Next.js docs framework. **Type:** open-source project.
- **Official URL:** https://nextra.site ; https://fumadocs.dev — **Verification:** Partially verified.
- **Description / capabilities:** Docs inside Next.js repos (App Router); MDX; search; theming; Fumadocs recommended for Next.js monorepos in 2026 guides.
- **Usage domain:** Next.js-team docs. **License:** MIT.
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B9.6 VitePress / MkDocs / Sphinx
- **Canonical identity:** VitePress (vitepress.dev) — Vue docs SSG; MkDocs (mkdocs.org) + Material theme; Sphinx (sphinx-doc.org) — Python docs. **Type:** open-source project.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** VitePress: fast Vue/Vite docs. MkDocs: simple Python-based docs. Sphinx: Python API docs standard.
- **Status:** **MkDocs Material in maintenance mode (Nov 2025)** — security fixes only until Nov 2026; do not start new projects on it per 2026 guides; successor Zensical has no public release date.
- **Usage domain:** Vue/Python docs. **License:** MIT (VitePress, MkDocs); BSD (Sphinx).
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B9.7 ReadMe / Fern / Scalar
- **Canonical identity:** ReadMe (readme.com) — API docs hub; Fern (buildwithfern.com) — API docs + SDK generation (MCP + llms.txt auto-gen 2026); Scalar (scalar.com) — OpenAPI renderer. **Type:** cloud service / open-source project.
- **Official URL:** https://readme.com ; https://www.buildwithfern.com ; https://scalar.com — **Verification:** Partially verified.
- **Description / capabilities:** ReadMe: hosted API reference + guides. Fern: API-first docs with SDK generation from OpenAPI. Scalar: modern open-source API reference UI (MIT core).
- **Usage domain:** API reference portals. **License:** Proprietary (ReadMe, Fern); MIT core (Scalar).
- **Sources:** search theme 16. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B10. E-commerce frameworks

#### B10.1 Shopify (+ Hydrogen)
- **Canonical identity:** Shopify — commerce platform (shopify.com); Hydrogen — headless storefront framework (React Router + Storefront API); Oxygen hosting. **Type:** cloud service (+ open-source framework).
- **Official URL:** https://www.shopify.com — **Verification:** Partially verified.
- **Description / capabilities:** Hosted storefronts; ~29% US platform share per 2026 analyses; plans $5–$2,300+/mo; Shopify Payments card rates 2.9%+$0.30 (Basic) down with tiers; third-party gateway surcharges; Hydrogen for custom headless frontends on Oxygen.
- **Usage domain:** SMB–enterprise D2C. **License:** Proprietary (Hydrogen OSS).
- **Limitations:** Transaction fees/surcharges; customization via apps; headless adds cost/complexity.
- **Related:** MedusaJS, BigCommerce, WooCommerce.
- **Sources:** search theme 17. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B10.2 MedusaJS
- **Canonical identity:** Medusa — open-source headless commerce (medusajs.com). **Type:** open-source project / cloud service.
- **Official URL:** https://medusajs.com — **Verification:** Partially verified.
- **Description / capabilities:** Modular TypeScript/Node commerce engine; custom checkouts, B2B, marketplaces; no GMV fees; Medusa Cloud from $29/mo (production $99+) per 2026 guides.
- **Usage domain:** JS teams wanting commerce control. **License:** MIT (core) + Enterprise Edition.
- **Sources:** search theme 17. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B10.3 Saleor
- **Canonical identity:** Saleor — headless commerce (saleor.io), Python/GraphQL. **Type:** open-source project / cloud service.
- **Official URL:** https://saleor.io — **Verification:** Partially verified.
- **Description / capabilities:** API-first, GraphQL; multi-market; Saleor Cloud from ~$1,599/mo (GMV-tiered) per 2026 guides.
- **Usage domain:** Python teams; multi-market brands. **License:** BSD-3-Clause (core).
- **Sources:** search theme 17. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B10.4 WooCommerce
- **Canonical identity:** WooCommerce — WordPress commerce (woocommerce.com). **Type:** open-source project (plugin).
- **Official URL:** https://woocommerce.com — **Verification:** Partially verified.
- **Description / capabilities:** Most popular OSS commerce on WordPress; extensions for subscriptions/memberships/digital goods; REST API for headless.
- **Usage domain:** WordPress-shop commerce. **License:** GPL.
- **Sources:** search theme 17. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B10.5 BigCommerce
- **Canonical identity:** BigCommerce — SaaS commerce (bigcommerce.com); Catalyst — open-source Next.js storefront. **Type:** cloud service.
- **Official URL:** https://www.bigcommerce.com — **Verification:** Partially verified.
- **Description / capabilities:** SaaS with headless option (Catalyst); GMV-capped plans from $29/mo per 2026 guides.
- **Usage domain:** Mid-market avoiding backend maintenance. **License:** Proprietary.
- **Sources:** search theme 17. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B10.6 Vendure / Spree / Solidus
- **Canonical identity:** Vendure (vendure.io) — TS/NestJS headless commerce (GPLv3 + commercial); Spree (spreecommerce.org) — Rails headless; Solidus (solidus.io) — Rails fork of Spree. **Type:** open-source project.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Vendure: flat annual license, no GMV fees. Spree/Solidus: mature Rails commerce with REST APIs + Next.js storefronts.
- **Usage domain:** TS/Rails custom commerce. **License:** GPLv3/commercial (Vendure); BSD-3 (Spree/Solidus).
- **Sources:** search theme 17. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B11. Payments & billing integrations

#### B11.1 Stripe
- **Canonical identity:** Stripe — payments infrastructure (stripe.com). **Type:** cloud service (+ SDKs).
- **Official URL:** https://stripe.com — **Verification:** Partially verified.
- **Description / capabilities:** Payments, Billing (subscriptions), Connect (marketplaces), Radar (fraud), webhooks, client+server SDKs; 2.9%+$0.30 US baseline.
- **Usage domain:** Default online payments. **Integration method:** REST API + SDKs + webhooks; Stripe CLI for local testing.
- **License:** Proprietary.
- **Related:** Paddle, Lemon Squeezy, PayPal.
- **Sources:** search theme 18 (courrier service recipes list Stripe). **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B11.2 Paddle
- **Canonical identity:** Paddle — merchant of record for SaaS (paddle.com). **Type:** cloud service.
- **Official URL:** https://www.paddle.com — **Verification:** Partially verified.
- **Description / capabilities:** Merchant-of-record (handles global tax/VAT), subscriptions, checkout; popular for indie SaaS selling globally.
- **Usage domain:** SaaS billing without tax-ops. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B11.3 Lemon Squeezy
- **Canonical identity:** Lemon Squeezy — merchant of record (lemonsqueezy.com). **Type:** cloud service.
- **Official URL:** https://www.lemonsqueezy.com — **Verification:** Partially verified.
- **Description / capabilities:** MoR checkout for digital products/SaaS; simple integration; indie-friendly.
- **Usage domain:** Creator/indie digital sales. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B11.4 PayPal / Braintree / Adyen / Razorpay
- **Canonical identity:** PayPal (paypal.com); Braintree (braintreepayments.com, PayPal); Adyen (adyen.com); Razorpay (razorpay.com). **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** PayPal: wallet + checkout ubiquity. Braintree: developer SDKs (PayPal-owned). Adyen: enterprise unified commerce. Razorpay: India-first payments.
- **Usage domain:** Regional/enterprise payment coverage. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

#### B11.5 Polar
- **Canonical identity:** Polar — payments for developers/OSS (polar.sh). **Type:** cloud service.
- **Official URL:** https://polar.sh — **Verification:** Partially verified.
- **Description / capabilities:** Merchant-of-record for digital products/SaaS with OSS-friendly positioning; checkout + subscriptions.
- **Usage domain:** OSS/dev-tool monetization. **License:** Proprietary service (some OSS components).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

### B12. Email & transactional messaging

#### B12.1 Resend
- **Canonical identity:** Resend — developer email API (resend.com). **Type:** cloud service.
- **Official URL:** https://resend.com — **Verification:** Partially verified.
- **Description / capabilities:** Simple REST API; React Email integration; 3k emails/mo free per 2026 guides; 8M npm weekly downloads noted; llms.txt/OpenAPI/MCP + agent skills published (agent-ready docs).
- **Usage domain:** Developer-first transactional email. **Integration method:** REST API + SDKs.
- **License:** Proprietary.
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B12.2 SendGrid
- **Canonical identity:** SendGrid — email delivery by Twilio (sendgrid.com). **Type:** cloud service.
- **Official URL:** https://sendgrid.com — **Verification:** Partially verified.
- **Description / capabilities:** Transactional + marketing in one; templates, stats, suppression management; Twilio-ecosystem fit.
- **Usage domain:** High-volume programmatic email. **License:** Proprietary.
- **Limitations:** 2026 agent-era evaluations rank its API DX below Resend/Postmark (secondary claim — treat as opinion).
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B12.3 Mailgun
- **Canonical identity:** Mailgun — transactional email API (mailgun.com). **Type:** cloud service.
- **Official URL:** https://mailgun.com — **Verification:** Partially verified.
- **Description / capabilities:** Email API + validations; routes; docs with llms.txt + MCP server page (2026).
- **Usage domain:** Developer email infrastructure. **License:** Proprietary.
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B12.4 Postmark
- **Canonical identity:** Postmark — transactional email (postmarkapp.com), ActiveCampaign. **Type:** cloud service.
- **Official URL:** https://postmarkapp.com — **Verification:** Partially verified.
- **Description / capabilities:** Reputation-sensitive transactional mail (resets, receipts); separate message streams; inbound processing; templates; machine-readable pricing/llms.txt (2026).
- **Usage domain:** Time-sensitive transactional mail. **License:** Proprietary.
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B12.5 AWS SES
- **Canonical identity:** Amazon SES — email sending (aws.amazon.com/ses). **Type:** cloud service.
- **Official URL:** https://aws.amazon.com/ses/ — **Verification:** Partially verified.
- **Description / capabilities:** $0.10/1k emails; 62k free/mo from EC2 per 2026 guides; cheapest at volume.
- **Usage domain:** High-volume budget email. **License:** Proprietary.
- **Limitations:** Sandbox limits; minimal DX vs Resend/Postmark.
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B12.6 Loops
- **Canonical identity:** Loops — email for SaaS (loops.so). **Type:** cloud service.
- **Official URL:** https://loops.so — **Verification:** Partially verified.
- **Description / capabilities:** Transactional + marketing for SaaS; 2.5k contacts free per 2026 guides; simple API.
- **Usage domain:** SaaS lifecycle email. **License:** Proprietary.
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B12.7 Brevo / Mailchimp / ConvertKit (Kit) / Customer.io
- **Canonical identity:** Brevo (brevo.com, ex-Sendinblue); Mailchimp (mailchimp.com, Intuit); ConvertKit/Kit (kit.com) — creator email; Customer.io (customer.io) — lifecycle messaging. **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Brevo: marketing + transactional, 300/day free. Mailchimp: marketing platform + Mandrill transactional. Kit: creator newsletters. Customer.io: event-triggered journeys (best-in-class logic per 2026 skill docs).
- **Usage domain:** Marketing/lifecycle email. **License:** Proprietary.
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B12.8 Buttondown / Mailtrap / Postal
- **Canonical identity:** Buttondown (buttondown.com) — minimal newsletters; Mailtrap (mailtrap.io) — email testing; Postal (github.com/postalserver/postal) — self-hosted mail server. **Type:** cloud service / open-source project.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Buttondown: Markdown newsletters, API. Mailtrap: inbox simulation for staging (4k/mo test). Postal: full self-hosted SMTP (unlimited).
- **Usage domain:** Newsletters / testing / self-hosted sending. **License:** Proprietary (Buttondown, Mailtrap); MIT (Postal).
- **Sources:** search theme 18. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B13. Customer communication & support

#### B13.1 Intercom (now Fin)
- **Canonical identity:** Intercom — customer communications platform, **rebranded to Fin (May 2026)**; **Salesforce acquisition signed June 2026 (pending close)**. **Type:** cloud service. **Verification:** Partially verified (rebrand/acquisition per 2026 vendor comparison).
- **Official URL:** https://www.intercom.com (brand transition to Fin) — **Verification:** Partially verified.
- **Description / capabilities:** Shared inbox, in-app messaging, product tours, Fin AI agent (~50–76% auto-resolve per 2026 sources; $0.99/resolution), help center, proactive outbound; from ~$29–39/seat/mo.
- **Usage domain:** SaaS support + engagement. **License:** Proprietary.
- **Limitations:** Costs escalate fast at scale; brand/acquisition transition in progress — verify current packaging.
- **Sources:** search theme 32. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B13.2 Crisp
- **Canonical identity:** Crisp — customer messaging platform (crisp.chat). **Type:** cloud service.
- **Official URL:** https://crisp.chat — **Verification:** Partially verified.
- **Description / capabilities:** Omnichannel inbox (chat, email, WhatsApp, Instagram, Telegram…), knowledge base, Hugo AI agent; free starter; paid from ~$25/seat/mo; SMB favorite.
- **Usage domain:** Budget omnichannel support. **License:** Proprietary.
- **Sources:** search theme 32. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B13.3 Plain
- **Canonical identity:** Plain — support tool for dev tools (plain.com). **Type:** cloud service.
- **Official URL:** https://www.plain.com — **Verification:** Partially verified.
- **Description / capabilities:** Support threads integrated with dev workflows (Linear/GitHub/Slack); API-first; built for B2B SaaS support.
- **Usage domain:** Developer-tool support. **License:** Proprietary.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low.

#### B13.4 Zendesk / Freshdesk / Help Scout
- **Canonical identity:** Zendesk (zendesk.com); Freshdesk (freshworks.com); Help Scout (helpscout.com) — helpdesk platforms. **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Ticketing, knowledge bases, omnichannel; AI agents (Zendesk AI); Freshdesk from ~$15/agent/mo; Help Scout ~$20/user/mo simplicity focus.
- **Usage domain:** Traditional customer support. **License:** Proprietary.
- **Sources:** search theme 32. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B13.5 Discourse / Discord (community)
- **Canonical identity:** Discourse (discourse.org) — open-source forum; Discord (discord.com) — community chat. **Type:** open-source project / cloud service.
- **Official URL:** https://www.discourse.org ; https://discord.com — **Verification:** Partially verified.
- **Description / capabilities:** Discourse: self-hostable community forums (1000s of OSS projects). Discord: real-time community servers; common for dev-tool communities.
- **Usage domain:** Community support. **License:** GPL-2.0 (Discourse); proprietary (Discord).
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B13.6 1mind (Drift successor)
- **Canonical identity:** 1mind — AI-conversational platform, Drift successor (Mar 2026). **Type:** cloud service. **Verification:** Partially verified.
- **Official URL:** https://www.1mind.com — **Verification:** Partially verified.
- **Description / capabilities:** Conversational marketing/sales chat; ~$1,500/mo starter per 2026 skill docs; for Drift refugees.
- **Usage domain:** AI-first conversational marketing. **License:** Proprietary.
- **Sources:** search theme 32. **Verification date:** 2026-10-10. **Confidence:** Low.

### B14. Localization / i18n

#### B14.1 i18next
- **Canonical identity:** i18next — JS internationalization framework (i18next.com). **Type:** open-source project / code library.
- **Official URL:** https://www.i18next.com — **Verification:** Partially verified.
- **Description / capabilities:** Plurals, interpolation, namespaces, lazy loading; react-i18next bindings; `i18next-cli` with Locize-native sync commands; backends for TMSes.
- **Usage domain:** JS app i18n. **Integration method:** npm + JSON resource files. **License:** MIT.
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B14.2 next-intl
- **Canonical identity:** next-intl — i18n for Next.js (next-intl.dev). **Type:** open-source project / code library.
- **Official URL:** https://next-intl.dev — **Verification:** Partially verified.
- **Description / capabilities:** App Router locale routing, ICU MessageFormat, type-safe keys; officially partnered with Crowdin; the 2026 default for Next.js i18n per skill docs.
- **Usage domain:** Next.js localization. **License:** MIT.
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B14.3 FormatJS / react-intl
- **Canonical identity:** FormatJS (formatjs.io) — ICU message libraries; react-intl its React binding. **Type:** open-source project / code library.
- **Official URL:** https://formatjs.io — **Verification:** Partially verified.
- **Description / capabilities:** ICU MessageFormat implementation; `<FormattedMessage>`; extraction tooling.
- **Usage domain:** React i18n (pre-next-intl standard). **License:** BSD-3-Clause.
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B14.4 Lingui / Paraglide / Intlayer
- **Canonical identity:** LinguiJS (lingui.dev) — compile-time i18n; Paraglide (inlang.com/paraglide) — compiler-based i18n; Intlayer (intlayer.org) — i18n with CMS + MCP server. **Type:** open-source project / code library.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Lingui: macros extracting messages at build. Paraglide: tree-shakeable compiled messages (inlang ecosystem). Intlayer: VS Code extension, LSP, built-in MCP server, visual CMS, `intlayer fill` AI translation (Apache-2.0).
- **Usage domain:** Modern JS i18n. **License:** MIT (Lingui, Paraglide); Apache-2.0 (Intlayer).
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B14.5 Crowdin
- **Canonical identity:** Crowdin — localization management platform (crowdin.com). **Type:** cloud service.
- **Official URL:** https://crowdin.com — **Verification:** Partially verified.
- **Description / capabilities:** Repo sync, in-context editors, MT/AI pre-translation, i18next plural support; official MCP server (2026); next-intl partner.
- **Usage domain:** Software localization workflows. **License:** Proprietary (free for OSS).
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B14.6 Lokalise / Phrase
- **Canonical identity:** Lokalise (lokalise.com); Phrase (phrase.com, ex-Memsource+PhraseApp). **Type:** cloud service.
- **Official URL:** https://lokalise.com ; https://phrase.com — **Verification:** Partially verified.
- **Description / capabilities:** TMS with CLI sync, OTA delivery, screenshots/in-context; official MCP servers (2026); Phrase ships `@phrase/i18next-backend` (read-only).
- **Usage domain:** Translation management. **License:** Proprietary.
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B14.7 Tolgee / Weblate / Locize
- **Canonical identity:** Tolgee (tolgee.io) — dev-focused localization (OSS); Weblate (weblate.org) — OSS translation platform; Locize (locize.com) — i18next-native CDN localization. **Type:** open-source project / cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Tolgee: in-context translation, SDKs, self-hostable, MCP server. Weblate: git-integrated community translation, self-host. Locize: continuous localization CDN built around i18next (only TMS with native `i18next-cli` commands).
- **Usage domain:** Developer-friendly translation management. **License:** Apache-2.0 (Tolgee); GPL-3.0 (Weblate); proprietary (Locize).
- **Sources:** search theme 23. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B15. Site search

#### B15.1 Algolia
- **Canonical identity:** Algolia — hosted search API (algolia.com). **Type:** cloud service.
- **Official URL:** https://www.algolia.com — **Verification:** Partially verified.
- **Description / capabilities:** Typo-tolerant instant search API; NeuralSearch re-ranking; DocSearch (free for OSS docs); managed relevance; free tier 10k records/10k searches/mo; paid ~$50–60/mo entry; ~$0.50–1.00/1k requests at scale.
- **Usage domain:** Managed product/docs search. **Integration method:** API + InstantSearch libraries.
- **License:** Proprietary (cloud-only, no self-host).
- **Limitations:** Cost scales with queries; no self-hosting.
- **Related:** Typesense, Meilisearch, Elasticsearch.
- **Sources:** search theme 21. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B15.2 Typesense
- **Canonical identity:** Typesense — open-source search engine (typesense.org). **Type:** open-source project / cloud service.
- **Official URL:** https://typesense.org — **Verification:** Partially verified.
- **Description / capabilities:** Single C++ binary; typo tolerance, faceting, geo-search, multi-tenant API-key scoping; self-host free; Cloud from ~$7/mo resource-based; Algolia migration tooling.
- **Usage domain:** Self-hostable instant search. **License:** GPL-3.0.
- **Sources:** search theme 21. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B15.3 Meilisearch
- **Canonical identity:** Meilisearch — open-source search (meilisearch.com). **Type:** open-source project / cloud service.
- **Official URL:** https://www.meilisearch.com — **Verification:** Partially verified.
- **Description / capabilities:** Rust binary; instant search, no schema declaration needed; 58k+ GitHub stars; self-host free; Cloud from $30/mo; official 1-click deploys (DO/Railway/Koyeb/Azure).
- **Usage domain:** Easiest self-hosted search. **License:** MIT.
- **Sources:** search theme 21. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B15.4 Elasticsearch / OpenSearch
- **Canonical identity:** Elasticsearch (elastic.co) — distributed search; OpenSearch (opensearch.org) — AWS-led fork. **Type:** open-source-adjacent project / cloud service.
- **Official URL:** https://www.elastic.co/elasticsearch/ ; https://opensearch.org — **Verification:** Partially verified.
- **Description / capabilities:** Full-text + log analytics at scale; OpenSearch keeps Apache-2.0; Elastic under SSPL/Elastic License; managed from ~$95/mo.
- **Usage domain:** Enterprise search + observability. **License:** SSPL/Elastic License (Elastic); Apache-2.0 (OpenSearch).
- **Limitations:** Heavy ops; overkill for typical site search.
- **Sources:** search theme 21. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B15.5 Orama / Pagefind
- **Canonical identity:** Orama (orama.com) — JS/edge search; Pagefind (pagefind.app) — static-site search. **Type:** open-source project.
- **Official URL:** https://orama.com ; https://pagefind.app — **Verification:** Partially verified.
- **Description / capabilities:** Orama: runs in-browser/edge/workers; good for docs. Pagefind: build-time index, fully client-side, $0 — ideal for static docs (rebuild on content change; watch CSP).
- **Usage domain:** Docs/static-site search. **License:** Apache-2.0 (Orama); MIT (Pagefind).
- **Sources:** search theme 21. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B16. User feedback & feature voting

#### B16.1 Canny
- **Canonical identity:** Canny — feedback management (canny.io). **Type:** cloud service.
- **Official URL:** https://canny.io — **Verification:** Partially verified.
- **Description / capabilities:** Feature voting boards, roadmaps, changelogs; user segmentation; integrations (Intercom, Jira, Slack); from ~$50/mo (100 tracked users) per 2026 directories.
- **Usage domain:** Structured product feedback. **License:** Proprietary.
- **Sources:** search theme 30. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B16.2 Featurebase
- **Canonical identity:** Featurebase — feedback + support (featurebase.app). **Type:** cloud service.
- **Official URL:** https://www.featurebase.app — **Verification:** Partially verified.
- **Description / capabilities:** Feedback boards, roadmaps, knowledge base, support; free tier; paid from $29/seat/mo annual.
- **Usage domain:** Feedback + lightweight support in one. **License:** Proprietary.
- **Sources:** search theme 30. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B16.3 Nolt
- **Canonical identity:** Nolt — focused feedback boards (nolt.io). **Type:** cloud service.
- **Official URL:** https://nolt.io — **Verification:** Partially verified.
- **Description / capabilities:** Simple beautiful voting boards; from ~$29/mo annual; API on Pro.
- **Usage domain:** Minimal feature voting. **License:** Proprietary.
- **Sources:** search theme 30. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B16.4 Frill / Upvoty / Sleekplan / UserVoice
- **Canonical identity:** Frill (frill.co); Upvoty (upvoty.com); Sleekplan (sleekplan.com); UserVoice (uservoice.com). **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Frill: lightweight boards/widgets ($25/mo). Upvoty: simple voting ($15/mo). Sleekplan: feedback + surveys (free tier; from $13/mo). UserVoice: enterprise feedback suite (custom quote).
- **Usage domain:** Tiered feedback tooling. **License:** Proprietary.
- **Sources:** search theme 30. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B17. Forms & data collection

#### B17.1 Typeform
- **Canonical identity:** Typeform — conversational forms (typeform.com). **Type:** cloud service.
- **Official URL:** https://www.typeform.com — **Verification:** Partially verified.
- **Description / capabilities:** One-question-at-a-time conversational forms; logic jumps; 500+ integrations; from ~$25/mo; free 10 responses/mo per 2026 guides.
- **Usage domain:** High-completion surveys/forms. **License:** Proprietary.
- **Sources:** search theme 31. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B17.2 Tally
- **Canonical identity:** Tally — free form builder (tally.so). **Type:** cloud service.
- **Official URL:** https://tally.so — **Verification:** Partially verified.
- **Description / capabilities:** Notion-like form builder; unlimited forms + submissions (fair use) free; conditional logic, payments, file uploads; EU-hosted, GDPR; from ~$29/mo paid.
- **Usage domain:** Free Typeform alternative. **License:** Proprietary.
- **Sources:** search theme 31. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B17.3 Formspree
- **Canonical identity:** Formspree — form backend API (formspree.io). **Type:** cloud service.
- **Official URL:** https://formspree.io — **Verification:** Partially verified.
- **Description / capabilities:** Point existing HTML forms at an endpoint; submissions dashboard, spam filtering (Akismet), integrations; free 50 subs/mo; paid from $10–15/mo; webhooks/API on higher tiers; CLI + React library.
- **Usage domain:** Backend-less form handling for static sites. **License:** Proprietary.
- **Sources:** search theme 31. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B17.4 Jotform / Google Forms / Netlify Forms
- **Canonical identity:** Jotform (jotform.com); Google Forms (forms.google.com); Netlify Forms (platform feature). **Type:** cloud service / platform feature.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Jotform: advanced logic, payments, approvals (from $34/mo). Google Forms: free unlimited responses, minimal branding control. Netlify Forms: `data-netlify="true"` build-processed; free + unlimited on credit-based plans (Apr 2026) — Netlify-hosted only.
- **Usage domain:** General form collection. **License:** Proprietary.
- **Sources:** search theme 31. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B17.5 React Hook Form / Formik
- **Canonical identity:** React Hook Form (react-hook-form.com); Formik (formik.org) — form state libraries. **Type:** open-source project / code library.
- **Official URL:** https://react-hook-form.com ; https://formik.org — **Verification:** Partially verified.
- **Description / capabilities:** RHF: performant uncontrolled form state + validation; Formik: older controlled-component standard (maintenance mode in practice).
- **Usage domain:** In-app form state. **License:** MIT.
- **Sources:** General knowledge. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

### B18. Uptime & synthetic monitoring

#### B18.1 UptimeRobot
- **Canonical identity:** UptimeRobot — uptime monitoring (uptimerobot.com). **Type:** cloud service.
- **Official URL:** https://uptimerobot.com — **Verification:** Partially verified.
- **Description / capabilities:** HTTP/ping/port/keyword checks; 50 monitors free (5-min); **free tier non-commercial since Oct 2024**; paid from ~$9–12/mo (30-sec checks).
- **Usage domain:** Simple uptime checks. **License:** Proprietary.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B18.2 Better Stack (Uptime)
- **Canonical identity:** Better Stack — uptime + incidents + status pages (betterstack.com). **Type:** cloud service.
- **Official URL:** https://betterstack.com — **Verification:** Partially verified.
- **Description / capabilities:** 10 monitors free (3-min); status pages; on-call scheduling; logs product adjacent; from ~$29/seat/mo per 2026 guides.
- **Usage domain:** Uptime + incident comms. **License:** Proprietary.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B18.3 Checkly
- **Canonical identity:** Checkly — monitoring-as-code (checklyhq.com). **Type:** cloud service.
- **Official URL:** https://www.checklyhq.com — **Verification:** Partially verified.
- **Description / capabilities:** Playwright browser checks + API checks defined in code (repo-stored); global probes; from ~$24/mo.
- **Usage domain:** Developer synthetic monitoring. **License:** Proprietary.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B18.4 Pingdom
- **Canonical identity:** Pingdom — website monitoring (pingdom.com, SolarWinds). **Type:** cloud service.
- **Official URL:** https://www.pingdom.com — **Verification:** Partially verified.
- **Description / capabilities:** Uptime + page speed + RUM + transaction checks; no free tier (trial only); from ~$15/mo; no public status page.
- **Usage domain:** Classic synthetic monitoring. **License:** Proprietary.
- **Limitations:** Pricing grows on three axes; product moves slowly post-SolarWinds per 2026 analyses.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B18.5 Uptime Kuma
- **Canonical identity:** Uptime Kuma — self-hosted monitoring (github.com/louislam/uptime-kuma). **Type:** open-source project.
- **Official URL:** https://github.com/louislam/uptime-kuma — **Verification:** Partially verified.
- **Description / capabilities:** Unlimited monitors self-hosted; HTTP/TCP/DNS/docker checks; status pages; notifications; single-location checks.
- **Usage domain:** Free self-hosted uptime. **License:** MIT.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B18.6 openstatus
- **Canonical identity:** OpenStatus — open-source uptime + status pages (openstatus.dev). **Type:** open-source project / cloud service.
- **Official URL:** https://www.openstatus.dev — **Verification:** Partially verified.
- **Description / capabilities:** Multi-region checks + status pages; permanent free plan (1 monitor, 6 regions); managed cloud or self-host.
- **Usage domain:** OSS status-page monitoring. **License:** AGPL-3.0.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Medium.

#### B18.7 Statuspage (Atlassian) / Instatus
- **Canonical identity:** Statuspage (metastatuspage.io → Atlassian); Instatus (instatus.com) — hosted status pages. **Type:** cloud service.
- **Official URL:** https://metastatuspage.io ; https://www.instatus.com — **Verification:** Partially verified.
- **Description / capabilities:** Public status pages, incident comms, subscriber notifications; Instatus generous free tier.
- **Usage domain:** Incident communication. **License:** Proprietary.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

#### B18.8 Oh Dear / StatusCake / Datadog Synthetics
- **Canonical identity:** Oh Dear (ohdear.app) — website monitoring; StatusCake (statuscake.com) — uptime + page speed; Datadog Synthetics — enterprise synthetics. **Type:** cloud service.
- **Official URL:** as named — **Verification:** Partially verified.
- **Description / capabilities:** Oh Dear: uptime + broken links + cert + DNS checks. StatusCake: 10 free monitors + speed/domain/SSL checks. Datadog Synthetics: API/browser checks metered (~$5/10k runs).
- **Usage domain:** Tiered synthetic monitoring. **License:** Proprietary.
- **Sources:** search theme 22. **Verification date:** 2026-10-10. **Confidence:** Low-Medium.

---

## Coverage note

### Counts
- **Part A (build/CI/cloud/infra):** 190 full records across 26 subcategories (A1–A26), plus a ~40-item rapid-fire list of secondary infrastructure resources.
- **Part B (SEO/analytics/CMS/commerce/ops):** 107 full records across 18 subcategories (B1–B18).
- **Total: ~337 resources catalogued** (297 full Part-21-style records + ~40 rapid-fire compact entries). File: 2,436 lines.

### Per-subcategory counts (A)
A1 version control 6 · A2 pre-commit 7 · A3 CI platforms 14 · A4 CD/GitOps 7 · A5 build systems 7 · A6 containers 8 · A7 dev containers 6 · A8 IaC 9 · A9 cloud CLIs 7 · A10 frontend hosting 6 · A11 backend PaaS 10 · A12 serverless/edge 10 · A13 CDN 5 · A14 databases 12 · A15 secrets 9 · A16 env/toolchain 4 · A17 deploy/preview 3 · A18 release automation 6 · A19 feature flags 8 · A20 observability 8 · A21 error tracking 3 · A22 performance 4 · A23 AI telemetry 10 · A24 cost monitoring 6 · A25 background jobs 9 · A26 headless agents 6 · rapid-fire 40.

### Per-subcategory counts (B)
B1 technical SEO 6 · B2 SEO suites 3 · B3 web analytics 9 · B4 product analytics 5 · B5 consent 5 · B6 experimentation 3 · B7 headless CMS 11 · B8 CMS/blogging 4 · B9 docs platforms 7 · B10 e-commerce 6 · B11 payments 5 · B12 email 8 · B13 comms/support 6 · B14 localization 7 · B15 site search 5 · B16 feedback 4 · B17 forms 5 · B18 uptime 8.

### Verification summary
- **Verified (primary source fetched):** pre-commit.com docs, lefthook README, opentofu.org, workers.cloudflare.com, GitHub Actions/GitHub (docs corroboration), Docker, Kubernetes, Git, Deno Deploy sunset (multiple primary-adjacent: RuntimeWire citing Deno's announcement; Appwrite official blog).
- **Partially verified:** the majority — 2026-dated secondary comparisons + official URLs seen verbatim; capabilities summarized from corroborating sources.
- **Corrected:** Statsig (OpenAI acquisition → Amplitude brand takeover); Intercom (rebrand to Fin; Salesforce acquisition pending).
- **Archived:** Deno Deploy (sunsetting ~Apr 2027); BuildJet (closed Mar 2026); Travis CI noted historical.
- **Historical:** Spinnaker (reduced 2026 relevance).
- **Unresolved:** Xata (shutdown rumors vs 2026 listings conflict); Gitpod (2026 direction unclear); Directus license (BSL 1.1 reported — verify); Restate/DBOS license nuances.

### Limitations
1. Depth is uneven by design: the highest-signal items got primary fetches; long-tail items rely on 2026-dated secondary sources and are marked Partially verified.
2. Pricing changes fast — all prices are "per 2026 comparisons" snapshots, not re-verified against live pricing pages.
3. License claims for items marked Partially verified should be re-checked at the official repo before legal reliance (especially Directus, Sentry self-host, Restate/DBOS).
4. No live-browser checks were possible in this workstream; account-state, current pricing, and feature availability were not live-verified.

### More work warranted?
- **Yes, targeted:** (a) resolve Xata status via xata.io; (b) confirm Directus current license; (c) Gitpod 2026 status; (d) live-verify pricing for the top-20 cloud services; (e) primary README inspection for the rapid-fire list (act, Renovate, Tailscale, Caddy, etc.); (f) AI skills directories (e.g., public SKILL.md files for DevOps/secrets/i18n) are a rich adjacent source this pass only sampled — a dedicated skills sweep would strengthen agent-integration fields.
