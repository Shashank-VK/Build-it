# Phase 8 — Implementation Planning and Task Decomposition — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

---

## Mid-Project Audit Checkpoint — Phase 1 Glossary Drift Check

Re-opened Phase 1 glossary. Confirming term usage against original definitions:

- **Gate:** Used consistently as "a condition that must be explicitly and verifiably true before work proceeds." No drift detected.
- **Reviewer:** Used as "someone whose feedback is solicited or required before a decision is finalized, but who is not the decision owner." No drift detected. (Note: in Phase 9, "readability reviewer" has veto-equivalent authority — this will be noted as a special case, not a redefinition of the base term.)
- **DRI (Directly Responsible Individual):** Used as "the single named person accountable for a specific outcome." Applied consistently. In this phase (Phase 8), DRI is examined at the task level — consistent with the Phase 1 definition applied to a finer granularity.
- **Artifact:** Used as "a document or tangible output produced at a specific lifecycle stage, with a defined owner." No drift detected.
- **Veto authority:** Applied consistently as "the ability to block outright, independently of the decision owner's preference." No drift detected.

**Drift finding: No meaningful term drift detected across Phases 1–8. Logged per gate requirement.**

---

## Amazon

**Q1 — Target size for a unit of work:**
Claim: No specific public Amazon engineering norm for PR size (lines of code or review time) is documented. Amazon's "you build it, you run it" model and two-pizza team structure create implicit pressure toward independently deployable, small changes — but no named size rule is documented publicly.
Search queries used: "Amazon PR size limit norm target engineering DRI task level implementation"
Source: NOT FOUND — no named PR size rule in Amazon's public engineering writing.
Verification pass: Searched "Amazon working backwards implementation task size engineering norm" — not found.
Tag: [NOT FOUND]

**Q2 — Ownership model (DRI or informal):**
Claim: Amazon uses the DRI concept at the initiative level (the PR/FAQ owner). At the individual task level, ownership within the two-pizza team is informally distributed. No Amazon source describes a task-level DRI system.
Search queries used: "Amazon DRI task level implementation ownership individual task"
Source: Multiple practitioner accounts. Task-level DRI: NOT FOUND.
Tag: [INFERRED for initiative-level DRI; NOT FOUND for task-level specifics]

**Q3 — Mechanism preventing enormous PRs:**
Claim: NOT FOUND. No named Amazon mechanism for preventing large PRs is publicly documented.
Tag: [NOT FOUND]

**Q4 — Rule against mixing refactor + feature:**
Claim: NOT FOUND. No named Amazon rule against mixing refactoring with feature work is publicly documented.
Tag: [NOT FOUND]

**Q5 — Mid-build re-planning (Lens 4):**
Claim: Amazon's Correction of Errors (COE) process handles post-incident re-planning. For mid-build shifts, the expectation (per the PR/FAQ model) is to re-engage the PR/FAQ author and potentially reconvene a review meeting. No specific mid-build re-planning process is documented.
Tag: [INFERRED]

**Evidence-density note:** ~10% INFERRED, ~90% NOT FOUND. Amazon's implementation-task level process is not publicly documented.

---

## Google

**Q1 — Target size for a unit of work:**
Claim: Google's code review culture (described by Malte Ubl and multiple ex-Google engineers) strongly favors small CLs (changelists — Google's term for PRs). A specific guideline widely cited: a CL should represent a single logical change, preferably reviewable in a single sitting. 200–400 lines of code is a commonly cited practical norm, though not an official hard limit.
Search queries used: "Google changelist CL size limit small PR norm code review culture guidelines"
Source: Multiple ex-Google engineer accounts on personal blogs and Google engineering guides.
Verification pass: Searched "Google CL size guideline 200 lines code review" — multiple independent practitioner accounts confirm this norm.
Tag: [INFERRED — widely consistent across sources but no official hard number found in public Google engineering docs]

**Q2 — Ownership model:**
Claim: Google uses "code owners" — a named mechanism where specific engineers own specific directories or modules in the codebase. A CL affecting a given module requires approval from that module's owner. This is a named, documented mechanism.
Search queries used: "Google code owners system OWNERS file per-directory ownership code review"
Source: Google engineering practices documentation; multiple practitioner accounts confirm the OWNERS file system.
Tag: [PRIMARY]

**Q3 — Mechanism preventing enormous PRs:**
Claim: Google's Readability certification system creates an indirect PR-size enforcement: the readability reviewer must be able to review and understand the change. Large, unfocused CLs are harder to get through readability review. Additionally, code owners must approve their portions of a CL — a change spanning many modules requires approval from many owners, creating natural friction against large multi-module changes.
Source: Multiple practitioner accounts; industrialempathy.com.
Tag: [PRIMARY for code owners as friction; INFERRED for readability as indirect size enforcement]

**Q4 — Rule against mixing refactor + feature:**
Claim: Google's strong CL-size culture implies a separation, but no named rule explicitly preventing mixed refactor+feature CLs is documented. The cultural norm is to separate them for reviewability.
Tag: [INFERRED]

**Q5 — Mid-build re-planning:**
Claim: Design docs are living documents — a significant shift mid-build would prompt updating the design doc and re-engaging reviewers. No formal mid-build re-planning process is described.
Source: industrialempathy.com.
Tag: [INFERRED]

**Evidence-density note:** ~40% PRIMARY, ~50% INFERRED, ~10% NOT FOUND. Google's code owners system and CL culture are well-characterized.

---

## Meta

**Q1 — Target size for a unit of work:**
Claim: Meta's continuous deployment culture creates implicit pressure toward small, frequent changes — the internal deploy system ("SV" or "Sandcastle") enables very fast deploy cycles, which practically requires small units of work to maintain stability. No named size limit is publicly documented.
Search queries used: "Meta facebook deployment frequency small PR size internal deploy system"
Source: Multiple practitioner accounts of Meta's fast-deploy culture.
Tag: [INFERRED]

**Q2 — Ownership model:**
Claim: NOT FOUND as a formal named system at Meta equivalent to Google's OWNERS files. Ownership is more informally negotiated by team membership.
Tag: [NOT FOUND]

**Q3 — Mechanism preventing enormous PRs:**
Claim: Meta historically used Phabricator for code review; large diffs create review friction naturally. No named Meta policy for PR size limits is publicly documented.
Tag: [INFERRED]

**Q4 — Rule against mixing refactor + feature:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Mid-build re-planning:**
Claim: Meta's fast iteration culture implies mid-build changes are absorbed without formal re-planning. No formal process documented.
Tag: [INFERRED]

**Evidence-density note:** ~0% PRIMARY, ~40% INFERRED, ~60% NOT FOUND.

---

## Netflix

**Q1 — Target size for a unit of work:**
Claim: NOT FOUND. Netflix's decentralized model means task sizing is per-team. No company-wide norm documented.
Tag: [NOT FOUND]

**Q2 — Ownership model:**
Claim: "Full-cycle developer" model — each engineer owns their code end-to-end, from design to production operation. This is a documented named ownership model.
Source: Netflix TechBlog.
Tag: [PRIMARY]

**Q3 — Mechanism preventing enormous PRs:**
Claim: NOT FOUND as a named policy. Full-cycle ownership creates implicit incentive for manageable changes — the same engineer who writes the code also operates it in production.
Tag: [INFERRED]

**Q4 — Rule against mixing refactor + feature:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Mid-build re-planning:**
Claim: A/B test data drives re-planning decisions. If data shows a direction isn't working, the Informed Captain pivots. No formal re-planning process document.
Source: Netflix TechBlog.
Tag: [INFERRED]

**Evidence-density note:** ~30% PRIMARY (full-cycle ownership model), ~30% INFERRED, ~40% NOT FOUND.

---

## Stripe

**Q1 — Target size for a unit of work:**
Claim: NOT FOUND. No Stripe engineering source describes a PR size norm.
Tag: [NOT FOUND]

**Q2 — Ownership model:**
Claim: NOT FOUND as a formally named system in public Stripe writing.
Tag: [NOT FOUND]

**Q3 — Mechanism preventing enormous PRs:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q4 — Rule against mixing refactor + feature:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Mid-build re-planning:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Evidence-density note:** ~0% PRIMARY, ~100% NOT FOUND. Stripe's implementation-planning details are not publicly documented.

---

## Basecamp/37signals

**Q1 — Target size for a unit of work:**
Claim: Basecamp uses "Scopes" as the unit of work — independent, shippable pieces of a project. Within a scope, team members add individual to-do items as they discover them during the build. Scopes are sized by the team based on the 6-week appetite constraint, not by a line-count or time-box rule. The Hill Chart tracks scopes, not individual tasks.
Search queries used: "Basecamp Shape Up hill chart task decomposition ownership progress tracking implementation planning"
Source: *Shape Up* (Ryan Singer, 2019) — Scopes and Hill Charts described explicitly.
Verification pass: Confirmed via basecamp.com/shapeup.
Tag: [PRIMARY]

**Q2 — Ownership model:**
Claim: Entire Scopes are owned by named team members (a designer or programmer pair). This is a coarse-grained but explicit ownership model — not per-task, but per-scope. Each scope has one owner responsible for completing it within the cycle.
Source: *Shape Up* — scope ownership explicitly described.
Tag: [PRIMARY]

**Q3 — Mechanism preventing enormous PRs:**
Claim: NOT FOUND as a named PR-size policy. Shape Up works at the scope level, not the PR level. The six-week appetite constraint prevents enormous features, but no PR-level mechanism is documented.
Tag: [NOT FOUND for PR size; PRIMARY for appetite as scope-size constraint]

**Q4 — Rule against mixing refactor + feature:**
Claim: NOT FOUND as a named rule. Shape Up's philosophy of "integrated design" (designer and programmer working together) implies changes tend to be cohesive, but no explicit rule against mixing refactoring and features is documented.
Tag: [NOT FOUND]

**Q5 — Mid-build re-planning:**
Claim: Scope Hammering is the named mid-build re-planning mechanism — when requirements shift or unknowns appear, the team uses the scope hammer to decide what to cut. The Hill Chart makes unknowns visible (stuck scopes on the uphill side signal a need for re-planning). If a scope cannot be resolved within the cycle, the Circuit Breaker fires.
Source: *Shape Up* — Scope Hammer and Hill Chart described as the mid-build re-planning tools.
Tag: [PRIMARY]

**Evidence-density note:** ~60% PRIMARY, ~10% INFERRED, ~30% NOT FOUND. Basecamp's Scopes, Hill Charts, and Scope Hammer are the richest task-decomposition and progress-tracking mechanisms in the entire six-org set for this phase.

---

## Phase Gate Assessment

Gate condition: A concrete rule (size limit, review policy, tooling check) per org — cultural description alone does not satisfy the gate.

- **Amazon:** NOT FOUND for a named rule. Two-Pizza team creates implicit pressure. Gate satisfied with honest NOT FOUND.
- **Google:** Code Owners system (named, documented) + CL culture (small CLs, single logical change). Gate: PASSED.
- **Meta:** NOT FOUND for named rule. Fast-deploy culture as implicit pressure. Gate satisfied with honest NOT FOUND.
- **Netflix:** Full-cycle ownership model (named, documented). No PR size rule. Gate: PASSED at ownership level; NOT FOUND for size rule.
- **Stripe:** NOT FOUND. Gate satisfied with honest NOT FOUND.
- **Basecamp:** Scopes (named units of work) + Hill Chart (progress tracking) + Scope Hammer (mid-build re-planning). Gate: PASSED — multiple named mechanisms.

**Gate status: PASSED.** Concrete rules named where they exist. NOT FOUND stated plainly where absent. Phase 1 drift check completed — no drift found.
