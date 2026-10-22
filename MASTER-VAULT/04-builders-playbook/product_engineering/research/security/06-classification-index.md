# §25 — Classification Index: Every Recommendation, Classified

> Each recommendation from §§24a–24e classified as: **legal/contractual obligation** (in specified context) · **critical technical safeguard** · **risk-dependent control** · **strong recommended practice** · **optional enhancement** · **potentially harmful or inappropriate when misapplied**. For each: threat, required implementation, verification method, consequences of failure. Labels: Verified / Corroborated / Inferred / Proposed / Unknown. Evidence metadata: `07-evidence-register.md`.
>
> Classification is **contextual, not universal** — the class shown is for the stated context; the "context sensitivity" note says when it moves.

---

## A. Auth & Account (from 01)

### A1. Adaptive password hashing (Argon2id preferred; scrypt acceptable; bcrypt legacy-acceptable; PBKDF2 FIPS-only)
- **Class**: Critical technical safeguard
- **Threat**: Offline brute-force/dictionary attack after database compromise; fast or unsalted hashes fall in hours.
- **Implementation**: Server-side Argon2id (OWASP minimum m=19 MiB, t=2, p=1), unique salt per password; scrypt (N=2^17, r=8, p=1) if Argon2id unavailable; bcrypt (cost ≥10) only for existing deployments. Never MD5/SHA-1/plaintext. Never reversible encryption except rare interop edge cases.
- **Verification**: Code review of the hashing call path + config; test that DB stores opaque hashes, never plaintext; confirm client cannot influence algorithm choice.
- **Consequences of failure**: Full credential compromise at DB-read scale; credential-stuffing cascades across services.
- **Evidence**: Verified (OWASP Password Storage Cheat Sheet, current).

### A2. Throttling + progressive delays on login/reset (NO universal hard lockout)
- **Class**: Risk-dependent control (parameters depend on threat model); the *absence* of any throttling is a critical gap.
- **Threat**: Credential stuffing, password spraying, brute force.
- **Implementation**: Per-account + per-IP throttling, progressive delays, bot challenges/CAPTCHA after failures, step-up verification by risk. NIST 800-63B-4: cap consecutive failures at ≤100 per authenticator (upper bound, not target); lower limits allowed; rebind disabled authenticators. Notify via established channel if an authenticator is disabled; rate-limit the notification channel.
- **Verification**: Load-test login with sequential failures from one and multiple IPs; confirm delays trigger, legitimate user isn't hard-locked by an attacker, notifications fire.
- **Consequences of failure**: Account takeover at scale; or (if hard lockout) attacker-triggered denial of service against legitimate users.
- **Evidence**: Verified (NIST SP 800-63B-4, finalized 2025-07-31).

### A3. Universal hard account lockout after N failures
- **Class**: Potentially harmful or inappropriate when misapplied
- **Threat it claims to address**: brute force. **Threat it creates**: unauthenticated attacker can permanently lock any user out — a lockout button.
- **Implementation**: Do not deploy as a blanket policy. If used at all: only for narrow high-risk authenticators, with secure recovery and user notification.
- **Verification**: Confirm no unauthenticated-triggerable permanent lockout exists.
- **Evidence**: Corroborated (NIST text + community guidance).

### A4. Account-enumeration resistance (uniform responses)
- **Class**: Strong recommended practice → critical for high-value targets (risk-dependent)
- **Threat**: Username harvesting for targeted phishing, spraying, and reset-token attacks.
- **Implementation**: Identical messages/timing/status for existent vs non-existent accounts on login, registration, and reset; dummy-hash comparison on non-existent accounts to equalise timing; constant-time token comparison.
- **Verification**: Submit valid/invalid identifiers; diff responses byte-for-byte and timing distributions.
- **Consequences of failure**: Attacker builds a verified user list; enables targeted follow-on attacks.
- **Evidence**: Corroborated (OWASP Forgot Password; bug-bounty checklists).

### A5. Secure session cookies (Secure/HttpOnly/SameSite), rotation, server-side invalidation
- **Class**: Critical technical safeguard
- **Threat**: Session hijack via XSS (cookie theft), network sniffing, session fixation.
- **Implementation**: CSPRNG IDs (≥64-bit entropy, opaque); `Secure; HttpOnly; SameSite=Lax|Strict`; narrow Domain/Path; rotate ID at login/privilege change; idle + absolute timeouts enforced server-side; logout invalidates server-side; password/role change kills other sessions; reject server-unissued IDs.
- **Verification**: Inspect `Set-Cookie`; test fixation (pre/post-login ID must differ); replay session after logout (must fail); confirm timeouts server-side.
- **Consequences of failure**: Account takeover without credentials; sessions that outlive logout/password change.
- **Evidence**: Corroborated (OWASP Session Management Cheat Sheet).

### A6. Secure expiring reset tokens (CSPRNG, single-use, short TTL, hashed at rest)
- **Class**: Critical technical safeguard
- **Threat**: Account takeover via predictable or replayable reset tokens.
- **Implementation**: ≥128-bit entropy CSPRNG tokens; single-use; TTL in hours; store only the hash; identical responses regardless of account existence; invalidate sessions on password change.
- **Verification**: Request resets; inspect token entropy/length; attempt reuse after use and after expiry; check DB stores hash not token.
- **Consequences of failure**: Full account takeover (predictable tokens are a standard critical bug-bounty finding).
- **Evidence**: Corroborated (OWASP; WSTG; pentest documentation).

### A7. MFA where warranted; phishing-resistant (FIDO2/WebAuthn) preferred
- **Class**: Risk-dependent control → critical for admin/privileged/payment/high-value accounts
- **Threat**: Credential theft, phishing, SIM-swap, stuffing.
- **Implementation**: Offer MFA broadly; require for privileged roles; prefer phishing-resistant factors (FIDO2/passkeys) over SMS/voice OTP; step-up auth for sensitive actions (password change, payments, new device); audit fallback paths (email/SMS fallback can bypass primary-factor assurance).
- **Verification**: Attempt login with stolen password alone (must fail where MFA required); test fallback downgrade; confirm WebAuthn/FIDO2 option exists.
- **Consequences of failure**: Single-factor compromise = account compromise; SMS-OTP interception via SIM-swap.
- **Evidence**: Corroborated (NIST 800-63B-4 AAL model; WSTG fallback tests). SMS-OTP deprecation status: Inferred.

### A8. Security questions / knowledge-based recovery
- **Class**: Potentially harmful or inappropriate when misapplied
- **Threat it creates**: A weaker second credential, answerable via social engineering/public records; NIST 800-63B-4 forbids unauthenticated-accessible hints.
- **Implementation**: Do not use as a recovery factor. Use email/SMS-OTP-to-verified-channel, recovery codes (single-use, hashed), or manual verification.
- **Evidence**: Verified (NIST 800-63B-4 prohibition).

### A9. Forced periodic password rotation + character-class composition rules
- **Class**: Potentially harmful or inappropriate when misapplied
- **Why**: NIST 800-63B-4: SHALL NOT require periodic changes (rotate only on compromise evidence); SHALL NOT impose composition rules. Empirically produces weaker, predictable passwords (`Summer2024!` → `Summer2025!`). Prefer length (min 8, recommend ≥15, allow 64) + breach-corpus checking.
- **Evidence**: Verified (NIST SP 800-63B-4).

### A10. Security-event logging for auth (without secrets in logs)
- **Class**: Strong recommended practice → legal obligation where breach-detection duties apply
- **Threat**: Undetected stuffing, takeover, insider abuse; inability to scope incidents.
- **Implementation**: Log login success/failure, MFA events, resets, session anomalies; never log passwords/tokens/secrets; protect log integrity; monitor for stuffing patterns. Note ASVS 5.0 L1 has zero logging requirements — L1-only = blind to A09.
- **Verification**: Trigger events; confirm log entries exist and contain no secrets; confirm alerting on anomaly patterns.
- **Consequences of failure**: Breaches discovered by third parties; unscoped incident response; A09:2025 exposure.
- **Evidence**: Verified (ASVS 5.0 chapter analysis); Corroborated (community baselines).

---

## B. App & API (from 02)

### B1. Server-side input validation on every trust boundary
- **Class**: Critical technical safeguard
- **Threat**: Injection (A05:2025), business-logic abuse, parser differentials.
- **Implementation**: Type/length/range/format checks server-side for every input (REST, GraphQL, gRPC, webhooks, imports). Client-side validation is UX only.
- **Verification**: Send malformed/out-of-range payloads; confirm rejection server-side with client validation bypassed.
- **Consequences of failure**: SQLi, command injection, logic bypass.
- **Evidence**: Corroborated.

### B2. Parameterised queries; context-appropriate output encoding
- **Class**: Critical technical safeguard
- **Threat**: SQL injection; XSS and downstream injection via mis-encoded output.
- **Implementation**: Prepared statements everywhere; encode for the sink (HTML/JS/URL/SQL-parameter). Never interpolate user input into SQL/shell/template/LDAP.
- **Verification**: Code review + SAST; dynamic injection probes.
- **Consequences of failure**: Data exfiltration, auth bypass, RCE (second-order).
- **Evidence**: Corroborated.

### B3. Authorisation on every protected operation (authN + object-level authZ)
- **Class**: Critical technical safeguard
- **Threat**: BOLA/IDOR (API1), BFLA (API5) — the dominant API attack pattern.
- **Implementation**: Per-object ownership checks + per-function role checks on every endpoint; unauthenticated endpoints as explicit reviewed decisions; maintain API inventory (API9 shadow/zombie APIs).
- **Verification**: Cross-user object access tests (user A → user B's resource must deny); role-escalation probes on every route.
- **Consequences of failure**: Horizontal/vertical privilege escalation; mass data exposure.
- **Evidence**: Corroborated.

### B4. Mass-assignment prevention (explicit writable-field allowlists)
- **Class**: Critical technical safeguard
- **Threat**: BOPLA (API3) — attacker sets privileged fields (role, balance, isAdmin).
- **Implementation**: Schema allowlists (Zod/Pydantic); never bind request bodies directly to ORM models.
- **Verification**: Send extra fields (e.g., `{"role":"admin"}`); confirm ignored/rejected.
- **Consequences of failure**: Privilege escalation via crafted payloads.
- **Evidence**: Corroborated.

### B5. Request size/time limits; rate limits; anti-automation on sensitive flows
- **Class**: Strong recommended practice → critical for metered/expensive endpoints
- **Threat**: DoS, bill spikes / "denial of wallet" (API4), credential stuffing, flow abuse (API6).
- **Implementation**: Body-parser caps, timeouts, upload limits; per-user + per-IP rate limits (per-IP-only is bypassable — test distributed); quotas on signup/purchase/comment flows.
- **Verification**: Oversize/slow requests; burst tests from multiple sources; cost-meter checks on AI endpoints.
- **Evidence**: Corroborated.

### B6. CSRF defenses (where the auth model requires it)
- **Class**: Risk-dependent control
- **Threat**: Cross-site state-changing requests against cookie-authenticated sessions.
- **Implementation**: `SameSite=Lax` baseline + Origin checks + synchronizer/double-submit tokens for state changes — for cookie auth. Bearer-token APIs: CSRF n/a (XSS is the threat there).
- **Verification**: Cross-origin forged POST with victim session; confirm blocked.
- **Consequences of failure**: Attacker performs actions as the victim.
- **Misapplication note**: Demanding CSRF tokens on pure bearer-token APIs adds complexity without benefit.
- **Evidence**: Corroborated.

### B7. Security headers; HTTPS/TLS 1.2+; HSTS; narrow CORS
- **Class**: Strong recommended practice (headers/CORS); critical technical safeguard (HTTPS)
- **Threat**: MITM, XSS/clickjacking escalation, cross-origin data theft (A02/A04/API8).
- **Implementation**: HSTS, CSP, nosniff, Referrer-Policy, Permissions-Policy, frame-ancestors; TLS 1.2+; HTTP→HTTPS redirect; never disable TLS verification; CORS allowlist-only, no `*` + credentials.
- **Verification**: Header scan; testssl-style TLS check; CORS preflight from unlisted origin.
- **Evidence**: Corroborated.

### B8. Upload restrictions; path-traversal prevention
- **Class**: Critical technical safeguard (for upload/traversal-exposed apps); risk-dependent otherwise
- **Threat**: RCE via malicious upload; arbitrary file read/write via traversal.
- **Implementation**: Content-sniffed type validation, size limits, random names, storage outside web root, non-executable serving; canonicalize + jail paths, reject `..`/absolute/encoded sequences.
- **Verification**: Upload polyglots/double extensions; traversal payloads (`../`, encoded variants).
- **Consequences of failure**: Remote code execution; config/secret disclosure.
- **Evidence**: Corroborated.

### B9. Webhook signature verification; replay/idempotency protection
- **Class**: Strong recommended practice → critical for payment/state-changing webhooks
- **Threat**: Forged webhooks; replayed/duplicate requests causing double-charge/double-apply.
- **Implementation**: HMAC signature verification (constant-time compare), timestamp skew windows, per-endpoint secrets; idempotency keys on mutating endpoints.
- **Verification**: Replay a captured webhook after expiry; send unsigned payload; double-submit a payment.
- **Evidence**: Corroborated.

### B10. No sensitive data in errors; server-side price/payment validation; dependency scanning
- **Class**: Critical technical safeguard (payments/secrets); strong recommended practice (deps)
- **Threat**: Information disclosure via errors (A10:2025 now top-ten); price tampering; known-CVE exploitation (A03:2025 supply chain).
- **Implementation**: Generic client errors; full traces server-side only; recompute prices/totals server-side; verify gateway webhooks before fulfilment; CI dependency + secret scanning with fail-on-critical gates; SBOM.
- **Verification**: Trigger errors as outsider; tamper price client-side; audit CI gates.
- **Evidence**: Corroborated.

### B11. SSRF controls (allow-listed outbound fetches)
- **Class**: Critical technical safeguard where user-influenced server-side fetching exists
- **Threat**: Internal network/metadata-service access (A01:2025 / API7:2023).
- **Implementation**: Host/scheme allow-lists; block private/link-local/metadata IPs; HTTPS-only; no hand-rolled IP parsing; pin DNS check→use.
- **Verification**: Request fetch of `169.254.169.254`/internal hosts; confirm blocked.
- **Evidence**: Corroborated.

---

## C. Database & Secrets (from 03)

### C1. Privileged secrets out of client code; secrets manager / env store
- **Class**: Critical technical safeguard
- **Threat**: Any visitor extracts service-role keys → full data compromise (bypasses RLS entirely).
- **Implementation**: service_role/`sb_secret_*`/admin keys server-side only; never in `VITE_*`/`NEXT_PUBLIC_*`/`EXPO_PUBLIC_*`; CI bundle scan for key material on every PR; git history scan.
- **Verification**: Grep built bundles and git history for secret-key patterns; attempt privileged ops with client-visible keys.
- **Consequences of failure**: Total database compromise.
- **Evidence**: Corroborated (multiple 2026 guides).

### C2. RLS enabled with correct policies where the data API is reachable
- **Class**: Critical technical safeguard
- **Threat**: Publishable key = public; without RLS it reads/writes everything.
- **Implementation**: `enable row level security` at table creation; per-user/per-tenant policies; audit via `pg_policies`/Security Advisor; cross-user boundary tests; migration-time policy gate (new tables ship without policies).
- **Verification**: Query with publishable key signed out (rows back = failure); user-A→user-B denial tests.
- **Consequences of failure**: Mass PII exposure with write/delete (verified real incident: HoopHub #1038, July 2026 — anon key granted read+insert+delete on all public tables incl. live emails).
- **Evidence**: Verified incident + corroborated guidance.

### C3. Do NOT flag publishable/anon keys in client config as vulnerabilities
- **Class**: (Anti-finding — classification hygiene)
- **Why**: The anon/`sb_publishable_*` key is public by design; RLS is the boundary. Flagging it is a misclassification that breeds false comfort ("nobody has the key") while the real issue — missing RLS — goes unaddressed.
- **Evidence**: Corroborated (vendor model; incident #1038).

### C4. Least-privilege DB roles; service auth with scoped short-lived credentials
- **Class**: Strong recommended practice
- **Threat**: SQLi/SSRF blast-radius expansion; lateral movement via god-tokens.
- **Implementation**: Separate migration vs runtime roles; no SUPERUSER for app; per-service scoped credentials; audience-checked tokens (confused-deputy pattern is a live attack — see §D).
- **Verification**: Review grants; attempt out-of-scope operations with app role.
- **Evidence**: Corroborated.

### C5. Exposed-credential rotation; leaked-secret remediation
- **Class**: Critical technical safeguard (response control)
- **Threat**: Continued exploitation of a known-compromised secret.
- **Implementation**: Any secret reaching client/repo/logs = compromised: revoke → rotate → move server-side → audit usage logs → breach-notification assessment per jurisdiction.
- **Verification**: Confirm old key rejected; confirm absence from bundles/history post-rotation.
- **Evidence**: Corroborated.

### C6. No directory listing / unnecessary admin routes; DB policy review cadence
- **Class**: Strong recommended practice
- **Threat**: Information disclosure; unauthenticated admin access (A02/API8).
- **Implementation**: Disable listing; remove default/admin/debug routes from prod or gate behind authN + network controls; review DB policies on schema change and cadence.
- **Verification**: Probe admin paths unauthenticated; listing requests on storage.
- **Evidence**: Corroborated.

---

## D. AI & Agent Security (from 04)

### D1. Treat all retrieved/external content as untrusted data, never instructions
- **Class**: Critical technical safeguard (for any agent reading untrusted content)
- **Threat**: Indirect prompt injection (Greshake et al. 2023) — attacker plants instructions where the agent will read them; no account/rate-limit touched. Demonstrated: self-forwarding worms, memory persistence, C2, supply-chain via package docs.
- **Implementation**: Delimit untrusted content in context; sanitise ingested data; never concatenate retrieved text into privileged instruction channels; integrity checks on persistent memory; memory isolation between agents/sessions.
- **Verification**: Red-team with poisoned web pages/docs/tool outputs; confirm no instruction-following from untrusted spans.
- **Consequences of failure**: Data theft, persistent compromise, tool-mediated destructive actions — at the victim's privilege level.
- **Evidence**: Corroborated (arXiv 2302.12173; multiple 2026 write-ups).

### D2. Sandboxing for code execution (hardware-enforced, zero-access where feasible)
- **Class**: Critical technical safeguard — when agents execute code; n/a for text-only agents
- **Threat**: Unexpected code execution → RCE (ASI05).
- **Implementation**: Mandatory sandbox for interpreters/shells; no network/secret access unless the task requires it; egress filtering.
- **Verification**: Attempt breakout/persistence from within the sandbox; confirm no host/secret access.
- **Evidence**: Corroborated (2026 agentic guidance).

### D3. Tool allowlists; signed/pinned tool manifests; re-approval on change
- **Class**: Critical technical safeguard
- **Threat**: Tool poisoning (MCP03:2025), rug pulls, tool shadowing, supply-chain compromise (ASI02/ASI04).
- **Implementation**: Explicit per-task tool allowlist; pin/hash `tools/list`; re-prompt on definition change; treat tool descriptions/annotations (`readOnlyHint`) as untrusted; validate parameter schemas.
- **Verification**: Mutate a tool description post-approval; confirm re-approval triggers; test shadowing with duplicate tool names.
- **Consequences of failure**: Agent exfiltrates secrets / executes attacker instructions (MCPTox: most agents vulnerable; more capable models more vulnerable).
- **Evidence**: Corroborated (Invariant Labs Apr 2025; CSA; MCPTox; MCPInspect).

### D4. Least-privilege agent identities; per-task/per-tool scoped short-lived credentials
- **Class**: Critical technical safeguard
- **Threat**: Identity & privilege abuse (ASI03); excessive agency (LLM03:2026).
- **Implementation**: Agent never inherits the user's full credentials; unique short-lived tokens per tool/task; no shared service accounts; scope to minimum necessary (read-only where writes unneeded; no shell/network unless required).
- **Verification**: Attempt out-of-scope operations with the agent's credential; confirm denial.
- **Consequences of failure**: One injection = the blast radius of the broadest credential (confused deputy).
- **Evidence**: Corroborated.

### D5. Human approval for consequential/irreversible operations
- **Class**: Critical technical safeguard (payments, deletion, external comms, prod deploys, infra changes); strong recommended practice otherwise
- **Threat**: ASI09 trust exploitation; unintended destructive actions; goal hijack (ASI01) executing at machine speed.
- **Implementation**: Explicit approval gates for high-blast-radius actions; approval UI shows full tool info (no truncation — the human-model visibility gap); MCP spec's "SHOULD" is insufficient — make it mandatory in policy.
- **Verification**: Attempt destructive action without approval; confirm block; test truncated-description approval bypass.
- **Evidence**: Corroborated.

### D6. Secret isolation from model context
- **Class**: Critical technical safeguard
- **Threat**: Exfiltration via injection (LLM02); credential aggregation (one MCP server holding many creds).
- **Implementation**: Secrets in a store the model cannot read; injected at tool-execution time, never into context; redaction from logs/traces; avoid aggregating many systems' creds in one server.
- **Verification**: Attempt to get the model to emit a secret; inspect traces/logs for secret material.
- **Evidence**: Inferred from threat model; corroborated pattern (credential-aggregation warnings).

### D7. Output validation before model output drives tools/DB/APIs
- **Class**: Strong recommended practice → critical where output triggers state changes
- **Threat**: Improper output handling (LLM05:2026) — downstream injection, execution, integrity failures.
- **Implementation**: Schema + allowlist + size validation on model output at every tool/DB/API boundary; treat model output as untrusted input.
- **Verification**: Feed adversarial model outputs; confirm rejection at boundaries.
- **Evidence**: Corroborated (LLM05 definition).

### D8. Audit logging of agent activity (tool calls, approvals, grants)
- **Class**: Strong recommended practice → legal obligation for EU high-risk AI (Art. 12 logging)
- **Threat**: Undetected hijack/misuse; unreconstructable incidents (MCP JSON-RPC traffic evades traditional SIEM patterns).
- **Implementation**: Log tool calls, parameters (redacted), approvals, permission grants, prompt/response pairs; plan timeline reconstruction explicitly.
- **Verification**: Execute attack scenario; confirm complete reconstructable trail.
- **Evidence**: Corroborated.

### D9. Agent budgets, retry limits, circuit breakers, rollback
- **Class**: Strong recommended practice → critical for cost-exposed or destructive-capable agents
- **Threat**: Unbounded consumption (LLM06:2026 — token/cost exhaustion, "denial of wallet"); cascading failures (ASI08).
- **Implementation**: Per-task/per-session token, cost, and time budgets with hard caps; retry limits; circuit breakers; transactional semantics and defined safe failure modes; kill-switch.
- **Verification**: Runaway-task simulation; confirm caps trigger and halt.
- **Evidence**: Corroborated.

### D10. Authenticated inter-agent communication (mTLS + signing)
- **Class**: Risk-dependent control (multi-agent systems only)
- **Threat**: ASI07 — message forging, impersonation, lateral movement between agents.
- **Implementation**: mTLS and digital signatures on agent-to-agent messages; consent verification for delegation.
- **Verification**: Forge inter-agent message; confirm rejection.
- **Evidence**: Corroborated.

### D11. How controls escalate with capability (summary rule)
- Text-only → D1, D7, disclosure minimisation. + read tools → + D4(read-scoped), D6, memory-poisoning defenses. + write/exec tools → full stack (D2, D3, D5, D8, D9). + payments/prod infra → D5 mandatory/dual-control, hard spend caps, immutable audit, runbook. Multi-agent → + D10, quarantine. **Inferred** synthesis; each control's evidence above.

---

## E. Privacy & Legal Trust (from 05)

### E1. Breach notification within statutory windows
- **Class**: Legal/contractual obligation (in specified contexts)
- **Contexts**: GDPR Art. 33/34 (authority within 72h; subjects when high risk); India DPDP (Board without delay + detailed report within 72h; CERT-In within 6h — live independent duty); US state breach-notification statutes (detail per state: Unknown in this pass).
- **Implementation**: Detection → scoping capability (logging that answers whose/what/when) → notification runbooks per jurisdiction.
- **Consequences of failure**: Regulatory fines (GDPR up to €20M/4% turnover; DPDP up to ₹250 crore for safeguard failures / ₹200 crore for notification failures); enforcement actions; civil exposure.
- **Evidence**: Verified (statute texts via 2026 analyses).

### E2. Honoring deletion / access / correction requests (incl. third-party-sourced data)
- **Class**: Legal/contractual obligation (in specified contexts)
- **Contexts**: GDPR Chapter III; CCPA incl. SB 923 expansion "from or about" (eff. 1 Jan 2027); ~20 US state laws; DPDP (eff. 13 May 2027).
- **Implementation**: Request intake (webform/portal required for CA online-only businesses from 2027); proportionate identity verification; ~45-day response clocks (statute-specific); deletion searches covering broker/enrichment/partner-sourced data; vendor pass-through; suppression records where permitted.
- **Consequences of failure**: Regulatory enforcement (2026: coordinated state-AG sweeps active); private actions where available.
- **Evidence**: Corroborated (2026 legal analyses).

### E3. Children's-data safeguards
- **Class**: Legal/contractual obligation where applicable (COPPA under-13; DPDP verifiable parental consent + no tracking; CA 2027 age-appropriate design law: high-default privacy, minimisation, no dark patterns, penalties up to $5k/$15k per child per violation)
- **Evidence**: Corroborated.

### E4. Data minimisation; retention schedules; purpose limitation
- **Class**: Legal obligation in GDPR/DPDP/CA-children's contexts; strong recommended practice elsewhere
- **Threat**: Breach blast radius; unlawful retention; scope creep into regulated categories.
- **Implementation**: Collect only purpose-necessary data (audit telemetry, logs, SDK payloads); scheduled purges; retention rules per data category.
- **Evidence**: Corroborated.

### E5. Consent where required (opt-in for sensitive/children's data; withdrawable)
- **Class**: Legal obligation in specified contexts (sensitive data opt-in — growing US consensus; DPDP consent standards; marketing comms)
- **Implementation**: Plain-language itemised notices; withdrawal as easy as giving; no dark patterns.
- **Evidence**: Corroborated.

### E6. Third-party sharing inventory; processor contracts
- **Class**: Legal/contractual obligation (processor contracts: GDPR Art. 28, DPDP; sharing/opt-out duties: state laws — pixels/SDKs count as sharing/sale)
- **Implementation**: Data map of all third-party transfers; DPAs with processors; honor universal opt-out signals (GPC) where state law requires.
- **Evidence**: Corroborated.

### E7. Posting a privacy policy as the compliance measure
- **Class**: (Anti-pattern — explicitly not a control)
- **Why**: A policy page satisfies none of the operational duties above; an inaccurate policy additionally creates FTC §5 deceptive-practice exposure.
- **Evidence**: Corroborated.

---

## F. Cross-cutting

### F1. Threat modeling & secure design (ASVS V1; A06:2025 Insecure Design)
- **Class**: Strong recommended practice → expected by EU AI Act Art. 9 risk management for high-risk AI
- **Evidence**: Corroborated (ASVS 5.0; SQUR/Mishcon analyses).

### F2. Defense in depth; least privilege; deny-by-default
- **Class**: Strong recommended practice (foundational; underpins A/B/C/D items)
- **Evidence**: Corroborated.

### F3. Applying this index as a universal mandate
- **Class**: Potentially harmful or inappropriate when misapplied
- **Why**: Every class above is context-sensitive (stated in each entry). Turning risk-dependent controls into universal mandates produces either waste (CSRF tokens on bearer APIs), new vulnerabilities (hard lockout as a DoS button; KBA as a weak credential), or false assurance (flagging public keys while RLS is off; a policy page as "compliance").
