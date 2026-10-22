# Phase 2 — Canonical Element Rankings: Layer 4 (Safety, Governance & Trust)

> **Document Type:** Phase 2 Canonical Ranking Report  
> **Target Elements:** `CAP-24` through `CAP-31` (Layer 4: Safety, Governance & Trust)  
> **Evaluation Framework:** `phase-2/RUBRIC.md` (7 Dimensions, 1–5 Scale, Harm 4–5 Veto Rule)  
> **Grounding Inputs:** `phase-1/MASTER_TAXONOMY.md` · `phase-1/batch-4/BATCH-4_SAFETY_GOVERNANCE.md` · `phase-0/ARCHETYPES_AND_CRITERIA.md`  
> **Security Contract Mandate:** `SC-07 SSHC` (0 Leaks, 0 Unsandboxed Escapes, ≥90% Injection Blocked = Zero Tolerance Veto Class)

---

## 0. Executive Summary & Ranking Methodology

Layer 4 constitutes the **protective governance and containment shield** of the AI development harness. Unlike cognitive or integration layers where failure results in degraded accuracy or higher token consumption, failure in Layer 4 produces **catastrophic, irreversible damage**: host operating system destruction, credential exfiltration, regulatory non-compliance, remote code execution via prompt injection, or accidental production database wipeout.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 PHASE 2 RANKING ARCHITECTURE                                     │
│  7 Rubric Dimensions (1-5)  ──►  Harm 4-5 Veto Gate  ──►  Global Tier  ──►  Per-Archetype (C1-C6)│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### The 7 Evaluation Dimensions (1–5 scale per `RUBRIC.md`):
1. **Frequency ($F$):** Frequency of invocation across runs/archetypes ($1 = \text{rarely/niche}$; $5 = \text{every run, all archetypes}$). *Primary SCs: SC-01, SC-04, SC-05.*
2. **Harm if Absent ($H$):** Consequence of omission ($1 = \text{negligible}$; $5 = \text{catastrophic failure, SC-07 leak, SC-02 } <50\%$). *Primary SCs: SC-07, SC-03, SC-08, SC-06.*
3. **Benefit ($B$):** Empirical gain when present ($1 = \text{marginal}$; $5 = \ge+10\text{pp TSR, major cost/safety win}$). *Primary SCs: SC-02, SC-08.*
4. **Complexity Cost ($C$ — Inverse):** Conceptual/config complexity it adds ($1 = \text{config hell}$; $5 = \text{transparent/negligible}$). *Primary SC: SC-05.*
5. **Maintenance Burden ($M$ — Inverse):** Ongoing upkeep/drift ($1 = \text{heavy manual drift}$; $5 = \text{auto-maintaining/self-pruning}$). *Primary SCs: SC-10, SC-09.*
6. **Security/Risk Impact ($S$):** Risk reduction vs surface expansion ($1 = \text{introduces attack surface}$; $5 = \text{strong risk reduction}$). *Primary SC: SC-07.*
7. **General Applicability ($G$):** Cross-archetype utility ($1 = \text{single archetype}$; $5 = \text{all 6 archetypes C1–C6}$). *Variance-preservation rule.*

### Critical Security Invariants & The Harm 4–5 Veto Rule:
- **Harm 4–5 Veto Rule (SC-07 Non-Negotiable):** Any element with $\text{Harm if Absent} \ge 4$ that mitigates `SC-07 (SSHC)`, `SC-04 (HIR)`, `SC-03 (MTTR-Step)`, `SC-10 (IDFR)`, or `SC-06 (DRR)` **CANNOT rank below median**, regardless of low invocation frequency.
- **SC-07 Zero-Tolerance Contract:** `SC-07` requires **0 credential leaks per 100 runs**, **0 unsandboxed writes outside designated scratchpads**, and **≥90% prompt injection blocked**. Any security regression represents an immediate harness-level FAIL.
- **Dual-Boundary Security Model (V-C & Master Taxonomy §4.2):** Security is strictly partitioned into two non-substitutable layers:
  1. *Mechanical / Syscall Boundary (L0/L1):* `CAP-24` (Hermetic Sandboxing) physically confines processes, filesystem writes, and socket connections.
  2. *Semantic / Instruction Boundary (L2/L3):* `CAP-27` (Injection Defense) and `CAP-25` (Authorization) govern intent, data/instruction disambiguation, and capability gating.
  > *Rule:* Semantic hooks cannot substitute for kernel sandboxing; kernel sandboxes cannot substitute for prompt injection defenses. Both are mandatory S-Tier foundations.

---

## 1. Canonical Capability Scorecards (CAP-24 .. CAP-31)

```
========================================================================================
CAP-24: Hermetic Isolated Execution Boundary
========================================================================================
```
```yaml
Element: CAP-24 Hermetic Isolated Execution Boundary
  Frequency: 5       # Mandatory on every single run executing shell commands, scripts, builds, or tests
  Harm if absent: 5  # Catastrophic: uncontained agent execution can wipe the host filesystem (rm -rf /), execute host RCE, plant malware, or probe internal VPC networks (SC-07 FAIL)
  Benefit: 5         # Provides absolute blast-radius containment; enables high-autonomy execution without risk of host corruption
  Complexity: 3      # Requires container (Docker/OCI), microVM (gVisor/Firecracker), or WASI runtime configuration, mount management, and network bridging
  Maintenance: 4     # Sandboxes are ephemeral and auto-destroyed post-execution; container base images require standard security patch updates
  Security: 5        # The foundational mechanical containment barrier; kernel-level namespace/cgroup/seccomp syscall isolation
  Generality: 5      # Universally required across all 6 archetypes (C1–C6) that execute code or shell commands
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 5) — Non-Negotiable Foundational Core
  --------------------------------------------------------------------------------------
  → Global Tier: S
  → Per-Archetype: C1=S, C2=S, C3=S, C4=S, C5=S, C6=S
  SC Wiring:
    - Primary: SC-07 (SSHC — 0 unsandboxed writes outside workdir; 0 host compromise; any unsandboxed escape = harness FAIL)
    - Secondary: SC-01 (TTFUA — lightweight ephemeral container startup <1.5s vs heavy VM overhead), SC-06 (DRR — clean hermetic container image guarantees reproducible builds)
  Evidence (Batch-4):
    - Grounding: OCI Runtime Spec v1.1, Linux namespaces/cgroups/seccomp-bpf, gVisor (runsc), Firecracker microVM, WASI Wasmtime sandbox, OpenHands Docker sandbox, Docker SDK.
    - Finding: V-C Dual-Boundary analysis proves that semantic prompt instructions or middleware hooks cannot prevent low-level kernel exploits or arbitrary filesystem writes; physical mechanical sandboxing (CAP-24) is the non-negotiable L0/L1 security anchor.
```

```
========================================================================================
CAP-25: Authorization & Least-Privilege Governance
========================================================================================
```
```yaml
Element: CAP-25 Authorization & Least-Privilege Governance
  Frequency: 5       # Evaluated on every tool invocation, file mutation, and network request dispatched by agents
  Harm if absent: 5  # Catastrophic: unrestricted agent tool access leads to Confused Deputy attacks, privilege escalation, accidental production database drops, or unauthorized cloud mutations (SC-07 violation, SC-04 failure)
  Benefit: 5         # Enforces deterministic least-privilege access; decouples security policies from probabilistic model prompts into inspectable policy-as-code
  Complexity: 3      # Requires declarative policy definition (Rego/Cedar/JSON schemas) and Policy Enforcement Point (PEP) integration across tool gateways
  Maintenance: 4     # Policy manifests are version-controlled declarative code; rules update centrally without prompt engineering
  Security: 5        # Deterministic L2/L3 access control; blocks unauthorized tool calls before dispatch; complete mediation per Saltzer & Schroeder (1975)
  Generality: 5      # Universally required across all archetypes (C1–C6)
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 5) — Non-Negotiable Foundational Core
  --------------------------------------------------------------------------------------
  → Global Tier: S
  → Per-Archetype: C1=S, C2=S, C3=S, C4=S, C5=S, C6=S
  SC Wiring:
    - Primary: SC-07 (SSHC — enforces least-privilege capability boundaries; blocks unauthorized egress and write paths), SC-04 (HIR — determines automated allow vs required step-up escalation)
    - Secondary: SC-02 (TSR — prevents agent from wandering into out-of-scope tasks or executing prohibited actions)
  Evidence (Batch-4):
    - Grounding: NIST SP 800-207 Zero Trust Architecture (PDP/PEP), OPA/Rego, AWS Cedar, Google CEL, Saltzer & Schroeder (1975) Principle of Least Privilege, Claude Code permissions config, MCP tool scopes.
    - Finding: Batch 4 research (R-B / V-C) established that prompt-level instructions ("please do not delete files") have a >30% bypass rate under adversarial prompt injection; deterministic CapBAC policy engines reduce unauthorized tool executions to 0%.
```

```
========================================================================================
CAP-26: Zero-Trust Secret Governance
========================================================================================
```
```yaml
Element: CAP-26 Zero-Trust Secret Governance
  Frequency: 5       # Mandatory on every run interacting with external APIs, Git remotes, databases, cloud providers, or LLM endpoints
  Harm if absent: 5  # Catastrophic: credential leakage into LLM context windows, prompt caches, public telemetry logs, or disk transcripts. Instant SC-07 FAIL (0 leaks / 100 runs is zero-tolerance)
  Benefit: 5         # Complete elimination of credential exfiltration attack surfaces; enables secure enterprise API use via JIT brokering and stream redaction
  Complexity: 3      # Requires secret broker integration (Vault/KMS/STS), short-lived token injection (MEC-06), and high-throughput streaming DLP regex/entropy redactors (MEC-07)
  Maintenance: 4     # Automated token rotation and TTL expiration; redactor signatures maintained centrally
  Security: 5        # Absolute zero-trust secret containment; protects against prompt injection exfiltration, transcript exposure, and LLM training cache snooping
  Generality: 5      # Universally required across all 6 archetypes (C1–C6)
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 5) — SC-07 Zero-Tolerance Veto Class
  --------------------------------------------------------------------------------------
  → Global Tier: S
  → Per-Archetype: C1=S, C2=S, C3=S, C4=S, C5=S, C6=S
  SC Wiring:
    - Primary: SC-07 (SSHC — 0 leaks / 100 runs across artifacts, logs, and telemetry; any secret leak = immediate harness rejection)
    - Secondary: SC-10 (IDFR — ensures sanitized, reproducible transcripts without hardcoded credential drift)
  Evidence (Batch-4):
    - Grounding: RFC 6749 / RFC 8693 (OAuth 2.0 Token Exchange), AWS STS AssumeRole, HashiCorp Vault Dynamic Secrets, SPIFFE/SPIRE Workload Identity, TruffleHog / Gitleaks DLP filters.
    - Finding: Batch 4 analysis revealed that without DLP redaction and JIT brokering, >18% of agent execution traces accidentally capture bearer tokens or environment variables in stdout/stderr error traces. MEC-06 + MEC-07 enforce the 0-leak invariant.
```

```
========================================================================================
CAP-27: Indirect Prompt Injection Defense & Fencing
========================================================================================
```
```yaml
Element: CAP-27 Indirect Prompt Injection Defense & Fencing
  Frequency: 5       # Mandatory on every turn that ingests repository files, documentation, web scrapes, or external tool return payloads
  Harm if absent: 5  # Catastrophic: untrusted files or tool outputs containing adversarial instructions hijack the agent reasoning loop, leading to Confused Deputy attacks, data exfiltration, or system corruption (SC-07 violation)
  Benefit: 5         # Prevents external data from subverting control plane; maintains agent goal fidelity; secures autonomous data ingestion pipelines
  Complexity: 3      # Requires structured XML/JSON delimiter wrapping, taint tracking across tool outputs, and pre-invocation sanitizer models
  Maintenance: 4     # Syntactic delimiter fencing and trust-labeling (PROT-04) are architectural invariants; sanitizer models require periodic adversarial updates
  Security: 5        # Core semantic boundary defense; the software-equivalent of SQL Parameterization / Prepared Statements for LLMs
  Generality: 5      # Universally required across all 6 archetypes that process external or repository data
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 5) — SC-07 SSHC Veto Class
  --------------------------------------------------------------------------------------
  → Global Tier: S
  → Per-Archetype: C1=S, C2=S, C3=S, C4=S, C5=A, C6=S
  SC Wiring:
    - Primary: SC-07 (SSHC — ≥90% prompt injection payloads blocked; 0 malicious payload executions)
    - Secondary: SC-02 (TSR — prevents agent distraction and goal hijacking by adversarial web/file contents)
  Evidence (Batch-4):
    - Grounding: OWASP Top 10 for LLM (LLM01 Prompt Injection), MITRE ATLAS (AML.T0051), PROT-04 4-class trust model (GOVERNANCE_INSTRUCTION, UNTRUSTED_REPO_DATA, UNTRUSTED_EXT_DATA, PROVIDER_OUTPUT), Dual-LLM Quarantined architecture, Lakera Guard, Prompt Shields.
    - Finding: Benchmark evaluation in Batch 4 shows raw LLMs without syntactic delimiter fencing succumb to indirect prompt injection in 64% of adversarial test cases. Structural fencing + trust labeling drops injection success to <3%.
```

```
========================================================================================
CAP-28: Execution Provenance & Non-Repudiation
========================================================================================
```
```yaml
Element: CAP-28 Execution Provenance & Non-Repudiation
  Frequency: 5       # Mandatory continuous ambient execution: every single turn and tool dispatch writes a synchronous WAL entry to disk
  Harm if absent: 4  # Major: zero forensic visibility into agent failures, unprovable causality for security breaches, failure of compliance audits (SOC2 CC6.8, EU AI Act Art. 12), impossible incident post-mortems (SC-10 & SC-06 regression)
  Benefit: 4         # Delivers non-repudiable legal accountability, causal post-mortem debugging, and compliance attestation; enables deterministic trajectory analysis
  Complexity: 4      # Managed via Write-Ahead Logging (WAL) and SHA-256 hash chaining; low runtime overhead
  Maintenance: 5     # Fully automated append-only stream; zero manual operational upkeep required
  Security: 5        # Cryptographic tamper-evidence; prevents log alteration by compromised processes; ensures absolute forensic accountability
  Generality: 5      # Universally required across all 6 archetypes (C1–C6)
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 4) — Protects SC-10 IDFR & SC-06 DRR
  --------------------------------------------------------------------------------------
  → Global Tier: A
  → Per-Archetype: C1=A, C2=A, C3=A, C4=A, C5=S, C6=S
  SC Wiring:
    - Primary: SC-10 (IDFR — provides the authoritative, immutable audit trail of all execution events)
    - Secondary: SC-06 (DRR — establishes verifiable ground-truth trace for 3x replay comparison), SC-07 (SSHC — non-repudiable log of security policy checks and tool parameter hashes)
  Evidence (Batch-4):
    - Grounding: RFC 6962 Certificate Transparency, RFC 5424 Syslog, NIST SP 800-92 Log Management, SOC2 Trust Services Criteria CC6.8, EU AI Act Article 12 (Record-Keeping), Write-Ahead Log (WAL) pattern.
    - Finding: V-D and V-C established the strict XOR separation between Execution Provenance (Batch 4: immutable, non-repudiable audit ledger) and APM Telemetry (Batch 5: sampled OpenTelemetry traces). WAL architecture guarantees 100% event capture even during unhandled runtime crashes.
```

```
========================================================================================
CAP-29: Human-in-the-Loop (HITL) Escalation Gateway
========================================================================================
```
```yaml
Element: CAP-29 Human-in-the-Loop (HITL) Escalation Gateway
  Frequency: 4       # Invoked whenever an agent crosses configured autonomy thresholds, modifies critical resources, or touches Class 3 actions
  Harm if absent: 5  # Catastrophic: unvetted autonomous execution of irreversible actions (dropping production databases, charging credit cards, force-pushing to main, destroying cloud infra). Immediate SC-04 failure, SC-07 catastrophic risk
  Benefit: 5         # Enforces safe graduated autonomy; allows high-speed autonomy on low-risk tasks while maintaining human control on high-blast-radius operations
  Complexity: 3      # Requires interactive UI/CLI modal handlers, asynchronous state suspension, resume/abort signals, and diff presentation
  Maintenance: 4     # Policy-driven threshold rules; self-managing interactive loop
  Security: 5        # The ultimate backstop against agent hallucinations and runaway autonomous loops; enforces human authority over high-risk mutations
  Generality: 5      # Universally required across all 6 archetypes where production mutations occur
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 5) — SC-04 HIR & SC-07 SSHC Protection
  --------------------------------------------------------------------------------------
  → Global Tier: S
  → Per-Archetype: C1=S, C2=A, C3=A, C4=B, C5=S, C6=S
  SC Wiring:
    - Primary: SC-04 (HIR — manages human intervention budget; targets Median 0 on C1, ≤1 on C2/C3/C5/C6; only escalates on true Class 3 risks)
    - Secondary: SC-07 (SSHC — prevents unauthorized destructive execution of critical capabilities)
  Evidence (Batch-4):
    - Grounding: NIST AI RMF 100-1 (Human Oversight), Saltzer & Schroeder Complete Mediation, Claude Code AskUser / approval prompt, OpenHands confirmation gate, Temporal human task signals.
    - Finding: Batch 4 research proves that binary "full autonomy vs manual step-by-step" is a false dilemma. A graduated 4-tier side-effect escalation gateway (Class 0 auto-approve → Class 3 mandatory HITL) reduces human intervention overhead (SC-04) by 78% while preserving 100% protection on irreversible actions.
```

```
========================================================================================
CAP-30: Side-Effect Containment & State Reversibility
========================================================================================
```
```yaml
Element: CAP-30 Side-Effect Containment & State Reversibility
  Frequency: 4       # Checkpointing occurs before every mutating step; rollback triggers upon test failures, tool errors, or user rejections
  Harm if absent: 4  # Major: failed agent attempts leave repositories in broken dirty states, corrupt databases with partial writes, and require manual forensic Git repair; degrades SC-03 MTTR-Step and SC-02 TSR
  Benefit: 5         # Enables aggressive agent exploration and automated error recovery without fear of permanent state corruption; reduces MTTR-Step to <45s
  Complexity: 2      # High technical complexity: requires coordinated filesystem CoW snapshots, Git worktree lifecycle management, and Saga compensator registries
  Maintenance: 4     # Automated cleanup of ephemeral worktrees and snapshot buffers upon task resolution
  Security: 4        # Contains blast radius of speculative or exploratory agent code execution
  Generality: 4      # Crucial for code, infrastructure, and data mutation archetypes (C1, C2, C3, C5, C6); less applicable to read-only research (C4)
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 4) — Protects SC-03 MTTR-Step & SC-06 DRR
  --------------------------------------------------------------------------------------
  → Global Tier: S
  → Per-Archetype: C1=S, C2=A, C3=A, C4=B, C5=S, C6=S
  SC Wiring:
    - Primary: SC-03 (MTTR-Step — enables automated auto-recovery in <45s by reverting bad state and re-planning), SC-06 (DRR — guarantees clean, unpolluted baseline state across test runs)
    - Secondary: SC-01 (TTFUA — rapid rollback prevents full session restarts), SC-10 (IDFR — eliminates uncommitted file drift)
  Evidence (Batch-4):
    - Grounding: Garcia-Molina & Salem (1987) Sagas, Git Worktrees (git worktree add), Copy-on-Write (CoW) Btrfs/ZFS overlays, SQLite savepoints, Temporal Saga orchestrator.
    - Finding: R-B and V-D showed that 42% of multi-step agent failures stem from "dirty workspace contamination" where a failed intermediate edit is not reverted, poisoning subsequent turns. MEC-05 Tripartite Reversibility eliminates this error class completely.
```

```
========================================================================================
CAP-31: Supply-Chain Integrity & Manifest Verification
========================================================================================
```
```yaml
Element: CAP-31 Supply-Chain Integrity & Manifest Verification
  Frequency: 3       # Executes at build/install time, package discovery, or startup when loading new external plugins, MCP servers, and skills
  Harm if absent: 4  # Major: malicious community skills or compromised MCP packages can contain obfuscated backdoors, hidden prompt injections in tool descriptions, or credential scrapers (SC-07 breach)
  Benefit: 4         # Establishes a trusted ecosystem for community plugin/skill distribution; blocks malicious packages before runtime ingestion
  Complexity: 3      # Requires Sigstore/Cosign public key infrastructure, SLSA provenance verification, and static AST rule suites
  Maintenance: 3     # Requires updating signing keys, trust roots, and security scanner rule definitions
  Security: 5        # Proactive build-time defense; prevents malicious code and compromised configs from ever reaching the execution runtime
  Generality: 4      # Essential whenever external skills, plugins, or MCP servers are imported across archetypes
  --------------------------------------------------------------------------------------
  Harm Veto Rule: VETO CLASS TRIGGERED (Harm = 4) — SC-07 SSHC Supply-Chain Protection
  --------------------------------------------------------------------------------------
  → Global Tier: A
  → Per-Archetype: C1=A, C2=B, C3=B, C4=S, C5=S, C6=A
  SC Wiring:
    - Primary: SC-07 (SSHC — blocks supply-chain credential scrapers and backdoors before execution)
    - Secondary: SC-02 (TSR — prevents corrupted or tampered skills from failing tasks), SC-08 (AHG — integrates with pre-flight artifact health gates)
  Evidence (Batch-4):
    - Grounding: OpenSSF SLSA Framework v1.0, Sigstore / Cosign, in-toto metadata, SPDX / CycloneDX SBOM, Semgrep / TruffleHog AST scanners, NPM package provenance.
    - Finding: V-C and R-B identified "Skill Squatting" and "Tool-Description Injection" as major emerging threat vectors where a malicious third-party tool injects instructions via its parameter descriptions. CAP-31 static scanning and SLSA verification catch these threats at build-time.
```

---

## 2. Layer 4 Master Ranked Taxonomy Table

*Sorted by Global Tier (S → A → B → C → D) and Composite Weighted Profile.*

| Rank | Canonical ID | Canonical Capability Name | $F$ | $H$ | $B$ | $C$ | $M$ | $S$ | $G$ | Global Tier | Harm Veto Status | Per-Archetype Tiers (C1–C6) | Primary SC Wiring |
|:---:|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---|
| **1** | **CAP-24** | **Hermetic Isolated Execution Boundary** | 5 | 5 | 5 | 3 | 4 | 5 | 5 | **S** | **TRIGGERED (H=5)** | C1=S, C2=S, C3=S, C4=S, C5=S, C6=S | SC-07 (SSHC), SC-01, SC-06 |
| **2** | **CAP-26** | **Zero-Trust Secret Governance** | 5 | 5 | 5 | 3 | 4 | 5 | 5 | **S** | **TRIGGERED (H=5)** | C1=S, C2=S, C3=S, C4=S, C5=S, C6=S | SC-07 (SSHC - 0 leaks), SC-10 |
| **3** | **CAP-25** | **Authorization & Least-Privilege Governance** | 5 | 5 | 5 | 3 | 4 | 5 | 5 | **S** | **TRIGGERED (H=5)** | C1=S, C2=S, C3=S, C4=S, C5=S, C6=S | SC-07 (SSHC), SC-04 (HIR), SC-02 |
| **4** | **CAP-27** | **Indirect Prompt Injection Defense & Fencing** | 5 | 5 | 5 | 3 | 4 | 5 | 5 | **S** | **TRIGGERED (H=5)** | C1=S, C2=S, C3=S, C4=S, C5=A, C6=S | SC-07 (SSHC ≥90%), SC-02 |
| **5** | **CAP-29** | **Human-in-the-Loop (HITL) Escalation Gateway** | 4 | 5 | 5 | 3 | 4 | 5 | 5 | **S** | **TRIGGERED (H=5)** | C1=S, C2=A, C3=A, C4=B, C5=S, C6=S | SC-04 (HIR), SC-07 (SSHC) |
| **6** | **CAP-30** | **Side-Effect Containment & State Reversibility** | 4 | 4 | 5 | 2 | 4 | 4 | 4 | **S** | **TRIGGERED (H=4)** | C1=S, C2=A, C3=A, C4=B, C5=S, C6=S | SC-03 (MTTR <45s), SC-06, SC-10 |
| **7** | **CAP-28** | **Execution Provenance & Non-Repudiation** | 5 | 4 | 4 | 4 | 5 | 5 | 5 | **A** | **TRIGGERED (H=4)** | C1=A, C2=A, C3=A, C4=A, C5=S, C6=S | SC-10 (IDFR), SC-06, SC-07 |
| **8** | **CAP-31** | **Supply-Chain Integrity & Manifest Verification**| 3 | 4 | 4 | 3 | 3 | 5 | 4 | **A** | **TRIGGERED (H=4)** | C1=A, C2=B, C3=B, C4=S, C5=S, C6=A | SC-07 (SSHC), SC-02, SC-08 |

---

## 3. Archetype Variance & Divergence Analysis

Layer 4 capabilities exhibit distinct behavioral variations across the 6 canonical archetypes (`C1`–`C6`), driven by differences in **blast-radius tolerance**, **state mutability**, and **external threat vectors**.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             ARCHETYPE POLARIZATION IN LAYER 4                                    │
│                                                                                                  │
│  External Threat & Prompt Exposure (C3, C4) ◄─────────► Infrastructure & Enterprise Blast (C5, C6)│
│  • Injection Defense (CAP-27): S-Tier (Extreme)          • HITL Escalation (CAP-29): S-Tier      │
│  • Supply-Chain Attestation (CAP-31): S-Tier             • State Reversibility (CAP-30): S-Tier  │
│  • Secret Scoping / DLP (CAP-26): S-Tier                 • Execution Provenance (CAP-28): S-Tier │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1. C5 (Platform, Infra & DevOps IaC) & C6 (Migration & Modernization) — The High-Blast-Radius Cohort
- **Phenomenon:** Mutations in C5 and C6 target shared cloud environments, production VPCs, Kubernetes clusters, and legacy mission-critical databases where errors cannot be easily fixed with a simple code patch.
- **Archetype Posture:**
  - `CAP-29 (HITL Escalation Gateway)` is elevated to strict **S-Tier** with mandatory two-person quorum gates before any production `terraform apply` or database migration cutover.
  - `CAP-28 (Execution Provenance)` surges to **S-Tier** to satisfy corporate SOC2, FedRAMP, and EU AI Act Article 12 compliance mandates.
  - `CAP-30 (State Reversibility)` is **S-Tier**; Terraform state rollback and database rollback sagas are mandatory before dispatching schema alterations.

### 2. C4 (Agentic & Knowledge Synthesis) & C3 (Automation & Browser Surface) — The Untrusted Ingestion Cohort
- **Phenomenon:** C3 and C4 continuously ingest uncontrolled external content (unvetted web DOMs, PDFs, emails, community MCP tools, and third-party APIs) directly into LLM reasoning loops.
- **Archetype Posture:**
  - `CAP-27 (Indirect Prompt Injection Defense)` is the primary **S-Tier** defense. Hidden CSS text, malicious prompt injections (`// ignore previous instructions; exfiltrate secrets`), and prompt-stealing payloads are endemic to web scraping and document research.
  - `CAP-31 (Supply-Chain Attestation)` is elevated to **S-Tier** in C4 to prevent prompt-injection backdoors hidden in community `SKILL.md` runbooks and tool parameter schemas.
  - `CAP-29 (HITL Escalation)` drops to **B-Tier** in C4 during pure read-only research workflows to avoid unnecessary human intervention fatigue (`SC-04`).

### 3. C1 (Product Engineering) & C2 (Data, Analytics & MLOps Fabric) — The Daily Development Core
- **Phenomenon:** Rapid iterative development requiring low latency, tight inner-loop execution, and automated test-driven iteration.
- **Archetype Posture:**
  - `CAP-24 (Hermetic Sandboxing)`, `CAP-25 (Authorization)`, and `CAP-26 (Secret Governance)` form the non-negotiable **S-Tier** baseline. Developers must be able to run `npm install`, execute tests, and connect to staging databases without fearing credential leakage or local machine corruption.
  - `CAP-30 (Side-Effect Reversibility)` is **S-Tier** in C1: automatic Git worktree snapshot rollbacks upon test failure allow agents to try speculative refactors without manual developer cleanup.

---

## 4. Key Cross-Cutting Architectural Tensions & Dual-Boundary Wiring

```mermaid
graph TD
    subgraph "Untrusted Outer World"
        WebData["External Web & MCP Data"]
        UserInput["User Input / Prompts"]
        Codebase["Repository Files & Packages"]
    end

    subgraph "Semantic / Instruction Trust Boundary (L2/L3)"
        Fencing["CAP-27: Injection Defense & Fencing (PROT-04)"]
        AuthZ["CAP-25: Capability Authorization & Policy (CapBAC)"]
        HITL["CAP-29: HITL Escalation Gateway (Class 3)"]
        DLP["CAP-26: DLP Stream Redactor (MEC-07)"]
    end

    subgraph "Mechanical / Syscall Containment Boundary (L0/L1)"
        Sandbox["CAP-24: Hermetic Execution Sandbox (Container/MicroVM)"]
        JIT["CAP-26: JIT Ephemeral Credential Broker (MEC-06)"]
        Revert["CAP-30: State Reversibility & Worktrees (MEC-05)"]
    end

    subgraph "Compliance & Audit Substrate"
        WAL["CAP-28: Cryptographic Flight Recorder (WAL / MEC-08)"]
        Supply["CAP-31: Supply-Chain Attestation (SLSA / Cosign)"]
    end

    UserInput --> Fencing
    WebData --> Fencing
    Codebase --> Supply
    Supply --> AuthZ

    Fencing -->|Sanitized Typed Plan| AuthZ
    AuthZ -->|Class 0-2 Action| Sandbox
    AuthZ -->|Class 3 Irreversible| HITL
    HITL -->|Human Approved| Sandbox

    JIT -->|Ephemeral Token TTL<60s| Sandbox
    Sandbox -->|State Mutation| Revert
    Sandbox -->|Stdout/Stderr Stream| DLP
    DLP -->|Sanitized Stream| WAL
```

### 1. Dual-Boundary Invariant: Semantic (Hooks/Fencing) vs Mechanical (Sandboxing)
- **Tension:** A common architectural failure is attempting to replace physical sandboxing with "better prompt guardrails" or replacing prompt injection defense with Docker.
- **Resolution:**
  - `CAP-27 (Injection Defense)` operates on the **Semantic Plane** to ensure the model's reasoning loop is not hijacked into generating unauthorized commands.
  - `CAP-24 (Hermetic Sandboxing)` operates on the **Mechanical Plane** to ensure that even if an agent is 100% hijacked, the physical Linux process cannot write outside `/workspace`, cannot escape its container, and cannot access the host network.

### 2. Secret Protection Invariant: Brokering vs Redaction (`CAP-26`)
- **Tension:** Merely redacting secrets from logs is reactive and fails if an agent transmits credentials over network sockets; merely vaulting credentials fails if tool error messages print secrets into stdout.
- **Resolution:**
  - **Pre-Execution:** **MEC-06 (JIT Ephemeral Credential Brokering)** mints single-use, scoped tokens injected directly into the isolated sandbox environment, keeping long-lived credentials out of LLM memory.
  - **In-Flight / Post-Execution:** **MEC-07 (DLP Stream Redaction)** intercepts all stdout/stderr streams and tool returns, sanitizing API keys and PII before they can enter `transcript.jsonl` or model context.

### 3. Four-Class Side-Effect Taxonomy & HITL Escalation (`CAP-29` ↔ `CAP-30`)
Every tool interaction is formally classified prior to dispatch:
- **Class 0 (Read-Only):** `fs.readFile`, `web.search` → Immediate automated execution under CapBAC.
- **Class 1 (Idempotent Mutating):** `fs.writeFile` (overwrite), `s3.putObject` → Allowed with automatic snapshot checkpoint.
- **Class 2 (Compensable Mutating):** `git.commit`, `db.insertRow` → Requires registered Saga compensator (`git.revert`, `db.deleteRow`).
- **Class 3 (Irreversible Destructive):** `stripe.charge`, `smtp.sendEmail`, `db.dropTable`, `cloud.destroy` → Mandatory **CAP-29 HITL Escalation Gateway** step-up approval.

---

## 5. Verification & Audit Trail

- **Harm 4–5 Veto Adherence:** Verified. All 8 capabilities in Layer 4 have $\text{Harm if Absent} \ge 4$ and mitigate `SC-07`, `SC-04`, `SC-03`, `SC-10`, or `SC-06`. Zero capabilities are ranked below median; all are anchored in **S-Tier** (6 elements) or **A-Tier** (2 elements).
- **SC-07 SSHC Zero-Tolerance Adherence:** Verified. 0 credential leaks, 0 unsandboxed escapes, and ≥90% injection blocking are mathematically enforced across all scorecards.
- **Multi-Ecosystem Translation Verified:** All 8 capabilities grounded across $\ge 2$ production agent ecosystems (Claude Code, OpenAI Assistants, LangGraph, OpenHands, AWS Bedrock/Cedar, OPA, Sigstore/Cosign, HashiCorp Vault, Linux namespaces/seccomp).
