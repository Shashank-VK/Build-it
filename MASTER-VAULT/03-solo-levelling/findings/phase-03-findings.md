# Phase 3 — Requirements, Scope, and Non-Goals — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

---

## Amazon

**Q1 — Requirement vs nice-to-have distinction:**
Claim: Amazon's PR/FAQ functions as both the requirements document and the scope-enforcement tool. The PR/FAQ's "Day 1" framing forces the team to define what is minimally required for a successful launch. Items not in the press release or FAQ are implicitly deferred. There is no separate formal priority-tier system (like MoSCoW) publicly documented for Amazon's early-stage process.
Search queries used: "Amazon PR/FAQ non-goals out of scope requirements mechanism scope creep prevention working backwards"
Source: Multiple practitioner accounts of the PR/FAQ process; *Working Backwards* (Bryar & Carr) describes "Day 1" definition as the scope anchor.
Verification pass: Searched "Amazon requirements prioritization tier system MoSCoW" — no formal tier system documented for the PR/FAQ stage.
Tag: [INFERRED]

**Q2 — Non-goals section — does it exist and what does it look like:**
Claim: The FAQ section of the PR/FAQ functions as the non-goals mechanism. Specifically, answering "What will be in future versions?" vs "What is in the initial release?" makes deferred scope explicit. There is no standalone "Non-Goals" heading — the FAQs carry this function.
Search queries used: "Amazon PR/FAQ non-goals FAQ section what won't we do scope"
Source: Multiple practitioner accounts confirm the FAQ section as the explicit exclusion mechanism. Stated in the same sources as above.
Verification pass: Searched "Amazon PR/FAQ non-goals explicit section" — no named standalone section found; FAQ confirmed as the mechanism.
Tag: [INFERRED]

**Q3 — Enforcement mechanism against scope creep:**
Claim: The signed-off PR/FAQ document serves as the reference point for scope enforcement. When new feature requests arise during development, they can be measured against the existing PR/FAQ. If they are out of scope, the team has a documented rejection basis. However, the enforcement is relational (the document + social accountability), not automated or checklist-enforced.
Search queries used: "Amazon PR/FAQ scope creep enforcement during development mechanism"
Source: Multiple practitioner accounts describe the PR/FAQ as the "source of truth" against scope expansion.
Verification pass: Searched "Amazon scope creep prevention mechanism during engineering" — consistent with PR/FAQ-as-reference characterization.
Tag: [INFERRED]

**Q4 — Authority to revise a non-goal mid-project:**
Claim: NOT FOUND. No specific named role or process for formally revising a PR/FAQ's deferred scope mid-project is publicly documented. Changes to scope would implicitly require revisiting the PR/FAQ and reconvening a review meeting.
Search queries used: "Amazon PR/FAQ revise scope mid-project authority who approves change"
Source: NOT FOUND.
Verification pass: Not found.
Tag: [NOT FOUND]

**Q5 — Documented instance of successful scope pushback:**
Claim: NOT FOUND. No specific public account of a named instance where scope reintroduction was formally resisted using the PR/FAQ is documented.
Search queries used: "Amazon PR/FAQ scope pushback real example feature rejected"
Source: NOT FOUND.
Tag: [NOT FOUND]

**Q6 — Change-management handling (Lens 4):**
Claim: Scope changes at the PR/FAQ stage are addressed by iterating the document — re-writing and re-reviewing. No formal change-order process is documented. The document is iterated before build begins; changes during build would require escalation back to the PR/FAQ owner and potentially a new review meeting.
Search queries used: "Amazon PR/FAQ scope change mid-build change order process"
Source: Multiple practitioner accounts describe PR/FAQ as iterative before build, not a fixed contract.
Tag: [INFERRED]

**Evidence-density note:** ~0% PRIMARY, ~60% INFERRED, ~40% NOT FOUND. Amazon's scope discipline is documented at the philosophy level but the specific enforcement mechanism (particularly for mid-project revisions) is not publicly detailed.

---

## Google

**Q1 — Requirement vs nice-to-have distinction:**
Claim: Google design docs use a Goals/Non-Goals structure. Within Goals, there is no formally published priority-tier system (like P0/P1/P2 in some orgs). The Goals section defines what the system must do; the Non-Goals section defines what it explicitly will not do. Priority within goals is informally determined by the engineer and reviewers.
Search queries used: "Google design doc requirements prioritization goals non-goals priority tier system"
Source: industrialempathy.com ("Design Docs at Google" by Malte Ubl, named ex-Google engineer) — confirms Goals and Non-Goals as the structural distinction, no priority tier within Goals described.
Verification pass: Searched "Google design doc P0 P1 priority system" — no formal tier system for design docs found.
Tag: [PRIMARY]

**Q2 — Non-goals section — does it exist and what does it look like:**
Claim: Google design docs include an explicit "Non-Goals" section as standard. Malte Ubl's public account describes Non-Goals as a place to list things people might expect the design to cover but that are intentionally excluded. Example structure from practitioner accounts: brief bulleted list with one-line justification for each exclusion, e.g., "No MFA in this release — handled in follow-up project."
Search queries used: "Google design doc non-goals section enforcement scope creep mechanism engineer account real example"
Source: industrialempathy.com — named ex-Google engineer explicitly describes the Non-Goals section as standard. Also google.com's own technical writing guide mentions Non-Goals in design docs.
Verification pass: Searched "Google design doc template non-goals section" — confirmed by multiple independent practitioner accounts citing Ubl's article and Google's own writing guides.
Tag: [PRIMARY]

**Q3 — Enforcement mechanism against scope creep:**
Claim: The Non-Goals section of the signed design doc serves as the reference for scope enforcement. According to the industrialempathy.com account: when feature requests emerge mid-project, the Non-Goals section "shifts the burden of proof to those wanting to change the scope." The enforcement is documentary and social — there is no automated check.
Search queries used: "Google design doc non-goals scope enforcement burden of proof mid-project"
Source: industrialempathy.com — explicit description of the mechanism.
Verification pass: Multiple secondary sources corroborate this characterization.
Tag: [PRIMARY]

**Q4 — Authority to revise a non-goal mid-project:**
Claim: NOT FOUND specifically. By implication from the design doc culture, revising a Non-Goal would require updating the design doc and re-engaging the original reviewers. No named role or formal change-order process for Non-Goals revisions is documented publicly.
Search queries used: "Google design doc revise non-goals mid-project who approves scope change"
Source: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Documented instance of successful scope pushback:**
Claim: NOT FOUND. No specific named public instance of a Google project using the Non-Goals section to push back against scope reintroduction is documented.
Search queries used: "Google design doc non-goals pushback real example scope rejected"
Source: NOT FOUND.
Tag: [NOT FOUND]

**Q6 — Change-management handling (Lens 4):**
Claim: Design docs are described as "living documents" — they can be updated as the project evolves. A Non-Goal can be revised by updating the design doc, but the expectation is that the new scope is explicitly re-discussed, not quietly added. No formal process for Lens 4 scope changes is documented.
Search queries used: "Google design doc living document scope change update Non-Goals mid-project"
Source: industrialempathy.com describes design docs as living; scope changes require updating the doc.
Tag: [PRIMARY]

**Evidence-density note:** ~60% PRIMARY (industrialempathy.com is a named ex-Google engineer technical account), ~10% INFERRED, ~30% NOT FOUND. Google's Non-Goals mechanism is the best-documented of the six orgs for this phase.

---

## Meta

**Q1 — Requirement vs nice-to-have distinction:**
Claim: NOT FOUND as a publicly documented formal system. Meta's fast-iteration culture suggests priority is informally determined. No formal "requirements tier" system is described in Meta's public engineering writing for the RFC stage.
Search queries used: "Meta RFC requirements prioritization tier system nice to have must have"
Source: NOT FOUND.
Tag: [NOT FOUND]

**Q2 — Non-goals section — does it exist and what does it look like:**
Claim: NOT FOUND as a named standard section. The Meta RFC template is not publicly documented in detail. Whether a Non-Goals equivalent exists in the RFC template is not confirmed in public sources.
Search queries used: "Meta RFC template non-goals out of scope section structure"
Source: NOT FOUND.
Tag: [NOT FOUND]

**Q3 — Enforcement mechanism against scope creep:**
Claim: SPECULATIVE. Meta's "move fast" culture suggests scope discipline is less formally enforced than at Amazon or Google. The Gatekeeper feature-flag system provides a technical scope boundary (features behind a flag that is never enabled are de facto excluded) but this is a deployment mechanism, not a requirements-scope mechanism.
Search queries used: "Meta facebook scope creep prevention mechanism RFC engineering"
Source: General characterization from Meta's engineering culture; Gatekeeper described as a deployment mechanism, not a requirements boundary.
Tag: [SPECULATIVE]

**Q4 — Authority to revise a non-goal mid-project:**
Claim: NOT FOUND.
Search queries used: "Meta RFC scope change authority revise mid-project"
Source: NOT FOUND.
Tag: [NOT FOUND]

**Q5 — Documented instance of successful scope pushback:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q6 — Change-management handling (Lens 4):**
Claim: NOT FOUND. Meta's fast-iteration culture implies scope can shift frequently, but no formal Lens 4 mechanism for scope changes within a project is documented.
Tag: [NOT FOUND]

**Evidence-density note:** ~0% PRIMARY, ~10% SPECULATIVE, ~90% NOT FOUND. Meta's scope-management specifics at the RFC level are not publicly documented. This is an honest finding, not a gap to fill.

---

## Netflix

**Q1 — Requirement vs nice-to-have distinction:**
Claim: No company-wide formal distinction. Each team/Informed Captain determines scope independently. There is no standard requirements document with a priority-tier system documented for Netflix.
Search queries used: "Netflix requirements prioritization nice to have must have formal scope discipline"
Source: Netflix Culture document; consistent characterization from Netflix TechBlog.
Tag: [PRIMARY — the absence of a company-wide system is itself a PRIMARY finding from Netflix's own Culture document]

**Q2 — Non-goals section — does it exist and what does it look like:**
Claim: No company-wide Non-Goals section is standard. Scope discipline is left to individual teams. This is a legitimate finding, not a gap — Netflix's "highly aligned, loosely coupled" model explicitly decentralizes these decisions.
Search queries used: "Netflix non-goals out of scope section design doc requirements"
Source: Netflix Culture document characterizes this as per-team autonomy.
Tag: [PRIMARY]

**Q3 — Enforcement mechanism against scope creep:**
Claim: No company-wide enforcement mechanism. Within a team, scope is enforced through the "Informed Captain" model — the captain is accountable for outcomes and can reject scope additions that don't serve the hypothesis being tested. A/B test metrics serve as the ultimate arbiter of what to include.
Search queries used: "Netflix scope creep prevention team level mechanism A/B test"
Source: Netflix TechBlog (multiple posts on full-cycle ownership and experimentation culture).
Tag: [PRIMARY]

**Q4 — Authority to revise scope mid-project:**
Claim: The Informed Captain has authority to revise scope at any time. No external approval is required. This is intentional — the F&R model grants this authority explicitly.
Search queries used: "Netflix scope change mid-project authority informed captain"
Source: Netflix Culture document.
Tag: [PRIMARY]

**Q5 — Documented instance of successful scope pushback:**
Claim: NOT FOUND. Netflix's decentralized model means scope pushback stories are not publicly documented as case studies.
Tag: [NOT FOUND]

**Q6 — Change-management handling (Lens 4):**
Claim: Scope changes are absorbed by the Informed Captain model with no formal process. The team pivots when A/B data warrants it. No formal change-order process.
Source: Netflix Culture document; Netflix TechBlog.
Tag: [PRIMARY]

**Evidence-density note:** ~60% PRIMARY, ~40% NOT FOUND. Netflix's scope discipline is well-characterized as deliberately decentralized — the absence of a formal mechanism is itself a primary, sourced finding.

---

## Stripe

**Q1 — Requirement vs nice-to-have distinction:**
Claim: Stripe's API-first culture makes the API surface itself the primary scope boundary. A capability not exposed in the API is a de facto non-goal. For internal requirements, no formal priority-tier system is publicly documented.
Search queries used: "Stripe API surface as scope boundary requirements non-goal API first"
Source: Multiple practitioner accounts describe Stripe's API as the product boundary; kenneth.io (named former Stripe engineer) describes the API review process as the scope gate.
Tag: [INFERRED]

**Q2 — Non-goals section — does it exist and what does it look like:**
Claim: The API specification itself functions as the Non-Goals mechanism — endpoints and parameters not in the API spec are not in scope. For design documents preceding API work, no standard Non-Goals section is publicly documented.
Search queries used: "Stripe API spec non-goals out of scope design doc section"
Source: Implied by the API-as-product philosophy described in multiple practitioner accounts.
Verification pass: Searched "Stripe design doc non-goals section" — not found as a named standard.
Tag: [INFERRED]

**Q3 — Enforcement mechanism against scope creep:**
Claim: The API review mailing list process enforces scope at the API level — proposed additions must go through the review. The API's backward-compatibility requirement also serves as a natural scope enforcement: breaking changes are treated as scope escalations requiring special review.
Search queries used: "Stripe scope creep prevention API review mailing list backward compatibility"
Source: kenneth.io (named former Stripe engineer) and multiple corroborating accounts.
Tag: [INFERRED]

**Q4 — Authority to revise scope mid-project:**
Claim: NOT FOUND. No specific role or process for formally revising API scope mid-project is publicly documented.
Tag: [NOT FOUND]

**Q5 — Documented instance of successful scope pushback:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q6 — Change-management handling (Lens 4):**
Claim: Stripe's date-based API versioning system handles scope change implicitly — new capabilities are added to new API versions, preserving the scope of old versions. This is a technical scope management mechanism, not a process document.
Search queries used: "Stripe API versioning scope change management date-based versioning"
Source: Multiple accounts confirm Stripe's date-based API versioning as a scope isolation mechanism.
Tag: [INFERRED]

**Evidence-density note:** ~0% PRIMARY (no stripe.com/blog source for this phase), ~60% INFERRED, ~40% NOT FOUND. Stripe's scope discipline is effectively enforced through API design culture, not process documents.

---

## Basecamp/37signals

**Q1 — Requirement vs nice-to-have distinction:**
Claim: In Shape Up, the "appetite" replaces the requirements list as the primary scope constraint. The appetite is a fixed time budget (e.g., 2 weeks = small batch; 6 weeks = large batch). What can be shipped within the appetite is in scope; what can't is not. There is no MoSCoW or priority-tier system — the time constraint forces the trade-offs automatically.
Search queries used: "Basecamp Shape Up no-gos scope enforcement circuit breaker mechanism scope hammer"
Source: *Shape Up* (Ryan Singer, 2019) — basecamp.com/shapeup explicitly describes appetite as the scope constraint.
Verification pass: Confirmed via basecamp.com/shapeup.
Tag: [PRIMARY]

**Q2 — Non-goals section — does it exist and what does it look like:**
Claim: "No-gos" are an explicit named section of the Pitch document (one of the five required sections). They list functionality or use cases deliberately NOT covered in this cycle. Structural form: a bulleted list of explicitly excluded scope items, stated at the pitch stage before any build commitment.
Search queries used: "Basecamp Shape Up no-gos section pitch document structure example"
Source: *Shape Up* (Ryan Singer, 2019) — Chapter on Pitches explicitly describes No-gos as a required section.
Verification pass: Confirmed via direct basecamp.com/shapeup text.
Tag: [PRIMARY]

**Q3 — Enforcement mechanism against scope creep:**
Claim: Three named enforcement mechanisms exist in Shape Up: (1) No-gos in the Pitch (pre-build exclusion list), (2) Scope Hammering (active questioning during build: "Is this a must-have? Could we ship without this?"), (3) Circuit Breaker (hard 6-week deadline — project stops at cycle end, no automatic extension). Together these create "fixed time, variable scope."
Search queries used: "Basecamp Shape Up scope hammer circuit breaker mechanism names"
Source: *Shape Up* (Ryan Singer, 2019) — all three mechanisms described explicitly. Confirmed via basecamp.com/shapeup.
Verification pass: Multiple independent summaries of Shape Up confirm all three named mechanisms.
Tag: [PRIMARY]

**Q4 — Authority to revise a no-go mid-project:**
Claim: The team building the project has authority to make scope trade-offs during the build cycle (scope hammering). Revising a No-go to include previously excluded scope would require escalating back to the Betting Table — there is no mid-cycle authority granted to expand scope without this.
Search queries used: "Basecamp Shape Up revise no-go mid-cycle who approves scope expansion"
Source: *Shape Up* describes the team as having authority to *cut* scope (scope hammer) but not to *add* excluded scope without re-engaging the shaping/betting process.
Tag: [PRIMARY]

**Q5 — Documented instance of successful scope pushback:**
Claim: The circuit breaker mechanism in Shape Up is itself a documented scope enforcement — if a project cannot ship within the appetite, it stops rather than extending. This is a documented mechanism for resisting scope that would blow the time budget. A specific named instance of this happening to a Hey.com feature is not publicly documented.
Search queries used: "Basecamp circuit breaker real instance project stopped scope exceeded"
Source: *Shape Up* describes the circuit breaker philosophy. Specific named instance: NOT FOUND publicly.
Tag: [PRIMARY for mechanism; NOT FOUND for specific named instance]

**Q6 — Change-management handling (Lens 4):**
Claim: Shape Up's Lens 4 answer is: scope changes during a cycle are handled by scope hammering (cutting, not adding). If requirements shift fundamentally mid-cycle, the project may be stopped by the circuit breaker and returned to shaping. There is no mid-cycle scope-addition process.
Source: *Shape Up* (Ryan Singer, 2019).
Tag: [PRIMARY]

**Evidence-density note:** ~90% PRIMARY, ~10% NOT FOUND (specific named instance only). Basecamp's scope discipline is the most explicitly documented of the six orgs — Shape Up names the mechanisms (No-gos, Scope Hammer, Circuit Breaker) and describes their structure precisely.

---

## Phase Gate Assessment

Concrete enforcement mechanism identified for every org where evidence exists:
- **Amazon:** PR/FAQ FAQ section as exclusion reference (INFERRED — no automation)
- **Google:** Non-Goals section with burden-of-proof shift (PRIMARY)
- **Meta:** NOT FOUND — honestly documented
- **Netflix:** Informed Captain model + A/B test outcomes (PRIMARY — deliberate decentralization)
- **Stripe:** API surface + API review process (INFERRED)
- **Basecamp:** No-gos + Scope Hammer + Circuit Breaker — three named mechanisms (PRIMARY)

**Gate status: PASSED.** No org forced into a uniform template. Meta and the mid-project revision questions across all orgs are honestly documented as NOT FOUND where appropriate.
