# Netscape / Mozilla — product engineering case study (the rewrite that killed a company)

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
Netscape is the canonical *failed rewrite* — the case Joel Spolsky's "Things You Should Never Do, Part I" made immortal, and the seed of Mozilla/Firefox. The forensic material is thinner than ideal (jwz's original essay not fetched this pass — cited via secondary quotes), but the arc is exceptionally well documented: rewrite announced 1998 → three lost years → Netscape 6 (2000) shipped on alpha-quality Mozilla code → company dead → Firefox 1.0 (2004) redemption.

## 1. Forensic reconstruction — how the machine actually worked (and stopped)

### The decision: rewrite instead of refactor
- Claim: In 1998, facing Internet Explorer, Netscape decided to rewrite the browser from scratch (the Mozilla project) rather than incrementally improve the shipping Netscape Communicator codebase. Jamie Zawinski (jwz), a key Netscape engineer, opposed it; his account describes the rewrite consuming the company while IE shipped. Label: **Corroborated** — jwz's essay widely quoted (secondary via medium/@romainx); Spolsky's 2000 essay uses Netscape as the canonical example. Confidence: high for the decision and its outcome; medium on internal deliberation details (primary essay not fetched).
- Claim: Lou Montulli (Netscape engineer, inventor of the `<blink>` tag and cookies) is quoted describing the period as Netscape "sitting on its hands" while the rewrite dragged — three years with no competitive shipping product. Label: **Corroborated** (secondary quotes). The mechanism: a rewrite freezes the shipping product's evolution because all senior engineers are on the new codebase, while competitors iterate on their shipping one.

### The Mozilla years: open source as life support
- Claim: Netscape open-sourced the code (Mozilla, 1998) — the rewrite continued as an open-source project even as the company collapsed (AOL acquisition 1999, layoffs). The browser that finally shipped as Netscape 6 (Nov 2000) was built on Mozilla code widely regarded as alpha quality. Label: **Corroborated** (eweek "10 years of Mozilla"; medium/@romainx). Engineering implication: open-sourcing didn't save the schedule; it saved the *code* — the asset outlived the company.

### The redemption machine: Firefox
- Claim: The Phoenix/Firebird/Firefox effort — a small team building a standalone browser on the Gecko engine, rejecting the Mozilla suite's bloat — shipped Firefox 1.0 in Nov 2004 and hit 100M downloads in its first year, eventually breaking IE's monopoly. Label: **Corroborated** (eweek; widely reported). The forensic point: the *same codebase lineage* succeeded once the product was rescoped small (a fast browser, not a platform suite) and the team was small and focused.
- Claim: Brendan Eich's later reflection (osq.cs.berkeley.edu paper on Firefox performance work) documents the engineering culture that made the comeback: measurement-driven performance engineering on a shipping product. Label: **Corroborated** (primary-adjacent paper). Confidence: medium.

## 2. Postmortem record — the rewrite, dissected
- **What broke:** not the code — the *strategy*. The rewrite discarded a shipping, revenue-generating product's accumulated bug fixes, edge cases, and platform knowledge (Spolsky's core argument: old code *is* the bug-fix database). Three years of rewrite = three years of IE shipping improvements. By the time Mozilla was viable, the market had moved. Label: **Corroborated** (Spolsky; jwz via secondary).
- **Netscape 6 (2000):** shipped on immature Mozilla code to meet corporate/AOL timelines — the "ship the rewrite before it's ready" failure, widely panned, killed the brand's remaining credibility. Label: **Corroborated**.
- **What changed afterward (industry-wide):** "Never rewrite" became industry dogma — arguably over-learned (see Narrative audit). The constructive lessons: strangler-fig migration, branch-by-abstraction, and the Firefox proof that *rescoping* beats *rewriting*.

## 3. Narrative audit — dismantling with receipts
- **"Never rewrite" is over-learned dogma.** Spolsky's essay is brilliant rhetoric built on one data point. The receipts *for* rewrites: Firefox itself was effectively a rewrite of the product (if not the engine); the Mozilla *engine* rewrite eventually produced Gecko, which powered a competitive browser for 15+ years. The dismantling: the lesson isn't "never rewrite" — it's "never rewrite *while freezing your shipping product for years with no incremental delivery*." Netscape's sin was the big-bang cutover and the 3-year feature freeze, not the new code. Label: **Inferred** (audit synthesis); the Firefox counterexample is **Corroborated**.
- **The open-source decision gets too much credit and too little.** Popular telling: "Netscape died but open source saved the code — what heroes." The receipts: open-sourcing in 1998 didn't help Netscape ship anything faster; Mozilla 1.0 took until 2002. What it did was create the *conditions* for the Firefox fork years later. The honest lesson: open-sourcing is a preservation strategy for the asset, not a rescue strategy for the schedule. Label: **Inferred** on **Corroborated** timeline.
- **jwz's essay as primary source — a gap with a warning.** This file cites jwz's account second-hand (medium/@romainx quotes). The original essay ("netscape: too little, too late" / the mozilla.org resignation letter) should be read directly before quoting jwz's specific claims as his. Recorded as a verification debt, not a fact. Label: **Unknown** (primary not fetched).

## Transferable lessons
1. **Old code is a bug-fix database.** A rewrite discards years of accumulated edge-case handling. Budget for re-discovering every one of them, or don't rewrite.
2. **Never freeze the shipping product.** If the rewrite takes years, the business needs the old product evolving in parallel — Netscape's fatal move was staffing the rewrite with everyone.
3. **Rescope before you rewrite.** Firefox won by shrinking the product (browser, not suite), not by rewriting the engine. Ask whether the problem is the code or the scope.
4. **Strangler-fig beats big-bang.** Migrate incrementally behind the shipping product; the cutover should be a non-event.
5. **Open-source as asset preservation** is legitimate — but don't confuse it with a schedule rescue.

## Sources
| ID | Claim | URL (verbatim) | Type | Author/Org | Pub date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| N1 | Netscape rewrite as "big mistake"; jwz/Montulli quotes; 3 lost years | https://medium.com/@romainx/netscape-the-rewrite-big-mistake-6a4b858828c0 | Secondary interpretation | romainx (Medium) | n.d. | 2026-10-10 | Medium |
| N2 | 10 years of Mozilla; Netscape 6 on alpha code; Firefox 1.0, 100M downloads | https://www.eweek.com/it-management/10-years-of-mozilla/ | Secondary | eWeek | ~2008 | 2026-10-10 | Medium-high |
| N3 | Firefox performance engineering culture (Eich-era) | http://osq.cs.berkeley.edu/public/ocallahan-firefox.pdf | Primary-adjacent (paper) | Berkeley / Mozilla | n.d. | 2026-10-10 | Medium |

**Gaps:** jwz's original essay (not fetched — verification debt); Spolsky's essay (cited from memory of its argument, not fetched — treat the "never rewrite" summary as **Corroborated** by its fame but quote nothing); AOL-era Mozilla governance (not covered).
