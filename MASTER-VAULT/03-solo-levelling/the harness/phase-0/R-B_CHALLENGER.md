# R-B CHALLENGER — P0-02 Archetype Longlist (JTBD) + P0-08 Metric Relevance Matrix

**Method:** Deliberately NOT starting from vendor taxonomy (chatbot/RAG/agent/code-gen). Started from Jobs-To-Be-Done: what does a solo/small-team builder actually *hire* software to do? Functional + Emotional + Social jobs (Christensen). Vocabulary intentionally diverged from R-A: `jobs to be done developer`, `solo founder project types`, `indie hacker archetypes`, `internal tools taxonomy glue work`, `browser automation RPA scraping taxonomy`, `content pipeline creator economy` — not `AI tool categories / LLM benchmarks`.

---

## P0-02: JTBD-Derived Archetype Longlist (12)

### JTBD Clusters → Archetypes

| # | JTBD (what builder hires product to do) | Archetype (name) | Technical Type(s) | Who hires it |
|---|---|---|---|---|
| **A1** | Ship revenue product that strangers pay for | **Revenue Product** — multi-tenant SaaS / marketplace / mobile app with auth, billing, tenancy | Next.js/Supabase/Stripe, auth, webhooks, subscriptions | Solo founder → paying users |
| **A2** | Give trusted team a UI over their own DB | **Internal Tool / Admin CRUD** — single-tenant, trusted users, no billing, fast CRUD | Retool, Lovable, Replit CRUD, internal Next.js | Ops / founder → team |
| **A3** | Stop doing manual copy-paste between SaaS tools | **Glue Integration / Workflow Automaton** — event-driven syncs, webhooks, cron jobs | n8n/Zapier/Pipedream/Trigger.dev/Prefect/Dagster | RevOps / founder → APIs |
| **A4** | Interact with the web *as a human would* when no API exists | **Browser/RPA Automaton** — scraping, form-fill, monitoring, reconciliation | Playwright/Puppeteer, Browserbase, Apify, UiPath, TagUI | Ops / growth |
| **A5** | Publish consistently to earn distribution | **Content Pipeline / Publishing Engine** — idea→research→draft→visual→schedule→analytics loop | n8n + Firecrawl + browser-use + Notion + schedulers | Creator / marketer |
| **A6** | Answer a one-time question with evidence | **Research Artifact** — notebook, report, dataset, memo | Jupyter, Python, Observable, PDF/HTML report | Founder / analyst |
| **A7** | Keep data fresh on a schedule with failure handling | **Recurring Data Pipeline** — ETL/ELT, orchestration, idempotency | Prefect/Dagster, dbt, cron, data quality checks | Data/Platform |
| **A8** | Keep prod up and fix what breaks | **Prod Steward / SRE** — oncall, bugfix, incident recovery, perf | Observability, CI/CD glue, MTTR workflows | Users → founder |
| **A9** | Turn attention into pipeline | **Growth/Distribution Engine** — programmatic SEO, outreach, email automation | MailerLite/SendGrid, Webflow/Framer, scraping + enrichment | Founder → market |
| **A10** | Collect money without manual invoicing | **Revenue Plumbing** — billing, entitlements, dunning, tax | Stripe, webhooks, proration, metering | Finance |
| **A11** | Decide whether to build at all (throwaway) | **Spike / Prototype** — time-boxed technical de-risk | Throwaway repo, eval harness | Founder → self |
| **A12** | Port / upgrade without losing data or compliance | **Migration / Modernization** — DB moves, arch changes, security audit | Data migration, infra, security debt | Founder → future self |

**Count:** 12 archetypes (vs typical vendor 5-6). All map 1:1 or 1:N to technical types — never the reverse.

### Challenge to Seed / Vendor List

**VENDOR-INVENTED (not a real JTBD — collapse or drop):**

1.  **"Chatbot / RAG / Agent" as 3 archetypes** — same job: *answer questions from private knowledge*. Splitting by retrieval method is implementation leakage. Merge to **Knowledge Assistant** and evaluate by task-completion + citation faithfulness, not architecture. Vendor invents categories to sell their stack.
2.  **"Text Summarization / Sentiment / Classification"** — toy NLP tasks. No solo builder wakes up to "do sentiment analysis." They want A6 (research artifact) or A5 (content repurposing engine). These are *sub-tasks*, not archetypes. Keeping them as top-level archetypes inflates benchmark coverage while hiding real work.
3.  **"Code Generation" as standalone** — every archetype involves code gen. Isolating it measures `lines of code` vanity while missing whether the Revenue Product actually charges a card (A1/A10).

**MISSING — ≥3 R-A would miss (with evidence):**

**M1: Content Pipeline / Publishing Engine (A5)**
Solo founders' #1 constraint in 2026 is *sustainable publishing*. New OS-level products (CreatorBit.ai, Funnel Flow Engine) explicitly `connect the entire creator workflow — from idea generation and script writing to content planning, automation, and analytics — into one intelligent system` with 5 engines for repurposing. Python automation stacks `generate ideas from trends → draft with GPT → visuals with SD → schedule across platforms → log analytics to Notion`. Open-source pipeline uses `firecrawl + browser-use + n8n` to `handle the movement for you` instead of manual copy-paste. Vendor docs omit this because it's not an LLM API shape — but for indie hackers it's 30-50% of shipped work. Harness ignoring it misses the highest-volume repeatable job.

**M2: Browser/RPA Automaton (A4)**
Taxonomy from `awesome-modern-browser-automation` covers `testing, scraping, monitoring, RPA, AI agents, repetitive workflows` across Playwright/Selenium/Puppeteer + cloud browsers (Browserbase/Browserless) + RPA (UiPath/Robocorp/TagUI). Production RPA toolkit's four bots are canonical: `WebScraperBot, ExcelConsolidatorBot, WeeklyReportBot, CrmErpSyncBot` with `logging, retry with exponential backoff, guaranteed teardown (Init→Process→End)`. Requires anti-detect, proxy rotation, CAPTCHA solving — harness challenges vendor's "API-only" worldview. Real builders live where there is *no API*.

**M3: Glue Integration / Workflow Automaton (A3)**
Empirical taxonomy of 12 glue-work types in 4 groups — Code/Technical Management, Mentoring/Support, Documentation, Community — plus systems-capability-debt taxonomy: `integration debt, functionality debt, data access debt` producing human glue work that `do-mode agents replace with automated execution`. Concretely: `n8n/Zapier/Make for calendars/forms/CRMs/Slack`, `Pipedream/Trigger.dev/Prefect/Dagster for event-driven internal pipelines`, `GitHub Actions/GitLab CI Jenkins as CI/CD glue`. Solo-founder guide confirms `complex integrations / enterprise APIs with poor docs` is exactly when you *must hire* vs AI-handled CRUD. Harness measuring only greenfield apps misses the glue that actually ships revenue.

**Bonus M4: Revenue Plumbing (A10)** — Stripe, metering, dunning, proration. Vendor demo never fails a charge; real builder's SaaS dies on webhook idempotency.

### Splits / Merges (≥2 each)

**SPLIT S1: "Web App" → A1 Revenue Product vs A2 Internal Tool**
Solo-founder guide: `landing page / CRUD → Use Lovable/Framer/Claude Code` (AI handles well) vs `performance at scale / security audit / complex integrations → need hire`. Conflating these lets harness pass on trivial admin CRUD and claim SaaS readiness. Separate SLOs: A1 needs tenant isolation, billing correctness, p95 latency; A2 needs RBAC + audit log + trusted-user UX, zero billing. One benchmark cannot cover both.

**SPLIT S2: "Data Analysis" → A6 One-Shot Research Artifact vs A7 Recurring Data Pipeline**
Same Python, opposite success criteria. A6: correctness, reproducibility, narrative quality — throwaway after delivery. A7: idempotency, freshness/delay, failure recovery, cost per run — runs forever. Merging them makes `deployment frequency` look good for a notebook (noise) and hides pipeline debt.

**MERGE M1: Vendor "Chatbot + RAG + AI Agent" → Single Archetype: Knowledge Assistant (subset of A5/A6)**
All three are conversational interfaces over retrieved knowledge. Evaluating them as three archetypes triples weight for one job and rewards architecture-matching over job completion. Merge and stratify by grounding faithfulness + task completion instead.

**MERGE M2: Vendor "Automation + Workflow" duplicates → A3+A4 unified as "Unattended Execution"**
Vendor splits Zapier-style glue vs RPA browser vs CI/CD glue as different categories — from JTBD they are identical: *do the boring work while I sleep with retry/teardown/metrics*. The harness should vary the *surface* (API vs browser vs file) not the category. Reference toolkit proves one `base_automation.py` serves all four bots.

---

## P0-08: Metric Relevance Matrix

### Candidate Metrics (18 — own list, not vendor's)

1.  Deployment Frequency (DORA)
2.  Lead Time for Changes (LTTC)
3.  Change Failure Rate (CFR)
4.  Mean Time to Recovery (MTTR)
5.  Output Volume — LOC / Commits / PRs / Tickets Closed
6.  Test Coverage %
7.  Build Success / CI Green %
8.  Active Users — MAU / DAU / Registered
9.  Revenue — MRR / Conversion Rate
10. Churn / D7 & D30 Retention
11. SEO Traffic / Pageviews / Hits
12. Latency p95 / Uptime / SLO %
13. Data Freshness / Pipeline Delay (max staleness)
14. Content Throughput — Artifacts/Week & Publishing Cadence
15. Automation Success Rate — % runs without human intervention
16. Cost per Task / Infra Cost per 1k runs
17. Security Findings / Vuln Count
18. Customer/Bug Signal — Support Tickets / Bug Reports (inverse)

**Scale:** HIGH = primary success signal | MED = useful secondary | LOW = marginal | NOISE = misleading/vanity/gamable in that archetype

### Matrix (compact — ratings; rationale follows)

| Metric \ Archetype | **A1 Revenue** | **A2 Internal Tool** | **A3 Glue** | **A4 Browser/RPA** | **A5 Content Pipe** | **A6 Research** | **A7 Data Pipe** | **A8 SRE** |
|---|---|---|---|---|---|---|---|---|
| **1 Deploy Freq** | MED | LOW | MED | LOW | NOISE | NOISE | MED | HIGH |
| **2 Lead Time** | MED | LOW | LOW | LOW | NOISE | NOISE | LOW | MED |
| **3 Change Failure %** | HIGH | MED | HIGH | HIGH | LOW | NOISE | HIGH | HIGH |
| **4 MTTR** | HIGH | MED | HIGH | HIGH | LOW | NOISE | HIGH | HIGH |
| **5 Output Volume** | NOISE | NOISE | NOISE | NOISE | NOISE | NOISE | NOISE | NOISE |
| **6 Test Coverage** | HIGH | MED | MED | MED | LOW | LOW | MED | HIGH |
| **7 Build Green %** | MED | MED | MED | MED | LOW | LOW | MED | HIGH |
| **8 Active Users** | HIGH | LOW | NOISE | NOISE | MED | NOISE | NOISE | LOW |
| **9 Revenue / Conv** | HIGH | NOISE | LOW | LOW | MED | NOISE | LOW | LOW |
| **10 Retention/Churn** | HIGH | LOW | NOISE | NOISE | HIGH | NOISE | NOISE | MED |
| **11 Pageviews/Traffic** | MED | NOISE | NOISE | NOISE | MED | NOISE | NOISE | NOISE |
| **12 Latency/Uptime** | HIGH | MED | MED | MED | LOW | NOISE | MED | HIGH |
| **13 Data Freshness** | LOW | LOW | HIGH | HIGH | MED | NOISE | HIGH | LOW |
| **14 Content Throughput** | LOW | NOISE | NOISE | NOISE | HIGH | LOW | NOISE | NOISE |
| **15 Auto Success %** | LOW | LOW | HIGH | HIGH | HIGH | NOISE | HIGH | MED |
| **16 Cost/Task** | MED | LOW | HIGH | HIGH | MED | LOW | HIGH | MED |
| **17 Security Findings** | HIGH | HIGH | MED | MED | LOW | LOW | MED | HIGH |
| **18 Tickets/Bugs ↓** | HIGH | MED | MED | MED | LOW | LOW | LOW | HIGH |

### Per-Cell Why (archetype-grouped)

**DORA (1-4): Lagging, gamable, speed≠value.** Study of 600k+ devs finds *no direct link between faster LTTC and improved output or quality*; prioritizing speed can *negatively affect performance*. `DORA metrics are lagging indicators — they tell you what happened, not why`, miss `complexity, external factors, priorities/planning/team alignment`. They `can be manipulated` via Goodhart's Law; only `29% of engineers` can speak to them and `52% say not at all or only somewhat effective`. Survey bias inflates self-assessments (94% rate themselves average+), and `as psych safety rises, reported results worsen`. Must be in a balanced stack, never solo.

- **A1 Revenue / A8 SRE:** CFR + MTTR + Uptime = HIGH (outage/regression = revenue loss). Deploy freq = MED/HIGH but secondary to stability.
- **A3/A4/A7 Glue/Browser/Data Pipe:** Freshness + Auto Success % dominate; DORA's deploy freq is LOW — success is *not deploying often* but *not waking humans*. CFR/MTTR HIGH because silent failures compound (dedupe, upsert, proxy health).
- **A2 Internal Tool:** Deploy freq LOW — trusted users tolerate batched deploys; MTTR MED.
- **A5 Content Pipe:** Deploy freq & lead time = NOISE — pipeline is content, not code deploys. Throughput + Auto Success% are truth.
- **A6 Research Artifact:** All four DORA = NOISE — one-shot delivery has no deploys/recovery; measuring them rewards busywork.

**Output Volume (5) — UNIVERSAL NOISE / VANITY.** `When orgs use them to count output (LOC, commits, tickets closed), metrics become poor proxy... incentivize gaming and demotivate top performers`. With AI generating code, `traditional metrics like LOC, commits, velocity are not only insufficient — they're misleading. Even DORA and SPACE must evolve`. Across all 8 archetypes: more output ≠ more outcome. Harness using PR count as global score is easily gamed (split commits, verbose codegen).

**Test Coverage / Build Green (6-7):** HIGH for A1/A8 (regression cost high), MED for A3/A4/A7 (pipeline determinism needs contract tests more than line coverage), LOW for A5/A6 (content correctness ≠ code coverage; build green matters only for pipeline code).

**Active Users / Revenue / Retention / Traffic (8-11): Classic vanity cluster.** Eric Ries: `registered users, downloads, raw pageviews` are vanity — `10,000 registered but 100 active` hides retention; `1M downloads / 900k uninstalls`; `pay $50 for 90k followers` ≠ sales. `Traffic without conversion is vanity — the question is never how many arrived, but how many moved forward`. Apply tests: *What decision does this enable? Can we reproduce it? Is it true?*

- **A1 Revenue:** Active users, revenue, retention = HIGH — *the* job is paying retained users.
- **A2 Internal Tool:** Active users = LOW (small trusted cohort); Revenue = NOISE (no billing); Traffic = NOISE.
- **A3/A4/A7 Glue/Browser/Data Pipe:** Users/Traffic/Revenue = NOISE — no human users, value is cost avoided and freshness. Churn is meaningless for a Cron sync.
- **A5 Content Pipe:** Content throughput = HIGH (publishing cadence is the product); retention/engagement HIGH (subscriber retention), raw pageviews = MED but vanity without CTR→conversion; revenue MED via affiliate/sponsor conversion.
- **A6 Research Artifact:** All acquisition metrics = NOISE — single stakeholder, value is decision enabled.
- **Global vanity trap for harness:** A harness that reports `total pageviews` or `registered users` aggregating A1+A2+A5 looks up-and-to-the-right while masking `200k downloads but 3k actives`, zero conversion, or dead Content Pipeline.

**Freshness / Auto Success / Cost (13,15,16) — Under-measured in vendor harness, dominant for automation archetypes.**

- **A3/A4/A7:** Data freshness = HIGH (stale CRM sync = lost deal; stale scrape = bad decision). Auto success % = HIGH — % runs without human = ROI. Cost/task = HIGH — scale matters (proxy, browser, compute).
- **A5:** Auto success HIGH, freshness MED, cost MED.
- **A1/A2:** Freshness LOW (request-time freshness via latency, not batch delay).

**Security (17):** HIGH for A1/A2/A8 (auth, tenant isolation, audit), MED for A3/A4/A7 (secrets, proxy hygiene, injection), LOW for A5/A6 (but still PII leakage risk).

**Tickets/Bugs inverse (18):** HIGH for A1/A8 (proxy for quality/user pain), MED for A2/A3/A4, LOW for A5/A6/A7 where absence of tickets hides silent data errors.

### Vanity Metrics Spotlight — Look Good Globally, Noise per Archetype

| Globally-Flattering Metric | Where It Is NOISE (and why it deceives) |
|---|---|
| **Deployment Frequency** | A5/A6 — more deploys ≠ more articles or better research; rewards churn |
| **Registered Users / Total Downloads** | A2/A3/A4/A6/A7 — `cannot go down`, `hides retention problems`; a data pipeline with 10k registered "users" has zero users |
| **Pageviews / Hits** | A2/A3/A4/A7 — internal/pipe archetypes have no public pages; inflates harness score while conversions stay flat (`30k→80k visitors, sales held at 8`) |
| **LOC / Commits / PRs** | All — gamable, Goodhart; AI-generated verbosity looks productive while CFR rises |
| **Social Followers / Press Mentions** | A1/A5 — `does not reflect quality or impact`; buying followers rarely → sales |
| **Test Coverage % alone** | A5/A6 — high coverage on content glue still ships wrong facts; without task-completion it is security blanket |

### Which Commonly-Cited Metrics Mislead *for a Harness Specifically*

1.  **Global DORA score averaged across archetypes.** Averaging CFR/MTTR from A1 (where deploy failure = outage) with A6 (where deploy is irrelevant) punishes research artifacts and rewards frequent but meaningless deploys in content pipes. Harness must *stratify* DORA by archetype or drop for A5/A6.
2.  **Output volume (LOC/commits/velocity) as productivity proxy.** With AI codegen, `LOC/commits/velocity are misleading` and `output metrics incentivize gaming`. Harness that scores "more code" will select verbose agents that score HIGH on vanity, LOW on auto success / CFR.
3.  **Vanity acquisition metrics (users/downloads/pageviews) as cross-archetype health.** `Vanity metrics create false confidence... go up and to the right without telling you anything about business health`. A harness aggregating these will show `up 400%` without disclosing `400% from what? 1,000 or 100,000?` and hides `900k uninstalls`. Require *cohort* + *funnel* alternatives per Ries: per-customer, split-test, cohort retention, stage-by-stage conversion.
4.  **DORA alone as "AI productivity."** DORA is `essential but insufficient; lagging; does not measure customer satisfaction, QA, work behind scenes`. Vendor harness that reports only DORA `measures going faster as endpoint, not on-time delivery`, driving `burnout` while users care most about `security, accuracy, preventing serious bugs` — exactly the high-relevance cells DORA misses.

**Recommendation for harness:** Never report a single global score. Report *stratified* matrix; gate promotion on HIGH cells per archetype; treat NOISE cells as zero-weight (or penalty if optimized). Require actionable alternatives: split-tests, per-customer/cohort metrics, funnel stage conversions — over raw totals.

---

## Sources (deliberately different vocabulary from R-A)

- JTBD framework — main vs related jobs, functional/emotional/social jobs [General JTBD literature]
- Solo founder project types & hiring vs AI-handling guide (`Lovable/Framer/Claude Code for landing/CRUD` vs `complex integrations/performance/data migrations/security audit hire`) — [github.com/whawkinsiv/solo-founder-skills — `skills/hiring/SKILL.md`](https://github.com/whawkinsiv/solo-founder-skills)
- Indie hacker archetypes & what builders actually build (SaaS/indie/consultant) — [Indie hacker archetypes search]
- Glue work taxonomy — 12 types across Code & Technical Management / Mentoring & Support / Documentation / Community Management; capability-debt taxonomy (integration/functionality/data access debt → human glue replaced by do-mode agents) — [Glue work taxonomy search]
- Internal tools / Where DevOps engineers use Python — IaC, CI/CD glue (GitHub Actions/GitLab CI/Jenkins), observability, ChatOps — [Internal tools taxonomy search]
- Workflow glue stacks — n8n/Zapier/Make for calendars/forms/CRMs/Slack; Pipedream/Trigger.dev/Prefect/Dagster for event-driven pipelines — [Workflow automation search]
- Browser automation taxonomy — testing/scraping/monitoring/RPA/AI agents; Frameworks (Playwright/Selenium/Puppeteer), Cloud browsers (Browserbase/Browserless/BrowserStack), RPA (UiPath/Automation Anywhere/Robocorp/TagUI), Protocols (WebDriver/CDP) — [awesome-modern-browser-automation contents taxonomy]
- RPA toolkit — four bots (WebScraper/ExcelConsolidator/WeeklyReport/CrmErpSync) with `base_automation.py` (logging, retry, teardown) — [rpa-automation-toolkit project structure]
- Content pipeline / Creator OS — CreatorBit.ai `AI operating system... connects entire creator workflow — idea→script→calendar→automation→analytics`; Funnel Flow Engine 5 Engines; Python automation `trends→GPT drafts→SD visuals→schedule→Notion analytics`; `firecrawl + browser-use + n8n` open-source pipeline — [Content pipeline automation search]
- Vanity vs actionable metrics — Eric Ries: `registered users/downloads/pageviews` are vanity; `easily manipulated, do not correlate to active users/engagement/CAC/revenue`; `traffic without conversion is vanity`; actionable = `active users, retention, CAC, revenue` + `split-tests, per-customer, cohort/funnel` — [Vanity metrics search]
- DORA limitations — lagging, incomplete, gaming/Goodhart, measures speed not value/on-time delivery, survey bias (94% inflated, low skill most over-optimistic), 600k-dev no link LTTC→quality, 52% say not effective, need holistic + leading indicators — [DORA metrics limitations search]
- SPACE & AI codegen — `With AI generating code, LOC/commits/velocity are misleading. Even DORA and SPACE must evolve` — [DORA/SPACE effectiveness search]

**Relevant harness path:** `C:\Users\Shashank Karamudi\Desktop\solo-levelling\the harness` (no files read — synthesis from first-principles JTBD + divergent web sources as instructed).
