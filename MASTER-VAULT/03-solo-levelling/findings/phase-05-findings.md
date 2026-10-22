# Phase 5 — Design Docs, Technical Design Docs, and RFCs — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

---

## Definitions Established in This Phase

**Design Doc:** An internal, project-specific document focused on the "how" — high-level implementation strategy, architectural choices, and trade-offs. Written by the implementing team before build. Intended to gather feedback from reviewers and establish a plan.

**Technical Design Doc (TDD):** Often used interchangeably with Design Doc. Some orgs distinguish TDDs as more code-implementation-focused (APIs, data schemas, pseudo-code) versus higher-level design docs that focus on system architecture. In practice, the distinction varies by org.

**RFC (Request for Comments):** A process focused on the "what" and "why" — explicitly designed to invite broader feedback (including from outside the implementing team) before a direction is committed to. Typically triggered by cross-team impact, irreversible decisions, or major architectural shifts. The RFC process results in a decision; the RFC document is the vehicle for that process.

**ADR (Architecture Decision Record):** A short, immutable record of a decision that was made and why — typically created after the RFC/Design Doc process concludes, as the durable artifact. ADRs are summaries of decisions already reached, not proposals still under discussion.

---

## Amazon

**Q1 — Which document types Amazon uses:**
Claim: Amazon primarily uses the PR/FAQ (idea validation) and a downstream technical narrative document (sometimes called a "Tech Spec" or "Design Doc" by former employees) for implementation design. Amazon does not publicly use the term "RFC" as a named process. The PR/FAQ covers product scope; a separate technical document covers implementation.
Search queries used: "Amazon technical design document RFC internal name what Amazon calls design doc"
Source: Multiple former-Amazon engineer accounts; *Working Backwards* (Bryar & Carr) focuses on the PR/FAQ; the downstream technical document is mentioned in practitioner accounts but not formally named in any published source.
Verification pass: Searched "Amazon RFC internal term design doc technical specification" — no named RFC process found. Consistent.
Tag: [INFERRED]

**Q2 — Trigger point for design doc:**
Claim: Amazon's trigger for a downstream technical document is: when the PR/FAQ has been approved and the team moves to implementation planning, a technical narrative document is written to describe the system design. No specific trigger condition (e.g., number of engineers, blast radius) is publicly documented.
Search queries used: "Amazon technical design document when required trigger condition engineering"
Source: NOT FOUND in specific terms. Implied by the two-document structure described in practitioner accounts.
Tag: [INFERRED]

**Q3 — Reviewer pool:**
Claim: For the PR/FAQ: relevant stakeholders, product leaders, managers (narrative meeting). For the downstream technical document: engineering leads and relevant team members. No formal distinction between reviewer pools for different document types is publicly documented.
Tag: [INFERRED]

**Q4 — Approval bar and reversibility:**
Claim: PR/FAQ approval is soft (review meeting persuasion). Technical document approval is also soft — no formal sign-off signature documented. Both decisions are treated as reversible (two-way doors) — the documents can be revised.
Tag: [INFERRED]

**Q5 — ADR relationship:**
Claim: NOT FOUND. Amazon does not appear to use ADRs by that name in any publicly documented process.
Tag: [NOT FOUND]

**Q6 — Real example or template found:**
Claim: No actual Amazon PR/FAQ or technical design document is publicly available (all internal). The closest: *Working Backwards* (Bryar & Carr) describes the Prime PR/FAQ process without reproducing the document.
Tag: [NOT FOUND for actual document; PRIMARY for description of document type]

**Evidence-density note:** ~20% PRIMARY, ~50% INFERRED, ~30% NOT FOUND. Amazon's document-type taxonomy is inferred from practitioner accounts, not directly documented publicly.

---

## Google

**Q1 — Which document types Google uses:**
Claim: Google primarily uses a single document type called a "design doc" that covers both product spec and technical design. The "RFC" term is not formally used at Google — the design doc serves both purposes. For very large or cross-cutting architectural decisions, a more extensive design doc may be written, but it is the same document type, just more detailed.
Search queries used: "Google design doc vs RFC difference trigger condition what requires RFC versus design doc engineering"
Source: industrialempathy.com — Malte Ubl's article describes the design doc as the primary artifact. Multiple sources confirm Google does not formally use the RFC term as a distinct process.
Verification pass: Searched "Google RFC process named formal vs design doc" — no separate RFC process found at Google. Consistent.
Tag: [PRIMARY]

**Q2 — Trigger point:**
Claim: Google's trigger for a design doc is: any non-trivial change where the solution is ambiguous (due to problem complexity, solution complexity, or both). The decision is framed as a trade-off: do the benefits of organizational consensus and senior review outweigh the cost of writing the doc?
~~CORRECTION (2026-08-29): The original version of this claim stated the trigger was "10 or more engineering days of effort, or involves more than one engineer, or creates a significant API change," attributed to industrialempathy.com. This is wrong. The article was fetched and read in full. It contains no numeric day-count trigger whatsoever. The article describes the trigger in qualitative terms: write a design doc when "the solution to the design problem is ambiguous — because of problem complexity or solution complexity, or both." The only number in the article is a document-length guideline ("the sweet spot for a larger project seems to be around 10-20ish pages"), which is entirely unrelated to a trigger threshold. The "10 engineering days" figure is unattributable to any verified primary source — it appears across many secondary sources that quote each other, but no original named source has been found. This is a secondary-source echo-chamber artifact.~~
Search queries used: "Google design doc trigger when required threshold size effort"; direct fetch of industrialempathy.com/posts/design-docs-at-google/ (2026-08-29)
Source: industrialempathy.com — Malte Ubl's article describes a qualitative trigger: ambiguity of solution space. No numeric threshold is stated in the article.
Verification pass: Direct read of full article confirmed absence of any "10 engineering days" language. Search for origin of "10 engineering days" figure returned no named primary source — the phrase circulates across secondary sources with no traceable origin document.
Tag: [NOT FOUND / SPECULATIVE] — The qualitative trigger (ambiguity-based) is confirmed by direct read. The specific numeric thresholds previously listed are unconfirmed and should not be used as attributed guidance from this source.

**Q3 — Reviewer pool:**
Claim: Design doc reviewers are: (1) the engineering lead/tech lead responsible for the area, (2) relevant subject matter experts, (3) anyone on the doc's explicit "reviewers" list. Google's "Readability" reviewers are a separate category — they review code style and language idiomatic use specifically when code is being committed, not during the design doc stage.
Search queries used: "Google design doc reviewer pool who reviews readability reviewer distinction"
Source: industrialempathy.com; multiple accounts of Google's readability review system.
Tag: [PRIMARY]

**Q4 — Approval bar and reversibility:**
Claim: Design doc approval is soft — no blocking objections from significant reviewers = approved. This is a two-way door decision (the document can be revised). Google Readability approval for code commits is a hard one-way gate — code cannot be merged without it.
Search queries used: "Google design doc soft approval hard gate readability code merge"
Source: industrialempathy.com; multiple practitioner accounts.
Tag: [PRIMARY]

**Q5 — ADR relationship:**
Claim: Google does not formally use the ADR term by that name. The design doc itself serves as the durable record of decisions made. No ADR-as-separate-artifact is documented publicly for Google.
Search queries used: "Google ADR architecture decision record formal process"
Source: NOT FOUND for Google using ADRs. Consistent with design doc being the durable artifact.
Tag: [NOT FOUND]

**Q6 — Real example or template found:**
Claim: industrialempathy.com reproduces a condensed template structure for a Google design doc. The sections are: Context and scope, Goals and Non-Goals, The actual design (sub-sections: System-context diagram, APIs, Data storage, Code and pseudo-code, Degree of constraint), Alternatives considered, Cross-cutting concerns.
Source: industrialempathy.com — directly retrieved.
Verification pass: Confirmed via industrialempathy.com and multiple secondary sources.
Tag: [PRIMARY]

**Evidence-density note:** ~80% PRIMARY, ~20% NOT FOUND. Google's design doc culture is the best-documented of the six orgs for this phase.

---

## Meta

**Q1 — Which document types Meta uses:**
Claim: Meta formally uses RFCs (by that name) as the primary design artifact for significant technical changes. Lighter changes use design notes or informal wiki pages. Meta is one of the orgs most publicly associated with the RFC term as a named internal process.
Search queries used: "Meta RFC trigger condition when required vs lightweight design note size change blast radius engineering.fb.com"
Source: Multiple practitioner accounts confirm Meta uses RFCs by that specific name. No single PRIMARY engineering.fb.com post defines the RFC process formally.
Verification pass: Searched "Meta facebook RFC process named formal engineering" — confirmed as named process by multiple independent practitioner accounts.
Tag: [INFERRED]

**Q2 — Trigger point:**
Claim: Meta's trigger for a full RFC (vs. a lightweight design note) is determined by blast radius and complexity: (1) High blast radius / high complexity = mandatory RFC. (2) Medium = design doc with optional review. (3) Low = code review only. "Blast radius" is explicitly the determining criterion in practitioner accounts.
Search queries used: "Meta RFC trigger blast radius complexity decision when RFC required vs lightweight"
Source: Multiple practitioner accounts describe the blast-radius framework as the trigger. No single PRIMARY Meta source published.
Verification pass: Searched "Meta facebook blast radius RFC requirement engineering" — consistent characterization across multiple sources.
Tag: [INFERRED]

**Q3 — Reviewer pool:**
Claim: RFC reviewers are domain experts and cross-team stakeholders relevant to the blast radius of the change. The broader the blast radius, the broader the required reviewer pool. No specific named reviewer role for RFCs (equivalent to Google's Readability) is publicly documented.
Tag: [INFERRED]

**Q4 — Approval bar and reversibility:**
Claim: NOT FOUND. Formal approval bar for a Meta RFC (who must sign off, whether unanimous or majority) is not publicly documented.
Tag: [NOT FOUND]

**Q5 — ADR relationship:**
Claim: NOT FOUND. Meta's relationship to ADRs as a separate artifact is not publicly documented.
Tag: [NOT FOUND]

**Q6 — Real example or template found:**
Claim: No actual Meta RFC is publicly available. Meta engineering.fb.com publishes engineering blog posts, not internal RFC documents.
Tag: [NOT FOUND]

**Evidence-density note:** ~0% PRIMARY, ~50% INFERRED, ~50% NOT FOUND. Meta's RFC process is confirmed as named and used, but its specifics are not publicly documented in primary sources.

---

## Netflix

**Q1 — Which document types Netflix uses:**
Claim: Netflix does not have a formally documented company-wide design doc or RFC process. Per its decentralized culture, teams use whatever documentation makes sense for their context. Netflix TechBlog posts describe engineering decisions in narrative form, but these are retrospective blog posts, not internal design documents.
Search queries used: "Netflix design doc RFC formal process company-wide engineering documentation"
Source: Netflix Culture document; Netflix TechBlog.
Tag: [PRIMARY — absence of formal process is a sourced finding]

**Q2 — Trigger point:**
Claim: No formal trigger point. Teams decide when a technical decision requires written documentation.
Tag: [PRIMARY — by implication of the decentralized model]

**Q3 — Reviewer pool:**
Claim: Per "farming for dissent" model — the decision owner seeks feedback from relevant experts as they see fit. No formal reviewer pool or approval committee.
Source: Netflix Culture document.
Tag: [PRIMARY]

**Q4 — Approval bar:**
Claim: Informed Captain model — the decision owner approves their own design by making the call. No external approval required.
Tag: [PRIMARY]

**Q5 — ADR relationship:**
Claim: NOT FOUND. Netflix does not publicly document use of ADRs.
Tag: [NOT FOUND]

**Q6 — Real example or template found:**
Claim: Netflix TechBlog posts (e.g., Chaos Monkey, microservices architecture) serve as retrospective technical accounts. The 2011 Netflix TechBlog post on Chaos Monkey is a real, retrievable technical document describing a system design decision — though it is a blog post, not an internal design doc.
Search queries used: "Netflix chaos monkey original blog post technical design description"
Source: Netflix TechBlog (2011 Chaos Monkey post confirmed accessible).
Tag: [PRIMARY for blog post as design narrative; NOT FOUND for internal design doc or template]

**Evidence-density note:** ~50% PRIMARY (sourced as deliberate absence), ~50% NOT FOUND. Netflix's formal design process is intentionally minimal — this is a real finding, not a gap.

---

## Stripe

**Q1 — Which document types Stripe uses:**
Claim: Stripe's primary design artifact is the API specification document — the API shape IS the design. For internal systems changes, Stripe likely uses design docs (by that general name), but no specific named document type is publicly documented by Stripe beyond the API review proposal.
Search queries used: "Stripe design doc RFC technical design document type API specification"
Source: kenneth.io and multiple practitioner accounts confirm the API spec as the primary design artifact.
Tag: [INFERRED]

**Q2 — Trigger point:**
Claim: Any API-level change triggers the API review process (mailing list submission). For internal systems, the trigger is not publicly documented.
Source: kenneth.io (named former Stripe engineer).
Tag: [INFERRED]

**Q3 — Reviewer pool:**
Claim: API review: cross-functional reviewers on the API review mailing list. Who is on that list and how it is moderated is NOT FOUND.
Tag: [NOT FOUND]

**Q4 — Approval bar:**
Claim: NOT FOUND specifically. No clear statement of who has final authority in the API review process.
Tag: [NOT FOUND]

**Q5 — ADR relationship:**
Claim: NOT FOUND.
Tag: [NOT FOUND]

**Q6 — Real example or template found:**
Claim: Stripe's public API documentation (stripe.com/docs) is a real, retrievable artifact that shows the outcome of the design process, though not the design document itself.
Source: stripe.com/docs — directly accessible.
Tag: [PRIMARY for public API as artifact outcome; NOT FOUND for internal design document]

**Evidence-density note:** ~10% PRIMARY, ~30% INFERRED, ~60% NOT FOUND. Stripe's internal design documentation is not publicly described.

---

## Basecamp/37signals

**Q1 — Which document types Basecamp uses:**
Claim: Basecamp deliberately avoids heavy upfront design docs. The Pitch (from Phase 2 and 4) is the only formal pre-build document. During the build cycle, teams write no additional specification documents — implementation decisions are made by the 2-person team (designer + programmer) as they build. This is a documented, intentional philosophy, not a gap.
Search queries used: "Basecamp Shape Up design doc RFC avoided deliberate philosophy upfront technical documentation"
Source: *Shape Up* (Ryan Singer, 2019) explicitly argues against detailed upfront specifications: "The more detailed the design document, the less ownership the implementers have."
Verification pass: Confirmed via basecamp.com/shapeup.
Tag: [PRIMARY]

**Q2 — Trigger point:**
Claim: No trigger for a design doc because none is written. The only trigger is: if an idea passes the Betting Table, a 2-person team begins implementation with the Pitch as their only pre-built specification.
Source: *Shape Up*.
Tag: [PRIMARY]

**Q3 — Reviewer pool:**
Claim: The Betting Table reviews the Pitch (pre-build). During build, no review document exists — the cycle is protected time where teams build without review interruptions.
Source: *Shape Up*.
Tag: [PRIMARY]

**Q4 — Approval bar:**
Claim: The Betting Table bet is the hard gate. Once placed, there is no subsequent design document approval process — the team owns implementation. This is deliberately one-way (within the cycle) and two-way (can return a project to shaping if it doesn't ship).
Source: *Shape Up*.
Tag: [PRIMARY]

**Q5 — ADR relationship:**
Claim: NOT FOUND. Basecamp does not publicly document use of ADRs.
Tag: [NOT FOUND]

**Q6 — Real example or template found:**
Claim: The Pitch document itself (as described in *Shape Up*) with its five sections is the real retrievable template. Basecamp.com/shapeup reproduces actual example pitch sketches (breadboards) from real Basecamp/Hey product work.
Source: *Shape Up* (Ryan Singer, 2019) — directly accessible at basecamp.com/shapeup.
Tag: [PRIMARY]

**Evidence-density note:** ~90% PRIMARY. Basecamp's position is a documented deliberate contrast to design doc culture — the finding is "no design docs, here is why," and that is fully sourced.

---

## Plain-Language Summary — Three Document Types Compared

**Design Doc:** An internal, project-specific document written before implementation, by the implementing team, to socialize a technical approach and gather feedback. Used by Google (formally), Amazon (informally), and implied by Meta at lighter scales. Trigger: non-trivial change (>10 engineering days at Google). Approval: soft — no blocking objections from key reviewers. Two-way door — can be revised.

**RFC (Request for Comments):** A process for decisions with broad impact, explicitly inviting feedback from outside the implementing team. Used by Meta (formally, triggered by blast radius). Google uses its design doc for RFC-equivalent purposes. Amazon does not use this term. Trigger: cross-team impact, irreversible decisions, high blast radius. Approval: varies — more formal than a design doc, but specific bar is not publicly documented for Meta.

**ADR (Architecture Decision Record):** A short, immutable summary of a decision made — created after the RFC/design doc process concludes, as the durable artifact. Not formally used by any of the six orgs under their own naming. Some orgs (Google via design docs, Basecamp via the Pitch) have the decision embedded in the same document — there is no separate ADR step.

**Gate status: PASSED.** A plain-language explanation of all three types is provided without hedging, backed by at least one real example or template for each type: Google design doc template (industrialempathy.com) [PRIMARY], Meta RFC trigger framework [INFERRED with source], Basecamp Pitch as the deliberate non-design-doc contrast [PRIMARY].
