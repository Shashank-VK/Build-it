# Fringe Engineering Practices — Unwritten Rules

**The Omniscient Resource Atlas · product_engineering / expansion-practices · Built 2026-10-10**
**Read-only research only.** Discovers, inspects, categorizes. Does not install, build, configure, rank, or recommend.

Labels: **Verified** (primary source read this pass) / **Corroborated** (≥2 independent sources) / **Inferred** (confident practitioner consensus, not re-verified) / **Proposed** (author synthesis) / **Unknown** (gap).
Evidence classes: `primary` · `secondary` · `practitioner` · `paper` · `forum` · `meta` · `community` (anonymous lore, labeled as such).

---

## 1. "Never rewrite from scratch" — Joel Spolsky (2000) vs. the counterexamples

**The rule.** Joel Spolsky, "Things You Should Never Do, Part I" (2000, joelonsoftware.com, **primary**): never throw away working code and rewrite from scratch — the old code embodies years of accumulated bug fixes and edge-case knowledge you will painfully rediscover. Canonical cautionary tale: Netscape 6, the multi-year rewrite that let Microsoft win the browser war. **Corroborated** (one of the most-cited software essays; Netscape history well-documented).

**The counterexamples (actively sought).**
- **DHH / Basecamp** (businessofsoftware.org, 2015 AMA recap, **practitioner**): rewrites *can* be right — Basecamp itself was rebuilt; the question is whether the rewrite is driven by genuine architectural dead-ends or developer boredom.
- **Herb Caudill**, "Lessons from 6 software rewrite stories" (Medium, **practitioner**): six rewrite narratives; success factors — the old system genuinely unmaintainable, old system kept running during the rewrite (strangler pattern), scope ruthlessly contained.
- **Synthesis (Proposed):** never *big-bang* rewrite; *strangler* rewrites (gradual replacement, Fowler's Strangler Fig pattern) succeed where big-bang rewrites die. The rule's real content is about risk management, not code age.

**Boundary.** Applies: mature systems with embedded domain knowledge, no edge-case test coverage. Doesn't: architectures where the data model itself is the blocker; tiny codebases where rewrite cost is trivial.

**Engineering implication.** Default to strangler migration; require a written "what knowledge is embedded in the old code and how we preserve it" plan before any rewrite.

---

## 2. "Always be deleting code" — and Chesterton's Fence

**The rule.** Senior engineers treat net-negative-LOC diffs as the highest-signal contributions; "the best code is no code" is interview and code-review folklore. (Full treatment: file 01 §5.)

**The counterweight.** Chesterton's Fence — G.K. Chesterton, *The Thing* (1929), "The Drift from Domesticity" (**primary**, classic text): don't remove a fence until you understand why it was put up. Programming usage **Corroborated** across multiple AI-era coding-skill repos and Brandon Bryson's 2020 Medium essay "Assessing Legacy Code Using Chesterton's Fence": before deleting "dead" code, do git-blame archaeology — find the commit, the ticket, the bug report; assume the previous developer was competent; if no reason is findable after real excavation, delete only behind a safety net (feature flag, revertable commit, canary).

**The productive tension (Proposed).** Both rules are true and incomplete: "always delete" without provenance is vandalism; "never touch" without understanding is hoarding. The mature unwritten rule is *deletion with provenance*.

---

## 3. "The demo is the spec" — Apple's demo-driven process

**The rule.** At Apple, the demo — not the written spec — is the artifact of record: features are developed against working demos reviewed by leadership, and the demo's behavior becomes the specification. **Corroborated.**

**Source metadata.** Account: bezdelev.com, "Apple's demo-driven feature development process" (**practitioner**, secondary account of Apple's internal process). Corroborated by Steve Jobs demo-review lore (the circulating "Steve Jobs skill" document). Accessed: 2026-10-10. Confidence: Medium — Apple doesn't document its internal process publicly; accounts are ex-employee reports, consistent with each other.

**Why it matters.** The inverse of Working Backwards (file 01 §9): instead of writing the press release first, you *build the thing* first and let the artifact carry the spec. Both reject the same enemy — the abstract requirements document nobody reads. Demo-as-spec works where iteration is cheap and taste is concentrated (a strong design leader reviewing demos); fails where behavior must be specified *before* building (third-party APIs, safety-critical systems, distributed teams needing contracts).

**Boundary.** Applies: consumer product development with a strong editorial center; prototyping-heavy cultures. Doesn't: platform/API work where the contract is the product; regulated domains.

---

## 4. Resume-Driven Development (RDD) — from forum insult to peer-reviewed paper

**The rule (observed anti-pattern).** Developers choose technologies to enrich resumes rather than serve the system: Kubernetes for five users, microservices for two developers, blockchain for to-do lists. **Corroborated** — now empirically studied.

**The paper.** "Résumé-Driven Development: A Definition and Empirical Characterization," arXiv:2101.12703 (Jan 2021), later ICSE-SEIS 2021 (**paper**). Surveyed 591 software professionals (130 hiring, 558 technical). Findings: 60% of hiring professionals agreed trends influence their job offerings; 82% of software professionals believed using trending technologies in daily work makes them more attractive to prospective employers. Formalizes RDD as two-sided: employers signal trendiness in job ads; applicants signal trendiness in resumes; both overemphasize trending tech at the expense of fit. Accessed: 2026-10-10. Confidence: High (peer-reviewed, n=591).

**First-hand case (LinkedIn).** Calen Legaspi (Orange & Bronze Software Labs), LinkedIn article "The Hidden Cost of Resume-Driven Development" (**practitioner**, public LinkedIn post): a client's embedded-Java codebase was half a gigabyte with 100+ Maven files — each departing architect had bypassed the previous architect's work to introduce their own preferred frameworks, leaving "a convoluted tangle of dead code." Mechanism: short-tenured architects optimizing for their next job.

**The defense (strongest counterargument).** Paul E. Davis (via dev.to practitioner discussion): RDD signals developers willing to learn new tech rather than cling to obsolete solutions — "if developers are not concerned with their own careers, it's not likely they'll be concerned with your business." The paper itself notes the two-sided nature: banning trendiness produces stagnation; the pathology is *selection on trendiness instead of fit*.

**Boundary.** Real where: technology churn correlates with staff turnover; architecture decisions lack written fit-justification. Healthy version: deliberate learning budgets (spikes, 20%-style time) that don't commit the production system to someone's resume.

**Engineering implication.** Require ADRs to include "why this technology *for this problem*" (cf. McKinley's exercises, file 01 §1); treat unexplained novelty as an RDD smell.

---

## 5. Conway's Law in practice — 1968 observation to the Inverse Conway Maneuver

**The rule.** Melvin Conway, "How Do Committees Invent?" (1967; rejected by Harvard Business Review for lack of proof; published in *Datamation*, 1968 — **primary**, historical): "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." **Corroborated.**

**The empirical record.**
- **MIT/Harvard "mirroring hypothesis"** (MacCormack, Rusnak & Baldwin, *Management Science* 2006 — **paper**): "strong evidence to support the mirroring hypothesis"; loosely-coupled organizations produce significantly more modular products. **Corroborated** (Wikipedia + thinkinglabs 2026 validation post + javacodegeeks 2026 review, all consistent).
- **Microsoft/Windows Vista** (Nagappan, Murphy & Basili, 2008 — **paper**): organizational metrics (e.g., engineers touching a binary) predicted failure-prone binaries across 3,404 binaries / 50M+ LOC with 86.2% precision, 84.0% recall — outperforming code churn, complexity, dependencies, coverage. **Corroborated.**
- **The boundary (Colfer & Baldwin, 2016 — paper, review of 142 studies):** mirroring is prevalent but *not universal*; in open collaborative (mostly open-source) projects, most descriptive studies did *not* support it. Premature modularization — modular orgs for supposedly modular architectures without deep technical knowledge — performed poorly.

**Practitioner lore.**
- **Steve Yegge's 2011 platform rant** (accidentally public Google+ post; mirrored at courses.cs.washington.edu — **primary**): the famous telling of Bezos's API mandate — all teams expose functionality through service interfaces, no back doors. The canonical *Inverse Conway Maneuver* story: design the communication structure (interfaces only) to force the architecture (services). **Corroborated** (existence and broad outlines undisputed; fine details debated).
- **Satya Nadella's 2018 reorg** (Microsoft): restructuring around cloud/AI as an implicit Conway maneuver — org structure redesigned to produce the desired product architecture. **Corroborated** (widely reported).
- **The Inverse Conway Maneuver** as named practice: deliberately design team boundaries first, let architecture follow. **Practitioner** consensus; evidence base is practitioner experience, not controlled studies.

**Boundary.** The law describes; the maneuver prescribes. The maneuver fails when boundaries are drawn from org charts rather than domain knowledge (Colfer & Baldwin's premature-modularization warning).

---

## 6. "Hallway-driven development" and other folk methodologies

**Status: community observation, origin Unknown.** "Hallway-driven development" — decisions made by whoever collars whom in the hallway, i.e., architecture by proximity and loudness rather than by process — circulates as practitioner slang. No canonical origin source was located this pass (searched; no attributable coinage found). Related folk taxa, all **community** level: *Guess-Driven Development* (Jonathan Hall, dev.to — changing things until the bug goes away, then committing the whole changeset); *CV-Driven Development* (synonym of RDD); *Hype-Driven Development*; *Demo-Driven Development* (distinct from Apple's process — building only what demos well).

**Why record them.** These terms function as *diagnostic vocabulary*: teams use them to name dysfunctions that official methodologies don't describe. Their evidentiary value is as field reports of failure modes, not as practices to adopt.

---

## 7. "Programming Sucks" — Peter Welch (2014)

**The text.** "Programming Sucks" (stilldrinking.org, 2014, **primary**): a profane, widely-shared essay arguing that programming is miserable because everything is broken, tools are terrible, and the field runs on folklore and suffering — yet programmers persist because building things is irresistible. **Corroborated** (canonical URL in context notes; enormously shared in practitioner circles).

**Why it belongs in unwritten rules.** It's the emotional charter of the "software disenchantment" lineage (cf. Nikita Prokopov's "Software Disenchantment," tonsky.me, 2018 — file 06): the unwritten rule it encodes is *cynical resilience* — expect the stack to be broken, distrust abstractions, and take pride in shipping despite the tools. Its counterweight is the craftsmanship literature (file 07): Welch says the tools suck; craftsmanship says *you* can still be good.

---

## Gaps in this file

- **Unknown:** Origin of "hallway-driven development" — no attributable coinage found; recorded as community observation.
- **Unknown:** Apple's demo-driven process rests on ex-employee accounts; no first-party Apple documentation located (expected — Apple doesn't publish internal process).
- **Unknown:** DHH's rewrite position sourced from a 2015 AMA recap (secondary); primary AMA transcript not fetched.
