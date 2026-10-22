# Template 18 — Launch-Readiness Checklist (technical correctness AND real user experience)

**Use when:** the final go/no-go for a public launch. Covers what release-readiness (template 14, per-release) doesn't: the *whole product* as a new user experiences it. Both halves must pass — a technically perfect launch of a confusing product is still a failed launch.

## Part A — Technical correctness

### A1. Build & deploy
- [ ] Release artefact is the tested artefact (R-12); release-readiness (template 14) passed for the launch build
- [ ] Rollback rehearsed; kill switches verified live
- [ ] Migrations rehearsed forward and back on production-shaped data
- [ ] Feature flags: owners, defaults, and expiry dates set (R-16, R-26)

### A2. Reliability & scale
- [ ] Load tested to _…×_ expected launch traffic; breaking point known
- [ ] Failure strategies verified (template 04, §4) — timeouts, breakers, degradation actually exercised
- [ ] Backups running, monitored, and restore-tested (R-24); RPO/RTO written and verified
- [ ] On-call rotation staffed, alert path tested end-to-end (R-29)

### A3. Security & privacy
- [ ] ASVS L1 gap register complete; zero blocking fails (template 13)
- [ ] Dependency scan clean per patch SLA (R-23); SBOM generated
- [ ] Secrets audit: none in code, logs, client bundles, or AI transcripts (R-15)
- [ ] Privacy checklist passed (template 17, §9); data-handling promises match behaviour

### A4. Observability & cost
- [ ] Golden-signal dashboards live (R-28); launch-specific alerts with runbooks (R-29)
- [ ] AI/model cost metering per feature in place; cost anomaly alerts set (R-32)
- [ ] Analytics events for the primary outcome metric verified end-to-end (R-02)

## Part B — Real user experience

### B1. First-run experience (tested as a stranger, on a clean account)
- [ ] Signup/onboarding completable with no outside help; value moment reachable in _…_ minutes
- [ ] A confused user can recover: help, search, support contact all real and monitored
- [ ] First-run UX states verified (loading, empty, error) — template 12

### B2. Authenticity & polish
- [ ] Product authenticity & polish checklist passed (template 17) — all ten sections

### B3. Content & communication
- [ ] Launch announcement (template 03, §1 press release) accurate against the *shipped* product — updated if scope changed
- [ ] Pricing page matches actual billing behaviour; no surprises in the first invoice path
- [ ] Support macros/FAQs ready for the top-5 expected questions; support team briefed
- [ ] Status page live if uptime is promised anywhere

### B4. The "day-two" test
- [ ] A returning user finds their data intact and the product sensibly changed (no silent resets)
- [ ] Notification/email behaviour sane (no spam, unsubscribe works, no secrets in emails)
- [ ] The kill/fix/keep evaluation is scheduled: metric _…_, date _…_, decider _…_ (template 16)

## Decision

- [ ] **LAUNCH** — both halves pass
- [ ] **HOLD** — blocking items: _…_ · owner each: _…_ · re-check date: _…_

*Partial launches (beta, waitlist, geo-limited) are legitimate — they still run this checklist, with N/A reasons for the deferred half.*

## Acceptance criteria

- [ ] No section skipped silently; every N/A has a written reason and a revisit date
- [ ] Part B was verified by someone who did not build the product, on a clean account, on a real device
- [ ] The post-launch evaluation (template 16) is scheduled before launch, not after

## Anti-patterns this blocks

Launching technically-ready-but-user-hostile products · AP-14 (launch messaging vs shipped reality) · AP-18 (cost surprises) · AP-19 (launch with no adoption plan).
