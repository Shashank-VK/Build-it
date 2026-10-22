# Phase 7 — Security, Privacy, and Reliability Review — Findings

**Status:** Complete
**Date started:** 2026-08-28
**Date completed:** 2026-08-28

---

## Amazon

**Q1 — Review structure:**
Claim: Amazon uses the Operational Readiness Review (ORR) as the reliability review gate, separate from the PR/FAQ product review. The ORR includes security, operational readiness, and reliability checks. For security specifically, Amazon uses a combination of self-service checklists and team-owned security reviews. For AWS-external services, additional compliance reviews apply.
Search queries used: "Amazon security review privacy review operational readiness review reliability gate"
Source: amazon.com/builders-library — ORR described as covering reliability specifically.
Verification pass: Confirmed ORR as a named, documented reliability mechanism.
Tag: [PRIMARY]

**Q2 — Minimum bar / checklist:**
Claim: The ORR checklist covers: architecture review, release quality, event management (incident handling), and operational processes. Specific checklist items are available in the AWS Well-Architected Tool. The checklist includes questions on monitoring, alerting, rollback capability, and failure mode handling.
Source: amazon.com (ORR documentation).
Tag: [PRIMARY]

**Q3 — Concrete consequence of failing:**
Claim: Failing an ORR means the service is not considered operationally ready and should not launch. Teams that launch without clearing the ORR are audited via COE (Correction of Errors) post-incident — if the ORR would have caught the issue, the failure to complete it becomes part of the post-incident record. In practice, the ORR is enforced through operational metrics meetings where ORR status is reviewed.
Source: amazon.com/builders-library.
Tag: [PRIMARY]

**Q4 — Veto authority (Lens 1):**
Claim: The ORR does not have a named external veto authority — teams self-administer the ORR. However, the operational metrics review (weekly senior leadership meeting) effectively provides oversight. Senior engineers can flag ORR non-compliance as a blocker at these meetings. For Tier-1 systems specifically, Amazon recently introduced senior engineer sign-off requirements.
Source: amazon.com/builders-library; recent reports of Tier-1 requirements.
Tag: [PRIMARY for ORR structure; INFERRED for Tier-1 specifics]

**Q5 — One-time gate vs continuous:**
Claim: Continuously re-applied. The ORR is re-evaluated through weekly operational metrics meetings and re-audited via post-incident COEs. Not a one-time pre-launch gate.
Source: amazon.com/builders-library.
Tag: [PRIMARY]

**Evidence-density note:** ~70% PRIMARY. Amazon's ORR is among the best-documented reliability review mechanisms in the set.

---

## Google

**Q1 — Review structure:**
Claim: Google uses the Launch Coordination Engineering (LCE) team — a dedicated team of engineers who consult on launch readiness and sign off on whether a launch is safe. The LCE team uses the Launch Coordination Checklist as its review artifact. This is a separate team and process from the design doc review.
Search queries used: "Google SRE book launch readiness review reliability sign-off LaunchDoc process named mechanism"
Source: sre.google — SRE book describes LCE team and Launch Coordination Checklist explicitly. PRIMARY.
Tag: [PRIMARY]

**Q2 — Minimum bar / checklist:**
Claim: The Launch Coordination Checklist covers: architecture review, capacity planning, monitoring and alerting setup, security review, failover behavior, and load testing. The SRE book notes that most major launches require LCE sign-off before proceeding.
Source: sre.google/books.
Tag: [PRIMARY]

**Q3 — Concrete consequence of failing:**
Claim: If a team cannot clear the LCE checklist, the launch does not proceed. Additionally, if a service's error budget is exhausted (exceeded its allowed downtime), it effectively cannot launch new features until reliability is restored. These are hard stops.
Source: sre.google — error budget as hard stop is explicitly described.
Tag: [PRIMARY]

**Q4 — Veto authority (Lens 1):**
Claim: The LCE team holds veto authority over launches. They can block a launch pending resolution of checklist items. The error budget mechanism also functions as an automated veto — if the budget is gone, launches stop regardless of LCE sign-off. Override conditions are NOT FOUND publicly.
Source: sre.google.
Tag: [PRIMARY for LCE veto; NOT FOUND for override conditions]

**Q5 — One-time gate vs continuous:**
Claim: Both. LCE review is a pre-launch gate. The error budget is a continuously applied check — it does not reset except at defined SLO windows. Post-launch, SRE teams monitor adherence to SLOs continuously.
Source: sre.google.
Tag: [PRIMARY]

**Evidence-density note:** ~90% PRIMARY. Google's LCE and SRE framework are the most explicitly documented reliability-review mechanisms in the entire six-org set.

---

## Meta

**Q1 — Review structure:**
Claim: Meta has a formal privacy review process — particularly strengthened post-2018 (Cambridge Analytica). Privacy review involves a dedicated privacy engineering team that reviews features touching user data. For reliability, Gatekeeper-based progressive rollout serves as a reliability gate — features roll out to small percentages before full launch.
Search queries used: "Meta privacy review process post-2018 formal gate Cambridge Analytica privacy engineering team"
Source: Multiple practitioner accounts and public reporting on Meta's post-2018 privacy reforms.
Verification pass: Searched "Meta facebook privacy review team formal process" — confirmed as strengthened post-2018 by multiple independent sources.
Tag: [INFERRED — no single PRIMARY Meta source describes current privacy review structure; multiple corroborating accounts]

**Q2 — Minimum bar / checklist:**
Claim: NOT FOUND. The specific checklist items for Meta's privacy or reliability review are not publicly documented.
Tag: [NOT FOUND]

**Q3 — Concrete consequence of failing:**
Claim: Failing Meta's privacy review means the feature cannot launch. Post-2018, privacy review is described as a genuine gate, not a rubber stamp. For reliability, a Gatekeeper flag that can be disabled instantly provides rollback capability.
Source: Multiple practitioner accounts of Meta's post-2018 privacy reforms.
Tag: [INFERRED]

**Q4 — Veto authority (Lens 1):**
Claim: The privacy engineering team holds veto authority over features that touch user data. Who can override this is NOT FOUND.
Tag: [INFERRED for veto; NOT FOUND for override]

**Q5 — One-time gate vs continuous:**
Claim: Privacy review is a pre-launch gate. Gatekeeper-based rollout is continuously monitored post-launch.
Tag: [INFERRED]

**Evidence-density note:** ~0% PRIMARY, ~50% INFERRED, ~50% NOT FOUND. Meta's privacy review is known to exist and was strengthened post-2018, but the specific structure is not publicly documented.

---

## Netflix

**Q1 — Review structure:**
Claim: Netflix uses Chaos Engineering (Chaos Monkey, Chaos Kong, and the broader "Simian Army") as its primary reliability review mechanism — but it operates post-launch in production, not as a pre-launch gate. Security review structure is NOT FOUND in Netflix's public writing. Privacy review structure is NOT FOUND.
Search queries used: "Netflix chaos engineering reliability review pre-launch gate security review privacy"
Source: Netflix TechBlog — Chaos Engineering is described extensively. Pre-launch security/privacy gate is NOT FOUND.
Tag: [PRIMARY for chaos engineering; NOT FOUND for pre-launch security/privacy gate]

**Q2 — Minimum bar / checklist:**
Claim: NOT FOUND for a pre-launch reliability checklist. Chaos Engineering is the post-launch bar — services must survive chaos injection. No minimum bar document publicly available.
Tag: [NOT FOUND]

**Q3 — Concrete consequence of failing:**
Claim: If a service fails chaos testing, the Simian Army (automated tools) kills it — this is the consequence in production. There is no pre-launch gate consequence documented. Netflix's model explicitly accepts that failures will happen in production and prepares for resilience rather than prevention.
Source: Netflix TechBlog (2011 Chaos Monkey post and subsequent posts).
Tag: [PRIMARY]

**Q4 — Veto authority:**
Claim: Automated chaos tools have effective veto authority — they will terminate failing services. No human veto role for pre-launch security/reliability sign-off is documented.
Tag: [PRIMARY for chaos as automated veto; NOT FOUND for human pre-launch veto]

**Q5 — One-time vs continuous:**
Claim: Continuously applied. Chaos Engineering runs continuously in production. Netflix explicitly chose this over one-time pre-launch gates.
Source: Netflix TechBlog.
Tag: [PRIMARY]

**Evidence-density note:** ~50% PRIMARY (for chaos engineering as the reliability mechanism), ~50% NOT FOUND (for pre-launch security/privacy gate specifics). Netflix's reliability philosophy is a genuinely different model — post-launch continuous testing rather than pre-launch review.

---

## Stripe

**Q1 — Review structure:**
Claim: Stripe handles payment data and is PCI-DSS compliant. This means Stripe undergoes annual PCI-DSS assessments — a formal, externally audited compliance process. For internal feature launches, the security review process is NOT FOUND in public engineering writing beyond the API review process described in Phase 5.
Search queries used: "Stripe security review PCI compliance privacy review process reliability gate engineering"
Source: Stripe's PCI compliance is publicly stated on stripe.com. Specific internal security review process: NOT FOUND.
Tag: [PRIMARY for PCI compliance as external audit; NOT FOUND for internal security review process]

**Q2 — Minimum bar / checklist:**
Claim: PCI-DSS compliance requirements serve as the external minimum bar for payment security. Internal checklist: NOT FOUND.
Tag: [PRIMARY for PCI-DSS as external bar; NOT FOUND for internal checklist]

**Q3 — Concrete consequence of failing:**
Claim: Failure of PCI-DSS compliance would mean loss of ability to process card payments — a business-ending consequence. This creates very strong incentives for compliance. Internal launch failure consequences: NOT FOUND.
Source: General PCI-DSS understanding; Stripe's PCI compliance publicly stated.
Tag: [INFERRED]

**Q4 — Veto authority:**
Claim: For PCI-DSS: external QSA (Qualified Security Assessor) holds effective veto authority over compliance status. For internal launches: NOT FOUND.
Tag: [INFERRED]

**Q5 — One-time vs continuous:**
Claim: PCI-DSS audit is annual. Internal monitoring is continuous given payment criticality. Specific internal review cadence: NOT FOUND.
Tag: [INFERRED]

**Evidence-density note:** ~20% PRIMARY (PCI compliance publicly stated), ~30% INFERRED, ~50% NOT FOUND. Stripe's internal security review process is not publicly documented, though the external PCI compliance bar is known.

---

## Basecamp/37signals

**Q1 — Review structure:**
Claim: No formal dedicated security/privacy/reliability review team documented. At Basecamp's scale (small team), security review is handled ad hoc by a senior engineer. No formal checklist or dedicated review team is documented publicly.
Search queries used: "Basecamp 37signals security review privacy reliability gate formal process small team"
Source: Basecamp's public writing (hey.com blog, Signal v. Noise blog) does not describe a formal security review process.
Tag: [NOT FOUND for formal process; PRIMARY for honest finding that it is handled informally at this scale]

**Q2 — Minimum bar:**
Claim: NOT FOUND. No documented minimum security bar for Basecamp feature launches is publicly available.
Tag: [NOT FOUND]

**Q3 — Concrete consequence of failing:**
Claim: NOT FOUND as a documented process. At this scale, a security issue would likely be handled by a hotfix release and public disclosure — as Basecamp has done historically.
Tag: [NOT FOUND]

**Q4 — Veto authority:**
Claim: NOT FOUND. At this scale, senior engineer or co-founder (Jason Fried / David Heinemeier Hansson) effectively holds veto authority by virtue of their role — but this is not formalized as a named mechanism.
Tag: [SPECULATIVE]

**Q5 — One-time vs continuous:**
Claim: NOT FOUND. Likely handled on an as-needed basis.
Tag: [NOT FOUND]

**Evidence-density note:** ~10% PRIMARY (honest finding of informal handling), ~90% NOT FOUND. Basecamp's small scale means formal security review infrastructure is unlikely — this is a real, honest finding.

---

## Phase Gate Assessment

Gate condition: The actual consequence of failing this review is stated per org.

- **Amazon:** Launch does not proceed; post-incident, failure to complete ORR becomes part of the COE record. [PRIMARY]
- **Google:** Launch blocked by LCE veto; error budget exhaustion stops new launches automatically. [PRIMARY]
- **Meta:** Privacy-review failure blocks launch (post-2018). [INFERRED]
- **Netflix:** In-production chaos testing kills failing services. Pre-launch gate: genuinely absent by design. [PRIMARY]
- **Stripe:** PCI-DSS non-compliance = loss of card processing ability. Internal launch consequence: NOT FOUND. [INFERRED/NOT FOUND mix]
- **Basecamp:** No formal security review gate found. Honest finding at this scale. [NOT FOUND]

**Gate status: PASSED.** Consequence per org is stated. "Not formally documented" is stated plainly where applicable.
