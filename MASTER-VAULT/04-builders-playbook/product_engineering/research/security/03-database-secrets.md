# §24c — Database & Secrets Security: Research Notes

> Scope: secrets handling, DB permissions, RLS, encryption, service auth, credential rotation/leaks, admin-surface exposure, public-vs-confidential key separation. Researched 2026-10-10. Read-only research. Metadata: `07-evidence-register.md`.

## 1. Core principle — privileged secrets out of client code

**Corroborated** (OWASP, community baselines, multiple 2026 vendor-integration guides):
- Never commit secrets — environment variables or a secrets manager; scan commits/PRs for hardcoded secrets (gitleaks, TruffleHog, git-secrets).
- Service-role / admin / private keys live **server-side only** (Edge Functions, server environments); never in `VITE_*` / `NEXT_PUBLIC_*` / `EXPO_PUBLIC_*` prefixed variables (bundlers inline them into client bundles).
- Never log tokens, passwords, session IDs, or secrets.

## 2. Supabase / Firebase-style publishable keys — the correct classification

**Corroborated by multiple independent 2026 sources + a real incident (see §6):**
- Supabase `anon` key (newer `sb_publishable_...` naming) is **public by design** — it ships in the browser bundle. Security comes from **Row-Level Security (RLS)**, not key secrecy. Treating it as a secret breeds false comfort ("nobody has the key") while the key is in plain sight.
- The **`service_role` key (newer `sb_secret_...`) bypasses RLS entirely** — for trusted server use only. Shipping it to the browser = total compromise of every row; correct RLS policies cannot help a privileged caller. The legacy JWT `service_role` key has no browser-use guard, so do not rely on the platform to catch it.
- ✅ Correct evaluation: flag *missing/disabled RLS* and *overly permissive policies* as the finding; flag *service_role/secret key in client code or git history* as critical; do **not** flag the mere presence of a publishable key in client config. New tables default to no policies — "with RLS off the publishable key reads everything" — so verify by querying with the publishable key while signed out: rows back = policy failure.
- Firebase follows the same model: the web API key is a project identifier, not a secret; Firestore/Storage security rules are the boundary. (Corroborated by vendor docs tradition; Supabase specifics verified above.)
- Audit `pg_policies` / Security Advisor, and test across user boundaries (user A requesting user B's rows must be denied). Supabase secret keys (`sb_secret_...`) reject browser use, but legacy JWT service keys do not.

## 3. Least-privilege database permissions & service auth

- Application DB users get the minimum grants needed (e.g., no `SUPERUSER`, no DDL in prod for app roles); separate roles for migrations vs runtime. **Corroborated** (standard guidance).
- Row-Level Security where the access model is per-user/per-tenant — RLS is the enforcement point for direct-DB-access architectures (Supabase, PostgREST, Hasura-style). Where the API layer owns authZ, RLS may be redundant — but **only safe together if the direct data API is off** (see §6 incident). **Corroborated**.
- Record/field-level access control: enforce at the data layer (RLS policies, views, column grants) not just the API layer, wherever clients can reach the store directly. **Corroborated**.
- Service-to-service auth: scoped, short-lived credentials per service; no shared god-tokens; mutual TLS or signed tokens with audience checks (the MCP "confused deputy" research shows token-passthrough without audience validation is a live attack pattern — see `04-ai-agent-security.md`). **Corroborated**.

## 4. Encryption & key management

- Encrypt sensitive data at rest (provider-managed or envelope encryption with a KMS/HSM); TLS in transit. Passwords are **hashed** (adaptive: Argon2id/scrypt — see `01-auth-account.md`), never encrypted, except rare interop edge cases. **Corroborated** (OWASP Password Storage Cheat Sheet).
- Key separation: encryption keys ≠ data; rotate keys per policy; never hardcode keys. **Corroborated**.

## 5. Exposed-credential rotation & leaked-secret remediation

- Any secret that reached a client bundle, public repo, log, or error message is **compromised**: rotate immediately, then move server-side. Searching git history and deployed bundles for the key value is part of the response. **Corroborated** (2026 Supabase key-model guides: "any secret key that ever reached the client is compromised and must be rotated").
- Response shape: revoke → rotate → audit usage logs for exploitation → notify if PII touched (breach-notification clocks vary by jurisdiction — see `05-privacy-legal.md`). **Inferred** from incident-response practice; jurisdiction specifics in §5 file.

## 6. Real misconfiguration incident (negative/positive evidence)

- **Verified incident**: HoopHub GitHub issue #1038 — Supabase emailed a `rls_disabled_in_public` CRITICAL alert (26 Jul 2026); reporter verified 2026-07-29 that the publishable/anon key (public by design, present in every installed app binary) granted read+insert+delete on every public table because PostgREST Data API was enabled while all authZ lived in the API layer with no RLS. Prod `users` table exposure included live PII (emails). This is the canonical example of the exact misclassification the checklist warns against: the key was never the secret — the missing RLS was the vulnerability.
- Supabase's own `rls_disabled_in_public` alerting (CRITICAL email) is a detection control worth noting — **Corroborated** (incident thread).

## 7. No directory listing / unnecessary admin routes; DB policy review

- Disable directory listing on static/object storage; remove default/admin pages and change default credentials; no unnecessary admin/debug routes in production; admin interfaces behind authN + network controls. **Corroborated** (WSTG-derived checklists).
- Review DB policies on a cadence and on every schema change (new tables ship without policies in Supabase — a policy review gate at migration time is the fix). **Corroborated**.

## 8. Public client config vs confidential credentials — separation rule

- Three buckets (corroborated taxonomy from 2026 integration guides):
  1. **Browser-safe**: project URL + publishable key (may carry `PUBLIC_` prefixes; safe to commit in `.env.example` form).
  2. **Server-only**: service-role/secret keys (env store only; CI secret at most; never in build output — enforce with a bundle scan on every PR).
  3. **Per-request**: the user's session JWT (transported in cookies by server client; never in `localStorage` for long-lived tokens).
- The per-user JWT scopes access through RLS — it is a bearer credential and must be treated as confidential in transit/storage, distinct from the publishable key which is public. **Corroborated**.

## 9. Classification pointers
- service_role/secret key in client or git history → **critical technical safeguard** failure.
- RLS disabled/missing on tables reachable via the data API → **critical technical safeguard** failure.
- Publishable key visible in client bundle with correct RLS → **not a finding** (document the provider's security model; flagging it is a misclassification).
- Secrets in logs/errors → **critical technical safeguard**.
