# Integration & Extensibility — Per-Element Knowledge Base (Phase 4, Batch D-3)

> **Date:** 2026-09-01 | **Sources:** `phase-1/MASTER_TAXONOMY.md`, `phase-2/RANKINGS.md`, `phase-1/batch-3/BATCH-3_INTEGRATION_EXTENSIBILITY.md`
> **Template:** 18-section per element. Consolidated.

---

## CAP-17 — Open Tool Interoperability (MCP)
1. **Overview:** Client-server middleware over MCP (JSON-RPC 2.0) for tool/resource/prompt discovery + execution.
2. **Why matters:** Standardizes M×N tool integration → M+N; universal bedrock (SC-02/07).
3. **How works:** MCP client ↔ server (stdio/SSE); `tools/resources/prompts`; registries (mcp.so, Glama).
4. **When use:** Any external tool/API integration across all archetypes.
5. **When NOT:** Native tools already in harness (files/terminal).
6. **Importance:** S-tier (universal).
7. **Essential:** `modelcontextprotocol/servers` + client.
8. **Optional:** mcp.so/Glama registries.
9. **Rules:** Capability negotiation; scoped perms per server.
10. **Deps:** PROT-01 protocol.
11. **Integration:** Exposes tools to CAP-03 orchestrator.
12. **Failure modes:** Server crash, transport, missing schema.
13. **Security:** Verify servers; injection-defense MCP output (B6).
14. **Maintenance:** Pin server versions; re-verify registries.
15. **Sources:** Batch-3 B3-01..05.
16. **Links:** https://modelcontextprotocol.io.
17. **Last verified:** 2026-09-01.
18. **Re-check:** MCP spec version change.

---

## CAP-18 — Procedural Skills Execution
1. **Overview:** Discover/load/execute on-demand procedural runbooks (progressive disclosure).
2. **Why matters:** Reusable domain workflows; context economy (SC-05).
3. **How works:** `SKILL.md` index (metadata) → full-body on activation.
4. **When use:** Repo research, architecture, testing, security, data (C1/C4/C6).
5. **When NOT:** Novel tasks needing bespoke prompts.
6. **Importance:** S-tier. C1/C4/C6=A/S; C3=C.
7. **Essential:** Skill catalog (5 materialized in `.harness/skills/`).
8. **Optional:** Community skill repos.
9. **Rules:** Progressive disclosure; verify each skill; anti-bloat (index not 40 files).
10. **Deps:** MEC-02 progressive disclosure.
11. **Integration:** Skills trigger via agent prompts.
12. **Failure modes:** Skill rot, ambiguous trigger, duplicate skills.
13. **Security:** Supply-chain verify skills (CAP-31).
14. **Maintenance:** Prune unused (Dead-Code Pruner).
15. **Sources:** Batch-3 B3-06/07.
16. **Links:** `.harness/skills/`.
17. **Last verified:** 2026-09-01.
18. **Re-check:** skill framework changes.

---

## CAP-19 — Ambient Rules Enforcement
1. **Overview:** Discover/apply directory-scoped constraints/conventions (AGENTS.md/CLAUDE.md/.cursorrules hierarchy).
2. **Why matters:** Consistency, security scope, coding standards (SC-07/08).
3. **How works:** CWD→root traversal; dedup by path; precedence.
4. **When use:** Any project (esp C1 product, C5 platform).
5. **When NOT:** Never (core).
6. **Importance:** S-tier. C1/C4/C5=S; C2/C3/C6=A.
7. **Essential:** Rules files (AGENTS.md).
8. **Optional:** rule linting.
9. **Rules:** Merge cleanly; dedup; scoped per subproject.
10. **Deps:** MEC-03 inheritance.
11. **Integration:** Injects ambient constraints into prompt.
12. **Failure modes:** Conflicting rules, stale directives.
13. **Security:** Rules can impose security policy.
14. **Maintenance:** Version rules.
15. **Sources:** Batch-3 B3-10/11/12.
16. **Links:** AGENTS-md convention.
17. **Last verified:** 2026-09-01.
18. **Re-check:** rule-file spec changes.

---

## CAP-20 — Lifecycle Interception & Hooks
1. **Overview:** Deterministic event-interception control plane (PreToolUse/PostToolUse/Stop...).
2. **Why matters:** Policy gates before dangerous execution (SC-07 zero-tolerance).
3. **How works:** Hook system fires sync handlers; block with exit 2; mutate args.
4. **When use:** Security gating, linting, telemetry — all archetypes.
5. **When NOT:** (Core, always present).
6. **Importance:** S-tier (universal).
7. **Essential:** hook system (`.harness/hooks/hooks.json` + pre_tool_guard.py).
8. **Optional:** lefthook/pre-commit.
9. **Rules:** Deterministic; non-bypassable; timeouts.
10. **Deps:** MEC-04 event system.
11. **Integration:** Wraps all tool execution.
12. **Failure modes:** Hook latency, matcher gaps.
13. **Security:** Core enforcement point.
14. **Maintenance:** Keep hooks minimal/fast.
15. **Sources:** Batch-3 B3-13/14/15.
16. **Links:** `.harness/hooks/`.
17. **Last verified:** 2026-09-01.
18. **Re-check:** hook spec changes.

---

## CAP-21 — Composite Plugin Packaging & Distribution
1. **Overview:** Standardized bundle (skills+rules+hooks+MCP config) with versioning/namespacing.
2. **Why matters:** Distributable extension units (SC-02/07).
3. **How works:** `plugin.json` manifest; parse+load components.
4. **When use:** Multi-component extensions; teams.
5. **When NOT:** Single-component ad-hoc.
6. **Importance:** A-tier. C1/C2/C4/C5=A; C3/C6=B.
7. **Essential:** (optional) plugin loader.
8. **Optional:** plugin marketplaces.
9. **Rules:** Manifest validation; version pinning.
10. **Deps:** CAP-18/19/20 components.
11. **Integration:** Loads into harness.
12. **Failure modes:** Broken bundles, conflict.
13. **Security:** Supply-chain verify (CAP-31).
14. **Maintenance:** Plugin lifecycle.
15. **Sources:** Batch-3 B3-16/17.
16. **Links:** (plugin spec).
17. **Last verified:** 2026-09-01.
18. **Re-check:** plugin format.

---

## CAP-22 — Model Gateway & Provider Abstraction
1. **Overview:** Provider-agnostic LLM interface: schema translation, failover, retry, rate-limit.
2. **Why matters:** Portability, resilience, cost (SC-02/05).
3. **How works:** LiteLLM/Portkey proxy normalizing APIs; failover tiers.
4. **When use:** Multi-provider or vendor-agnostic harness (all).
5. **When NOT:** Single-provider locked tool.
6. **Importance:** S-tier (universal).
7. **Essential:** LiteLLM (`.harness/telemetry/litellm-config.yaml`).
8. **Optional:** Portkey/OpenRouter.
9. **Rules:** OpenAI-compatible normalization; failover; retry bounds.
10. **Deps:** Prot-02 schemas.
11. **Integration:** All model calls route through.
12. **Failure modes:** Proxy overhead, provider outage.
13. **Security:** Scope keys; never leak to prompt.
14. **Maintenance:** Provider version churn.
15. **Sources:** Batch-3 B3-18/19.
16. **Links:** https://docs.litellm.ai.
17. **Last verified:** 2026-09-01.
18. **Re-check:** provider/API changes.

---

## CAP-23 — Dynamic Model Routing & Tier Selection
1. **Overview:** Route turns to cost-optimal vs high-reasoning models by complexity (Pareto).
2. **Why matters:** Cost-quality Pareto (SC-05).
3. **How works:** Classifier/route engine (LiteLLM Router / OpenRouter; note RouteLLM was gate-removed for maintenance stall).
4. **When use:** High-volume C3/C4 with mixed complexity.
5. **When NOT:** Uniform single-model tasks.
6. **Importance:** A-tier. C3=S; C1/C2/C4/C6=A; C5=B.
7. **Essential:** (optional) OpenRouter.
8. **Optional:** LiteLLM routing/RouterRunnable.
9. **Rules:** Budget-guard; per-task complexity heuristic.
10. **Deps:** CAP-22 gateway.
11. **Integration:** Dispatch before model call.
12. **Failure modes:** Misrouting cost/quality.
13. **Security:** N/A (dispatch only).
14. **Maintenance:** Recalibrate router.
15. **Sources:** Batch-3 B3-20/21.
16. **Links:** https://docs.litellm.ai (router); https://openrouter.ai.
17. **Last verified:** 2026-09-01.
18. **Re-check:** router model versions.

---

## PROT-01 — Model Context Protocol (Protocol)
1. **Overview:** Open standard (JSON-RPC 2.0, stdio/SSE) client-server contract.
2. **Why matters:** Cross-vendor tool interop.
3. **How works:** Spec + client/server runtimes.
4. **When use:** Always (MCP backbone).
5. **When NOT:** Native-only harness.
6. **Importance:** S-tier.
7. **Essential:** spec + reference servers.
8. **Optional:** registries.
9. **Rules:** Version pin; capability negotiation.
10. **Deps:** —
11. **Integration:** Backs CAP-17.
12. **Failure modes:** Spec drift.
13. **Security:** Server trust.
14. **Maintenance:** Track spec.
15. **Sources:** Batch-3 B3-01.
16. **Links:** https://modelcontextprotocol.io.
17. **Last verified:** 2026-09-01.
18. **Re-check:** Spec version.

---

## PROT-02 — Function Calling / Tool-Use Schema (Protocol)
1. **Overview:** JSON-Schema tool parameter contracts across models.
2. **Why matters:** Deterministic tool invocation.
3. **How works:** `parameters/properties` schema emission.
4. **When use:** All tool use.
5. **When NOT:** —
6. **Importance:** S-tier.
7. **Essential:** JSON-Schema.
8. **Optional:** —.
9. **Rules:** Strict schema; validation.
10. **Deps:** —
11. **Integration:** Powers E1-E11.
12. **Failure modes:** Schema mismatch.
13. **Security:** Validate args.
14. **Maintenance:** —.
15. **Sources:** Batch-3 B3-22.
16. **Links:** JSON-Schema.
17. **Last verified:** 2026-09-01.
18. **Re-check:** —.

---

## PROT-03 — Harness-as-Code (HaC) Specification
1. **Overview:** Declarative versioned schema for agents/tools/permissions/hooks config.
2. **Why matters:** Diffable, reversible, migratable harness (SC-06/08/10).
3. **How works:** YAML/JSON schema; schema evolution engine.
4. **When use:** The harness itself (always).
5. **When NOT:** —
6. **Importance:** S-tier.
7. **Essential:** `.harness/harness.config.yaml`.
8. **Optional:** HaC migration tools.
9. **Rules:** Version; validate; parity across envs.
10. **Deps:** —
11. **Integration:** Defines whole harness.
12. **Failure modes:** Schema drift.
13. **Security:** Config is policy.
14. **Maintenance:** Migration engine.
15. **Sources:** Batch-5 B5-11.
16. **Links:** `.harness/`.
17. **Last verified:** 2026-09-01.
18. **Re-check:** config schema.

---

*End of D-3 (Integration).*