# Meta — Forensic Supplement

**Workstream:** forensics · **Researched:** 2026-10-10 · Read-only research; no installation, building, ranking, or recommendation.
**Supplements:** `../cases-hyperscale/03-meta.md` (Sapling monorepo, 2021 BGP outage, Reality Labs losses, AI-coding targets). This file reconstructs the developer-workflow machine (Phabricator diff stacks, review-time engineering, bootcamp), extends the failure record, and audits "move fast" against the metaverse write-off and the layoff-era culture accounts.
**Confidence key:** **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** (as before). All sources accessed 2026-10-10.

---

## PART 1 — REVERSE-ENGINEER: how the machine actually works

### The diff machine: Phabricator stacks, review-time engineering

**MT-R1 — Stacked diffs as the unit of work.** Meta's developer-workflow documentation (primary, 2022) describes the distinctive practice: instead of submitting a single diff, engineers submit **stacks of diffs** — "a series of changes, each standing alone but also building on the previous changes" — so reviewers discuss each change in isolation and refactoring is separated from functional changes. The flow: commit → Phabricator ("Phab"), Meta's CI-and-review tool, which displays comments and test plan, runs the relevant tests (identified by **predictive test selection** — an ML model choosing which tests have the highest signal, since running all tests on every change is "infeasible"), shows results inline, and lands diffs on "Ship It" approval. Language-specific static analysis runs as part of the flow (e.g., RacerD for Java concurrency bugs); mobile apps get Sapienz automated UI testing. · **Verified (primary-technical)** · Source: developers.facebook.com/blog/post/2022/11/15/meta-developers-workflow-exploring-tools-used-to-code/ (Meta developer blog, 2022-11). · *Engineering implication: Meta's review unit is the stack, not the PR — the tooling (predictive test selection, stacked review UI) exists because monorepo scale makes GitHub-style PR CI economically infeasible.*

**MT-R2 — Review latency as an engineered metric.** A Meta engineering post ("Move faster, wait less: Improving code review time," 2022-11) shows the company treats **Time In Review** (goal metric) and **Eyeball Time** (guardrail) as product metrics and runs **experiments on its own internal tools** — including "Next Reviewable Diff," an ML-ranked review queue inspired by streaming-service binge mechanics, which produced a 17% increase in review actions/day (44% for flow users). · **Verified (primary-technical)** · Source: engineering.fb.com/2022/11/16/culture/meta-code-review-time-improving/ (2022-11). · *Implication: Meta dogfoods experimentation on the developer experience itself — the review queue is optimized like a consumer product.*

**MT-R3 — Bootcamp as cultural firmware.** New engineers go through a **six-week Bootcamp**: hired as engineers, not into teams; exposed to multiple engineering areas through real code; then matched to growing teams. VentureBeat's account (citing Meta's Tom Occhino-era framing via David Recordon): "We expect new hires to... move fast, to be open, to focus on impact. Part of their job is to question whether they're doing that." Every ~18 months engineers may take a month to hack around and contemplate switching fields. · **Corroborated (press on company statements)** · Source: venturebeat.com/dev/facebook-bootcamp. · *Forensic note: Bootcamp is the onboarding mechanism for the "move fast" culture — it selects for people who internalize the values before they're placed. Contrast with the 2026 layoffs-era accounts (MT-D2).*

**MT-R4 — Practitioner corroboration of the "move fast" tooling culture.** HN thread on Meta developer tools (news.ycombinator.com/item?id=36504554, 2023): ex-Meta engineers describe the freedom to revert previously committed code with the implicit responsibility model — "Nothing at FB is someone else's problem"; reviewers added to revert-diff reviews; candid, ego-light code review. One: "Moving fast was so damn cool... the open-ness of it all." · **Corroborated (first-hand-practitioner, unverifiable)** · Source: HN thread (2023). · *Note the tense: past-tense nostalgia — "used to say." See D2.*

### Decision flow: how the metaverse got decided

**MT-R5 — The $80B decision that bypassed product-market feedback.** In late 2021 Zuckerberg rebranded Facebook → Meta and committed the company to the metaverse; Reality Labs accumulated ~$80B in operating losses since 2020 ($6B in Q4 2025 alone); Horizon Worlds never passed a few hundred thousand MAU (WSJ, Oct 2022: <200,000 MAU from internal docs); in 2026 Meta cut ~10% of Reality Labs, shuttered three VR studios, discontinued metaverse-for-work, and announced Horizon Worlds' shutdown on Quest (June 15, 2026) — then **reversed the shutdown decision after public backlash**, keeping it alive. Meanwhile Ray-Ban Meta smart glasses became the breakout: ~2M units of the new generation + 7M by EssilorLuxottica, sales doubled Q2 2026. · **Corroborated (press)** · Sources: economictimes.indiatimes.com (2026-03); technewsvision.co.uk / onlinetechguru.co.uk (2026-09); tradersunion.com (2026-03). · *Forensic implication: the "experiment and iterate" company (MT-R2) placed a single $80B top-down bet with no kill signal for four years — and when the kill signal arrived, it was partially reversed by PR backlash, not by data. The decision machinery documented in Part 1 of the sibling simply did not govern this bet.*

**MT-R6 — Builders wouldn't live in it.** Per digit.in's retrospective (2026-03, citing the birthday-party footage and internal accounts): when Meta leadership required employees to spend time in Horizon Worlds, **some developers automated the whole thing** — launching via Android command over USB, taping the headset's proximity sensor so it registered as worn, without ever entering the world. "The people logging the most hours had never been inside." · **Corroborated (press on internal accounts)** · Source: digit.in/features/general/mark-zuckerberg-shuts-metaverse (2026-03). · *Implication: the dogfooding mechanism that validates Meta's developer tools (MT-R2) failed completely for the flagship consumer bet — the telemetry said "engaged," the humans were cheating the sensor.*

---

## PART 2 — POSTMORTEM: the public failure record (beyond the sibling file)

Sibling covered: Oct 2021 BGP outage, Reality Labs losses, Libra/Diem, Facebook Home. **New:**

**MT-P1 — Horizon Worlds shutdown announced, then un-shutdown (2026).** Announced closure on Quest by June 15, 2026 (app removed from Quest Store by end of March 2026; users to lose saved assets and avatar credits); after public backlash, Meta **decided to keep Horizon Worlds going**. · Corroborated (technewsvision.co.uk, 2026-09). · *Forensic note: a product-kill reversed by backlash is not iteration — it's governance by PR.*

**MT-P2 — Ray-Ban Stories flop (2021) → Ray-Ban Meta success (2023+).** The first-generation Stories: "ninety percent of owners left the glasses to rot in their drawers" — a bona fide flop; the second generation (better cameras) sold ~2M units "surprising even Zuckerberg." · Corroborated (technewsvision.co.uk, 2026-09). · *Implication: the AI-glasses success was an iteration story the metaverse wasn't — small bets, fast hardware learning.*

**MT-P3 — The 2026 AI-coding-target regime and its discontents.** Internal documents (via Business Insider, reported by PeopleMatters, 2026-03): team-level targets of 65% of creation-org engineers writing >75% of code with AI tools in H1 2026; 55% of code changes in central product teams AI-agent-supported; "AI-driven impact" central to performance from 2026 (HR head Janelle Gale). Counter-evidence: ex-engineer Jeremy Bernier's (deleted) X post calling Meta "the most toxic company I've worked for" after the 10% layoffs — "Squid Game" stack-ranking under AI pressure (Analytics Insight, 2026-05). Official counter: spokesperson said performance rewards AI-driven *outcomes*, not usage. · **Press/first-hand, partially unverifiable** (sibling F9/F21). · *This is the live experiment — verdict not yet in; record both sides.*

**MT-P4 — WhatsApp/Instagram/Facebook outages 2024–2025.** No new primary evidence captured this pass beyond the sibling's 2021 record — **Unknown this pass** (flagged as a follow-up, not as a clean record).

---

## PART 3 — DISMANTLE: narratives vs evidence

### D1 — "We experiment and iterate" vs the $80B top-down bet
- **Official narrative:** Meta's strength is experimental, data-driven iteration (growth team lore, MT-R2's internal-tools experiments).
- **Contradiction:** The defining strategic act of the Zuckerberg era — the 2021 rename and ~$80B Reality Labs investment — was a CEO conviction bet that **never faced the experiment machinery**: internal docs showed <200k MAU in Oct 2022 and investment continued for three more years; the eventual Horizon Worlds kill was reversed by backlash, not data. Meanwhile the actual hit (AI glasses) came from iterating small hardware bets — the very mechanism the metaverse bet bypassed.
- **Forensic verdict:** The experimentation culture is real at the *product* level (Verified, MT-R1/R2) and absent at the *strategy* level (Corroborated, MT-R5/R6). Meta's machine optimizes features brilliantly and strategies barely at all. · **Verdict: narrative split by altitude — true for diffs, false for bets.**

### D2 — "Move fast" vs the layoff-era culture accounts
- **Official narrative:** Hacker culture — openness, speed, "nothing is someone else's problem," Bootcamp firmware (MT-R3), ex-engineer nostalgia (MT-R4).
- **Contradiction:** The 2026 accounts describe survivalist stack-ranking: a since-deleted X post by ex-engineer Jeremy Bernier after the 10% layoffs called Meta "the most toxic company I've worked for," describing "Squid Game" dynamics under AI-pressure performance systems (Analytics Insight, 2026-05). Official line: performance rewards AI-driven outcomes, not usage (sibling F9). The HN nostalgia is past-tense — "they *used to* say."
- **Forensic verdict:** The "move fast" culture is attested by multiple ex-engineers as a real past state; its current state is disputed by current-era accounts. The AI-coding targets (55–75% usage mandates) are the exact inversion of the old bottom-up ethos — mandated adoption is not hacker culture. · **Verdict: narrative is a period piece — Verified for 2012–2021, contested for 2025–2026.**

### D3 — Open-source as virtue vs open-source as leverage
- **Official narrative:** Meta donates React/PyTorch to foundations out of ecosystem stewardship (sibling F2).
- **Counter-reading (evidence-grounded, not cynical):** The React Foundation move (announced Oct 2025, completed ~Feb 2026) came *after* the 2017 BSD+Patents licensing fight in which the Apache Software Foundation barred React — donation followed a trust crisis, not just generosity. Donating industry-critical infra to neutral foundations de-risks *Meta's own* dependence on single-vendor governance — including itself. The PyTorch precedent (2022) similarly externalized governance cost while Meta retained influence via founding membership.
- **Forensic verdict:** Open-sourcing is both genuine ecosystem contribution *and* strategic de-risking; the "virtue" framing omits the leverage math. Not a falsehood — an incomplete story. · **Verdict: narrative qualified — the donations are real; the motives are mixed and the sequencing (post-crisis) matters.**

---

## EVIDENCE REGISTER (forensics additions)

| ID | Claim | URL | Source type | Author/org | Pub date | Accessed | Confidence | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|
| MTFR-01 | Stacked diffs; predictive test selection; RacerD; Sapienz; Phab flow | https://developers.facebook.com/blog/post/2022/11/15/meta-developers-workflow-exploring-tools-used-to-code/?locale=en_US | Primary-technical (company dev blog) | Meta | 2022-11 | 2026-10-10 | High | — |
| MTFR-02 | Time In Review / Eyeball Time; Next Reviewable Diff +17% actions/day | https://engineering.fb.com/2022/11/16/culture/meta-code-review-time-improving/ | Primary-technical (eng blog) | Meta Engineering | 2022-11 | 2026-10-10 | High | — |
| MTFR-03 | Bootcamp: six-week, hired-as-engineers, move-fast indoctrination | https://venturebeat.com/dev/facebook-bootcamp | Secondary (press, company statements) | VentureBeat | n.d. (old) | 2026-10-10 | Medium | — |
| MTFR-04 | Ex-engineer nostalgia for move-fast tooling culture ("nothing is someone else's problem") | https://news.ycombinator.com/item?id=36504554 | First-hand-practitioner (unverifiable) | HN commenters (ex-Meta) | 2023 | 2026-10-10 | Low-medium | Past-tense; contrasts with MTFR-05 |
| MTFR-05 | Horizon Worlds shutdown announced for June 15, 2026, then kept alive after backlash | https://technewsvision.co.uk/can-you-forget-how-you-feel-about-meta/ | Secondary (press) | TechNewsVision | 2026-09 | 2026-10-10 | Medium | Corroborated by asianetnews, digit.in |
| MTFR-06 | $80B Reality Labs losses; <200k MAU (WSJ Oct 2022); 10% layoffs; 3 studios shut | https://economictimes.indiatimes.com/news/new-updates/why-mark-zuckerberg-is-shutting-down-metas-horizon-world-five-years-after-calling-it-next-big-thing-and-80-billion-investment/articleshow/129677176.cms?from=mdr | Secondary (press) | Economic Times | 2026-03 | 2026-10-10 | Medium | Corroborated by tradersunion.com |
| MTFR-07 | Employees faked Horizon Worlds engagement (USB launch, taped proximity sensor) | https://www.digit.in/features/general/mark-zuckerberg-shuts-metaverse-10-bizarre-moments-that-defined-it.html | Secondary (press, internal accounts) | Digit.in | 2026-03 | 2026-10-10 | Medium-low (single source) | — |
| MTFR-08 | Ray-Ban Stories 90% drawer rate → Ray-Ban Meta ~2M+7M units, sales doubled Q2 2026 | https://technewsvision.co.uk/can-you-forget-how-you-feel-about-meta/ | Secondary (press) | TechNewsVision | 2026-09 | 2026-10-10 | Medium | — |
| MTFR-09 | "Squid Game" culture account after 10% layoffs (deleted X post) | https://www.analyticsinsight.net/news/its-like-squid-game-ex-meta-engineer-slams-company-culture-mark-zuckerberg-after-layoffs | Secondary (press, first-hand post) | Analytics Insight (Jeremy Bernier) | 2026-05 | 2026-10-10 | Low (deleted original) | Contradicts move-fast narrative |

## GAPS (this workstream, Meta)
- Primary source for current AI-coding-target internal docs (only via BI/PeopleMatters).
- Meta's mobile release-train machinery (sibling debt).
- WhatsApp/Instagram/Facebook 2024–2025 outage specifics.
- Whether the React Foundation governance actually constrains Meta's influence (too early).
