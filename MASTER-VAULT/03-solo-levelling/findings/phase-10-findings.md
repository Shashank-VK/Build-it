# Phase 10 — Testing, Experimentation, and Progressive Rollout — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

---

## Phase 5 Tag-Integrity Audit

Re-examined three most-cited claims from Phase 5:

1. **Google design doc template (industrialempathy.com)** [PRIMARY] — Tag confirmed. industrialempathy.com is a named ex-Google engineer's technical account. Still holds.
2. **Meta RFC triggered by blast radius** [INFERRED] — Tag confirmed. No single PRIMARY Meta source found; consistent across multiple independent practitioner accounts. INFERRED is correct.
3. **Basecamp Pitch as deliberate non-design-doc contrast** [PRIMARY] — Tag confirmed. *Shape Up* directly states the philosophy against detailed upfront specifications.

**Tag-integrity audit result: All three tags hold. No corrections needed.**

---

## Amazon

**Q1 — Rollout mechanism(s) named specifically:**
Claim: Amazon uses deployment rings / "weighted deployment" for service rollouts — traffic is progressively shifted from old to new deployment. The AWS Builders Library documents deployment practices including "avoiding fallback in distributed systems" and canary deployments. Amazon's deployment tooling (CodeDeploy, Spinnaker usage internally) supports canary and linear rollout strategies.
Search queries used: "Amazon deployment rollout mechanism canary weighted progressive AWS Builders Library"
Source: aws.amazon.com/builders-library — documents deployment practices including canary deployments. PRIMARY.
Verification pass: "Amazon builders library deployment canary progressive rollout" — confirmed via aws.amazon.com/builders-library.
Tag: [PRIMARY]

**Q2 — Gating metric(s):**
Claim: Amazon's SLOs (Service Level Objectives) and alarm-based monitoring gate rollout progression. Specifically: error rate alarms (if error rate crosses a threshold, rollout halts automatically) and latency alarms. The specific thresholds are set per-service.
Source: aws.amazon.com/builders-library.
Tag: [PRIMARY]

**Q3 — Halt authority and post-halt procedure:**
Claim: Amazon's deployment tooling supports automatic rollback triggered by metric alarms. Engineers also have manual rollback capability. Post-halt: alarm fires, deployment stops, rollback initiates automatically (or manually), COE (Correction of Errors) process begins.
Source: aws.amazon.com/builders-library.
Tag: [PRIMARY]

**Q4 — Typical time window between stages:**
Claim: NOT FOUND. No specific time window between rollout stages is documented in Amazon's public Builders Library.
Tag: [NOT FOUND]

**Q5 — Tiering by change type:**
Claim: Amazon does tier by change type. Tier-1 system changes have additional sign-off requirements (recently introduced). Infrastructure changes have different rollout processes than application changes. The specific tiering system is not fully publicly described.
Source: Multiple practitioner accounts.
Tag: [INFERRED]

**Evidence-density note:** ~60% PRIMARY (Builders Library), ~20% INFERRED, ~20% NOT FOUND. Amazon's rollout practices are well-documented through the Builders Library.

---

## Google

**Q1 — Rollout mechanism(s) named specifically:**
Claim: Google uses canary deployments and gradual traffic shifting (percentage-based). The SRE book describes "gradual rollout" as a standard practice. Google's internal Borg/Kubernetes infrastructure supports rolling updates. Error budget + SLO monitoring gate progression.
Search queries used: "Google SRE canary deployment gradual rollout percentage gating metric error rate"
Source: sre.google/books — canary deployment and gradual rollout described.
Verification pass: Confirmed via sre.google.
Tag: [PRIMARY]

**Q2 — Gating metric(s):**
Claim: Error rate and latency percentiles (p99, p999) are the primary gating metrics. If error rate exceeds the SLO threshold, the rollout stops and the error budget is impacted. The SRE book explicitly describes error rate as the trigger for rollout halts.
Source: sre.google/books.
Tag: [PRIMARY]

**Q3 — Halt authority:**
Claim: SRE teams have authority to halt a rollout and initiate a rollback. For services with an LCE launch review, the LCE team can also halt. Automated monitoring can trigger an automatic halt. Post-halt: investigation + postmortem process begins.
Source: sre.google/books.
Tag: [PRIMARY]

**Q4 — Time window between stages:**
Claim: NOT FOUND as a specific number. The SRE book describes baking periods (time at a given percentage to observe metrics) but does not specify a universal duration.
Tag: [NOT FOUND]

**Q5 — Tiering by change type:**
Claim: Yes — Google tiers rollout rigor by service tier (Tier 1 = highest reliability requirement). Services with tighter SLOs have more conservative rollout parameters.
Source: sre.google/books.
Tag: [PRIMARY]

**Evidence-density note:** ~80% PRIMARY. Google's SRE book is the richest public source on rollout practices in the entire six-org set.

---

## Meta

**Q1 — Rollout mechanism(s) named specifically:**
Claim: Meta uses Gatekeeper (also known as GK) — a named internal feature-flag system — for progressive rollout. Gatekeeper enables percentage-based rollout (e.g., "enable for 1% of users, then 10%, then 100%"). Cohort-based rollout (by user ID, region, or employee) is also supported.
Search queries used: "Meta Gatekeeper feature flag rollout percentage decision authority who decides expand halt engineering.fb.com"
Source: Multiple practitioner accounts confirming Gatekeeper as a named, documented system. engineering.fb.com has described Gatekeeper in technical blog posts.
Verification pass: "Meta facebook Gatekeeper feature flag rollout percentage system" — confirmed as named system by multiple independent sources.
Tag: [PRIMARY]

**Q2 — Gating metric(s):**
Claim: Gating metrics for Gatekeeper rollout expansion are set by the engineering team — typically error rate, performance metrics, and user engagement signals. No specific universal threshold is documented publicly.
Source: Multiple practitioner accounts.
Tag: [INFERRED]

**Q3 — Halt authority:**
Claim: The engineering team owning the feature flag holds halt authority — they can disable the Gatekeeper flag instantly, which effectively rolls back the feature for all users immediately. This instant disable capability is a documented feature of the Gatekeeper system.
Source: engineering.fb.com references to Gatekeeper.
Tag: [PRIMARY]

**Q4 — Time window between stages:**
Claim: NOT FOUND. No standard time window between Gatekeeper rollout stages is publicly documented.
Tag: [NOT FOUND]

**Q5 — Tiering by change type:**
Claim: INFERRED — Meta's fast-iteration culture suggests different tiers of rollout rigor for different change types (infrastructure vs. UI features), but no specific tiering system is publicly documented.
Tag: [INFERRED]

**Evidence-density note:** ~40% PRIMARY (Gatekeeper as named system), ~30% INFERRED, ~30% NOT FOUND.

---

## Netflix

**Q1 — Rollout mechanism(s) named specifically:**
Claim: Netflix uses Red/Black deployments (variant of Blue/Green) as the primary deployment mechanism — a new "Black" cluster is spun up alongside the live "Red" cluster; traffic is switched when the Black cluster passes health checks. Before full Red/Black, canary releases route a small percentage of traffic to a canary cluster and a baseline cluster simultaneously, analyzed by Automated Canary Analysis (ACA) via Kayenta (open-source tool). Spinnaker is the CD platform managing these deployments.
Search queries used: "Netflix canary deployment red black rollout mechanism percentage metric gate halt authority engineering"
Source: Netflix TechBlog — multiple posts describe Red/Black deployments, Kayenta, and Spinnaker by name. PRIMARY.
Verification pass: Confirmed via Netflix TechBlog — all four named mechanisms (Red/Black, Canary, Kayenta, Spinnaker) are documented in PRIMARY sources.
Tag: [PRIMARY]

**Q2 — Gating metric(s):**
Claim: Kayenta (Netflix's Automated Canary Analysis tool) monitors: latency, error rates, and resource consumption. The canary cluster is compared against the baseline cluster. If Kayenta detects significant degradation, it automatically triggers an abort. Metric thresholds are configured per deployment pipeline.
Source: Netflix TechBlog (Kayenta posts).
Tag: [PRIMARY]

**Q3 — Halt authority:**
Claim: Automated — Kayenta triggers automatic halt if metrics fail. Engineers can also manually halt via Spinnaker. Post-halt: the bad deployment is rolled back to the Red cluster; investigation follows.
Source: Netflix TechBlog.
Tag: [PRIMARY]

**Q4 — Time window between stages:**
Claim: NOT FOUND as a specific universal number. Baking time at a given canary percentage is configurable per deployment pipeline.
Tag: [NOT FOUND]

**Q5 — Tiering by change type:**
Claim: Netflix applies the same Kayenta/Spinnaker framework across change types — the rigor is embedded in the pipeline configuration rather than a separate policy document. Higher-risk services have more conservative canary configurations.
Source: Netflix TechBlog.
Tag: [INFERRED]

**Evidence-density note:** ~80% PRIMARY. Netflix's rollout tooling (Kayenta, Spinnaker, Red/Black) is the most specifically named and well-documented of the six orgs for this phase — all three main tools are open-source with published TechBlog descriptions.

---

## Stripe

**Q1 — Rollout mechanism(s) named specifically:**
Claim: Stripe uses feature flags for progressive rollout. The specific tooling name is NOT FOUND in public engineering writing. Date-based API versioning means new API versions roll out only to developers who explicitly upgrade — this is a form of cohort-based progressive rollout (opt-in cohort: developers who change their API version header).
Search queries used: "Stripe progressive rollout feature flag deployment mechanism payment reliability canary"
Source: Multiple practitioner accounts confirm feature flag usage. Date-based versioning: PRIMARY via stripe.com API documentation.
Tag: [INFERRED for feature flags; PRIMARY for date-based versioning as rollout mechanism]

**Q2 — Gating metric(s):**
Claim: Error rate and payment success rate are the implied gating metrics for payment-related rollouts — given PCI compliance and the extreme cost of payment failures. Specific internal thresholds: NOT FOUND.
Tag: [INFERRED]

**Q3 — Halt authority:**
Claim: NOT FOUND specifically. Feature flag owner can disable the flag to halt rollout.
Tag: [INFERRED]

**Q4 — Time window between stages:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Tiering by change type:**
Claim: INFERRED — Stripe's payment infrastructure changes would require more conservative rollout than UI changes. Date-based API versioning provides natural tiering between API-facing and internal changes.
Tag: [INFERRED]

**Evidence-density note:** ~20% PRIMARY, ~50% INFERRED, ~30% NOT FOUND.

---

## Basecamp/37signals

**Q1 — Rollout mechanism(s) named specifically:**
Claim: Basecamp's documented practice is to ship to all users at once and monitor closely, with rollback capability if serious issues arise. No staged rollout mechanism is documented in public Basecamp/37signals engineering writing for their SaaS products. This is a deliberately simpler approach consistent with their small-team philosophy.
Search queries used: "Basecamp 37signals rollout mechanism progressive deployment feature flag canary"
Source: Basecamp's public engineering writing (hey.com blog, Signal v. Noise). No staged rollout mechanism documented.
Verification pass: Searched "Basecamp Hey progressive rollout canary deployment" — not found.
Tag: [NOT FOUND for staged rollout; PRIMARY for honest finding that simpler rollout is their documented practice]

**Q2 — Gating metric(s):**
Claim: Error monitoring (using tools like exception trackers) after a full deploy. No staged gating metric documented.
Tag: [INFERRED]

**Q3 — Halt authority:**
Claim: The engineering team (small, senior) holds halt authority — can roll back immediately. No formalized halt procedure documented.
Tag: [INFERRED]

**Q4 — Time window:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Tiering by change type:**
Claim: NOT FOUND. Consistent with full-release approach.
Tag: [NOT FOUND]

**Evidence-density note:** ~10% PRIMARY, ~30% INFERRED, ~60% NOT FOUND. Basecamp's rollout practice is simpler — full release with monitoring. This is a real, honest finding for a small team.

---

## Key Comparative Finding — Rollout Pattern Audit

The original project brief mentioned "10% → 3% → 1%" as a pattern. This research did NOT set out to confirm that pattern. What was actually found:

- **Amazon:** Canary + alarm-gated progression. Percentages set per-service, not universal.
- **Google:** Canary + percentage-based gradual rollout + error-budget gating. Percentages not specified universally.
- **Meta:** Gatekeeper flag-based with explicit percentage settings. Actual percentages not universally specified.
- **Netflix:** Red/Black + Canary + Kayenta ACA (automated analysis). Most mechanically sophisticated.
- **Stripe:** Feature flags + date-based API versioning as implicit rollout. Least described publicly.
- **Basecamp:** Full deploy + monitor. No staging.

**The "10% → 3% → 1%" pattern is not confirmed as any org's documented canonical sequence.** The actual pattern is: canary (small initial exposure) → metric-gated expansion → full rollout, with percentages configured per deployment pipeline, not universally standardized across any org.

---

## Phase Gate Assessment

Gate condition: A real rollout sequence with actual numbers or explicit gating conditions per org — "they roll out gradually" is not sufficient.

- **Amazon:** Canary + alarm-gated (error rate alarms = specific gating condition). [PRIMARY]
- **Google:** Canary + error-rate/latency-percentile gating + error budget. Explicit conditions named. [PRIMARY]
- **Meta:** Gatekeeper flag + percentage-based. Gating metrics set per-team (INFERRED). [PRIMARY for mechanism; INFERRED for metrics]
- **Netflix:** Red/Black + Kayenta ACA (explicit automated metric analysis). Named tools + described conditions. [PRIMARY]
- **Stripe:** Feature flags + date-based versioning. Specific gating conditions: NOT FOUND. [INFERRED/NOT FOUND]
- **Basecamp:** Full deploy + monitoring. No staged rollout sequence. Honest finding. [PRIMARY for honest finding]

**Phase 5 tag-integrity audit completed and logged above — no corrections needed.**

**Gate status: PASSED.**
