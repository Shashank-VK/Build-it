---
name: repo-surveyor-map
description: Generates architectural maps, entry-point graphs, dependency topologies, and module boundaries before code modifications. Use when exploring a new codebase, analyzing system architecture, or onboarding to an unfamiliar repository.
domain: Codebase Exploration & Repo Research
version: 1.0.0
triggers:
  - "explore repo"
  - "map codebase"
  - "understand architecture"
  - "survey project"
  - "analyze repository structure"
tier: Essential
---

# Repo Surveyor & Architectural Mapping Runbook

## 1. Objective
Deterministically survey an unfamiliar or evolving codebase, extract structural hierarchy, identify runtime entrypoints and module boundaries, and generate a standardized architectural map (`REPO_MAP.md`) before proposing or executing code modifications.

This skill enforces **Class-0 (Read-Only)** isolation to guarantee zero side-effects during exploration while maintaining a tight token budget (<2,000 tokens consumed for discovery).

---

## 2. Pre-Conditions & Constraints
- **Side-Effect Classification**: Class 0 (Strictly Read-Only).
- **Tool Permissions**: `list_dir`, `view_file`, `grep_search`, `find_by_name`, `run_command` (read-only queries: `git status`, `find`, `python3`).
- **Context Hygiene**: Never dump raw recursive file listings of vendor or build directories (`node_modules`, `venv`, `target`, `dist`, `.git`).
- **Depth Bound**: Directory traversal MUST be bounded to depth $\le 3$.

---

## 3. Deterministic 5-Stage Execution Protocol

```mermaid
flowchart TD
    S1["Stage 1: Manifest & Tech Stack Detection"] --> S2["Stage 2: Bounded Directory Topology"]
    S2 --> S3["Stage 3: Entrypoint & Surface Identification"]
    S3 --> S4["Stage 4: Dependency & Boundary Extraction"]
    S4 --> S5["Stage 5: Synthesis & REPO_MAP.md Generation"]
    S5 --> V["Verification Assertions Gate"]
```

### Stage 1: Manifest & Tech Stack Detection
Scan repository root for package managers, runtime configs, and build manifests:

1. **Query primary manifests**:
   - JavaScript/TypeScript: `package.json`, `pnpm-workspace.yaml`, `turbo.json`, `tsconfig.json`
   - Python: `pyproject.toml`, `requirements.txt`, `Pipfile`, `setup.py`
   - Rust: `Cargo.toml`, `Cargo.lock`
   - Go: `go.mod`, `go.sum`
   - Java/Kotlin: `pom.xml`, `build.gradle`, `build.gradle.kts`
   - Infrastructure/Containers: `Dockerfile`, `docker-compose.yml`, `Taskfile.yml`, `Makefile`
2. **Execute manifest inspection**:
   - Extract: project name, version, runtime engines, dependencies, and test/build scripts.

### Stage 2: Bounded Directory Topology
Extract the top-level repository skeleton to depth 3 with explicit exclusions:

1. **Exclusion List**:
   ```
   .git, .github, node_modules, __pycache__, .pytest_cache, .venv, venv, 
   target, dist, build, .next, .turbo, .coverage, .harness/telemetry
   ```
2. **Deterministic Traversal Command**:
   ```bash
   python3 -c "
   import os, json
   EXCLUDES = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 'target', 'dist', 'build', '.next'}
   def tree(dir_path, depth=0, max_depth=3):
       if depth > max_depth: return
       try:
           entries = sorted(os.listdir(dir_path))
       except PermissionError: return
       for entry in entries:
           if entry in EXCLUDES or entry.startswith('.'): continue
           full_path = os.path.join(dir_path, entry)
           rel_path = os.path.relpath(full_path, '.')
           is_dir = os.path.isdir(full_path)
           print(f'{chr(32) * (depth * 2)}- {'📁 ' if is_dir else '📄 '}{entry}')
           if is_dir:
               tree(full_path, depth + 1, max_depth)
   tree('.')
   "
   ```

### Stage 3: Entrypoint & Routing Surface Identification
Locate the primary application entrypoints, HTTP routers, CLI commands, and worker jobs:

1. **Search for canonical entrypoints**:
   - Web/API: `src/index.ts`, `src/main.rs`, `main.py`, `app.py`, `server.js`, `cmd/server/main.go`, `src/app/layout.tsx`
   - CLI/Binary: `bin/`, `cli.py`, `cmd/`, `src/cli.ts`
   - Config/Lifecycle: `AGENTS.md`, `.harness/`, `Taskfile.yml`, `Makefile`
2. **Verify symbol exports and router definitions**:
   - Grep for router mounts (`FastAPI()`, `express()`, `createRouter()`, `gin.Default()`).

### Stage 4: Internal Module Dependency & AST Boundary Graph
Identify the architectural layers and inter-module import flow:

1. **Layer Classification**:
   - **Presentation / API Layer**: Controllers, Route handlers, GraphQL resolvers, UI pages.
   - **Domain / Core Business Logic**: Entities, Services, Use-cases, State machines.
   - **Data Access / Persistence**: ORM models, Repositories, Migrations, DB schemas.
   - **Cross-Cutting & Infrastructure**: Auth middleware, Logging, Metrics, Utilities, Harness config.
2. **Boundary Validation**:
   - Verify that Presentation depends on Domain, and Data Access implements Domain interfaces (Dependency Inversion principle).

### Stage 5: Architectural Synthesis & `REPO_MAP.md` Generation
Synthesize the extracted intelligence into a standardized, token-efficient repository map.

---

## 4. Standardized Output Schema (`REPO_MAP.md`)

When executing this skill, output or persist the survey in the following exact format:

```markdown
# Repository Architectural Map: <Project Name>

> **Date:** <YYYY-MM-DD> | **Repository Type:** <Monorepo / Single Package / CLI / Service>
> **Primary Stack:** <Language + Framework + Database + Build System>

---

## 1. High-Level System Topology
```mermaid
graph TD
    Client["Clients / Consumers"] --> Gateway["API / Presentation Layer"]
    Gateway --> Domain["Core Business Logic / Services"]
    Domain --> Data["Data Access & Storage"]
    Domain --> Ext["External Services / Integrations"]
```

## 2. Directory Hierarchy & Responsibilities
| Path | Layer / Responsibility | Key Technologies |
| :--- | :--- | :--- |
| `src/api/` | REST / GraphQL endpoints | FastAPI, Pydantic |
| `src/core/` | Domain logic & orchestrators | Pure Python, Asyncio |
| `src/db/` | Schemas, models & migrations | PostgreSQL, Alembic |
| `tests/` | Unit, integration & E2E suites| Pytest, Testcontainers |

## 3. Runtime Entrypoints & Control Flow
- **API Server Entrypoint**: `src/main.py:app` (Runs via `uvicorn src.main:app`)
- **CLI Entrypoint**: `src/cli.py` (`cli_main()`)
- **Worker / Background Queue**: `src/workers/task_consumer.py`

## 4. Invariants & Safe Modification Zones
- 🟢 **Safe for Feature Additions**: `src/services/`, `src/api/v1/`, `tests/`
- 🟡 **Requires Care (Shared Contracts)**: `src/models/`, `src/core/interfaces/`
- 🔴 **Restricted (Requires Explicit Review)**: `.harness/`, `migrations/`, `auth/`

## 5. Verification & Test Commands
- **Lint & Format**: `<command, e.g. ruff check .>`
- **Typecheck**: `<command, e.g. mypy --strict .>`
- **Fast Test Suite**: `<command, e.g. pytest tests/unit -q>`
- **Full Regression**: `<command, e.g. pytest tests/ -v>`
```

---

## 5. Verification Assertions & Exit Criteria

Before declaring the repo survey complete, assert that all four verification criteria are satisfied:

1. **[Assertion VA-01: Runtime Stack Identified]**: Primary runtime, package manager, and test runner are explicitly identified with exact configuration file references.
2. **[Assertion VA-02: Zero Unbounded File Dumps]**: No directory dumps exceeding depth 3 or containing vendor directories exist in the output.
3. **[Assertion VA-03: Canonical Entrypoint Resolved]**: At least 1 verified entrypoint file path exists and is confirmed via `view_file` or `grep_search`.
4. **[Assertion VA-04: Test Execution Verified]**: The exact command line required to run tests is documented and verified against existing project manifests.

---

## 6. Anti-Patterns to Avoid

| Anti-Pattern | Bad Agent Action | Correct Skill Behavior |
| :--- | :--- | :--- |
| **Context Flooding** | Running `find .` or `ls -R` and dumping 50,000 lines into context. | Run bounded Python tree scanner with strict exclusion set. |
| **Hallucinated Frameworks** | Assuming Next.js or Django without checking `package.json` or `pyproject.toml`. | Inspect root manifests in Stage 1 before hypothesizing architecture. |
| **Unanchored File Edits** | Modifying files before understanding module dependencies. | Identify invariants and Safe Modification Zones before planning edits. |
| **Blind Test Invocations** | Guessing `npm test` when the repo uses `pnpm test` or `cargo test`. | Read manifest scripts to extract exact verified test commands. |
