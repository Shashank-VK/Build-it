# §30 — CI/CD & GitOps (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## CI-01 — Dagger — ACTIVE (with a documented exit case)
- Purpose / problem: Programmable CI engine: pipelines as TypeScript/Go/Python functions running in containers via BuildKit — same pipeline locally and in CI (`dagger call build`).
- OSS/commercial: OSS (Apache-2.0 engine) + Dagger Cloud (Individual free visualization; Team $50/mo distributed caching).
- Integration: Runs inside GitHub Actions via `dagger/dagger-for-github`; does not replace the CI runner, replaces step definitions.
- Maintenance: Active (2026).
- **Counter-evidence (primary source):** shepherdjerred/monorepo **ripped out its entire Dagger module in Jul 2026** — 23 files, ~9k LOC, 121 functions, plus Buildkite pipeline and git hooks — with the replatform plan marked "Abandoned." The associated skill note calls Dagger notes "historical." This is a real-world "migrating away" data point: the local/CI parity promise did not survive contact with this repo's operational reality.
- Limitations: 4–12 hours to rewrite YAML pipelines as modules (per 2026 evaluation); distributed caching paywalled; another abstraction to debug.
- Alternatives: Earthly, depot.dev builds, plain GitHub Actions, Nix.
- Switching costs: Medium (module code portable as containers).
- Use: U(Verified) — adopted by some; exited by others (both documented).

## CI-02 — Depot — ACTIVE
- Purpose / problem: Fast Docker builds: managed remote builders with persistent layer caching; GitHub Actions drop-in (`depot/build-push-action`); Turborepo remote cache on GHA runners.
- OSS/commercial: Commercial SaaS (~$20/mo entry). **Minor incident Oct 8, 2026** (us-east-1 + Depot CI job-start failures, 1h54m, resolved — via Pingoru).
- Maintenance: Active (2026); 2–10x faster Docker builds claimed (cache-dependent).
- Limitations: $20/mo hard to justify until Docker builds are a proven bottleneck (per 2026 evaluation); build infra is now a vendor dependency.
- Security: Builds run on vendor infra; OIDC auth (no long-lived secrets).
- Alternatives: Dagger (BuildKit), Earthly, native GHA cache, Blacksmith.
- Switching costs: Low (drop-in action swap).
- Use: U(Verified) — evaluated/adopted in real repos (mattbutlerengineering CI/CD evaluation, Feb 2026).

## CI-03 — Buildkite — ACTIVE
- Purpose / problem: Hybrid CI/CD: pipelines in YAML (static or dynamically generated); agents run on your infra, UI in cloud.
- OSS/commercial: Commercial SaaS (agent-based pricing).
- Maintenance: Active (2026).
- Limitations: You operate the agents (K8s agents, queues, admission control); dynamic pipeline generation is powerful but complex.
- Alternatives: GitHub Actions, GitLab CI, CircleCI.
- Switching costs: Medium.
- Use: U(Verified) — shepherdjerred/monorepo ran Buildkite with Kueue admission (80Gi/24CPU) until the Jul 2026 CI strip.

## CI-04 — Woodpecker CI — ACTIVE
- Purpose / problem: Lightweight community CI engine; **fork of Drone** (post-license-change).
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026).
- Alternatives: Drone, Gitea Actions, Forgejo Actions.
- Switching costs: Low.
- Use: U(Proposed).

## CI-05 — Drone (Harness) — MAINTAINED
- Purpose / problem: Container-native CI (was the OSS standard); now under Harness.
- OSS/commercial: License changed (verify current — historically Apache-2.0 → more restrictive); Harness commercial.
- Maintenance: Maintained under Harness (2026). (Depth debt on license/versions.)
- Alternatives: Woodpecker, Harness CI.
- Use: U(Proposed).

## CI-06 — Earthly — ACTIVE
- Purpose / problem: "Makefile + Dockerfile" reproducible builds (Earthfiles); local/CI parity.
- OSS/commercial: OSS (license verify — historically MPL-2.0) + commercial.
- Maintenance: Active (2026).
- Alternatives: Dagger, Nix, plain Docker.
- Use: U(Proposed). (Depth debt.)

## CI-07 — GitHub Actions — ACTIVE
- Purpose / problem: The default CI/CD for GitHub repos; 6,000+ marketplace actions; OIDC to clouds.
- OSS/commercial: Commercial (GitHub; free tier generous for public repos).
- Maintenance: Active (2026).
- Limitations: Runner minutes pricing; YAML sprawl; marketplace action supply-chain risk (pin SHAs).
- Security: OIDC, environments, required checks; compromised actions are a real attack vector.
- Alternatives: GitLab CI, Buildkite, CircleCI.
- Switching costs: Medium (workflow rewrite).
- Use: U(Verified) — ubiquitous.

## CI-08 — Argo CD — ACTIVE (GitOps standard)
- Purpose / problem: Declarative GitOps continuous delivery for Kubernetes (desired-state in Git, drift detection, sync).
- OSS/commercial: OSS Apache-2.0 (CNCF graduated).
- Maintenance: Active (2026).
- Alternatives: FluxCD, Argo Rollouts (progressive delivery), Harness.
- Switching costs: Medium.
- Use: U(Verified) — GitOps standard alongside Flux.

## CI-09 — FluxCD — ACTIVE (narrative correction: NOT archived)
- Purpose / problem: GitOps for Kubernetes (source/helm/kustomize controllers).
- OSS/commercial: OSS Apache-2.0 (CNCF graduated).
- Maintenance: **Active — CNCF graduated**; the "Flux is archived/dead" narrative confuses Weaveworks' 2024 commercial shutdown with the project. (Per summary correction.)
- Alternatives: Argo CD.
- Use: U(Verified) — CNCF project.

## CI-10 — Tekton — MAINTAINED
- Purpose / problem: Kubernetes-native CI/CD building blocks (Pipelines, Triggers).
- OSS/commercial: OSS Apache-2.0 (CD Foundation).
- Maintenance: Maintained (2026); slower innovation vs GitHub Actions.
- Alternatives: Argo Workflows, Dagger.
- Use: U(Proposed). (Depth debt.)

## CI-11 — Jenkins — MAINTAINED
- Purpose / problem: The extensible automation server (1,800+ plugins).
- OSS/commercial: OSS MIT (CD Foundation).
- Maintenance: Maintained (2026); new projects rarely choose it.
- Alternatives: GitHub Actions, GitLab CI.
- Switching costs: High (plugin sprawl).
- Use: U(Verified) — massive legacy installed base.

## CI-12 — CircleCI — ACTIVE
- Purpose / problem: Cloud-native CI/CD with Docker layer caching and parallelism.
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: GitHub Actions, Buildkite.
- Use: U(Proposed).

## CI-13 — Harness — ACTIVE
- Purpose / problem: AI-powered software delivery platform (CI, CD, feature flags via FME, cost governance); acquirer of Drone and Split.
- OSS/commercial: Commercial.
- Maintenance: Active (2026).
- Alternatives: GitHub Actions + Argo CD, GitLab.
- Use: U(Proposed). (Depth debt.)

## CI-14 — Spacelift — ACTIVE
- Purpose / problem: CI/CD for infrastructure (Terraform, Pulumi, OpenTofu, CloudFormation).
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026).
- Alternatives: Terraform Cloud, Atlantis, env0.
- Use: U(Proposed). (Depth debt.)

## CI-15 — Travis CI — DEPRECATED (effectively)
- Purpose / problem: Once the default OSS CI.
- Maintenance: **Effectively dead for OSS — free tier for open source killed Nov 2020**; exodus to GitHub Actions. (Per summary.)
- Alternatives: GitHub Actions.
- Use: Historical.

## Notable status findings (CI/CD)
- Dagger — a **documented exit** (Jul 2026: 9k LOC removed) tempers the "pipelines as code" hype; the value prop is real but so is the abstraction cost.
- Depot — real speedups, real vendor dependency (incident Oct 8, 2026).
- FluxCD — **not archived** (CNCF graduated); Weaveworks ≠ Flux.
- Travis CI — the original "free OSS CI is dead" (Nov 2020).

---

### Per-record metadata (condensed)
- Dagger exit: github.com/shepherdjerred/monorepo PR #1516 (Jul 15, 2026) — primary source; skill note "Dagger/dynamic-pipeline notes below are historical." Confidence: High.
- Depot: mattbutlerengineering CI/CD evaluation (Feb 2026, GitHub); pingoru.io incident Oct 8, 2026. Confidence: Medium–High.
- Buildkite: shepherdjerred/monorepo skill docs (2026). Confidence: Medium.
- k6-adjacent CI patterns: raidan-ai testing SKILL. Confidence: Medium.
- DevOps tool landscape: clubanderson/awesome-devops-tools-2026 (GitHub). Confidence: Low–Medium (curated list).
- FluxCD/Travis: summary evidence. Confidence: High (established records).
