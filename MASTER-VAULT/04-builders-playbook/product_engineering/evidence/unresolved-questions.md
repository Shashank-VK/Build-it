# Unresolved Questions — merged across all 20 streams

**Built:** 2026-10-10 (assembly) · Deduped across every workstream's honest-gaps section. The report's §18 carries a curated top-15; this file is the complete merged list. Each entry: the question, why it matters, what would resolve it, and which stream(s) flagged it. Nothing here is answered by assertion — that is the point.

---

## A. Measurement gaps — the numbers nobody publishes

**A1. Cost per verified result.** The fully loaded cost of one change that survives 30 days in production incident-free: (license + inference $/dev/mo) + (human review/rework/debug minutes × loaded cost) + (escaped-defect cost). *Why it matters:* every AI-adoption ROI claim in the corpus is missing its denominator; without it, throughput gains can't be weighed against review/rework/defect costs. *What would resolve it:* org-level instrumentation joining license/inference spend to review-time tracking and escaped-defect costs; a multi-org published study. *(economics — Unknown; §18 top-15 #1)*

**A2. AI-era maintenance cost as a measured number.** The classic figures are Corroborated (Gartner 55–80% of IT budgets; IEEE 60–80% of lifecycle cost), but the AI-era tail is Inferred from structural code metrics (GitClear: duplication +81%, refactoring 21%→<4%, correlational) and Unknown as a measured cost. *Why it matters:* the most important number for AI-era build decisions — whether velocity gains survive the maintenance tail — has no public measurement. *What would resolve it:* longitudinal cost studies on AI-assisted codebases (defect-fix hours, refactoring effort, incident cost by code provenance). *(gaps T9; economics; build-ship honest gaps — Unknown)*

**A3. User outcomes tied to AI adoption.** No study connects AI coding adoption to customer-facing outcomes (satisfaction, retention, SLA attainment) with any control. *Why it matters:* the entire productivity debate is about intermediate metrics (PRs, throughput); the customer is absent. *What would resolve it:* product analytics joined to engineering adoption data, with controls. *(economics — Unknown; §18 #2)*

**A4. AI-era waiting-time decomposition.** No published value-stream map with a before/after wait-vs-work decomposition. *Why it matters:* if AI speeds up work but queues grow (review bottleneck), net lead time may not move — unmeasurable today. *What would resolve it:* value-stream mapping studies (DORA 2025 recommends; none published). *(economics — Unknown; §18 #3)*

**A5. Review-queue lengths by change provenance.** Review/CI/deploy queue depth time series segmented by AI-vs-human authorship. *Why it matters:* the review-tax thesis (T2) predicts queues growing on the AI side; no engineering-intelligence platform publishes it. *What would resolve it:* LinearB/DX/Cursor-style platforms publishing provenance-segmented queue data. *(economics — Unknown)*

**A6. Recovery time (MTTR) under AI adoption.** No controlled or matched before/after study of incident recovery with AI-assisted debugging. *Why it matters:* faster authoring is worth less if AI-authored incidents are harder to diagnose. *What would resolve it:* incident data joined to adoption data. *(economics — Unknown; §18 #5)*

**A7. First-pass success rate.** No pre-registered industry rate for AI-assisted changes with a pre-AI baseline. *Why it matters:* "acceptance rate" is vendor-graded; an independent success definition is missing. *What would resolve it:* a standard definition + a multi-org study. *(economics — Inferred/Unknown; §18 #6)*

**A8. Spec quality and spec time under AI adoption.** The stage whose importance *rises* as generation gets cheap has no published measurement. *Why it matters:* if specs are the new bottleneck, investment is misallocated to generation. *What would resolve it:* studies measuring spec completeness/review cycles vs downstream defect rates. *(economics — Unknown; §18 #4)*

**A9. Review-tax magnitudes.** AI-authored PRs running 2–3× human size, collapsing approval times, rubber-stamp comment density: illustrative vendor analyses (Keypup, Cursor), not independently audited. Direction Corroborated; magnitudes Unverified. *Why it matters:* capacity planning for the review bottleneck needs real numbers. *What would resolve it:* independent audit of PR-size/review-time distributions by authorship across multiple orgs. *(gaps T2; domain-a — Unknown; §18 #15)*

**A10. Internal defect and security rates of AI-generated code at the hyperscalers.** Unknown at all five companies studied — "the most important unanswered question in the set." *Why it matters:* the labs shipping the tools don't publish the defect ledger; everyone else is extrapolating from lab studies. *What would resolve it:* hyperscaler-published defect/security rates by code provenance (unlikely) or large-scale independent mining of provenance-labelled codebases. *(cases-hyperscale — Unknown; §18 #7)*

**A11. AI-quality SLOs from assistant vendors.** No vendor publishes per-feature inference costs, full golden datasets, judge prompts, training-data composition — or any AI-quality SLO (only uptime SLAs). *Why it matters:* buyers can't compare quality, only marketing. *What would resolve it:* vendor-published quality SLOs and eval transparency. *(domain-b — Unknown; §18 #13)*

**A12. Judge–human correlation for LLM-as-judge.** 80–85% is practitioner-cited; no primary study located. *Why it matters:* the entire eval-harness industry leans on an unanchored number. *What would resolve it:* published calibration studies. *(domain-b — Unknown)*

---

## B. Causal questions — does X cause Y?

**B1. Whether AI-adoption mandates produce outcomes or gaming.** The Meta tokenmaxxing arc (2025 targets → Sept 2026 reversal) suggests gaming; formally Unknown. *Why it matters:* the difference between a rollout strategy and a Goodhart machine. *What would resolve it:* a controlled comparison of mandated vs voluntary adoption cohorts on outcome metrics (not usage metrics). *(gaps T3; cases-hyperscale C3 — Unknown; §18 #8)*

**B2. Whether Anthropic's multi-agent figures replicate.** 90.2% lift over single-agent on research evals at ~15× token cost — vendor-published, uncorroborated by independent replication. *Why it matters:* the most-cited multi-agent evidence is single-vendor. *What would resolve it:* third-party benchmark replications (automation G-04). *(automation — Corroborated-low; §18 #9)*

**B3. The causal effect of any single test-type mix on escaped defects.** No controlled experiment; the test-pyramid critiques are principled practitioner arguments, not trials. *Why it matters:* the quality-gate system (§11) leans on consensus, not causation. *What would resolve it:* controlled trials varying test mix holding all else constant (expensive; unlikely). *(build-ship — Unknown; §18 #11)*

**B4. Whether junior-employment declines are AI-caused.** Stanford "Canaries" employment data is high-confidence (Corroborated, six outlets); AI-as-cause is the authors' interpretation, contested vs. rate-hike hiring correction. *Why it matters:* existential for craft transmission and hiring strategy. *What would resolve it:* disentangling studies (firm-level AI adoption × junior hiring, controlling for macro). *(gaps T2; expansion-practices #56 — causal attribution Unknown; §18 context)*

**B5. The precise team-size threshold where microservices pay off.** Accounts range from an 11-engineer team that regretted it to an 18-engineer startup succeeding with 2 services; team size is a proxy for deploy contention, scaling-profile divergence, and operational maturity. *Why it matters:* the most-asked architecture question has no numeric answer. *What would resolve it:* multi-org studies controlling for the real variables (spec-arch D2 — Unknown; §18 #12)*

**B6. Whether undisclosed injection breaches have occurred at major vendors.** Unknowable from public sources. *Why it matters:* the absence of evidence is not evidence of absence for prompt-injection. *What would resolve it:* only vendor disclosure; treat as Unknown, not as safe. *(domain-b — Unknown)*

---

## C. Verification debt — primaries not fetched this pass

These are not unknowns about the world; they are known claims whose primary sources weren't fetched. Directions are cross-corroborated; exact figures/quotes need re-verification before external citation.

**C1.** Gurley's "From Open Source Software to Open Source Strategy" essay (May 2026) — chased through four consistent secondaries; primary not fetched. *(gaps T5; §18 verification debt)*
**C2.** Meta's internal AI-usage performance documents — press-reported (BI, Wired), not primary. *(gaps T3)*
**C3.** FTC's 2026 fake-review enforcement actions — practitioner/legal secondaries; no FTC primary fetched. *(gaps T10)*
**C4.** Stripe's API docs (idempotency/versioning discipline) — cited via secondary architecture narratives. *(gaps T6)*
**C5.** Discovery frameworks' primary texts (Torres, Cagan, Blank, Fitzpatrick, Ulwick books; svpg.com/producttalk.org) — represented via community summaries; verbatim quotes are attributed, not verified. *(discovery)*
**C6.** CB Insights' ~42% "no market need" postmortem figure — corroborated via citers; original methodology unchecked. *(discovery)*
**C7.** Rules-stream primary texts (Brooks, Knuth, Fowler, Ousterhout, Kleppmann, Ries, Cagan, Torres, Shostack, Phoenix Project) — labelled Corroborated on canonical status + secondary confirmation, not Verified. *(rules)*
**C8.** DORA 2025/2026 benchmark tiers — 2024-vintage via mirrors; treat tier numbers as approximate. *(rules)*
**C9.** Faros.ai's 242.7% incidents-per-PR figure — needs primary verification. *(economics; §18 verification debt)*
**C10.** Google's internal CL-size study — widely cited, not publicly inspectable. *(build-ship; §18 verification debt)*
**C11.** arXiv mutation/LLM-test study (2607.22880) — accessed via practitioner notes, not the paper. *(build-ship; §18 verification debt)*
**C12.** Langfuse/LangSmith/Braintrust current features; OpenTelemetry GenAI semantic conventions — not verified this pass. *(automation G-02, G-03; §18 verification debt)*
**C13.** GitHub github.blog primaries (code-review metrics, Rust migration) — cited via research notes, not fetched first-party. *(cases-product D-02)*
**C14.** OpenAI incident narratives; Stripe/Spotify incident narratives — single-sourced or lacking official write-ups. *(cases-product D-03)*
**C15.** UX primary studies (NNG/Baymard/Google figures) — cited second-hand via practitioner sources; magnitudes directional. *(ux-states)*
**C16.** WCAG/EN 301 549 details — OJEU citation status of v4.1.1 as of 2026-10-10 unconfirmed; EAA fine totals single-sourced; UK PSBAR single-sourced. *(quality)*

---

## D. Vendor & industry unknowns — not publicly documented

**D1.** Hyperscaler internals: internal CI scale, precise financials, NVIDIA internal process (VCS/CI/review/SDL), Microsoft ring-deployment primary, Sept-2026 hybrid RCA completion, Google SRE postmortem template primary text. *(cases-hyperscale; forensics verification debt)*
**D2.** Stripe: any official postmortem; internal process — all Unknown (reputation without postmortems). *(forensics)*
**D3.** Cursor: engineering writing; ARR audit; SpaceX-neutrality question. *(forensics)*
**D4.** Replit: canonical postmortem for the freeze-violation incident; guardrail architecture. *(forensics)*
**D5.** Spotify: current org-model primary ("abandoned the model" single-sourced). *(forensics)*
**D6.** Airbnb: AI-productivity figure audit; sprawl-unwind status. *(forensics)*
**D7.** Anthropic: Cowork "outside threat model" confirmation (single-source); CVSS re-rating rationale. *(forensics)*
**D8.** OpenAI: internal incident-review mechanics; petition figure. *(forensics)*
**D9.** Amazon: Builder's Library COE primaries; open-letter confirmation; full FT Kiro text. *(forensics)*
**D10.** No public third-party safety audit of a commercial assistant's injection defenses. *(domain-b — Unknown; §18 #14)*
**D11.** Sprig status entirely unverified; Maze 2023–2026 status; Rasa ownership; Dify/Flipt licenses; Unleash license (AGPL-3.0 vs Apache-2.0); Dragonfly/KeyDB 2026 releases. *(expansion-tools verify-later list)*
**D12.** M&A close confirmations: Supabase↔Turso; Portkey→Palo Alto Networks; Promptfoo→OpenAI; Khan v. Figma docket. *(expansion-tools)*
**D13.** Inngest Oct 2025 outage — independent reports not pulled (single ADR source). *(expansion-tools)*
**D14.** Dependabot's compute backend internals — GitHub Docs describes behavior only. *(automation G-07)*
**D15.** MCP adoption numbers ("10,000+ servers") — single 2026 guide; needs corroboration. *(automation G-08)*
**D16.** CERT advisory primary text (Sentry/Seer chain) — not located. *(automation G-05)*

---

## E. Method & scope limitations — what the research could not do

**E1. No live browser.** All web evidence via search-result text and page-text fetches; no website visits claimed. *(expansion-companies; applies to all streams)*
**E2. English-language bias.** No systematic non-English source sweep; US-centric startup/SaaS applicability to other markets, regulated industries, and hardware is unexamined. *(discovery; expansion-companies)*
**E3. LinkedIn login wall.** Public practitioner posts largely inaccessible; used via search-result capture with limitations noted. *(expansion-companies; forensics)*
**E4. Paywalled sources.** The Information (Blackwell), FT (Kiro), Puck (Netflix) via secondary quotation only. *(forensics)*
**E5. Deleted sources.** Meta "Squid Game" X post (deleted); Cursor's removed blog post — via secondary reporting, low confidence. *(forensics)*
**E6. Vendor-interest contamination.** Keypup (review-tax), Kaamfu (governance), Practical Logix (platform consulting), SlashData (analyst), and single-vendor telemetry (CrowdStrike, MCPTox) originate from vendors selling the remedy — mechanisms corroborated independently; vendor figures treated as illustrative. *(gaps; security)*
**E7. Diminishing-returns stops.** Discovery: searches beyond ~2–3 per company recycled secondary content. Hyperscale: 18 query batches, stopped when sources repeated. UX: no r/userexperience threads retrieved. *(cases-product D-06; cases-hyperscale; ux-states)*
**E8. Excluded as unverified (kept for a future pass):** the Dunstan "AI Code Review Paradox" syndication; the "$60M Klarna lesson" framing; AI Weekly's 159-deployment library figures; Backstage "~89% market share"; Cursor pricing-backlash evidence (not captured, not asserted). *(gaps honest-gaps #3; cases-product D-04)*
**E9. Possible blind spots flagged, not verified:** SOC 2 / ISO 27001 *certification* engineering never surfaced in any sibling file; game-dev practices and green software surfaced nothing and were dropped. *(gaps honest-gaps #7)*
**E10. Publication dates approximate** where inferred from page/crawl metadata; "accessed 2026-10-10" throughout. *(expansion-companies; discovery)*

---

## F. Open contradictions (kept unresolved — do not silently resolve)

**F1.** Cui et al. (+26% tasks for less-experienced devs) vs METR (−19% for expert maintainers) — resolved provisionally by task-type/expertise differences, not by a unifying study. *(economics)*
**F2.** In-the-wild agent PRs passing human review had *fewer* security smells than human code (Kraishan 2026, OR 0.63) vs lab studies showing ~45% of AI-generated code contains OWASP Top-10 issues — different populations (reviewed vs unreviewed). *(domain-a; economics)*
**F3.** "47% satisfaction increase" and "15-min baseline" Klarna figures are unsourced myths (E12) vs the verified 11→<2 min resolution-time improvement — do not repeat the myths. *(domain-b)*
**F4.** Microservices failure statistics (73% fail; 42% consolidating) are marketing-adjacent and Unverified; first-hand accounts agree on direction, not magnitude. *(spec-arch D1)*
**F5.** AGENTS.md adoption counts (20K/60K) are industry-guide claims, Unverified precise; the cross-tool convention status is Corroborated. *(spec-arch D5)*
