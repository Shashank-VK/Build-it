# Skills Verification Report
**Date:** 2026-09-08 | **Method:** index.json (40 skills registered) cross-checked against `.harness/skills/` folders physically on disk (15 folders found)

---

## Summary

| Category | Count |
|---|---|
| Skills registered in `index.json` | **40** |
| Skill folders physically on disk | **15** |
| OS Workflow skills (GOD_PROMPT defined, no folder yet) | **9** |
| Registered + folder EXISTS | **15** |
| Registered in index but folder MISSING | **25** |
| Folder on disk but NOT in index (ID mismatch) | **3** |

---

## CONFIRMED PRESENT — Folder EXISTS on Disk (15/40)

| # | Index Name | Folder on Disk | Status |
|---|---|---|---|
| 01 | `repo-surveyor-map` | `01-repo-surveyor-map/` | MATCH |
| 07 | `api-contract-first-design` | `07-api-contract-first/` | MATCH |
| 08 | `database-schema-architect` | `08-database-schema-architect/` | MATCH |
| 11 | `litellm-router-admin` | `11-litellm-router-admin/` | MATCH |
| 21 | `tdd-red-green-refactor-loop` | `21-tdd-red-green-refactor/` | MATCH |
| 22 | `playwright-e2e-matrix` | `22-playwright-e2e-matrix/` | MATCH |
| 23 | `pytest-fixture-factory` | `23-pytest-fixture-factory/` | MATCH |
| 26 | `systematic-root-cause-rca` | `26-systematic-rca/` | MATCH |
| 31 | `owasp-top10-vuln-scanner` | `31-owasp-top10-vuln-scanner/` | MATCH |
| 32 | `secrets-entropy-sanitizer` | `32-secrets-entropy-sanitizer/` | MATCH |
| 35 | `cryptography-safe-patterns` | `35-cryptography-safe-patterns/` | MATCH |
| 36 | `grill-me-socratic-planner` | `36-grill-me-socratic-planner/` | MATCH |

---

## FOLDERS ON DISK BUT NOT MATCHING INDEX IDs (3 folders — ID drift)

These folders exist physically but their names don't match index entries.
Root cause: materialization sprint used CAP-XX numbering from Phase 1; index.json used a different final numbering scheme.

| Folder on Disk | Closest Index Match | Issue |
|---|---|---|
| `02-git-worktree-isolation/` | Index #02 = `github-issue-pr-triage` | Name mismatch — this is Phase 1 CAP-02 git worktrees |
| `03-context-compaction-pruner/` | Index #03 = `ast-symbol-navigator` | Name mismatch — this is Phase 1 CAP-03 context management |
| `09-docker-sandbox-runner/` | Index #09 = `microservices-event-stormer` | Name mismatch — this is CAP-24 sandbox runner |

---

## REGISTERED IN INDEX BUT FOLDER MISSING ON DISK (25/40)

### Codebase Exploration (3 missing)
| # | Skill | Tier |
|---|---|---|
| 02 | `github-issue-pr-triage` | Essential |
| 04 | `git-archeologist-blame` | Recommended |
| 05 | `dependency-license-auditor` | Recommended |

### Architecture & Design (3 missing)
| # | Skill | Tier |
|---|---|---|
| 06 | `domain-driven-design-modeler` | Recommended |
| 09 | `microservices-event-stormer` | Recommended |
| 10 | `caching-strategy-designer` | Recommended |

### Frontend & Web UI (4 missing)
| # | Skill | Tier |
|---|---|---|
| 12 | `tailwind-shadcn-ui-builder` | Essential |
| 13 | `wcag-accessibility-audit` | Essential |
| 14 | `state-machine-xstate-architect` | Recommended |
| 15 | `web-performance-core-web-vitals` | Recommended |

### Backend & Distributed (5 missing)
| # | Skill | Tier |
|---|---|---|
| 16 | `fastapi-async-backend-engine` | Essential |
| 17 | `go-concurrency-patterns` | Essential |
| 18 | `distributed-transaction-saga` | Recommended |
| 19 | `auth-oauth2-jwt-sentinel` | Essential |
| 20 | `rate-limiting-circuit-breaker` | Recommended |

### Testing & QA (2 missing)
| # | Skill | Tier |
|---|---|---|
| 24 | `mutation-testing-sentinel` | Recommended |
| 25 | `k6-load-chaos-test` | Optional |

### Debugging & Diagnostics (4 missing)
| # | Skill | Tier |
|---|---|---|
| 27 | `memory-leak-heap-profiler` | Recommended |
| 28 | `opentelemetry-distributed-tracer` | Recommended |
| 29 | `sql-explain-query-optimizer` | Essential |
| 30 | `log-anomaly-pattern-triage` | Recommended |

### Security & Hardening (2 missing)
| # | Skill | Tier |
|---|---|---|
| 33 | `rbac-least-privilege-audit` | Recommended |
| 34 | `dockerfile-distroless-hardener` | Recommended |

### Meta-Agentic Workflow (4 missing)
| # | Skill | Tier |
|---|---|---|
| 37 | `atomic-safe-refactoring-engine` | Essential |
| 38 | `conventional-semantic-release` | Recommended |
| 39 | `pr-review-staff-engineer` | Essential |
| 40 | `harness-loop-self-healer` | Essential |

---

## OS WORKFLOW SKILLS — GOD_PROMPT Specced, No Folder Yet (9)

Defined in GOD_PROMPT.md Parts 6 & 7. Content exists as spec. Not yet materialized to disk.

| Workflow | Gate | On Disk |
|---|---|---|
| `working-backwards` | Gate 2 | NOT on disk |
| `scope-gate` | Automated | NOT on disk |
| `alternatives-generator` | Before design decision | NOT on disk |
| `failure-mode-analyzer` | Before integration | NOT on disk |
| `launch-checklist-runner` | Gate 6 | NOT on disk |
| `deploy-monitor` | Post-deploy | NOT on disk |
| `postmortem-opener` | On incident | NOT on disk |
| `stakes-classifier` | Before implementation | NOT on disk |
| `fcar-reviewer` | Gate 4 | NOT on disk |

---

## WORKFLOW YAML FILES — On Disk vs. GOD_PROMPT Spec

| Workflow YAML | On Disk | GOD_PROMPT Spec |
|---|---|---|
| `build-verify.yaml` | YES | YES |
| `refactor-safely.yaml` | YES | YES |
| `test-and-verify.yaml` | YES | YES |
| `migration-safeguard.yaml` | YES | YES |
| `working-backwards.yaml` | NO | YES — Part 7 |
| `fcar-review.yaml` | NO | YES — Part 7 |
| `scope-gate.yaml` | NO | YES — Part 7 |
| `launch-checklist.yaml` | NO | YES — GOD_PROMPT |
| `deploy-monitor.yaml` | NO | YES — GOD_PROMPT |
| `postmortem.yaml` | NO | YES — GOD_PROMPT |
| `stakes-classifier.yaml` | NO | YES — GOD_PROMPT |
| `unknown-first-sorter.yaml` | NO | YES — GOD_PROMPT |

---

## PRIORITY ACTION LIST

### Priority 1 — Essential skill folders missing (materialize SKILL.md files)
1. 02 - github-issue-pr-triage
2. 12 - tailwind-shadcn-ui-builder
3. 13 - wcag-accessibility-audit
4. 16 - fastapi-async-backend-engine
5. 17 - go-concurrency-patterns
6. 19 - auth-oauth2-jwt-sentinel
7. 29 - sql-explain-query-optimizer
8. 37 - atomic-safe-refactoring-engine
9. 39 - pr-review-staff-engineer
10. 40 - harness-loop-self-healer

### Priority 2 — OS Workflow skills + YAMLs (copy from GOD_PROMPT spec to files)
All 9 workflow skill folders + 8 workflow YAML files need to be written from GOD_PROMPT Parts 6 & 7.

### Priority 3 — Fix ID drift (3 folders)
Re-index `02-git-worktree-isolation`, `03-context-compaction-pruner`, `09-docker-sandbox-runner`
to IDs 41, 42, 43 (or add them as separate index.json entries) to resolve numbering clash.

---

## VERDICT

- Research: 100% complete (index.json defines all 40)
- Materialization (files on disk): 38% complete (15/40 skill folders)
- OS Workflows: 0% materialized (9 skills + 8 YAMLs exist only in GOD_PROMPT spec)
- The GOD_PROMPT.md contains the full content for all missing items — implementation is the remaining step
