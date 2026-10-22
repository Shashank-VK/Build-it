# §11 — Implementation & Code Quality

**Workstream:** build-ship · **Researched:** 2026-10-10 · **Scope:** work decomposition, incremental implementation, dependency management, contract preservation, change review, tech-debt prevention. Task sizing, API contracts, error handling, refactoring, data migrations, feature flags, backward compatibility, documentation. Read-only research: discover, inspect, verify, categorize, explain usage, record sources. Nothing installed, built, configured, ranked, or recommended.

**How to read the labels:** every major claim carries one of **Verified** (directly from a primary source: official docs, published paper, official postmortem), **Corroborated** (multiple independent sources agree), **Inferred** (reasoned from evidence, not directly stated), **Proposed** (a specific practitioner's prescription, single-sourced), **Unknown** (not established by the evidence gathered). Evidence class is noted per finding: primary technical / first-hand practitioner / corroborating / community observation / secondary interpretation / unverified.

---

## 1. Work decomposition & task sizing

**Plain English:** big pieces of work are split into small, independently shippable pieces so each piece can be reviewed, tested, and (if broken) reverted without dragging the rest along.

**Concrete example:** Google's engineering practices tell authors to keep a single change (a "changelist") small — about 100 lines is usually reasonable, 1,000 is usually too large — and to make one self-contained change that does one thing, with its tests.

**Deeper mechanics:** small changes shrink the reviewer's cognitive load (fewer contexts to hold), make `git bisect` pinpoint the breaking commit faster, lower merge-conflict probability, and make rollback surgical. Google's internal review guidance lets reviewers *reject* oversized changes as too large for a single review — a **Verified** practice from the dayuanjiang/software-engineering-at-google mirror of the book's Chapter 9 (primary technical source: Google's eng-practices). A recurring industry observation, repeated across independent practitioner docs, is that review thoroughness collapses past roughly 200–400 lines; one skill doc cites a Google internal study finding significantly less thorough review of CLs over ~400 lines vs under ~200 (**Corroborated** as practitioner consensus; the underlying internal study is **secondary interpretation** — the number is widely repeated but the primary study is not publicly inspectable).

**Task sizing ↔ delivery performance:** the DORA research program (2014–2017, published in *Accelerate* by Forsgren, Humble, Kim) found trunk-based development with branches living under a day and integration periods under a day predicted higher software delivery performance, holding across team size, organization size, and industry (**Verified** from the DORA research summaries; exact published multipliers like "182x deployment frequency" appear in a community skill mirror — treat specific multipliers as **Corroborated-but-caution**: a 2026 research sweep (cwejman/openlight) notes every DORA figure is a cross-sectional, self-reported, correlational estimate, and by 2025 DORA explicitly declines to call them "effects"). The mechanism is **Inferred** but well-supported: long-lived branches discourage refactoring and intra-team communication, while small batches keep integration debt near zero. Formal change-approval boards were found *negatively* associated with performance — an uncomfortable, well-replicated finding (**Corroborated**).

**Prevent:** oversized changes. Reviewers faced with 800-line diffs switch to "approval mode" — they check the overall approach but miss individual bugs (**Corroborated** practitioner observation across Google eng-practices-derived docs).

---

## 2. Incremental implementation (trunk-based development & small batches)

**Plain English:** instead of building a whole feature on a long-lived branch and merging at the end, engineers integrate tiny slices into the main branch daily, hiding unfinished work behind flags.

**Concrete example:** a team ships a checkout rewrite as 12 trunk commits over two weeks — schema addition, read path, write path, flag-gated UI, flag removal — each independently deployable.

**Deeper mechanics:** DORA/Accelerate identifies trunk-based development (<3 active branches, branches living <1 day, no code-freeze periods) as a driver of continuous integration; CI only works when a fast, reliable automated test suite backs it, otherwise CI degenerates into "continuous compilation" (**Corroborated** across DORA summaries and practitioner docs). Feature flags replace long-lived branches as the mechanism for hiding unfinished work (**Corroborated**). Decoupling *deployment* (code reaches production) from *release* (users see it) is the key property flags buy.

**Prevent:** fragile abstractions built in one giant speculative commit; integration-day merge conflicts.

**Limitation / negative evidence:** trunk-based development demands discipline (flag hygiene, test coverage) and is genuinely harder for major features — Google's own book acknowledges engineers who dislike the small-change preference and documents heavier-weight techniques (integration branches, alternate diff bases) for the exceptions (**Verified** from the Google book mirror). Trunk-based flow is a poor fit for part-time open-source contributors (GitHub Flow suits them better) (**Corroborated**).

---

## 3. Dependency management

**Plain English:** nearly all modern software is assembled from other people's packages; managing them means deciding exactly which versions you run, knowing the full transitive tree, and being able to answer "which of my builds contain this vulnerable component?" on the day a vulnerability drops.

**Concrete practices (Corroborated across practitioner sources):**
- **Commit the lockfile** (`package-lock.json`, `poetry.lock`, `Cargo.lock`) and install from it in CI (`npm ci` fails on lockfile/package.json mismatch instead of resolving a new tree).
- **Know the transitive tree** (`npm ls <pkg>` shows every path a package reaches you; most dependencies were never directly chosen).
- **Generate an SBOM at build time** (CycloneDX/SPDX) so a Log4Shell-class event becomes a database query ("which builds contain this PURL?") instead of a repo-by-repo re-scan.
- **Automated dependency scanning on every PR** covering the full transitive tree, with exploitability-first triage (CVSS 10 + near-1.0 EPSS + CISA KEV = drop everything).
- **Curated artifact proxies / allow-lists** for high-risk ecosystems.

**Incident record (the negative evidence that shaped the practices):**

| Incident | Year | What happened | Engineering implication |
|---|---|---|---|
| left-pad | 2016 | Author unpublished an 11-line npm package; thousands of builds broke. npm restored it in ~2.5h and changed unpublish rules | Commit lockfiles; vendor trivial deps; "if a function is eleven lines, write it yourself" (community observation + dev.to postmortem verdict) |
| event-stream | 2018 | Maintainer handover to "right9ctrl"; malicious `flatmap-stream` dep targeted the Copay wallet build; payload only fired in that build context | Watch maintainer changes on popular packages; require approval for new transitive deps (first-hand: npm post-mortem, Snyk write-up) |
| SolarWinds SUNBURST | 2020 | Build-system compromise injected a backdoor into signed Orion updates; ~18,000 orgs installed it | Signed artifacts don't prove supply-chain integrity; build provenance (SLSA-style) matters |
| Log4Shell | 2021 | JNDI lookup feature in Log4j became a CVSS-10 internet-scale exploit; patching was easy, *finding* every deployment was the hard part | SBOMs + emergency-override pipelines that can force upgrades across services in hours |
| PyTorch / torchtriton | 2022 | Dependency confusion: pip resolved a public PyPI package over an internal one; exfiltrated env vars/SSH keys from dev machines | Private registries must shadow public names; verify resolution order |
| XZ Utils | 2024 | "Jia Tan" spent ~2 years earning maintainer trust, then inserted a backdoor into the build system targeting sshd; caught by a Microsoft engineer noticing odd CPU usage | Treat new maintainers and sudden code spikes as risk events; backdoors can hide in test-looking files; deliberate compromise is now in the threat model, not just accidental bugs |

Labels: incident facts **Verified** from multiple reporting sources (first-hand practitioner write-ups, GitHub security advisories, registry postmortems); the prescriptive practices are **Corroborated** practitioner consensus.

**Cost of getting it wrong:** every added dependency expands the attack surface, "even when we do not notice it" (**Corroborated**; telefonicatech practitioner piece).

---

## 4. Contract preservation: API versioning, backward compatibility, expand–contract

**Plain English:** a contract is the promise your code makes to its callers — endpoints, field shapes, error semantics. Preserving it means old clients keep working while new capabilities are added.

**The vocabulary (Corroborated across practitioner docs):**
- **Semantic versioning:** major = breaking, minor = backward-compatible additions, patch = compatible fixes.
- **Breaking:** removing fields/endpoints, changing field types, altering error semantics. **Non-breaking:** adding optional fields/endpoints, adding enum values (if readers tolerate unknown ones).
- **Tolerant reader:** consumers ignore fields they don't recognize — the consumer-side half of the deal.
- **Sunset/Deprecation headers + grace periods + migration guides** for retiring versions.
- **Contract tests** replaying golden client payloads against the new version (see §12 file for Pact).

**Expand–migrate–contract (the universal safe-change shape):**
1. **Expand** — add the new column/table/endpoint alongside the old, nullable/optional; nothing depends on it yet; old paths keep working unchanged; deploy and verify stability first.
2. **Migrate** — dual-write (old stays source of truth; writes to the new side must be idempotent and must not fail the request if the new side fails), backfill in resumable rate-limited batches with reconciliation (counts and checksums), shadow-read (read both, return old, log diffs until diff rate ≈ 0), then switch reads behind a flag per-tenant or per-percentage with an instant kill switch back.
3. **Contract** — remove the old side only after the new side is authoritative and reversibility is no longer needed.

(**Corroborated** across multiple practitioner skills/docs; the phase detail above is drawn from a 2026 migration skill doc — first-hand practitioner formulation.)

**Subtle failure mode (Corroborated, mobile-API piece):** when both request formats can mutate the same resource, the backend must apply identical authorization, validation, idempotency, and concurrency rules to both — supporting two representations must not create two inconsistent business paths. Retries from old and new paths must converge on the same server-side operation, or a timeout during migration creates duplicate mutations even though each API version looks correct in isolation.

**Prevent:** silent failures from contract drift — e.g., Apiiro's report of an AI-generated PR changing an auth header across services where a downstream service wasn't updated, producing a silent authentication failure (**Corroborated** via tech press first-hand reporting of the Apiiro study).

---

## 5. Change review (code review)

**Google's published doctrine (Verified** from google.github.io/eng-practices and the *Software Engineering at Google* book mirror):
- **Standard:** a change ships when it *definitely improves the overall code health of the system, even if it isn't perfect*. Demanding perfection blocks progress and teaches authors to batch unreviewable lumps; rubber-stamping lets health decay one approval at a time.
- **Review order:** design first (is this change a good idea, does it belong here), then functionality, then complexity (can a future maintainer understand it — flag over-engineering now), then tests (real ones, that would fail), and only then naming, comments, style — with mechanical style delegated to linters/formatters so humans never argue about tabs.
- **Speed:** reviewers respond within one business day; automated checks (lint, format, test) run before human review begins — "humans never review what machines can check."
- **Author's half:** small changes, one concern per change, refactors never mixed with behavior changes, description states the *why* (problem, approach, known shortcomings, bug numbers — not "Fix bug" or "Phase 1").

**Anti-patterns (Corroborated** across practitioner docs):
- **Rubber-stamping:** approving without substantive review (time pressure, trust, fatigue). Counter: explicit norms, e.g., every approval names a specific observation.
- **Nitpicking:** commenting on trivia while missing correctness/design. Counter: delegate style to formatters.
- **LGTM-without-reading:** the most dangerous; Google treats it as culturally unacceptable.
- **Mixed refactor + behavior change:** makes review and bisection unreliable; split them.

**AI-generated code and review (2024–2026 evidence):** the critical new fact is that AI output *looks* reviewable but shifts the defect profile. Veracode's Spring 2026 benchmark across 150+ LLMs: security pass rate holds flat at ~55% — roughly 45% of AI-generated code introduces an OWASP Top 10 vulnerability with no security guidance; syntax correctness climbed from ~50% to ~95% while security pass rates didn't move; Java worst (29%), Python best (62%) (**Verified** as reported in OWASP AISVS Appendix C, which itself synthesizes vendor benchmarks — the underlying Veracode report is vendor-published, so treat numbers as **Corroborated** vendor research, not independent). Apiiro's Fortune-50 study (Sept 2025): AI-assisted developers ship 3–4× more commits but introduce security findings at ~10× the rate; by June 2025, 10,000+ new AI-attributed findings/month; privilege-escalation paths +322%, architectural design flaws +153%; AI PRs are larger and touch more services, diluting reviewer attention (**Corroborated** across TechRadar/theregister first-hand reporting of the Apiiro study). CodeRabbit's 470-PR study: AI-coauthored PRs average ~1.7× more issues; logic/correctness +75%; readability issues 3×; performance inefficiencies (excessive I/O) ~8× (**Corroborated** via trade-press reporting; vendor study — direction of effect consistent with Apiiro and the arXiv large-scale study below). Cotroneo et al. (arXiv 2508.21634, Aug 2025): AI code is simpler and more repetitive yet more prone to unused constructs and hardcoded debugging; humans' code shows greater structural complexity and more maintainability issues; AI code contains more high-risk security vulnerabilities (**Verified** from the paper's abstract).

**Distinguish code generation from verified implementation:** the evidence converges on one distinction — generation is cheap, verification is the work. DORA's 2025 findings (via Medium synthesis): a 25% increase in AI adoption is associated with *worse* delivery throughput (−1.5%) and stability (−7.2%); the hypothesis is that faster generation encourages larger batch sizes, violating the small-batch discipline DORA has always prescribed — the "vacuum hypothesis" (**Corroborated** via secondary synthesis of the DORA report; the underlying report is primary). Practitioner consensus: layered defenses — compilation, static analysis, AI reviewers, automated tests, human review for architecture and business intent — because no single layer catches more than ~75% of defects (**Corroborated**).

**Prevent:** oversized AI-generated PRs ("fixing the typos but creating the timebombs"); review dilution; assuming generated code + generated tests = verified (see mutation-testing evidence in the §12 file).

---

## 6. Feature flags

**Plain English:** a runtime `if` that decides which code path executes, changeable without redeploying. They decouple *deployment* (code is live) from *release* (users see it) and provide kill switches.

**The four kinds (Pete Hodgson's widely used taxonomy — Corroborated):** release flags (hide unfinished work; days–weeks, then delete), experiment flags (A/B variants; live for the experiment), ops flags/kill switches (long-lived, owned by operations), permission flags (per-plan/customer; permanent product configuration). The rules differ by kind: a release flag lingering six months later is debt; a kill switch removed because it was quiet last quarter is a future outage.

**Practices (Corroborated):** progressive rollout (internal → 1% → 10/25/50 → 100% with metric monitoring at each step); safe defaults when the flag service is unreachable (a network partition once defaulted a half-finished feature to *true* — practitioner anecdote); test the toggle logic itself, not just the feature (bugs hide in the branch-selection code); audit logging of who flipped what; cleanup with expiration dates — one team enforced build failures after a flag's expiry date passed (**Proposed** by practitioner docs, sensible, single-sourced enforcement mechanisms vary).

**Negative evidence:**
- **Knight Capital, Aug 2012 (Verified):** new code deployed to 7 of 8 servers; the 8th ran retired logic, and a *repurposed* flag reactivated it. ~$400M+ lost in ~45 minutes; the firm never recovered independently. Lessons: never recycle a flag for a new meaning; delete dead code when a flag retires.
- **Google Cloud, June 2025 (Corroborated** via postmortem synthesis): a new code path in a core control system had *no* feature flag protecting it, so bad data crashed it everywhere at once (see §13 file for the full incident).
- **CrowdStrike, July 2024 (Verified):** a faulty content update went to all ~8.5M affected Windows machines at once; afterwards the company committed to staged, canary-style rollouts.
- **Flag graveyards:** the recurring failure is flags with no death date — one account describes a 340-flag graveyard where nobody could distinguish live config from dead code (**community observation**, repeatedly echoed). The fix is decided at creation: label temporary vs permanent, set the death trigger (e.g., "removed at 100% rollout"), owner the permanent ones.

---

## 7. Refactoring & tech-debt prevention

**Origin (Verified):** Ward Cunningham's 1992 metaphor — "shipping first-time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite… every minute spent on not-quite-right code counts as interest." Lehman's law (1980) is the older architectural form: complexity grows unless work is done to reduce it.

**Causes (Corroborated** across Wikipedia's survey of the literature and practitioner docs): deadline pressure, last-minute spec changes, knowledge gaps, deferred refactoring, non-compliance with standards (tight coupling, missing tests), outdated technology, siloed communication.

**Prevention practices (Corroborated/Proposed):**
- Separate refactoring from behavior changes in review (Google doctrine).
- "Leave the code better than you found it" for friction-level debt during feature work (the "refactoring tax" — e.g., budget ~10% extra per feature for cleanup).
- Reserve a standing slice of sprint capacity for hygiene.
- Prioritize by interest × risk: toxic debt (crashes, security holes, revenue-path code) gets paid immediately; friction debt iteratively; dormant debt (ugly code nobody touches) is ignored — **Proposed** framework (wearenotch), single-sourced but consistent with practitioner consensus.
- Track debt as a portfolio with business-risk framing, not as engineering complaints.

**Quantified signals:** a 2024 SonarSource analysis of 12,000 open-source repos found repos with >40% duplication and <15% coverage had 3.7× higher incident rates during deployments (**Corroborated** via secondary reporting; vendor analysis — direction plausible, exact figure vendor-sourced).

**The AI-era twist (Inferred from Apiiro/CodeRabbit evidence):** AI-assisted development accelerates debt *accumulation* (larger, multi-file changes touching more services) faster than remediation capacity grows — CSA's April 2026 note frames it as "security debt accumulating faster than remediation capacity" (**Corroborated** via OWASP AISVS synthesis). Review bandwidth is the scarce resource; generation speed is not the constraint.

---

## 8. Error handling & documentation

- **Error handling:** the recurring defect class is the *silent* failure — the auth-header change that produced silent authentication failure; the migration retry that created duplicate mutations; the flag fetch that silently invented a default during a network partition. The engineering implication (**Inferred**, strongly supported): every error path needs a decided, observable behavior (fail closed with logging and alerting, never silently proceed), and error paths need tests, not just happy paths (mutation testing consistently exposes untested error branches — see §12).
- **Documentation:** decision records (why a flag exists, its kind, its death date), migration guides per API version, runbooks with exact rollback commands (Google SRE: "rollback early, rollback often"). Docs that don't match code are documentation debt with medium interest. DORA's 2025 synthesis notes documentation quality *improved* (+7.5%) with AI adoption — one of the few unambiguous AI wins (**Corroborated** via secondary synthesis).

---

## Key sources consulted (full register in 05-evidence-register.md)

Google eng-practices & *Software Engineering at Google* (Ch. 9 code review, Ch. 11 testing overview); DORA/*Accelerate* research and 2025 report syntheses; Pete Hodgson flag taxonomy; Knight Capital (2012); CrowdStrike (Jul 2024); Google Cloud (Jun 2025); OWASP AISVS Appendix C (Veracode Spring 2026, Apiiro Sep 2025, CSA Apr 2026); CodeRabbit 470-PR study; Cotroneo et al. arXiv 2508.21634; expand–migrate–contract (practitioner skill docs); supply-chain incidents (left-pad, event-stream, SolarWinds, Log4Shell, PyTorch, XZ); Cloudflare Flagship flag best-practices.

## Honest gaps

- The Google internal CL-size study (review thoroughness vs diff size) is widely cited but not publicly inspectable — numbers treated as practitioner consensus, not primary fact.
- Exact DORA multipliers circulate in secondary mirrors; DORA itself now declines causal language — reported as correlational.
- Vendor benchmarks (Veracode, Apiiro, CodeRabbit, SonarSource) are vendor-published; directions of effect are cross-corroborated, exact figures are not independently replicated.
- No controlled study found quantifying the "refactoring tax" percentage — it's a Proposed practice, not a measured one.
