# 18 — CI/CD (Git / Worktrees / Pre-commit / CI / Actions / PR Flows / Containers / Devcontainers / IaC / Agents)

> Part 3 · B-category catalog · Infra-Ops researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> KIND LEGEND — [SERVICE] managed SaaS · [OSS] self-hostable code · [UTILITY] local CLI/lib · [INTEGRATION] plugin/adapter wiring two systems.

Scope: git/worktrees, pre-commit, CI/CD engines, Actions marketplace, PR flows (changesets/semantic-release), containers/devcontainers, IaC, headless CI agents. Hosting/edge/CDN/observability live in 19-cloud-deploy.md.

## Index (20 resources)

01 Git + Git Worktrees · 02 pre-commit framework · 03 Husky + lint-staged · 04 GitHub Actions · 05 GitLab CI/CD · 06 Jenkins · 07 CircleCI · 08 Buildkite · 09 Tekton / Argo Workflows · 10 Dagger · 11 Earthly · 12 Docker / Podman · 13 Devcontainers spec · 14 Terraform / OpenTofu · 15 Pulumi / Ansible · 16 Changesets / semantic-release (PR-flow) · 17 GitHub Flow / trunk-based + required checks · 18 Depot / BuildJet / Blacksmith (runner infra) · 19 Headless CI agents (Duo Workflow / Copilot Workspace exemplar) · 20 Spacelift / Atlantis (IaC CI/CD)

---

### 01 — Git + Git Worktrees [UTILITY]
- **Canonical identity:** `util:git` — https://git-scm.com/docs/git-worktree
- **Category:** CI/CD → VCS + parallel workspaces
- **Type:** [UTILITY] OSS CLI
- **Official URL:** https://git-scm.com/
- **Description:** Distributed VCS; `git worktree add ../hotfix` gives linked checkout per branch — parallel agent/CI lanes without stash/clone churn.
- **Contents inspected:** git-worktree docs pattern via WebSearch.
- **Capabilities:** Linked worktrees, sparse-checkout, partial clone for monorepos.
- **Usage domain:** Multi-agent parallel edits, hotfix lanes.
- **Integration:** [UTILITY] (`git worktree list/add/remove`; harness per-worktree env).
- **Compatibility:** Any Git host/CI.
- **Deps:** Git 2.20+.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** GPL-2.0.
- **Security/limits:** Per-worktree secrets isolation (no shared `.env` symlink); clean locks on abort.
- **Related:** GitHub Actions, pre-commit.
- **Sources:** git-scm.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 02 — pre-commit framework [UTILITY]
- **Canonical identity:** `util:pre-commit` — `github:pre-commit/pre-commit`
- **Category:** CI/CD → Pre-commit gates
- **Type:** [UTILITY] OSS
- **Official URL:** https://pre-commit.com/
- **Description:** `.pre-commit-config.yaml` hooks (trailing-whitespace, end-of-file, gitleaks, black/prettier/eslint, semgrep) — same hooks re-runnable in CI (`pre-commit run --all-files`).
- **Contents inspected:** Search-verified identity.
- **Capabilities:** Multi-lang hook envs, autoupdate, CI parity.
- **Usage domain:** Every commit (fast linters/secrets) before PR CI.
- **Integration:** [UTILITY] (git hooks + GHA `pre-commit/action`).
- **Compatibility:** Python/Node/Go hooks.
- **Deps:** Python + hook runtimes.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Client-side bypassable (`--no-verify`) — always re-run server-side in CI.
- **Related:** Husky, Gitleaks, Semgrep.
- **Sources:** pre-commit.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 03 — Husky + lint-staged [UTILITY]
- **Canonical identity:** `npm:husky` + `npm:lint-staged`
- **Category:** CI/CD → Git hooks (JS)
- **Type:** [UTILITY] OSS
- **Official URL:** https://typicode.github.io/husky/
- **Description:** Husky manages `.husky/` hooks; lint-staged runs formatters/linters only on staged files (fast JS DX).
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Pre-commit/pre-push lanes without full-suite cost.
- **Usage domain:** JS/TS repos complementing pre-commit framework.
- **Integration:** [UTILITY] (`npx husky init`; lint-staged config in package.json).
- **Compatibility:** Node 18+.
- **Deps:** Node.
- **Availability:** npm free.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Same bypass caveat — mirror in CI required checks.
- **Related:** pre-commit, ESLint/Prettier.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 04 — GitHub Actions [SERVICE]
- **Canonical identity:** `service:github-actions` — https://docs.github.com/actions
- **Category:** CI/CD → CI engine (market leader 2026)
- **Type:** [SERVICE] managed (+ ARC self-host)
- **Official URL:** https://docs.github.com/actions
- **Description:** Event YAML in-repo; 20k+ Marketplace actions; reusable workflows (`workflow_call`), composite actions, OIDC→AWS/GCP/Azure (no long-lived secrets), large/GPU + M2 runners; 60%+ market, 68% OSS adoption 2026.
- **Contents inspected:** JetBrains 2025 + EITT + Youngju 2026 deep-dives.
- **Capabilities:** Matrix, concurrency, environments/approvals, artifacts/cache, ARC on K8s.
- **Usage domain:** Default when code lives on GitHub (personal 39%, org 33%).
- **Integration:** [SERVICE] (uses: `actions/setup-node@v4`, `aws-actions/configure-aws-credentials`; OIDC federation).
- **Compatibility:** Linux/Win/macOS hosted + ARC.
- **Deps:** Runner minutes; secrets scoping.
- **Availability:** SaaS (2000 free min public; Teams $4/user/mo exemplar).
- **Maintenance:** Active.
- **License:** Proprietary runners; workflows user code.
- **Security/limits:** Pin actions by SHA; top-level `permissions: {}` + per-job escalation; review Marketplace scopes.
- **Related:** GitLab CI, Dagger, Argo CD (CD layer).
- **Sources:** GitHub Docs; WebSearch 2026 surveys.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 05 — GitLab CI/CD [SERVICE + OSS]
- **Canonical identity:** `service:gitlab-ci` — https://docs.gitlab.com/ee/ci/
- **Category:** CI/CD → DevSecOps platform
- **Type:** [SERVICE] SaaS + [OSS] self-managed
- **Official URL:** https://docs.gitlab.com/ee/ci/
- **Description:** `.gitlab-ci.yml` with `needs:` DAGs, Auto DevOps (SAST/DAST/container/license built-in), Runners (Docker/K8s/Shell/SSH), Duo Workflow (AI review/tests, GA 2026), CVS re-scans.
- **Contents inspected:** 2026 deep-dives (19% org adoption; 90%+ of GitLab users).
- **Capabilities:** Single-app SCM+CI+security+K8s+compliance; multi-project pipelines.
- **Usage domain:** Regulated/finance/public-sector + K8s-native teams on GitLab.
- **Integration:** [SERVICE] (pipeline editor, environments, K8s agent).
- **Compatibility:** SaaS + self-host runners.
- **Deps:** Runner infra or SaaS minutes (400 free exemplar).
- **Availability:** Open-core (Premium $29/user/mo exemplar).
- **Maintenance:** Active (17.x 2024–2026).
- **License:** MIT (CE parts); proprietary tiers.
- **Security/limits:** Best when standardized on GitLab VCS; other VCS shallowly integrated.
- **Related:** GitHub Actions, Jenkins.
- **Sources:** GitLab Docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 06 — Jenkins [OSS]
- **Canonical identity:** `oss:jenkins` — https://www.jenkins.io/
- **Category:** CI/CD → Classic automation server
- **Type:** [OSS] self-hosted (Java)
- **Official URL:** https://www.jenkins.io/
- **Description:** Declarative Jenkinsfile, Blue Ocean, 1800–20000 plugins (per source), JCasC, K8s pod-template agents, shared libs; still Fortune-500 backbone but -8% YoY, rare for greenfield.
- **Contents inspected:** 2026 verdicts (28% org use; highest TCO via maintenance).
- **Capabilities:** Multi-VCS, extreme customization, on-prem/data-residency.
- **Usage domain:** Complex legacy + banks/telcos with DevOps staff.
- **Integration:** [OSS] (plugins for every VCS/cloud/tool).
- **Compatibility:** Anywhere JVM runs; agents horizontal.
- **Deps:** Controller + agents + plugin upkeep.
- **Availability:** Free OSS (+infra/ops cost dominant).
- **Maintenance:** Active (2.x) but Hold for new (radar).
- **License:** MIT.
- **Security/limits:** Plugin sprawl = CVE surface; JCasC + pinned plugins + isolated agents mandatory.
- **Related:** TeamCity, Buildkite.
- **Sources:** jenkins.io; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 07 — CircleCI [SERVICE]
- **Canonical identity:** `service:circleci` — https://circleci.com/
- **Category:** CI/CD → Cloud-native CI
- **Type:** [SERVICE] SaaS (+ self-host runners partial)
- **Official URL:** https://circleci.com/
- **Description:** Credit-based; parallelism + orbs; leads Apple-Silicon/ARM/GPU runners; fast PR feedback for small teams.
- **Contents inspected:** 2026 roundups (cloud-native + enterprise recognized).
- **Capabilities:** Matrix, caching, parallelism controls, macOS fleet.
- **Usage domain:** Mobile + cloud-native teams needing macOS/GPU.
- **Integration:** [SERVICE] (orbs; GHA-analog YAML).
- **Compatibility:** Linux/macOS/Windows clouds.
- **Deps:** Credits.
- **Availability:** SaaS (free tier + commercial).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** OIDC + contexts for secrets; audit orb versions.
- **Related:** GHA, Buildkite.
- **Sources:** circleci.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 08 — Buildkite [SERVICE + OSS agents]
- **Canonical identity:** `service:buildkite` — https://buildkite.com/
- **Category:** CI/CD → Monorepo-scale CI
- **Type:** [SERVICE] SaaS control + [OSS] self-hosted agents
- **Official URL:** https://buildkite.com/
- **Description:** Hybrid: SaaS orchestration, user agents (Shopify/Airbnb/Lyft pattern); per-user SaaS; Bazel/Nx/Turborepo-friendly.
- **Contents inspected:** Youngju 2026 (high-end monorepo standard).
- **Capabilities:** Elastic agents, annotations, test analytics.
- **Usage domain:** Large monorepos needing self-host compute + SaaS UX.
- **Integration:** [SERVICE] (agent tokens; pipelines YAML).
- **Compatibility:** Any agent host (K8s/VM/metal).
- **Deps:** Agent fleet ops.
- **Availability:** SaaS per-user + infra.
- **Maintenance:** Active.
- **License:** Proprietary (agents OSS).
- **Security/limits:** Harden agent hosts (ephemeral, least-privilege IAM via OIDC).
- **Related:** GHA ARC, CircleCI.
- **Sources:** buildkite.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Tekton / Argo Workflows [OSS]
- **Canonical identity:** `oss:tekton` — https://tekton.dev/ ; `oss:argo-workflows` — https://argoproj.github.io/workflows/
- **Category:** CI/CD → K8s-native pipelines
- **Type:** [OSS] (CRDs on K8s)
- **Official URL:** https://tekton.dev/
- **Description:** Tekton Tasks/Pipelines/PipelineRuns (+ OpenShift Pipelines enterprise); Argo Workflows/Events/Rollouts for ML/batch/CI DAGs.
- **Contents inspected:** 2026 layer map (CI that lives inside K8s).
- **Capabilities:** Container-per-step, RBAC-native, GitOps-friendly.
- **Usage domain:** K8s-depth teams; ML/batch estates.
- **Integration:** [OSS] (kubectl/Argo CD pairing; GHA for CI → Argo CD for CD).
- **Compatibility:** K8s clusters.
- **Deps:** Cluster + artifact storage.
- **Availability:** Free OSS.
- **Maintenance:** Active (CDF/Argo).
- **License:** Apache-2.0.
- **Security/limits:** RBAC + Workload Identity per pipeline; no privileged steps.
- **Related:** Argo CD/Flux (19), Jenkins X.
- **Sources:** tekton.dev/argoproj via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — Dagger (programmable CI) [OSS + SERVICE]
- **Canonical identity:** `oss:dagger` — https://dagger.io/
- **Category:** CI/CD → Container-native programmable CI
- **Type:** [OSS] + [SERVICE] Cloud (traces/cache)
- **Official URL:** https://dagger.io/
- **Description:** Pipelines as Go/TS/Python code (not YAML); every step containerized on BuildKit; `dagger call test --source=.` — CI YAML collapses to one line; testable pipelines; Series B 2026.
- **Contents inspected:** Youngju 2026 (runs atop GHA/GitLab/Jenkins).
- **Capabilities:** Local-CI parity, content-addressed caching, parallelism graph.
- **Usage domain:** Teams hitting YAML-scale pain; Replit/Vercel/Anthropic evals 2026.
- **Integration:** [OSS] SDK + [SERVICE] Cloud viz; invoked from any CI.
- **Compatibility:** Any CI + local Docker/BuildKit.
- **Deps:** BuildKit; registry.
- **Availability:** OSS free; Cloud SaaS.
- **Maintenance:** Active (Docker-founder startup).
- **License:** Apache-2.0 (engine).
- **Security/limits:** Code-is-config — review pipeline code like app code; pin module versions.
- **Related:** Earthly, Depot.
- **Sources:** dagger.io via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 11 — Earthly (local-CI parity builds) [OSS + SERVICE]
- **Canonical identity:** `oss:earthly` — https://earthly.dev/
- **Category:** CI/CD → Build/CI unification
- **Type:** [OSS] + [SERVICE] Cloud
- **Official URL:** https://earthly.dev/
- **Description:** `Earthfile` merges Dockerfile+Makefile+CI; `earthly +docker` local == CI line; BuildKit caching consistent both sides.
- **Contents inspected:** 2026 new-category write-ups.
- **Capabilities:** Repro builds, satellites for shared cache.
- **Usage domain:** Polyglot repos wanting debug-local equality.
- **Integration:** [OSS] (one-line GHA step) + Cloud cache.
- **Compatibility:** Docker/BuildKit hosts.
- **Deps:** Registry for push.
- **Availability:** OSS free; Cloud SaaS.
- **Maintenance:** Active.
- **License:** MPL-2.0.
- **Security/limits:** Secrets via `--secret`, never ARG-baked; verify base digests.
- **Related:** Dagger, Depot.
- **Sources:** earthly.dev via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — Docker / Podman (container layer) [OSS/UTILITY]
- **Canonical identity:** `util:docker` — https://www.docker.com/ ; `util:podman` — https://podman.io/
- **Category:** CI/CD → Container runtime
- **Type:** [OSS]/[UTILITY] (Docker commercial Desktop/Hub; Podman daemonless OSS)
- **Official URL:** https://www.docker.com/
- **Description:** N/A-layer used with any CI: build/push/pull, multi-arch, layer cache; Podman rootless + systemd for hardened agents.
- **Contents inspected:** 2026 CI layer tables (Docker as execution infra).
- **Capabilities:** Repro envs, SBOM attest hooks, registry push.
- **Usage domain:** Every containerized CI/CD.
- **Integration:** [UTILITY] (`docker buildx`; podman drop-in).
- **Compatibility:** Linux; Desktop VM Mac/Win.
- **Deps:** Registry; BuildKit.
- **Availability:** OSS free (+commercial).
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Pin base by digest; `--cap-drop=ALL`, non-root, read-only where possible (see 17-security).
- **Related:** Devcontainers, Dagger/Earthly.
- **Sources:** docker.com via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — Devcontainers spec [OSS STANDARD]
- **Canonical identity:** `spec:devcontainers` — https://containers.dev/
- **Category:** CI/CD → Repro dev env
- **Type:** [OSS] standard + [UTILITY] CLI
- **Official URL:** https://containers.dev/
- **Description:** `devcontainer.json` (image/features/ports/postCreate) reproducible in VS Code/Codespaces/devpod/CI; eliminates works-on-my-machine.
- **Contents inspected:** Search-verified identity.
- **Capabilities:** Features, lifecycle scripts, GPU/mount matrix.
- **Usage domain:** Onboarding + agent sandboxes with identical toolchain.
- **Integration:** [INTEGRATION] (IDE + CI `devcontainer ci` / devpod).
- **Compatibility:** Docker/Podman backends.
- **Deps:** Container runtime.
- **Availability:** Free spec/OSS.
- **Maintenance:** Active (Microsoft-led spec).
- **License:** MIT.
- **Security/limits:** Review features (they run as root by default); pin feature versions.
- **Related:** Docker, Codespaces.
- **Sources:** containers.dev via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Terraform / OpenTofu (IaC declarative) [OSS]
- **Canonical identity:** `oss:terraform` — https://www.terraform.io/ ; `oss:opentofu` — https://opentofu.org/
- **Category:** CI/CD → IaC
- **Type:** [OSS] (Terraform BSL; OpenTofu MPL-2.0 fork)
- **Official URL:** https://opentofu.org/
- **Description:** HCL plan/apply, state, providers; OpenTofu community fork post-license change; `terraform plan` as PR check, apply on merge (Atlantis/Spacelift).
- **Contents inspected:** 2026 IaC CI/CD layer (Spacelift/Atlantis/Terragrunt/env0).
- **Capabilities:** Drift detect, policy-as-code (OPA/Checkov) gates.
- **Usage domain:** Cloud landing zones managed via PRs.
- **Integration:** [OSS] (`tofu plan/apply`; CI artifacts for plans).
- **Compatibility:** AWS/GCP/Azure/K8s providers.
- **Deps:** Remote state (S3/GCS + lock).
- **Availability:** Free OSS (Cloud SaaS optional).
- **Maintenance:** Active (both lines).
- **License:** BSL-1.1 (TF) / MPL-2.0 (Tofu).
- **Security/limits:** State holds secrets — encrypt + restrict; require human approve on apply with destroy-plan guard.
- **Related:** Pulumi, Spacelift/Atlantis.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — Pulumi / Ansible (IaC alternatives) [OSS + SERVICE]
- **Canonical identity:** `oss:pulumi` — https://www.pulumi.com/ ; `oss:ansible` — https://www.ansible.com/
- **Category:** CI/CD → IaC / config-mgmt
- **Type:** [OSS] (+ Pulumi Deployments [SERVICE])
- **Official URL:** https://www.pulumi.com/
- **Description:** Pulumi: general-purpose langs (TS/Python/Go) infra-as-code; Ansible: agentless SSH playbooks for config/drift.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Policy packs, secrets providers, idempotent playbooks.
- **Usage domain:** Code-first infra (Pulumi) + fleet config (Ansible).
- **Integration:** [OSS]/[SERVICE] (CI plan/preview → manual approve → deploy).
- **Compatibility:** Major clouds + on-prem SSH.
- **Deps:** State backend (Pulumi Cloud/self-host).
- **Availability:** OSS free; Cloud SaaS.
- **Maintenance:** Active.
- **License:** Apache-2.0 / GPL-3.0 (Ansible).
- **Security/limits:** Same state-secret + approve discipline as Terraform.
- **Related:** Terraform/OpenTofu, Crossplane.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — Changesets / semantic-release (PR release flows) [OSS]
- **Canonical identity:** `npm:@changesets/cli` ; `npm:semantic-release`
- **Category:** CI/CD → PR flows / versioning
- **Type:** [OSS] utilities
- **Official URL:** https://github.com/changesets/changesets
- **Description:** Changesets: human-authored bump notes per PR → Version Packages PR → publish; semantic-release: Conventional Commits → auto semver+changelog+GH release.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** Monorepo-aware versioning, changelog gates.
- **Usage domain:** Library/design-system release trains.
- **Integration:** [INTEGRATION] (GHA release workflow on merge).
- **Compatibility:** npm/pnpm/yarn; GH releases.
- **Deps:** CI token with contents:write (scoped to release job).
- **Availability:** npm free.
- **Maintenance:** Active.
- **License:** MIT.
- **Security/limits:** Restrict publish tokens (OIDC trusted publishing where possible); require CODEOWNERS on version PRs.
- **Related:** GitHub Flow, npm trusted publishing.
- **Sources:** GitHub via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — GitHub Flow / trunk-based + required checks [INTEGRATION pattern]
- **Canonical identity:** `pattern:pr-flow` — https://docs.github.com/get-started/using-github/github-flow
- **Category:** CI/CD → PR workflow
- **Type:** [INTEGRATION] (branch protection + checks)
- **Official URL:** https://docs.github.com/
- **Description:** Short-lived branches → PR → required checks (build/test/SAST/SCA) → CODEOWNERS review → squash/merge → deploy; trunk-based variant with feature flags for high-velocity.
- **Contents inspected:** GitHub Flow docs pattern 2026.
- **Capabilities:** Enforceable quality gates (not prompt guidance).
- **Usage domain:** Default team flow.
- **Integration:** [INTEGRATION] (branch rulesets, required workflows, merge queues).
- **Compatibility:** GitHub/GitLab equivalents.
- **Deps:** CI checks defined.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Platform terms.
- **Security/limits:** Require signed commits + blocking checks; merge queues prevent semantic conflicts.
- **Related:** Changesets, Dagger.
- **Sources:** GitHub Docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — Depot / BuildJet / Blacksmith (fast runners + cache) [SERVICE]
- **Canonical identity:** `service:runner-infra-exemplar` — https://depot.dev/ ; https://buildjet.com/ ; https://blacksmith.sh/
- **Category:** CI/CD → Execution infra (runners/cache)
- **Type:** [SERVICE]
- **Official URL:** https://depot.dev/
- **Description:** Drop-in faster GHA runners + BuildKit/RBE/Turborepo remote cache; Blacksmith similar; cut build minutes for monorepos.
- **Contents inspected:** 2026 execution-infra layer (BuildJet/Depot/Blacksmith + Turborepo/Nx Cloud).
- **Capabilities:** vCPU/GPU options, warm caches, concurrency.
- **Usage domain:** Monorepos where GHA-hosted minutes dominate cost.
- **Integration:** [INTEGRATION] (`runs-on: depot-ubuntu-22.04`; cache actions).
- **Compatibility:** GHA-native.
- **Deps:** SaaS quota.
- **Availability:** Commercial SaaS.
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Ephemeral runners + OIDC (no PATs); verify cache poisoning controls (isolate PR caches).
- **Related:** Dagger/Earthly, Turborepo.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — Headless CI agents (Duo Workflow / Copilot Workspace exemplar) [SERVICE/INTEGRATION]
- **Canonical identity:** `service:headless-agent-exemplar` (GitLab Duo Workflow; GitHub Copilot Workspace)
- **Category:** CI/CD → Headless coding agents
- **Type:** [SERVICE] + [INTEGRATION] (triggered from issues/PRs, runs in CI sandbox)
- **Official URL:** https://docs.gitlab.com/ee/user/duo/ (exemplar)
- **Description:** Issue→plan→MR agents with CI-executed tests; GA Duo Workflow 2026; best as draft authors with required human review + green gates.
- **Contents inspected:** 2026 Duo GA notes; agent-eval reports (Replit/Vercel/Anthropic evals).
- **Capabilities:** Plan, patch, open MR, iterate on CI failures.
- **Usage domain:** Backlog acceleration under strict gates.
- **Integration:** [INTEGRATION] (labels/commands trigger; results as MR).
- **Compatibility:** GitLab/GitHub estates.
- **Deps:** Model + runner quota.
- **Availability:** Commercial (Ultimate/Enterprise tiers).
- **Maintenance:** Active, fast-moving.
- **License:** Proprietary.
- **Security/limits:** WARNING — agent output is [PROMPT-ONLY] until CI checks + human approve + sandboxed exec (see 17-security) enforce it; restrict to non-prod branches.
- **Related:** Permissions model, sandboxing.
- **Sources:** GitLab/GitHub docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Spacelift / Atlantis (IaC CI/CD) [SERVICE + OSS]
- **Canonical identity:** `service:spacelift` — https://spacelift.io/ ; `oss:atlantis` — https://www.runatlantis.io/
- **Category:** CI/CD → Terraform automation
- **Type:** [SERVICE] (Spacelift) + [OSS] (Atlantis)
- **Official URL:** https://spacelift.io/
- **Description:** PR `plan` comments → approve → `apply`; policy gates, drift detection, state handling; Atlantis self-hosted webhook flow; Spacelift SaaS with stacks.
- **Contents inspected:** 2026 Terraform-CI layer (Spacelift/Atlantis/Terragrunt/env0).
- **Capabilities:** Plan artifacts, concurrency locks, audit trail.
- **Usage domain:** GitOps for infra.
- **Integration:** [SERVICE]/[OSS] (VCS webhooks).
- **Compatibility:** Terraform/OpenTofu/Pulumi/Ansible runners.
- **Deps:** State backend + VCS app.
- **Availability:** SaaS free-2-seats exemplar / OSS free.
- **Maintenance:** Active.
- **License:** Proprietary / Apache-2.0.
- **Security/limits:** Lock apply to protected branches + manual approve; separate plan/apply credentials (least-privilege).
- **Related:** Terraform/OpenTofu, OIDC.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Composition rule (2026 best practice)
- Separate layers: CI (GHA/Buildkite/CircleCI) ≠ CD/GitOps (Argo CD/Flux — see 19) ≠ build-accel (Dagger/Earthly + Depot cache).
- Decide by 5 axes: Git host, K8s depth, monorepo scale, self-host policy, cloud lock-in + team size (small=SaaS, large=self-host agents with owners).
- Count: 20 resources (12 OSS · 5 SERVICE · 3 UTILITY/INTEGRATION mixes — see per-record KIND).
