# Payments, Billing & Entitlement Engineering: Research Notes

> Discipline: **payments, billing & entitlement engineering** — subscription lifecycle management, metering for usage-based pricing, dunning/retry logic, proration, tax handling (VAT/GST/sales tax), invoicing, entitlements/feature gating, license/seat management, reconciliation, webhook handling and idempotency, double-charge prevention, refund flows.
> Researched 2026-10-10. Read-only research; no implementation work performed.
> Claim labels: **Verified** (directly documented) · **Corroborated** (≥2 independent sources agree) · **Inferred** (follows from evidence, not directly stated) · **Proposed** (analyst suggestion) · **Unknown** (could not verify).
> Full source metadata and per-finding audit trail: `02-evidence-register.md`.

---

## 1. What the discipline is

### Plain English
Billing engineering is the discipline of **making sure the right customer is charged the right amount, at the right time, exactly once, in the right jurisdiction's currency and tax treatment** — and that what they can *use* (entitlements) always matches what they *paid for*. Everything else is product; this is the money pipe. A bug here doesn't just look bad, it moves money, creates legal liability, or silently leaks revenue.

### Technical mechanics
The discipline rests on four mechanical pillars:

1. **Idempotency** — the guarantee that a retried operation has the same effect as doing it once. At the HTTP layer this is the `Idempotency-Key` header: Stripe guarantees one effect per key for **24 hours** (returning the original response on retry instead of creating a second object). Keys should be derived from the *business* operation (`order_id + payment_intent_id`, or the internal `payments.id`), never blindly reused across different amounts — reusing a client key after an internal fee or coupon changed makes Stripe hand back a *cached PaymentIntent for a different amount*. **Corroborated** (Stripe docs via practitioner reconstructions; multiple independent walkthroughs).
2. **Webhook handling with signature verification** — payment providers deliver events at-least-once: duplicates, delayed, and out of order are the norm, not the exception. Three sub-requirements: (a) verify the HMAC-SHA256 signature against the **raw request body** (parsed/re-serialized JSON breaks verification) and enforce the timestamp tolerance window (Stripe's default is 5 minutes, defeating replay attacks); (b) dedupe on the event ID *before* doing work — the atomic-claim pattern `INSERT ... ON CONFLICT DO NOTHING` into a `webhook_events` table, returning 200 on duplicates (a `check-then-insert` is a race); (c) never derive state from event order alone — re-fetch authoritative state or design event-sourced subscription state that applies transitions idempotently. **Corroborated** (Stripe webhook docs conventions + ≥4 independent practitioner implementations; the atomic-claim pattern recurs identically across stacks).
3. **Event-sourced subscription state** — a subscription is a state machine (`trialing → active → past_due → unpaid → canceled`, plus `incomplete`, `incomplete_expired`, `paused`), and transitions must be explicit, validated, and owned. A critical separation: **the processor's billing state and the app's entitlement state are different things.** A subscription in `past_due` may still have full app access during a grace period. Code that grants access on `subscription.status === 'active'` alone will either lock out grace-period customers or — the worse failure, documented in real PRs — keep granting paid access forever because `.updated` events were mapped purely from price, ignoring status. **Corroborated** (multiple OSS webhook implementations + Stripe docs semantics; real failure documented in fix commits).
4. **Metering pipelines for usage-based pricing** — ingest → dedupe → aggregate → rate → invoice → collect → reconcile. Raw usage events flow (often via Kafka/event bus) into an aggregation layer keyed by tenant×meter×period with **event-time** semantics and watermarks for late events; Stripe's Meter Events API accepts an `identifier` per event for dedup; rate limits are real (v1 meter endpoint ~1,000 events/sec; the v2 stream path ~10,000/sec); a nightly reconciliation compares internal aggregates against Stripe-recorded usage with alerting thresholds (one practitioner HLD uses 0.01% drift, ~$10K/month at $100M ARR). **Corroborated** (Stripe Meters API docs conventions via practitioner reconstructions; two independent pipeline architectures agree on the ingest→reconcile shape).

### The billing object graph (Stripe-shaped, the industry's de facto standard)
**Product → Price → Subscription → Invoice → PaymentIntent → Payment**, with webhooks as the async nervous system and **Checkout / Customer Portal** as the hosted surfaces. Trial conversion, proration, seat changes, and plan upgrades all mutate the Subscription; every mutation generates invoice/charge events that must be reconciled locally. **Verified** (Stripe's public object model, consistently documented across practitioner sources).

---

## 2. Why it is COMPULSORY — the failure evidence

Billing failures are mandatory-handling because the blast radius is money + trust + legal liability, and the failure modes are ordinary distributed-systems failure modes that every other layer treats as bugs but billing treats as *financial events*.

**Double-charge incidents (the signature failure).** The canonical mechanism: provider succeeds, response is lost (timeout, closed connection, proxy), client or frontend auto-retry fires with a *new* idempotency key, and a second charge is created. Documented instances:
- A practitioner incident reconstruction: mobile client with 800ms timeout + one auto-retry generating a fresh key per attempt → **3,100 duplicate captures, ~$145k gross money moved** before containment; refunds left net cost dominated by support time and trust loss. **Corroborated** (incident reconstruction + convergent mechanism in ≥3 other sources).
- A Medium incident write-up: webhook timeout at a load balancer (28s), handler had already charged, provider retried over 72 hours, handler returned 500 on a later attempt prompting more retries → **11 charges of $77 ($847 total)** against one customer; $3,047 total cost including refunds/support. **Corroborated** (mechanism consistent with Stripe's documented 3-day webhook retry window).
- GitHub commit evidence of a subtler variant: a billing sweep released a settled charge and rolled the date in one step, destroying the only "this cycle is already billed" signal; an editor opened before the roll resubmitted a stale billing date, leaving a due date with no linked charge, so the next sweep **posted a second charge for an already-paid cycle — silently**. **Verified** (commit message with root-cause analysis, 2026-09).
- A stale-proration-window defect: a plan-change settlement computed to a few minor currency units (1, 3, 16 observed) that no card network accepts → indeterminate charge state holding a settlement reservation → **transitions refused while the reservation stands, so subscribers could not even cancel; three subscriptions had to be freed by hand**. **Verified** (commit message with root-cause analysis).

**Webhook outages are silent.** A widely-shared practitioner lesson: Stripe retries non-2xx deliveries for **up to 3 days**; if an endpoint silently stops receiving events, teams discover it only when the MRR chart "looks weird" — weeks of drift. One postmortem-style account found `incomplete` rows conflating "started a checkout" with "tried to pay and failed", making dashboards report phantom failed revenue. **Corroborated** (retry window documented in Stripe docs; phantom-row case Verified as first-hand practitioner account).

**Involuntary churn is revenue leakage, not a product problem.** Failed payments cause roughly **20–50% of total SaaS churn** depending on the source's population, and most of it is recoverable. Baremetrics-derived benchmarks put failed payments at ~9% of MRR monthly; Recurly's data puts recovery on failed *annual* invoices at 23% vs 53% for monthly — one failure on an annual plan loses a whole year. This is the quantitative case for the dunning discipline (§4). **Corroborated** (convergent benchmarks across Recurly/Stripe-published/practitioner modeling; ranges differ by source — treat as direction-trusted, magnitude-discounted).

**Tax liability is legal, not engineering.** Stripe (processor) leaves the seller as the legal merchant — *you* owe VAT in the EU, GST in Australia, and sales tax in 40+ US states; Stripe Tax calculates (~0.5% per transaction) and helps with registration/filing but liability stays with you. A merchant-of-record (Paddle, Lemon Squeezy, Creem, and Stripe's own Managed Payments product) absorbs the legal-seller role and files/remits. VAT penalty regimes make "I didn't know" non-exculpatory. The engineering implication: choosing processor-vs-MoR is a **legal and operational decision wearing a technical costume**. **Corroborated** (convergent across MoR-vendor comparisons; the processor-vs-MoR liability structure is directionally consistent).

**Chargebacks cost multiples of the dispute.** A $100 dispute costs ~$400+ fully loaded (fees, staff, lost merchandise); merchants win only ~45% of disputes; Stripe charges $15 per dispute (+$15 if contested); winning a dispute does not necessarily improve the chargeback ratio, and Visa's VAMP threshold drops to 0.9% in April 2026. **Corroborated** (reason-code guide + chargeback-ratio references; 2026 projection figures single-sourced — magnitude-discounted).

---

## 3. How world-class companies do it

### Stripe (the industry's deepest billing-engineering blog)
- **Billing as a complete platform**: subscription management, invoice collection, reconciliation, and revenue recognition integrated into the payments stack. Subscription schedules (start in future, backdate, schedule upgrades/downgrades), sub-cent billing (fractional unit prices like $0.0005/MB), and **pending updates** — a change applies only when payment succeeds, so a seat-add that fails to charge never changes access. **Verified** (Stripe Billing product announcements via official blog).
- **Machine-learned recovery**: Smart Retries — retry timing chosen by models trained on billions of transactions, tuned to decline code, customer payment history, and issuer time-of-day patterns; up to 8 retries over a 2-month window. Automatic card updates (Visa/Mastercard updater programs) refresh expired/replaced cards *before* the next charge. Stripe's own 2020-era claim: **41% of failed payments recovered** through card updates + smart retries + related capabilities; a 2026 practitioner analysis puts Smart Retries alone at ~51–57% of failed recurring payments. **Corroborated** (Stripe's figure is vendor-published — direction-trusted, magnitude-discounted; convergent independent modeling).
- **Idempotency semantics documented as contract**: idempotency keys retained ≥24h; keys in logs (never put PII in a key); authentication/rate-limit outcomes (401/429) are deliberately *not* cached — documented as behavior, matching the devops-daily reconstruction. **Corroborated**.

### Adyen (the acquiring-side model)
Adyen built payments, acquiring (banking licenses US/EU/UK), risk management, and data products on **one platform** rather than stitching providers: single technical environment for online/in-person/marketplace, authorization-rate optimization from cross-merchant transaction data, local acquiring per market. Scale signal: €1.3943T processed volume in FY2025, take rate ~17 bps. The billing-engineering lesson: **fewer PSP seams → fewer reconciliation surfaces**; the trade-off is depth of self-built billing-logic versus Stripe's developer-facing billing toolkit. **Corroborated** (analyst/company-report figures + engineering-positioning coverage). Engineering-internals detail on Adyen's ledger itself is **Unknown** in the public record.

### Paddle / Lemon Squeezy / Creem (merchant-of-record)
The MoR absorbs global tax registration, calculation, collection, filing, and remittance — ~5% + 50¢ all-in on Paddle vs Stripe's ~2.9% + 30¢ *before* tax tooling and liability. Subscription migration is supported via PCI-compliant card-data transfer (cards are re-imported, customers don't re-enter them). **Corroborated** (fee structures from vendor comparisons; migration claim vendor-stated — direction-trusted).

### Open-source billing systems
- **Kill Bill** (Apache 2.0, Java, ~15 years in production, 5,753 GitHub stars, release 0.24.21 Aug 2026): the oldest and most complete OSS billing engine — catalog, subscription lifecycle, usage billing, invoicing, payments, refunds, entitlements, tax — via plugin architecture (Stripe, PayPal, Avalara plugins). Operated heavily: Java/Jetty + MySQL/Postgres, event bus → webhooks/Kafka for downstream sync. The known trade-off: **heaviest operational burden**; metering less polished than purpose-built meters. **Corroborated** (official docs + independent 2026 usage-billing platform comparison).
- **Lago** (open core, AGPL-3.0): API-first metering + usage-based billing between product usage and revenue — event ingestion, aggregation into billable metrics, pricing rules, entitlements, invoicing; Ruby on Rails + React + Postgres + Redis + Kafka/Redpanda + ClickHouse. **Corroborated** (repo analysis via DeepWiki + docs).
- **OpenMeter** (open core, Apache-2.0, v1.0.0-beta.233 Sep 2026): CloudEvents-style ingestion; event `id` is the server-side dedup key (resend-on-retry is a no-op); meters with entitlements/limits for quota workflows. **Corroborated** (official SDK docs via repo).
- Pattern across all three: **dedup key on the event is the non-negotiable primitive**; the billing engine itself never owns a separate meter store twice (an ADR records OpenMeter *rejected* for a billing role where Postgres metering already existed, to avoid duplicate metering substrates). **Verified** (ADR text).

### Entitlement architectures: centralized service vs embedded checks
Two deployment shapes, both documented:
- **Centralized entitlement service**: a dedicated service as single source of truth; app code calls a lightweight API/SDK ("does customer X have capability Y?"); designed for low latency with caching and **fail-open defaults** so a slow/unreachable service doesn't block user actions; subscribes to billing-platform changes (upgrades, downgrades, renewals) to update entitlements automatically. **Corroborated** (Ordway/Stigg-style practitioner guidance ×2+).
- **The entitlements pattern vs tier checks**: never branch on plan names in feature code (`if plan == "pro"`). Plans grant *entitlements*; entitlements control features. Rationale: tier renames/splits and custom enterprise deals (a startup wanting Pro analytics + Starter limits) otherwise require finding every tier check — miss one and you give away features or lock paying customers out. **Corroborated** (Medium pattern essay + dev.to untangled-entitlements; convergent rationale).
- Billing software "isn't designed to carry out these checks or grant access" — the entitlement service doubles as an **anti-corruption layer** shielding the app from billing-integration errors, a fail-safe if the billing system is unreachable, and it makes switching billing providers feasible. It also handles what billing systems don't: **grandfathering** legacy plans and scheduled segment migrations. **Corroborated** (dev.to; anti-corruption-layer framing).
- Separated concern confirmed in the wild: multiple Stripe-integration codebases keep `subscriptions` (Stripe mirror) and entitlements/plan-grant tables **separate**, with past_due handled as a distinct grace state rather than an access cut-off. **Verified** (multiple repo implementations + issue/commit evidence).

---

## 4. Key practices

### Trial → paid conversion mechanics
- Trials must be a first-class subscription state (`trialing`), not "no subscription yet": access derives from state, period dates tracked (`trial_end`), and conversion mid-trial either restarts a billing period or the provider handles the transition. No-card trials lapse to read-only with data retained (one skill's policy: 14-day no-card trial → read-only, 90-day data retention) — the retention window is the reactivation lever. **Corroborated** (convergent across Stripe-semantics docs and practitioner skill documents; specific retention numbers are per-company policy, not standards).
- Fulfillment must be gated on **verified server-side state**, never on client checkout success: create the local entitlement only from a verified webhook (or a server-side retrieve), never from the redirect URL the customer lands on. **Corroborated**.

### Grace periods and dunning cascades
The standard cascade, convergent across practitioners and providers:
1. **Pre-dunning (prevention)**: card-expiry alerts at 30/15/7 days; account updater services (Visa/Mastercard auto-update — Stripe's is on by default in most plans; claimed to silently prevent 15–25% of expired-card failures); backup payment method capture at signup; pre-billing notification for annual plans.
2. **Smart retries, decline-code-aware**: soft declines (insufficient funds, processor timeout) retry 3–5× over 7–10 days, timing shifted (day-of-month of the original success, time of day); hard declines (stolen card, closed account) → don't retry, ask for a new card; SCA/3DS-required → route the customer to re-authenticate. Stripe's Smart Retries: up to 8 attempts over 2 months, ML-chosen timing.
3. **Dunning emails**: day 0/1 ("we couldn't process your payment", 41% open rate within 24h per practitioner data), day 3 (urgency), day 7 (value loss), day 10–14 (final notice + offer: discount, pause instead of cancel). Rules: direct no-login card-update link (every extra click kills conversion), specific failure reason, sent from a real person, no guilt.
4. **Grace-period access policy**: `past_due` retains full access for the window (days 1/3/5/7 anchor on the original decline); the failure mode to engineer out is cutting access instantly on transient failure. After exhaustion → `canceled`, retain data per offboarding policy, keep the reactivation path.
5. **Debounce notifications**: send the "payment failed" email **once per dunning cycle** (skip if already in a grace status) — a real commit fixed exactly this after treating every `.updated` as fresh.
6. Recoverable involuntary churn is cited at **2–10% of revenue** (practitioner skill) — worth optimizing, magnitude vendor-adjacent.

### Proration models
Proration is where small arithmetic errors become support tickets and disputes:
- Standard policy table: seat adds / plan upgrades → charge prorated difference for remaining days immediately; seat removals / downgrades → credit at next invoice or take effect at next period start (never an immediate refund of unused time — GitHub Copilot's documented policy matches this shape). **Corroborated** (Copilot docs + practitioner skill; the *direction* of each rule is convergent; exact day-counting conventions are per-provider).
- Failure modes documented: (a) quote showing the *recurring price as of the quote* rather than the boundary it recurs from, so an expiring promo misprices the preview (CHF 729.68 quoted vs 770.21 actual in one case); (b) sub-network-minimum settlements stranding subscriptions (see §2). Mitigation: define proration policy per change type explicitly, compute in **integer minor units with half-up rounding in whole days** (or be explicit about seconds), and show the customer the exact prorated amount at confirmation. **Corroborated**.
- Proration-mode vocabulary (immediate charge / bill later / do-not-bill keeping the billing date / schedule at renewal) is supported across Stripe (subscription schedules, pending updates) and newer providers (Dodo: `difference_immediately`, `prorated_immediately`, `full_immediately`, `do_not_bill`). **Corroborated**.

### Multi-currency and tax
- EU VAT: VAT MOSS/OSS for B2C (charge the customer's country rate), B2B reverse charge with valid VAT ID; US sales tax: economic-nexus thresholds post-*Wayfair*; GST/JCT elsewhere. Don't build the rate engine — use Stripe Tax / Avalara / Vertex / TaxJar, and validate VAT IDs (VIES) and US exemption certificates. **Corroborated**.
- Multi-currency: decide where FX happens (processor-settled vs platform-converted); divergence monitoring between estimated and settled balances catches currency-conversion mismatches (documented in a Salesforce↔Stripe drawdown architecture). **Inferred** from one detailed architecture; general FX-at-settlement practice **Corroborated**.
- Currency amounts everywhere in **integer minor units with explicit ISO 4217 code**; never floats. **Corroborated** (universal practitioner consensus).

### Invoicing
Draft → **FINALIZE (immutable)** → pay; corrections are **credit notes**, never edits to a finalized invoice (append-only, like the ledger). Stripe Invoicing: 0.4–0.5% per paid invoice, automatic tax calculation, smart reminders, ACH/wire auto-reconciliation. Revenue recognition (ASC 606) is a separate export — the processor knows *cash*, not *contract terms*; spreading an annual payment over 12 months of performance obligations is the billing system's/accounting's job. **Corroborated**.

### Refund flows
Refunds are new journal entries, not edits; refunds issued through the PSP carry idempotency keys of their own; the incident-repair pattern is: pair processor IDs by customer purchase attempt, refund the *later* capture, write audit rows, hand finance a CSV. Stripe refunds don't automatically adjust tax already remitted — tax adjustment is your accounting's problem (MoR vendors absorb this). Partial-refund states (`PARTIALLY_REFUNDED`) must be modeled explicitly, not inferred from amounts. **Inferred/Corroborated** (refund-via-PSP mechanics Verified in practitioner code; tax-adjustment implication Corroborated by MoR tax-liability structure).

### Seat/license management
Seats are quantities on a subscription, not subscriptions per user: add-seat → immediate prorated charge; remove-seat → effective end of cycle (or immediate if revoked); assignment changes are effective immediately while billing follows the proration policy. Guardrails: suspend keys/API access at defined thresholds (one implementation: soft over-quota still 200s until 3× tier limit → 429; suspended → 402), and map `past_due/unpaid/canceled/incomplete_expired/paused` explicitly rather than mirroring Stripe's enum blindly (Stripe has added statuses before — one codebase stores the status verbatim with no CHECK constraint for that reason). **Verified** (multiple implementation references).

---

## 5. Failure modes and postmortems (catalog)

| # | Failure | Mechanism | Cost / blast radius | Evidence |
|---|---|---|---|---|
| F1 | Double charge on retry | Success-at-processor, failure-before-recording-key; retry with fresh key | $145k gross (3,100 dupes); $3,047 total on an $847 overcharge | Corroborated — incident reconstructions (SoftwareNews Medium; CodeByUmar Medium) |
| F2 | Webhook retry storm | Handler slow/timeouts → provider retries up to 3 days; no event-ID dedup | 11 charges of $77; bank fraud alert; public tweet | Corroborated — practitioner postmortem (SoftwareInterviewRules Medium); retry window Verified via Stripe docs conventions |
| F3 | Double billing from stale state | Sweep released settled charge and rolled date in one step, destroying the "already billed" signal; stale editor resubmission | Second charge posted silently for an already-paid cycle | Verified — GitHub commit root-cause (dondon3109, 2026-09) |
| F4 | Settlement stranding | Prorated settlement of a few minor units rejected by card networks → reservation held → all transitions refused, incl. cancel | 3 subscriptions freed by hand | Verified — GitHub commit root-cause (selisedigitalplatforms) |
| F5 | Grace status ignored | `.updated` mapped purely from price; `past_due` users kept paid access indefinitely | Revenue leakage until Stripe deleted the sub (or forever) | Verified — GitHub issue + fix commit (filemorph; c-cremeens issue) |
| F6 | Phantom failed revenue | Pre-payment checkout abandonment stored as `incomplete` rows indistinguishable from failed payments | Misleading dashboards; panic over money that never moved | Verified — first-hand practitioner account (dev.to, 2026-10) |
| F7 | Lost webhook fulfillment | Signature verified, work started, timeout; retry crashes on half-written state; subscription never activates | Customer paid; database disagrees | Corroborated — dev.to idempotent-webhooks guide; convergent |
| F8 | Proration misquote | Preview priced as-of-quote not as-of-boundary; expiring promo mispriced | CHF 729.68 vs 770.21; support escalations | Verified — GitHub commit root-cause (selisedigitalplatforms) |
| F9 | Dunning email flood | Every `.updated` triggered a payment-failed email | Customer harassment during one failure | Verified — fix commit debouncing to once per dunning cycle (filemorph) |
| F10 | `cancel_at_period_end` staleness | Dashboard read the boolean from a re-fetched-but-misread subscription; showed "Renews" for a canceled sub | Customer trust; support load | Verified — first-hand practitioner account (dev.to) |
| F11 | Duplicate fulfillment | Same event delivered twice → credits/features granted twice | Revenue leakage (usually noticed only in the wrong direction) | Corroborated |
| F12 | Tax liability surprise | Processor setup with global sales; no VAT/GST registration | Penalties, back-filing; non-exculpatory ignorance | Corroborated — MoR comparisons ×several |

**Common root causes across the catalog:** (1) success recorded *after* the side effect instead of before it (claim-then-act); (2) check-then-insert instead of atomic claim; (3) trusting event payload/order instead of re-reading authoritative state; (4) no reconciliation loop, so silent drift compounds; (5) conflating billing state with entitlement state in one field. **Inferred** (synthesis of F1–F12; each individual cause documented in at least one source).

---

## 6. Bottlenecks

1. **Reconciliation at scale.** Nightly batch (compare provider settlement/report files vs local ledger) works until volume and multi-PSP routing make "nightly" too slow; the trajectory is toward **streaming reconciliation** (consume the event stream continuously, near-real-time drift alerts). Shard ledgers by account/home region to keep writes single-shard; TigerBeetle-style purpose-built financial databases enforce double-entry invariants at the storage engine (100K–500K TPS claimed vs 100–1K TPS naive Postgres under contention — vendor benchmarks, magnitude-discounted). **Inferred/Corroborated** (design-handbook deep dives ×3 convergent on double-entry + reconciliation; TigerBeetle figures vendor-adjacent).
2. **Metering accuracy vs cost.** Pre-aggregation (fast dashboards, hard to correct) vs query-time aggregation (slow, always accurate); real-time metering needed only for enforcement (rate limits, prepaid balances, alerts), batch suffices for invoicing. Stripe meters only aggregate `sum`/`count`/`last` — peak-concurrent or daily-average must be computed and reported as `last`; Stripe meters track usage **per customer, not per subscription**. The cost lever: batch event ingestion with idempotent `identifier`s and a reconciliation loop, not per-event synchronous billing calls. **Corroborated**.
3. **Entitlement checks on hot paths.** Centralized checks add latency to every request; the standard answers are local caching with TTL and fail-open defaults for availability, with the centralized service as the source of truth and webhooks driving cache invalidation. **Corroborated** (entitlement guidance ×2; fail-open default documented).
4. **Idempotency-key lifecycle.** Keys accumulate forever; Stripe keeps them ≥24h — past that window, a retry is a *new* operation. Local key stores need TTL (24–48h) and a cleanup job, or the table becomes "one of your biggest and slowest." Cross-horizon dedup (replays >24h) must be handled by the business-key layer (`order_id + payment_intent_id` unique constraint), not the provider key. **Corroborated**.
5. **Tax complexity growth.** Every new jurisdiction is a new rate table, registration, and filing obligation; the bottleneck is compliance labor, not code — the MoR decision is the pressure valve. **Inferred** (structural; consistent with tax-penalty evidence).

---

## 7. Where it slots into the product lifecycle

Billing engineering sits at the **build→ship→operate** boundary but has tendrils through the whole lifecycle:

- **Design/ideation**: pricing-model choice (per-seat, usage-based, hybrid, credit drawdown) determines metering architecture — decide before building, because retrofitting event-time metering onto a request-time system is a rewrite. Entitlement taxonomy (plan → entitlements → features) should be defined when the pricing page is designed, not after.
- **Build**: webhook handler + idempotency layer + subscription state machine + entitlement checks land here. The two-hosted-surface rule applies: use Stripe Checkout/Customer Portal rather than hand-rolling card capture (PCI scope), with separate webhook endpoints per concern (own billing vs connected accounts) to keep signature secrets and routing sane — a real lesson from a first-build retrospective. **Verified** (practitioner account).
- **Test**: duplicate-delivery, invalid-signature, stale-event, partial-failure, and retry-after-timeout tests are the billing-specific matrix; Stripe CLI `stripe trigger` / test clocks simulate lifecycle transitions. **Corroborated**.
- **Ship**: migration path for existing subscribers (PCI-compliant card import) if changing providers; proration-policy announcement; dunning email copy review (no guilt).
- **Operate (permanent)**: reconciliation jobs, dispute evidence deadlines (chargeback evidence submission is time-boxed — freeze-and-notify on `charge.dispute.created`), dunning tuning by decline-code mix, tax registration/filing calendar, MRR/leakage dashboards with drift alerts. Billing is never "done": rate tables change, card networks change rules (Visa VAMP threshold drops to 0.9% April 2026), and providers add statuses.

**The one-sentence placement:** billing is the lifecycle's *financial control plane* — it converts product usage into revenue with exactly-once semantics, and every other lifecycle stage (pricing design, checkout UX, dunning emails, revenue recognition) is either upstream input to it or downstream consumption of its ledger.

---

## 8. What I could not verify (Unknown)

- Adyen's internal billing/ledger engineering (no public engineering deep-dive found on their subscription or ledger internals; only platform-positioning and financial reporting).
- Stripe's exact ML features for Smart Retries (vendor-described only; no public paper or feature list).
- Paddle/Lemon Squeezy internal architecture (vendor-published only).
- A public, instrumented measurement of double-charge *frequency* across the industry — incidents are reported individually; no aggregate dataset found.
- Exact Stripe meter-event rate limits beyond the practitioner-reported v1 ~1,000 events/sec and v2 stream ~10,000 events/sec figures (single secondary source for v2 — verify against current docs).
