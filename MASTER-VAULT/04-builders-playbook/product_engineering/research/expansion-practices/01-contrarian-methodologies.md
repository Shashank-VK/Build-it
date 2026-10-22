# Fringe Engineering Practices — Contrarian Methodologies

**The Omniscient Resource Atlas · product_engineering / expansion-practices · Built 2026-10-10**
**Read-only research only.** Discovers, inspects, categorizes. Does not install, build, configure, rank, or recommend.

## How to read the labels

- **Verified** — read directly in the primary source during this pass.
- **Corroborated** — reported consistently by ≥2 independent sources, or once in a primary source not fetched this pass.
- **Inferred** — standard practitioner consensus the author is confident about but did not re-verify against a primary source this pass.
- **Proposed** — the author's synthesis; not a report of anyone's practice.
- **Unknown** — could not be established; listed as a gap.

**Evidence classes:** `primary` (author's own essay/blog/book), `secondary` (reporting about the practice), `practitioner` (first-hand write-up), `paper`, `forum` (HN/Reddit/X discussion), `meta` (surveys, literature reviews), `community` (anonymous practitioner lore, labeled as such).

---

## 1. Choose Boring Technology — Dan McKinley (2015)

**Claim.** Every company gets roughly three "innovation tokens" to spend on novel technology; spend them only where the business differentiates. Everything else should be boring (well-understood, widely deployed), because boring tech's failure modes are *known*, while shiny tech fails in unknown unknowns. **Verified**, primary.

**Source metadata.** Claim: "choose boring technology; innovation tokens". URL: `https://mcfunley.com/choose-boring-technology`. Source type: primary (author's blog). Author: Dan McKinley (then ex-Etsy principal engineer). Pub date: 2015 (updated 2015-07-27 for a talk). Accessed: 2026-10-10. Confidence: High.

**What the essay actually says (read in full this pass).** McKinley credits Kellan Elliott-McCrea's decision-making at Etsy. Sections: *Embrace Boredom* — about three innovation tokens per company, wallet tends to be overestimated; boring ≠ bad ("PHP is boring. Python is boring. Memcached is boring. Squid is boring. Cron is boring"); boringness means failure modes are well understood; known unknowns vs unknown unknowns (Rumsfeld framing, invoked with stated distaste). *Optimize Globally* — adding technology has company-wide scope; the baggage is "operations" and "cognitive overhead"; "the 'best' tool is the one that occupies the 'least worst' position for as many of your problems as possible"; long-term reliability costs "vastly exceed any inconveniences you encounter while building it." *Choose New Technology, Sometimes* — prescribed exercise: "consider how you would solve your immediate problem without adding anything new"; if the "problem" is that someone wants to use the technology, abort; write down exactly what makes the current stack prohibitively expensive; expect company-wide visibility for adding tech. *Just Ship* — polyglot freedom is "a naive definition of the problems at best, and motivated reasoning at worst."

**Concrete Etsy evidence inside the essay.** Footnote 1: early Etsy hired Python programmers, built a "pointless middle layer" that took years to amputate; meanwhile 90th-percentile search latency was about two minutes. Footnote 4: Etsy's activity feeds were built on the boring PHP/MySQL/Memcached/Gearman stack instead of Redis; "attention turned elsewhere for several years… activity feeds scaled up 20x while *nobody was watching it at all*" — the claimed long-term benefit of restraint. (First-hand, but self-reported; single company.)

**Corroboration.** The "innovation token" metaphor is one of the most-cited pieces of engineering wisdom online; summarized consistently across practitioner roundups (stvck.dev, refactoringenglish.com, namecheap.com essays list) — all consistent on the three-token framing. A 2026 longevity-analysis paper (lastsys.com) extended the argument: "boring" is necessary but not sufficient — what matters for decades is *replaceability*; spend tokens on domain, not infrastructure — unless infrastructure novelty is the product.

**Strongest counterargument (the beloved idea's counter-case).** Matt Layman — a self-described boring-technology practitioner — wrote a failed-SaaS postmortem (2019-12-18, mattlayman.com, hosted at github.com/mblayman/mattlayman.com): he *followed* the boring-tech playbook and the business still failed. Implication: tech-choice discipline is orthogonal to product-market fit; boring technology cannot save a product nobody wants. **Corroborated** (primary blog post; single case). A second boundary: "boring" ages — jQuery was the boring 2012 choice and is now a maintenance burden; COBOL was the boring 1985 choice (lastsys paper, **Inferred** argument, well-grounded in examples).

**When it applies / doesn't.** Applies: teams whose differentiator is not infrastructure; early-stage teams with limited operational capacity. Doesn't: database/infrastructure companies (McKinley explicitly carves these out); domains where the boring tool genuinely cannot meet the load (Etsy's own Solr carve-out for full-text faceted search).

**Engineering implication.** Gate new-tech adoption on an explicit written exercise (solve-without-new-tech + written cost-of-current-stack); track innovation-token spend per team as a forcing function.

---

## 2. "Agile is Dead" — Dave Thomas (2014) and the anti-agile polemics

**Claim.** The word "agile" has been subverted into a meaningless marketing term; the noun should be retired in favor of the adjective "agility." **Verified** (canonical URL, secondary quotation; primary page fetch blocked in this pass but the essay text is widely quoted verbatim).

**Source metadata.** Claim: "retire the word Agile". URL: `https://pragdave.me/blog/2014/03/04/time-to-kill-agile.html`. Source type: primary (author's blog). Author: Dave Thomas, Pragmatic Programmer co-author and Agile Manifesto signatory (Snowbird, Feb 2001). Pub date: 2014-03-04. Accessed: 2026-10-10. Confidence: High on the claim (exact wording corroborated across tdan.com, SD Times, HN item 21148413).

**Key quoted line (corroborated):** "The word 'agile' has been subverted to the point where it is effectively meaningless, and what passes for an agile community seems to be largely an arena for consultants and vendors to hawk services and products."

**The wider polemic timeline.**
- **Ron Jeffries** (2018, primary blog): "developers should abandon Agile" — Jeffries, also a manifesto signatory, coined/endorsed "Dark Agile/Dark Scrum" as the name for the corrupted form. **Corroborated** (tdan.com history of the polemic; cited consistently).
- **Kurt Cagle** (Forbes, 2019): "The End of Agile" — sparked a torrent of anti-agile developer comments on Slashdot. **Corroborated.**
- **Cliff Berg + 14** (2020): launched Agile2.net; book *Agile 2 — The Next Iteration of Agile* (2021) — an attempt to re-found rather than abandon. **Corroborated.**
- **Miriam Posner, UCLA** (2022): "Agile and the Long Crisis of Software." **Corroborated** (tdan.com).
- **2026 entrant:** Matthew Sullivan, "The Agile Zombie" (Medium, Sep 2026) — argues all obituaries attacked the merchandising, never the premise; attacks the premise instead. **Corroborated** (fetchable Medium piece; single-author opinion).

**Counterargument (what the polemics are usually really about).** The polemics almost universally distinguish the *word/industry* from the *practices*: Jeffries himself wrote that "the values and principles of the Manifesto… still offer the best way I know to build software." The HN practitioner consensus (item 21148413, **forum**) is that resentment is aimed at agile-as-management-control-instrument (story points as performance scoring), not at small steps / honest feedback / adjusting. Jack Skeels ("Why you should probably never say 'Agile'", 2020) argues the toolkit "wasn't made for you" — most organizations never understood empowerment-in-action and cling to "Random Agile."

**When it applies / doesn't.** The obituaries apply to branded, certification-driven agile-as-product. They do not apply to — and their authors explicitly exempt — the underlying loop (small steps, honest feedback, adjust).

**Engineering implication.** Treat "Agile™" (ceremonies, certifications, consultants) and "agility" (feedback loops, working software) as different objects; audit which one your org bought.

---

## 3. The monolith revival — from contrarian quote to conference default

**Claim.** The industry is consolidating back from microservices to modular monoliths; the "42% of teams abandoning microservices" viral statistic is fabricated. **Corroborated.**

**Source metadata.** Claim: monolith-reversal trend. Multiple sources; strongest named cases below. Accessed: 2026-10-10. Confidence: Medium-High on named cases; Low on aggregate statistics.

**Named, well-documented reversals.**
- **Amazon Prime Video VQA team (2023):** moved from a distributed serverless microservices design to a monolith; reported ~90% infrastructure cost reduction *and* improved scalability/resilience. Source: Marcin Kolny, Prime Video tech blog (`primevideotech.com`, **primary**, eng-blog). Caveat from practitioner Tony Mac (**corroborating**, secondary): one team, one workload — not an Amazon-wide repudiation.
- **Segment (2018–2020):** 100+ services consolidated back to one; well-documented company engineering writing. **Corroborated.**
- **Istio istiod (Mar 2020):** the service-mesh project itself merged its five control-plane services into one binary because one team operated them all. **Corroborated.**
- **InVision:** cited in the MDPI literature review as another reversion case. **Corroborated** via meta-review only.

**The fact-check that matters.** A 2026 fact-check (stepto.net) traced the viral "42% are abandoning microservices" claim: no such figure exists in the CNCF 2024 survey; the number appears fabricated/amplified by SEO content. A deep technical-design doc (github.com/vinayagrw/models-to-margins, **corroborating**, secondary analysis) independently concluded: microservices *adoption* plateaued at high levels and is not collapsing; the 2024–2026 wave of "we killed 47 microservices" posts is mostly anonymous SEO content with no named-company reversal at Segment/Prime-Video scale; an academic anchor exists — "From Microservice to Monolith" (MDPI Electronics, Apr 2024), a multivocal literature review cataloguing motives: cost, complexity, team size.

**The arc.** Kelsey Hightower's "monoliths are the future" (Jan 2020, contrarian quote) → analyst hedging (2023) → first-class framework support (Spring Modulith 1.0→2.1, Microsoft Aspire) → InfoQ "early majority" (Apr 2024) → by 2025 "right-size your boundaries" as settled conference wisdom (Sam Newman, 2025). Shopify and Meta run monoliths at scale. **Corroborated** (technical-design doc + InfoQ reporting).

**Strongest counterargument.** Microservices at the right scale are not discredited — Amazon still runs them massively; the reversal cases share a pattern: teams adopted microservices *before* they had the organizational scale that justifies them. The dev.to practitioner RFC (k0wsh1k_0x, Sep 2026, **practitioner**): "We failed because we borrowed an architecture built for a different sized team and assumed the benefits would show up automatically." A second practitioner (Devrim Ozcay, SpringOne 2024 talk write-up): 47 microservices → monolith, deploy time 40 min → 6 min, cloud costs −63% — but note the self-selection: people who succeeded with microservices don't write reversal posts.

**When it applies / doesn't.** Applies: teams < ~15 engineers with no per-service ownership; domains where services are thin wrappers over one Postgres. Doesn't: orgs with real team-scale boundaries; workloads with genuinely independent scaling needs (the Prime Video case is one team's workload, not Amazon).

**Engineering implication.** Architecture should follow team shape and actual traffic, not projected scale; modular monolith with clean internal boundaries is the default; split later on evidence.

---

## 4. #NoEstimates — Woody Zuill (Dec 2012)

**Claim.** Estimates of time/effort/cost are often waste or actively harmful because management misuses them and they're systematically inaccurate; teams should explore making decisions without them. **Corroborated.**

**Source metadata.** Claim: "#NoEstimates movement". URLs: `https://medium.com/backchannel/estimates-we-don-t-need-no-stinking-estimates-dcbddccbd3d4` (Scott Rosenberg, Backchannel, 2015-02-26); `http://zuill.us/WoodyZuill/2013/05/17/the-noestimates-hashtag/` (Zuill's own definition); `http://www.toddlittleweb.com/Papers/Estimates%20or%20NoEstimates%20IEEE%202016-01-22a.pdf` (Todd Little, IEEE). Author: Woody Zuill (software manager, Southern California irrigation manufacturer). Origin: tweet at 5:53 p.m., 2012-12-10: "#NoEstimates — I've added a litte more fuel to the fire" (spelling sic, **Corroborated** via Rosenberg). Accessed: 2026-10-10. Confidence: High on origin story; Medium on practice claims.

**Zuill's own definition (2013-05-17, corroborated):** "#NoEstimates is a hashtag for the topic of exploring alternatives to estimates [of time, effort, cost] for making decisions in software development. That is, ways to make decisions with 'No Estimates'." Not a methodology — a conversation topic. Vasco Duarte had been tweeting similar ideas under #EstWaste; Ron Jeffries dubbed it the "NoEstimates Movement."

**Evidence for/against.**
- **Todd Little's IEEE analysis** (data from 55 projects, 9 organizations, startups to multinationals): story-point velocity adds value over raw throughput when story sizes vary widely; with uniform story sizes, tracking throughput (just counting done items) is as good — no significant advantage to story points. Bucketing scheme (Fibonacci vs powers of 2) barely matters. This is the empirical core of the debate, and it *partially* supports the NoEstimates position: if you slice work small and uniform, estimation adds little. **Corroborated** (paper, single study).
- **Practitioner models:** Zuill's own context (mob programming at Hunter Industries, 2011–2012; pay-per-iteration contracting); Vasco Duarte / Troy Magennis on forecasting with Monte Carlo instead of estimation. **Practitioner.**
- **Opposition:** Software Planet Group ("The Fallacy of #NoEstimates"): customers need predictability; refusing to estimate serves developers, not customers. ÜberConf course notes: three camps — estimates misused by management (the NoEstimates camp), estimation as waste (Kanban camp), estimation as necessary for planning (Scrum camp). **Secondary.**

**When it applies / doesn't.** Applies: continuous-flow teams with small, uniform work items and high trust (pay-per-iteration contracting; long-lived product teams). Doesn't: fixed-scope/fixed-price contracting; organizations that need portfolio-level forecasting (where Monte-Carlo-over-throughput is the honest replacement, not "no forecasting").

**Engineering implication.** The actionable takeaway is not "never estimate" but "shrink work until estimation is unnecessary, and replace story points with throughput forecasting where forecasting is genuinely needed."

---

## 5. The "delete code" movement / best-code-is-no-code

**Claim.** Code is a liability, not an asset; the best code is no code; deletion should be a celebrated, routine practice. **Corroborated** as practitioner consensus; **Inferred** as to measurable outcomes.

**Lineage.** The slogan "the best code is no code" is community folklore (HN item 22033827, 2020 discussion, **forum**): one widely-upvoted framing — "code you should be writing should be things that are the core of what your business does… Everything else should be a commoditized product or open source infrastructure." The institutional ancestor is **YAGNI** (Extreme Programming). Jeff Atwood's 2007 "How To Become a Better Programmer by Not Programming" and Patrick McKenzie's 2011 "Don't Call Yourself a Programmer" are adjacent canon (stvck.dev roundup).

**Practitioner articulations.** Exception Not Found (2018, **practitioner**): "the logical extreme of my position is that **the best code is no code at all**… aim for less code than you previously had… every day." Dev.to "Delete All The Codes" (**practitioner**): code has carrying costs — library upgrades, language upgrades, security fixes, build maintenance; "code that does not exist… doesn't need any of the things." Frank Oge (Feb 2026, **practitioner**): "Your job as a software engineer is not to write code. Your job is to solve business problems." Practices: "zero net code" per feature; celebrating negative-LOC PRs; scheduled deletion reviews.

**The counter-case / boundary (Chesterton's Fence).** The deletion ethos collides directly with Chesterton's Fence (G.K. Chesterton, *The Thing*, 1929 — "The Drift from Domesticity"): never tear down a fence until you understand why it was put up. The principle is now formalized in multiple AI-era coding-skill repos as a mandatory pre-deletion protocol: git-blame archaeology, commit/ticket excavation, assume the previous developer was competent, and if no reason is findable, delete only behind a safety net (flag, revertable commit, canary). **Corroborated** (multiple independent skill repos + Brandon Bryson's 2020 Medium essay on legacy code). The tension is the point: "always be deleting" and "never delete what you don't understand" are *both* unwritten rules; the synthesis is *deletion with provenance*.

**When it applies / doesn't.** Applies: dead code, deprecated features, NIH infrastructure, speculative generality. Doesn't: load-bearing workarounds whose context is lost (delete behind a flag); compliance/audit-required code paths.

**Engineering implication.** Make deletion a first-class, reviewed activity (negative-LOC PRs celebrated; deletion records kept) but pair it with a Chesterton's Fence protocol so the movement doesn't become vandalism.

---

## 6. "Worse is Better" — Richard Gabriel (1989)

**Claim.** Software that is simple to implement (even if less "correct"/complete/consistent) wins over software that is "the right thing," because simplicity drives adoption, and adoption drives evolution. **Verified** (essay text, canonical URL).

**Source metadata.** URL: `https://www.dreamsongs.com/RiseOfWorseIsBetter.html`. Author: Richard P. Gabriel. Pub date: 1989 (essay "Lisp: Good News, Bad News, How to Win Big"; expanded in *The Rise of "Worse is Better"*). Accessed: 2026-10-10. Confidence: High.

**The argument (summary).** Gabriel contrasted MIT/Stanford ("the right thing": correctness, consistency, completeness prioritized; simplicity secondary) with New Jersey/Bell Labs ("worse is better": simplicity of implementation first, even at the cost of the other three). His claim: worse-is-better software spreads faster (easier to port, easier to understand), and its very spread creates the conditions for it to be improved — Unix and C beat Lisp systems not by being better but by being simpler to adopt. The essay is a deliberate provocation, not a controlled study — treat as **primary** philosophical argument, not empirical evidence.

**Corroboration / afterlife.** The essay is the canonical citation for every "simplicity beats correctness" debate since: it underwrites "choose boring technology," the "worse is better" defense of PHP/JavaScript/Go pragmatism, and the anti-perfectionist wing of the craftsmanship debate. Gabriel himself later wrote follow-ups ("Worse Is Better Is Worse," 2000s) complicating the thesis. **Corroborated.**

**Counterargument.** The thesis is unfalsifiable as stated (survivors are declared "worse-is-better winners" retroactively); critics note it can be used to justify shipping sloppy software. The strongest steelman against it: in safety-critical, correctness-critical, or protocol domains, "the right thing" demonstrably wins (e.g., cryptographic protocols, aviation software) — adoption dynamics don't apply where failure is catastrophic.

**When it applies / doesn't.** Applies: platform/ecosystem competition, developer tools, network-effect software. Doesn't: safety-critical systems, security protocols, domains where a defect costs more than adoption gains.

---

## 7. Grug-brained developer — Carson Gross (2022)

**Claim.** Experienced developers should deliberately think like "grug" — a simple [REDACTED] — favoring boring, obvious, simple solutions over clever abstractions; complexity is the enemy. **Verified** (site text; grugbrain.dev).

**Source metadata.** URL: `https://grugbrain.dev/`. Author: Carson Gross (creator of htmx). Pub date: 2022. Accessed: 2026-10-10. Confidence: High on existence/claims (the site is the primary artifact; widely linked, including Theo video references per context notes).

**The argument (summary).** Written in [REDACTED] voice as a deliberate rhetorical device: complexity very bad; say what mean; big brain take too many big words. Substantive points beneath the schtick: prefer duplication over the wrong abstraction; avoid clever type-system gymnastics; "grug wonder: why big brain make simple thing complex?"; test-driven development and refactoring are grug-approved; most "best practices" debates are big-brain status games. It is the 2020s folk-art restatement of McKinley + YAGNI + "worse is better" for the post-framework-exhaustion era.

**Reception.** Enormously shared; became shorthand ("grug-brained") for deliberate simplicity. Criticism (**forum**, community): the [REDACTED] voice can be used to dismiss legitimate complexity (distributed systems, type safety) as "big-brain" showing off; it risks anti-intellectualism as an aesthetic.

**Engineering implication.** Useful as a code-review heuristic ("would grug understand this?") but not as an architecture principle — some problems are irreducibly complex and grug-braining them produces the wrong simplicity.

---

## 8. No-meetings experiments — Shopify's calendar purge (2023)

**Claim.** Deleting recurring meetings en masse recovers large amounts of maker time; meetings are a bug to be fixed. **Corroborated.**

**Source metadata.** Event: 2023-01-03, Shopify deleted ~12,000 recurring meetings with 3+ attendees, recovering ~76,500 hours of meeting time. Announcer: Kaz Nejatian (COO); endorsed by CEO Tobi Lütke. Policy additions: no-meeting Wednesdays; meetings >50 people only on Thursdays 11am–5pm; "meetings are a bug." Sources: meetburn.app retrospective; Fast Company ("this is what happened when we canceled all meetings", fastcompany.com/90888605/shopify-exec-this-is-what-happened-when-we-canceled-all-meetings). Accessed: 2026-10-10. Confidence: High on the event; Medium on lasting effects (follow-up reporting is thinner).

**Aftermath reporting (corroborated, thinner).** Shopify reported the purge forced intentionality about which meetings returned; practitioners widely copied the "meeting cost calculator" idea. Counter-evidence: no public controlled study shows sustained productivity gains; coordination costs can reappear as ad-hoc interruptions (the classic "no-meetings → more Slack" substitution, **community** observation, **Inferred**).

**When it applies / doesn't.** Applies: orgs with meeting sprawl and strong async-writing culture. Doesn't: orgs where meetings are the actual decision mechanism and no written replacement exists — deleting them deletes decisions, not overhead.

---

## 9. Working Backwards (PR/FAQ) — Amazon (2004–)

**Claim.** Writing a future press release + FAQ *before* building forces customer-centric clarity and kills weak ideas cheaply. **Corroborated.**

**Source metadata.** Origin: Jeff Bezos, internal email June 2004 ("no more PowerPoint"); the six-page narrative memo culture. Popularized internally 2004–2005; externally by Ian McAllister (Quora) and by Colin Bryar & Bill Carr, *Working Backwards* (St. Martin's Press, 2021) — Bryar was Bezos's chief of staff 2003–2004; Carr launched Prime Video. Public artifacts: AWS Executive Insights whitepaper; re:Invent 2023 talk "Define your next $1B opportunity"; aboutamazon.com insider-culture page. Accessed: 2026-10-10. Confidence: High on the practice's existence and mechanics; **Unknown** on causal effectiveness (no controlled study; "most major products since 2004 came through it" is survivorship — it counts shipped launches, not killed proposals).

**Mechanics (verified across sources).** One-page mock press release dated at a future launch, written before budget/team/code; then FAQ in two halves — customer questions first, then internal (viability, resources, risk). Five questions: who is the customer; what is the problem/opportunity; what is the solution and top benefit; how do we describe the experience; how do we test and measure. Forcing function: executives ask "so what?" — if not meaningfully better/faster/easier/cheaper than alternatives, don't build.

**Counterargument / failure modes.** Practitioner Cedric Chin (Commoncog, "Putting Amazon's PR/FAQ to Practice") names real failure modes: customer-uncertainty assumption (the doc assumes you know the customer; early-stage teams often don't), over-scoping, emotional resistance. Adjacent academic anchor for "writing forces thinking": Bangert-Drowns et al. meta-analysis (2004) — small positive effect of writing-to-learn interventions; *adjacent*, not a test of PR/FAQ. Risk: the document becomes theater — a beautifully written fiction that substitutes for customer contact (the "demo is the spec" tension, see file 03).

**When it applies / doesn't.** Applies: new-product bets with identifiable customers; orgs that can say no. Doesn't: pure research/exploration; teams without customer access (the doc then just encodes guesses).

---

## 10. "Disagree and commit" — Bezos (2016 letter), via Andy Grove

**Claim.** Once a decision is made, commit wholly even if you disagreed; voicing dissent then committing beats consensus-seeking for decision velocity. **Corroborated.**

**Source metadata.** Popularized: Jeff Bezos, 2016 shareholder letter, section "High-Velocity Decision Making": "If you have conviction on a particular direction, even though there's no consensus, it's helpful to say, 'Look, I know we disagree on this but will you gamble with me on it? Disagree and commit?'" Bezos's example: greenlighting an Amazon Studios original he doubted — "I disagree and commit and hope it becomes the most watched thing we've ever made." Codified as part of the "Have Backbone" leadership principle. Lineage: attributed to Andy Grove's Intel culture (per Grove biographer Richard Tedlow via Inc./Business Insider reporting) — "once you do [decide], create a strategy vector." Meta CTO Andrew Bosworth revived it as an ultimatum in 2025 ("disagree and commit or leave"). Accessed: 2026-10-10. Confidence: High on Bezos's articulation; Medium on the Grove lineage (secondhand via biographer).

**Boundary / misuse.** The phrase degrades into a silencing tool when power is asymmetric — Bosworth's 2025 usage ("commit or leave") is the canonical example of the failure mode: disagree-and-commit only works where dissent was genuinely heard first. **Corroborated** (2025 reporting).

**When it applies / doesn't.** Applies: reversible (Type-2) decisions where speed beats certainty. Doesn't: irreversible decisions (Bezos's own Type-1/Type-2 distinction); situations where dissenters' concerns predict the failure mode and get ignored.

---

## 11. "Nobody ever got fired for picking Java" — Alex Payne (2013)

**Claim.** Technology conservatism is career-risk management: safe, defensible choices protect the chooser even when they're wrong. **Corroborated.**

**Source metadata.** Author: Alex Payne (early Twitter engineer). Pub date: 2013 (essay widely circulated; exact URL not re-fetched this pass). Accessed: 2026-10-10. Confidence: Medium (well-attested in practitioner canon; primary page not opened this pass).

**Why it matters.** It's the cynical twin of "choose boring technology": McKinley argues boring tech is *technically* superior (known failure modes); Payne observes it's *politically* superior (nobody blames you for the consensus choice). The fringe insight: many "boring technology" adoptions are actually blame-avoidance, not engineering judgment — which is why the boring choice sometimes persists past its technical justification (cf. the COBOL/jQuery aging problem in §1).

---

## 12. "Move fast and break things" → retired (Facebook, 2014)

**Claim.** Facebook's famous motto was retired in 2014, replaced by "Move fast with stable infrastructure" — evidence that even the canonical move-fast shop hit the limits of the ethos. **Corroborated.**

**Context.** The motto (attributed to Zuckerberg, 2009–2014 era) embodied the extreme-practice wing of shipping culture. Its retirement coincided with Facebook's scale making breakage catastrophically expensive — the boundary condition made visible: "move fast and break things" works when the cost of breakage is low and reversibility is high; at planetary scale with ads revenue on the line, stability becomes the binding constraint. Pairs with the error-budget concept (file 04): the mature form of "move fast" is *budgeted* risk-taking, not unbounded risk-taking.

---

## Gaps in this file

- **Unknown:** Primary fetch of Dave Thomas's 2014 essay was not completed this pass (URL known, page not opened); claims rest on corroborated quotation. Ron Jeffries's 2018 "abandon Agile" post likewise corroborated, not fetched.
- **Unknown:** Alex Payne's 2013 essay URL not re-verified this pass.
- **Unknown:** No controlled studies found for Working Backwards effectiveness; all evidence is insider testimony + adjacent research.
