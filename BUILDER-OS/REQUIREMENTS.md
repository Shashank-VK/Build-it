# Superior OS — Phase 2 Requirements (true-power mapping)

Source of truth for behavior: `../how-to-use/` (707 cards). This OS beats the `files/deve/` template on power, efficiency, usefulness. Deve core is kept; every addition below is grounded in a contract card.

## Keep from deve (proven, do not regress)
- Loop rails: max_steps=15, IAL debounce, deterministic termination (ECT), FCAR fresh-context review.
- 6 decision gates + tiny/default/high-stakes tiering + FCAR rubric + override policy.
- Cedar ABAC default-deny + check.py + presets + pre_tool_guard + checkpoint hook + secret-scan + sandbox gate.sh.
- 9 process skills + 10 YAML workflows + Taskfile verify/test/lint/secret-scan/sandbox/fcar/new-project.
- 9 os docs + 6 artifact templates + pytest suite (test_pre_tool_guard, test_scope_check).

## Add for POWER (do things deve cannot do)
1. Engineering-depth skills (15, verbatim the-harness runbooks): 01-repo-surveyor-map, 02-git-worktree-isolation, 03-context-compaction-pruner, 07-api-contract-first, 08-database-schema-architect, 09-docker-sandbox-runner, 11-litellm-router-admin, 21-tdd-red-green-refactor, 22-playwright-e2e-matrix, 23-pytest-fixture-factory, 26-systematic-rca, 31-owasp-top10-vuln-scanner, 32-secrets-entropy-sanitizer, 35-cryptography-safe-patterns, 36-grill-me-socratic-planner.
2. Subagents (4): coder, explorer, planner, reviewer specs with sandbox + step budgets.
3. Executable workflows (4): build-verify, test-and-verify, migration-safeguard, refactor-safely (+ eval-gate from Domain-B08 evals).
4. Real MCP layer: mcp_servers.json (filesystem/playwright/context7/github stdio configs) + MCP_SECURITY.md (transport/auth/tool-poisoning defenses, inspector).
5. Quality-gate system: Evidence Principle (every claim/test cited), eval-gate (evals for AI features), accessibility WCAG-AA + performance budgets at Gate 6.
6. Post-tool auto-linter hook (ruff + AST) from the harness hooks.
7. Change-coverage discipline (adapted from Phase 1 coverage ledger): every behavior change ships with receipt (tests + line ranges + sha) in build-log; gaps quarantined, never silently dropped.

## Add for EFFICIENCY (do deve things cheaper/faster)
8. Tier router: tiny/default/high-stakes task profiles selecting model effort + gate depth (from tier router + stakes-classifier).
9. Parallel-worker discipline: 40-cap fanout with idempotent rerun + checkpoint-per-receipt (adapted Phase 1 manager pattern) for repo-wide jobs (migrations, evals).
10. Context engineering: compaction-pruner + repo maps + llms.txt + progressive skill disclosure (skills index.json).
11. Spend/log discipline: LiteLLM tiers + spend-log hard caps + Langfuse tracing (advisory→enforced).
12. Claim-evidence discipline (adapted fetch-log): every external claim (version/URL/capability) logged with URL+HTTP+date; failures queued, never invented.

## Add for USEFULNESS (cover products deve ignores)
13. Disciplines (6): api-product (date versioning), billing (money-pipe), mobile-release, notifications (central orchestration), finops, trust-safety (+ ai-act/compliance pointers).
14. Rules upgrade: 34 engineering rules + 19 anti-patterns digests (deve had 10 rules).
15. Templates (+10): problem-validation, PRD, technical-design, ADR, test-plan, code-review, security-verification, release-readiness, incident-response, post-launch-evaluation.
16. Domain playbooks: A (build product), B (LLM features: RAG/evals/cost), C (ops) checklists.
17. Company forensics notes: 16 verdicts as cautionary tales (knight-capital $440M first).

## Acceptance
- `task verify` exit 0 (pytest + lint + secret-scan + new gates).
- Every new skill/workflow has SKILL/frontmatter or state machine + DoD + evidence fields.
- No OpenCode-only absolute paths; universal notes flag tool differences.
- how-to-use/ untouched (read-only); superior-os/ references card IDs, never copies raw corpus.
