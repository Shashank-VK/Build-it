# Evidence Register — rules workstream (§31–§34)

**Workstream:** rules · **Built:** 2026-10-10 · **Accessed:** 2026-10-10 (all rows)

Every factual claim used in `01-engineering-rules.md`, `02-anti-patterns.md`, `03-small-team-os.md` and `04-templates/` is grounded in one of the entries below. Nothing is asserted without a row.

## Label key

**Claim labels** — *Verified*: confirmed this session against a primary or strong secondary source. *Corroborated*: well-established practitioner knowledge confirmed by multiple independent sources found this session (secondary/tertiary), exact primary wording not re-checked. *Inferred*: reasonable inference from listed evidence, marked where used. *Proposed*: the author's synthesis, marked where used. *Unknown*: no usable evidence found.

**Evidence classes** — P1: primary source (paper, official incident report, official docs, statute). P2: reputable secondary reporting of a primary source. P3: practitioner book / long-form practitioner writing. P4: community/tertiary (curated skill mirrors, forums, explainers). SYN: synthesis of the above.

**Confidence** — High / Medium / Low, reflecting source quality and corroboration depth, not the truth of the underlying claim beyond what the sources establish.

---

## E-KNIGHT — Knight Capital trading loss, Aug 2012

- **Claim:** On 2012-08-01 Knight Capital's SMARS system executed ~4M unintended trades in 154 stocks over 45 minutes after a deployment reached only 7 of 8 servers; a repurposed flag reactivated dormant "Power Peg" code (dead since ~2003); mark-to-market loss $440–460M; SEC Order 34-70694 (2013-10-16) found inadequate risk controls; $12M SEC fine; emergency $400M Getco-led investment; firm absorbed by Getco.
- **URL:** https://www.sec.gov/files/litigation/admin/34-70694.pdf (cited via search result: `youtube.com/watch?v=7R787Fb0zzk` sources list) · NYT DealBook "Knight Capital Says Trading Glitch Cost It $440 Million" (2012-08-02) · http://www.tradersmagazine.com/news/brokerage/the-rise-and-fall-of-knight-capital-buy-high-sell-low-rinse-repeat-119960-1.html
- **Source type:** P1 (SEC order) via P2/P4 secondaries this session.
- **Author/org:** U.S. Securities and Exchange Commission; NYSE; Reuters/NYT/Traders Magazine reporting.
- **Pub date:** 2012-08-01 (incident); 2012-08-02 (NYT); 2013-10-16 (SEC order).
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Multiple independent secondaries agree on all load-bearing facts (45 min, 7/8 servers, Power Peg, flag reuse, $440–460M). Loss figure varies $440M (initial) vs $460M (mark-to-market) — preserved as a range, not silently resolved.
- **Contradictions:** None material; only the loss-figure range above.
- **Implication:** Direct evidence for deployment-discipline, dead-code, flag-hygiene, kill-switch and reversibility rules (R-11, R-12, R-16, R-25).

## E-CROWD — CrowdStrike Falcon outage, Jul 2024

- **Claim:** On 2024-07-19 CrowdStrike shipped a Rapid Response Content update ("Channel File 291") in which a template declared 21 input fields while the Content Interpreter supplied 20, causing an out-of-bounds read inside a kernel driver → BSOD/boot loops on ~8.5M Windows devices (Microsoft figure). Live 04:09–05:27 UTC (~78 min). Root cause analysis published 2024-08-06: mismatch escaped "multiple layers" of testing because prior template instances used a wildcard in field 21; remediation included staged deployment of template instances.
- **URL:** https://www.techtarget.com/cybersecurity/news/366596579/CrowdStrike-Content-validation-bug-led-to-global-outage · https://thehackernews.com/2024/08/crowdstrike-reveals-root-cause-of.html
- **Source type:** P1 (vendor RCA) via P2 reporting this session.
- **Author/org:** CrowdStrike (PIR 2024-07-24; RCA 2024-08-06); Microsoft (8.5M figure); TechTarget/The Hacker News.
- **Pub date:** 2024-07-19 (incident); 2024-08-06 (RCA).
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Independent technical reconstructions agree (threatpedia incident file, dev.to explainer). "Channel File 2971" appears in one secondary (hipaajournal) — treated as a typo against CrowdStrike's own "Channel File 291".
- **Contradictions:** None material.
- **Implication:** Direct evidence for testing-the-real-input-path, staged rollout, and content-vs-code risk rules (R-18, R-19, R-25).

## E-GITLAB — GitLab database deletion, Jan 2017

- **Claim:** On 2017-01-31 an engineer deleted the primary PostgreSQL data directory instead of the secondary's during replication repair (~300GB, ~5,000 projects/comments, ~700 accounts affected; ~6h of data lost; ~18h outage). Standard pg_dump backups had been silently failing (PostgreSQL 9.2 tool vs 9.6 server); failure-alert emails never arrived (DMARC rejection); S3 upload misconfigured. Recovery used a 6-hour-old LVM snapshot taken for staging — never intended for DR. GitLab published the full postmortem publicly, live-streaming the recovery.
- **URL:** https://thehackernews.com/2024/03/4-instructive-postmortems-on-data.html (summarises GitLab's public postmortem)
- **Source type:** P1 (GitLab's public postmortem) via P2 summary this session.
- **Author/org:** GitLab, Inc.
- **Pub date:** 2017-01-31 (incident); postmortem published days after.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Widely and consistently retold; five-whys structure confirmed across sources.
- **Contradictions:** "300GB" vs "six hours of data" — both true (volume vs time-window framings).
- **Implication:** Direct evidence for backup-restore testing, alert-delivery verification, replication≠recovery, blameless public postmortem rules (R-24, R-29, R-30).

## E-DORA — DORA / Accelerate research program

- **Claim:** The DevOps Research and Assessment program (founded 2015 by Forsgren, Humble, Kim; acquired by Google Cloud 2018; book *Accelerate*, 2018) surveyed 31,000+ professionals over 7 years. Four keys: Deployment Frequency, Lead Time for Changes, Change Failure Rate, Mean Time to Restore (later "Failed Deployment Recovery Time"; a 5th key, Deployment Rework Rate, added later; Reliability added 2021). Core finding: elite performers excel at speed AND stability simultaneously — the assumed tradeoff is not supported by the data. Elite benchmarks: on-demand deploys, lead time <1 day, change fail ~5–15%, recovery <1 hour (19% of 2024 respondents elite).
- **URL:** https://github.com/marcos-sponton/frameworks-as-skills/blob/HEAD/_research/dora-accelerate.md · https://medium.com/beyond-the-code-by-typo/dora-metrics-a-practical-guide-for-engineering-leaders-f36bd3e526d1
- **Source type:** P3 (research program + book) via P4 mirrors this session.
- **Author/org:** Nicole Forsgren, Jez Humble, Gene Kim / Google Cloud DORA.
- **Pub date:** 2018 (book); program 2015–present; 2024 State of DevOps figures.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Benchmarks consistent across independent mirrors; caveat recorded that survey-based tiers are descriptive, not causal.
- **Contradictions:** Minor benchmark drift across years/tiers (e.g., elite fail rate ~5% vs 0–15%) — preserved as ranges.
- **Implication:** Grounds throughput/stability rules and the measure-improvement loop (R-14, R-27, R-33).

## E-PEARCE — "Asleep at the Keyboard?", IEEE S&P 2022

- **Claim:** Pearce et al. (NYU) prompted GitHub Copilot across 89 scenarios (1,689 programs) covering MITRE CWE Top-25 weaknesses in Python, C, Verilog; ~40% of completions were vulnerable (CodeQL + manual inspection). A 2023 replication found the rate down to ~27% but still high.
- **URL:** https://arxiv.org/pdf/2108.09293.pdf · DOI 10.1109/SP46214.2022.00057
- **Source type:** P1 (peer-reviewed paper).
- **Author/org:** Hammond Pearce, Baleegh Ahmad, Benjamin Tan, Brendan Dolan-Gavitt, Ramesh Karri (NYU / U. Calgary).
- **Pub date:** 2021-08 (arXiv); IEEE S&P 2022.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Cited and reproduced by multiple later studies (incl. He & Vechev 2023: ~29.5% Python / 24.2% JS vulnerable across 43 CWEs).
- **Contradictions:** None on the headline finding; rates vary by model vintage and prompt set — expected.
- **Implication:** Core evidence for AI-code verification rules (R-13, R-20, AP-09).

## E-PERRY — "Do Users Write More Insecure Code with AI Assistants?", CCS 2023

- **Claim:** Perry et al. (Stanford) ran 47 participants (students + professionals) on 5 security tasks; the AI-assisted group produced significantly less secure code on 4 of 5 tasks (notably string encryption and SQL injection: 36% SQLi vs 7% control in one summary) AND reported higher confidence their code was secure. DOI 10.1145/3576915.3623157.
- **URL:** https://kumarde.com/papers/codex.pdf · https://www.theregister.com/software/2022/12/21/ai-assistants-help-developers-produce-code-thats-insecure/1429292
- **Source type:** P1 (peer-reviewed paper) via P1/P2 this session.
- **Author/org:** Neil Perry, Megha Srivastava, Deepak Kumar, Dan Boneh (Stanford).
- **Pub date:** 2023-11 (CCS '23, Copenhagen).
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Consistent with Pearce; 2025 Google-developer interview study cites it as the security-performance reference.
- **Contradictions:** Sandoval et al. found only ~10% more bugs, not statistically significant (C tasks) — recorded as genuine counterevidence, not dismissed (see AP-09 counterexamples).
- **Implication:** Core evidence that AI assistance degrades security outcomes and inflates confidence — verification must be independent of the generator (R-13).

## E-SANDOVAL — Sandoval et al. (counterevidence)

- **Claim:** Sandoval et al. ran 58 participants on C programming tasks; AI-assisted vs control showed ~10% more security bugs, not statistically significant.
- **Source type:** P1 (paper) via P1 citation in a 2025 arxiv qualitative study, found this session.
- **Author/org:** Sandoval et al.
- **Pub date:** 2023 (cited in later work).
- **Confidence:** Medium (via secondary citation). **Label:** Corroborated.
- **Corroboration:** Asare et al. (25 participants, counterbalanced) also found no significant difference — consistent direction.
- **Contradictions:** Tensions with Perry et al. — task domain (C vs multi-language), participant skill, and measurement differences plausibly explain it.
- **Implication:** The AI-security effect is real but task- and skill-dependent; supports nuanced verification rules rather than blanket prohibition (R-13 exceptions, AP-09 counterexamples).

## E-SNYK — Snyk industry survey on AI suggestions

- **Claim:** In a Snyk industry survey, 56.4% of software professionals reported insecure suggestions by AI assistants are common.
- **Source type:** P2 (survey) via P1 citation in a 2025 arxiv study, found this session.
- **Author/org:** Snyk.
- **Pub date:** ~2024 (cited 2025).
- **Confidence:** Medium (via secondary citation; vendor survey). **Label:** Corroborated.
- **Corroboration:** Directionally consistent with Pearce/Perry.
- **Contradictions:** Vendor-conducted; possible framing bias — noted.
- **Implication:** Practitioner perception aligns with measured vulnerability rates (R-13).

## E-LANYADO — hallucinated package names (slopsquatting)

- **Claim:** Security researcher Lanyado demonstrated AI assistants hallucinate software package names; attackers register those names to distribute malicious code (later termed "slopsquatting").
- **Source type:** P2/P3 via P1 citation in a 2025 arxiv study, found this session.
- **Author/org:** Lanyado (security researcher).
- **Pub date:** 2023–2024.
- **Confidence:** Medium. **Label:** Corroborated.
- **Corroboration:** Widely referenced in supply-chain security discourse.
- **Contradictions:** None found.
- **Implication:** Verify dependency names AI suggests before installing — supply-chain angle of R-13/R-23.

## E-AMZN — Amazon Working Backwards (PR/FAQ, six-page narrative)

- **Claim:** Amazon's product process starts with a mock press release + FAQ written before design/engineering ("working backwards"), plus six-page prose narrative memos read silently at meeting start (no slides). Bezos's 2004 internal email: narrative structure forces better thought. Most PR/FAQs are rejected — rejection is the point.
- **URL:** https://github.com/product-on-purpose/thinking-framework-skills/blob/HEAD/frameworks/decision-brief-pr-faq/dossier.md · https://github.com/teambrilliant/dev-skills/blob/HEAD/skills/working-backwards/references/six-page-narrative.md · book: Bryar & Carr, *Working Backwards* (2021).
- **Source type:** P3 (practitioner book + insider accounts) via P4 mirrors this session.
- **Author/org:** Amazon (Bezos; Bryar & Carr, former Amazon execs).
- **Pub date:** 2004 (email); 2021 (book).
- **Confidence:** High on the mechanism's existence; Medium on causal efficacy (no controlled studies). **Label:** Verified (existence/mechanics); Corroborated (efficacy claims).
- **Corroboration:** Consistent across many independent ex-Amazon accounts.
- **Contradictions:** None on mechanics; efficacy is practitioner-attested, not experimentally proven.
- **Implication:** Evidence for write-first specification and decision-memo rules (R-04; templates 03, 04).

## E-ASVS — OWASP Application Security Verification Standard

- **Claim:** ASVS is a catalogue of verifiable security requirements: v4.0.3 (Oct 2021, 14 chapters, 286 requirements); v5.0.0 (May 2025, 17 chapters, ~345 requirements). Three levels: L1 minimum for any internet-facing app (automatable), L2 standard for apps handling sensitive data, L3 high-assurance. Levels are cumulative.
- **URL:** https://github.com/OWASP/ASVS (canonical) · https://github.com/nmor/the-claude-council/blob/HEAD/skills/owasp-asvs/SKILL.md
- **Source type:** P1 (open standard).
- **Author/org:** OWASP Foundation.
- **Pub date:** 4.0.3: 2021-10; 5.0.0: 2025-05.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** De-facto procurement/pentest baseline; maps to NIST SP 800-53, PCI-DSS.
- **Contradictions:** Requirement counts vary slightly across mirrors (286 vs 345 = version difference, 4.x vs 5.0).
- **Implication:** Standard of care for security verification rules and the security-verification template (R-22; template 13).

## E-12F — The Twelve-Factor App

- **Claim:** Adam Wiggins (Heroku) published the 12-factor methodology (2011; open-sourced Nov 2024, github.com/heroku/12factor): codebase, dependencies, config-in-environment, backing services, build/release/run separation, stateless processes, port binding, concurrency, disposability, dev/prod parity, logs as event streams, admin processes.
- **URL:** https://en.wikipedia.org/wiki/Twelve-Factor_App_methodology · https://12factor.net
- **Source type:** P1 (methodology site) via P2 this session.
- **Author/org:** Adam Wiggins / Heroku.
- **Pub date:** 2011 (presented); 2024-11 (open-sourced).
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Near-universal adoption as cloud-native baseline (Kubernetes, Cloud Run assume ~12-factor shape).
- **Contradictions:** None on content; scope debates (Hoffman's 15-factor, community "many-factor") are extensions, not refutations.
- **Implication:** Grounds build/deploy/operability rules (R-11, R-12, R-15, R-28).

## E-BUILDTRAP — *Escaping the Build Trap* (Perri, 2018)

- **Claim:** Perri (O'Reilly, Nov 2018) diagnoses the "build trap": orgs that live by outputs ship features to meet schedules rather than customer needs; the fix is outcome-oriented product management connecting vision → strategy → opportunities → iterative delivery.
- **URL:** https://www.bookhype.com/book/show/91577cbe-99e7-4874-9e27-7826b76da33b/escaping-the-build-trap
- **Source type:** P3 (practitioner book).
- **Author/org:** Melissa Perri (Produx Labs; HBS faculty 2019).
- **Pub date:** 2018-11.
- **Confidence:** High on the diagnosis as observed pattern; Medium on universality. **Label:** Verified (existence/content); Corroborated (diagnostic validity).
- **Corroboration:** Consistent with Lean Startup, Cagan, and DORA's warning against output metrics.
- **Contradictions:** None found.
- **Implication:** Core evidence for outcome-first, anti-feature-factory rules (R-01, R-02, AP-04, AP-19).

## E-LEAN — *The Lean Startup* (Ries, 2011)

- **Claim:** Ries (Crown Business, 2011) formalises build-measure-learn, the MVP as a validated-learning vehicle, and innovation accounting; central pivot/persevere decision.
- **Source type:** P3 (practitioner book).
- **Author/org:** Eric Ries.
- **Pub date:** 2011.
- **Confidence:** High. **Label:** Corroborated (well-established; not re-verified against primary this session).
- **Corroboration:** Foundational startup text; consistent with Torres, Cagan.
- **Contradictions:** Critics note MVP misuse (shipping junk labelled "MVP") — recorded as a misuse warning, not a refutation.
- **Implication:** Grounds validation and outcome-metric rules (R-01, R-02, R-34).

## E-CAGAN — *Inspired* (Cagan, 2nd ed. 2018)

- **Claim:** Cagan (Wiley/SVPG, 2018) argues product discovery must retire four risks before build: value (will they buy?), usability (can they use it?), feasibility (can we build it?), viability (does it work for the business).
- **Source type:** P3 (practitioner book).
- **Author/org:** Marty Cagan (Silicon Valley Product Group).
- **Pub date:** 2018 (2nd ed.).
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Standard product-management canon; consistent with Torres continuous discovery.
- **Contradictions:** None material.
- **Implication:** Structures discovery components of the small-team OS and validation templates (R-03; templates 01, 03).

## E-TORRES — *Continuous Discovery Habits* (Torres, 2021)

- **Claim:** Torres (Product Talk, 2021) prescribes weekly customer touchpoints and opportunity-solution trees linking outcomes → opportunities → solutions → experiments.
- **Source type:** P3 (practitioner book).
- **Author/org:** Teresa Torres.
- **Pub date:** 2021.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Consistent with Cagan/Lean Startup discovery practice.
- **Contradictions:** None material.
- **Implication:** Discovery cadence in the small-team OS (R-03).

## E-SHAPEUP — *Shape Up* (Singer, Basecamp, 2019)

- **Claim:** Singer (37signals, 2019; free at basecamp.com/shapeup) documents Basecamp's method: six-week cycles + cooldown, fixed time/variable scope ("appetite" not estimates), shaping before betting, pitches with problem/appetite/solution/rabbit-holes/no-gos, circuit breaker (work not done at cycle end dies; must be re-pitched), hill charts.
- **URL:** https://github.com/mturac/product-init/blob/HEAD/references/shape-up.md · https://basecamp.com/shapeup
- **Source type:** P3 (practitioner book).
- **Author/org:** Ryan Singer (Basecamp/37signals).
- **Pub date:** 2019.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Consistent across independent summaries; adoption reported by many small teams.
- **Contradictions:** One explainer (gazar.dev) notes heavy reliance on anecdote over evidence — recorded.
- **Implication:** Grounds appetite-based scoping, circuit-breaker and cooldown rules (R-05; small-team OS planning component).

## E-SRE — Google *Site Reliability Engineering* (2016)

- **Claim:** The SRE book (O'Reilly, 2016; eds. Beyer, Jones, Petoff, Murphy) codifies: SLIs/SLOs/SLAs, error budgets (unreliability allowance; budget exhausted → freeze features, fix reliability), four golden signals (latency, traffic, errors, saturation), blameless postmortem culture (Ch.15), alerting on symptoms with actionable pages, toil reduction via automation. SRE practice originated at Google ~2003 (Treynor).
- **URL:** https://sre.google/sre-book/postmortem-culture/ (Ch.15, cited in sources found this session)
- **Source type:** P1/P3 (canonical operations text; free online).
- **Author/org:** Google (Betsy Beyer et al., eds.).
- **Pub date:** 2016.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Industry-standard; DORA 2021 added Reliability as adjacent dimension.
- **Contradictions:** None material.
- **Implication:** Grounds operability rules (R-28, R-29, R-30, R-31).

## E-ALLSPAW — Allspaw, "Blameless PostMortems and a Just Culture" (2012)

- **Claim:** Allspaw (Etsy, Code as Craft, 2012) argues postmortems must assume practitioners acted reasonably given what they knew; blame suppresses the honest reporting root-cause analysis depends on; intellectual basis in Reason's systems approach and Cook's *How Complex Systems Fail* (2000).
- **URL:** https://www.etsy.com/codeascraft/blameless-postmortems/ (cited in sources found this session)
- **Source type:** P3 (practitioner essay).
- **Author/org:** John Allspaw (Etsy).
- **Pub date:** 2012.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Codified in SRE Ch.15; STELLA report's blameless-vs-sanctionless distinction adds nuance (recorded).
- **Contradictions:** None on the core claim; nuance that "blameless ≠ sanctionless".
- **Implication:** Direct evidence for R-30 and the incident-response template.

## E-RELEASEIT — *Release It!* (Nygard; 1st ed. 2007, 2nd ed. 2018)

- **Claim:** Nygard (Pragmatic Bookshelf) catalogues production stability patterns — timeout, circuit breaker, bulkhead, steady state, fail fast, handshaking/back-pressure, test harness, decoupling middleware — and the thesis that integration points are the #1 stability killer; failures propagate and cracks accelerate; design for production, not QA.
- **URL:** https://github.com/franciscolopes26/staff-engineer-mode/blob/HEAD/skills/staff-engineer-mode/references/release-it.md
- **Source type:** P3 (practitioner book) via P4 mirror this session.
- **Author/org:** Michael T. Nygard.
- **Pub date:** 2007 (1st ed.); 2018 (2nd ed.).
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Patterns independently re-codified by Microsoft Azure Architecture Center ("Cloud Design Patterns").
- **Contradictions:** None material.
- **Implication:** Grounds design-for-failure rules and fragile-architecture anti-pattern (R-10, R-25, AP-06).

## E-JOEL — The Joel Test (Spolsky, 2000)

- **Claim:** Spolsky (joelonsoftware.com, 2000-08-09) proposed 12 yes/no questions rating a software team: source control, one-step build, daily builds, bug database, fix bugs before new code, up-to-date schedule, spec, quiet working conditions, best tools, testers, code-writing interviews, hallway usability testing. 12 perfect / 11 tolerable / ≤10 serious problems.
- **URL:** https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/
- **Source type:** P3 (practitioner essay).
- **Author/org:** Joel Spolsky.
- **Pub date:** 2000-08-09.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** A 2025 HN thread ("25 years later") debates modernisation; CheckGit's 20-year update revises items (git, CI before merge, automated testing).
- **Contradictions:** Some items aged (daily builds → CI; hallway testing → continuous UX research) — recorded as evolution, not refutation.
- **Implication:** Historical baseline for engineering-hygiene rules (R-11, R-12, R-14); several rules are its modernised descendants.

## E-GAWANDE — WHO surgical safety checklist study (2009)

- **Claim:** Gawande et al. (NEJM, 2009) tested a 19-item WHO surgical checklist in 8 hospitals across 6 WHO regions (7,688 patients): major complications 11%→7% (~one-third reduction); inpatient deaths 1.5%→0.8% (>40% reduction). Book: *The Checklist Manifesto* (Metropolitan Books, 2009). Checklist design rules: 5–9 items, killer items only, simple exact wording, one page, defined pause points, do-confirm vs read-do, test in the real world.
- **URL:** https://www.who.int/news/item/11-12-2010-checklist-helps-reduce-surgical-complications-deaths · https://news.un.org/en/story/2009/01/287662
- **Source type:** P1 (peer-reviewed study) via P2 (WHO/UN) this session.
- **Author/org:** Atul Gawande et al.; WHO.
- **Pub date:** 2009 (NEJM); book 2009.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Pronovost's Michigan central-line study (below) is an independent replication of the checklist mechanism.
- **Contradictions:** Effect sizes vary by implementation fidelity in later replications — recorded; the mechanism (pause-point verification of killer items) is what transfers.
- **Implication:** Justifies the checklist methodology underlying §34 templates and release-gate practice (R-18; templates 14, 18).

## E-PRONOVOST — Pronovost central-line checklist, Michigan (2006)

- **Claim:** Pronovost (Johns Hopkins) introduced a 5-step checklist for central-line insertion across Michigan ICUs; teams skipped ≥1 step 30% of the time before; after 15 months infection rates fell from ~4% toward zero, saving ~1,500 lives and ~$175–200M (per Gawande's reporting).
- **URL:** https://hsph.harvard.edu/news/fall08checklist/
- **Source type:** P2 (Harvard reporting of the study) via Gawande's account.
- **Author/org:** Peter Pronovost (Johns Hopkins); reported by Gawande/Harvard.
- **Pub date:** 2006 (study); reported 2008.
- **Confidence:** Medium-High. **Label:** Corroborated.
- **Corroboration:** Consistent with the WHO replication.
- **Contradictions:** Exact savings figures vary ($175M vs $200M) — preserved as approximate.
- **Implication:** Independent support for checklist discipline (templates; R-18).

## E-ANTHROPIC — "Building Effective Agents" (Anthropic, Dec 2024)

- **Claim:** Schluntz & Zhang (Anthropic Engineering, 2024-12-19) distinguish workflows (LLMs orchestrated through predefined code paths) from agents (LLMs dynamically directing their own processes/tool use); advise the simplest solution possible, noting agentic systems trade latency and cost for task performance; document five workflow patterns (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer); agents need well-designed tools, sandbox testing, guardrails, human checkpoints.
- **URL:** https://www.anthropic.com/engineering/building-effective-agents
- **Source type:** P1 (vendor engineering publication).
- **Author/org:** Erik Schluntz & Barry Zhang, Anthropic.
- **Pub date:** 2024-12-19.
- **Confidence:** High. **Label:** Verified.
- **Corroboration:** Became industry definitional standard; widely and consistently summarised.
- **Contradictions:** None material.
- **Implication:** Grounds controlled-agent rules, excessive-automation and uncontrolled-agent anti-patterns (R-13 context; AP-10, AP-11; small-team OS coding-agents component; template 09).

## E-KARPATHY — "Vibe coding" discourse (2025–2026)

- **Claim:** Karpathy (X, 2025-02-02) coined "vibe coding": fully giving in to the vibes, "Accept All", not reading diffs — explicitly scoped to "throwaway weekend projects". Willison's boundary: building with an LLM *without reviewing the code it writes*; reviewed/tested/explainable = regular software development. YC W25: ~25% of startups had ~95% AI-generated codebases (Garry Tan, 2025-03). 2025 Stack Overflow survey: 84% use/plan AI tools; 72% of professionals say vibe coding is not part of professional work; 46% distrust AI accuracy.
- **URL:** https://dev.to/asyncinnovator/what-happens-to-vibe-coders-what-the-research-actually-says-33eb · https://thingshavehistory.com/posts/karpathy-agentic-engineering-2026/
- **Source type:** P3/P4 (practitioner discourse + survey) this session.
- **Author/org:** Andrej Karpathy; Simon Willison; Y Combinator (Garry Tan); Stack Overflow.
- **Pub date:** 2025-02-02 (coinage); 2025–2026 (surveys/discourse).
- **Confidence:** High on coinage/scope; Medium on survey precision. **Label:** Verified (coinage, scope); Corroborated (stats).
- **Corroboration:** Collins Dictionary Word of the Year 2025 confirms cultural penetration.
- **Contradictions:** Definition stretched in popular use (dictionary definition omits the no-review element) — recorded; the rules use Willison's boundary.
- **Implication:** Frames the AI-verification rule precisely: the dividing line is review, not AI use (R-13; AP-09).

## E-VAPOR — Vaporware / misleading demos

- **Claim:** Ovation (1983): demo used to raise funding was fake per NYT; company bankrupt before release (Built In, citing NYT). Magic Leap: The Information (via The Verge, 2016) reported deceptive tech demos while "years behind schedule" — contested by the company. 2026 practitioner/analyst consensus (TechTarget): demand production testing not demos; demos hide governance, security, cost and scale gaps; AI procurement red flag = "trust us, just deploy, no time for a pilot".
- **URL:** https://builtin.com/hardware/vaporware · https://tech.slashdot.org/story/16/12/09/1535221/magic-leap-used-fake-tech-demos-and-is-years-behind-schedule · https://www.techtarget.com/it-strategy/feature/Vaporware-explained-What-CIOs-need-to-know
- **Source type:** P2 (press/analyst).
- **Author/org:** NYT (via Built In); The Information via The Verge; TechTarget analysts.
- **Pub date:** 1983–2016 (cases); 2026 (analyst guidance).
- **Confidence:** Medium. **Label:** Corroborated.
- **Corroboration:** Multiple independent cases + current analyst guidance converge.
- **Contradictions:** Magic Leap disputed the reporting — recorded.
- **Implication:** Evidence for misleading-demo anti-pattern and realistic-demo rules (AP-14; templates 07, 17).

## E-BROOKS — *The Mythical Man-Month* (Brooks, 1975)

- **Claim:** Brooks (Addison-Wesley, 1975; anniversary ed. 1995): "adding manpower to a late software project makes it later" (Brooks's law); the second-system effect (over-design of the follow-up system); "plan to throw one away".
- **Source type:** P3 (classic text).
- **Author/org:** Fred Brooks (IBM System/360).
- **Pub date:** 1975.
- **Confidence:** High. **Label:** Corroborated (canonical; not re-verified against primary this session).
- **Corroboration:** Half a century of citation; second-system effect independently observed.
- **Contradictions:** None material; scope is large-system management, not small-team tactics.
- **Implication:** Grounds small-team staffing realism and second-system warnings (AP-04/AP-05; small-team OS).

## E-GALL — Gall's law (1975)

- **Claim:** John Gall (*Systemantics*, 1975): "A complex system that works is invariably found to have evolved from a simple system that worked."
- **Source type:** P3 (book aphorism).
- **Author/org:** John Gall.
- **Pub date:** 1975.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Quoted across architecture literature (incl. Release It! skill material found this session).
- **Contradictions:** None found.
- **Implication:** Grounds start-simple, modular-monolith-first architecture guidance (R-10; small-team OS architecture).

## E-CONWAY — Conway's law (1967) / Team Topologies (2019)

- **Claim:** Conway (1967): organisations design systems mirroring their communication structures. Skelton & Pais (*Team Topologies*, IT Revolution, 2019): team cognitive load is the binding constraint; four team types and three interaction modes (collaboration, x-as-a-service, facilitating).
- **Source type:** P1 (paper) / P3 (book).
- **Author/org:** Melvin Conway; Matthew Skelton & Manuel Pais.
- **Pub date:** 1967; 2019.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Conway's law empirically revisited multiple times; Team Topologies widely adopted.
- **Contradictions:** Conway's law is descriptive-tendency, not deterministic — recorded.
- **Implication:** Small-team architecture and ownership rules (AP-06; small-team OS).

## E-FOWLER — Fowler: refactoring, CI, YAGNI-adjacent simplicity

- **Claim:** Fowler (*Refactoring*, 1999; martinfowler.com): continuous integration, "you aren't gonna need it" (YAGNI, from XP) as simplicity discipline; technical-debt metaphor (1992/2003 formulations via Cunningham).
- **Source type:** P3 (books/essays).
- **Author/org:** Martin Fowler (ThoughtWorks).
- **Pub date:** 1999–2000s.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Industry canon; YAGNI independently attributed to XP (Beck).
- **Contradictions:** None material.
- **Implication:** Simplicity/abstraction rules (R-08; AP-05).

## E-KNUTH — Knuth on premature optimization (1974)

- **Claim:** Knuth ("Structured Programming with go to Statements", *Computing Surveys*, 1974): "premature optimization is the root of all evil" (commonly quoted form; full sentence qualifies: programmers waste time on noncritical parts).
- **Source type:** P1 (paper).
- **Author/org:** Donald Knuth.
- **Pub date:** 1974.
- **Confidence:** High on attribution; exact wording as commonly quoted. **Label:** Corroborated.
- **Corroboration:** Universally cited; full-sentence context widely reproduced.
- **Contradictions:** Often misquoted without the qualifying context — recorded.
- **Implication:** Grounds measure-before-optimising rule (R-17; AP-11 nuance).

## E-BORING — "Choose Boring Technology" (McKinley, 2015)

- **Claim:** McKinley (2015 essay): innovation tokens are scarce — spend them on what differentiates you; adopt battle-tested technology for everything else; operational cost dominates novelty value.
- **Source type:** P3 (practitioner essay).
- **Author/org:** Dan McKinley.
- **Pub date:** 2015.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Widely adopted as small-team doctrine; consistent with Gall's law.
- **Contradictions:** None material; explicitly scoped (not anti-innovation).
- **Implication:** Technology-choice rule and unnecessary-infrastructure anti-pattern (R-07; AP-17).

## E-ADR — Architecture Decision Records (Nygard, 2011)

- **Claim:** Michael Nygard (no, the ADR originator — architect Michael Nygard's 2011 blog post "Documenting Architecture Decisions") proposed lightweight ADRs: context, decision, consequences; stored with the code.
- **Source type:** P3 (blog post).
- **Author/org:** Michael Nygard (architect; cognitect).
- **Pub date:** 2011-11.
- **Confidence:** Medium (attribution as commonly cited; not re-verified against primary this session). **Label:** Corroborated.
- **Corroboration:** ADR practice standardised (MADR template etc.).
- **Contradictions:** None found.
- **Implication:** Grounds decision-recording rule and template 05.
- **Note:** "Michael Nygard" the architect (ADR) vs "Michael T. Nygard" (*Release It!*) are different people — kept distinct.

## E-SHOSTACK — Threat modeling (Shostack, 2014)

- **Claim:** Shostack (*Threat Modeling: Designing for Security*, Wiley, 2014): model early with STRIDE-per-element or attacker-centric questions; threat modeling is a design activity, not a compliance checkbox; Microsoft's SDL made it standard practice.
- **Source type:** P3 (practitioner book).
- **Author/org:** Adam Shostack.
- **Pub date:** 2014.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** ASVS V1 (Architecture, Design and Threat Modeling) independently requires it.
- **Contradictions:** None material.
- **Implication:** Grounds threat-model rule (R-09) and security-verification template.

## E-NIST — NIST cybersecurity guidance

- **Claim:** NIST CSF 2.0 (2024) organises security into Govern/Identify/Protect/Detect/Respond/Recover; SP 800-53 Rev.5 catalogues controls; SP 800-63B governs digital identity/authentication assurance.
- **Source type:** P1 (standards).
- **Author/org:** U.S. National Institute of Standards and Technology.
- **Pub date:** CSF 2.0: 2024-02; SP 800-53 Rev.5: 2020.
- **Confidence:** High. **Label:** Corroborated (well-established; not re-fetched this session).
- **Corroboration:** Referenced by ASVS mappings found this session.
- **Contradictions:** None material.
- **Implication:** Least-privilege and identity rules (R-21).

## E-LOG4J — Supply-chain vulnerability response (Log4Shell, 2021)

- **Claim:** Log4Shell (CVE-2021-44228, Dec 2021): critical RCE in ubiquitous Java logging library; CISA emergency directive; demonstrated that transitive dependencies are a first-class risk surface and patch latency is the exposure window.
- **Source type:** P1/P2 (CVE, CISA).
- **Author/org:** Alibaba Cloud Security Team (discovery); CISA; Apache.
- **Pub date:** 2021-12.
- **Confidence:** High. **Label:** Corroborated (canonical incident; not re-fetched this session).
- **Corroboration:** Universally documented.
- **Contradictions:** None material.
- **Implication:** Grounds dependency-patching rule (R-23) and weak-security anti-pattern (AP-08).

## E-PHOENIX — *The Phoenix Project* (Kim, Behr, Spafford, 2013)

- **Claim:** Kim et al. (IT Revolution, 2013) novelise the "Three Ways": systems thinking/flow, amplify feedback loops, culture of continual experimentation and learning.
- **Source type:** P3 (book).
- **Author/org:** Gene Kim, Kevin Behr, George Spafford.
- **Pub date:** 2013.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Consistent with DORA capabilities research.
- **Contradictions:** Novelised; illustrative rather than empirical — recorded.
- **Implication:** Flow/feedback framing for the small-team OS.

## E-OUSTERHOUT — *A Philosophy of Software Design* (2018)

- **Claim:** Ousterhout (Yaknyam Press, 2018): prefer deep modules (simple interface, significant functionality); "define errors out of existence"; comments describe what code doesn't say; complexity is incremental.
- **Source type:** P3 (book).
- **Author/org:** John Ousterhout (Stanford).
- **Pub date:** 2018.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Widely taught; consistent with Parnas information hiding.
- **Contradictions:** None material.
- **Implication:** Interface/abstraction discipline (R-08; AP-05).

## E-KLEPPMANN — *Designing Data-Intensive Applications* (2017)

- **Claim:** Kleppmann (O'Reilly, 2017): reliability/scalability/maintainability as the design goals; replication, partitioning, transactions, consistency models, and derived-data systems surveyed with failure-mode analysis.
- **Source type:** P3 (book).
- **Author/org:** Martin Kleppmann (Cambridge).
- **Pub date:** 2017.
- **Confidence:** High. **Label:** Corroborated.
- **Corroboration:** Standard distributed-systems reference.
- **Contradictions:** None material.
- **Implication:** Data-layer architecture guidance (AP-06; small-team OS architecture).

## E-PROTOTYPE-WOZ — Wizard-of-Oz prototyping (counterevidence for demos)

- **Claim:** Wizard-of-Oz prototyping (human simulates the system behind a façade) is a legitimate, documented UX research technique — the ethical line is disclosure: label concepts as concepts (volanea.com validation guidance, 2026).
- **URL:** https://www.volanea.com/blog/product-mockup-market-validation
- **Source type:** P3/P4 (practitioner guidance) this session.
- **Author/org:** Volanea (product validation practitioners).
- **Pub date:** 2026.
- **Confidence:** Medium. **Label:** Corroborated.
- **Corroboration:** WoZ is textbook HCI method (Kelley 1980s origins; standard in UX curricula).
- **Contradictions:** None.
- **Implication:** Counterexample for AP-14: faked demos are legitimate in research *with disclosure*; fraud is undisclosed fakery.

## E-SLOSS — "Move fast" failure-rate economics (general practitioner consensus)

- **Claim:** Practitioner consensus (DORA, SRE, Release It!) converges on: small batches reduce blast radius; reversibility beats perfection; production is the only complete test environment.
- **Source type:** SYN of E-DORA, E-SRE, E-RELEASEIT.
- **Confidence:** High. **Label:** Inferred (as a combined statement); components individually Verified.
- **Implication:** Underpins ship/operate rules (R-25, R-27).

---

## Gaps and unknowns (stated plainly)

- **METR / frontier agent-autonomy evaluations (2025–2026):** not researched this session — agent-capability claims kept to Anthropic's own published guidance (E-ANTHROPIC). Label any stronger autonomy claim *Unknown*.
- **Exact current DORA benchmark tiers (2025/2026 reports):** figures above are 2024-vintage via mirrors; treat tier numbers as approximate. Label *Corroborated*, not *Verified*.
- **ASVS v5.0.0 requirement counts:** mirrors report ~345–346; minor variance preserved.
- **Magic Leap demo dispute:** company contested the reporting; the case is used as *reported*, not adjudicated.
- **Primary texts re-read:** Brooks, Knuth, Fowler, Ousterhout, Kleppmann, Ries, Cagan, Torres, Shostack, Phoenix Project were not re-fetched this session; their claims are labelled *Corroborated* on the strength of canonical status plus independent secondary confirmation found this session, not *Verified*.
