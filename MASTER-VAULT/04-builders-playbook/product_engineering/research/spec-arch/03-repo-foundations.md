# Repository Foundations & Dev Conventions (§10)

**Workstream:** spec-arch · **Research date:** 2026-10-10 · **Labels:** Verified / Corroborated / Inferred / Proposed / Unknown
**Evidence register:** `04-evidence-register.md`.

**Thesis:** foundations are not bureaucracy — they are *defect prevention with the cost paid once*. The file below separates what earns its keep (prevents recurring defect classes) from what can wait. Rule of thumb used throughout: **if a foundation's absence has produced the same incident twice, it's not premature — it's overdue.**

---

## 1. Prevents recurring defects — do before substantial implementation

### 1.1 One repo per deployable, protected `main`, required CI gates

**What:** a single codebase in version control per deployable unit; `main` is always deployable; no direct pushes — changes land via pull request with required status checks (build, tests, lint/typecheck, secret scan) that *block* merge on failure.
**Mechanics:** branch protection rules (require PR, require passing checks, no force-push, dismiss stale reviews); short-lived branches (hours–2 days) merged to trunk, or trunk-based commits behind feature flags.
**Why it prevents defects:** the merge gate is what makes parallel work safe — human or agent. "Locally green is necessary but not sufficient; the PR's checks are the source of truth." Without required checks, a red trunk becomes everyone's problem and merges become trust-based. **Corroborated** across CI/CD practitioner guides (jacob-balslev CI/CD skill; bjgreenberg multi-agent coordination; nerdev-co git-ci skill).
**Failure mode if skipped:** unreviewed pushes, "works on my machine" merges, red main discovered at deploy time.
**Agent angle:** with AI agents writing code, the mechanical gate matters more, not less — agents produce volume; the gate is the quality filter. Partition parallel agents by file/module to avoid collisions. **Inferred** from multi-agent coordination guidance.

### 1.2 Type checking + linting + formatting, enforced in CI

**What:** a type checker (mypy/pyright, TypeScript strict, etc.), a linter (ESLint, Ruff), and an opinionated formatter (Prettier, Black/ruff format) — all running as blocking CI checks, not optional local habits.
**Mechanics:** types catch wrong-shape data at write time; linters catch bug-prone patterns (unused vars, undefined names, overly broad catches); formatters end style debates permanently.
**Evidence (honest):** static typing prevents roughly 15% of public JS bugs (Gao et al. — **Verified**), improves code quality/readability, but does *not* strongly reduce overall bug density (Bogner & Merkel; UC Davis large-scale study: effects "quite small" — **Verified**). The 2026 TypeScript-ecosystem study explains why: today's fault density concentrates in config/dependency/testing layers. **Do not oversell types** — they are one layer. Their real, underrated value: they make code navigable and refactorable (fewer file switches, faster comprehension in controlled studies — **Verified**), which compounds over a codebase's life.
**Why still foundational:** cheap, fast (seconds), deterministic, and they catch the *stupid* bugs before humans or agents spend review cycles on them. Lint rules also encode team conventions mechanically (see 1.6).
**Failure mode if skipped:** style churn in every PR, "undefined is not a function" class bugs reaching review, refactors that nobody dares.

### 1.3 Dependency management: explicit, locked, scanned

**What:** every dependency declared in a manifest (`package.json`, `go.mod`, `requirements` via uv/pip-tools), versions locked (`package-lock.json`, `uv.lock`), no reliance on system-global packages, isolated environments (virtualenv, containers).
**Mechanics:** lockfiles make builds reproducible — "anyone can set up the environment from scratch with confidence" (12-factor, factor II). Automated updates (Dependabot/Renovate) + vulnerability scanning (`npm audit`, bandit, CodeQL, dependency review as CI checks).
**Why it prevents defects:** undeclared/unlocked dependencies produce "works here, breaks there" and silent breakage on transitive updates; unmaintained deps are the top-cited attack vector in practitioner CI guides. **Corroborated.**
**Failure mode if skipped:** irreproducible builds, supply-chain incidents, "it worked last week" mysteries.

### 1.4 Configuration & secrets: strict separation

**What:** config that varies between deploys (DB URLs, API keys, feature flags) lives *outside* the code: environment variables and/or a secret manager (Vault, AWS Secrets Manager/Parameter Store). Secrets never in version control — enforced by secret scanning in CI.
**Mechanics:** the 12-factor rule (config in the environment) keeps builds environment-independent; a `.env.example` (values blank) documents required variables; the app fails fast at startup on missing required config.
**Nuance (negative evidence):** env-var purism has real costs — one practitioner's account of 42 env vars producing 2-hour onboarding setups and prod-only drift bugs. Working compromise (**Inferred** as sound): version-controlled *non-secret* base config + environment overrides + secrets-only in env/secret manager + startup validation. The non-negotiable part is *secrets*, not the mechanism for everything.
**Failure mode if skipped:** leaked credentials in git history (unfixable by deletion alone — rotation required), environment-specific branches, prod surprises.

### 1.5 Test organisation with a real pyramid

**What:** tests organised by scope and speed — fast hermetic unit tests (base, many), integration/contract tests (middle), end-to-end against staging (top, few). Test layout mirrors source layout; module-boundary integration tests prove each module's public API.
**Mechanics:** CI runs fast-to-slow and fails fast; flaky tests are quarantined or fixed, never retried-into-green ("if the gates are advisory, the green checkmark is theater" — practitioner CI guide).
**Why it prevents defects:** tests traceable to requirements (FR IDs) make regressions *attributable* — you know which requirement broke. Contract tests at module/service boundaries catch the integration failures that unit tests can't see.
**Failure mode if skipped:** regressions discovered by users; fear-driven development (nobody refactors without tests).

### 1.6 Coding conventions + automated policy enforcement

**What:** written conventions (naming, error handling, API response shapes, import rules) *plus* mechanical enforcement: linters, import-boundary checkers (e.g., import-linter for modular-monolith module contracts), format-on-save, pre-commit hooks, and CI gates.
**Why it prevents defects:** conventions that live only in a wiki decay; conventions in CI are *law*. Module-boundary enforcement is the canonical example: "a convention that must be mechanically guarded, not just documented" (fusioniiit ADR). **Corroborated.**
**Failure mode if skipped:** boundary erosion, inconsistent error handling (silent swallows, string-matched errors), review cycles spent on style instead of logic.

### 1.7 Environment setup: one-command, documented, parity-checked

**What:** a new contributor (human or agent) goes from clone to running app + tests with documented, minimal steps — ideally one command (setup script, `docker compose up`, devcontainer). Dev/prod parity: the local stack resembles production closely enough that environment bugs are rare.
**Why it prevents defects:** every manual setup step is a drift vector; "works on my machine" is an environment bug, and environment bugs are the ones types and linters can't catch (the 2026 TS study's point).
**Failure mode if skipped:** multi-hour onboarding, environment-specific bugs, contributors who never run the full suite.

### 1.8 Docs that prevent re-litigation: README, ADRs, CONTRIBUTING

**What:** README (what this is, how to run, how to test, where things live); `docs/adrs/` (decision records — see 02 §"Reversible decisions"); CONTRIBUTING (how to propose changes, PR expectations, review bar).
**Why it prevents defects:** ADRs stop the same architecture debate every quarter and make broken assumptions inspectable; README/CONTRIBUTING stop the "how do I…?" interrupt cycle and the wrong-file edits. **Corroborated** (software-architecture-guild ADR guide; Google Cloud ADR docs).
**Failure mode if skipped:** decisions re-litigated, onboarding by oral tradition, repeated wrong-pattern contributions.

### 1.9 Project instructions for agents: AGENTS.md-style files

**What:** a repo-root (and per-package, in monorepos) markdown file telling coding agents how the project works: annotated structure, task→file mapping, conventions, common tasks, and *what not to do*. The cross-tool convention is `AGENTS.md` (backed by OpenAI, Google, Cursor et al.; 20,000+ repos by Aug 2025, 60,000+ by late 2025 per industry guides — **Corroborated** as adoption trend; exact counts **Unverified**). Claude Code natively reads `CLAUDE.md` (workaround: one-line `@AGENTS.md` import or symlink — **Verified** via Claude Code docs references and practitioner commits).
**What to include (highest value first):** task-to-file mapping ("add a page → src/app/…/page.tsx"); conventions (auth helper, DB client, error shapes); what-NOT-to-do (never edit generated dirs, never hand-roll auth); build/test commands. Keep it version-free where possible — restating facts that live in `build.sbt`/`package.json` rots (microsoft/synapseml commit lesson — first-hand practitioner).
**Why it prevents defects:** without it, agents guess — and agent guesses produce plausible, convention-violating code that passes casual review. Explicit anti-overengineering rules ("write the minimum code that solves *this* problem"; YAGNI test before abstracting) counter the documented agent default of over-abstraction (agents-playbook; jidechao AGENTS.md).
**Failure mode if skipped:** agents invent patterns, scatter logic across layers, build plugin systems for three fixed integrations.

---

## 2. Can safely be deferred — with explicit triggers

| Foundation | Defer until | Trigger to add it |
|---|---|---|
| Exhaustive ADRs for every decision | Team > ~5 or first "why did we…?" repeat | Second re-litigation of the same choice |
| Monorepo tooling (Nx/Turborepo, multi-package orchestration) | 2+ packages with real cross-deps | Build/test coupling actually hurts |
| Sophisticated CI (matrix builds, hermetic cert gates, multi-platform) | Fast core gates green and trusted | A defect class the core gates demonstrably miss |
| Full observability platform (traces, SLOs, error budgets) | Production traffic with users depending on it | First "we can't tell what broke" incident |
| Staging environment mirroring prod | Pre-launch or integration risk | E2E tests needed against realistic deps |
| Automated dependency updates (Renovate/Dependabot) | Dependency count becomes unmanageable manually | First missed critical CVE |
| Commit-message linting / conventional commits enforcement | History archaeology needed | "Which commit introduced this?" pain |
| Docs site / generated API docs | External consumers of the API | First external integrator |
| Reproducible-builds maximalism (pinned OS images, hermetic toolchains) | Regulated/compliance context or supply-chain incident | Audit requirement or incident |
| Feature-flag infrastructure (dedicated service) | Need to decouple deploy from release | First "we can't ship because X isn't ready" |
| Load/perf test harness | NFRs at risk | First perf regression or pre-launch gate |

**Principle:** defer *ceremony*, never *gates*. The blocking CI checks (§1.1–1.2), lockfiles, and secret hygiene are day-one; the elaborate pipeline stages can grow when a missed defect class justifies them. Each deferred item gets a trigger — "deferred is not deleted."

---

## 3. The defect-prevention ranking (why this order)

1. **Spec quality** (01) — prevents the largest, costliest defect class; nothing downstream compensates.
2. **Protected main + required CI** — prevents integration defects and makes all other gates trustworthy.
3. **Types + lint + format in CI** — prevents cheap bug classes at seconds of cost.
4. **Locked deps + secret hygiene** — prevents irreproducibility and credential incidents (the unfixable-by-revert kind).
5. **Test pyramid traceable to requirements** — prevents regressions and makes failures attributable.
6. **Mechanical convention enforcement** (import boundaries, pre-commit) — prevents architectural erosion.
7. **One-command env setup + parity** — prevents environment-class bugs, the layer types can't reach.
8. **ADRs + README + CONTRIBUTING + AGENTS.md** — prevents re-litigation, wrong-file edits, and agent invention.

Items 1–4 are *load-bearing*: each prevents a defect class that is expensive, recurring, and unfixable by later diligence. Items 5–8 are *compounding*: their value grows with team size, codebase age, and agent involvement.

---

## 4. Reproducible builds — what it actually means

**Plain English:** the same source + the same declared inputs always produce the same runnable artifact, on any machine. **Mechanics:** locked dependencies, pinned base images/toolchains, no network access or timestamps leaking into artifacts, builds from clean checkouts in CI (not from a developer's laptop state). **Why:** "it built on my machine" and "the deployed artifact differs from the tested one" are the same defect — unverified provenance. CI builds the artifact once, signs it, and promotes *that same artifact* through environments (never rebuild per environment). **Label: Corroborated** as CI/CD best practice; full hermetic reproducibility (bit-for-bit) is a higher bar needed mainly in regulated/supply-chain-sensitive contexts — deferrable otherwise (see table).
