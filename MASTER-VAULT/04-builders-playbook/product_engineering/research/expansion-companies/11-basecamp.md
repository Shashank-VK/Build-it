# Basecamp / 37signals — product engineering case study

Workstream: expansion-companies · Researched 2026-10-10 · Read-only research; no installation, ranking, or recommendation.

## Scope notes
37signals is the contrarian-process exemplar: Shape Up (the methodology), calm-company operations, by-product strategy (Rails extracted from Basecamp), and the HEY-vs-Apple App Store fight. Sources are secondary syntheses of their books/blogs plus press on HEY.

## Findings

### Product development process (Shape Up)
- Claim: Shape Up (Ryan Singer, Basecamp) inverts estimation: fix the *appetite* (how much time the idea is worth), then shape a version of the solution that fits — "start with a number, end with a design" vs estimation's "start with a design, end with a number." Label: **Corroborated** — dev.to book notes + skills syntheses (basecamp.com/shapeup is the primary; not fetched this pass).
- Claim: Bets are commitments to uninterrupted 6-week cycles; cool-downs between cycles; no automatic extension of unfinished work (if it didn't fit the appetite, maybe it wasn't worth doing); backlogs are a "growing pile that gives us the feeling of always being behind" — "important ideas will come back." Label: **Corroborated** (same).
- Claim: Hill charts track uphill (figuring out the approach) vs downhill (execution) by gut feel, not ticket counts; "good enough" is judged against the current baseline, not the ideal. Label: **Corroborated** (same).
- Claim: Assign projects, not tasks — "talented people don't like being treated like code monkeys or ticket takers." Label: **Corroborated** (same).
- Claim: The method emerged from a real constraint: in Basecamp's early years their only engineer (DHH) worked ~10 hours/week, forcing ruthless scoping. Label: **Corroborated** — tomevault skill (secondary); the 10-hr figure is single-source — Medium-low.

### Culture / operations
- Claim: "Calm company" doctrine (It Doesn't Have to Be Crazy at Work): chaos/anxiety/meetings-all-day are "perversions of work," side effects of broken models. Label: **Corroborated** — 37signals.com/books (primary publisher page).
- Claim: By-product strategy: sell what the main product already paid for — Rails (extracted from Basecamp), the books (Getting Real, Rework, Remote, Shape Up), Hotwire/Turbo/Stimulus, remote-work thought leadership. "Competitors can copy your features. They cannot copy your thinking." Label: **Corroborated** — wondelai 37signals-way synthesis.
- Claim: DHH's contrarian technical stances (against microservices, TypeScript, cloud orthodoxy) are part of the brand and the hiring filter. Label: **Corroborated** — tayiorbeii 37signals-way skill.

### Ship / operate (HEY launch)
- Claim: HEY (email, $99/yr, launched June 15, 2020) was initially approved, then Apple rejected updates (bug fixes blocked) and threatened removal unless HEY added in-app purchase — 15–30% of revenue to Apple. DHH's public campaign ("outrageous demand... they'll REMOVE THE APP") ran June 16–25. Label: **Corroborated** — Macworld, The Register, AppleInsider (June 2020).
- Claim: Apple said the v1.0 approval was "a mistake"; Hey wasn't a "reader" app; Phil Schiller said he wouldn't budge. Label: **Corroborated** — TechAdvisor/AppleInsider.
- Claim: Resolution (June 25, 2020): Apple "definitively approved" HEY with NO IAP and no 30% cut — Basecamp added a free temp-address tier and work-account support, threading the guideline needle. DHH: "Hopefully this paves an illuminated path for approval for other multi-platform SaaS applications... New policies, new precedence." Label: **Corroborated** — Engadget, TechAdvisor.
- Lesson: a small company with a loud founder and a sympathetic press narrative moved Apple's App Store precedent — platform power is negotiable when the fight is public and the ask is framed as fairness, not special treatment. Label: **Inferred** from the verified sequence.

### Documented failures
1. HEY's App Store near-removal (above) — a *distribution* failure, not an engineering one; resolved by negotiation + product tweak. No engineering postmortem located. Label: **Corroborated**.

### Transferable lessons
- Appetite-before-estimate (Shape Up) kills the estimate-trap and the backlog-guilt cycle. Label: **Corroborated**.
- Calm is a strategy: fewer rituals, no sprint theater, uninterrupted build time — but it requires saying no to growth-at-all-costs. Label: **Corroborated**.
- Sell your by-products: process, tools, and books are nearly pure-margin distribution for the main product's ideas. Label: **Corroborated**.
- When a platform squeezes you, fight in public with a principled frame — and have a product-level concession ready (the free tier) that lets the platform save face. Label: **Inferred** from HEY case.

## Sources
| ID | Claim area | URL | Type | Author/org | Date | Accessed | Confidence |
|---|---|---|---|---|---|---|---|
| BA-01 | Shape Up mechanics (appetite, betting, hill charts) | https://github.com/tomevault-io/tomes/blob/HEAD/./wdavidturner--product-skills/skills/shape-up/SKILL.md | Secondary (method synthesis) | tomevault-io | 2026 | 2026-10-10 | Medium |
| BA-02 | Shape Up book notes | https://dev.to/danlebrero/book-notes-shape-up-stop-running-in-circles-and-ship-work-that-matters-e2b | Secondary (reader notes) | danlebrero / DEV | 2021 | 2026-10-10 | Medium |
| BA-03 | Books publisher page (Shape Up, Calm, Rework) | http://37signals.com/books | Primary (publisher) | 37signals | current | 2026-10-10 | High |
| BA-04 | By-product strategy, DHH contrarianism | https://github.com/wondelai/skills/blob/HEAD/37signals-way/references/opinionated-software.md | Secondary (synthesis) | wondelai | 2026 | 2026-10-10 | Low-medium |
| BA-05 | HEY rejection, 30% demand, DHH tweets | https://www.macworld.com/article/674369/apple-threatens-to-remove-email-app-if-they-dont-hand-over-30.html | Secondary (press) | Macworld | Jun 2020 | 2026-10-10 | Medium |
| BA-06 | HEY definitive approval, no IAP, precedent | https://www.engadget.com/apple-basecamp-hey-email-app-store-154225649.html | Secondary (press) | Engadget | Jun 2020 | 2026-10-10 | Medium |
| BA-07 | Apple "mistake" approval, Schiller no-budge | https://www.techadvisor.com/article/739592/apple-approves-hey-email-app-despite-original-commission-demands.html | Secondary (press) | TechAdvisor | Jun 2020 | 2026-10-10 | Medium |

## Postmortem record (retrofit 2026-10-10): HEY vs. the App Store (June 2020)
- **What happened:** Basecamp launched HEY (email service) on iOS without in-app purchase; Apple rejected updates demanding the 30% IAP cut. DHH went to public war — the fight was cited in congressional antitrust hearings; Apple eventually approved HEY under a "reader app" compromise after Basecamp added a free tier. Label: **Corroborated** (widely reported, June 2020). Confidence: high on the arc.
- **The engineering angle:** HEY's launch *also* had ordinary product issues (invite-system scaling, onboarding friction). The App Store fight overshadowed the product postmortem — the company fought Apple instead of narrating its own launch bugs. That's the audit point, made in the next section.

## Narrative audit (retrofit 2026-10-10)
- **"Calm company" vs. the founder's war footing.** The books preach calm, reasonable 40-hour weeks — while DHH personally wages the industry's loudest public wars (vs. Apple, vs. the cloud, vs. VCs). The calm is *for employees*; the combat is *the marketing*. A coherent division of labor — but the books present calm as the whole philosophy.
- **The 2021 memo and the third who left.** The ban on political discussion at work led to roughly a third of staff departing. "Calm" turned out to mean "the founders' definition of calm, enforced top-down" — the same top-down authority the books criticize elsewhere. No company gets a free pass, including the one that wrote the book on the alternative.
- **Leaving the cloud: audit the $7M.** DHH's claimed savings from cloud repatriation are widely cited — and widely caveated (it excludes the engineering cost of running your own hardware; Basecamp's workload is unusually stable and predictable). A real data point for *their* workload, not a general proof. Your workload isn't Basecamp's.
