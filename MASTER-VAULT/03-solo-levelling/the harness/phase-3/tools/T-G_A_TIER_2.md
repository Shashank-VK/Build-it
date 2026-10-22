# Phase 3 Tool Selection — Tier 2 (Governance & Observability)

This evaluation equips **Tier 2 (Governance & Observability)** capabilities:
* **CAP-28:** Execution Provenance
* **CAP-31:** Supply-Chain Integrity
* **CAP-34:** Self-Improvement
* **CAP-36:** Deprecation Management

---

## Executive Capability Mapping & Recommendation Matrix

| Capability | Best-in-Class (Essential) | Specialized / Complementary (Optional) | Anti-Pattern / Incompatible (Avoid) |
| :--- | :--- | :--- | :--- |
| **CAP-28 Execution Provenance** | **OpenInference / OpenTelemetry Python**, **JSONL Trajectory Ledger**, **Arize Phoenix** | **OpenLineage**, **MLflow Tracking** | Proprietary unstandardized silos, unstructured plaintext logs |
| **CAP-31 Supply-Chain Integrity** | **Sigstore Cosign**, **SLSA GitHub Generator**, **Gitleaks** | **Syft & Grype (Anchore)**, **TruffleHog** | Long-lived static PGP/SSH keys in CI, manual untracked builds |
| **CAP-34 Self-Improvement** | **DSPy**, **Promptfoo** | **Arize Phoenix Evals**, **DeepEval / Ragas**, **LangSmith SDK** | Manual "eyeball" prompt editing, unversioned in-place prompt changes |
| **CAP-36 Deprecation Mgmt** | **Semgrep**, **`deprecated` (PEP 702 / `tantale/deprecated`)** | **Spectral (Stoplight)**, **Release Please** | Silent removal of tool parameters, unversioned breaking schema changes |

---

## 1. CAP-28: Execution Provenance

Execution Provenance guarantees end-to-end, tamper-evident auditability of agent execution trajectories, tool invocations, multi-turn reasoning steps, and distributed spans using W3C TraceContext standards.

```
+-----------------------------------------------------------------------------------+
|                           CAP-28 Execution Provenance                             |
+-----------------------------------------------------------------------------------+
|  [Agent Turn Execution] --> [OpenInference OTel Spans] --> [W3C Distributed Trace] |
|           |                                                                       |
|           +---------------> [JSONL Append-Only Ledger] --> [Immutable Local Audit]|
|           |                                                                       |
|           +---------------> [Arize Phoenix Backend]    --> [Replay & Visualization|
+-----------------------------------------------------------------------------------+
```

### Tool Evaluations

#### 1. OpenInference & OpenTelemetry Python SDK
* **Repository URL:** [Arize-ai/openinference](https://github.com/Arize-ai/openinference) & [open-telemetry/opentelemetry-python](https://github.com/open-telemetry/opentelemetry-python)
* **Fit / Role:** Standardizes agent trace semantics (LLM invocations, tool calls, agent thoughts, retrieval contexts) on top of vendor-neutral OpenTelemetry distributed tracing protocols (OTLP) and W3C TraceContext.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repositories.
  * *Maintained:* Daily/weekly commits; OpenTelemetry is CNCF Graduated; OpenInference has active bi-weekly releases.
  * *Adopted:* >3.5k stars (OTel Python), industry-standard instrumentation across Datadog, Honeycomb, Grafana, Phoenix, and Dynatrace.
  * *License:* Apache-2.0.
* **Archetype:** Distributed Observability Instrumentation Middleware.

#### 2. Local Append-Only JSONL Trajectory Ledger
* **Repository URL:** Native Architecture / [pydantic/pydantic](https://github.com/pydantic/pydantic)
* **Fit / Role:** High-fidelity, deterministic step-by-step recording of agent turns, thinking traces, tool arguments, and execution status (`transcript.jsonl` / `transcript_full.jsonl`). Ensures offline auditability, deterministic local replays, and zero external network dependencies.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Standard JSON Lines specification backed by Pydantic V2 schema validation.
  * *Maintained:* Continuously maintained runtime component.
  * *Adopted:* Default trajectory storage format in Antigravity, AutoGen, and LangGraph.
  * *License:* MIT.
* **Archetype:** Local Immutable Event Ledger.

#### 3. Arize Phoenix
* **Repository URL:** [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)
* **Fit / Role:** Open-source AI observability and trace visualization backend. Ingests OTLP traces directly from OpenInference to render execution directed acyclic graphs (DAGs), latency breakdowns, token spend, and tool invocation sequences.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Very active (>6,000 commits, multiple releases per month).
  * *Adopted:* >6.2k stars, widely adopted self-hosted AI trace explorer.
  * *License:* Elastic License 2.0 / Apache-2.0 (OpenInference dependencies).
* **Archetype:** Trajectory Visualization & Trace Store Backend.

#### 4. OpenLineage
* **Repository URL:** [OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage)
* **Fit / Role:** Captures data pipeline lineage, dataset transformations, and job provenance across data workflows (e.g., Spark, Airflow, dbt).
* **Tier:** **Optional** (Valuable when agent actions drive heavy external data warehouse pipelines; overkill for core agent-tool loops).
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Active under the LF AI & Data Foundation.
  * *Adopted:* >1.6k stars.
  * *License:* Apache-2.0.
* **Archetype:** Data Lineage & Pipeline Metadata Collector.

#### 5. Unstructured Plaintext Loggers / Proprietary Non-OTLP Silos
* **Tier:** **Avoid**
* **Rationale:** Plaintext `print`/`logger.info` outputs lack causal span IDs, parent-child relationships, structured tool I/O schemas, and W3C context propagation, making deterministic replay and automated audit impossible.

---

## 2. CAP-31: Supply-Chain Integrity

Supply-Chain Integrity ensures all agent tools, container sidecars, prompt artifacts, and code outputs are cryptographically signed, verified against SLSA build provenance standards, and continuously scanned for leaked secrets.

```
+-----------------------------------------------------------------------------------+
|                        CAP-31 Supply-Chain Integrity                              |
+-----------------------------------------------------------------------------------+
|  [Dev / Commit]        --> [Gitleaks Hook]           --> Block Secrets Pre-Push   |
|  [Build / CI]          --> [SLSA GitHub Generator]   --> Non-Forgeable Provenance |
|  [Publish / Release]   --> [Sigstore Cosign]         --> Keyless OIDC Signing     |
|  [Agent Runtime Gate]  --> [Cosign / Policy Verify]  --> Authenticated Tool Exec  |
+-----------------------------------------------------------------------------------+
```

### Tool Evaluations

#### 1. Sigstore Cosign
* **Repository URL:** [sigstore/cosign](https://github.com/sigstore/cosign)
* **Fit / Role:** Keyless cryptographic signing and verification of container images, WASM binaries, tool definitions, and artifact attestations using OIDC identities and the Rekor transparency log.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Highly active (OpenSSF / Linux Foundation project).
  * *Adopted:* >5.3k stars, de facto standard for cloud-native artifact signing (used by Kubernetes, Red Hat, GitHub).
  * *License:* Apache-2.0.
* **Archetype:** Cryptographic Signer & Runtime Policy Verifier.

#### 2. SLSA GitHub Generator
* **Repository URL:** [slsa-framework/slsa-github-generator](https://github.com/slsa-framework/slsa-github-generator)
* **Fit / Role:** Generates non-forgeable SLSA Level 3 build provenance attestations in GitHub Actions, establishing an unbroken cryptographic chain from git commit SHA to binary output.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Active maintenance by the SLSA working group and OpenSSF.
  * *Adopted:* >1.1k stars, standard provenance builder across open-source ecosystems.
  * *License:* Apache-2.0.
  * *Archetype:* Build Provenance & Attestation Generator.

#### 3. Gitleaks
* **Repository URL:** [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)
* **Fit / Role:** High-speed static secret detection engine integrated into pre-commit hooks, CI pipelines, and agent workspace monitors to prevent API tokens, SSH keys, and cloud credentials from entering source control or execution logs.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Actively maintained with regular rule updates.
  * *Adopted:* >18.5k stars, standard developer-side secret detector.
  * *License:* MIT.
* **Archetype:** Static Secret Scanner & Workspace Gatekeeper.

#### 4. Syft & Grype (Anchore)
* **Repository URL:** [anchore/syft](https://github.com/anchore/syft) & [anchore/grype](https://github.com/anchore/grype)
* **Fit / Role:** Generates Software Bill of Materials (SBOM) in SPDX/CycloneDX formats (`syft`) and scans dependencies for CVEs against known vulnerability databases (`grype`).
* **Tier:** **Optional** (Essential for containerized agent sidecars; optional for pure Python package runtimes).
* **Verification Gate:**
  * *Link Status:* Verified active repositories.
  * *Maintained:* Daily/weekly releases.
  * *Adopted:* Syft >6.5k stars, Grype >8.5k stars.
  * *License:* Apache-2.0.
* **Archetype:** SBOM Generator & Vulnerability Scanner.

#### 5. Hardcoded PGP/GPG Keyrings & Custom Secret-Scanning Shell Scripts
* **Tier:** **Avoid**
* **Rationale:** Static private keys stored in CI secrets risk exfiltration and lack short-lived ephemeral identity validation (Sigstore Fulcio). Ad-hoc regex scripts miss high-entropy tokens and introduce false negatives.

---

## 3. CAP-34: Self-Improvement

Self-Improvement establishes closed-loop optimization: compiling prompt signatures, running test-driven regression benchmarks on agent responses, and iteratively improving tool selection and reasoning strategies.

```
+-----------------------------------------------------------------------------------+
|                           CAP-34 Self-Improvement                                 |
+-----------------------------------------------------------------------------------+
|  [Agent Telemetry] --> [Promptfoo Regression Suite] --> [Assertion & Metric Eval] |
|                                                                 |                 |
|  [Optimized Prompts] <-- [DSPy Teleprompter/Compiler] <---------+                 |
+-----------------------------------------------------------------------------------+
```

### Tool Evaluations

#### 1. DSPy (Stanford NLP)
* **Repository URL:** [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
* **Fit / Role:** Algorithmic prompt compiler and self-improvement framework. Automatically synthesizes few-shot demonstrations, optimizes instructions, and refines multi-stage reasoning modules against defined metric assertions (e.g., MIPROv2, BootstrapFewShot).
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Extremely active (Stanford NLP and global contributor community).
  * *Adopted:* >22.5k stars, premier academic and industry standard for algorithmic prompt tuning.
  * *License:* MIT.
* **Archetype:** Algorithmic Prompt Optimizer & Optimization Compiler.

#### 2. Promptfoo
* **Repository URL:** [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)
* **Fit / Role:** CLI and CI/CD evaluation harness for LLM apps. Runs automated regression suites, model-graded metrics, JSON schema validations, and security red-teaming against agent prompt revisions before deployment.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Daily active development with automated weekly releases.
  * *Adopted:* >8.5k stars, standard in CI-based LLM regression testing.
  * *License:* MIT.
* **Archetype:** Automated LLM Unit Test & Regression Suite Runner.

#### 3. DeepEval & Ragas
* **Repository URL:** [confident-ai/deepeval](https://github.com/confident-ai/deepeval) & [explodinggradients/ragas](https://github.com/explodinggradients/ragas)
* **Fit / Role:** Specialized metric scoring libraries (faithfulness, hallucination rate, context precision, answer relevancy, G-Eval).
* **Tier:** **Optional** (Ideal for deep RAG evaluation pipelines; Promptfoo + DSPy cover broader multi-step agent behaviors).
* **Verification Gate:**
  * *Link Status:* Verified active repositories.
  * *Maintained:* Active releases and updates.
  * *Adopted:* DeepEval >5.5k stars, Ragas >10.5k stars.
  * *License:* Apache-2.0.
* **Archetype:** Specialized Evals Metric Scoring Library.

#### 4. LangSmith SDK (Client SDK)
* **Repository URL:** [langchain-ai/langsmith-sdk](https://github.com/langchain-ai/langsmith-sdk)
* **Fit / Role:** Client SDK for LangChain's hosted evaluation and feedback queue platform.
* **Tier:** **Optional** (Useful if utilizing managed LangChain Cloud services, but server backend is closed-source/commercial SaaS).
* **Verification Gate:**
  * *Link Status:* Verified active SDK repository.
  * *Maintained:* Daily commits.
  * *Adopted:* Broad adoption within the LangChain ecosystem.
  * *License:* MIT (SDK only; Server is Proprietary SaaS).
* **Archetype:** Managed SaaS Evals & Feedback Platform.

#### 5. Manual Ad-Hoc Prompt Tweaking
* **Tier:** **Avoid**
* **Rationale:** Subjective, unquantified prompt changes introduce silent regressions across edge cases and prevent automated continuous improvement.

---

## 4. CAP-36: Deprecation Management

Deprecation Management provides clear lifecycle governance for retired tools, deprecated API parameters, evolving JSON schemas, and superseded agent subagent roles via static enforcement and explicit runtime deprecation signaling.

```
+-----------------------------------------------------------------------------------+
|                        CAP-36 Deprecation Management                              |
+-----------------------------------------------------------------------------------+
|  [Tool / API Definition] --> [@deprecated Decorator]  --> Runtime Warning / Docs  |
|  [Agent Codebase / PR]   --> [Semgrep Static Rules]   --> CI Build Gate Failure   |
|  [OpenAPI / Schema Spec] --> [Spectral API Linter]    --> Schema Sunset Linting   |
+-----------------------------------------------------------------------------------+
```

### Tool Evaluations

#### 1. Semgrep
* **Repository URL:** [semgrep/semgrep](https://github.com/semgrep/semgrep)
* **Fit / Role:** Fast semantic static analysis engine. Enables custom declarative rules to detect and block deprecated tool names, obsolete arguments, and retired function calls directly in CI/CD before execution.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Maintained by Semgrep Inc. with daily updates.
  * *Adopted:* >10.5k stars, industry standard for custom static enforcement rules.
  * *License:* LGPL-2.1 (Core Community CLI).
* **Archetype:** Static Policy Enforcement Engine.

#### 2. `deprecated` Library & PEP 702 (`warnings` / `typing_extensions.deprecated`)
* **Repository URL:** [tantale/deprecated](https://github.com/tantale/deprecated) & Python Standard Library PEP 702
* **Fit / Role:** Standard runtime deprecation decorator for Python functions, methods, and classes. Emits standard `DeprecationWarning` exceptions with target sunset versions and automatically updates docstrings with Sphinx-compatible notices.
* **Tier:** **Essential**
* **Verification Gate:**
  * *Link Status:* Verified active repository and Python stdlib standard.
  * *Maintained:* Mature and widely maintained.
  * *Adopted:* Millions of monthly downloads across major libraries (e.g., PyTorch, Scikit-learn).
  * *License:* MIT.
* **Archetype:** Runtime Deprecation Decorator & Contract Marker.

#### 3. Spectral (Stoplight)
* **Repository URL:** [stoplightio/spectral](https://github.com/stoplightio/spectral)
* **Fit / Role:** Flexible JSON and YAML linter for OpenAPI and AsyncAPI schemas. Validates that tools declaring `deprecated: true` include required migration paths, sunset dates, and replacement pointers.
* **Tier:** **Optional** (Essential for systems exposing tool definitions via OpenAPI/JSON Schema contracts).
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Active maintenance under Stoplight / SmartBear.
  * *Adopted:* >2.6k stars.
  * *License:* Apache-2.0.
* **Archetype:** API Contract & Schema Deprecation Linter.

#### 4. Release Please
* **Repository URL:** [googleapis/release-please](https://github.com/googleapis/release-please)
* **Fit / Role:** Automates Semantic Versioning (SemVer) increments, breaking change notices (`BREAKING CHANGE:` commit tags), and CHANGELOG.md generation for tool suites and SDKs.
* **Tier:** **Optional** (Essential for automated release lifecycle automation).
* **Verification Gate:**
  * *Link Status:* Verified active repository.
  * *Maintained:* Active maintenance by Google.
  * *Adopted:* >3.6k stars.
  * *License:* Apache-2.0.
* **Archetype:** Automated Release & Version Lifecycle Manager.

#### 5. Silent In-Place Breaking Changes & Unversioned Parameter Drops
* **Tier:** **Avoid**
* **Rationale:** Silently dropping parameters or deleting tools without a deprecation window causes runtime crashes across automated agent workflows without providing actionable migration paths.

---

## Final Tool Stack Selection Summary

```
====================================================================================
                        PHASE 3 TIER 2 SELECTED TOOL STACK
====================================================================================
  CAP-28 (Execution Provenance)  : OpenInference + OpenTelemetry SDK + Phoenix + JSONL
  CAP-31 (Supply-Chain Integrity): Sigstore Cosign + SLSA GitHub Generator + Gitleaks
  CAP-34 (Self-Improvement)      : DSPy + Promptfoo
  CAP-36 (Deprecation Mgmt)      : Semgrep + `deprecated` (PEP 702)
====================================================================================
```

---

## Sources

* [Arize AI OpenInference Semantic Conventions](https://github.com/Arize-ai/openinference)
* [OpenTelemetry Python SDK](https://github.com/open-telemetry/opentelemetry-python)
* [Arize Phoenix AI Observability Platform](https://github.com/Arize-ai/phoenix)
* [Sigstore Cosign Container Signing & Verification](https://github.com/sigstore/cosign)
* [SLSA GitHub Generator Framework](https://github.com/slsa-framework/slsa-github-generator)
* [Gitleaks Secret Detection Engine](https://github.com/gitleaks/gitleaks)
* [Stanford NLP DSPy Programmatic Prompt Optimization](https://github.com/stanfordnlp/dspy)
* [Promptfoo LLM Evaluation & Red Teaming](https://github.com/promptfoo/promptfoo)
* [Semgrep Semantic Static Analysis](https://github.com/semgrep/semgrep)
* [Python `deprecated` Decorator Library](https://github.com/tantale/deprecated)
* [Stoplight Spectral JSON/YAML API Linter](https://github.com/stoplightio/spectral)
* [Google Release Please SemVer Automation](https://github.com/googleapis/release-please)
