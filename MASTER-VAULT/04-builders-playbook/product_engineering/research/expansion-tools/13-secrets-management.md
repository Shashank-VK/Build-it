# §30 — Secrets Management (expansion-tools)

Workstream: expansion-tools · Researched 2026-10-10 · Read-only research. Neutral records: no rankings, no recommendations.

Legend: **U(Verified)** = real company/team demonstrably uses it · **U(Proposed)** = mentioned as option, use not demonstrated · **U(Unknown)** = unclear. Status flags: ACTIVE / MAINTAINED / EXPERIMENTAL / DEPRECATED / SUPERSEDED / UNAVAILABLE / CONTROVERSIAL.

---

## SM-01 — HashiCorp Vault — ACTIVE (license saga: MPL-2.0 → BSL 1.1)
- Purpose / problem: The secrets-management standard: dynamic secrets, PKI, encryption-as-a-service, identity-based access; HCP Vault / Vault Enterprise.
- OSS/commercial: License saga — **MPL-2.0 → BSL 1.1 (Aug 2023)**; community fork **OpenBao** (Linux Foundation; v2.7.0 Sep 23, 2026).
- Maintenance: Active (HashiCorp/IBM — IBM as licensor line per Mar 2026 sources).
- Limitations: Operational complexity (unseal, HA, storage backends); BSL restricts competitive hosting.
- Alternatives: OpenBao, Infisical, Doppler, cloud KMS/SM.
- Switching costs: High (policies, auth methods, integrations).
- Use: U(Verified) — enterprise standard.

## SM-02 — OpenBao — ACTIVE (the fork)
- Purpose / problem: Community fork of Vault (pre-BSL codebase), Linux Foundation; drop-in compatibility goal.
- OSS/commercial: OSS (MPL-2.0 lineage).
- Maintenance: Active — **v2.7.0 (Sep 23, 2026)**.
- Limitations: Younger ecosystem; enterprise features lag Vault Enterprise.
- Alternatives: Vault, Infisical.
- Switching costs: Low (from Vault).
- Use: U(Proposed).

## SM-03 — Infisical — ACTIVE
- Purpose / problem: Developer-first secrets platform: open-source core (self-host free forever), dynamic secrets, secret scanning, PKI/SSH, broad integrations; expanding into identity/access management and **security infrastructure for AI agents/workloads**.
- OSS/commercial: Open-core. **$16M Series A** (Elad Gil participating; ~2025). Pricing: Pro $18/identity/mo; free tier: 5 identities, 3 projects, 3 environments, rate-limited (200 reads/min); self-hosted: no rate limits.
- Maintenance: Active (2026).
- Limitations: RBAC/SSO/audit logs are paid gates; enterprise surface younger than Vault.
- Security: Zero-knowledge claims weaker than 1Password's documented model (per 2026 comparison — verify).
- Alternatives: Doppler, OpenBao, Vault, Akeyless.
- Switching costs: Medium.
- Use: U(Proposed).

## SM-04 — Doppler — ACTIVE (name collision warning)
- Purpose / problem: Developer-centric secrets sync: clean UX, dependable propagation across environments/platforms, integrations, config syncs.
- OSS/commercial: Commercial proprietary SaaS (no self-host). **$20M Series A led by CRV** (2022; GV, Sequoia, YC participated). Pricing: Developer free for 3 users; $8/mo per additional user; audit retention 3 days (Developer) → 90 (Team) → 1,095 (Enterprise).
- Maintenance: Active (2026); best-in-class onboarding polish per 2026 comparisons.
- Limitations: SaaS-only (no self-host); static-secrets focused (no dynamic secrets/PKI/SSH vs Infisical); governance features paywalled.
- **Name collision:** "Doppler" is also a Whetstone Research onchain token-launch protocol ($9M seed, Pantera, 2026) — unrelated; disambiguate in searches.
- Alternatives: Infisical, 1Password, Vault.
- Switching costs: Medium.
- Use: U(Proposed).

## SM-05 — 1Password (Secrets Automation) — ACTIVE
- Purpose / problem: Secrets management via Connect server, service accounts, CLI; built on SecretHub acquisition.
- OSS/commercial: Commercial. Teams Starter $19.95/mo (10 users); Business $7.99/user/mo.
- Maintenance: Active (2026).
- Limitations: No true free plan (14-day trial); explicitly documented zero-knowledge model is the differentiator.
- Alternatives: Doppler, Infisical.
- Switching costs: Medium.
- Use: U(Proposed).

## SM-06 — AWS Secrets Manager / Parameter Store — ACTIVE
- Purpose / problem: Native AWS secrets storage with rotation, IAM integration.
- OSS/commercial: Commercial (AWS).
- Maintenance: Active.
- Limitations: AWS-coupled; per-secret/API-call pricing at scale.
- Alternatives: Vault, Infisical.
- Switching costs: Low inside AWS; high outside.
- Use: U(Verified) — AWS standard.

## SM-07 — Akeyless — ACTIVE
- Purpose / problem: SaaS secrets management with DFC (distributed fragments cryptography); zero-knowledge architecture.
- OSS/commercial: Commercial SaaS.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Vault, Infisical.
- Use: U(Proposed).

## SM-08 — sops (Mozilla) — MAINTAINED
- Purpose / problem: Encrypt secrets in Git (age/PGP + KMS); GitOps-native.
- OSS/commercial: OSS MPL-2.0.
- Maintenance: Maintained (2026). (Depth debt.)
- Alternatives: Sealed Secrets, ESO.
- Use: U(Proposed).

## SM-09 — External Secrets Operator — ACTIVE
- Purpose / problem: Sync secrets from external managers (Vault, AWS SM, Doppler, Infisical) into Kubernetes.
- OSS/commercial: OSS Apache-2.0.
- Maintenance: Active (2026). (Depth debt.)
- Alternatives: Sealed Secrets.
- Use: U(Proposed).

## Notable status findings (secrets)
- Vault — **BSL 1.1 (Aug 2023)** → **OpenBao fork (LF), v2.7.0 Sep 2026**.
- Infisical — **$16M Series A**, expanding from secrets into identity + AI-agent security infra.
- Doppler — **$20M Series A (CRV, 2022)**; SaaS-only; name-collides with a crypto protocol.

---

### Per-record metadata (condensed)
- Infisical vs Doppler: securityboulevard.com (Jul 2026); merginit.com free-secrets comparison (Jun 2026). Confidence: Medium.
- Infisical $16M Series A: pulse2.com (~2025). Confidence: Medium.
- Doppler $20M Series A: siliconangle.com (Apr 2022); thenewstack.io; darkreading.com. Confidence: High.
- Doppler crypto collision: investorshangout.com (2026). Confidence: Medium.
- Vault/OpenBao: summary evidence. Confidence: High.
