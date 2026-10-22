# Phase 1 — Ground Rules, Definitions, and Org Shortlist Lock-In — Findings

**Status:** Complete  
**Date started:** 2026-08-28  
**Date completed:** 2026-08-28  

---

## Locked Glossary

**Artifact:** A document or tangible output produced at a specific lifecycle stage, with a defined owner and at least one designated reviewer. An artifact is distinguished from general notes by having a named author, a defined purpose, and a condition under which it is considered complete or reviewed. Examples: PR/FAQ, design doc, RFC, postmortem report.

**Gate:** A condition that must be explicitly and verifiably true before work is allowed to proceed to the next lifecycle stage. A gate is not a checkpoint that can be quietly waved through — it requires specific, checkable criteria to be satisfied. Examples: "design doc approved by at least two reviewers," "launch review checklist all-green."

**Decision owner:** The single named person or role whose call it ultimately is when a decision must be made. They may consult widely, but the decision is theirs. Distinct from reviewers. If no single owner can be named, the decision-ownership structure is unclear — itself a finding worth recording.

**Reviewer:** Someone whose feedback is solicited or required before a decision is finalized, but who is not the decision owner. Reviewers may have formal sign-off rights. Distinction from decision owner matters: a reviewer who can actually block (veto) is functionally more than a reviewer.

**Veto authority:** The ability of a named role to block a decision outright — independently of the decision owner's preference — without needing to override or escalate. Not the same as having strong opinions or being a senior reviewer. Example: Amazon's Bar Raiser role holds veto authority over hiring decisions regardless of the hiring team's preference.

**Reversible ("two-way door") decision:** A decision that can be undone at acceptable cost if it turns out to be wrong. Reversibility is relative to organizational scale and context — the same technical decision may be reversible for a solo developer and irreversible for a 10,000-person company. What makes a decision reversible is not that it is small, but that the cost of undoing it is acceptable.

**Irreversible ("one-way door") decision:** A decision that cannot be cheaply undone once made — due to technical debt, external commitments, contractual lock-in, customer expectations, or architecture constraints baked into downstream systems. The distinction from reversible decisions matters for who is allowed to make the call and how much deliberation is warranted.

**DRI (Directly Responsible Individual):** The single named person accountable for a specific outcome, regardless of how many others contribute to it. The DRI is answerable for the outcome, not just the process. Borrowed from Apple attribution (used in Amazon and other orgs without the Apple label). A project without a DRI has no named accountable person — itself a finding worth recording.

**Escalation:** The defined path by which a decision or disagreement that cannot be resolved at the current level is passed to a higher authority or different process for resolution. A well-functioning escalation path is explicit, not improvised case-by-case. An escalation path that is unclear or relies on informal relationships is itself a structural weakness.

**Non-goal:** Something explicitly and deliberately excluded from the scope of a project or document — stated in writing so that it cannot be quietly re-included later without re-opening the decision. Distinct from "things not yet decided" (which are undecided, not ruled out) and from "things nobody thought to mention" (which are gaps, not non-goals). A genuine non-goal is something someone actively wanted, considered, and ruled out.

**Alternatives considered:** A documented account of options that were actively evaluated and rejected, with the rejection rationale stated. Prevents relitigating decisions whose reasoning is no longer visible. An "alternatives considered" section that lists only obviously bad alternatives is not genuinely useful — it must include real options that were seriously weighed.

**Progressive rollout:** Releasing a change to a subset of users, traffic, or infrastructure before full release. The subset can be defined by percentage, user cohort, geography, time window, or a metric gate (e.g., "expand only if error rate stays below X%"). The defining feature is that full release is not the first release — controlled exposure precedes it.

**Blameless postmortem:** An incident review structured to find systemic causes — process gaps, architectural weaknesses, tooling failures — rather than assign individual fault. "Blameless" does not mean consequences-free; it means the review process focuses on the system, not on punishing the person who happened to be at the keyboard. A postmortem that is labeled blameless but still focuses on individual error is not blameless in practice.

**Adversarial review:** A review performed by a party — human or AI — that has no stake in the original decision being correct, and that is explicitly structured so it can and should find real flaws rather than simply confirm the original reasoning. The key distinction from a standard review: the adversarial reviewer is trying to find what is wrong, not what is right. An adversarial review that consistently finds nothing is either evidence of unusually high quality or evidence that the review is not actually adversarial.

---

## Confirmed Org Shortlist

### Confirmation Method
For each org, at least one search was run to verify the existence of a real, publicly accessible, *technical* trail — engineering blog posts, conference talks, books written by practitioners, or public methodology documents. The standard used: would this trail yield PRIMARY-tagged claims by the tagging rules in the Master Framework? Marketing pages and brand reputation were explicitly excluded from the confirmation criterion.

---

**1. Amazon**  
Trail confirmed via: *Working Backwards* (Bryar & Carr, 2021) — a book written by two former Amazon SVPs specifically about the PR/FAQ, six-pager, and bar raiser mechanisms as process tools, not brand narrative. Also confirmed via multiple published former-employee accounts of the PR/FAQ format and the "silent reading" meeting structure. The technical trail here is among the richest of the six orgs.  
Search queries used: "Amazon working backwards PR/FAQ six-pager engineering blog technical account"  
Verification pass: Cross-referenced with search for "amazon bar raiser mechanism" — independently confirmed from multiple former-employee sources. Confirmed.  
Tag: [PRIMARY] — trail exists and is technically specific.

**2. Google**  
Trail confirmed via: Google's SRE book series (sre.google/books) — published by Google with named Google SRE practitioners, freely available online. Also confirmed via industrialempathy.com, a published piece by a named ex-Google engineer describing Google's design doc culture with specific structural details. Google also maintains a publicly accessible SRE resources page (sre.google).  
Search queries used: "Google SRE book design doc template engineering blog technical process"  
Verification pass: Searched specifically for "Google readability review" — multiple independent practitioner accounts found. Confirmed.  
Tag: [PRIMARY] — trail exists and is technically specific.

**3. Meta**  
Trail confirmed via: engineering.fb.com (Meta's own engineering blog), which publishes specific technical accounts of internal systems. RFC process, Gatekeeper (feature flagging), and Bootcamp are all documented in multiple engineering.fb.com posts and independently in practitioner accounts.  
Search queries used: "Meta engineering RFC process bootcamp Gatekeeper feature flags engineering blog"  
Verification pass: Searched specifically for "engineering.fb.com Gatekeeper feature flags" — confirmed as a named, documented internal system described in technical terms. Confirmed.  
Tag: [PRIMARY] — trail exists and is technically specific.

**4. Netflix**  
Trail confirmed via: netflixtechblog.com (Netflix's engineering blog, actively maintained), which has published original technical accounts of Chaos Monkey (with specific implementation details), blameless postmortem culture, and the Freedom & Responsibility philosophy. The Netflix culture doc is also publicly available. Both sources are written by Netflix engineers, not external commentators.  
Search queries used: "Netflix freedom and responsibility chaos monkey blameless postmortem engineering blog technical"  
Verification pass: Searched for "Netflix chaos monkey original blog post" — the original 2011 Netflix TechBlog post on Chaos Monkey was found and is still accessible. Confirmed.  
Tag: [PRIMARY] — trail exists and is technically specific.

**5. Stripe**  
Trail confirmed via: stripe.com/blog/engineering (Stripe's engineering blog), stripe.dev, and multiple named practitioner accounts of Stripe's API review process and documentation-as-product philosophy. The Markdoc open-source project is a concrete, verifiable artifact of Stripe's documentation tooling philosophy. Stripe engineers have published extensively on API design discipline.  
Search queries used: "Stripe engineering blog API design documentation process technical writing"  
Verification pass: Searched specifically for "Stripe API review process engineer blog" — found kenneth.io post by a named former Stripe engineer with specific process details. Confirmed.  
Tag: [PRIMARY] — trail exists and is technically specific.

**6. Basecamp/37signals — SELECTED over Linear**

**Comparison:**

| Dimension | Basecamp/37signals | Linear |
|---|---|---|
| Primary source | *Shape Up* (Ryan Singer, 2019) — full-length methodology book, publicly free at basecamp.com/shapeup, 19 chapters covering the entire product development lifecycle | linear.app/method — a web page with ~12 principles, no chapter-length treatment of any single topic |
| Author credentials | Ryan Singer: Head of Product Strategy at Basecamp for 15+ years, wrote the book as a practitioner account of 15 years of refinement | linear.app/method: no named individual author, presented as company philosophy |
| Depth | ~130 pages covering shaping, betting, building, circuit breakers, scope management, and hill charts as specific named mechanisms | Brief descriptions of principles like "Cycles not sprints," "Scope small" — useful but not mechanism-level |
| Technical specificity | Describes specific artifacts (pitch document, appetite, breadboard, fat marker sketch) with enough detail to be directly replicable | Describes orientations and values rather than specific artifacts or gate conditions |
| Verification trail | Confirmed by accessing basecamp.com/shapeup directly — full text present and readable | Confirmed by accessing linear.app/method — page loads but is largely JavaScript-rendered, readable content is principle-level only |
| Relevance to solo operator | Directly addresses how a small team (typically 2 people: one designer, one programmer) ships work in 6-week cycles | Addresses small-team velocity but without the same mechanism-level specificity |

**Decision:** Basecamp/37signals wins on depth, mechanism-level specificity, and author credibility. The *Shape Up* book is the strongest single source of the lean-team category — and its specific mechanisms (appetite, betting table, circuit breaker) are precisely the kind of named, replicable things this research needs to analyze.

Search queries used:  
- "Basecamp Shape Up methodology book public writing process" → confirmed full book publicly available at basecamp.com/shapeup  
- "linear.app Linear Method engineering process public blog writing depth" → confirmed linear.app/method exists but is principle-level, not mechanism-level  
Verification pass: Directly fetched basecamp.com/shapeup and linear.app/method. Shape Up: 1,215 total lines of accessible content, full chapters with named mechanisms. Linear Method: largely JavaScript-rendered, principle-level content only. Confirmed.  
Tag: [PRIMARY] — direct source retrieval, not inferred.

---

## AI System Shape — Explicitly Undecided

Confirmed: No assumption has been made about whether the eventual system uses one agent, several, skills-only, workflows, or a hybrid. This is recorded here explicitly and will not be assumed anywhere in Phases 1–12. The shape will be decided in Phase 13 from evidence gathered in Phases 2–12.

This statement applies from this point forward without needing to be restated in every subsequent phase.

---

## Phase Gate

**Gate condition:** Glossary is locked with a one-paragraph working definition for every required term. Org shortlist is confirmed with a real technical trail verified for each org, not just brand reputation. The lean-team slot is decided with explicit reasoning stated. The AI system shape is explicitly undecided and recorded.

**Gate status:** PASSED. All four conditions are met.
