# §24b — Application & API Security: Research Notes

> Scope: server-side validation, injection, authZ, CSRF, headers, transport, CORS, uploads, traversal, webhooks, replay, errors, payments, dependencies. Researched 2026-10-10. Read-only research. Canonical metadata: `07-evidence-register.md`.

## 1. Threat framing — the current OWASP maps

- **OWASP Top 10:2025** (current; verified via live redirect): A01 Broken Access Control (incl. SSRF), A02 Security Misconfiguration, A03 Software Supply Chain Failures (new), A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software/Data Integrity Failures, A09 Logging & Alerting Failures, A10 Mishandling of Exceptional Conditions (new).
- **OWASP API Security Top 10:2023** (still current): API1 BOLA · API2 Broken Authentication · API3 BOPLA (mass assignment + over-exposure) · API4 Unrestricted Resource Consumption · API5 BFLA · API6 Unrestricted Sensitive Business Flows · API7 SSRF · API8 Security Misconfiguration · API9 Improper Inventory Management · API10 Unsafe Consumption of APIs. Industry practitioners note API1/BOLA is the dominant API attack pattern (~40% of API attacks cited by one 2026 analysis — **Unverified single-source estimate**, treat as directional).
- **ASVS 5.0.0** (345 reqs, 17 chapters) is the requirements-level reference; the Top 10s are risk taxonomies, not test suites.

## 2. Input validation & injection defense

- **Server-side validation is non-negotiable**: client-side validation is UX, not a control. Validate type, length, range, format on **every** trust boundary (REST, GraphQL, gRPC, webhooks, file imports). **Corroborated** (OWASP, API hardening skill guidance, baseline configs).
- **Parameterised queries** (prepared statements) for all database access — the primary SQL-injection control (A05). Never string-interpolate user input into SQL/shell/LDAP/template expressions. **Corroborated** (community baseline: "never insert user input into HTML, SQL, shell, or template contexts without context-appropriate escaping").
- **Context-appropriate output encoding**: encode for the *sink* — HTML entity encoding for HTML, JS encoding for script contexts, URL encoding for URLs, parameterisation for SQL. No single "sanitize()" is correct everywhere. **Corroborated**.
- Deserialization: never deserialize untrusted data with formats that execute code; prefer JSON over language-native pickles with strict type checking. **Corroborated**.

## 3. Authorisation on every protected operation

- **Check authN *and* object-level authZ on every endpoint** — BOLA/API1 and BFLA/API5. "Make unauthenticated endpoints an explicit reviewed decision, not an oversight." **Corroborated**.
- Per-object ownership checks (`auth.uid() = owner_id` style), per-function role checks; never rely on client-side gating or "hidden" routes (API9: undocumented/shadow/zombie APIs and old versions are a named risk — maintain an API inventory).
- **Mass-assignment prevention** (API3/BOPLA): explicit allowlist of writable fields (e.g., Zod/Pydantic schemas); never bind request bodies directly to ORM models. **Corroborated** (API hardening guidance).

## 4. Resource & abuse limits

- Request size limits, body-parser caps, timeouts, file-upload size/count limits — counters to API4 Unrestricted Resource Consumption (DoS, bill spikes, "denial of wallet" for metered AI endpoints). **Corroborated**.
- Rate limiting on auth endpoints (credential stuffing), on expensive endpoints, and on signup/comment/purchase flows (API6 anti-automation). Per-user *and* per-IP signals; distributed attacks bypass per-IP-only limits — a known false-negative in assessments. **Corroborated** (bug-bounty checklist).

## 5. CSRF — where the auth model requires it

- CSRF applies to **cookie-based auth**; bearer-token (Authorization header) models are not CSRF-exploitable in the classic sense (there, XSS is the enemy). **Corroborated**.
- Layered default: `SameSite=Lax` (blocks most CSRF) + Origin/Referer checks + double-submit cookie or synchronizer token for state-changing operations. **Corroborated** (2026 hardening guide).
- **Risk-dependent**: CSRF tokens are unnecessary overhead for pure bearer-token APIs; omitting them there is correct, not a gap. Imposing them is **potentially harmful when misapplied** only in the sense of wasted complexity — low harm, but the checklist should not demand it universally.

## 6. Security headers, HTTPS, CORS

- Baseline headers (OWASP Secure Headers Project): `Strict-Transport-Security` (HSTS), `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`, `X-Frame-Options`/frame-ancestors. Missing headers = API8 misconfiguration class. **Corroborated**.
- **HTTPS everywhere**: TLS 1.2+ minimum, HSTS site-wide, HTTP→HTTPS redirect; never disable TLS verification in code. **Corroborated**.
- **Narrow CORS**: reflect only allowlisted origins; never `Access-Control-Allow-Origin: *` with `Allow-Credentials: true`; keep `Vary: Origin`. **Corroborated**.

## 7. File uploads & path traversal

- Uploads: validate file type by **content sniffing** (magic bytes), not extension; size limits; store outside web root with random names; never execute uploaded content; serve with `Content-Disposition: attachment` / non-sniffable MIME where appropriate; AV/sandbox scanning for high-risk flows. **Corroborated** (ASVS V12 File & Resources; community guides).
- Path traversal: canonicalize and jail paths to an intended directory; reject `..`, absolute paths, null bytes, and encoding tricks; use allowlisted filenames. **Corroborated** (standard guidance).

## 8. Webhooks, replay, idempotency

- **Webhook verification**: verify HMAC signatures on a shared secret (compare with constant-time compare), validate timestamps within a skew window, use per-endpoint secrets, pin the sender's IP/allowlist where feasible. **Corroborated** (standard vendor practice; community baseline).
- **Replay/duplicate protection**: timestamp + nonce tracking, idempotency keys on mutating/payment endpoints — prevents double-charge/double-apply on retried requests. **Corroborated**.

## 9. Errors, payments, dependencies

- **No sensitive data in errors**: generic messages to clients; stack traces, SQL errors, and internal paths only to server logs. Note A10:2025 (Mishandling of Exceptional Conditions) now elevates error-handling failures to a top-ten category. **Corroborated**.
- **Server-side price/payment validation**: never trust client-supplied prices, totals, quantities, or payment statuses — recompute server-side; verify payment-gateway webhooks before fulfilling. **Corroborated** (standard e-commerce guidance).
- **Dependency scanning**: automated CVE scanning in CI (npm audit / Trivy / Snyk / pip-audit / govulncheck), fail on critical/high; secret scanning on commits (gitleaks/TruffleHog); SBOM for supply-chain visibility. **Corroborated**. Note A03:2025 expands "vulnerable components" to whole-ecosystem supply-chain failures.

## 10. SSRF

- Now folded into A01:2025; standalone API7:2023 for APIs. Control: never fetch user-supplied URLs without host/scheme allow-list; block private/link-local/metadata IPs (`169.254.169.254`), enforce HTTPS-only, don't hand-roll IP parsers (octal/hex/IPv4-mapped tricks), pin DNS check→use. **Corroborated** (MCP OAuth-discovery guidance applies the same pattern to server-side fetches).

## 11. Negative evidence
- I did not enumerate the OWASP Secure Headers Project's 2026 header list exhaustively; the baseline above is the stable core. **Unknown** at exhaustive-list granularity.
- The "~40% of API attacks are BOLA" figure is a single-source estimate — **Unknown** reliability; do not cite as fact.
