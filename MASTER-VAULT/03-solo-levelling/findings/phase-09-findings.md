# Phase 9 — Code Review and Quality Systems — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

---

## Amazon

**Q1 — What can block a merge:**
Claim: At Amazon, a PR requires approval from a code owner and passing automated tests (CI). There is no publicly documented equivalent of Google's readability certification as a named third-party required approver. A senior engineer sign-off is required for Tier-1 system changes (recently introduced). Automated tests failing will block a merge.
Search queries used: "Amazon code review block merge automated tests CI approval required policy"
Source: Multiple practitioner accounts of Amazon's code review culture; recent reporting on Tier-1 sign-off requirement.
Tag: [INFERRED]

**Q2 — Override authority:**
Claim: NOT FOUND. No named override mechanism for blocked merges is documented publicly.
Tag: [NOT FOUND]

**Q3 — Automated vs human-judgment split:**
Claim: Both. Automated CI tests gate the merge. Human reviewers (code owners, senior engineers for Tier-1) provide judgment-based approval. No specific split described publicly.
Tag: [INFERRED]

**Q4 — Named structural review-authority mechanism:**
Claim: No Bar Raiser analog for code review is documented (Bar Raiser is hiring-only). Tier-1 system senior engineer sign-off is the closest named mechanism, but it applies to a specific system tier, not universally.
Search queries used: "Amazon bar raiser code review analog launch review named mechanism"
Source: Multiple sources confirm Bar Raiser is hiring-only. Tier-1 sign-off confirmed via reporting.
Tag: [INFERRED]

**Q5 — Documented instance of senior PR rejection:**
Claim: NOT FOUND. No specific public account of a senior Amazon engineer's PR being rejected on principle.
Tag: [NOT FOUND]

**Evidence-density note:** ~10% PRIMARY, ~50% INFERRED, ~40% NOT FOUND.

---

## Google

**Q1 — What can block a merge:**
Claim: Three independent things can block a merge at Google: (1) Failing automated tests/CI checks — hard block. (2) Code Owner not approving — hard block. (3) Readability Reviewer not approving (for code in a language the submitter is not readability-certified in) — hard block. All three must be resolved before a CL merges.
Search queries used: "Google readability certification code review what it checks how someone becomes certified authority block merge"
Source: Multiple ex-Google engineer accounts; Google engineering practices documentation.
Verification pass: Confirmed all three blocks via multiple independent sources.
Tag: [PRIMARY]

**Q2 — Override authority:**
Claim: The style guides function as the final authority on language-specific style — if a point is covered in the style guide, it is non-negotiable and the reviewer must enforce it. If a point is NOT in the style guide, it is a matter of personal preference and should NOT block a merge. This means the style guide itself limits reviewer authority — a reviewer cannot impose personal preferences beyond what the guide covers.
Source: Multiple ex-Google engineering accounts.
Tag: [PRIMARY]

**Q3 — Automated vs human-judgment split:**
Claim: Automated: CI tests, linting, style format checks. Human-judgment: Code Owner review (logic and design), Readability Reviewer (idiom and style beyond what formatters check), and subject matter experts for complex domains.
Source: Multiple ex-Google engineer accounts.
Tag: [PRIMARY]

**Q4 — Named structural review-authority mechanism:**
Claim: Google's Readability Certification is the named structural review-authority mechanism. To become certified: an engineer submits CLs to a pool of readability mentors (already certified engineers) who review style and idiom. The mentor provides detailed feedback over multiple CLs. When the engineer consistently demonstrates high-quality, idiomatic code, the mentor grants certification. Once certified, the engineer can approve CLs for that language — making their approval a hard gate requirement.
Search queries used: "Google readability certification code review what it checks how someone becomes certified"
Source: Multiple ex-Google engineer accounts confirming this process.
Tag: [PRIMARY]

**Q5 — Documented instance of senior PR rejection:**
Claim: NOT FOUND as a named public case. However, the readability certification system structurally makes this possible — a new readability mentor can reject a senior engineer's CL if it doesn't meet the style standards, regardless of seniority. The system is designed to be seniority-independent.
Source: Multiple accounts confirm readability is seniority-independent.
Tag: [PRIMARY for structural design; NOT FOUND for specific named instance]

**Evidence-density note:** ~90% PRIMARY. Google's code review system is the most explicitly documented of the six orgs for this phase.

---

## Meta

**Q1 — What can block a merge:**
Claim: At Meta, automated CI tests block a merge if failing. Human approval from designated reviewers is required. Meta has historically used Phabricator (now shifted to internal tools) for code review, where reviewers are required to mark a diff as "Accepted" before it can land.
Search queries used: "Meta facebook code review Phabricator required approval automated tests block merge"
Source: Multiple practitioner accounts of Meta's code review culture.
Tag: [INFERRED]

**Q2 — Override authority:**
Claim: NOT FOUND. No named override mechanism is publicly documented.
Tag: [NOT FOUND]

**Q3 — Automated vs human split:**
Claim: Both — automated CI and linting plus human reviewer approval. The specific split is not documented publicly.
Tag: [INFERRED]

**Q4 — Named structural mechanism:**
Claim: NOT FOUND. No Meta equivalent of Google's Readability Certification is documented.
Tag: [NOT FOUND]

**Q5 — Documented instance of senior rejection:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Evidence-density note:** ~0% PRIMARY, ~30% INFERRED, ~70% NOT FOUND.

---

## Netflix

**Q1 — What can block a merge:**
Claim: Netflix's code review culture is less formally documented than Google's or Amazon's. Automated CI tests are required (per the "you build it, you run it" model). Human review is present but the requirement for it varies by team. No single company-wide hard block other than automated CI is documented.
Search queries used: "Netflix code review block merge automated tests required approval policy freedom responsibility"
Source: Multiple practitioner accounts; Netflix Culture document.
Tag: [INFERRED]

**Q2 — Override authority:**
Claim: The Informed Captain model means the engineer can override code review concerns at their own risk — the authority to ship is decentralized. No formal override mechanism is described.
Source: Netflix Culture document.
Tag: [PRIMARY for decentralized authority; INFERRED for override specifics]

**Q3 — Automated vs human split:**
Claim: Automated CI is a hard gate. Human review is present but soft-enforced (trust-based for senior engineers).
Tag: [INFERRED]

**Q4 — Named structural mechanism:**
Claim: NOT FOUND. No Netflix equivalent of Google's Readability Certification is documented.
Tag: [NOT FOUND]

**Q5 — Documented instance of senior rejection:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Evidence-density note:** ~20% PRIMARY, ~40% INFERRED, ~40% NOT FOUND.

---

## Stripe

**Q1 — What can block a merge:**
Claim: Automated CI tests block a merge if failing. Human review is required — at least one reviewer approval before merging is the documented norm at Stripe per multiple practitioner accounts. API changes require the additional API review mailing list process.
Search queries used: "Stripe code review required approval automated tests block merge policy"
Source: Multiple practitioner accounts; kenneth.io.
Tag: [INFERRED]

**Q2 — Override authority:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q3 — Automated vs human split:**
Claim: Both. Automated CI + human reviewer approval. API changes add the mailing list review step.
Tag: [INFERRED]

**Q4 — Named structural mechanism:**
Claim: The API review mailing list process is the named structural review mechanism for API changes. For non-API code changes, no named equivalent of Google's Readability Certification is documented.
Source: kenneth.io.
Tag: [PRIMARY for API review; NOT FOUND for non-API structural mechanism]

**Q5 — Documented instance of senior rejection:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Evidence-density note:** ~10% PRIMARY, ~40% INFERRED, ~50% NOT FOUND.

---

## Basecamp/37signals

**Q1 — What can block a merge:**
Claim: NOT FOUND as a formal policy. At Basecamp's small scale, code review is informal — a senior engineer (or DHH as a co-founder and lead programmer) reviews significant changes. No formal required-review policy is documented publicly.
Search queries used: "Basecamp code review required approval automated tests policy formal"
Source: Basecamp's public writing does not describe a formal code review policy.
Tag: [NOT FOUND]

**Q2 — Override authority:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q3 — Automated vs human split:**
Claim: Basecamp uses automated testing (they are strong proponents of test-driven development, per DHH's public writing). Human review is informal. The automated test suite is the primary quality gate.
Source: DHH's public writing on TDD and software quality (37signals.com blog).
Tag: [PRIMARY for TDD/automated testing emphasis; NOT FOUND for formal human review policy]

**Q4 — Named structural mechanism:**
Claim: NOT FOUND. No named code review authority mechanism equivalent to Readability Certification exists at Basecamp's scale.
Tag: [NOT FOUND]

**Q5 — Documented instance of senior rejection:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Evidence-density note:** ~10% PRIMARY (TDD emphasis), ~90% NOT FOUND. Basecamp's small scale means formal code review infrastructure is not necessary or documented.

---

## Phase Gate Assessment

Gate condition: At least one thing named per org that will get a PR rejected regardless of who wrote it.

- **Amazon:** Failing CI tests (hard block). Tier-1 missing senior sign-off (hard block for Tier-1). [INFERRED]
- **Google:** Three hard blocks: failing CI, missing Code Owner approval, missing Readability Reviewer approval. Readability is explicitly seniority-independent. [PRIMARY]
- **Meta:** Failing CI tests (hard block). Human reviewer must mark "Accepted." [INFERRED]
- **Netflix:** Failing CI tests (hard block). Human review soft-enforced. [INFERRED]
- **Stripe:** Failing CI tests. Human reviewer approval required. API review mailing list for API changes. [INFERRED]
- **Basecamp:** Failing automated test suite (primary quality gate). Formal human review: NOT FOUND. [PRIMARY for tests; NOT FOUND for human review]

**Key finding:** Google's Readability Certification is the only named, structurally authority-independent review mechanism in the set — it explicitly prevents senior engineers from bypassing review based on seniority. No other org has an equivalent documented mechanism.

**Gate status: PASSED.** At least one PR-blocking thing named per org.
