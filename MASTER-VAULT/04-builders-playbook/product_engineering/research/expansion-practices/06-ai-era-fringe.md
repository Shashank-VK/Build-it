# Fringe Engineering Practices — AI-Era Fringe

**The Omniscient Resource Atlas · product_engineering / expansion-practices · Built 2026-10-10**
**Read-only research only.** Discovers, inspects, categorizes. Does not install, build, configure, rank, or recommend.

Labels: **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** (see file 01 for definitions).
Evidence classes: `primary` · `secondary` · `practitioner` · `paper` · `forum` · `meta` · `community`.

---

## 1. "Vibe coding" — Karpathy's coinage and its mutation

**The claim.** "Vibe coding": building software by prompting an AI in natural language, accepting its output without reading it, guided by vibes rather than understanding. **Corroborated.**

**Source metadata.** Coinage: Andrej Karpathy, X post, 2026-02-02 (**primary**): "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." **Critical qualifier in the original post** (routinely dropped in retellings): Karpathy framed it for *"throwaway weekend projects"* — not production systems. The term became Collins Dictionary Word of the Year 2025. Karpathy later (Sequoia AI Ascent, 2026-04-30, via thingshavehistory.com — **secondary**) declared the vibe-coding era over, replaced by "agentic engineering." Accessed: 2026-10-10. Confidence: High on the coinage and qualifier (primary post); High on the mutation (the qualifier's erasure is observable across coverage).

**The mutation (Proposed analysis).** The term underwent semantic drift within months: from "a fun way to do throwaway projects" to a marketing banner for AI coding products to a pejorative for reckless AI-generated production code. Every debate about "vibe coding" since has been three different arguments (prototyping method / product category / engineering malpractice) using one phrase. Evidence labels must track *which* meaning a claim uses.

---

## 2. The YC W25 statistic — "25% of codebases 95% AI-generated"

**The claim.** In YC's Winter 2025 batch, ~25% of startups had codebases ~95% AI-generated. **Corroborated** with caveats.

**Source metadata.** Jared Friedman (YC partner), via TechCrunch, 2025-03-06 (**secondary**, reporting Friedman's statement): "a quarter of startups in YC's current cohort have codebases that are almost entirely AI-generated." Garry Tan (YC CEO) caveat (**primary**, same coverage): this reflects *early-stage* codebases — small, greenfield, pre-scale. Accessed: 2026-10-10. Confidence: Medium-High on the statement; the figure is self-reported by founders to YC, not independently audited.

**Why it matters.** It's the strongest *existence proof* that AI-generated codebases are real at the seed stage — and simultaneously the most misused statistic in the debate, because it says nothing about what happens at scale, under maintenance, or under security review (see §§4–6).

---

## 3. The "70% Problem" — Addy Osmani (2024)

**The claim.** AI coding assistants get you ~70% of the way fast, but the last 30% — debugging, edge cases, integration, production-hardening — takes as long as it ever did, and the 70% can be *misleading* because it looks done. **Corroborated.**

**Source metadata.** Addy Osmani, "The 70% Problem: Hard Truths About AI-Assisted Coding" (Substack, addyo.substack.com, late 2024 — **primary**); discussed at zed.dev/blog/ai-70-problem-addy-osmani (**secondary**). The argument: AI excels at greenfield boilerplate and well-specified components; it collapses on the long tail of real software (state management across boundaries, subtle bugs, performance, security). The "70%" is rhetorical, not measured — Osmani doesn't claim a study; it's a practitioner's model of where the pain concentrates. Accessed: 2026-10-10. Confidence: High on the argument's content; the number is illustrative, not empirical.

**Corroboration.** The 70% problem is the qualitative twin of the quantitative findings in §§4–5: speedups concentrate in the easy middle; defect rates rise in the hard tail.

---

## 4. The productivity paradox — RCT and observational evidence

**The METR RCT (2025).** METR's randomized controlled trial: 16 developers, 246 tasks — developers using AI tools were **19% slower** than the control group, while *believing* they were faster (a 39-percentage-point perception gap). Published 2025-07 (**paper**). This is the single most important datum in the AI-coding debate: the only RCT design in the set, and it found negative productivity effects *plus* systematic misperception. **Corroborated** (paper + wide secondary coverage). Caveats: small n (16 devs); task mix may not generalize; tool vintage matters (2025-era tools).

**DORA 2024.** 39,000 respondents: a 25-percentage-point increase in AI adoption associated with **−7.2% delivery stability** and **−1.5% throughput** (**meta**, dora.dev/research/2024/dora-report/). **DORA 2025**: throughput recovered upward, but instability remained elevated — the pattern suggests teams are shipping *more* with AI while breaking *more*. **Corroborated.**

**Uplevel Data Labs (2024-09-26).** ~800 developers (Uplevel customers), ~350 using GitHub Copilot; three-month pre/post comparison: **no significant improvement** in PR cycle time or throughput (cycle time −1.7 min, deemed "inconsequential"); **41% increase in detected bugs**. Data analyst Matt Hoffman: "It's obviously not a causal relationship… We just don't understand the why just yet" (IT Brew, CIO coverage — **secondary**). Accessed: 2026-10-10. Confidence: Medium-High on the numbers; the study is vendor-conducted (Uplevel sells engineering metrics) and observational, not causal — Hoffman says this himself.

**GitClear (211M lines analyzed).** Code churn/refactoring patterns shifted: refactoring-related activity fell from ~25% to under 10% of commits; copy/paste code rose from ~8% to 12%+ (**secondary**, vendor research). Interpretation: AI-assisted code is *added* more than *maintained* — the codebase grows faster than it's refactored. **Corroborated** (widely cited; vendor-sourced).

**Stack Overflow Developer Survey 2025.** 49,000 respondents: 84% AI tool adoption — but only 33% trust AI output vs 46% distrust; just 3% "highly trust" it; 66% report spending time fixing "almost-right" AI code (**meta**). The trust gap is the survey's headline: near-universal *use*, minority *trust*.

**UIUC et al. (Jan 2025, paper).** Copilot usage associated with increased code duplication (**paper**). **Corroborated.**

**The synthesis (Proposed).** The quantitative record converges: AI coding tools increase *code volume* and *perceived* speed while degrading *stability, trust, and maintainability signals*. The paradox dissolves if you distinguish *typing speed* (up) from *engineering throughput* (flat-to-down): software's bottleneck was never typing.

---

## 5. The security record — vibe-coded production is a vulnerability firehose

**The pattern.** AI-generated applications systematically ship with missing authorization, exposed secrets, and injection flaws — because the models optimize for *working demos*, not *threat models*. **Corroborated** across independent sources.

**Named incidents and studies.**
- **Moltbook leak (Wiz, Feb 2026):** 1.5M API tokens and 35K emails exposed; missing Supabase row-level security (RLS). Case study at github.com/boxed-dev/vibe-coding-security (moltbook-supabase-leak.md — **practitioner**/repo). **Corroborated** (Wiz research + repo).
- **CVE-2025-48757 (Lovable RLS):** disputed CVE around Lovable-generated apps' Supabase RLS configuration; advisories at github.com/pranava0x0/vibe-coding-security (**practitioner**/repo). Status *disputed* — recorded as such. **Corroborated** as disputed.
- **Escape.tech (Oct 2025):** scanned 5,600 AI-built ("vibe") apps; found 2,038 critical vulnerabilities (**secondary**, vendor research).
- **RedAccess (May 2026):** ~380,000 vibe-coded apps scanned; ~5,000 leaking sensitive data (**secondary**, vendor research).
- **Georgia Tech (Q1 2026):** 35 CVEs in March 2026 vs 6 in January — attributed to AI-generated code entering production (**secondary**, university-associated reporting).
- **Ox Security:** anti-patterns present in 80–100% of AI-generated code samples (**secondary**, vendor research).
- **SonarQube (2026):** 53% of AI-generated code "looks correct but hides defects" (**secondary**, vendor research).
- **Veracode (2026):** 44% of AI-assisted tasks introduce a known vulnerability (**secondary**, vendor research).
- **Apiiro:** 7,000 developers, 62,000 repos — 10,000+ new security findings per month by June 2025, a 10× six-month spike (**secondary**, vendor research).

**Confidence note.** Nearly all security statistics are vendor-sourced (Escape, RedAccess, Ox, SonarQube, Veracode, Apiiro sell security products). The *direction* is consistent across independent vendors, which raises confidence in the pattern; the *magnitudes* should be discounted for vendor incentive. The Moltbook case (Wiz) is the strongest single incident (named, technical, third-party researched).

**Engineering implication.** AI-generated code requires *adversarial* review by default: RLS/auth checks, secret scanning, and dependency auditing are not optional extras but the minimum viable review for generated code. The "70% problem" (§3) is sharpest here — security lives in the last 30%.

---

## 6. "Agentic engineering" — Karpathy's 2026 reframing

**The claim.** The "vibe coding" era (chat-and-paste) is over; the current era is "agentic engineering" — developers directing fleets of coding agents with specs, tests, and review. **Corroborated** as Karpathy's stated position.

**Source metadata.** Karpathy, Sequoia AI Ascent, 2026-04-30 (via thingshavehistory.com — **secondary**). The reframing matters because it concedes the vibe-coding critique: unsupervised generation doesn't produce production software; *supervised* agent fleets might. Whether "agentic engineering" escapes the productivity paradox (§4) is **Unknown** — no RCT-grade evidence located this pass.

---

## 7. Agent-skeptic manifestos and the "AI codebase bankruptcy" genre

**The genre.** A growing practitioner literature of *postmortems* on AI-built codebases: teams inheriting generated codebases they can't maintain, "bankruptcy" declarations (throw away the generated codebase and rewrite with understanding), and skeptic manifestos arguing that generated code is a liability multiplier (cf. file 01 §5: code is a liability — AI multiplies code volume, hence liability). **Community/practitioner** level — widely discussed on X, Reddit, HN; individual postmortems are first-hand but self-selected (people write postmortems about failures, not about the generated codebases quietly working).

**Social-platform traces captured this pass.** Zeitgeist captures (XMLs in /tmp, per context): a "vibe-coding logging-black-hole" reel (generated code with no observability — you can't debug what you can't see); "before/after LLMs" memes; Threads posts of agents building entire apps. These are **community** evidence of the cultural moment, not of engineering outcomes.

**The METR time-horizon counterpoint.** METR's "Measuring AI Ability to Complete Long Tasks" (Mar 2025, arXiv:2503.14499; Time Horizon 1.1, Jan 2026): task-completion time horizons doubling every ~7 months (2019–2024), accelerating to ~4.3 months post-2023; by May 2026, frontier models at ~12h (50% reliability) for human-expert task time. **Corroborated** (**paper** + dashboard). The tension with §4: *capability* horizons (what agents can do in evals) keep rising while *productivity* outcomes (what happens in real teams) stay flat-to-negative. Both can be true: agents are getting more capable at well-specified tasks while real work stays messy, interrupt-driven, and coordination-bound. Documented critiques of the horizon metric: clean self-contained tasks vs messy real work; human baselines from contractors 5–18× slower than repo maintainers; single-lab, single-scaffold-family.

---

## 8. Prompt-as-code controversies

**The debate.** Should prompts be versioned, tested, and reviewed like code ("prompt-as-code"), or is that ceremony that misunderstands the medium? **Community/practitioner** level — no consensus located.

**The positions.** For: prompts are load-bearing production artifacts; unversioned prompt changes are unreviewed production changes; the Chesterton's Fence logic (file 03 §2) applies — you can't safely edit what you don't understand, and prompts are the least-understood artifacts in the stack. Against: prompts are *intent specifications*, not code — versioning them like code imports software-engineering ceremony into a medium where evals, not unit tests, are the verification method; the iteration speed that makes prompts useful dies under code-review process. **Inferred** from practitioner discourse; recorded as an open controversy.

---

## Gaps in this file

- **Unknown:** No RCT-grade evidence on "agentic engineering" (2026) productivity — the METR RCT tested chat-era tools.
- **Unknown:** Security statistics are overwhelmingly vendor-sourced; independent academic measurement of AI-generated-code vulnerability rates is thin.
- **Unknown:** "AI codebase bankruptcy" postmortems are self-selected; no data on the base rate of generated codebases that survive.
- **Unknown:** The METR 2026 follow-up claims (frontier risk reports) were partially verified via secondary dashboards; primary METR 2026 publications not fully chased this pass.
