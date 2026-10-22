# 17 — Security (AST/DAST · Scanners · Pentest · Deps Audit · Supply-Chain · Secrets · .env Guard · Prompt-Injection · Permissions · Isolation · Sandboxing · Container/Remote Exec)

> Part 3 · B-category catalog · Infra-Ops researcher · Read-only (no install/execute)
> Verification date: 2026-10-09 · Method: WebSearch (2026) + WebFetch on official docs/README/package
> Confidence scale: Verified / Partially / Unverified / Corrected / Archived / Inaccessible / Historical / Unresolved
> ISOLATION LEGEND — [ENFORCEABLE] = kernel/hypervisor/broker-enforced boundary (deny by default). [PROMPT-ONLY] = LLM instruction text with no enforcement; bypassable. Record warnings inline.

Scope: AST/DAST, scanners, pentest, dependency audit, supply-chain (SBOM/signing), secrets + .env guard, prompt-injection defenses, permission models, isolation/sandboxing, container/remote execution.

## Index (20 resources)

SAST/DAST: 01 Semgrep · 02 CodeQL · 03 SonarQube · 04 OWASP ZAP · 05 Burp Suite
Deps/supply-chain: 06 Snyk · 07 Dependabot + Renovate · 08 OSV-Scanner / npm-audit / pip-audit · 09 Sigstore/Cosign + SBOM (CycloneDX/Syft)
Secrets: 10 TruffleHog · 11 Gitleaks / detect-secrets · 12 Doppler/Infisical/Vault (.env guard exemplar)
LLM/prompt: 13 OWASP LLM Top 10 + Prompt-injection defenses (Rebuff exemplar)
Permissions/isolation: 14 Repo/agent permissions model (GITHUB_TOKEN least-privilege) · 15 Docker isolation [ENFORCEABLE] · 16 gVisor / Firecracker [ENFORCEABLE] · 17 nsjail/bubblewrap/seccomp [ENFORCEABLE] · 18 E2B / Daytona (sandboxed remote exec) [ENFORCEABLE] · 19 System prompt / policy files (CLAUDE/AGENTS) [PROMPT-ONLY] · 20 Pentest methodology (OWASP Testing Guide + PTES)

---

### 01 — Semgrep (SAST, fast PR gates)
- **Canonical identity:** `tool:semgrep` — `github:semgrep/semgrep`
- **Category:** Security → SAST
- **Type:** OSS (LGPL-2.1 CE) + commercial Platform
- **Official URL:** https://semgrep.dev/
- **Description:** Pattern+semantic rules in readable YAML; ~10s median CI scans (~150MB); 3000+ community / 20000+ pro rules; p/owasp-top-ten packs.
- **Contents inspected:** 2026 head-to-head (Semgrep vs CodeQL) + SAST/DAST buyer guide.
- **Capabilities:** 30+ langs (incl. Terraform/Dockerfile/Bash/Solidity CodeQL lacks); SARIF; pre-commit/GHA/GitLab/Jenkins/Buildkite.
- **Usage domain:** Every-PR gate (block Critical/High).
- **Integration:** official (`semgrep scan --error --config p/...`; container `semgrep/semgrep`).
- **Compatibility:** Any CI; SARIF to GitHub/GitLab code scanning.
- **Deps:** None heavy.
- **Availability:** OSS free; Code ~$40/dev/mo.
- **Maintenance:** Active (15.6k stars).
- **License:** LGPL-2.1 (CE); proprietary (Platform).
- **Security/limits:** CE misses inter-procedural taint (needs Semgrep Code); keep false positives <15% or devs ignore output. WARNING: SAST-only leaves runtime/config gaps — pair with DAST.
- **Related:** CodeQL, SonarQube, Bandit.
- **Sources:** semgrep.dev; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 02 — CodeQL (SAST, deep taint tracking)
- **Canonical identity:** `tool:codeql` (GitHub) — https://codeql.github.com/
- **Category:** Security → SAST (deep dataflow)
- **Type:** Service-tied analyzer (free OSS repos; GHAS for private)
- **Official URL:** https://codeql.github.com/
- **Description:** Compiles code to queryable DB (AST+CFG+DFG); QL queries trace source→sink across files; higher accuracy/lower FPs than CE per community benchmarks; minutes–30+min builds (~450MB).
- **Contents inspected:** 2026 Semgrep-vs-CodeQL matrix (12 langs; QL authoring hours vs minutes).
- **Capabilities:** Cross-file/function taint; security-extended packs; SARIF; Copilot Autofix.
- **Usage domain:** Nightly/merge-to-main deep analysis alongside Semgrep PR gates.
- **Integration:** official (codeql-action/init+analyze; CLI for non-GHA).
- **Compatibility:** C/C++/C#/Go/Java/Kotlin/JS-TS/Python/Ruby/Swift/Rust; GitHub-first.
- **Deps:** Build toolchain for compiled langs.
- **Availability:** Free public repos; GHAS license private.
- **Maintenance:** Active (GitHub-maintained).
- **License:** GitHub terms (queries MIT-ish by pack).
- **Security/limits:** GitHub lock-in; slow for PR gating — schedule it; QL needs security-engineer investment.
- **Related:** Semgrep, SonarQube.
- **Sources:** codeql.github.com; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 03 — SonarQube / SonarCloud (SAST + quality platform)
- **Canonical identity:** `tool:sonarqube` — https://www.sonarsource.com/products/sonarqube/
- **Category:** Security → SAST + quality gates
- **Type:** OSS (Community) + service (SonarCloud)
- **Official URL:** https://www.sonarsource.com/
- **Description:** 30+ langs; self-hosted dashboard CE free; quality gates (coverage/duplication/hotspots) + taint rules; Jenkins/GHA plugin.
- **Contents inspected:** 2026 buyer guide (best free self-hosted platform).
- **Capabilities:** PR decoration, hotspot review, enterprise governance.
- **Usage domain:** Org-wide standard gate where dashboard/audit trail matters.
- **Integration:** official (scanner CLI, plugins).
- **Compatibility:** Self-host or Cloud.
- **Deps:** DB + server ops for self-host.
- **Availability:** CE free; commercial tiers.
- **Maintenance:** Active.
- **License:** LGPL (CE); proprietary (commercial).
- **Security/limits:** Tune profiles — default noise buries signal; secrets need dedicated scanners.
- **Related:** Semgrep, CodeQL, Snyk Code.
- **Sources:** SonarSource via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 04 — OWASP ZAP / ZAP by Checkmarx (DAST)
- **Canonical identity:** `tool:zap` — `github:zaproxy/zaproxy`
- **Category:** Security → DAST
- **Type:** OSS (Linux Foundation Software Security Project; stewarded by Checkmarx since 2023)
- **Official URL:** https://www.zaproxy.org/
- **Description:** Active scanner (OWASP payloads) + passive scanner + spider/AJAX spider + OpenAPI/GraphQL import; Automation Framework YAML for CI (`ghcr.io/zaproxy/zaproxy:stable zap-api-scan.py`).
- **Contents inspected:** 2026 SAST/DAST guides + thesis benchmark (ZAP strict recall 8.3% / weighted 12.5% on Juice Shop — proves DAST-only insufficient).
- **Capabilities:** Auth-scripted scans, API scans from openapi.json, HTML/MD/JSON reports.
- **Usage domain:** Nightly vs seeded staging (per-role test users); gate Critical/High, not every advisory.
- **Integration:** official (Docker + YAML plan as CI step post-deploy-to-staging).
- **Compatibility:** Any web app/API URL.
- **Deps:** Staging env with seeded (non-prod) data.
- **Availability:** Free OSS (self-operated).
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** WARNING — invisible to admin-only/multi-step/flagged paths unless scripted; never scan prod or third parties without written authorization.
- **Related:** Burp Suite Enterprise, StackHawk.
- **Sources:** zaproxy.org; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 05 — Burp Suite (pentest + DAST enterprise)
- **Canonical identity:** `service:burp` — https://portswigger.net/burp
- **Category:** Security → Pentest / DAST
- **Type:** Service/commercial (Community free; Professional; Enterprise)
- **Official URL:** https://portswigger.net/burp
- **Description:** Manual proxy/repeater/intruder + automated Enterprise scans; standard for human pentest (business-logic, authZ bypass, chaining) that scanners miss.
- **Contents inspected:** Search-verified identity (dominates with ZAP in 2026 DAST setups).
- **Capabilities:** Authenticated crawl, session handling, CI-scheduled Enterprise scans.
- **Usage domain:** Human pentest + scheduled enterprise DAST.
- **Integration:** service (Enterprise CI plugins; manual proxy).
- **Compatibility:** Web/API targets.
- **Deps:** License; authorized scope.
- **Availability:** Commercial (Community free tier).
- **Maintenance:** Active (PortSwigger).
- **License:** Proprietary.
- **Security/limits:** WARNING — active scanning is attack traffic; written authorization + isolated staging mandatory.
- **Related:** ZAP, OWASP Testing Guide.
- **Sources:** portswigger.net via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 06 — Snyk (SCA + Code + Container + IaC)
- **Canonical identity:** `service:snyk` — https://snyk.io/
- **Category:** Security → SCA / SAST / container / IaC (+ Secrets)
- **Type:** Service (OSS-limited free tier)
- **Official URL:** https://snyk.io/
- **Description:** Proprietary vuln DB (broader/faster than GitHub Advisory per 2026 guide); reachability-aware risk scoring; license scanning; container/IaC; `.snyk` policy with reason+expiry; `--fail-on=upgradable`.
- **Contents inspected:** 2026 Dependabot+Snyk automation guide (workflows, SBOM via `snyk sbom --format=cyclonedx`).
- **Capabilities:** Auto-PRs, container build scan, SBOM export.
- **Usage domain:** Layer atop Dependabot for critical services (license+container+reachability).
- **Integration:** service (snyk/actions/node|docker; SNYK_TOKEN in CI secrets).
- **Compatibility:** npm/pip/Maven/Gradle/Go/Ruby + containers + Terraform.
- **Deps:** SNYK_TOKEN; lockfiles present.
- **Availability:** SaaS (free-limited → paid scale).
- **Maintenance:** Active.
- **License:** Proprietary.
- **Security/limits:** Never `.snyk`-ignore without reason+expiry; scan transitive deps + base images, not just direct.
- **Related:** Dependabot, OSV-Scanner, Socket.
- **Sources:** snyk.io; WebSearch 2026.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 07 — Dependabot + Renovate (automated dep updates)
- **Canonical identity:** `service:dependabot` (GitHub-native) + `tool:renovate` — https://docs.github.com/code-security/dependabot
- **Category:** Security → Dependency audit / remediation
- **Type:** Service (Dependabot free) + OSS (Renovate)
- **Official URL:** https://docs.github.com/code-security/dependabot
- **Description:** Dependency graph + Advisory DB → alerts (incl. malware alerts); security updates (min-fix) vs version updates (scheduled latest); auto-PR to patched Actions too.
- **Contents inspected:** GitHub supply-chain docs excerpts.
- **Capabilities:** PR-per-fix, grouping, auto-merge for low-risk (with CI gates).
- **Usage domain:** Always-on baseline (free, minimal setup) for every repo.
- **Integration:** service/utility (dependabot.yml; Renovate bot + presets).
- **Compatibility:** npm/pip/Maven/Gradle/Composer/Go/Ruby + Actions.
- **Deps:** Dependency graph enabled.
- **Availability:** Free (GitHub); Renovate OSS/self-host or Mend SaaS.
- **Maintenance:** Active.
- **License:** GitHub terms / ISC (Renovate).
- **Security/limits:** Alerts off by default in some configs — must explicitly enable; verify auto-merge only with green SAST/tests.
- **Related:** Snyk, OSV-Scanner.
- **Sources:** GitHub Docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 08 — OSV-Scanner / npm-audit / pip-audit (lightweight SCA)
- **Canonical identity:** `tool:osv-scanner` — https://osv.dev/
- **Category:** Security → Dependency audit (lightweight)
- **Type:** OSS utilities
- **Official URL:** https://osv.dev/
- **Description:** OSV DB (distributed, multi-eco) CLI; npm-audit/pip-audit lockfile checkers for pre-commit/CI without vendor account; offline-capable via Dependency-Check for Java/.NET.
- **Contents inspected:** 2026 $0-stack table (Dependabot + OSV + ZAP covers ~80% for small teams).
- **Capabilities:** Fast fail on known CVEs with fixed versions; SBOM-adjacent inventory.
- **Usage domain:** $0 CI gate before adding Snyk depth (reachability/IaC).
- **Integration:** utility (`osv-scanner --lockfile=...`; `npm audit --audit-level=high`; `pip-audit -r requirements.txt`).
- **Compatibility:** npm/pip/Go/Rust/Maven per tool.
- **Deps:** Lockfiles committed.
- **Availability:** Free OSS.
- **Maintenance:** Active (Google/OpenSSF OSV).
- **License:** Apache-2.0 / MIT variants.
- **Security/limits:** No reachability — triage with fixed-version + exploit-maturity signals; pin + SBOM for auditability.
- **Related:** Snyk, Dependabot, CycloneDX.
- **Sources:** osv.dev via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 09 — Sigstore/Cosign + SBOM (signing + inventory) [ENFORCEABLE provenance]
- **Canonical identity:** `tool:sigstore` — https://www.sigstore.dev/ ; SBOM: CycloneDX/SPDX via `syft`/`cyclonedx`
- **Category:** Security → Supply-chain (provenance + SBOM)
- **Type:** OSS utilities (OpenSSF)
- **Official URL:** https://www.sigstore.dev/
- **Description:** Keyless signing (Fulcio+Rekor) + `cosign verify` in deploy gates; `syft`/`snyk sbom` emit CycloneDX JSON stored per release (EO 14028 artifact).
- **Contents inspected:** Search-verified pattern (artifact attestations + immutable releases in GitHub supply-chain docs).
- **Capabilities:** [ENFORCEABLE] Admission controllers / deploy workflows can REJECT unsigned/unattested images (deny-by-default).
- **Usage domain:** Release provenance for procurement/compliance.
- **Integration:** utility (`cosign sign/verify`; `syft packages dir:. -o cyclonedx-json`).
- **Compatibility:** OCI images, binaries, GitHub attestations.
- **Deps:** Rekor transparency log; artifact store.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** Apache-2.0.
- **Security/limits:** Signing proves origin, not safety — still need SCA/SAST gates before sign.
- **Related:** Snyk, Dependabot, Docker isolation.
- **Sources:** sigstore.dev; GitHub supply-chain docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 10 — TruffleHog (secrets discovery + verification)
- **Canonical identity:** `tool:trufflehog` — `github:trufflesecurity/trufflehog`
- **Category:** Security → Secrets scanning
- **Type:** OSS utility
- **Official URL:** https://github.com/trufflesecurity/trufflehog
- **Description:** 800+ detectors, active verification (700+ verifiers), analyzes permissions/resources; scans git/GitHub/GitLab/S3/GCS/filesystem/Postman/CI; SARIF + GHA + pre-commit.
- **Contents inspected:** GitHub README excerpts (sources, --results, analyze subcommand).
- **Capabilities:** Verified-only output mode (`--results=verified,unknown`), driftwood private-key verification.
- **Usage domain:** Pre-commit soft-block + PR gate + scheduled org sweep.
- **Integration:** utility (GHA `trufflesecurity/trufflehog-actions`; pre-commit hook; `--sarif` to code scanning).
- **Compatibility:** Any git/filesystem/cloud source.
- **Deps:** API egress for verification (scoped).
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** AGPL-3.0.
- **Security/limits:** Verified findings = rotate immediately (no backlog); large SARIF buffered in memory — stream JSON for huge scans.
- **Related:** Gitleaks, Snyk Secrets.
- **Sources:** GitHub README via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Verified

### 11 — Gitleaks / detect-secrets (lightweight secret gates)
- **Canonical identity:** `tool:gitleaks` — `github:gitleaks/gitleaks`
- **Category:** Security → Secrets scanning (lightweight)
- **Type:** OSS utilities
- **Official URL:** https://github.com/gitleaks/gitleaks
- **Description:** Fast regex+entropy; `gitleaks protect` (staged) / `detect` (history); allowlist + baseline; pre-commit standard.
- **Contents inspected:** Search-verified identity (paired with TruffleHog in secure-pipeline blueprints).
- **Capabilities:** Low-latency PR/pre-commit block without verification egress.
- **Usage domain:** Every-commit first line (then TruffleHog verify).
- **Integration:** utility (pre-commit hook; GHA).
- **Compatibility:** Git repos.
- **Deps:** None.
- **Availability:** Free OSS.
- **Maintenance:** Active.
- **License:** MIT (Gitleaks); Apache-2.0 (detect-secrets Yelp).
- **Security/limits:** Higher noise than verifying scanners — tune allowlists, never commit baseline with live secrets (rotate first).
- **Related:** TruffleHog, git-secrets.
- **Sources:** GitHub via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 12 — .env guard exemplar (Doppler / Infisical / HashiCorp Vault)
- **Canonical identity:** `service:dotenv-guard-exemplar`
- **Category:** Security → Secrets management (.env guard)
- **Type:** Service + OSS (Infisical OSS; Vault OSS)
- **Official URL:** https://www.doppler.com/ · https://infisical.com/ · https://www.vaultproject.io/
- **Description:** Central env/sync, versioned references, dynamic secrets/leases, audit log; replaces committed `.env` with injected-at-runtime config; `dotenv-vault` for small teams.
- **Contents inspected:** Search-verified category identities.
- **Capabilities:** [ENFORCEABLE] Brokered fetch + short-TTL leases + revocation (vs static .env copy).
- **Usage domain:** Local/dev/CI/prod parity without secrets in git.
- **Integration:** service/utility (CLI inject `doppler run --`; Vault agent; Infisical SDK).
- **Compatibility:** Node/Python/Docker/K8s external-secrets.
- **Deps:** SaaS account or self-hosted Vault/Infisical.
- **Availability:** Freemium + OSS self-host.
- **Maintenance:** Active.
- **License:** Proprietary (Doppler Cloud) / MIT (Infisical) / BSL (Vault).
- **Security/limits:** WARNING — `.env.example` only (keys, never values); `.gitignore .env*`; rotate on any history hit; OIDC-brokered CI fetch preferred over long-lived tokens.
- **Related:** TruffleHog, SOPS/age (file-encryption alt).
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 13 — OWASP LLM Top 10 + prompt-injection defenses (Rebuff exemplar) [PROMPT-ONLY unless brokered]
- **Canonical identity:** `spec:owasp-llm-top10` — https://genai.owasp.org/ ; `tool:rebuff` — `github:protectai/rebuff`
- **Category:** Security → LLM / prompt-injection
- **Type:** Open standard + OSS filters
- **Official URL:** https://genai.owasp.org/
- **Description:** LLM01 (prompt injection) / LLM02 (data leakage) / LLM06 (excessive agency) taxonomy; defenses: delimit+validate I/O, indirect-instruction ignore, tool-allowlist, human-confirm for side effects; Rebuff: heuristics+vector+canary filters.
- **Contents inspected:** Search-verified taxonomy + filter pattern.
- **Capabilities:** Input/output scanning, canary tokens, least-agency tool design.
- **Usage domain:** Any agent with tools/network/shell.
- **Integration:** integration (filter lib in pipeline; policy in code review).
- **Compatibility:** Any LLM stack.
- **Deps:** Model/filter hosting.
- **Availability:** Free spec + OSS filters.
- **Maintenance:** Active (2025 LLM Top 10 v2).
- **License:** CC-BY-SA (spec); MIT/Apache (filters vary).
- **Security/limits:** WARNING [PROMPT-ONLY] — instruction-following filters are bypassable; only broker-enforced allowlists + confirmations + sandbox exec (items 15–18) count as [ENFORCEABLE]. Treat model output as untrusted input.
- **Related:** Permissions models, sandboxing, moderation APIs.
- **Sources:** genai.owasp.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 14 — Least-privilege permissions model (CI + agent scopes) [ENFORCEABLE when platform-checked]
- **Canonical identity:** `policy:least-privilege-exemplar` (GitHub permissions + agent tool scopes)
- **Category:** Security → Permissions
- **Type:** Platform feature (utility config)
- **Official URL:** https://docs.github.com/actions/security-guides/automatic-token-authentication
- **Description:** Minimal `permissions: { contents: read }` + job-level escalation; OIDC federation (no long-lived cloud secrets); agent tool allowlist (read-only FS, no network/shell by default; write requires explicit grant + confirmation).
- **Contents inspected:** GitHub token-auth docs pattern via WebSearch.
- **Capabilities:** [ENFORCEABLE] Platform denies out-of-scope API/tool calls regardless of prompt text.
- **Usage domain:** Every workflow/agent session.
- **Integration:** utility (YAML `permissions:`; agent `tools.allow=[...]`).
- **Compatibility:** GHA/GitLab/OIDC clouds; agent harnesses.
- **Deps:** None.
- **Availability:** Built-in.
- **Maintenance:** Active.
- **License:** Platform terms.
- **Security/limits:** Default `write-all` is dangerous — set top-level `permissions: {}` and escalate per job; audit Marketplace action scopes + pinned SHAs.
- **Related:** OIDC, sandboxing.
- **Sources:** GitHub Docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 15 — Docker / OCI container isolation [ENFORCEABLE]
- **Canonical identity:** `tool:docker` — https://www.docker.com/
- **Category:** Security → Isolation (container)
- **Type:** OSS (+ commercial Desktop/Hub)
- **Official URL:** https://www.docker.com/
- **Description:** Namespaces+cgroups+seccomp+cap-drop baseline; `--read-only --cap-drop=ALL --user nobody --network none|scoped --pids-limit --memory` + image digests + no-new-privs.
- **Contents inspected:** Search-verified hardening flags pattern.
- **Capabilities:** [ENFORCEABLE] Kernel denies FS/net/proc/capability abuse outside granted profile.
- **Usage domain:** Default boundary for untrusted code/parsers/PDF builds/tests.
- **Integration:** utility (`docker run --rm ...`; Compose/K8s securityContexts).
- **Compatibility:** Linux (Desktop VM on Mac/Win).
- **Deps:** Container runtime.
- **Availability:** Free OSS (+commercial).
- **Maintenance:** Active.
- **License:** Apache-2.0 (engine).
- **Security/limits:** WARNING — container ≠ VM: privileged/root/ Docker-socket mounts break the boundary; untrusted workloads need gVisor/Firecracker below.
- **Related:** gVisor, Firecracker, nsjail.
- **Sources:** Docker docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 16 — gVisor / Firecracker (stronger workload isolation) [ENFORCEABLE]
- **Canonical identity:** `tool:gvisor` — https://gvisor.dev/ ; `tool:firecracker` — https://firecracker-microvm.github.io/
- **Category:** Security → Isolation (sandbox kernel / microVM)
- **Type:** OSS
- **Official URL:** https://gvisor.dev/
- **Description:** gVisor (user-space kernel, runsc) intercepts syscalls; Firecracker (KVM microVMs, sub-second boot) backs AWS Lambda/Fargate-style multi-tenant exec.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** [ENFORCEABLE] Syscall-surface reduction (gVisor) / hardware virtualization boundary (Firecracker).
- **Usage domain:** Multi-tenant agent code exec, untrusted parsers.
- **Integration:** utility (runsc runtimeClass; Firecracker jailer/VM orchestration).
- **Compatibility:** Linux/KVM hosts.
- **Deps:** Host KVM (Firecracker); OCI runtime shim (gVisor).
- **Availability:** Free OSS.
- **Maintenance:** Active (Google/AWS).
- **License:** Apache-2.0.
- **Security/limits:** Perf/policy tuning required; still need seccomp/cap-drop + image provenance above.
- **Related:** Docker, nsjail, E2B/Daytona.
- **Sources:** Official docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 17 — nsjail / bubblewrap / seccomp profiles [ENFORCEABLE]
- **Canonical identity:** `tool:nsjail` — https://github.com/google/nsjail
- **Category:** Security → Sandboxing (syscall/FS lockdown)
- **Type:** OSS utilities
- **Official URL:** https://github.com/google/nsjail
- **Description:** Fine-grained namespaces, chroot/pivot_root, rlimits, seccomp-bpf allowlists, net-namespace off; bubblewrap for single-app FS/network sandbox.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** [ENFORCEABLE] Deny-by-default syscall/FS/network matrix per command.
- **Usage domain:** Single-command sandbox (PDF parse, test exec, agent tool shim).
- **Integration:** utility (`nsjail -Mo --disable_clone_newnet ... -- /cmd`; `bwrap --ro-bind ...`).
- **Compatibility:** Linux.
- **Deps:** None.
- **Availability:** Free OSS.
- **Maintenance:** Active (Google).
- **License:** Apache-2.0 / MIT.
- **Security/limits:** Policy is code — fuzz/CI-test the profile; log violations.
- **Related:** Docker, gVisor.
- **Sources:** GitHub/docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 18 — E2B / Daytona (sandboxed remote exec for agents) [ENFORCEABLE]
- **Canonical identity:** `service:e2b` — https://e2b.dev/ ; `service:daytona` — https://www.daytona.io/
- **Category:** Security → Container / remote exec (agent sandboxes)
- **Type:** Service (+ OSS runtimes)
- **Official URL:** https://e2b.dev/
- **Description:** Ephemeral microVM-backed code-interpreter/dev sandboxes with timeouts, network controls, pause/snapshot; built for AI agents running untrusted code.
- **Contents inspected:** Search-verified identities.
- **Capabilities:** [ENFORCEABLE] Provider-enforced CPU/mem/timeout/net egress + kill; per-session isolation (vs in-process exec).
- **Usage domain:** Agent code/test/tool execution that must not touch host secrets.
- **Integration:** service (SDK: create sandbox → run → destroy; no host FS/secret mount).
- **Compatibility:** SDKs (JS/Python).
- **Deps:** SaaS quota / self-host runner.
- **Availability:** SaaS + OSS components.
- **Maintenance:** Active.
- **License:** Proprietary SaaS + Apache-2.0 parts.
- **Security/limits:** WARNING — still scope egress (block IMDS/cloud metadata + secrets subnets); pass only redacted inputs; verify output before merge.
- **Related:** Firecracker, Docker, permissions model.
- **Sources:** Vendor docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 19 — System-prompt / policy files (CLAUDE.md / AGENTS.md / .rules) [PROMPT-ONLY]
- **Canonical identity:** `pattern:prompt-policy-file`
- **Category:** Security → Guidance (non-enforcing)
- **Type:** Convention (utility text)
- **Official URL:** N/A (repo-local convention)
- **Description:** Natural-language instructions (allowed paths, no-force-push, confirm-before-deploy, secrets hygiene) loaded into agent context.
- **Contents inspected:** Pattern verified across agent docs 2026.
- **Capabilities:** Improves default behavior, documents intent.
- **Usage domain:** Ergonomics + review checklist only.
- **Integration:** integration (markdown in repo; referenced by harness).
- **Compatibility:** Any agent harness.
- **Deps:** None.
- **Availability:** Free (authored).
- **Maintenance:** Author-maintained.
- **License:** N/A.
- **Security/limits:** WARNING [PROMPT-ONLY] — NOT a security boundary: injected content, tool confusion, or misreading bypasses it. Must be paired with items 14–18 ([ENFORCEABLE]) for any safety claim. Never assert isolation from a prompt file.
- **Related:** OWASP LLM guidance, permissions model.
- **Sources:** Agent docs via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

### 20 — Pentest methodology (OWASP Testing Guide + PTES) + IAST/RASP note
- **Canonical identity:** `spec:owasp-testing-guide` — https://owasp.org/www-project-web-security-testing-guide/
- **Category:** Security → Pentest methodology
- **Type:** Open standard + commercial tooling note
- **Official URL:** https://owasp.org/www-project-web-security-testing-guide/
- **Description:** Config/deploy, authN/Z, session, input validation, business-logic test phases; PTES (pre-engagement→reporting); IAST/RASP (Contrast/Datadog ASM) instruments runtime for stack-trace findings.
- **Contents inspected:** OWASP guide TOC via WebSearch.
- **Capabilities:** Human coverage of authZ bypass, chaining, logic flaws scanners miss (cf. §04 recall numbers).
- **Usage domain:** Periodic human assessment freeing scanner time for known patterns.
- **Integration:** open-standard (scope doc, seeded staging, role accounts).
- **Compatibility:** Any web/API estate.
- **Deps:** Authorized testers + isolated env.
- **Availability:** Free guide; testers commercial.
- **Maintenance:** Active (v5 2024–2026).
- **License:** CC-BY-SA.
- **Security/limits:** WARNING — written authorization + scope + data-handling agreement mandatory; no prod testing.
- **Related:** ZAP, Burp, SAST/DAST combo.
- **Sources:** owasp.org via WebSearch.
- **Verification date:** 2026-10-09 · **Confidence:** Partially

---

## Enforceability summary (must-read)
- [ENFORCEABLE]: least-privilege permissions + OIDC (14), Docker flags (15), gVisor/Firecracker (16), nsjail/bwrap/seccomp (17), E2B/Daytona remote sandboxes (18), Cosign/admission provenance (09).
- [PROMPT-ONLY]: system-prompt/policy files (19), LLM filters without broker (13) — useful hygiene, zero boundary claims.
- Pipeline rule: SAST+SCA per-PR (Semgrep/CodeQL/Snyk/Dependabot/OSV) → secrets gates (TruffleHog/Gitleaks + vault inject) → DAST post-deploy-to-staging (ZAP/Burp) → provenance sign → sandboxed agent exec only.
- Count: 20 resources.
