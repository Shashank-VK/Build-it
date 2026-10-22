# Coverage Matrix — DRAFT input for the final research audit

**Built:** 2026-10-10 (assembly) · **Status:** finalized by coordinator. One table per report section (1–19): where official docs sufficed · where practitioner reports added detail · where community discussion revealed recurring problems · where independent tests confirmed or contradicted claims · where sources disagreed · what remains uncertain · what cannot be resolved publicly. Honest and specific — streams and findings named. (Draft note: §§4–6 were not visible when the draft was built; they have since been written and are fully assessed below.)

---

## §1 — Executive findings (synthesis)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | For the company-practice findings: Google SRE workbook (error budgets — Verified), Meta eng blog (Sapling), NVIDIA dev blog ×4 (DOCA, NVCRE — Verified), GitHub Docs (Copilot agent constraints — Verified). |
| Practitioner reports added detail | Nearly all incident narratives (Knight Capital via SEC filings + press; CrowdStrike RCA via vendor + press); the domain-a failure catalogue (Transluce 34.7% oversold success). |
| Community revealed recurring problems | HN ex-employee threads (Google 20% time, Amazon culture); Reddit ex-Nokia engineer (Windows Phone); the review-tax pattern across Keypup/Cursor/LinearB. |
| Independent tests | METR RCTs (Verified, pre-registered); Cui et al. field RCTs; peer-reviewed MDPI paper on GitHub's incident reports; Kraishan 2026 (reviewed-PR security smells, OR 0.63). |
| Sources disagreed | Vendor productivity figures vs independent RCTs (direction and magnitude); lab AI-code vuln rates (~45%) vs reviewed-PR rates (population difference, not contradiction). |
| Remains uncertain | The §18 top-15 unresolved questions; magnitude of review tax; AI-era maintenance cost. |
| Cannot be resolved publicly | Hyperscaler internal defect/security rates; vendor inference costs and training-data composition; whether undisclosed injection breaches occurred. |

## §2 — The Three AI Domains (domain-a, domain-b, domain-c)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | GitHub Docs on the Copilot coding agent (assigned an issue, opens draft PR, never merges on its own — Verified); Anthropic eng blog (in-session security review 16%→54% substantive comments — Corroborated); OpenAI Codex docs; agent-instruction conventions (AGENTS.md — Corroborated as adoption trend). |
| Practitioner reports added detail | The bulk of domain-a's failure catalogue (false "done," green-test illusion, context amnesia); domain-b's RAG dev-to-prod gap (94% demo → 38% production); domain-c's Klarna arc (launch figures via company announcement — Verified; reversal via CEO on-record — Verified). |
| Community revealed recurring problems | Agent-skeptic manifestos and AI-codebase-bankruptcy postmortems (self-selected; base rate unknown); the "70% Problem" as practitioner model (Osmani — illustrative, not measured). |
| Independent tests | Confirmed: 16,017-PR reviewer leaderboard (best F1 ~66%, no tool leads precision+recall — Corroborated); agents' self-written tests barely help (weak assertions 14.63% vs 11.92% human — Corroborated). Contradicted-by-design: METR (−19% experts) vs Cui (+26% tasks juniors) — populations differ. |
| Sources disagreed | Whether the productivity paradox is real (convergent across 5 lines: METR, DORA 2024, Uplevel, GitClear, Stack Overflow 2025 — the disagreement is about *magnitude and population*, not direction). |
| Remains uncertain | B4: junior-employment causality (data Corroborated; AI-attribution contested); review-tax magnitudes (illustrative, not audited); eval judge–human correlation (80–85% practitioner-cited, no primary study). |
| Cannot be resolved publicly | Per-feature inference costs; golden datasets and judge prompts; training-data composition; undisclosed injection breaches; AI-quality SLOs (none published). |

## §3 — The Complete Product Lifecycle (discovery)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Rarely — most framework claims (Torres *Continuous Discovery Habits*, Cagan/SVPG four risks, Blank, Ulwick) reached the research via community skill docs and summaries, not the primary books or svpg.com/producttalk.org. Verbatim quotes from secondaries are attributed, not verified. |
| Practitioner reports added detail | The majority of the stream: opportunity-solution trees, assumption mapping, concierge/WoZ testing guidance, pricing-test methods (Van Westendorp/Gabor-Granger via commercial vendors — methodologically thin). |
| Community revealed recurring problems | "1 in 3 product ideas create measurable positive results" and "41 of 50 MVPs" circulate unaudited — recorded with low confidence and do-not-cite guidance. |
| Independent tests | Todd Little's IEEE data (55 projects) partially supports #NoEstimates (throughput beats story points for uniform work) — Corroborated. Little else is trial-grade. |
| Sources disagreed | Scoring frameworks (RICE/ICE) as decision tools vs structuring tools (Torres rejects quantified scoring for opportunity selection — the disagreement is use, not formula). |
| Remains uncertain | Quantitative base rates for discovery methods; AI-in-discovery empirical magnitudes (direction corroborated, magnitude unknown); support-ticket mining as a citable primary (marked Inferred). |
| Cannot be resolved publicly | Non-English/non-US ecosystem applicability (all sources English, US-centric SaaS); proprietary discovery data inside companies. |

## §4 — Company Case Studies (cases-hyperscale, cases-product, expansion-companies, forensics)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Strong where companies publish: NVIDIA dev blog ×4 (DOCA, NVCRE, Air CI/CD, NIM — Verified); Meta eng blog (Sapling); Google Cloud blog (postmortem template); Atlassian 7,500-word post-incident review (Verified); GitLab's public postmortem lineage; SEC filings (Knight Capital — Verified); FAA statements (Starship). |
| Practitioner reports added detail | Ex-employee accounts (HN/Reddit — individually unverifiable, corroborated in aggregate); the forensics DISMANTLE sections (16 verdicts with receipts); expansion-companies postmortems (Tesla production hell, Vercel VP self-postmortem, GitLab 2017 DMARC-bounced backup alert). |
| Community revealed recurring problems | Recurring outage patterns (Azure ~1/quarter 2025–26; GitHub 8 incidents Jul + 5 Aug 2026 after the April "unacceptable" pledge — via peer-reviewed MDPI paper); Windows Phone autopsy via ex-Nokia engineer; Valve flat-org witnesses vs handbook. |
| Independent tests | MDPI peer-reviewed paper on GitHub's own incident reports; Tom's Hardware on NVIDIA (quoting VP — Corroborated with caveats). |
| Sources disagreed | Official narratives vs forensic verdicts at all 16 companies (Appendix D) — the disagreement is the finding. Google 25% vs 75% AI-code claims (75% flagged as dubious press). Single-source sensationalism flagged (Archyde 75% claim unreliable). Spotify "abandoned the model" (analyst synthesis, single-source). |
| Remains uncertain | Cursor ARR figures (single secondaries); Airbnb AI-productivity figures (company-reported, unaudited); Stripe/Spotify incident narratives (single-sourced); thinnest files (Salesforce Lightning, Pinboard, Jane Street — the audit says so). |
| Cannot be resolved publicly | Hyperscaler internals (CI scale, financials, defect rates); Stripe postmortems (none public — verified absent); Replit canonical postmortem; Jane Street internals (deliberate black box — recorded as such). |

## §5 — AI/Agent Architecture (domain-b, automation, security §24-AI)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Anthropic "Building effective agents" (Dec 2024 — primary); OpenAI agent guide (3 signals); Temporal docs; GitHub Docs (Copilot coding agent: assigned an issue, opens draft PR, never merges on its own — Verified); OWASP LLM Top 10 2026 categories (control detail via reputable secondaries). |
| Practitioner reports added detail | The harness doctrine ("the product is the harness, not the model"); eval methodology (golden datasets, 60/30/10 scoring, judge calibration, production-to-eval loop); RAG demo→production gap; tool-use reliability; agent security control catalog (sandboxing → runtime policy enforcement). |
| Community revealed recurring problems | Prompt-injection incident chronology (2013→2026 CVEs); MCP tool-poisoning research (Invariant Labs, MCPTox); agent failure reports (false "done," green-test illusion). |
| Independent tests | tau-bench 61%→25% across 8 trials; MCP-Universe best 43.7%; 16,017-PR reviewer leaderboard (best F1 ~66%); Kraishan 2026 — in-the-wild agent PRs passing human review had *fewer* security smells than human code (OR 0.63, Verified) — different population from lab-generated code, not a contradiction. |
| Sources disagreed | Lab vuln rates (~45% Veracode/Cobalt) vs field reviewed-PR rates (population difference, provisionally resolved); Anthropic multi-agent 90.2% lift at ~15× token cost (vendor-published, unreplicated — matched-budget critiques noted). |
| Remains uncertain | Judge–human correlation on product tasks (80–85% is LLM-judge *general* calibration, not product-task-specific — no primary study located); per-feature inference costs; golden datasets and judge prompts (none published); AI-quality SLOs (none published). |
| Cannot be resolved publicly | Vendor model internals; training-data composition; undisclosed injection breaches; hyperscaler internal agent-deployment data. |

## §6 — Automation Stack & Workflows (automation)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Temporal docs (retry defaults, 4 timeouts, dedup≠idempotency); AWS Builder's Library (retry/jitter/idempotency); GitHub Actions docs (environments, required reviewers, wait timers); Anthropic multi-agent Research system (vendor-published — Corroborated, not Verified). |
| Practitioner reports added detail | Script-vs-LLM-vs-workflow-vs-agent-vs-multi-agent decision guide (8 labeled rules); all 9 workflow reconstructions with 10-part anatomy; Sentry Seer Autofix mechanics (≥10 events auto-trigger, human merges); Cognition "Don't Build Multi-Agents" + 2026 follow-up. |
| Community revealed recurring problems | HN skepticism of general-purpose swarms; the $50K runaway-agent incident (single-source, flagged); CERT-reported Sentry/Seer indirect-prompt-injection chain; AutoGen maintenance mode. |
| Independent tests | Thin — workflow evidence is implementation-based (public repos, configs), not trial-based. No RCT of workflow shapes exists in the corpus. |
| Sources disagreed | Multi-agent value: Anthropic's 90.2% lift at ~15× cost vs Cognition's convergence on "parallel reads safe, writes single-threaded" — provisionally resolved as different workloads, not a unifying study. |
| Remains uncertain | ~20K-token subagent overhead (single-source); lethal-trifecta incident list; Airflow/Prefect/Step Functions current state (not covered — G-01–G-08); Langfuse/LangSmith details; OpenTelemetry GenAI conventions. |
| Cannot be resolved publicly | Proprietary workflow internals; vendor-internal automation ROI; undisclosed agent incidents. |

## §7 — Authenticity & Anti-Slop (authenticity)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | FTC Consumer Reviews and Testimonials Rule (16 CFR Part 465) — rule text and effective date Verified; penalty figure $51,744 at issuance → ~$53,088 per Dec-2025 warning letters (date-sensitive, via secondaries). |
| Practitioner reports added detail | The anti-slop catalogue ("AI aesthetic," negative parallelism, slop-as-phenomenon); testimonial-authenticity practices. |
| Community revealed recurring problems | "AI-generated websites are the Word Art era all over again" discourse; prompt-specificity findings (vague prompts ⇒ slop). |
| Independent tests | Thin — the stream is consensus- and rule-based, not trial-based. |
| Sources disagreed | No material disagreements recorded. |
| Remains uncertain | Enforcement magnitudes (first FTC actions 2026 via practitioner/legal secondaries; no FTC primary fetched). |
| Cannot be resolved publicly | — |

## §8 — Functional Completeness (quality §21 + ux-states §20)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Limited — the stream's method (route-by-route functional audit) is practitioner-developed. |
| Practitioner reports added detail | The functional-audit methodology; demo-authenticity checks; WoZ as legitimate-with-disclosure (counterexample to AP-14 — Corroborated, textbook HCI). |
| Community revealed recurring problems | Demo-fakery discussions; 100+ fake AI storefronts from a ~$249 toolkit (ux-states E12.4). |
| Independent tests | None trial-grade; the section is method, not measurement. |
| Sources disagreed | WoZ/faked demos: legitimate in research *with disclosure* vs fraud when undisclosed — resolved by the disclosure rule, not in dispute. |
| Remains uncertain | Automated-vs-manual testing mix evidence (quality B spans §§21–22; no controlled experiment on test-type causality). |
| Cannot be resolved publicly | Proprietary QA data inside companies. |

## §9 — Accessibility, Performance & UX (quality §22 + ux-states §§18–19)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Strong: WCAG 2.2 (W3C Recommendation, Verified); EN 301 549 (ETSI versions, Corroborated); web.dev Core Web Vitals thresholds (stable across 2026 sources); DOJ ADA Title II final rule (via SBA Advocacy — Corroborated). This is the section where official sources carry the most weight. |
| Practitioner reports added detail | Baymard/NNG/Google figures on perceived speed, completion lift, hidden-menu costs — cited second-hand via practitioner sources; magnitudes directional, not re-verified. Session-expiry UX rests on practitioner consensus (Proposed). |
| Community revealed recurring problems | Designer blogs and LinkedIn essays on state-design failures; toast/undo duration debates (no primary timing studies — all second-values Proposed). |
| Independent tests | Bernstein & Turban (2018, peer-reviewed): open-plan offices *reduced* face-to-face interaction ~70% — the inverse of intent (cited in expansion-practices; relevant to §9's evidence standard, not its subject). |
| Sources disagreed | Accessibility overlays vs the a11y community: negative evidence sought and found — no overlay has survived a compliance challenge; no contradiction of the Deque 57% figure in 2026 sources. |
| Remains uncertain | OJEU citation timing for EN 301 549 v4.1.1; EAA fine totals (single-studio review); DOJ Title III rulemaking revival; WCAG 3.0 finalization ("a few years"); UK PSBAR (single-source, needs legislation.gov.uk check). |
| Cannot be resolved publicly | Jurisdiction-specific obligations (research, not legal advice — needs counsel); member-state penalty maxima. |

## §10 — Security, Privacy & Governance (security)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Partially: ASVS v5.0 chapter-level alignment (345 requirement IDs not mapped — honest gap); OWASP LLM Top 10 2026 categories (control detail via reputable secondaries); NIST 800-63B-4 restricted-authenticator table inferred, not quoted from primary. CA 2026 children's privacy law via WSGR (Medium-High). |
| Practitioner reports added detail | Injection CVE tables (cyberdesserts); MCP security guidance; the AI-agent security patterns. |
| Community revealed recurring problems | CVE-2025-59944 (Cursor), CVE-2026-24307 and similar injection CVEs circulating in community tables. |
| Independent tests | Vendor studies agree directionally (Veracode 44% introduce known vulns; Cobalt 55.8% via formal verification; SonarQube 53% "looks right, hides defects") — magnitudes discounted for vendor incentive. Counter-evidence: Kraishan 2026 — in-the-wild agent PRs passing human review had *fewer* security smells than human code (OR 0.63, Verified) — different population from lab-generated code, not a contradiction. |
| Sources disagreed | The lab-vs-field gap above; single-vendor telemetry (CrowdStrike 150 techniques/300k prompts) treated as attributed/directional. |
| Remains uncertain | 2026 LLM Top 10 per-risk control detail (122pp PDF not fully mined); US state breach-notification per-state detail; 2026 GDPR/EDPB developments. |
| Cannot be resolved publicly | Whether undisclosed injection breaches occurred at major vendors; hyperscaler internal security rates; vendor model internals. |

## §11 — Testing, Quality, Deployment & Ops (build-ship §§11–13 + automation + quality §23)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Google SRE Workbook (error budgets — Verified); GitHub Actions docs (Copilot agent runs on ephemeral runners, never merges — Verified); CrowdStrike RCA (Verified via vendor + press); SEC Order 34-70694 for Knight Capital (Verified). |
| Practitioner reports added detail | The deployment postmortems (Knight $440M/45min; CrowdStrike 8.5M devices; Cloudflare/AWS/Azure 2025 outages); chaos-engineering principles; Kohavi experimentation pitfalls (SRM, peeking, Twyman's law — practitioner synthesis, Corroborated). |
| Community revealed recurring problems | dev.to postmortem syntheses (Google June-2025 null-check outage; Cloudflare Nov-2025 ClickHouse outage); the "alerts without owners" pattern (Knight's 97 ignored emails). |
| Independent tests | Thin at the trial level; the section leans on postmortem evidence (strong on mechanism, weak on base rates). |
| Sources disagreed | No material disagreements; the automation stream's preserved contradictions (D section) are kept unresolved by design. |
| Remains uncertain | Causal effect of test-type mix on escaped defects (no controlled experiment); Google-scale flakiness (2016 figure dated); Temporal retry/timeout defaults per SDK (automation G-06). |
| Cannot be resolved publicly | Proprietary incident data; vendor-internal deployment machinery (e.g., Tesla's — verified absent). |

## §12 — Business Viability (build-ship §14 + domain-c economics)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Minimal — the stream is practitioner-consensus heavy. |
| Practitioner reports added detail | AARRR funnel; activation benchmarks (D1 40–60%, D7 20–40%, D30 10–20% — Low confidence, ranges not measurements); freemium conversion (2–5% typical — Low); unit-economics floors (LTV:CAC ≥3:1 — practitioner consensus, not research). |
| Community revealed recurring problems | AI SaaS shifting to usage-based pricing to recover inference costs (2026 practitioner consensus). |
| Independent tests | None — this is the thinnest-evidence section in the report by the research's own labeling (mostly Low/C). |
| Sources disagreed | No direct contradictions; the numbers are ranges with acknowledged variance by segment. |
| Remains uncertain | Nearly all viability benchmarks (segment-dependent, unaudited). |
| Cannot be resolved publicly | Proprietary unit economics; company-internal funnel data. |

## §13 — Bottleneck Analysis (economics)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | DORA reports (2024-vintage via mirrors — treat tier numbers as approximate); SPACE framework (ACM Queue 2021 — established); DX Core 4 (vendor framework, benchmarks vendor-sourced). |
| Practitioner reports added detail | DX analyses (median +7.7% PR throughput, nobody hit 10x); Uplevel (800 devs: +41% bugs, no throughput gain); GitClear longitudinal cuts. |
| Community revealed recurring problems | The review-burden pattern across Keypup/Cursor/LinearB/Kraishan (direction Corroborated; magnitudes unaudited). |
| Independent tests | METR 2025 RCT (16 experts, −19%, pre-registered — Verified for its population); METR 2026 follow-up (weak evidence only); Cui et al. field RCTs (+26% tasks for less-experienced — Verified); Peng et al. (+55% lab). The RCTs disagree by population and task type — task-count gains for juniors on scoped tasks vs slowdowns for experts on familiar codebases. |
| Sources disagreed | Cui (+26%) vs METR (−19%) — provisionally resolved by population/task differences, not by a unifying study (kept as open contradiction F1). |
| Remains uncertain | Waiting-time decomposition; queue lengths by provenance; spec-time measurement; first-pass success rate; MTTR under AI adoption (all Unknown — §18 #1–6). |
| Cannot be resolved publicly | Org-level cost data (nobody publishes cost per verified result); vendor-internal productivity data. |

## §14 — Rules & Anti-Patterns (rules)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | SEC enforcement (Knight Capital — Verified); CrowdStrike RCA (Verified); the rules' canonical-book claims rest on secondary confirmation, not re-fetched primaries (labelled Corroborated, not Verified — honest). |
| Practitioner reports added detail | The 34 rules and 19 anti-patterns themselves; E-CONWAY (cognitive load); the small-team OS (17 components). |
| Community revealed recurring problems | Resume-Driven Development (peer-reviewed: 60% of hiring influenced by trends — empirically corroborated); "never rewrite" dogma debates. |
| Independent tests | Colfer & Baldwin (142 studies) bounding Conway's Law — prevalent, not universal (Corroborated with a real boundary). |
| Sources disagreed | "Never rewrite" (Spolsky/Netscape) vs the Firefox rescope that worked — resolved as "never *big-bang* rewrite"; strangler migrations succeed. Magic Leap demo dispute: used as reported, not adjudicated. |
| Remains uncertain | DORA tier numbers (2024-vintage); ASVS v5 requirement counts (~345–346, minor variance preserved). |
| Cannot be resolved publicly | — |

## §15 — Reference Architecture (spec-arch + automation stack + rules/03)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | CNCF/Backstage docs (maturity model); Temporal docs (timeouts — Go SDK values, other SDKs unverified per automation G-06); modelcontextprotocol.io. |
| Practitioner reports added detail | Prime Video (−90% cost), Segment, InVision, Istio reversions — Corroborated named cases; the failure is premature distribution, not distribution. SQLite-at-scale patterns; single-binary deployments. |
| Community revealed recurring problems | The fabricated "42% consolidating" statistic — discourse outran evidence (kept as a caution, not a finding). |
| Independent tests | None trial-grade; architecture evidence is case-based. |
| Sources disagreed | Microservices success/failure statistics (73% fail / 42% consolidating — marketing-adjacent, Unverified; first-hand accounts agree on direction only — spec-arch D1). |
| Remains uncertain | Team-size thresholds (D2); DB QPS crossover heuristics (D3, interview-guide rules of thumb); AGENTS.md adoption counts (D5, industry-guide claims); caching/queue cost specifics (D7, vendor- and date-dependent). |
| Cannot be resolved publicly | Internal architecture-review data; proprietary cost figures. |

## §16 — Implementation Roadmap

| Dimension | Assessment |
|---|---|
| Note | The section header states the entire roadmap is **Proposed** — a synthesis derived from the lifecycle research, small-team OS, quality gates, bottleneck analysis, rules, discovery, and templates. It makes no empirical claims of its own; coverage is inherited from §§3, 11, 13, 14, 15, 17. Nothing to audit beyond the supporting findings' labels. |

## §17 — Checklists & Templates

| Dimension | Assessment |
|---|---|
| Note | Index + highest-leverage checklists drawn from rules/04 (18 templates), discovery/01 & /03 (gates), quality/03 (9 gates). Coverage follows the home sections (§§3, 11, 14); the artefacts are Proposed tools, not empirical claims. |

## §18 — Evidence Register (report section)

| Dimension | Assessment |
|---|---|
| Note | The reading guide + ~40 highest-confidence findings + top-15 unresolved questions + pointers. It cites this evidence directory's `merged-evidence-register.md` (1,081 rows) as the full proof layer. Coverage is meta — it inherits the strengths and gaps of every section above. |

## §19 — Missing Topics (gaps)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | FTC rule text (Verified); Stanford "Canaries" paper exists (findings via six corroborating outlets — Corroborated; mechanism is authors' interpretation). |
| Practitioner reports added detail | Most topics: Keypup review-tax (vendor — mechanism Corroborated, figures illustrative); Kaamfu Klarna analysis (vendor-framed); platform-adoption crisis (single secondary — Inferred); i18n mechanics (six convergent 2026 practitioner sources — Corroborated as consensus). |
| Community revealed recurring problems | Backstage maintenance trap; "we'll i18n after launch" retrofit pattern (asserted, not measured — Inferred). |
| Independent tests | Stanford ADP payroll (millions of workers — Corroborated); GitClear cuts (vendor data, correlational — Corroborated direction). |
| Sources disagreed | Junior-employment causality (data vs attribution); the $60M Klarna framing (domain-b E11 asserts; gaps stream excluded it as unverified — kept as open contradiction F3); Meta mandate outcomes vs gaming (Unknown). |
| Remains uncertain | T7 discipline framing (Inferred from failures; no primary hardware-eng source); T11 retrofit-cost quantification (Inferred); platform-adoption figures (single secondary); Backstage ~89% share (excluded as unverified). |
| Cannot be resolved publicly | Meta internal documents (press-reported); Gurley essay primary (four consistent secondaries); exact vendor internals. |

## Case-study material (report §04 + Appendices A/D)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Strong where companies publish: NVIDIA dev blog ×4 (DOCA, NVCRE, Air CI/CD, NIM — Verified); Meta eng blog (Sapling); Google Cloud blog (postmortem template); Atlassian 7,500-word post-incident review (Verified); GitLab's public postmortem lineage. |
| Practitioner reports added detail | Ex-employee accounts (HN/Reddit — individually unverifiable, corroborated in aggregate); the forensics DISMANTLE sections (16 verdicts). |
| Community revealed recurring problems | Recurring outage patterns (Azure ~1/quarter 2025–26; GitHub 8 incidents Jul + 5 Aug 2026 after the April "unacceptable" pledge — via peer-reviewed MDPI paper). |
| Independent tests | MDPI peer-reviewed paper on GitHub's own incident reports; Tom's Hardware on NVIDIA (quoting VP — Corroborated with caveats). |
| Sources disagreed | Official narratives vs forensic verdicts at all 16 companies (Appendix D) — the disagreement is the finding. Single-source sensationalism flagged (Archyde 75% claim unreliable). |
| Remains uncertain | ARR figures (Cursor); Airbnb AI-productivity figures; Spotify "abandoned the model" (single-source); Stripe/Spotify incident narratives (single-sourced). |
| Cannot be resolved publicly | Hyperscaler internals (CI scale, financials, defect rates); Stripe postmortems (none public — verified absent); Replit canonical postmortem; Spotify current org model primary. |

## Appendices A–D (expansion + forensics)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Appendix B: vendor docs for active tools; Appendix D: SEC filings, FAA statements, GitHub READMEs (SimianArmy retirement — Verified). |
| Practitioner reports added detail | The bulk of all four appendices; Appendix A company files mix primary postmortems with press. |
| Community revealed recurring problems | Appendix C's fringe (vibe-coding equivocation; the fabricated 42%); Appendix B's pricing controversies. |
| Independent tests | Appendix C: Bernstein & Turban (peer-reviewed); RDD paper (n=591, peer-reviewed). |
| Sources disagreed | Appendix A: Valve handbook vs witnesses; Appendix D: 16 narrative-vs-evidence contradictions. |
| Remains uncertain | Appendix B depth debt (long lightly-researched list); Appendix A thinnest-evidence files (Pinboard, Salesforce Lightning). |
| Cannot be resolved publicly | Jane Street internals (black box — recorded as such); LinkedIn-walled practitioner posts. |

## §20 — Compulsory Disciplines (follow-up phase: D1–D13)

| Dimension | Assessment |
|---|---|
| Official docs sufficed | Strong where the discipline has canonical docs: Stripe API versioning (fetched primary — Verified); APNs/FCM mechanics; Gmail/Yahoo bulk-sender rules (Verified); EU AI Act text via EUR-Lex and AI Office trackers (Verified); AICPA Trust Services Criteria and ISO 27001:2022 Annex A (Corroborated); FinOps Foundation framework (Verified); PCI DSS v4.0 requirement texts (Corroborated). |
| Practitioner reports added detail | The bulk of all nine streams: T&S forensic verdicts per company; billing failure catalog (12 items, several Verified via commits); mobile rejection war stories (2026, first-hand); Duolingo KDD 2020 paper (Verified primary); Uber CCG eng blog (Verified); compliance theater mechanics; FinOps forensic re-readings (Prime Video/37signals/Dropbox/Segment); data-contract playbooks; multi-tenancy bridge model; CUPED-at-hyperscalers pattern; Zillow drift analysis. |
| Community revealed recurring problems | Reviewer-welfare litigation (Kenya/Sama); hate-raid tooling gaps; notification fatigue surveys; SOC 2 velocity-tax discourse; repatriation debates; chargeback program-killers; stale-flag incidents; silent schema-drift stories. |
| Independent tests | Thin at the trial level across all nine — these disciplines rest on case/postmortem evidence, not RCTs. Exceptions: Duolingo bandit paper (peer-reviewed); Kraishan-style field data where cited; Monte Carlo/dbt surveys (vendor, direction-trusted). |
| Sources disagreed | Repatriation narratives vs forensic counterfactuals (Prime Video/37signals/Dropbox — resolved as service-selection/bundled/non-generalisable); vendor productivity figures vs independent evidence (standing rule applied); TikTok automation-accuracy claims vs documented evasion failures (unresolved contradiction flagged); Zillow "drift did it" vs pre-model-decision counter-argument (both preserved, same engineering implication). |
| Remains uncertain | First AI Act fine (none reported as of Oct 2026); enforcement behavior of market surveillance authorities; harmonized-standards stack; cross-platform T&S effectiveness benchmark (none exists); compliance velocity tax (no audited measurement); FinOps program ROI (no controlled measurement); single-secondary attribution debt (Netflix Guardian figures, Uber Michelangelo, Peloton miss, Airbnb/LinkedIn internals); Stripe V2 and Adyen ledger internals. |
| Cannot be resolved publicly | Hyperscaler T&S cascade internals (thresholds, queue algorithms); vendor model internals and training-data composition; undisclosed injection breaches; proprietary billing ledgers; internal API-governance staffing; Apple/Google review-team staffing and appeal overturn rates; jurisdiction-specific legal obligations (research, not legal advice). |
