# expansion-companies — evidence register

Workstream: expansion-companies · Compiled 2026-10-10 · Read-only research.

## Coverage statistics
- **37 case files**, 230 catalogued sources (per-file Sources tables).
- **~26 primary sources** (company engineering blogs fetched in full, public repos read directly, regulatory filings, peer-reviewed papers, executive interviews, job postings quoted verbatim, teardown reports).
- **~60 first-hand/community sources** (ex-employee accounts, HN/Reddit threads, practitioner blogs, forum posts).
- **Remainder:** secondary analysis, trade press, contemporary reporting, community syntheses (GitHub awesome-lists, skill repos).
- All sources accessed 2026-10-10. Every major claim carries a methodology label: **Verified** (primary source fetched) / **Corroborated** (multiple independent secondaries) / **Inferred** (analyst synthesis, labeled) / **Proposed** (hypothesis) / **Unknown** (not found).

## Strongest primary evidence (by file)
| File | Primary source(s) |
|---|---|
| 01-cloudflare | Nov 2023 control-plane postmortem (blog.cloudflare.com, fetched) |
| 09-gitlab | Jan 2017 DB incident (about.gitlab.com postmortem lineage; livestream documented) |
| 13-palantir | FDE/Sr-FDE job postings quoted verbatim (theladders, fwddeploy.com) |
| 14-spacex | FAA mishap findings via space.com (Flight 7, Mar 2025); SpaceX updates page |
| 15-apple | Ex-employee Erin Caton (MobileMe); Fortune "Inside Apple" (auditorium) |
| 16-knight-capital | SEC administrative proceeding PDF (secdatabase) |
| 18-healthcare-gov | 4sight Health case study; Dickerson profile |
| 23-valve | Valve Handbook for New Employees (2012, PDF) |
| 24-riot-games | technology.riotgames.com: client architecture, Hextech UI, LKG pipeline, LoR |
| 28-tesla | Musk admission quote (contemporaneous press, Apr 2018) |
| 29-framework | iFixit teardown (10/10); June 2026 delay reporting (5 independent outlets) |
| 30-ibm-carbon | github.com/carbon-design-system/carbon repo (README, file listing, fetched) |
| 31-atlassian | 7,500-word post-incident review (Apr 29, 2022, via TechTarget) |
| 32-adobe-spectrum | adobe/react-spectrum + spectrum-web-components repos (AI artifacts verified) |
| 34-vercel | Tom Occhino interview (The New Stack) — App Router self-postmortem |
| 35-datadog | Distributed DataFusion engineering blog (read in full) |
| 37-lean-outliers | Oct 2021 BGP outage (Meta postmortem lineage via dev.to/Threatpost) |

## Verification debts (things cited but not directly fetched)
1. **jwz's original Netscape essay** (file 17) — cited via secondary quotes only.
2. **Spolsky "Things You Should Never Do"** (file 17) — argument summarized, not quoted from primary.
3. **Atlassian's 7,500-word review** (file 31) — via TechTarget, not fetched verbatim.
4. **Slack's primary engineering-blog posts** (file 36) — via ByteByteGo/sre-world/kuma-blog secondaries.
5. **Figma-deal regulatory record** (file 32) — figures Corroborated, no single primary citation fetched.
6. **Riot's technology blog article URLs** — titles verbatim, exact paths not preserved from search.
7. **Cegłowski's "Website Obesity Crisis"** (file 26) — cited, not fetched.
8. **Salesforce SLDS internals** (file 33) — thinnest file; primary team writing not found.
9. **Tesla 2021 firmware-rewrite primary** (file 28) — cited, not fetched.
10. **Lyte Lin's primary talks** (file 24) — cited, not fetched.
11. **Allchin "crashing into the ground" memo** (file 21) — via WSJ reporting, not fetched.
12. **Srivastava's Vista quality papers** (file 21) — cited, not fetched.

## Source-quality incidents caught during research
- **archyde.com (Framework delay):** contained fabricated-sounding details (wrong CPU, unverifiable "chief engineer" memo, thermal claims no other outlet reported). Excluded; documented in file 29 §2. Lesson recorded: triangulate incident news across ≥3 independent sources — AI content farms now pollute hardware news.
- **medium/@arijitghosh646 (Starship Flight 1):** "utterly embarrassing" framing treated as opinion, not fact; FAA's 63-action list used instead. Documented in file 14.
- **Midjourney figures (~40 people, ~$200M):** analyst-derived, unaudited — used directionally only. Documented in file 37.
- **Entrepreneur $200M→$500K (Digg):** declined-offer vs. asset-sale comparison flagged as imprecise framing. Documented in file 19.

## Honest limitations
- **LinkedIn:** public practitioner posts exist but are largely login-walled; not accessed. Limitation recorded in files 13 (Palantir FDEs) and the register.
- **Non-English sources:** not systematically searched; no material non-English evidence was needed for the claims made, but the net is acknowledged as English-biased.
- **Wayback Machine:** used once (file 05, fluxer.app mirror). Dead primary pages (e.g., old Mozilla docs) were cited via live secondaries instead.
- **Job postings as evidence:** used for Palantir (files 13) — contractor postings may dilute the internal model; confidence labeled accordingly.
- **No live browser:** all web evidence via search-result text and page-text fetches; no website visits claimed.
- **Dates:** "accessed 2026-10-10" throughout; publication dates are as reported by sources, some approximate ("n.d." where the source gave none).
- **Gaps per file** are listed in each file's closing "**Gaps:**" line — this register does not duplicate them; the 12 verification debts above are the cross-file items worth a second pass.

## Label key (as used in every file)
- **Verified** — primary source fetched and read (eng blog, repo, filing, paper, verbatim quote).
- **Corroborated** — ≥2 independent secondary/community sources converging.
- **Inferred** — analyst synthesis from verified/corroborated facts; the reasoning is shown.
- **Proposed** — hypothesis offered for testing, not asserted.
- **Unknown** — looked for, not found.
- **Verified-absent** — searched; the thing's absence is itself the finding (e.g., no public postmortems).
