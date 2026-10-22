# Independent Validation Report: Harvester Taxonomy (`ARCHETYPES_AND_CRITERIA.md`)

**Target File:** [`ARCHETYPES_AND_CRITERIA.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-0/ARCHETYPES_AND_CRITERIA.md)  
**Evaluation Scope:** 6 Canonical Archetypes (C1–C6), 10 Success Criteria (SC-01..10), and Rubric Wiring Consistency.

---

## Executive Summary & Audit Matrix

| Category | Item Count | CORRECT | PARTIAL | FABRICATED | OUTDATED |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Canonical Archetypes** | 6 | 2 | 4 | 0 | 0 |
| **2. Success Criteria** | 10 | 7 | 3 | 0 | 0 |
| **3. Rubric Wiring** | 4 sections | 3 | 1 | 0 | 0 |

---

## 1. Canonical Archetypes (C1–C6)

### C1: Product Engineering (0→1 → Scale)
- **Verdict:** `PARTIAL`
- **Evidence:** Bundles Web Apps (`R-A 01`), Backend Services (`R-A 02`), Dev Tooling/CLI/SDK (`R-A 10`), and Internal CRUD (`R-B A2`). While Web and Backend share HTTP/DB primitives, **Dev Tooling/CLI/SDK** operates across fundamentally different runtime boundaries (POSIX stdio/pipes, exit codes, distribution via package registries, zero network daemons). Additionally, treating `mobile/client` as a simple capability toggle ignores distinct build/signing toolchains (Xcode, Gradle, App Store sandboxes).
- **Specific Correction:** Restrict C1 core to Web/API SaaS. Isolate `cli-sdk` and `mobile-client` as explicit execution sub-modes requiring distinct harness smoke checks (stdio/exit-code assertions for CLI; headless emulator harnesses for mobile).

### C2: Data, Analytics & MLOps Fabric
- **Verdict:** `CORRECT`
- **Evidence:** Soundly unifies batch/streaming ETL, reverse-ETL, and MLOps under shared state invariants: data quality, schema enforcement, DAG orchestration, lineage, and reproducibility. The constraint matrix accurately models compute cost asymmetry and PII security boundaries.
- **Specific Correction:** None. Sub-mode toggles (`batch`/`streaming`/`reverse-etl` and `training` vs `inference`) maintain appropriate harness boundaries.

### C3: Automation & Browser Surface Ops
- **Verdict:** `PARTIAL`
- **Evidence:** Conflates deterministic API/webhook/iPaaS integration (`R-A 04` / `R-B A3`) with non-deterministic Headless Browser RPA (`R-A 05` / `R-B A4`). API integration features high reliability, fixed schemas, low latency, and lightweight runtimes. Browser RPA is prone to DOM shifts, bot detection, dynamic hydration, and heavy memory footprints. Forcing them into one archetype obscures radically different instrumentation needs.
- **Specific Correction:** Mandate that the `browser-surface` toggle activates dedicated DOM snapshotting, visual regression diffs, and proxy/stealth harnesses, rather than inheriting basic API retry logic.

### C4: Agentic & Knowledge Synthesis Systems
- **Verdict:** `PARTIAL`
- **Evidence:** Combines stateful, tool-using agentic loops (ReAct/crews) with read-only long-horizon research synthesis (`R-A 08` / `R-B A6`). Tool-using agents perform destructive environment mutations requiring sandboxing, loop break limits, and rollback capabilities. Read-only synthesis has zero environment mutation risk and depends entirely on citation grounding and token retrieval.
- **Specific Correction:** Split into explicit sub-archetypes: `C4-Agent` (tool execution, sandbox boundaries, mutation budget) vs `C4-Synthesis` (read-only, search/scrape, citation gate).

### C5: Platform, Infra & DevOps (IaC)
- **Verdict:** `PARTIAL`
- **Evidence:** Core IaC (Terraform, Pulumi, K8s, CI/CD) is sound with clear declarative semantics (plan/apply, drift detection). However, assigning `embedded/firmware` as a capability toggle under C5 is technically unsound. Firmware/RTOS development involves low-level systems programming (memory-mapped I/O, cross-compilers, hardware emulators), which is completely orthogonal to cloud infrastructure-as-code and CI/CD pipelines.
- **Specific Correction:** Remove `embedded/firmware` from C5. Reclassify embedded systems as an explicit non-goal or isolate into an independent hardware profile.

### C6: Migration, Modernization & Strangler Rebuild
- **Verdict:** `CORRECT`
- **Evidence:** Clearly defined with distinct constraints (AST codemods, shadow traffic capture, dual-write diffing, zero-downtime cutover safety). Cannot be subsumed by standard greenfield product engineering.
- **Specific Correction:** None.

---

## 2. Success Criteria (SC-01..10)

### SC-01: Time-to-First-Usable-Artifact (TTFUA)
- **Verdict:** `CORRECT`
- **Evidence:** OpenTelemetry span instrumentation (`run.start` → `artifact.smoke_pass` + `/health` poller) in `trace.jsonl` is objective and industry standard. P50/P95 thresholds (<90s for C1, <150s C2-C3, <180s C4) are well-calibrated.
- **Specific Correction:** Formally define the smoke-pass contract enum per archetype (e.g., HTTP 200, build exit code 0, DAG dry-run pass).

### SC-02: End-to-End Task Success Rate (TSR)
- **Verdict:** `PARTIAL`
- **Evidence:** Blends automated benchmark execution (`verdict.json`) with subjective human evaluation (`n=10 human spot-check`) without specifying arbitration rules when automated passes conflict with human spot-checks.
- **Specific Correction:** Decouple human evaluation into a calibration metric (Audit / False Positive Rate) rather than an ad-hoc component of automated TSR scoring.

### SC-03: MTTR-Step (Auto-Recovery)
- **Verdict:** `CORRECT`
- **Evidence:** Trace-driven timestamp delta (`tool.error` → `tool.success`) coupled with 10% chaos fault-injection provides an objective measure of recovery resilience. Thresholds (P50 <45s, ≥80% attempts, max 3 retries) are concrete.
- **Specific Correction:** Explicitly differentiate retryable errors (network timeouts, 429 rate limits) from deterministic failures (401 unauthorized, syntax errors) in the trace parser.

### SC-04: Human Intervention Rate (HIR)
- **Verdict:** `CORRECT`
- **Evidence:** Directly tracks discrete `human.input` and `was_blocked` trace events. Thresholds (Median 0 for C1, ≤1 for C2/C3/C5/C6, ≤2 for C4) accurately reflect autonomy targets.
- **Specific Correction:** None.

### SC-05: Cost per Successful Run (CPSR)
- **Verdict:** `CORRECT`
- **Evidence:** Comprehensive formula `(tokens×price + compute×price + API $) / successes`. LiteLLM cost ledger instrumentation is standard. Absolute dollar caps (<$0.80 C1, <$1.20 C4, <$1.50 C3-browser) prevent runaway token consumption.
- **Specific Correction:** Mandate model version pinning in the cost ledger to prevent external API pricing adjustments from skewing longitudinal benchmarks.

### SC-06: Determinism & Reproducibility Rate (DRR)
- **Verdict:** `PARTIAL`
- **Evidence:** Specifying "byte-identical" artifacts on 3x LLM replay is technically unrealistic due to non-deterministic GPU kernel float operations and timestamp injections, even with temperature 0. The fallback criteria ("diff + test pass + embedding ≥0.98") is sound.
- **Specific Correction:** Remove "byte-identical" from the requirement; anchor DRR strictly on semantic equivalence (AST diff + unit test suite pass + embedding similarity for prose).

### SC-07: Security & Secret-Handling Conformance (SSHC)
- **Verdict:** `CORRECT`
- **Evidence:** Grounded in concrete tools (`gitleaks --no-git`, egress network allowlists, 10-payload prompt injection red-teaming). Binary zero-tolerance gate ("0 leaks / 100 runs; 0 unsandboxed writes; any leak = FAIL") is appropriate.
- **Specific Correction:** None.

### SC-08: Artifact Health Gate Pass Rate (AHG)
- **Verdict:** `PARTIAL`
- **Evidence:** Standard CI validation concepts (`typecheck`, `lint`, `terraform validate`, `dbt test`). However, the instrument references `gate.sh`, which is listed as unbuilt under Open Gaps (§7 Gap 3: "Publish per-archetype gate.sh variants... due Phase 3").
- **Specific Correction:** Define default fallback CLI commands (`pytest`, `cargo check`, `ruff check`, `npm test`) for Phase 0/1 execution until custom scripts are provided.

### SC-09: Context & State Persistence Under Compaction (CSP)
- **Verdict:** `CORRECT`
- **Evidence:** Objective 40k-token synthetic probe with 5-question QA validation across compaction boundaries and cosine similarity check (>0.90). Thresholds (≥85% C4/C6, ≥75% C2) are well-calibrated.
- **Specific Correction:** None.

### SC-10: Idempotency & Drift-Free Re-run (IDFR)
- **Verdict:** `CORRECT`
- **Evidence:** Standard double-execution verification (`run; run --again`) diffing `plan.json` / `manifest.json`. 100% no-op threshold for C5 (IaC), C2 (pipelines), and C6 (shadow) matches industry convergence standards.
- **Specific Correction:** None.

---

## 3. Rubric Wiring & Internal Consistency

### 3.1 Rubric Dimension Mapping (§4.1)
- **Verdict:** `CORRECT`
- **Evidence:** Dimensions (Frequency, Harm-if-absent, Benefit, Complexity, Maintenance, Security, Generality) map logically to primary and secondary SCs with clear causal mechanisms.

### 3.2 Harm 4–5 Rule (§4.2)
- **Verdict:** `PARTIAL`
- **Evidence:** §4.2 specifies Harm 5 (SC-07, SC-03, SC-08), Harm 4 (SC-06, SC-09, SC-10), and Harm ≤2 (SC-01, SC-05). However, **SC-04 (HIR)** and **SC-02 (TSR)** are omitted from the explicit Harm hierarchy in §4.2 despite being present in Table 4.1.
- **Specific Correction:** Explicitly map SC-02 (total task failure) to Harm 5 and SC-04 (excessive manual intervention) to Harm 3.

### 3.3 Leading vs Lagging & Level Consistency (§4.3 vs §3)
- **Verdict:** `CORRECT`
- **Evidence:** SC-01, 03, 04, 05, 06, 09 are uniformly classified as Leading; SC-02, 07, 08, 10 are uniformly classified as Lagging. Harness/Project/Run levels are aligned across both sections.

### 3.4 Anti-Averaging & Trace Schema (§4.4, §4.5)
- **Verdict:** `CORRECT`
- **Evidence:** Enforces reporting of the 10th percentile (p10) bottleneck archetype to prevent masking failures with aggregate means. The `wiring.json` schema captures regressions and observed deltas cleanly.

---

## 4. Required Action Items Before Gate Approval

1. **Decouple CLI & Mobile from C1:** Retain Web/API in C1; formalize CLI and Mobile into distinct execution profile sub-modes with dedicated smoke gates.
2. **Remove Embedded from C5:** Classify firmware/RTOS as out-of-scope rather than an IaC toggle.
3. **Refactor DRR (SC-06):** Drop "byte-identical" language in favor of semantic AST and test suite equivalence.
4. **Complete Harm Rule Matrix (§4.2):** Explicitly insert SC-02 and SC-04 into the Harm classification tiers.
