# Fringe Engineering Practices — Indie / Bootstrapper Wisdom

**The Omniscient Resource Atlas · product_engineering / expansion-practices · Built 2026-10-10**
**Read-only research only.** Discovers, inspects, categorizes. Does not install, build, configure, rank, or recommend.

Labels: **Verified** / **Corroborated** / **Inferred** / **Proposed** / **Unknown** (see file 01 for definitions).
Evidence classes: `primary` · `secondary` · `practitioner` · `paper` · `forum` · `meta` · `community`.

---

## 1. "Do Things That Don't Scale" — Paul Graham (2013)

**The claim.** Startups should do unscalable things early (manual onboarding, hand-recruiting users, concierge service) because the learning and initial traction compound; optimize for growth later. **Corroborated.**

**Source metadata.** Paul Graham, "Do Things That Don't Scale" (paulgraham.com, July 2013 — **primary** essay). Canonical examples: Stripe's Collison brothers doing manual merchant setup; Airbnb's founders photographing listings themselves. Mirrored widely (bishoprockcap PDF mirror noted in context). Accessed: 2026-10-10. Confidence: High on the essay's content; the examples are Graham's first-hand YC observations.

**The engineering translation (Proposed).** In code terms: don't build the scalable system first — build the *concierge* system: manual scripts, admin panels instead of user-facing automation, single-server deployments, SQLite instead of distributed databases. The indie version of the essay is: *your scaling problems are hypothetical; your missing users are actual.* This is the philosophical root of the boring-stack and single-binary movements below.

**Boundary.** Applies: pre-product-market-fit, when the binding constraint is learning. Doesn't: post-PMF, when manual processes become the bottleneck (the essay says this explicitly — do unscalable things *until* they break, then scale the specific thing that broke).

---

## 2. Maker's Schedule, Manager's Schedule — Paul Graham (2009)

**The claim.** Makers (programmers, writers) need long uninterrupted blocks; managers work in hour-sized meeting blocks. One meeting in a maker's day destroys it, because the cost isn't the meeting — it's the two half-days on either side that can't hold deep work. **Corroborated.**

**Source metadata.** Paul Graham, "Maker's Schedule, Manager's Schedule" (paulgraham.com, July 2009 — **primary**). Follow-up: Cal Newport's deep-work literature (secondary elaboration). Accessed: 2026-10-10. Confidence: High.

**Why it's fringe-but-foundational.** The essay is the theoretical basis for no-meeting Wednesdays (Shopify, file 01 §8), the open-plan critique (file 02 §5), and every "meeting cost calculator." Its edge over generic productivity advice: it frames the conflict as *structural* (two incompatible schedule types) rather than personal (bad time management), which is why it changed company policies rather than just individual habits.

---

## 3. Shape Up — Basecamp / Ryan Singer (2019)

**The claim.** Replace backlogs and estimates with *appetite* (fixed time budgets), six-week cycles, and *bets* (shaped pitches chosen by leadership) instead of prioritized backlogs; build in a circuit breaker (if it doesn't fit the appetite, don't build it). **Corroborated.**

**Source metadata.** Ryan Singer, *Shape Up* (basecamp.com/shapeup, 2019 — **primary**, free online book). Core mechanics: work is *shaped* (a rough solution sketch with boundaries, not a spec) before betting; teams get a fixed appetite (e.g., six weeks) and full autonomy within it; no daily standups, no velocity tracking, no backlog grooming — the backlog is explicitly abolished ("backlogs are not a good way to manage"). Cool-down periods between cycles. Accessed: 2026-10-10. Confidence: High on the book's content (primary, freely available).

**Evidence for/against.** For: Basecamp ran it for years across multiple products; it's the most complete *written* alternative to Scrum from a successful product company. Against: it's optimized for Basecamp's context — small senior teams, a profitable bootstrapped company that can afford to *not* build things; the "betting table" assumes leadership with good product taste. Critics (**forum**/practitioner): Shape Up under-specifies discovery (shaping is described but the discovery input is hand-waved) and can concentrate power in the shapers. No controlled studies; evidence is Basecamp's sustained use + practitioner adoption reports.

**Boundary.** Applies: small senior teams, products with discretionary scope, companies that can say no. Doesn't: large programs with external dependencies; teams needing fine-grained coordination; orgs where leadership product taste is the bottleneck.

---

## 4. The boring-stack manifesto — boringstackoverflow (GitHub)

**The claim.** For most web applications, the optimal stack is boring: a monolith, server-rendered, on a single VPS (Hetzner-class, ~$5/month), with SQLite/Postgres, Caddy or nginx, systemd or Docker-compose — and crucially, *no Kubernetes*, whose benefits scale with fleet size while its costs land on day one. **Corroborated** (as a practitioner movement; outcomes are self-reported).

**Source metadata.** github.com/boringstackoverflow/boring-stack — MANIFESTO.md (**practitioner**, repo). Core arguments: Kubernetes' complexity is justified at fleet scale; for a single app it's pure overhead; boring infrastructure fails in known ways; the money saved on infrastructure complexity buys product development. Accessed: 2026-10-10. Confidence: Medium-High on the movement's claims as *stated*; outcomes are anecdotal.

**The lineage.** This is McKinley's "choose boring technology" (file 01 §1) applied to infrastructure, crossed with Graham's "do things that don't scale" (§1): start on the $5 VPS; move when the $5 VPS is the actual bottleneck. It's also the economic complement to the monolith revival (file 01 §3): the modular monolith *deploys* to the boring stack.

**Counterargument.** The boring stack under-specifies: multi-region, compliance (SOC 2 logging/audit), and team-scale operations (who owns the VPS when the founder is on vacation?). The honest version includes the exit ramp: boring *until* the bottleneck is real, then boring-at-the-next-scale (managed Postgres, then read replicas — not Kubernetes on day one).

---

## 5. Single-binary deployments — Go + SQLite + go:embed

**The practice.** Ship the entire application as one static binary: Go (or similar) compiled with the frontend embedded (go:embed), SQLite as the database (file or Turso/Litestream-backed), no separate app server / asset pipeline / database server to operate. **Corroborated** as a practitioner pattern.

**Source metadata.** Pattern documentation: HN discussions of the "HAG stack" and similar (news.ycombinator.com — **forum**); practitioner blog posts on Go + SQLite + Litestream deployments; Turso/LibSQL as the SQLite-at-scale story. Accessed: 2026-10-10. Confidence: Medium-High on the pattern's existence and mechanics; Medium on scale claims (self-reported).

**Why it matters.** The single binary is the *deployable artifact* of the boring-stack philosophy: one file to build, one file to ship, one file to roll back. It eliminates entire categories of operational failure (dependency drift, asset-pipeline breakage, database connection topology). The trade: you're betting the application fits in one process — which, per §4, it does until it demonstrably doesn't.

---

## 6. SQLite at scale — the lore

**The claim.** SQLite handles far more load than its "toy database" reputation suggests: read-heavy workloads at serious scale, hundreds of writes per second, multi-gigabyte databases — all on a single file. **Corroborated** (as practitioner lore with credible technical grounding).

**Source metadata.** Key thread: HN discussion with practitioner reports — e.g., 512KB writes at 500+/second; SQLite's own documentation (sqlite.org — **primary**) describing its testing regime (100% branch coverage, the most tested database in the world by some measures) and its suitability claims. Litestream (Ben Johnson) added streaming replication, removing the biggest operational objection (single-file = single point of failure); Turso commercialized the edge story. Accessed: 2026-10-10. Confidence: Medium-High on technical claims (SQLite's docs + test regime are primary); Medium on the wilder production anecdotes (forum-reported).

**The boundary (important).** SQLite's write model is single-writer; it doesn't do high-concurrency *write* scaling. The lore's honest form: SQLite is astonishing for read-heavy and moderate-write workloads; the moment you need concurrent writers at scale, you need Postgres. The fringe error is treating "SQLite at scale" as "SQLite *instead of* Postgres always" — the correct reading is "SQLite *before* Postgres until the write bottleneck is real."

---

## 7. The indie synthesis (Proposed)

The indie/bootstrapper wisdom converges on one meta-rule: **defer every scaling decision until the scaling problem is actual, and spend the savings on product.** Do Things That Don't Scale (defer operational scaling) → Maker's Schedule (defer coordination scaling) → Shape Up (defer process scaling) → boring stack (defer infrastructure scaling) → single binary + SQLite (defer architectural scaling). Each is the same move at a different layer. The failure mode of the whole lineage is identical too: deferral becomes denial — the team that won't scale the thing that *actually* broke. The discipline is in the trigger condition, not the deferral.

---

## Gaps in this file

- **Unknown:** No systematic data on boring-stack outcomes (cost savings, incident rates) — all evidence is self-reported practitioner accounts.
- **Unknown:** SQLite-at-scale production anecdotes are forum-reported; no consolidated primary-source survey located.
- **Unknown:** Shape Up adoption outcomes outside Basecamp are practitioner-reported; no controlled comparison with Scrum exists.
