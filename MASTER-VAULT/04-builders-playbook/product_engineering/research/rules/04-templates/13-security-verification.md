# Template 13 — Security Verification

**Use when:** before any internet-facing deploy (ASVS L1 gate, R-22); for trust-boundary changes (threat model, R-09). **Enforces:** R-09, R-21, R-22, R-23. Structured on OWASP ASVS chapters.

## 1. Scope and target level

- Target: **ASVS L1** (minimum, pre-launch) / **L2** (sensitive data — the maturing target)
- In scope (URLs, APIs, components): _…_
- Out of scope with reason: _…_

## 2. Threat model (required for trust boundaries)

*Assets, actors, entry points, mitigations. Ten minutes for simple systems; more for auth/payments/agents.*

| Asset | Actors | Entry points | Mitigation |
|---|---|---|---|
| _e.g., user PII_ | _anon internet, authenticated user, insider_ | _signup API, admin panel_ | _…_ |

*Agent systems: list every tool/capability the agent holds and its permission (see template 09, §4).*

## 3. ASVS gap register (the release artefact)

*One row per applicable requirement. This register — not a feeling — is what "we take security seriously" means.*

| ASVS chapter | Requirement (ID) | Verdict (Pass / Fail / N-A) | Evidence (test, scan, review ref) | Owner | Close date |
|---|---|---|---|---|---|
| V1 Architecture & threat modeling | | | | | |
| V2 Authentication | | | | | |
| V3 Session management | | | | | |
| V4 Access control | | | | | |
| V5 Validation & encoding | | | | | |
| V6 Cryptography (stored) | | | | | |
| V7 Errors & logging | | | | | |
| V8 Data protection | | | | | |
| V9 Communications (TLS) | | | | | |
| V10 Malicious code / supply chain | | | | | |
| V11 Business logic / abuse cases | | | | | |
| V12 Files & resources | | | | | |
| V13 API & web services | | | | | |
| V14 Configuration & secrets | | | | | |

*(Chapter list follows ASVS 4.0.3; v5.0.0 reorganises into 17 chapters — use whichever version the team standardises on, and name it.)*

## 4. Automated verification results

- [ ] SAST run on this release: _tool, result_
- [ ] SCA / dependency scan: _tool, result_ — critical/high reachable findings: _none / listed with patch SLA_
- [ ] Secrets scan: _tool, result_
- [ ] DAST / smoke (if applicable): _…_

## 5. AI-generated code review

*For AI-assisted diffs touching auth, crypto, validation, access control, or agent tools: reviewer name, date, and explicit "independently verified" sign-off (R-13).*

> _Fill in._

## 6. Disclosure readiness

- [ ] `SECURITY.md` published with contact and response SLA
- [ ] `security.txt` present at `/.well-known/security.txt`
- [ ] Coordinated-disclosure path tested (someone actually receives the report)

## Acceptance criteria

- [ ] Gap register complete — every applicable requirement has a verdict and evidence
- [ ] Zero Fail rows without an owner and close date; zero Fails on L1 for launch
- [ ] Threat model exists for every trust boundary in scope
- [ ] Patch SLA defined for new findings (critical reachable: days, not quarters)

## Anti-patterns this blocks

AP-08 (weak security) · AP-09 (AI-generated vulnerabilities) · AP-10 (uncontrolled agent permissions).
