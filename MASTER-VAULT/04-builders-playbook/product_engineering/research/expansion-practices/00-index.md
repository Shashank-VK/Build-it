# Expansion Practices — The Full Menagerie (Index)

**The Omniscient Resource Atlas · product_engineering / expansion-practices · Built 2026-10-10**
One line per practice: the claim + the verdict. Detail lives in the theme files (01–07); metadata lives in `evidence-register.md`.

## Contrarian methodologies (→ 01-contrarian-methodologies.md)

1. **Choose Boring Technology** (McKinley, 2015) — ~3 innovation tokens per company; spend on differentiators only. **Verdict: Verified in primary; the strongest tech-choice heuristic in the corpus, with a real counter-case (Layman's failed SaaS).**
2. **"Agile is Dead"** (Dave Thomas, 2014; Jeffries 2018; Cagle 2019; Agile2 2020) — retire the noun, keep the adjective. **Verdict: Corroborated; the obituaries attack the merchandising, and their authors exempt the actual practices.**
3. **Monolith revival** (Prime Video −90%, Segment, Istio, InVision) — the industry is right-sizing back from microservices. **Verdict: Named cases corroborated; the viral "42%" statistic is fabricated — discourse outran evidence.**
4. **#NoEstimates** (Zuill, Dec 2012) — explore decisions without time/effort/cost estimates. **Verdict: Corroborated; Todd Little's IEEE data (55 projects) partially supports it — throughput beats story points for uniform work.**
5. **Delete-code movement** — code is a liability; best code is no code. **Verdict: Practitioner consensus; must be paired with Chesterton's Fence or it becomes vandalism.**
6. **"Worse is Better"** (Gabriel, 1989) — simplicity of implementation beats correctness for adoption. **Verdict: Verified essay; powerful for platforms, unfalsifiable as stated, inapplicable to safety-critical domains.**
7. **Grug-brained developer** (Carson Gross, 2022) — deliberately simple thinking beats clever abstraction. **Verdict: Verified; useful code-review heuristic, not an architecture principle.**
8. **No-meetings experiments** (Shopify purge, Jan 2023: 12,000 meetings, 76,500 hrs) — meetings are a bug. **Verdict: Event corroborated; lasting-effect evidence thin; coordination cost reappears as chat.**
9. **Working Backwards / PR-FAQ** (Amazon, 2004–) — write the future press release before building. **Verdict: Mechanics corroborated; effectiveness unproven (survivorship); real failure modes documented by practitioners.**
10. **"Disagree and commit"** (Bezos 2016 letter; via Andy Grove) — voice dissent, then commit wholly. **Verdict: Corroborated; degrades into a silencing tool under power asymmetry (Bosworth 2025).**
11. **"Nobody ever got fired for picking Java"** (Alex Payne, 2013) — boring choices are career-risk management. **Verdict: Corroborated; the cynical twin of Choose Boring Technology — explains why boring choices outlive their justification.**
12. **"Move fast and break things" retired** (Facebook, 2014) — even the canonical move-fast shop hit the limit. **Verdict: Corroborated; the mature form is budgeted risk (error budgets).**

## Abandoned approaches (→ 02-abandoned-approaches.md)

13. **SAFe horror stories** (scaled-agile-facts repo; Fitbit) — SAFe experienced as rebranded waterfall. **Verdict: Pattern corroborated across independent accounts; single-company stories are practitioner-reported.**
14. **Microservices reversions** — Prime Video, Segment, InVision, Istio consolidated back. **Verdict: Corroborated; the failure is premature distribution, not distribution.**
15. **"You build it, you run it" → burnout** (Vogels, ACM Queue 2006) — cargo-culted without a platform, it burns teams out; the industry answer was platform engineering + Team Topologies' cognitive-load framing. **Verdict: Quote verified; misuse pattern corroborated.**
16. **10x engineer myth** (Sackman 1968 → Nichols debunk → Shanley essay) — pop version is a myth; task-level variation is real, team-level attribution is the fundamental attribution error. **Verdict: Lineage corroborated; DORA shows system factors dominate.**
17. **Open-plan offices** (Bernstein & Turban, 2018) — face-to-face interaction *dropped* ~70%; email +67%, IM +75%. **Verdict: Peer-reviewed; the opposite of the stated purpose.**
18. **Remote-work bans** (Yahoo 2013; IBM 2017) — both justified as collaboration; neither produced documented gains; both read as cost-cutting/control. **Verdict: Events corroborated; "collaboration" justifications should be treated as hypotheses, not truths.**
19. **Holacracy** (Zappos 2013–2018, ~14% took severance; Medium dropped it 2016) — power didn't disappear, it went informal. **Verdict: Corroborated; fails as top-down CEO philosophy project.**
20. **Stack ranking** (Microsoft abandoned Nov 2013; Amazon OLR dropped 2016; creeping back 2025) — incentivizes sabotage-by-inaction. **Verdict: Abandonment corroborated; the 2025 return is single-source.**
21. **Google 20% time** — died ~2013 by incentive incompatibility, not decree; Area 120 (2016) was the successor, cut back 2022. **Verdict: Timeline corroborated; lesson: a perk the promo process punishes is not a perk.**
22. **Unlimited vacation** (Namely 2018: 13 vs 15 days; Deel 2025: culture-dependent) — policy doesn't determine time off; culture does. **Verdict: Corroborated; without norms it's a cost-saving measure in a perk costume.**
23. **Spotify model** — a 2012 snapshot, never a framework; Spotify itself moved on. **Verdict: Corroborated by Kniberg's own words; copying it is cargo-culting.**

## Unwritten rules (→ 03-unwritten-rules.md)

24. **"Never rewrite from scratch"** (Spolsky, 2000; Netscape 6) — but DHH and Herb Caudill's 6 stories show rewrites can work. **Verdict: Rule corroborated; the real rule is "never *big-bang* rewrite" — strangler migrations succeed.**
25. **"Always be deleting" vs. Chesterton's Fence** (1929) — the mature rule is *deletion with provenance*. **Verdict: Both corroborated; the tension is the point.**
26. **"The demo is the spec"** (Apple) — features developed against working demos reviewed by leadership. **Verdict: Corroborated via ex-employee accounts; no first-party Apple documentation (expected).**
27. **Resume-Driven Development** — choosing tech for resumes, not systems; now a peer-reviewed paper (arXiv:2101.12703, n=591: 60% of hiring influenced by trends, 82% of devs believe trendiness aids hiring). **Verdict: Empirically corroborated; the pathology is selection on trendiness *instead of* fit.**
28. **Conway's Law** (1968) — org communication structures copy into designs; MIT/Harvard mirroring hypothesis + Vista org-metrics study (86.2% precision) support it; Colfer & Baldwin (142 studies) bound it — prevalent, not universal. **Verdict: Corroborated with a real boundary; the Inverse Conway Maneuver is practitioner experience, not science.**
29. **"Hallway-driven development"** and folk methodologies — diagnostic slang for dysfunctions official methods don't name. **Verdict: Community observation; origin unknown.**
30. **"Programming Sucks"** (Welch, 2014) — the emotional charter of cynical resilience. **Verdict: Verified essay; pairs against the craftsmanship literature.**

## Extreme practices (→ 04-extreme-practices.md)

31. **Trunk-based development at scale** (Google: 2B-line monorepo, ~16k commits/day) — DORA-predictive of elite performance, but only as a bundle (flags, fast CI, tests). **Verdict: Corroborated; the branch policy without the bundle is the failure mode.**
32. **Continuous deployment at scale** (Flickr 10+/day 2009 → DevOpsDays; Etsy ~50/day; Amazon every 11.6s, 2011) — a socio-technical bundle, not a cadence. **Verdict: Corroborated; fails where rollback is impossible.**
33. **Chaos engineering** (Netflix Simian Army, 2011; survived the Sept 2014 AWS 10% reboot) — continuous automated fault injection. **Verdict: Corroborated; without observability maturity it's just breaking production.**
34. **GameDays** (Jesse Robbins, Amazon ~2003) — the human complement to chaos: training the socio-technical system. **Verdict: Corroborated via first-person retrospective.**
35. **Blameless postmortems** (Allspaw, Etsy 2012; Dekker/Woods roots; SRE book ch. 15) — second-story thinking. **Verdict: Corroborated; degrades into absolution theater without tracked remediation.**
36. **Error budgets** (Google SRE book, 2016) — reliability as a spendable resource; the mature form of "move fast." **Verdict: Corroborated; fails where SLOs are gamed or unenforced.**
37. **Feature flags** (Fowler/Hodgson taxonomy, 2017: release/experiment/ops/permissioning) — decouple deploy from release. **Verdict: Corroborated; flag debt is the failure mode — flags are inventory with carrying costs.**
38. **On-call compensation** — paging is labor; Google's 50% ops-load cap is the documented standard. **Verdict: Practitioner consensus; no systematic survey located.**

## Indie / bootstrapper wisdom (→ 05-indie-bootstrapper-wisdom.md)

39. **"Do Things That Don't Scale"** (Graham, 2013) — unscalable concierge work early; scale what breaks. **Verdict: Verified essay; the philosophical root of the whole indie lineage.**
40. **Maker's vs. Manager's Schedule** (Graham, 2009) — one meeting destroys a maker's day; the conflict is structural. **Verdict: Verified; changed company policies, not just habits.**
41. **Shape Up** (Basecamp/Singer, 2019) — appetite over estimates, bets over backlogs, six-week cycles. **Verdict: Verified in primary; optimized for small senior teams that can say no; no controlled studies.**
42. **Boring-stack manifesto** (boringstackoverflow) — monolith on a $5 VPS; Kubernetes costs land day one, benefits scale with fleet size. **Verdict: Movement corroborated; outcomes anecdotal; needs an honest exit ramp.**
43. **Single-binary deployments** (Go + SQLite + go:embed) — one file to build, ship, roll back. **Verdict: Pattern corroborated; bets the app fits in one process.**
44. **SQLite at scale** — far more capable than its reputation (Litestream/Turso remove the SPOF objection); single-writer is the real boundary. **Verdict: Technically corroborated; wildest anecdotes are forum-reported.**
45. **Indie synthesis** — defer every scaling decision until the problem is actual; the discipline is in the trigger condition. **Verdict: Proposed synthesis.**

## AI-era fringe (→ 06-ai-era-fringe.md)

46. **"Vibe coding"** (Karpathy, Feb 2025) — coined for *throwaway weekend projects*; the qualifier was erased in retelling. **Verdict: Coinage verified; the term now means three different things — track which one a claim uses.**
47. **YC W25: 25% of codebases 95% AI-generated** (Friedman via TechCrunch, Mar 2025; Tan caveat: early-stage) — existence proof at seed stage, misused beyond it. **Verdict: Corroborated with caveats; self-reported, unaudited.**
48. **The "70% Problem"** (Osmani, late 2024, Substack) — AI gets you 70% fast; the last 30% takes as long as ever. **Verdict: Corroborated as practitioner model; the number is illustrative, not measured.**
49. **The productivity paradox** — METR RCT (16 devs, −19% slower, 39pt perception gap); DORA 2024 (39k resp: +25pp AI → −7.2% stability); Uplevel (800 devs: +41% bugs, no throughput gain); GitClear (refactoring 25%→<10%); Stack Overflow 2025 (84% use, 46% distrust). **Verdict: Convergent — AI raises code volume and perceived speed while degrading stability/trust signals; typing was never the bottleneck.**
50. **The security record** — Moltbook (Wiz, Feb 2026: 1.5M tokens, missing RLS); Escape.tech (2,038 critical vulns in 5,600 apps); RedAccess (~5k of 380k apps leaking); SonarQube 53% "looks right, hides defects"; Veracode 44% introduce known vulns. **Verdict: Pattern corroborated across independent vendors; magnitudes discounted for vendor incentive; security lives in the last 30%.**
51. **"Agentic engineering"** (Karpathy, Apr 2026) — the vibe-coding era is over; supervised agent fleets are the new claim. **Verdict: Position corroborated; no RCT-grade evidence it escapes the paradox.**
52. **AI codebase bankruptcies & agent-skeptic manifestos** — postmortems of unmaintainable generated codebases; self-selected. **Verdict: Community/practitioner; base rate unknown.**
53. **Prompt-as-code controversy** — version prompts like code vs. evals-not-unit-tests. **Verdict: Open controversy; no consensus located.**

## Craft culture (→ 07-craft-culture.md)

54. **Software Craftsmanship Manifesto** (2009; from Uncle Bob's Agile 2008 keynote) — well-crafted software, steadily adding value, community of professionals, productive partnerships. **Verdict: Text verified; "well-crafted" resists operationalization — the permanent argument with "good enough."**
55. **Staff Engineer archetypes** (Larson, 2021: Tech Lead, Architect, Solver, Right Hand) — mismatches explain staff-level failures. **Verdict: Taxonomy corroborated as synthesis; no empirical validation; big-tech-shaped.**
56. **Seniority collapse** (Stanford Digital Economy Lab 2025: devs 22–25 employment −20% from 2022 peak; 30+ grew) — the numbers are real; AI as cause is contested (vs. rate-hike hiring correction). **Verdict: Employment data high-confidence; causal attribution unknown — and it's an existential question for craft transmission.**
57. **Craftsmanship vs. "good enough"** — both right about different code lifetimes; match craft investment to expected lifetime. **Verdict: Proposed synthesis.**

---

## How to use this index

- Each numbered item maps to its theme file for full sourcing, counterarguments, and boundary conditions.
- `evidence-register.md` carries per-finding metadata (claim, URL, source type, author/org, pub date, accessed date, confidence, corroboration, contradictions, engineering implication).
- Labels: **Verified** = read in primary this pass; **Corroborated** = ≥2 independent sources; **Inferred** = confident consensus, not re-verified; **Proposed** = author synthesis; **Unknown** = gap.
