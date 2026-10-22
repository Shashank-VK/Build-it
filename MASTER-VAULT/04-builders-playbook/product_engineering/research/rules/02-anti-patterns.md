# §32 — Anti-Pattern Catalogue

**Workstream:** rules · **Built:** 2026-10-10 · **Read-only:** research only — documented failure modes and their corrections, not adoption advice.

For each anti-pattern: cause, warning signs, impact, evidence (claim labels per `05-evidence-register.md`), corrective action, and a counterexample where the normally-discouraged practice is appropriate.

---

## AP-01 — Weak product validation

- **Cause:** Building from opinion, authority ("the CEO asked"), or solution-love instead of evidence; discovery treated as a phase to skip rather than risks to retire.
- **Warning signs:** no named customer talked to in the last month; the PRD's "evidence" section cites internal meetings; success defined as shipping.
- **Impact:** the most expensive failure mode — a well-built product nobody wants; months of engineering converted into learning that a week of interviews would have provided.
- **Evidence:** Cagan's value-risk framing `[E-CAGAN · Corroborated]`; Perri's build trap — output without outcome `[E-BUILDTRAP · Verified]`; Ries on validated learning `[E-LEAN · Corroborated]`. Violated rule: R-01, R-03.
- **Corrective action:** problem-validation template (04-templates/01) before resourcing; weekly customer contact cadence (Torres); kill criteria defined up front (R-02).
- **Counterexample:** *Appropriate to build on thin validation* when the cost of building is near-zero (a weekend prototype), when the builder *is* the expert user with deep domain immersion, or when validation itself requires the artefact to exist (novel interactions nobody can evaluate hypothetically).

## AP-02 — Scope creep

- **Cause:** fixed-scope commitments with variable time; no explicit no-go list; stakeholders adding "just one more thing" without re-appetising; fear of saying no.
- **Warning signs:** the spec grows but the date doesn't move; "phase 1" quietly absorbs phase 2; rabbit holes nobody named in advance.
- **Impact:** slipped dates, death marches, quality sacrificed to protect scope (testing cut first), team burnout.
- **Evidence:** Shape Up's diagnosis — estimates grow to protect the team; the fix is appetite-first with named no-gos and a circuit breaker `[E-SHAPEUP · Verified]`. Violated rule: R-05.
- **Corrective action:** fixed appetite with pre-authorised no-gos (template 04); any addition forces an explicit subtraction; circuit breaker kills overruns instead of extending them.
- **Counterexample:** *Appropriate to expand scope* when discovery mid-build reveals the shaped problem was wrong and the new scope is *smaller* in time but different in shape (re-shaping, not creep); and in genuinely exploratory R&D where the scope *is* the learning.

## AP-03 — Generic design

- **Cause:** designing from patterns libraries and competitor screenshots instead of from the specific job the user is doing; "best practice" applied without the context that made it best.
- **Warning signs:** the product looks like every other dashboard; users can complete flows but can't explain why they'd choose this over alternatives; design reviews discuss components, never jobs-to-be-done.
- **Impact:** no differentiation; features that are usable but uncompelling; lost to competitors who understood the specific workflow.
- **Evidence:** Practitioner consensus across Cagan/Torres discovery literature — value risk is retired by specificity, not by polish `[E-CAGAN · Corroborated][E-TORRES · Corroborated]`. Violated rule: R-03 (value/usability risks).
- **Corrective action:** design from observed user workflows (prototype acceptance template 07 requires named users and tasks); differentiate on the 1–2 workflows that matter, be boring everywhere else (R-07).
- **Counterexample:** *Appropriate to be generic* for undifferentiated surfaces — settings pages, auth flows, admin tables: here familiarity *is* the usability win, and custom design is vanity.

## AP-04 — Unnecessary features

- **Cause:** roadmap as a wishlist; sales-driven one-offs; "competitor has it" reasoning; no kill mechanism (R-34 never runs); features as a proxy for progress.
- **Warning signs:** features with no owner and no metric; settings pages nobody can navigate; the codebase's most complex code serves the least-used feature.
- **Impact:** permanent maintenance tax; cognitive load on users and developers; slower everything (builds, onboarding, debugging); the product becomes unlearnable.
- **Evidence:** Perri — outputs over outcomes `[E-BUILDTRAP · Verified]`; Brooks's second-system effect — the follow-up system over-designed with every feature anyone ever wanted `[E-BROOKS · Corroborated]`. Violated rules: R-01, R-34.
- **Corrective action:** kill/fix/keep reviews on a cadence; every feature keeps its outcome metric and owner or gets removed; removal ships with rollout care (R-25).
- **Counterexample:** *Appropriate to ship a rarely-used feature* when it's a compliance/legal requirement, a loss-leader for a key account with eyes-open economics, or a platform capability whose value is at portfolio level (judged there, not per-feature).

## AP-05 — Premature abstraction

- **Cause:** designing for imagined futures; confusing "might need" with "needs"; architects rewarded for generality; building the framework before the third use case exists.
- **Warning signs:** abstractions with one implementation; configuration for scenarios never requested; "extension points" nobody extends; simple changes require understanding the framework first.
- **Impact:** the simple case becomes hard; wrong guesses ossify into load-bearing structure; velocity declines as abstraction weight grows.
- **Evidence:** Fowler/XP simplicity discipline `[E-FOWLER · Corroborated]`; Ousterhout — complexity is incremental, deep modules beat speculative generality `[E-OUSTERHOUT · Corroborated]`. Violated rule: R-08.
- **Corrective action:** rule of three (abstract on the third real use, not the first imagined one); keep seams clean so future abstraction is cheap; code review challenges generality without a caller.
- **Counterexample:** *Appropriate to abstract early* when building an actual platform (the abstraction is the product), when the domain pattern is genuinely stable and well-understood (e.g., i18n, multi-tenancy for a SaaS), or when a wrong-but-reversible abstraction is cheaper than three divergent implementations.

## AP-06 — Fragile architecture

- **Cause:** integration points without failure strategies; synchronous chains of dependencies; no bulkheads; shared mutable state across boundaries; "it won't fail" as the design.
- **Warning signs:** one slow vendor degrades everything; deploys require coordinated multi-service choreography; nobody can draw the failure modes; incidents cascade.
- **Impact:** cascading outages; un-deployable systems; every incident becomes a Sev-1; Conway's-law drift — the architecture mirrors org confusion.
- **Evidence:** Nygard — integration points are the #1 stability killer; failures propagate, cracks accelerate `[E-RELEASEIT · Verified]`; Knight Capital/CrowdStrike as cascade case studies `[E-KNIGHT · Verified][E-CROWD · Verified]`. Violated rule: R-10.
- **Corrective action:** per-integration failure strategy (timeout/breaker/bulkhead/degrade) in the design doc (template 04); chaos/load testing of the nasty modes; modular-monolith-first for small teams (Gall's law `[E-GALL · Corroborated]`).
- **Counterexample:** *Appropriate to accept fragility* in a timeboxed prototype you're willing to throw away (Brooks: plan to throw one away `[E-BROOKS · Corroborated]`) — provided the throwaway decision is explicit and the prototype can't reach production unchanged.

## AP-07 — Poor testing

- **Cause:** testing treated as a phase after build; critical paths covered only by manual clicking; flaky suites trained the team to ignore red; "we'll test after launch".
- **Warning signs:** releases routinely surprise; the suite is red so often nobody looks; no test for the exact path that just failed in production; manual regression checklists before every deploy.
- **Impact:** regressions shipped silently; release fear → bigger batches → bigger failures (the DORA death spiral); support load from preventable bugs.
- **Evidence:** CrowdStrike — the missing non-wildcard test for field 21 `[E-CROWD · Verified]`; DORA change-failure-rate as the stability metric `[E-DORA · Verified]`; WHO/Pronovost — verification gates catch what memory misses `[E-GAWANDE · Verified]`. Violated rules: R-18, R-19.
- **Corrective action:** gate releases on critical-path tests; quarantine flaky tests with owners; test production-shaped inputs through real paths (R-19); test plan template (04-templates/10).
- **Counterexample:** *Appropriate to under-test* genuinely throwaway spikes and prototypes — but label them unshippable; and *appropriate to test less* where the cost of failure is trivial and the cost of the test exceeds it (a personal blog's CSS).

## AP-08 — Weak security

- **Cause:** security as a pre-launch checkbox (or never); no threat model; hand-rolled auth/crypto; secrets in code; dependencies unpatched; AI-generated security logic unreviewed.
- **Warning signs:** no ASVS-style requirement list; "we'll do a pentest next quarter" as the whole plan; admin service accounts; keys in repo history; AI-written auth code merged on vibes.
- **Impact:** breaches, the costliest and least forgivable failure class; supply-chain compromise; regulatory exposure; the incident you can't postmortem your way out of reputationally.
- **Evidence:** Pearce (~40% of AI completions vulnerable) `[E-PEARCE · Verified]`; Perry (AI-assisted devs less secure *and* more confident) `[E-PERRY · Verified]`; Log4Shell `[E-LOG4J · Corroborated]`; ASVS as the standard of care `[E-ASVS · Verified]`. Violated rules: R-09, R-21, R-22, R-23.
- **Corrective action:** threat model at design (R-09); ASVS L1 gate before internet-facing launch (R-22); secrets scanning, SCA, patch SLAs; independent review of AI-generated security code (R-13, R-20).
- **Counterexample:** *Appropriate to defer hardening* only for truly local, single-user, offline prototypes — with a written "not shippable" marker and a date; never for anything networked.

## AP-09 — AI-generated code without verification

- **Cause:** "Accept All" workflows; treating the model as an oracle; velocity pressure; the confidence inflation Perry et al. measured — the less you check, the safer it feels.
- **Warning signs:** PRs the author can't explain; diffs merged without reading; AI-suggested packages installed unchecked; security-sensitive code (auth, crypto, SQL) generated and merged same-day.
- **Impact:** vulnerable code at machine speed; supply-chain injection via hallucinated packages; confident-but-wrong logic in exactly the places (auth, crypto, injection) where wrongness is catastrophic.
- **Evidence:** Pearce et al. `[E-PEARCE · Verified]`; Perry et al. — the confidence finding is the mechanism `[E-PERRY · Verified]`; Snyk survey 56.4% `[E-SNYK · Corroborated]`; slopsquatting `[E-LANYADO · Corroborated]`; Karpathy's throwaway-only scope and Willison's review boundary `[E-KARPATHY · Verified]`. Violated rules: R-13, R-20.
- **Corrective action:** review/test/explain standard for all AI-assisted code; SAST+SCA+secrets on every PR; verify dependency names against registries; agent instructions (template 09) cap autonomy and require verification steps.
- **Counterexample:** *Appropriate to skip verification* for Karpathy's original scope — throwaway weekend projects with no users, no secrets, no network trust — and for trivially reviewable boilerplate where the "review" is a glance at a 5-line diff (cheap, not skipped).

## AP-10 — Uncontrolled agents

- **Cause:** giving agents broad tool access "to see what they can do"; no permission boundaries; no human checkpoints on consequential actions; confusing a demo of autonomy with production readiness.
- **Warning signs:** an agent with production write access; no log of what the agent did; destructive actions (deletes, migrations, deploys) available without confirmation; "the agent did something unexpected" as a recurring incident class.
- **Impact:** the blast radius of a bug becomes the blast radius of the agent's permissions; un-auditable changes; incidents nobody can reconstruct.
- **Evidence:** Anthropic — agents need well-designed tools, sandbox testing, guardrails, human checkpoints; start with the simplest pattern `[E-ANTHROPIC · Verified]`; least-privilege as the control `[E-NIST · Corroborated]`; Knight Capital as the parable of automation without a kill switch `[E-KNIGHT · Verified]`. Violated rules: R-13, R-21.
- **Corrective action:** tool manifests with least privilege; human approval for consequential actions; full action logging; sandbox-first testing; workflows (deterministic) preferred over agents (autonomous) where the path is known (Anthropic's taxonomy).
- **Counterexample:** *Appropriate to grant broad autonomy* in sandboxed, consequence-free environments (research, simulation, games) and in read-only investigation agents whose worst case is a wrong answer — the control scales with consequence.

---

## AP-11 — Excessive automation

- **Cause:** automating before understanding; "automate everything" as ideology; automating a broken process (which just produces wrongness faster); automation nobody monitors.
- **Warning signs:** pipelines nobody understands end-to-end; automation that pages humans at 3 a.m. for things it should handle or shouldn't have done; toil *increased* by maintaining the automation.
- **Impact:** amplified failures (Knight Capital's automation executed 4M bad trades in 45 minutes); unmaintainable Rube Goldberg pipelines; learned helplessness — nobody knows how the system works anymore.
- **Evidence:** Knight Capital — automation without circuit breakers `[E-KNIGHT · Verified]`; SRE's toil discipline — automate *toil* (manual, repetitive, automatable, tactical, no enduring value), not judgment `[E-SRE · Verified]`; Knuth on unmeasured optimisation `[E-KNUTH · Corroborated]`. Violated rules: R-17, R-29.
- **Corrective action:** automate toil first (SRE definition); keep humans in the loop for judgment calls; every automation gets monitoring, a kill switch, and an owner; measure before automating (R-17).
- **Counterexample:** *Appropriate to over-automate deliberately* in safety interlocks (the automation *is* the safety system, e.g., automatic train brakes) and in high-frequency domains where human reaction time is the bottleneck — there the automation gets the engineering rigour of a safety system, not a script.

## AP-12 — Broken interactions

- **Cause:** designing screens instead of flows; happy-path-only thinking; no error/empty/loading states designed; frontend and backend developed against different assumptions.
- **Warning signs:** buttons that do nothing on failure; forms that lose input on error; flows that dead-end; "it works if you do it in the right order".
- **Impact:** user trust erosion; support tickets for things that "should just work"; the product feels broken even when the backend is fine.
- **Evidence:** Practitioner consensus in UX engineering (Cagan usability risk `[E-CAGAN · Corroborated]`); volanea validation guidance — show real input, concrete output, the decision it improves `[E-PROTOTYPE-WOZ · Corroborated]`. Violated rules: R-03 (usability risk), R-19.
- **Corrective action:** design flows end-to-end including failure branches; contract between frontend/backend (types, error shapes); interaction testing beyond the happy path; UX states checklist (template 17).
- **Counterexample:** *Appropriate to leave interactions rough* in Wizard-of-Oz prototypes and concierge MVPs — the human behind the curtain *is* the interaction design, provided it's disclosed in research contexts `[E-PROTOTYPE-WOZ · Corroborated]`.

## AP-13 — Incomplete responsive behaviour

- **Cause:** designing desktop-first and "checking mobile later"; testing only at the designer's viewport; breakpoints as an afterthought.
- **Warning signs:** horizontal scroll on phones; tap targets that need a stylus; tables that explode; "just use the desktop site" as the mobile strategy.
- **Impact:** for most products, the majority experience is broken; accessibility and SEO damage; lost users who never complain, just leave.
- **Evidence:** Industry-wide practitioner consensus; responsive design as baseline since ~2010s (Ethan Marcotte, *Responsive Web Design*, 2011) `[Corroborated]`; product-authenticity checklist treats responsive as launch-blocking (template 17). Violated rule: R-03 (usability risk).
- **Corrective action:** design mobile-first or at least mobile-concurrently; test on real devices at real viewports; responsive checks in visual QA (template 12) and launch readiness (template 18).
- **Counterexample:** *Appropriate to defer* for internal tools used exclusively on desktops (documented, not assumed), and for early prototypes validating a desktop-only workflow — with responsive on the explicit roadmap before public launch.

## AP-14 — Misleading product demos

- **Cause:** demo-driven development — optimising for the applause of the demo rather than the reality of production; undisclosed fakery; confusing investor/customer demos with validation.
- **Warning signs:** the demo never touches real data; "we'll figure out scale/security/cost later"; different code path for demo vs product; capabilities shown that don't exist, undisclosed.
- **Impact:** vaporware dynamics — funding and commitments secured against fiction; the Ovation end-state (fake demo → bankruptcy) or the Magic Leap end-state (years behind, trust burned); AI-era procurement failures when "trust us, just deploy" replaces pilots.
- **Evidence:** Ovation (1983, NYT: demo was fake) and Magic Leap (2016, The Information via The Verge: deceptive demos alleged, contested) `[E-VAPOR · Corroborated]`; 2026 analyst guidance — demand production testing, not demos; demos hide governance/security/cost gaps `[E-VAPOR · Corroborated]`; the demo-vs-product AI gap (no guardrails, no cost accounting in demos) `[E-VAPOR · Corroborated]`. Violated rules: R-02, R-04.
- **Corrective action:** disclose what's real (prototype acceptance template 07 requires it); demo on production-shaped data; separate *validation* demos (explicitly fake, disclosed) from *commitment* demos (real capabilities only).
- **Counterexample:** *Appropriate to fake* in Wizard-of-Oz research and concept validation — undisclosed fakery in *research* is fraud, but *disclosed* simulation is a legitimate, textbook method `[E-PROTOTYPE-WOZ · Corroborated]`; and in pure vision pieces labelled as vision.

## AP-15 — Missing UX states

- **Cause:** designing only the happy path; states treated as edge cases; "we'll handle errors later" (later never comes).
- **Warning signs:** blank screens during loads; silent failures; no empty states ("no results" shows nothing); destructive actions without confirmation; errors in console only.
- **Impact:** users can't tell what happened or what to do next; support load; the product feels unfinished regardless of feature count.
- **Evidence:** Practitioner UX consensus; the product-authenticity checklist (template 17) enumerates the states as launch-blocking `[SYN · Proposed structure, Corroborated content]`. Violated rules: R-03, R-19.
- **Corrective action:** the UX-states inventory (loading, empty, error, offline, permission-denied, rate-limited, destructive-confirm, success) designed per flow from the start; visual QA template (12) checks each.
- **Counterexample:** *Appropriate to omit* only where the state is genuinely impossible (a local, synchronous, infallible operation) — and "impossible" should survive five minutes of adversarial review; prototypes may stub states but must list them as debt.

## AP-16 — Poor observability

- **Cause:** instrumentation deferred to "after launch"; logs as printf archaeology; metrics nobody defined; monitoring confused with alerting.
- **Warning signs:** incidents discovered by customers; debugging via SSH and grep; dashboards that nobody trusts; "we don't know" as the first incident update.
- **Impact:** slow detection, slower diagnosis; incidents that could be minutes become hours; no data for improvement (R-33 starves).
- **Evidence:** SRE four golden signals `[E-SRE · Verified]`; GitLab's missing filesystem monitoring at the incident's start `[E-GITLAB · Verified]`; Twelve-Factor XI `[E-12F · Verified]`. Violated rules: R-28, R-29.
- **Corrective action:** golden signals from day one; structured logs; dashboards before launch (template 14); alert on symptoms with runbooks.
- **Counterexample:** *Appropriate to stay lean* for throwaway prototypes (minimal logging, noted as debt) — but anything with a second user or a dependency gets the four signals; the cost is tiny, the regret is large.

## AP-17 — Unnecessary infrastructure

- **Cause:** resume-driven architecture; confusing "web-scale" with "our scale"; premature distribution; innovation tokens spent on plumbing instead of product.
- **Warning signs:** Kubernetes for a CRUD app; microservices with one team; Kafka before the second consumer; infrastructure the team can't debug at 3 a.m.
- **Impact:** operational load swamps product work; hiring constrained to exotic-skill unicorns; every change pays the distributed-systems tax for no benefit.
- **Evidence:** McKinley's boring-technology doctrine `[E-BORING · Corroborated]`; Gall's law — evolve from working simple systems `[E-GALL · Corroborated]`; Conway/Team Topologies — cognitive load as the binding constraint `[E-CONWAY · Corroborated]`. Violated rule: R-07.
- **Corrective action:** boring defaults (managed Postgres, monolith-first, PaaS); ADR for every infrastructure choice naming the innovation tokens spent (R-06); scale the architecture when measurement demands it (R-17).
- **Counterexample:** *Appropriate to build heavy early* when the product *is* infrastructure, when load is contractually guaranteed from day one (a migration with known traffic), or when regulatory/data-residency requirements genuinely demand topology upfront.

## AP-18 — Unmeasured AI costs

- **Cause:** AI features priced by vibes; no per-request metering; demo economics mistaken for production economics; abuse and power-user patterns unmodelled.
- **Warning signs:** nobody knows the cost per user; the API bill surprises monthly; no cost anomaly alerts; "we'll optimise prompts later".
- **Impact:** negative unit economics discovered at scale; margin collapse on success (the more users, the more you lose); abuse-driven bill spikes.
- **Evidence:** Demo-vs-product AI economics analyses `[E-VAPOR · Corroborated]`; Anthropic's cost/latency tradeoff framing `[E-ANTHROPIC · Verified]`. Violated rule: R-32 **[Proposed]**.
- **Corrective action:** meter per request, attribute per feature/cohort (R-32); cost in the launch checklist (template 18); caps and anomaly alerts; design for the expensive tail (caching, smaller models for easy cases — Anthropic's workflow patterns).
- **Counterexample:** *Appropriate to run unmeasured* during tiny prototypes and internal tools — with rough metering even there, because the habit is the point and the cost of metering is near-zero.

## AP-19 — Poor adoption / commercial viability

- **Cause:** building without a distribution path; ignoring willingness-to-pay evidence; confusing signups with customers; unit economics as an afterthought; "if we build it they will come".
- **Warning signs:** launches with no launch plan; free users who never convert; CAC unknown; pricing decided by gut; the viability risk (Cagan's fourth) never retired.
- **Impact:** the build trap's terminal stage — a working product with no business; runway burned on engineering that distribution can't monetise.
- **Evidence:** Cagan's viability risk `[E-CAGAN · Corroborated]`; Perri — strategy connecting vision to economic outcomes `[E-BUILDTRAP · Verified]`; Ries — vanity vs actionable metrics `[E-LEAN · Corroborated]`; TechTarget 2026 — ROI defined before procurement, not discovered after `[E-VAPOR · Corroborated]`. Violated rules: R-01, R-02, R-03.
- **Corrective action:** viability evidence in idea evaluation (template 02); pricing/willingness-to-pay tested before build; actionable metrics only; kill criteria honoured (R-34).
- **Counterexample:** *Appropriate to defer monetisation* for deliberately loss-led strategies with eyes-open economics and a funded runway (a documented bet, not a hope); and for open-source / public-goods work where adoption *is* the outcome.

---

## Anti-pattern index

| ID | Anti-pattern | Primary violated rule(s) |
|---|---|---|
| AP-01 | Weak product validation | R-01, R-03 |
| AP-02 | Scope creep | R-05 |
| AP-03 | Generic design | R-03 |
| AP-04 | Unnecessary features | R-01, R-34 |
| AP-05 | Premature abstraction | R-08 |
| AP-06 | Fragile architecture | R-10 |
| AP-07 | Poor testing | R-18, R-19 |
| AP-08 | Weak security | R-09, R-21, R-22, R-23 |
| AP-09 | AI-generated code without verification | R-13, R-20 |
| AP-10 | Uncontrolled agents | R-13, R-21 |
| AP-11 | Excessive automation | R-17, R-29 |
| AP-12 | Broken interactions | R-03, R-19 |
| AP-13 | Incomplete responsive behaviour | R-03 |
| AP-14 | Misleading product demos | R-02, R-04 |
| AP-15 | Missing UX states | R-03, R-19 |
| AP-16 | Poor observability | R-28, R-29 |
| AP-17 | Unnecessary infrastructure | R-07 |
| AP-18 | Unmeasured AI costs | R-32 |
| AP-19 | Poor adoption / commercial viability | R-01, R-02, R-03 |

Every anti-pattern above carries at least one counterexample: the catalogue is a set of defaults with named escape hatches, not a list of prohibitions.
