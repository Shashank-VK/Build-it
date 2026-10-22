# Final Research Audit

**Date:** 2026-10-10 · **Scope:** all 20 research streams, 19 report sections, 5 appendices · **Full per-section detail:** [coverage-matrix.md](coverage-matrix.md) · **Proof layer:** [merged-evidence-register.md](merged-evidence-register.md) (1,081 rows) · **Open questions:** [unresolved-questions.md](unresolved-questions.md) (50+)

This audit answers the mandatory questions: where official documentation suffices, where practitioner reports add detail, where community discussion reveals recurring problems, where independent tests confirm or contradict claims, where sources disagree, what remains uncertain, and what cannot be resolved with public information.

## 1. Where official documentation suffices

Official sources carry the most weight in exactly four areas:

- **Accessibility and web standards (§9).** WCAG 2.2 (W3C Recommendation), EN 301 549 (ETSI), Core Web Vitals thresholds (web.dev), and the ADA Title II final rule are all primary-verified. This is the strongest official-source section in the report.
- **Security standards (§10).** OWASP ASVS 5.0.0, OWASP Top 10:2025, LLM Top 10 2026, Agentic ASI01–ASI10 2026, NIST 800-63B-4 — versions and dates verified against primaries (chapter-level for ASVS; requirement-ID-level mapping is honest debt).
- **Regulatory facts.** The FTC Consumer Reviews Rule text and effective date, EU AI Act Article 50 transparency duties (effective 2 Aug 2026), the EAA applicability date (28 June 2025) — all primary-verified. Enforcement *magnitudes* (fine totals, first actions) rest on secondary reporting.
- **Company-published engineering artifacts** — where they exist: NVIDIA's dev blog, Meta's Sapling posts, Google's SRE workbook, Atlassian's 7,500-word post-incident review, GitLab's postmortem lineage, GitHub's Copilot agent docs, Anthropic's "Building effective agents."

Everywhere else, official sources are necessary but insufficient — which is why the research was built on the full public ecosystem.

## 2. Where practitioner reports add the decisive detail

The majority of the report's load-bearing findings come from practitioner evidence, not official docs:

- **Incident and failure narratives** (§4, §11): Knight Capital (SEC filings + press), CrowdStrike RCA, Cloudflare/AWS/Azure 2025 outages, Vercel's VP self-postmortem ("the App Router wasn't really finished"), Tesla's production hell, GitLab 2017's DMARC-bounced backup alert.
- **The AI failure catalogues** (§2, §5): domain-a's false-"done"/green-test-illusion findings, domain-b's RAG demo→production gap, domain-c's Klarna arc (launch figures and CEO reversal both on-record).
- **The delivery-economics record** (§13): DX's +7.7% median, Uplevel's 800-dev study, GitClear's longitudinal cuts — all practitioner/independent-analyst work that vendor case studies never publish.
- **The fringe record** (Appendix C): the fabricated "42% microservices abandonment" statistic was *caught* by practitioner-source auditing, not by any official correction.

## 3. Where community discussion reveals recurring problems

Unofficial sources earned their place by surfacing patterns no official source admits:

- **The review-tax pattern** — AI PRs 2–3× larger, review load concentrating on seniors, no dashboard capturing it — emerged across Keypup, Cursor, LinearB, and Kraishan before any vendor acknowledged it.
- **Narrative-vs-reality gaps** — Google's 20%-time death by promo incentives, Amazon's culture threads, the Windows Phone autopsy via an ex-Nokia engineer, Valve's handbook-vs-witnesses split.
- **Recurring outage shapes** — Azure at roughly one control-plane incident per quarter 2025–26; GitHub's incident cluster after its "unacceptable" pledge (via a peer-reviewed MDPI paper on GitHub's *own* incident reports).
- **Demo-fakery and slop discourse** — the "Word Art era" debates, prompt-specificity findings, ~$249 AI-storefront toolkits.

Community evidence was never treated as fact on its own: single threads are labeled community observation; only recurring, multi-source patterns graduate to Corroborated.

## 4. Where independent tests confirm or contradict claims

Genuinely independent measurement is the scarcest and most valuable evidence in the corpus:

- **Confirmed by RCTs:** METR 2025 (−19% for experts on familiar codebases, pre-registered); Cui et al. (+26% tasks for less-experienced developers, field RCTs); Todd Little's IEEE data partially supporting #NoEstimates.
- **Confirmed by peer review:** Bernstein & Turban 2018 (open-plan offices *reduced* face-to-face interaction ~70%); the MDPI paper on GitHub incidents; Colfer & Baldwin's 142-study review bounding Conway's Law (prevalent, not universal); the RDD paper (n=591).
- **Contradictions that resolved by population:** Cui (+26%) vs METR (−19%) — juniors on scoped tasks vs experts on familiar codebases; lab vuln rates (~45%) vs Kraishan 2026's field finding (reviewed agent PRs had *fewer* security smells, OR 0.63) — lab-generated vs human-reviewed populations.
- **Contradictions kept open:** the $60M Klarna framing (asserted in one stream, excluded as unverified in another); multi-agent value (Anthropic's 90.2% lift at 15× cost vs Cognition's single-threaded-writes convergence); junior-employment causality (Stanford payroll data is solid; AI attribution is contested).

## 5. Where sources disagree — the honest ledger

The disagreements that matter, none papered over:

1. **Productivity paradox magnitude** — convergent direction (5 lines of evidence), disputed magnitude and population.
2. **Google's AI-code share** — ">25% of new code" (Pichai, Corroborated) vs a 75% press claim (flagged dubious).
3. **Spotify's squad model** — the industry copied a document whose page one warned against copying; whether Spotify "abandoned the model" is analyst synthesis, single-source.
4. **Meta's AI mandates** — token-maxxing tied to performance reviews (unverifiable docs) vs the September 2026 reversal (press-reported).
5. **Cursor's economics** — the 5% model-traffic figure (CEO on-record) reframes the "wrapper" thesis; growth partly mispriced inference (analyst inference, not company disclosure).
6. **Anthropic's safety posture** — the lab's own red team exfiltrated credentials 24/25 times; the threat model is simultaneously a published artifact and a policy instrument.
7. **Microservices "exodus" statistics** — named reversals real; aggregate percentages fabricated or marketing-adjacent.

## 6. What remains uncertain

The 50+ unresolved questions in [unresolved-questions.md](unresolved-questions.md) cluster into six themes. The most decision-relevant:

- **Measurement gaps:** cost per verified result, AI-era waiting-time decomposition, first-pass success rate, MTTR under AI adoption, queue lengths by provenance — *nobody publishes these*.
- **Causal questions:** does test-type mix causally change escaped defects? Does AI cause the junior-employment dip or is it a rate-hike hiring correction?
- **Verification debt:** Gurley's OSS essay primary, Meta internal docs, FTC 2026 enforcement primaries, Stripe API docs, ~60 lightly-researched tool records, DORA 2024-vintage tier numbers.
- **Vendor unknowns:** per-feature inference costs, golden datasets, training-data composition, AI-quality SLOs — *no vendor publishes any of these*.
- **Open contradictions:** the seven disagreements above, each labeled as such wherever it appears.

## 7. What cannot be resolved publicly

Stated plainly so nobody wastes effort:

- **Hyperscaler internals:** internal defect/security rates of AI-generated code, CI scale figures, financial breakdowns, proprietary incident data — at all five hyperscalers.
- **Stripe's reliability record:** no public postmortem exists; the reputation is structurally unauditable (verified absent, not merely unfound).
- **Replit's canonical postmortem:** the industry's most instructive agent failure still has none.
- **Jane Street's engineering:** a deliberate black box — recorded as such.
- **Undisclosed breaches:** whether injection or exfiltration incidents occurred at major vendors and were never disclosed is unknowable from public sources.
- **LinkedIn-walled practitioner knowledge:** captured best-effort only; the login wall is a real coverage boundary, noted wherever it bit.

## 8. Method limitations (honest)

- **Source-language skew:** the corpus is overwhelmingly English and US-SaaS-centric; non-English ecosystems are under-covered (noted per stream).
- **Temporal skew:** the 16 original streams were researched before the source-expansion steer; the 4 later streams (expansion ×3, forensics, gaps) carry the wider net (GitHub exhaustively, Wayback, job postings, newsletters, podcasts). The coverage differential is real and disclosed here rather than hidden.
- **Vendor contamination:** Keypup, Kaamfu, SlashData, DX, GitClear, Uplevel, Veracode, Apiiro, CodeRabbit, SonarSource sell or market adjacent remedies. Mechanisms from these sources were independently corroborated wherever possible; their *figures* are treated as directional/illustrative, never as measurements. Every such figure carries its attribution inline.
- **Dedupe limits:** the 1,081-row merged register was deduped heuristically (exact-URL + claim-similarity + manual curation of famous cases). The long tail may hold a few near-duplicates phrased differently.
- **652 findings** in source registers carry no claim label (shown as `—` in the merged register with confidence preserved); nothing was invented to fill the gap.
- **No live-browser verification** was possible in this environment; all web evidence comes from search-result text and page fetches dated 2026-10-10.

## Audit verdict

The report's strongest ground is **mechanism-level knowledge**: how failures actually happen (postmortems), how systems are actually built (forensic reconstructions), and where official narratives break (dismantled with receipts). Its weakest ground is **quantified base rates**: most headline numbers are vendor-published, single-sourced, or practitioner-consensus ranges — and the report says so every time. The honest unknowns are not a defect of the research; they are its most actionable output, because they name exactly what the industry does not measure and therefore cannot manage.
