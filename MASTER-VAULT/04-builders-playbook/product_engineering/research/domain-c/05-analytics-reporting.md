# Domain C — AI Automating Organisational Work: Analytics & Reporting

**Workstream:** domain-c · **Area 5 of 8** · Researched 2026-10-10

> Scope: AI that does the organisation's analytical work — natural-language querying of data, automated report generation, anomaly detection, root-cause investigation, dashboard narration. The consumers are managers and executives making decisions; a wrong number here lands in a board deck.

**Plain-English terms:**
- **NL-to-SQL** — you type "revenue by region last quarter" and the AI writes the database query. Concrete example: asking "why did churn rise 12%?" and getting a chart. The deeper mechanics: the model must map your words to the actual table and column names in a messy company database — this mapping is where most failures happen.
- **Semantic layer / semantic model** — the company's agreed definitions of metrics ("active customer," "revenue") stored as governed metadata. Without it, the AI guesses which definition you meant.
- **The "almost-right tax"** (InfoWorld's term) — the time humans spend debugging and fact-checking AI-generated analysis because it doesn't quite understand company-specific rules.
- **Text-to-SQL benchmarks (Spider 2.0)** — standardised tests of how well models turn English into correct database queries on realistic enterprise schemas.

---

## 1. How organisations deploy it

Two architectural postures, with very different reliability:

**Posture A — chat on top of BI (most common, least reliable):** an NL interface bolted onto existing dashboards/warehouse. The model generates SQL against raw schemas. Fast demos, brittle in production.

**Posture B — governed investigation layer (the pattern serious deployments converge on):**
1. Governed semantic model defines every metric once (Looker's "source of truth" approach).
2. NL queries resolve against the semantic model, not raw tables.
3. The AI tests multiple hypotheses for "why" questions (not just "what" charts).
4. A review/validation layer (sometimes a second "skeptic" agent) checks logic, statistics, and causation-vs-correlation errors before delivery.
5. Outputs carry assumptions, data sources, and lineage — decision logic a human can validate.

One open-source reference implementation (GitHub: rakshitkaintura/data_analytics_automation) runs a **16-node LangGraph pipeline** — query understanding, SQL generation, LLM-as-judge SQL evaluation *before* execution, retry loop with error feedback, a **Skeptic Agent** that adversarially reviews every insight (logical consistency, statistical rigor, causation vs correlation), and a **Reflection Agent** that distills each SQL failure into a reusable rule so the same mistake is never repeated. This is the state of the art in *oversight architecture*, from a builder's repo (first-hand/community evidence).

## 2. Documented cases and evidence

**The business-context failure (InfoWorld, ~Aug 2025 — Corroborated):**
Models are "great at syntax, mediocre at semantics, and really bad at business context." The value hides in seams: how the org defines *active customer*, which discount codes apply on Tuesdays, SKU names changed after the acquisition, why *revenue* means different things to Finance vs Sales. On Spider 2.0 enterprise-schema benchmarks, models peak around **59% exact-match accuracy**, falling to ~**40%** with transformation/code complexity. "The closer we get to real business context, the more the artificial intelligence struggles."

**Google's admission by design (Corroborated — product documentation):**
Looker's Conversational Analytics is explicitly grounded in the existing Looker semantic model, described as "the source of truth," *specifically so responses stay accurate and consistent*. Read plainly: without a governed semantic layer behind it, the same NL interface would be guessing. (BuildBerg analysis, Sept 2026.)

**The governance response (Gartner prediction — Corroborated):**
By 2028, **half of all organisations will adopt zero-trust data governance models specifically because unverified AI-generated data is accumulating inside their systems** — i.e. enough companies have been burned by confident wrong answers that "verify before you trust it" is becoming a formal governance category.

**Vendor framing to treat sceptically:**
Scoop Analytics' content (Medium posts by Scoop-affiliated authors — vendor marketing) draws a useful conceptual line between *automation* (faster dashboards, NL queries, anomaly alerts) and *investigation* ("here's why, here's the evidence, here's what it costs, here's what to do"), and proposes a three-layer architecture (automatic data prep, real ML execution, business-language translation). The distinction is analytically sound; the product claims are **Unverified**.

## 3. Measured outcomes

| Metric | Value | Label |
|---|---|---|
| NL→SQL exact match, enterprise schemas (Spider 2.0) | ~59% peak, ~40% with complexity | Benchmark — Corroborated |
| Org adoption of zero-trust data governance by 2028 | 50% (prediction) | Gartner — Corroborated prediction |

Note: the public record is thin on *measured business outcomes* of AI analytics deployments (decision quality, time-to-insight with baselines). Most published material is vendor framing or benchmark scores, not field results. **This is itself a finding: the evidence base for "AI analytics ROI" is weaker than for support or AP automation.**

## 4. Failure modes

1. **Confident wrong numbers**: the model produces plausible SQL that is logically wrong (bad joins, wrong date logic, wrong metric definition) — "hallucinates with confidence" per a verified G2 reviewer quoted in industry coverage.
2. **Metric-definition drift**: two departments' different definitions of "revenue" produce two different answers to the same question; without a semantic layer there is no tiebreaker.
3. **Schema evolution brittleness**: a new CRM field breaks the NL interface until someone updates the semantic model ("wait for IT").
4. **Causation laundering**: the AI presents a correlation as a recommended action without evidence grading.
5. **Unverified data accumulation**: AI-generated figures get copied into decks, docs, and downstream datasets, compounding error (the driver of the Gartner zero-trust prediction).
6. **The board-deck problem**: no built-in mechanism tells the user whether the answer was fast-and-confident or actually correct.

## 5. Human oversight / approval design

- **Semantic-layer governance**: metric definitions owned, versioned, and change-controlled — the single highest-leverage control.
- **Skeptic/red-team review**: a second agent (or human analyst) adversarially reviews insights for logic, stats, and causation errors before delivery.
- **LLM-as-judge SQL evaluation** before execution; retry loops with error feedback; failure-distillation into persistent rules (the Reflection Agent pattern).
- **Provenance on every figure**: assumptions, data sources, query logic attached; "explain how you reached that recommendation" must return decision logic, not confidence scores.
- **Tiered autonomy**: exploratory analysis can be AI-led; anything entering a forecast, filing, or board deck gets human sign-off.

## 6. Cost vs benefit

- Where it works: collapsing the question→answer loop for *well-defined* metrics on *governed* data (hours of analyst slicing → seconds).
- Where it doesn't: the "almost-right tax" — analyst time spent verifying AI output can exceed the time saved generating it, especially on messy schemas. The 59%/40% benchmark figures quantify the ceiling.
- The investigation-vs-automation distinction matters for buying: most vendors sell Level 1 (faster charts) as "AI-powered"; the expensive part is the semantic and validation layers.

## 7. Data governance / privacy

- NL interfaces widen data access: anyone who can ask can potentially reach any table the interface can query — row/column-level security must be enforced in the query path, not the UI.
- Query logs are sensitive (they reveal what executives are investigating — M&A, layoffs); treat as confidential.
- AI-generated datasets need lineage labels so downstream users know a figure was machine-generated and unverified.

## 8. Open gaps

- Almost no published field measurements of decision-quality improvement or time-to-insight with proper baselines.
- No standard for "verified" vs "unverified" AI-generated figures inside BI tools.
- Benchmark scores (Spider 2.0) measure query correctness, not business usefulness.
