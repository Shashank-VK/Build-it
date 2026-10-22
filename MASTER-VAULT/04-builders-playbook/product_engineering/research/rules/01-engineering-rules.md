# §31 — Canonical Engineering-Rules Catalogue

**Workstream:** rules · **Built:** 2026-10-10 · **Read-only:** research only — these rules are documented practice and synthesised guidance, not adoption advice.

Each rule carries: the rule itself; why it exists; evidence (with claim labels per `05-evidence-register.md`); the context where it applies; the risks it addresses; what violating it looks like; how it can be enforced; whether enforcement can be automated; what exceptions may be justified; and a classification.

**Classifications:** *Critical control* (violation can kill the product/company — non-negotiable), *Release gate* (must be satisfied before a release ships), *Strong practice* (default for professional teams; skipping needs a reason), *Context-dependent recommendation* (apply when the context matches), *Company-specific convention* (documented at a specific company; adopt deliberately, not by default).

Evidence tags like `[E-KNIGHT · Verified]` resolve in `05-evidence-register.md`.

---

## Discovery

### R-01 — Ship outcomes, not outputs
- **Classification:** Critical control (for any funded initiative); Release gate (for feature approval).
- **The rule:** No significant build begins without a named, measurable customer or business outcome it is expected to move, and a falsifiable belief about why the build will move it.
- **Why it exists:** Organisations that manage by output volume drift into the build trap: schedules full of shipped features, no movement in anything customers or the business cares about. An outcome-first rule forces the "why" before the "what".
- **Evidence:** Perri's build-trap diagnosis — companies that "live and die by outputs" ship features to meet schedules rather than customer needs `[E-BUILDTRAP · Verified]`; Ries's innovation accounting — progress is validated learning against metrics, not lines shipped `[E-LEAN · Corroborated]`.
- **Applies when:** any work consuming more than a trivial appetite; product teams; funded roadmaps.
- **Risks addressed:** feature factories; wasted engineering capacity; shipping things nobody uses.
- **Violation looks like:** a roadmap measured in "features shipped per quarter"; a launch with no success metric defined; "we'll figure out the metrics after launch".
- **Enforcement:** every initiative document names its outcome metric and target before resourcing; leadership reviews outcome movement, not output counts.
- **Automatable:** Partially — dashboards can track outcome metrics and flag launches with none defined; the judgment of *which* outcome is human.
- **Exceptions:** pure infrastructure/tech-debt work (outcome = lead time, reliability, cost — still measurable); exploratory spikes (timeboxed, outcome = a decision).

### R-02 — Define the measurable success metric before the build
- **Classification:** Strong practice.
- **The rule:** Before building, write down the metric, the target, the time window, and what you will do if the target is missed (persevere, fix, or kill).
- **Why it exists:** Metrics defined after launch get chosen to flatter the launch. Pre-commitment converts "did it work?" from politics into arithmetic.
- **Evidence:** Ries's innovation accounting and the pivot/persevere decision `[E-LEAN · Corroborated]`; Shape Up's appetite as a pre-committed budget — the business owes the team a bounded spend, the team owes a shippable slice `[E-SHAPEUP · Verified]`.
- **Applies when:** every product change with a hypothesis behind it.
- **Risks addressed:** vanity metrics; zombie features nobody owns; sunk-cost continuation.
- **Violation looks like:** "success = launch on time"; post-hoc metric shopping; a feature with no owner six months later.
- **Enforcement:** the PRD/template 03 requires a metrics section; post-launch evaluation (template 16) compares actuals to the pre-committed target.
- **Automatable:** Yes for tracking (dashboards, alerts on metric movement); no for choosing the metric.
- **Exceptions:** None — even a spike's metric can be "decision made by date X".

### R-03 — Retire the four product risks before committing to build
- **Classification:** Strong practice.
- **The rule:** Before significant build, gather evidence against four risks: value (will anyone want it?), usability (can they use it?), feasibility (can we build it?), viability (does it work for the business?). Unretired risks are explicit, not assumed away.
- **Evidence:** Cagan's four-risk framework is the standard product-discovery canon `[E-CAGAN · Corroborated]`; Torres's continuous discovery — weekly customer contact and opportunity-solution trees `[E-TORRES · Corroborated]`; Perri's outcome-over-output argument `[E-BUILDTRAP · Verified]`.
- **Applies when:** new products, new features, new markets; proportionally lighter for iterations on proven surfaces.
- **Risks addressed:** building the wrong thing well; usability failures discovered after launch; infeasible architectures; unit-economics surprises.
- **Violation looks like:** "the CEO asked for it" as the entire evidence base; a prototype tested only by the team that built it; feasibility discovered mid-build.
- **Enforcement:** problem-validation and idea-evaluation templates (04-templates/01, 02) require one evidence line per risk; unretired risks are listed as bets in the PRD.
- **Automatable:** No — evidence gathering is human work; templates make omissions visible.
- **Exceptions:** Throwaway prototypes and spikes (their purpose *is* to retire feasibility risk cheaply); emergency fixes.

### R-04 — Write the launch artefact before the design
- **Classification:** Company-specific convention (Amazon); Context-dependent recommendation elsewhere.
- **The rule:** For significant initiatives, write the customer-facing announcement (press release / launch note / changelog entry) and an FAQ answering hard internal and external questions *before* design or engineering starts. If the press release is boring or the FAQs have no answers, the idea is not ready.
- **Why it exists:** Writing the finished-product story in plain prose surfaces weak thinking that hides in bullet points and live narration; it forces customer language, pricing, and tradeoffs to be confronted early.
- **Evidence:** Amazon's Working Backwards PR/FAQ and six-page narrative practice — Bezos's 2004 internal email on narrative forcing better thought; most PR/FAQs are rejected, which is the point `[E-AMZN · Verified for mechanics, Corroborated for efficacy]`.
- **Applies when:** new products, major features, API launches, pricing changes — anywhere the customer story is non-obvious.
- **Risks addressed:** solution-in-search-of-a-problem; undiscovered pricing/economics holes; launch-day messaging invented under pressure.
- **Violation looks like:** a design doc with no customer problem paragraph; launch copy written the week of release; FAQs that dodge price and limitations.
- **Enforcement:** require the PR/FAQ as the first artefact in the initiative folder; review it before resourcing.
- **Automatable:** No.
- **Exceptions:** Internal tooling with no external customer (write the internal announcement instead); tiny iterations.

---

## Design

### R-05 — Fix the time, flex the scope
- **Classification:** Strong practice.
- **The rule:** Give work a fixed appetite (how much time it is worth), then cut scope — never quality — to fit. Work that cannot fit the appetite is re-scoped or killed, not extended.
- **Why it exists:** Estimates grow to protect the team; appetites shrink the problem to protect the calendar. Fixed time forces the decisions about what truly matters instead of letting scope expand indefinitely.
- **Evidence:** Shape Up's appetite-vs-estimate inversion and circuit breaker — overrun work dies rather than borrowing next cycle's budget `[E-SHAPEUP · Verified]`; consistent with DORA's small-batch findings `[E-DORA · Verified]`.
- **Applies when:** product development cycles; any team that has ever watched a deadline slip by "just two more weeks" repeatedly.
- **Risks addressed:** scope creep; death-march projects; quality sacrificed to protect scope.
- **Violation looks like:** fixed-scope/fixed-date commitments; "we're 80% done" for three months; cutting testing to protect the feature list.
- **Enforcement:** shaping produces explicit no-gos and rabbit holes (template 04); the circuit breaker is honoured publicly when invoked.
- **Automatable:** No — but cycle dashboards make overruns visible.
- **Exceptions:** Regulatory deadlines with genuinely fixed scope (then fix time by adding parallelism early, or descope explicitly with stakeholders); R&D with unknowable scope (timebox as a spike).

### R-06 — Record significant decisions where the code lives
- **Classification:** Strong practice.
- **The rule:** Architectural and consequential product decisions are recorded as short Architecture Decision Records (context → decision → consequences) stored alongside the code, written at decision time.
- **Why it exists:** Code shows *what*; six months later nobody remembers *why*. ADRs make the reasoning reviewable, onboarding faster, and reversals deliberate instead of accidental.
- **Evidence:** Nygard's ADR proposal (2011) and its standardisation across the industry `[E-ADR · Corroborated]`; consistent with Amazon narrative discipline `[E-AMZN]`.
- **Applies when:** any decision that constrains future work (tech choices, data models, API contracts, build-vs-buy).
- **Risks addressed:** re-litigating settled decisions; accidental reversal of load-bearing choices; knowledge loss when people leave.
- **Violation looks like:** "we chose Postgres because… uh"; the same framework debate every year; a migration that rediscovers why the old choice was made.
- **Enforcement:** template 05 in the repo; code review asks "where's the ADR?" for structural changes.
- **Automatable:** Partially — linters can require an ADR file reference in PRs touching architecture paths; content is human.
- **Exceptions:** Truly reversible, low-stakes choices (naming, formatting); decisions fully captured in the PR description for small changes.

### R-07 — Spend innovation tokens only on what differentiates you
- **Classification:** Strong practice.
- **The rule:** For everything that is not your core differentiation, choose the boring, battle-tested technology. Novelty is a budget: spend it where it buys advantage.
- **Why it exists:** Every exotic choice is operational debt you pay forever — in hiring, debugging, upgrades, and 3 a.m. pages. Boring technology has known failure modes and a community that has already survived them.
- **Evidence:** McKinley's "Choose Boring Technology" — innovation tokens are scarce `[E-BORING · Corroborated]`; Gall's law — working complex systems evolve from working simple ones `[E-GALL · Corroborated]`.
- **Applies when:** technology selection for startups and small teams especially; any team without dedicated platform staff.
- **Risks addressed:** unnecessary infrastructure (AP-17); operational overload; hiring bottlenecks around exotic stacks.
- **Violation looks like:** a three-person team running Kubernetes, Kafka, and a service mesh for a CRUD app; choosing a database because the conference talk was exciting.
- **Enforcement:** tech choices require an ADR (R-06) naming what is boring and where the innovation tokens are spent.
- **Automatable:** No.
- **Exceptions:** The product *is* the novel technology (then the novelty is the differentiation); research spikes.

### R-08 — No speculative generality (YAGNI)
- **Classification:** Strong practice.
- **The rule:** Build what is needed now, with clean seams for what is likely next. Do not build frameworks, abstractions, or configurability for futures that have no committed customer.
- **Why it exists:** Speculative abstractions are the most expensive code: they complicate the real use case, ossify wrong guesses, and must be maintained. The future is a poor requirements author.
- **Evidence:** XP/Fowler simplicity discipline `[E-FOWLER · Corroborated]`; Ousterhout on deep modules and complexity being incremental `[E-OUSTERHOUT · Corroborated]`; premature abstraction is a named anti-pattern (AP-05).
- **Applies when:** all application code; especially early-stage products.
- **Risks addressed:** premature abstraction; framework-itis; code nobody dares to delete.
- **Violation looks like:** a plugin architecture with one plugin; configuration for scenarios never requested; "we'll need it when we scale".
- **Enforcement:** code review challenges generality without a current caller; shaping lists no-gos (R-05).
- **Automatable:** Partially — dead-code and unused-parameter analysis catches some; judgment is human.
- **Exceptions:** Genuine platform work (the abstraction *is* the product); stable, well-understood domain patterns (e.g., i18n from day one for a global product).

### R-09 — Threat-model before you build trust boundaries
- **Classification:** Release gate (for systems handling sensitive data, money, identity, or safety-relevant functions); Strong practice otherwise.
- **The rule:** Before building anything that crosses a trust boundary (auth, payments, PII, multi-tenant isolation, AI agents with tool access), produce a lightweight threat model: assets, actors, entry points, and how each is mitigated. Revisit when the boundary moves.
- **Why it exists:** Security retrofitted after build is architecture-shaped; threat modeling at design time is cheap and finds the flaws that code review cannot (missing checks, confused deputy, excessive agent permissions).
- **Evidence:** Shostack's threat-modeling discipline `[E-SHOSTACK · Corroborated]`; OWASP ASVS V1 (Architecture, Design and Threat Modeling) requires it `[E-ASVS · Verified]`; Perry/Pearce show AI-generated auth/crypto code is disproportionately vulnerable `[E-PERRY · Verified]`.
- **Applies when:** trust boundaries, as above; agent tool permissions (what can the agent touch?).
- **Risks addressed:** weak security (AP-08); uncontrolled agents (AP-10); authorisation flaws — consistently among the costliest defect classes.
- **Violation looks like:** an agent with full production database write access "for now"; auth designed as "we'll add roles later"; no list of what the system trusts.
- **Enforcement:** security-verification template (04-templates/13) requires the threat-model section; release gate for sensitive systems.
- **Automatable:** Partially — attack-surface inventories can be generated; the model itself is human.
- **Exceptions:** Purely local, single-user, no-network prototypes; static content sites (still do the 10-minute version).

### R-10 — Design for failure at every integration point
- **Classification:** Strong practice.
- **The rule:** Every call across a process or network boundary gets an explicit failure strategy: timeout, retry-with-backoff (only where idempotent), circuit breaker, bulkhead isolation, or graceful degradation. "It won't fail" is not a strategy.
- **Why it exists:** Integration points are the #1 killer of system stability; failures propagate and cracks accelerate under load. Resilience is a design concern, not an operations afterthought.
- **Evidence:** Nygard's stability patterns — timeout, circuit breaker, bulkhead, fail fast, steady state, back-pressure `[E-RELEASEIT · Verified]`; independently re-codified by Microsoft Azure Architecture Center.
- **Applies when:** any distributed call: HTTP APIs, databases, queues, LLM provider calls, webhooks.
- **Risks addressed:** cascading failures; fragile architecture (AP-06); 3 a.m. pages from a slow vendor.
- **Violation looks like:** HTTP calls with no timeout; retry storms amplifying an outage; one slow dependency exhausting the whole connection pool.
- **Enforcement:** design review checklist (template 04) asks the failure question per integration; load/chaos testing verifies the strategy.
- **Automatable:** Partially — linters can flag missing timeouts; libraries can default them on.
- **Exceptions:** None for production paths; prototypes may defer but must label the debt.

---

## Build

### R-11 — Everything in version control; mainline always releasable
- **Classification:** Critical control.
- **The rule:** All production artefacts (code, config, infra, docs-that-matter) live in version control. The main branch is always in a releasable state: every merge keeps the build green and the suite passing.
- **Why it exists:** Version control is the difference between "we lost the code" and "we rolled back in minutes". A releasable mainline is what makes every other shipping discipline (small batches, fast recovery, bisecting) possible.
- **Evidence:** Joel Test items #1–3 (source control, one-step build, daily builds — modernised to CI) `[E-JOEL · Verified]`; DORA elite performance rests on trunk-based flow `[E-DORA · Verified]`; Knight Capital's partial deployment is what happens when release discipline is manual and unverified `[E-KNIGHT · Verified]`.
- **Applies when:** always, from the first commit.
- **Risks addressed:** unrecoverable loss; unrepeatable builds; "works on my machine" releases; partial deployments.
- **Violation looks like:** config edited directly in production; "don't deploy on Fridays because main is broken"; releases assembled by hand.
- **Enforcement:** branch protection (no direct pushes to main); CI must pass before merge; releases built only from tagged mainline commits.
- **Automatable:** Yes — branch protection, required checks, and tag-only release pipelines.
- **Exceptions:** None. This is the floor.

### R-12 — One-step, reproducible builds; build, release, and run strictly separated
- **Classification:** Critical control.
- **The rule:** A release is produced by one command from a clean checkout, reproducibly. Build (compile artefacts), release (combine artefact + config), and run (execute in the environment) are distinct, auditable stages — the same artefact that was tested is what ships.
- **Why it exists:** Multi-step manual builds are error-prone exactly when stakes are highest (near shipping). Stage separation is what makes "test what you ship" literally true.
- **Evidence:** Joel Test #2 (one-step build) `[E-JOEL · Verified]`; Twelve-Factor V (build/release/run) `[E-12F · Verified]`; Knight Capital's inconsistent server state is the failure mode `[E-KNIGHT · Verified]`.
- **Applies when:** any software that ships to anyone beyond the author's laptop.
- **Risks addressed:** broken releases; untestable artefacts; deployment drift across machines.
- **Violation looks like:** a release runbook with 14 manual steps; "the staging build is different from the prod build"; binaries built on a developer laptop.
- **Enforcement:** CI builds all release artefacts; the release pipeline promotes immutable artefacts between environments.
- **Automatable:** Yes — this rule is almost entirely automation.
- **Exceptions:** None for shipped software.

### R-13 — No AI-generated code reaches production unverified
- **Classification:** Critical control.
- **The rule:** Code produced with AI assistance is treated as untrusted input until a human (or a qualified independent check) has reviewed, tested, and understood it. The dividing line is review, not AI use: reviewed, tested, explainable AI-assisted code is normal software development; unreviewed output is not shippable.
- **Why it exists:** Measured evidence shows AI assistance increases vulnerability rates (~40% of Copilot completions vulnerable across CWE scenarios; AI-assisted participants produced significantly less secure code) *and* inflates developer confidence in the result. The model optimises for plausible, not correct.
- **Evidence:** Pearce et al. ~40% vulnerable (replication ~27%) `[E-PEARCE · Verified]`; Perry et al. — less secure code *plus* higher self-reported confidence `[E-PERRY · Verified]`; 56.4% of professionals report insecure AI suggestions are common `[E-SNYK · Corroborated]`; hallucinated package names as supply-chain vector `[E-LANYADO · Corroborated]`; Karpathy's own scope ("throwaway weekend projects") and Willison's review boundary `[E-KARPATHY · Verified]`.
- **Applies when:** any AI-generated or AI-modified code, config, infra, or migration destined for production or shared use.
- **Risks addressed:** AI-generated code without verification (AP-09); supply-chain injection via hallucinated dependencies; confident-but-wrong security logic.
- **Violation looks like:** "Accept All" on diffs; merged PRs the author cannot explain; AI-suggested packages installed without checking they exist.
- **Enforcement:** code review explicitly covers AI-assisted diffs (template 11); SAST/SCA/secrets scans run on every PR; dependency additions verified against registries.
- **Automatable:** Partially — scanners catch known-bad patterns; understanding and design review are human.
- **Exceptions:** Genuinely throwaway prototypes (Karpathy's original scope) — still never merged to main; boilerplate/config where the diff is trivially reviewable at a glance (review is then cheap, not skipped).

### R-14 — Keep changes small, coherent, and reviewable
- **Classification:** Strong practice.
- **The rule:** Changes are sliced so one change does one thing and can be reviewed in one sitting. Large changes are stacked or split; "big bang" PRs are the exception requiring justification.
- **Why it exists:** Review quality collapses as diff size grows; small changes are easier to test, revert, bisect, and deploy safely. Throughput and stability both come from small batches.
- **Evidence:** DORA — elite performers deploy on demand with <1-day lead times, which structurally requires small batches `[E-DORA · Verified]`; Google's engineering practices on small CLs (Corroborated, industry-wide).
- **Applies when:** all code review; especially agent-produced code, which tends toward large diffs.
- **Risks addressed:** rubber-stamp reviews; unrevertable changes; slow lead times.
- **Violation looks like:** 3,000-line PRs titled "misc fixes"; refactors bundled with behaviour changes; agent sessions that rewrite half the repo.
- **Enforcement:** PR size guidance in the review template; agent instructions (template 09) cap diff scope per task.
- **Automatable:** Partially — CI can warn on diff size; splitting is human.
- **Exceptions:** Mechanical codemods and generated code (review the generator and spot-check the output); initial repo scaffolding.

### R-15 — Configuration in the environment; secrets never in code
- **Classification:** Critical control.
- **The rule:** Anything that varies between deploys (credentials, endpoints, feature flags, tuning) lives in the environment, not the codebase. Secrets are never committed, never logged, never pasted into chats or prompts.
- **Why it exists:** Code is copied, forked, screenshared, and fed to AI tools; secrets in code leak through all of those. Env-based config is also what makes one artefact deployable everywhere (R-12).
- **Evidence:** Twelve-Factor III (config in environment) `[E-12F · Verified]`; continuous public secret-leak incidents (Corroborated, industry-wide).
- **Applies when:** always.
- **Risks addressed:** credential leaks; environment-specific code branches; unshippable artefacts.
- **Violation looks like:** API keys in the repo history; `.env` committed "temporarily"; secrets in AI chat transcripts and logs.
- **Enforcement:** secrets scanners on every commit/PR (block on detection); environment-based config required by the deploy pipeline.
- **Automatable:** Yes — pre-commit and CI secret scanning; this is one of the most automatable rules.
- **Exceptions:** None. (Local dev uses local secret stores, not committed files.)

### R-16 — Delete dead code; never repurpose flags or identifiers
- **Classification:** Strong practice.
- **The rule:** Dead code is deleted, not left dormant. Feature flags, config keys, and identifiers are never recycled for new meanings — a retired name stays retired.
- **Why it exists:** Dormant code is a loaded weapon: a future change can re-arm it in ways no one predicts. Repurposed identifiers create action-at-a-distance bugs that code review cannot see, because the danger lives in the *old* code nobody is reading.
- **Evidence:** Knight Capital — "Power Peg" dead since ~2003 was reactivated when its flag was repurposed for the Retail Liquidity Program; the old code existed on the one un-updated server `[E-KNIGHT · Verified]`. This rule is substantially *synthesised from* that incident `[Proposed as a named rule; evidence Verified]`.
- **Applies when:** all codebases, especially long-lived ones with flag systems.
- **Risks addressed:** reactivation of dead behaviour; flag-collision outages; untestable legacy paths.
- **Violation looks like:** commented-out blocks "kept just in case"; `if (false)` branches; a flag named `enable_new_checkout` now controlling something unrelated.
- **Enforcement:** code review; flag lifecycle (creation → rollout → cleanup ticket); periodic dead-code sweeps.
- **Automatable:** Partially — coverage and static analysis flag unreachable code; flag-cleanup needs process.
- **Exceptions:** None for repurposing identifiers. For deletion: keep dead code only behind a dated removal ticket, not indefinitely.

### R-17 — No optimisation without measurement
- **Classification:** Strong practice.
- **The rule:** Performance work starts from a measured baseline, a profiled bottleneck, and a target. "It might be slow" is not a finding.
- **Why it exists:** Programmers reliably mis-predict bottlenecks; unmeasured optimisation complicates code, introduces bugs, and usually optimises the wrong thing. Measurement also defines "done".
- **Evidence:** Knuth (1974) on premature optimisation `[E-KNUTH · Corroborated]`; DORA/Accelerate's warning against optimising without outcome linkage `[E-DORA · Verified]`.
- **Applies when:** all performance work; capacity planning.
- **Risks addressed:** excessive automation/over-engineering (AP-11); complexity without benefit; optimisation that pessimises.
- **Violation looks like:** caching layers added before any latency measurement; microservice splits "for performance" with no load data; hand-rolled data structures in cold paths.
- **Enforcement:** performance tasks require baseline/profile/target in the task definition (template 08); load tests verify the gain.
- **Automatable:** Partially — profiling and benchmarks are tools; the decision is human.
- **Exceptions:** Known-asymptotic mistakes (an O(n²) loop over unbounded input found by inspection); choosing a sane default (index the obvious column).

---

## Test

### R-18 — Critical paths are tested, and releases gate on the tests
- **Classification:** Release gate.
- **The rule:** The paths that must work (signup, payment, core workflow, data integrity) have automated tests, and a red suite blocks the release. Coverage is a side effect; the gate is "the critical paths are proven on every change".
- **Why it exists:** Untested critical paths fail at the worst moment — under real load, on release day. A gate converts "we should test" into "the pipeline refuses to ship".
- **Evidence:** Joel Test modernisation (build *and test* before merge) `[E-JOEL · Verified]`; CrowdStrike — the missing test for non-wildcard matching in the 21st field is exactly the untested critical path `[E-CROWD · Verified]`; DORA change-failure-rate as the stability metric `[E-DORA · Verified]`; WHO/Pronovost — verification checklists as gates catch what memory misses `[E-GAWANDE · Verified]`.
- **Applies when:** any release to real users; proportionally to blast radius.
- **Risks addressed:** poor testing (AP-07); regressions shipped silently; release-day surprises.
- **Violation looks like:** "we'll test after launch"; a suite so flaky the gate is routinely overridden; critical flows covered only by manual clicking.
- **Enforcement:** CI gates on the suite; flaky-test quarantine with owner and deadline; test plan template (04-templates/10).
- **Automatable:** Yes — gating is automation; writing meaningful tests is human.
- **Exceptions:** None for critical paths. Non-critical paths may carry lighter coverage with the gap recorded.

### R-19 — Test the thing that actually ships, through the path it actually takes
- **Classification:** Strong practice.
- **The rule:** Tests exercise production-shaped inputs through the real code path — including content, config, and data pipelines, not just application code. Dev/prod parity is maintained so test results mean something.
- **Why it exists:** CrowdStrike's code passed "multiple layers" of testing because every test used a wildcard in the dangerous field — the tests never exercised the real input path. Mocks and fixtures that don't resemble production prove nothing about production.
- **Evidence:** CrowdStrike RCA — wildcard matching in tests hid the 21-vs-20 mismatch until the first real template instance `[E-CROWD · Verified]`; Twelve-Factor X (dev/prod parity) `[E-12F · Verified]`; Nygard's test-harness pattern — simulate nasty, real failure modes, not happy paths `[E-RELEASEIT · Verified]`.
- **Applies when:** anything with config/content/data pipelines (feature flags, ML prompts, detection rules, migrations); integration tests generally.
- **Risks addressed:** false confidence from green suites; content-shipped bugs that bypass code review; environment-specific failures.
- **Violation looks like:** tests that only use happy-path fixtures; content updates deployed with no validation; "it passed in staging" where staging differs from prod.
- **Enforcement:** test plan (template 10) requires production-shaped cases for risky paths; content/config changes get the same pipeline as code.
- **Automatable:** Partially — contract tests, fixture generators, parity checks; designing adversarial cases is human.
- **Exceptions:** None — but depth scales with risk (a blog's CSS needs less than a payment content pipeline).

### R-20 — Every production change gets a second pair of eyes
- **Classification:** Release gate.
- **The rule:** No change reaches production without review by someone (or something qualified) other than the author. For high-risk changes — auth, money, data migration, security boundaries — the reviewer must be a qualified human, and AI-generated diffs get extra scrutiny, not less.
- **Why it exists:** Authors are blind to their own assumptions; review catches the class of errors testing misses (wrong requirements, missing edge cases, security logic flaws). Evidence shows AI-assisted authors are *more* confident and *less* secure — the review must be independent of the generator.
- **Evidence:** Perry et al. — AI-assisted developers wrote less secure code while believing it more secure, so the reviewer cannot be the same overconfident loop `[E-PERRY · Verified]`; industry code-review research (Bacchelli & Bird and successors) finds review catches defects testing misses `[Corroborated]`; GitLab's public postmortem culture shows review as a learning surface `[E-GITLAB · Verified]`.
- **Applies when:** all production changes; bar raises with risk.
- **Risks addressed:** AI-generated code without verification (AP-09); single-author blind spots; "works on my machine" logic errors.
- **Violation looks like:** self-merged PRs to main; rubber-stamp "LGTM" in 30 seconds; AI review bots as the *only* reviewer on security-sensitive diffs.
- **Enforcement:** branch protection requiring review; review checklist (template 11) with risk-tiered reviewer requirements.
- **Automatable:** Partially — assignment, checklists, and AI pre-review; the judgment is human.
- **Exceptions:** Automated, pre-approved change classes (dependency patch bumps within policy, generated-code regeneration with pinned inputs) — the *policy* was human-reviewed instead.

---

## Secure

### R-21 — Least privilege by default, everywhere
- **Classification:** Critical control.
- **The rule:** Every identity — human, service, and AI agent — gets the minimum permissions it needs, for the minimum time it needs them. Defaults deny; access is granted explicitly and reviewed periodically.
- **Why it exists:** Breaches and mistakes are bounded by the permissions of the compromised or mistaken actor. Over-privileged agents and service accounts convert small bugs into total compromise.
- **Evidence:** NIST CSF/SP 800-53 least-privilege controls `[E-NIST · Corroborated]`; ASVS access-control chapters `[E-ASVS · Verified]`; Anthropic's guidance that agents need guardrails and bounded tool access `[E-ANTHROPIC · Verified]`; Knight Capital had no effective kill switch or risk limit wired to anything `[E-KNIGHT · Verified]`.
- **Applies when:** IAM, service accounts, API keys, database roles, and especially agent tool permissions.
- **Risks addressed:** weak security (AP-08); uncontrolled agents (AP-10); blast-radius amplification of any bug.
- **Violation looks like:** `admin` service accounts for read-only jobs; agents with production write access "temporarily" for six months; wildcard IAM policies.
- **Enforcement:** permission reviews on a cadence; agent tool manifests reviewed like code; alerts on privilege escalations.
- **Automatable:** Partially — IAM analysers flag excess privilege; right-sizing needs human judgment.
- **Exceptions:** Break-glass emergency access — timeboxed, logged, and reviewed after.

### R-22 — Meet ASVS Level 1 before any internet-facing deploy
- **Classification:** Release gate.
- **The rule:** Before an internet-facing application serves real traffic, it is verified against OWASP ASVS Level 1 (the automatable baseline: auth, session, access control, input validation, crypto, logging, config, and the rest). Level 2 becomes the target as the product matures and handles sensitive data.
- **Why it exists:** "We take security seriously" is not verifiable; a levelled, versioned requirement catalogue turns it into pass/fail rows with evidence. L1 is deliberately the set of controls testable by automation — there is no cost excuse.
- **Evidence:** OWASP ASVS v4.0.3/v5.0.0 — 14/17 chapters, three cumulative levels `[E-ASVS · Verified]`; Pearce/Perry show the vulnerability classes ASVS covers are exactly what AI-assisted code gets wrong `[E-PEARCE · Verified][E-PERRY · Verified]`.
- **Applies when:** any internet-facing application or API; internal tools proportionally.
- **Risks addressed:** weak security (AP-08); procurement failures; the OWASP Top 10 recurring in every new codebase.
- **Violation looks like:** launch with no security review at all; "we'll do a pentest next quarter" as the entire plan; auth hand-rolled without a requirement list.
- **Enforcement:** security-verification template (04-templates/13) structured on ASVS chapters; the gap register (pass/fail/N-A per requirement, owner, close date) is the release artefact.
- **Automatable:** Substantially — L1 is designed for automated verification (SAST, SCA, DAST, secrets scanning); L2/L3 need manual review.
- **Exceptions:** None for internet-facing. Truly local/offline prototypes may defer with a written date.

### R-23 — Patch known vulnerabilities promptly; know your dependencies
- **Classification:** Release gate (for critical/high severity in reachable code); Strong practice otherwise.
- **The rule:** Dependencies are pinned via lockfiles, inventoried (SBOM or equivalent), continuously scanned, and patched on a defined SLA by severity — critical reachable vulnerabilities same-day to days, not quarters.
- **Why it exists:** Attackers industrialised the window between disclosure and patching. Log4Shell showed a transitive logging dependency could be a remote-code-execution vector in nearly everything. You cannot patch what you cannot inventory.
- **Evidence:** Log4Shell (CVE-2021-44228, Dec 2021) and the CISA emergency directive `[E-LOG4J · Corroborated]`; ASVS malicious-code/supply-chain chapter `[E-ASVS · Verified]`; hallucinated-package supply-chain attacks `[E-LANYADO · Corroborated]`.
- **Applies when:** any shipped software with dependencies (i.e., all of it).
- **Risks addressed:** weak security (AP-08); supply-chain compromise; silent exposure windows.
- **Violation looks like:** no lockfile; dependencies updated "when someone remembers"; a critical CVE unpatched for months; no inventory of what's even deployed.
- **Enforcement:** SCA scanning in CI blocking on critical; patch-SLA tracked like any SLA; SBOM generated per release.
- **Automatable:** Yes — scanning, inventory, and even automated patch PRs; the merge decision stays human for risky majors.
- **Exceptions:** Unreachable vulnerabilities (documented with reachability analysis, not assumed); end-of-life dependencies get a migration plan with a date, not indefinite exception.

### R-24 — Backups exist, are monitored, and restore-tested
- **Classification:** Critical control.
- **The rule:** Production data is backed up on a schedule, backup *success* is monitored with alerts that are themselves tested end-to-end, and restores are rehearsed on a cadence — because a backup that cannot be restored is not a backup.
- **Why it exists:** GitLab had four backup/replication procedures; the one that saved them was an accident. Silent backup failure (pg_dump version mismatch; failure emails eaten by DMARC) plus untested restore is the standard shape of data-loss incidents.
- **Evidence:** GitLab 2017 — 300GB deleted, silent pg_dump failures, undelivered alerts, 18-hour restore from a lucky snapshot `[E-GITLAB · Verified]`.
- **Applies when:** any production data you cannot afford to lose or recreate.
- **Risks addressed:** unrecoverable data loss; extended outages; the "replication is not recovery" fallacy.
- **Violation looks like:** "backups run nightly" with nobody checking; restore never attempted; alerts that fire into a dead mailbox.
- **Enforcement:** restore drills on a calendar (game days); alert-path tests (break the notifier, confirm a human gets paged); RPO/RTO written down and verified.
- **Automatable:** Substantially — backup verification jobs, automated restore-to-staging, alert-path synthetics; the drill discipline is human.
- **Exceptions:** None for production data. Ephemeral/cache data is explicitly classified as such — the classification itself is the control.

---

## Ship

### R-25 — Every release is reversible and rolled out progressively
- **Classification:** Release gate.
- **The rule:** Every production change can be undone quickly (rollback, feature-flag kill, traffic shift), and risky changes reach users progressively (canary / staged rollout / blue-green) rather than all at once. Rollback is rehearsed, not theoretical.
- **Why it exists:** Knight Capital's panicked rollback of healthy servers *spread* the defect to the whole fleet — reversibility without a rehearsed, correct procedure is not reversibility. CrowdStrike's own RCA lists staged deployment as a required fix. Blast-radius control is what converts incidents from company-killers into bad afternoons.
- **Evidence:** Knight Capital — rollback made it worse; no kill switch `[E-KNIGHT · Verified]`; CrowdStrike RCA finding: "Template Instances should have staged deployment" `[E-CROWD · Verified]`; Twelve-Factor IX (disposability: fast startup/graceful shutdown enables safe rollout) `[E-12F · Verified]`; Release It! steady-state and bulkhead thinking `[E-RELEASEIT · Verified]`.
- **Applies when:** every production release; progressive rollout scales with blast radius.
- **Risks addressed:** unrecoverable bad deploys; fleet-wide simultaneous failure; panic-driven remediation.
- **Violation looks like:** "rollback" meaning "re-deploy the old build and hope"; 100% traffic flips on Friday evening; database migrations with no down-migration or expand/contract plan.
- **Enforcement:** release-readiness checklist (template 14) requires the rollback procedure and rollout plan; game-day the rollback quarterly.
- **Automatable:** Substantially — progressive-delivery controllers automate canary analysis and automatic rollback on metric regression.
- **Exceptions:** Irreversible-by-nature changes (data migrations, crypto key rotations) — these get the *strictest* progressive treatment and rehearsal, not an exemption from the rule's intent.

### R-26 — Gate risky changes behind flags, not branches
- **Classification:** Context-dependent recommendation.
- **The rule:** Behaviour changes with uncertain outcomes ship dark behind feature flags with named owners and expiry dates, and are enabled progressively. Long-lived branches are the alternative you are avoiding.
- **Why it exists:** Flags decouple *deployment* from *release*: code can ship safely and be activated, tuned, or killed independently. Long-lived branches drift, conflict, and batch risk.
- **Evidence:** Industry practice converged across DORA elite performers and progressive-delivery literature `[E-DORA · Verified; Inferred as combined practice]`; Knight Capital's flag *reuse* is the cautionary tale for flag hygiene `[E-KNIGHT · Verified]`.
- **Applies when:** risky or uncertain behaviour changes; phased launches; kill-switch needs (R-25).
- **Risks addressed:** big-bang releases; unreleasable branches; inability to turn off a bad feature without a deploy.
- **Violation looks like:** month-old feature branches; flags with no owner that nobody dares remove (see R-16); "just deploy it, we can roll back" for a data-model change.
- **Enforcement:** flag registry with owner + expiry; CI flags stale flags; flags are config (R-15), never repurposed identifiers (R-16).
- **Automatable:** Partially — flag platforms automate targeting and expiry alerts; the decision to flag is human.
- **Exceptions:** Truly trivial changes; changes that cannot be meaningfully split (then use progressive rollout instead, R-25).

### R-27 — Deploy small, deploy often, keep lead time short
- **Classification:** Strong practice.
- **The rule:** Work ships in small batches on a continuous cadence; lead time from commit to production is measured and kept short (elite: under a day). Release trains and freeze windows are treated as symptoms to cure, not processes to cherish.
- **Why it exists:** Small batches are individually low-risk, easy to review, easy to revert, and fast to get feedback on. The research finds speed and stability rise together — batch size is the lever.
- **Evidence:** DORA — elite: on-demand deploys, <1-day lead time, ~5% change-fail, <1-hour recovery; speed/stability not a tradeoff `[E-DORA · Verified]`; Joel Test's daily builds as the 2000 ancestor `[E-JOEL · Verified]`.
- **Applies when:** all product engineering; cadence scales with team size (daily for small teams is normal).
- **Risks addressed:** release anxiety; batch-risk accumulation; slow feedback loops.
- **Violation looks like:** quarterly releases; "code freeze" months; lead time measured in weeks with nobody alarmed.
- **Automatable:** Substantially — CI/CD pipelines, automated gates, and DORA dashboards.
- **Exceptions:** Regulated or safety-critical domains with mandated release processes (still shrink batches *within* the mandated process); app-store review constraints (batch accordingly, keep internal cadence).

---

## Operate

### R-28 — Instrument the four golden signals before you need them
- **Classification:** Strong practice.
- **The rule:** Every user-facing system emits latency, traffic, errors, and saturation from day one, with dashboards a stranger could read. Logging is structured; key business events are tracked alongside technical signals.
- **Why it exists:** You cannot debug what you cannot see, and incidents never wait for instrumentation to be added. The four signals are the minimum set under which serious problems rarely stay invisible.
- **Evidence:** Google SRE's four golden signals `[E-SRE · Verified]`; Twelve-Factor XI (logs as event streams) `[E-12F · Verified]`; GitLab's incident began with *missing* monitoring for the deleted path `[E-GITLAB · Verified]`.
- **Applies when:** any system with users or dependents; proportionally from the first deploy.
- **Risks addressed:** poor observability (AP-16); blind incident response; "we didn't know until customers told us".
- **Violation looks like:** SSH-and-grep debugging in production; no dashboard for the new service; errors counted only in anecdotes.
- **Enforcement:** service checklist requires golden-signal dashboards before launch (template 14); alerts reference the dashboards.
- **Automatable:** Substantially — instrumentation libraries, auto-dashboards, structured logging standards.
- **Exceptions:** None for user-facing systems. Throwaway prototypes get minimal logging with a note.

### R-29 — Alert on symptoms, page only on what is actionable
- **Classification:** Critical control (for on-call health); Strong practice generally.
- **The rule:** Alerts fire on user-visible symptoms (or their leading indicators), not on every internal anomaly. Pages wake humans only for issues requiring immediate human action; everything else is a ticket. Every alert has a runbook link; alerts without runbooks are bugs.
- **Why it exists:** Alert fatigue is how real pages get ignored; unactionable pages train humans to silence the system. Worse, GitLab's backup-failure emails went to a dead mailbox — an alert nobody receives is the most expensive failure because it looks exactly like a healthy system.
- **Evidence:** Google SRE alerting philosophy (symptom-based, actionable paging) `[E-SRE · Verified]`; GitLab — failure notifications lost to DMARC rejection `[E-GITLAB · Verified]`.
- **Applies when:** any on-call rotation; any automated monitoring.
- **Risks addressed:** alert fatigue; missed real incidents; burnout.
- **Violation looks like:** hundreds of unactionable alerts; pages for CPU at 80%; alerts with no runbook and no owner; the alert path itself never tested.
- **Enforcement:** alert review cadence (add/remove/tune); every new alert ships with a runbook (template 15 references); alert-path synthetics prove delivery.
- **Automatable:** Yes — alert routing, runbook linking, and delivery-path tests are automation.
- **Exceptions:** None. If it pages, it must be actionable — otherwise demote it.

### R-30 — Blameless postmortems for every significant incident
- **Classification:** Strong practice.
- **The rule:** After every significant incident, a written postmortem asks how the *system* allowed the outcome — never who caused it. It records timeline, impact, contributing factors, and action items with owners and dates, and is shared with the wider team.
- **Why it exists:** Blame suppresses the honest reporting that root-cause analysis depends on; people shade the story to protect themselves. The premise that everyone acted reasonably given what they knew corrects for hindsight bias. "Human error" is the start of the investigation, never the conclusion.
- **Evidence:** Allspaw (2012) — blameless postmortems and just culture `[E-ALLSPAW · Verified]`; SRE Ch.15 codifies it `[E-SRE · Verified]`; GitLab's fully public postmortem as the exemplar `[E-GITLAB · Verified]`; Cook (2000) on hindsight bias as the primary obstacle to accident investigation `[Corroborated via E-ALLSPAW sources]`.
- **Applies when:** every significant incident; near-misses worth the learning.
- **Risks addressed:** repeat incidents; hidden systemic causes; fear-driven silence.
- **Violation looks like:** postmortems that name a person as the cause; "engineer will be more careful" as the action item; incidents never written up because "we fixed it".
- **Enforcement:** incident-response template (04-templates/15) ends with the postmortem; action items tracked to closure like any work.
- **Automatable:** No — templates and tracking help; the analysis is human.
- **Exceptions:** None — but depth scales with impact (a one-paragraph note for minor incidents is still a postmortem).

### R-31 — Govern risk-taking with error budgets
- **Classification:** Context-dependent recommendation.
- **The rule:** Define SLOs for user-facing reliability; the error budget (100% − SLO) is the shared allowance for risk. While budget remains, ship features freely; when exhausted, work shifts to reliability until the budget recovers. The policy is agreed in advance, not negotiated mid-incident.
- **Why it exists:** Without a budget, reliability debates are vibes: product wants speed, ops wants caution, and the loudest voice wins. A budget converts the tradeoff into a number both sides agreed to beforehand.
- **Evidence:** Google SRE error budgets `[E-SRE · Verified]`; DORA 2021 added Reliability as an adjacent outcome dimension `[E-DORA · Verified]`.
- **Applies when:** teams with meaningful reliability expectations and a product/ops tension to mediate; services with measurable SLIs.
- **Risks addressed:** reliability death spirals; feature-vs-stability politics; perfectionism (100% is the wrong target — it's wasteful).
- **Violation looks like:** "five nines" as an aspiration with no budget math; freezing all deploys after one incident, then forgetting by next quarter.
- **Enforcement:** SLOs in the service definition; budget-burn alerts; the freeze policy written down before it's needed.
- **Automatable:** Substantially — burn-rate alerting is standard tooling.
- **Exceptions:** Pre-product-market-fit prototypes (no users to promise reliability to); safety-critical systems where the "budget" framing needs regulatory shaping.

### R-32 — Measure AI spend per feature and per user
- **Classification:** Strong practice. **[Proposed as a named rule; evidence Corroborated/Inferred]**
- **The rule:** Token/API/compute cost of AI features is metered per request, attributed per feature and per user cohort, and reviewed against the value those features produce. Unit economics are known before scale, not discovered after.
- **Why it exists:** AI costs are variable, opaque, and scale with usage — the exact shape of cost that bankrupts unit economics silently. Demos ignore token usage, API limits, and scaling cost; products cannot.
- **Evidence:** Practitioner analyses of demo-vs-product AI economics (demos ignore token usage, scaling cost, abuse patterns) `[E-VAPOR · Corroborated]`; Anthropic's explicit latency/cost-vs-performance tradeoff framing `[E-ANTHROPIC · Verified]`; FinOps-for-LLM practice emerging 2024–2026 `[Inferred from industry discourse]`.
- **Applies when:** any product with LLM/API-based AI features in the request path.
- **Risks addressed:** unmeasured AI costs (AP-18); negative unit economics discovered at scale; abuse-driven cost spikes.
- **Violation looks like:** no idea what a power user costs per month; "the API bill went up 10× and we don't know why"; no per-feature cost attribution.
- **Enforcement:** cost dashboards per feature/cohort; cost anomaly alerts; cost included in the launch-readiness checklist (template 18).
- **Automatable:** Yes — metering and attribution are instrumentation work.
- **Exceptions:** Tiny prototypes and internal tools (still meter roughly; the habit matters more than precision).

---

## Improve

### R-33 — Measure delivery performance and review the trend
- **Classification:** Context-dependent recommendation.
- **The rule:** Track the DORA keys (deployment frequency, lead time, change failure rate, recovery time) at team level, review trends on a cadence, and act on the bottleneck — not on individual productivity. Never use these metrics to rank people.
- **Why it exists:** What gets measured gets improved; what gets measured *at the wrong level* gets gamed. Team-level delivery metrics illuminate process bottlenecks (slow CI, painful deploys, flaky gates) that no amount of individual effort fixes.
- **Evidence:** DORA/Accelerate — the metrics predict organisational performance; elite teams excel at all four `[E-DORA · Verified]`; DORA's own guidance: team-level, never individual `[E-DORA · Verified]`.
- **Applies when:** teams shipping regularly; even two-person teams benefit from lead-time and recovery-time awareness.
- **Risks addressed:** invisible process drag; misattributing system problems to people; optimising vanity activity metrics (commits, story points).
- **Violation looks like:** ranking developers by commits or PRs; DORA dashboards nobody looks at; "we feel slow" with no numbers.
- **Enforcement:** lightweight dashboard; quarterly review asking "what's the bottleneck and what changes it?".
- **Automatable:** Yes — metrics pipelines are standard tooling.
- **Exceptions:** Pre-team solo hacking (still useful, just informal); using the metrics punitively is not an exception — it's a violation.

### R-34 — Kill, fix, or keep: every feature earns its place
- **Classification:** Strong practice.
- **The rule:** On a cadence, each significant feature is judged against its pre-committed outcome metric (R-02): keep and invest, fix with a bounded effort, or kill and reclaim the maintenance cost. No feature survives on sentiment.
- **Why it exists:** Every shipped feature is a maintenance liability and a cognitive-load tax forever. Without a kill mechanism, products accrete into unmaintainable bundles of half-used features — the build trap's end state.
- **Evidence:** Perri — culture of outcomes over outputs `[E-BUILDTRAP · Verified]`; Ries — pivot or persevere `[E-LEAN · Corroborated]`; Shape Up's circuit breaker as the kill mechanism `[E-SHAPEUP · Verified]`.
- **Applies when:** any product with more than a handful of features; especially post-launch portfolios.
- **Risks addressed:** unnecessary features (AP-04); maintenance sprawl; the inability to simplify.
- **Violation looks like:** features nobody can name the owner of; "we can't remove it, someone might use it"; settings pages with 40 toggles.
- **Enforcement:** post-launch evaluation (template 16) feeds a kill/fix/keep review; removal gets the same rollout care as launch (R-25).
- **Automatable:** Partially — usage analytics flag candidates; the decision is human.
- **Exceptions:** Regulated/compliance features (kept for legal reasons — the "outcome" is compliance); platform capabilities with indirect value (judged at portfolio level).

---

## Rule index

| ID | Rule | Classification | Phase |
|---|---|---|---|
| R-01 | Ship outcomes, not outputs | Critical control | Discovery |
| R-02 | Define the measurable success metric before the build | Strong practice | Discovery |
| R-03 | Retire the four product risks before committing to build | Strong practice | Discovery |
| R-04 | Write the launch artefact before the design | Company-specific convention | Discovery |
| R-05 | Fix the time, flex the scope | Strong practice | Design |
| R-06 | Record significant decisions where the code lives | Strong practice | Design |
| R-07 | Spend innovation tokens only on what differentiates you | Strong practice | Design |
| R-08 | No speculative generality (YAGNI) | Strong practice | Design |
| R-09 | Threat-model before you build trust boundaries | Release gate | Design |
| R-10 | Design for failure at every integration point | Strong practice | Design |
| R-11 | Everything in version control; mainline always releasable | Critical control | Build |
| R-12 | One-step, reproducible builds; build/release/run separated | Critical control | Build |
| R-13 | No AI-generated code reaches production unverified | Critical control | Build |
| R-14 | Keep changes small, coherent, and reviewable | Strong practice | Build |
| R-15 | Configuration in the environment; secrets never in code | Critical control | Build |
| R-16 | Delete dead code; never repurpose flags or identifiers | Strong practice | Build |
| R-17 | No optimisation without measurement | Strong practice | Build |
| R-18 | Critical paths are tested; releases gate on the tests | Release gate | Test |
| R-19 | Test the thing that actually ships, through the real path | Strong practice | Test |
| R-20 | Every production change gets a second pair of eyes | Release gate | Test |
| R-21 | Least privilege by default, everywhere | Critical control | Secure |
| R-22 | Meet ASVS Level 1 before any internet-facing deploy | Release gate | Secure |
| R-23 | Patch known vulnerabilities promptly; know your dependencies | Release gate | Secure |
| R-24 | Backups exist, are monitored, and restore-tested | Critical control | Secure |
| R-25 | Every release is reversible and rolled out progressively | Release gate | Ship |
| R-26 | Gate risky changes behind flags, not branches | Context-dependent | Ship |
| R-27 | Deploy small, deploy often, keep lead time short | Strong practice | Ship |
| R-28 | Instrument the four golden signals before you need them | Strong practice | Operate |
| R-29 | Alert on symptoms, page only on what is actionable | Critical control | Operate |
| R-30 | Blameless postmortems for every significant incident | Strong practice | Operate |
| R-31 | Govern risk-taking with error budgets | Context-dependent | Operate |
| R-32 | Measure AI spend per feature and per user | Strong practice | Operate |
| R-33 | Measure delivery performance and review the trend | Context-dependent | Improve |
| R-34 | Kill, fix, or keep: every feature earns its place | Strong practice | Improve |

**Counts:** 7 Critical control · 7 Release gate · 15 Strong practice · 4 Context-dependent recommendation · 1 Company-specific convention. Two rules are marked Proposed synthesis (R-16's naming, R-32); all others rest on documented practice with evidence in `05-evidence-register.md`.
