# §24e — Privacy & Legal Trust: Research Notes

> Scope: data minimisation, retention, consent, disclosures, deletion, access requests, third-party sharing, applicable legal obligations (GDPR, CCPA/CPRA as amended, others — verified current as of 2026-10-10). NOT LEGAL ADVICE — research notes only; verify against statute text and counsel. Read-only research. Metadata: `07-evidence-register.md`.

## 0. Standing caveat (applies to this whole file)

A privacy-policy page is **not** a substitute for compliance. Posting a policy does not satisfy consent, minimisation, retention, rights-fulfilment, or security obligations — it is one disclosure artifact among many operational duties. **Corroborated** (FTC Act §5 "unfair or deceptive" enforcement tradition; every regime below requires operational processes behind the notice).

## 1. GDPR (EU) — still in force; security and rights duties

- **Verified stable**: GDPR in force since 25 May 2018; applies to processing of EU residents' personal data regardless of where the business sits (extraterritorial scope). Core duties relevant to product engineering:
  - **Art. 5** principles: lawfulness/fairness/transparency, purpose limitation, **data minimisation**, accuracy, storage limitation (retention), integrity/confidentiality, accountability.
  - **Art. 32** security of processing: appropriate technical/organisational measures (pseudonymisation, encryption, resilience, regular testing).
  - **Art. 33/34** breach notification: supervisory authority **within 72 hours** of awareness; communication to data subjects when high risk.
  - **Chapter III** data-subject rights: access (Art. 15), rectification (16), erasure (17), restriction (18), portability (20), objection (21).
  - **Art. 35** DPIAs for high-risk processing; **Art. 28** processor contracts.
- Fines up to €20M or 4% of global annual turnover (higher tier). **Verified** (long-standing statutory text; these are stable provisions).
- **Unknown**: I did not survey 2026 GDPR amendment activity or EDPB guidance changes for this pass — treat specifics (e.g., any 2025–2026 EDPB opinions on AI training data) as unverified; the core duties above are stable law.

## 2. CCPA / CPRA (California) — as amended through 2026

**Corroborated** (Osano, Lexology, JD Supra, WSGR — all reporting Sept/Oct 2026):
- Baseline (CCPA as amended by CPRA, operative 2023): rights to know, delete, correct, opt out of sale/sharing, limit use of sensitive PI; applies to for-profit businesses doing business in California meeting thresholds (revenue > ~$26.6M inflation-adjusted for 2025–26, or 100,000+ CA consumers/households' data bought/sold/shared, or 50%+ revenue from selling/sharing PI — **corroborated** via 2026 compliance summaries).
- **SB 923 (Expanding Privacy Rights Act), signed 27 Sept 2026, effective 1 Jan 2027** — two changes:
  1. Deletion right expands from PI collected **"from"** the consumer to PI collected **"from or about"** the consumer — third-party-sourced/enriched/broker data must now be deleted too (closes the "we didn't collect it from you" loophole; matches DE/IN/MD/NJ standard). Businesses may keep a suppression record (minimum data to keep it deleted).
  2. Online-only businesses with a direct consumer relationship must offer an **online request method** (webform/portal) for know/delete/correct requests, not just an email address.
- Operational impact: deletion workflows must inventory third-party-sourced data (CRM, marketing platforms, enrichment vendors) — "do we know everywhere that information came from?"
- **2026 enforcement climate**: coordinated state-AG sweeps active; Global Privacy Control / universal opt-out signals effectively mandatory across a large bloc of states as of Jan 2026 (CA, CO, CT, DE, MD, MN, MT, NE, NH, NJ, OR, TX per advertiser-focused 2026 analysis — **corroborated-as-attributed**, single analysis).
- **SB 690 (2026)**: limits CIPA pen-register claims for website/app tracking (narrows one private-action path; CCPA rights unaffected). **Corroborated** (allaboutcookies, JD Supra).
- **California children's/age-appropriate design law** (2026 session, effective 1 Jan 2027): high-default privacy for child users, data-minimisation to what is necessary for the service the child is actively using, no dark patterns, no default profiling/geolocation; penalties up to $5,000/$15,000 per violation per child. **Corroborated** (WSGR Oct 2026).

## 3. US state patchwork (2026)

- **~20 states** with comprehensive privacy laws in effect as of 2026 (IN, KY, RI newly effective 1 Jan 2026); **23–24 enacted total** counting laws taking effect 2027–2028 (OK and LA 1 Jan 2027; AL 1 May 2027; VT 1 Jan 2028). Florida's Digital Bill of Rights is narrower (>$1B revenue + second condition). **Corroborated** (privacylawmap May 2026; IAPP-derived trackers; secureprivacy Aug 2026). Trackers differ on counting methodology — use 20-in-effect / 24-enacted as the working figure, methodology-dependent.
- **No federal comprehensive privacy law**; the American Privacy Rights Act (APRA) expired without a full vote and has not been reintroduced. Sectoral federal laws apply by data type: HIPAA (health), COPPA (under-13), GLBA (financial), FERPA (education), FTC Act §5 (unfair/deceptive — applies regardless of size). **Corroborated**.
- Common consumer rights across states: know/access, delete, correct, portability, opt out of sale/targeted advertising; most use 45-day response windows (check statute-specific). **Corroborated**.
- Sensitive data (precise geolocation, health inferences, neural data in OR/CT) increasingly requires **opt-in** consent, not opt-out. **Corroborated** (secureprivacy 2026).
- Practical baseline for a US-facing consumer product: CCPA/CPRA as the strictest commonly-applicable regime + sectoral law if touching health/kids/finance. (Practitioner recommendation, **Proposed** as research posture, not law.)

## 4. India — DPDP Act 2023 + DPDP Rules 2025

**Corroborated** (ConsentOS timeline, dev.to security-researcher explainer, indian-law-plugin rules, LawStreet, siriusstar — all 2026):
- DPDP Rules notified **13 Nov 2025**; phased commencement: Data Protection Board + definitions immediate; **Consent Manager registration mandatory from 13 Nov 2026**; core Data Fiduciary obligations, Data Principal rights, and penalty provisions enforceable **13 May 2027** (G.S.R. 843(E)).
- Security duties (Rule 6): encryption/obfuscation/masking/tokenisation, access controls, logging + monitoring, **≥1-year log retention**, backups/continuity, processor contracts requiring safeguards. Penalties up to **₹250 crore** for failure to take reasonable security safeguards; up to ₹200 crore for breach-notification failures and children's-data violations.
- Breach notification: inform affected individuals + the Board **without delay**; detailed report to the Board **within 72 hours**. Separately, CERT-In directions require cyber-incident reporting **within 6 hours** (already live, independent of DPDP).
- Consent: plain-language itemised notice; withdrawal as easy as giving; verifiable parental consent for children's data, no tracking of children.
- Retention: delete once purpose is served; large platform categories face scheduled retention rules.

## 5. EU AI Act / NIS2 / CRA — security-relevant obligations (summary; detail in 04)

- **EU AI Act** in force 1 Aug 2024; high-risk AI obligations: Art. 15 cybersecurity/robustness (provider duty, discharged via Art. 9 risk management); Digital Omnibus (7 May 2026) moved deadlines to 2 Dec 2027 / 2 Aug 2028; AI-generated-content transparency duties from 2 Dec 2026. **Corroborated**.
- **NIS2**: in-scope entities must include AI systems in risk management, vulnerability management, incident response. **Corroborated**.
- **EU Cyber Resilience Act (CRA)**: products with digital elements incl. most AI agents in scope; vulnerability reporting duties from Sept 2026; full conformity Dec 2027; CRA compliance deemed to satisfy AI Act Art. 15 for high-risk systems. **Corroborated** (Mishcon 2026).

## 6. Operational privacy controls (the engineering checklist)

| Control | Why (regime-agnostic) |
|---|---|
| **Data minimisation** | Collect only what the purpose needs (GDPR Art. 5(1)(c); CA children's law; DPDP purpose limitation). Review telemetry/analytics payloads, logs, and third-party SDK data flows. |
| **Retention schedules + deletion** | Storage limitation (GDPR), purpose-served deletion (DPDP), expanded CCPA deletion "from or about" (SB 923, eff. 2027). Scheduled purges; suppression lists where allowed. |
| **Consent where required** | Opt-in for sensitive data (growing US consensus), children's data (DPDP, CA 2027 law, COPPA), marketing comms (ePrivacy/TCPA-adjacent — **Unknown** detail here). Consent must be withdrawable as easily as given. |
| **Disclosures** | Privacy notice describing categories, purposes, sharing, rights, retention — accurate and current (FTC §5 deceptive-practice risk if it lies). |
| **Deletion / access request workflows** | Intake (webform required for CA online-only from 2027), identity verification proportionate to risk, 45-day-ish response clocks, coverage of third-party-sourced data, vendor pass-through. |
| **Third-party sharing inventory** | Pixels/SDKs = "sharing"/"sale" under state laws (Meta/TikTok/LinkedIn pixels trigger opt-out duties); DPDP/CPRA processor contracts; data-mapping the minimum viable compliance artifact. |
| **Breach readiness** | 72-hour clocks (GDPR, DPDP Board), 6-hour CERT-In (India), state AG breach-notification statutes (US — **Unknown** detail per state here); logging that can answer "whose data, what data, when." |

## 7. Classification pointers (full table in 06)
- Breach notification within statutory windows; honoring deletion/access requests; children's-data safeguards where applicable; processor contracts → **legal/contractual obligations** (in the specified contexts).
- Minimisation, retention schedules, sharing inventory, consent UX → **critical technical safeguards / strong recommended practice** depending on regime applicability.
- A posted privacy policy alone → explicitly **not** a control (anti-pattern to list it as one).
