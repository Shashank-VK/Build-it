# Cursor (Anysphere) — Forensic Supplement

**Workstream:** forensics · **Researched:** 2026-10-10 · Read-only research; no installation, building, ranking, or recommendation.
**Supplements:** `../cases-product/10-cursor.md` (dogfooding, custom models, feature spectrum, transparency critique). This file reconstructs the company machinery (hiring, stack, the SpaceX acquisition), adds the **2026 business-record the sibling missed** (pricing revolt, $60B SpaceX acquisition, OpenAI model cutoff), and audits the narratives.
**Confidence key:** **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown**. All sources accessed 2026-10-10.
**Scope note:** Cursor publishes minimal first-party engineering writing; this file leans on CEO interviews, hiring-process documentation, and press. Numerical claims are third-party unless noted.

---

## PART 1 — REVERSE-ENGINEER: how the machine actually works

### The hiring machine (the best-documented part of the company)

**CU-R1 — The 2-day work trial as the decision mechanism.** The interview loop (documented in github.com/ombharatiya/ai-engineer-interview-questions, 2026): recruiter screen → 1–3 technical rounds (live coding: filesystem/dedup, hash trees over repo data, streaming/editor primitives) → **on-site work trial up to two days in SF** (desk, laptop, frozen codebase snapshot; some reports: paid 8–9 hour project day ending in presentation/video debrief of tradeoffs) — "Can you go end-to-end in an unfamiliar real codebase? What do you build when left alone without direction?" **The trial is the decision round.** Culture fit via meals and founder conversation. Truell (a16z/Lenny's podcasts): hires ~1 person every 2–3 months early on and "obsesses over" each; self-critique: "we actually hired too slow" early, over-indexing on brand-name schools — "spent a bunch of time on the wrong profile" (corrected toward nontraditional/later-career profiles). · **Corroborated (CEO statements via podcasts + candidate reports)** · Sources: github.com/ombharatiya/ai-engineer-interview-questions/blob/HEAD/14-company-interview-questions/cursor-anysphere.md; github.com/memories-ai-labs/ai-founder-kb/by-source/lenny-s-podcast.md (Lenny's Newsletter, 2026); github.com/amitgaur/ai-interviewing/research/anchor-cursor.md. · *Engineering implication: the trial selects for exactly the company's product thesis — autonomous end-to-end building. The hiring machine and the product are the same idea.*

**CU-R2 — The deliberate AI-in-screens ban.** The company whose product is AI-assisted coding **forbids AI use in its own technical screens**: Truell's reasoning (via amitgaur synthesis): (1) signal purity — unassisted programming as "a really great time-boxed test for skill and intelligence"; (2) don't filter on tooling familiarity ("much rather hire those people and then teach them on the job"); (3) the 2-day trial observes real working style (including AI use) in the default team environment. Selecting for: generalists who ship fast, bottom-up experimentation instinct, genuine passion for the problem space. · **Corroborated (CEO statements via secondary synthesis)** · Source: github.com/amitgaur/ai-interviewing/research/anchor-cursor.md. · *Forensic note: this is a genuine contrarian practice with a coherent rationale — and a natural experiment. If the "AI-native hiring" wave is right, Cursor's screen is wrong; if raw capability still predicts, it's right. No outcome data either way (gap).*

**CU-R3 — Stack and scale (reconstructed).** ~100–150 employees (2026; Truell: "as we've grown to about 100 people," CEO Insider interview); SF-concentrated; stack: TypeScript/React (editor), Rust (performance-critical components), Python (ML/eval), custom ML infra for training coding models (techinterview.org, 2026). Tooling: Notion (wiki/eng docs), Slack, Cursor (dogfooding). Truell's operating maxims: "macro optimists and micro pessimists"; "be skeptical of advice"; "started with a solution in search of a problem... it worked because we stuck with it." · **Corroborated (CEO interview + third-party guides)** · Sources: ceoinsider.io/interview/michael-truell; techinterview.org/companies/cursor/.

### The business machine (2025–2026)

**CU-R4 — The ARR trajectory (third-party, widely repeated).** ARR: $100M (Jan 2025) → $500M (Jun 2025) → $1B (Nov 2025) → $2B (Feb 2026) → $3B (Apr 2026) → **$4B (Jun 2026)** — "evidence that value in an AI coding app is built fast and lives in distribution, workflow, and data, not in any single rented model" (ainvest, 2026-08). All figures third-party; treat as **Unverified** individually, directionally consistent across sources. · **Unverified (multiple secondaries agree on trajectory)** · Sources: ainvest.com/news/openai-cut-cursor-5-figure-holds-leverage-2608/ (2026-08); dataconomy.com (2025-12, $1B + TechCrunch profitability concerns).

---

## PART 2 — POSTMORTEM: the public failure record (beyond the sibling file)

Sibling covered: transparency critique (no SWE-bench, removed blog post); pricing backlash noted as unverified gap. **This pass fills the gaps:**

**CU-P1 — The pricing revolt (July 2025).** Investors flagged AI coding editors "losing money thanks to high costs they paid to the model makers" (TechCrunch, 2025-12-09); Anysphere shifted Cursor **from flat subscription to usage-based pricing, directly passing API fees to users** — producing surprise bills and "an uproar among some of its users" / "widespread complaints... about transparency and affordability." Truell's rationale: usage evolved from "a quick JavaScript question" to "hours of work" — "the pricing model had to shift." Enterprise response: a dedicated team building cloud-like cost-management tooling (spend controls, billing groups, visibility dashboards). · **Corroborated (press, CEO on record)** · Sources: techcrunch.com/2025/12/09/why-cursors-ceo-believes-openai-anthropic-competition-wont-crush-his-startup/; dataconomy.com/2025/12/10/cursor-ceo-says-no-ipo-planned-as-revenue-hits-1b/. · *Forensic note: the unit-economics crisis hit the AI-coding pure-play first and hardest — the same token-economics wall Microsoft and Meta hit internally (02-microsoft.md F10, 03-meta.md F10), but as an existential pricing event rather than a cost-cap memo.*

**CU-P2 — The SpaceX acquisition ($60B, Aug 2026).** SpaceX announced the all-stock acquisition of Anysphere in June 2026; completed mid-August 2026. In April 2026 Cursor had announced a partnership to use SpaceXAI's Colossus compute for model training (compute-constrained). Post-acquisition: Truell's Compile 26 keynote — "over 95% of Cursor users no longer write code... they manage agents"; Origin (agent-native Git platform, "a shot at GitHub"); a from-scratch model backed by SpaceX. · **Corroborated (press)** · Sources: businesstimes.com.sg (2026-08-29); ciol.com (2026-08); YouTube Compile 26 keynote summary (hyperautomationlabs). · *Implication: the independent "fastest B2B SaaS" story ended in absorption — the compute moat (Colossus) mattered more than the ARR.*

**CU-P3 — OpenAI cuts off Cursor's models (Aug 28, 2026; shutoff Nov 12, 2026).** OpenAI notified SpaceX it would wind down model provision to Cursor, citing inability to be "confident that SpaceX will use our technology within our terms of service, based on our experience with Elon Musk's companies violating contracts" (specifically: X's post-acquisition breach; Musk's admission under oath that xAI violated ToS). OpenAI stressed **Cursor itself was not accused of violating terms** — the trigger was the change-of-control clause. Truell's response: "sorry to see" it; **OpenAI models serve ~5% of Cursor traffic** ("narrow but real"); in talks to resolve. Musk: "I couldn't care less." Anthropic's Tom Brown: "Cursor has been a trusted partner of Anthropic since Sonnet 3.5. We'll continue to increase compute to support Claude models in Cursor." · **Corroborated (press, all sides on record)** · Sources: businesstimes.com.sg (2026-08-29); wccftech.com (2026-08-29); ciol.com (2026-08); ainvest.com (2026-08). · *Forensic note: the 5% figure is the single most illuminating number in the AI-coding business — it quantifies how little the "model underneath" matters to the product's value (distribution, workflow, data). It also shows model supply is a *political* risk, not just a technical one: your inference provider can become your adversary's adversary.*

---

## PART 3 — DISMANTLE: narratives vs evidence

### D1 — "The model is the product" vs the 5% figure
- **Official narrative (industry default):** AI coding tools are wrappers; the lab's model is the product; better model = better tool.
- **Contradiction:** Cursor's ARR went $0.1B→$4B in 16 months "without ever being tied to any single lab's model" (ainvest); when OpenAI cut supply, Truell revealed OpenAI models were **~5% of traffic** — and the business didn't blink. Anthropic immediately offered *more* compute.
- **Forensic verdict:** The wrapper thesis is backwards for the winner: **distribution + workflow + data > model**. The multi-sourcing (Anthropic as the deep partner since Sonnet 3.5, own Composer model in development) is the structural reason. Any analysis valuing AI-coding companies on "which model they use" is measuring the wrong thing. · **Verdict: narrative dismantled — with the company's own number as the receipt (Corroborated).**

### D2 — "Fastest-growing B2B SaaS" vs the unit-economics revolt
- **Official narrative:** Hypergrowth ($4B ARR, fastest to $1B).
- **Contradiction:** The growth was built on a pricing model (flat subscription) that **lost money on heavy users** — the July 2025 forced migration to usage-based pricing and the user uproar show the growth was partly subsidized by mispriced inference. The "fastest" record was set while selling dollars for ninety cents on the heaviest usage.
- **Forensic verdict:** Growth real (directionally), profitability of that growth questionable at the time. The honest version: Cursor grew fastest by underpricing its COGS, then repriced. This is the standard blitzscale playbook — the dismantling target is anyone citing the ARR as evidence of *business-model* strength rather than *distribution* strength. · **Verdict: narrative qualified (Corroborated).**

### D3 — "Independent disruptor" vs the SpaceX absorption
- **Official narrative (2023–2025):** The MIT-student startup out-executing Microsoft/GitHub.
- **Contradiction:** By Aug 2026 the company is a SpaceX division; its model-training future depends on Colossus; its model supply depends on Anthropic's goodwill and OpenAI's forbearance. The independence was a phase, not a structure.
- **Forensic verdict:** Not a failure — $60B is a win by any measure — but the "disruptor" narrative's endpoint matters: **the AI-coding market consolidated into compute owners and distribution owners**, and Cursor chose to become part of a compute owner. The remaining question (open): whether SpaceX ownership changes the product's neutrality as a multi-model platform. · **Verdict: narrative closed by acquisition — record the endpoint (Corroborated).**

### D4 — The transparency gap (extends sibling)
- Sibling's critique stands and sharpens: no SWE-bench scores published, a removed blog post, proprietary benchmarks — "the engineering is impressive, but the evidence is harder to verify than it should be" (The AI Engineer, 2026-03). **New evidence for the file:** the company's biggest 2026 claims (95% of users manage agents; 3x faster cloud agents; 6M+ automation runs; Amplitude's 20,000-component migration) come from a **keynote marketed by a third-party YouTube channel**, not from an engineering blog. The transparency posture hasn't changed with scale. · **Corroborated (critic) + new instance.**

---

## EVIDENCE REGISTER (forensics additions)

| ID | Claim | URL | Source type | Author/org | Pub date | Accessed | Confidence | Corroboration / contradictions |
|---|---|---|---|---|---|---|---|---|
| CUFR-01 | 2-day work trial as decision round; hire 1 per 2–3 months; "hired too slow" self-critique | https://github.com/ombharatiya/ai-engineer-interview-questions/blob/HEAD/14-company-interview-questions/cursor-anysphere.md ; https://github.com/memories-ai-labs/ai-founder-kb/blob/HEAD/by-source/lenny-s-podcast.md | Secondary (candidate reports + CEO podcast via notes) | community (Lenny's Newsletter source) | 2026 | 2026-10-10 | Medium | — |
| CUFR-02 | AI banned in own screens: signal purity; don't filter on tooling; trial observes real style | https://github.com/amitgaur/ai-interviewing/blob/HEAD/research/anchor-cursor.md | Secondary (CEO statements via synthesis) | community (Truell statements) | 2026 | 2026-10-10 | Medium | — |
| CUFR-03 | ~100–150 people; TS/React/Rust/Python; Notion/Slack; "macro optimists, micro pessimists" | https://ceoinsider.io/interview/michael-truell ; https://techinterview.org/companies/cursor/ | Secondary (CEO interview + guide) | CEO Insider; TechInterview | 2026 | 2026-10-10 | Medium | — |
| CUFR-04 | Pricing revolt: flat→usage-based (July 2025); investor loss concerns; surprise bills; enterprise cost tooling | https://techcrunch.com/2025/12/09/why-cursors-ceo-believes-openai-anthropic-competition-wont-crush-his-startup/ | Secondary (press, CEO on record) | TechCrunch | 2025-12-09 | 2026-10-10 | Medium-high | Corroborated by dataconomy |
| CUFR-05 | SpaceX $60B all-stock acquisition (announced June, completed mid-Aug 2026); Colossus partnership (Apr 2026) | https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/openai-end-agreement-spacexs-ai-coding-tool-cursor-deepening-musk-altman-clash | Secondary (press) | Business Times (Reuters) | 2026-08-29 | 2026-10-10 | Medium-high | Corroborated by ciol, stockopedia |
| CUFR-06 | OpenAI cutoff (Aug 28, 2026; shutoff Nov 12); change-of-control clause; Cursor not accused; 5% traffic figure; Anthropic offers more compute | https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/openai-end-agreement-spacexs-ai-coding-tool-cursor-deepening-musk-altman-clash ; https://wccftech.com/anthropic-pounces-as-openai-abandons-spacexs-cursor-vowing-to-increase-claude-compute-even-as-openai-cites-contract-distrust/ | Secondary (press, all sides quoted) | Business Times; WCCFTech | 2026-08-29 | 2026-10-10 | Medium-high | — |
| CUFR-07 | ARR trajectory $0.1B→$4B (Jan 2025–Jun 2026); value in distribution/workflow/data | https://www.ainvest.com/news/openai-cut-cursor-5-figure-holds-leverage-2608/ | Secondary (trade press) | AInvest | 2026-08 | 2026-10-10 | Low-medium (third-party figures) | Directionally consistent across sources |

## GAPS (this workstream, Cursor)
- First-party engineering writing (almost none exists publicly).
- Outcome data on the AI-free-screen hiring philosophy (the natural experiment, unmeasured).
- Independent audit of ARR figures.
- Whether SpaceX ownership affects multi-model neutrality (open question).
- Internal incident/quality record (Unknown).
