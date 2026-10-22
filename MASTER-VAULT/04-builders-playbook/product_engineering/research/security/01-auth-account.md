# §24a — Auth & Account Security: Research Notes

> Scope: application security from design through production — authentication, account lifecycle, session handling, abuse controls. Researched 2026-10-10. Read-only research; no implementation work performed.
> Claim labels used: **Verified** (primary/authoritative source checked) · **Corroborated** (≥2 independent sources agree) · **Inferred** (follows from evidence, not directly stated) · **Proposed** (analyst suggestion) · **Unknown** (could not verify).
> Canonical source list and per-finding metadata: `07-evidence-register.md`.

## 1. Current authoritative baselines (as of 2026-10-10)

### OWASP ASVS 5.0.0 (30 May 2025) — current
- **Verified**: OWASP ASVS 5.0.0, released 30 May 2025 (launched at Global AppSec EU Barcelona 2025), is the current major version; 345 requirements across 17 chapters (70 L1 / 183 L2 / 92 L3). Supersedes 4.0.3 (2021). Source: OWASP/ASVS GitHub README.
- Note: ASVS 5.0 removed direct CWE and NIST mappings — IDs must be cited versioned (e.g. `v5.0.0-2.1.1`); unversioned IDs are ambiguous. Also ASVS requirements state security *goals*, not mechanisms.
- ASVS L1 contains ~zero requirements in the Security Logging/Error Handling chapter — an L1-only gate is blind to an entire Top-10 risk class. (Corroborated by an independent 2026 checklist analysis.)

### OWASP Top 10 (web) — 2025 edition current
- **Verified**: `https://owasp.org/Top10/` redirects to OWASP Top 10:2025 — the 8th edition, superseding 2021. Codes A01:2025–A10:2025:
  - A01 Broken Access Control (absorbs 2021's standalone SSRF)
  - A02 Security Misconfiguration (moved 5→2)
  - A03 Software Supply Chain Failures (new; expands "Vulnerable and Outdated Components")
  - A04 Cryptographic Failures · A05 Injection · A06 Insecure Design
  - A07 Authentication Failures · A08 Software or Data Integrity Failures
  - A09 Security Logging & Alerting Failures
  - A10 Mishandling of Exceptional Conditions (new)
- ⚠️ **Contradiction noted**: one mid-2026 blog claimed no 2025 edition exists and 2021 remains latest. This is **refuted** by the live owasp.org redirect (checked 2026-10-10) and multiple independent 2026 sources. Treat it as stale/SEO content.
- OWASP API Security Top 10: **2023 edition still current** (API1:2023 BOLA … API10:2023 Unsafe Consumption of APIs). Corroborated across 2026 sources; no newer edition released.

### OWASP LLM / Agentic guidance — current editions
- **OWASP Top 10 for LLM Applications: 2026 edition** published 3 August 2026 (122-page PDF), superseding the 2025 edition (published Nov 2024). Current codes: LLM01:2026 Prompt Injection · LLM02:2026 Sensitive Information Disclosure · LLM03:2026 Excessive Agency · LLM04:2026 Supply Chain · LLM05:2026 Data and Model Poisoning · LLM06:2026 Unbounded Consumption · LLM07:2026 Misinformation · LLM08:2026 Hidden Context Exposure · LLM09:2026 Vector and Embedding Weaknesses · LLM10:2026 Improper Output Handling. **Corroborated** by Warrant's line-by-line reading (retrieved the PDF 2026-08-06) and an independent standards register (fetched 2026-08-25). Note the 2025 numbering differs substantially — always cite the edition year.
- **OWASP Top 10 for Agentic Applications (ASI), 2026 edition**: ASI01 Agent Goal Hijack · ASI02 Tool Misuse & Exploitation · ASI03 Identity & Privilege Abuse · ASI04 Agentic Supply Chain · ASI05 Unexpected Code Execution · ASI06 Memory & Context Poisoning · ASI07 Insecure Inter-Agent Communication · ASI08 Cascading Failures · ASI09 Human-Agent Trust Exploitation · ASI10 Rogue Agents / Uncontrolled Autonomy. **Corroborated** by ≥4 independent 2026 sources. (A Dec-2025-dated harness mapping used an earlier OA1–OA10 numbering — evidence the list was stabilised in the 2026 release.)
- Supporting: OWASP GenAI Red Teaming Guide v1.0 (23 Jan 2025); OWASP MCP Top 10 (2025), with tool poisoning codified as MCP03:2025. See `04-ai-agent-security.md`.

### NIST SP 800-63B Rev. 4 — finalized 2025-07-31
- **Verified**: NIST SP 800-63B-4 (Digital Identity Guidelines: Authentication and Authenticator Management) finalized 31 July 2025, effective 1 Aug 2025. Official: `https://pages.nist.gov/800-63-4/sp800-63b.html`. It is stricter ("SHALL") than Rev. 3 in places and **reverses** old composition/expiry guidance:
  - **SHALL NOT** require periodic password changes; force change only on evidence of compromise.
  - **SHALL NOT** impose composition rules (character-class mixing); min length 8, recommend ≥15, allow up to 64.
  - Check new passwords against known-breach corpora.
  - Throttling: verifier **SHALL** limit consecutive failed attempts using a given authenticator to **no more than 100** (upper bound, not a target; lower limits allowed), with rebind of disabled authenticators; allow bot-detection challenges to avoid locking legitimate users out.
  - Cookies are acceptable only as short-term session secrets, not as authentication.

## 2. Password hashing — current guidance (auth/account checklist item: "appropriate algorithms")

**Verified** (OWASP Password Storage Cheat Sheet, current master, checked via official cheatsheetseries repo):
1. **Argon2id first** — minimum m=19 MiB, t=2, p=1 (several equivalent memory/CPU trade-off configs listed).
2. **scrypt** if Argon2id unavailable — N=2^17, r=8, p=1.
3. **bcrypt** framed as *legacy systems only* — work factor ≥10, password limit 72 bytes; pre-hashing to dodge the 72-byte limit introduces "password shucking"/null-byte issues and is not a clean workaround.
4. **PBKDF2** only for FIPS-140 compliance — ≥600,000 iterations, HMAC-SHA-256.
5. Pepper: optional defense-in-depth only.

Implications for evaluation:
- New systems: Argon2id expected; scrypt acceptable; bcrypt alone is "legacy-acceptable" but not best practice — classification: **strong recommended practice** (bcrypt with adequate work factor is not a finding of critical severity; MD5/SHA-1/unsalted/fast hashes are **critical technical safeguard** failures).
- Server-side hashing only; never expose the hash computation to the client (client-side "pre-hashing" without server-side adaptive hashing provides no offline-attack resistance).

## 3. Login & password-reset rate limiting / bot & abuse protection

- NIST 800-63B-4: throttling is a **SHALL**; the "no more than 100" cap is an *upper bound* — treat it as ceiling, not default. Additional techniques (bot challenges, risk signals) MAY be used to reduce lockout-DoS on legitimate users. **Verified** (primary NIST text via multiple readers of the final).
- OWASP Authentication Cheat Sheet distinguishes brute force (one account, many passwords), password spraying (many accounts, one common password), credential stuffing (reused credentials). Telemetry should not treat them identically. **Corroborated** (community implementation + cheat sheet reference).
- **Do NOT impose universal hard account lockout.** The DoS risk is documented: an unauthenticated actor triggering permanent lockout = lockout button for attackers. Preferred: progressive delays, per-account + per-IP throttling, bot challenges, step-up verification; if an authenticator must be disabled, notify via an established channel, provide secure recovery, and rate-limit the notification channel itself. **Corroborated** (NIST text + community security guidance). Classification: risk-dependent control; universal hard lockout can be **potentially harmful when misapplied**.

## 4. Account-enumeration resistance

- Login, registration, and password-reset responses must be uniform for existent vs non-existent accounts ("If an account with this email exists, a reset link was sent"). **Corroborated** (OWASP Forgot Password guidance; bug-bounty checklists flag differing messages as standard findings).
- Covers: response text, response time (hashing work factor can leak existence — compare against a dummy hash on non-existent accounts), status codes, and reset-token delivery behavior. Rate-limit outbound notification emails so the defense can't be repurposed as a spam tool. **Inferred/Corroborated** from community guidance.
- Timing side-channels: use constant-time comparison for token/hash comparison. **Corroborated**.

## 5. Session cookies — secure flags, rotation, invalidation

**Corroborated** across OWASP Session Management Cheat Sheet and multiple community mirrors (canonical: `https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html`):
- Generate IDs with a CSPRNG, ≥64 bits entropy, opaque (no meaningful content).
- Exchange session IDs **only in cookies** (never URLs); flags: `Secure`, `HttpOnly`, `SameSite=Lax` or `Strict`; narrow Domain/Path.
- **Rotate session ID at every privilege change** (login, role change, password update) — prevents session fixation. Reject server-unissued IDs.
- Idle timeout (commonly 2–30 min per guidance) + absolute lifetime (hours, per sensitivity), **enforced server-side**; do not rely on client-side expiry.
- Logout must **invalidate server-side**; replaying an old session after logout must fail. Password/role change should invalidate other active sessions.
- Tokens (JWTs) must be verified: signature **and** `iss`/`aud` claims; never accept unsigned tokens; avoid long-lived auth tokens in `localStorage` (XSS-exposed). **Corroborated** (bug-bounty checklists, baseline configs).
- Bug-bounty lens: common real findings — missing `SameSite`/`Secure`, session surviving logout (cosmetic logout), fixation (ID unchanged post-login), predictable IDs. **Corroborated**.

## 6. Password-reset tokens

**Corroborated** (OWASP Forgot Password Cheat Sheet + WSTG):
- CSPRNG, high entropy (≥128-bit equivalent), single-use, short TTL (hours, not days), stored **as a hash** server-side (token in DB is a bearer credential — hashing it limits damage of DB read).
- Identical responses for existent/non-existent accounts (enumeration resistance).
- Invalidate all sessions/tokens on password change.
- Predictable reset tokens (sequential IDs, timestamps) → full account takeover; this is a standard high/critical bug-bounty finding class. **Corroborated** (pentest vault documentation).

## 7. MFA — where warranted; phishing-resistant preferred

- NIST 800-63B-4 assurance levels (AAL1/2/3): AAL2 requires two factors; AAL3 requires hardware-based phishing-resistant authenticators. MFA "where warranted" → treat as **risk-dependent control**; for privileged/admin/payment/high-value accounts → **strong recommended / critical** depending on exposure.
- Current industry direction: phishing-resistant MFA (FIDO2/WebAuthn/passkeys) preferred over SMS/voice OTP (SIM-swap, interception). NIST 800-63B-4 deprecates/weakens SMS-based OTP relative to earlier drafts — **Inferred** from guidance trajectory; the finalized text restricts "restricted authenticators." (Marked Inferred — I did not pull the full authenticator-restriction table.)
- Test MFA fallback paths: fallback to email/SMS code can be a bypass of the primary factor's assurance. **Corroborated** (WSTG identity-management test cases).
- Step-up authentication for sensitive actions (password change, payments, new device): risk-based re-auth. **Corroborated**.

## 8. Secure logout / expiry; recovery safeguards; brute-force protections; security-event logging

- Logout: server-side invalidation + client cookie cleared; accessible logout control. **Corroborated**.
- Recovery safeguards: recovery codes single-use and hashed; "security questions" (mother's maiden name etc.) are **not** acceptable — NIST 800-63B-4 eliminates knowledge-based hints ("SHALL NOT permit subscriber to store a hint accessible to an unauthenticated claimant"). **Verified** (NIST text via readers). Treat KBA as **potentially harmful when misapplied** (creates a weaker second credential).
- Brute-force: see §3 — throttling + progressive delays + risk-based; avoid permanent unauthenticated-triggerable lockout.
- Security-event logging: log authentication events (login success/failure, MFA events, password/reset events, session anomalies) **without** logging secrets/tokens/passwords; note ASVS 5.0 has **zero L1** logging requirements — an L1-only posture leaves A09 (Security Logging & Alerting Failures) unaddressed. **Verified** (ASVS chapter analysis). Log integrity + monitoring for credential-stuffing patterns. **Corroborated**.

## 9. Negative evidence / what I could not verify
- I did not pull the full ASVS 5.0 V2 (Authentication) requirement list (345 reqs) — item-level mapping to each checklist bullet is **Unknown** at requirement-ID granularity; chapter-level alignment is solid.
- Exact NIST 800-63B-4 restricted-authenticator table (SMS OTP status) — **Inferred**, not quoted from primary text.

## 10. Classification pointers (see 06-classification-index.md for the full table)
- Argon2id/scrypt hashing, CSPRNG reset tokens, server-side session invalidation, throttling without hard lockout, enumeration resistance → critical technical safeguards or risk-dependent controls (context-dependent).
- Universal hard account lockout; security questions as recovery; composition rules + forced rotation → **potentially harmful or inappropriate when misapplied**.
