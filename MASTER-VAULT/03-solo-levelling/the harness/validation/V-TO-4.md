# Independent Validation Report: Safety & Governance Tools (`T-D_SAFETY.md`)

## Executive Summary & Architectural Distinction

The tool selections in [`T-D_SAFETY.md`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/phase-3/tools/T-D_SAFETY.md) were independently audited across repository validity, maintenance velocity, functional reality, tier classification, and licensing.

### Critical Distinction: Pre-Tool Guard / Regex vs. Real Sandbox
The document **rigorously and correctly distinguishes** between mechanical isolation and semantic policy evaluation:
- **Mechanical Sandboxing ($L_0/L_1$ — CAP-24):** Tools like **Bubblewrap** and **gVisor (`runsc`)** intercept Linux system calls, unshare namespaces, and enforce seccomp-bpf filters. They guarantee mechanical confinement (preventing host file corruption, network exfiltration, or kernel escapes) regardless of what code or command the LLM generates.
- **Pre-Tool Guards / Regex / Policy Engines ($L_2/L_3$ — CAP-25 / CAP-27):** Tools like **CEL**, **OPA**, **Cedar**, and regex filters operate on structured ASTs and string parameters *before* dispatch. The document explicitly warns that prompt instructions, regex pattern guards, or DLP scanners **cannot replace an execution sandbox**, just as a syscall sandbox cannot prevent prompt injection or logical policy violations.

---

## Per-Tool Validation & Verdicts

### 1. gVisor (`runsc`)
- **Links:** [`google/gvisor`](https://github.com/google/gvisor) · [`gvisor.dev`](https://gvisor.dev) (Valid)
- **Maintenance:** **Active** (Daily commits by Google; regular stable releases; Apache-2.0).
- **Capability Reality:** **Real & Proven.** Implements a user-space Linux kernel (`Sentry`) and filesystem mediator (`Gofer`) in Go. Intercepts untrusted syscalls via KVM/ptrace, blocking container breakout CVEs.
- **Tier Plausibility:** **Essential (S-Tier)** for server-side and multi-tenant sandboxed execution.
- **Verdict:** **PASS** — Foundational, battle-tested standard powering GKE Sandbox and Cloud Run.

---

### 2. Docker Ephemeral (`moby` & `docker-py`)
- **Links:** [`moby/moby`](https://github.com/moby/moby) · [`docker/docker-py`](https://github.com/docker/docker-py) (Valid)
- **Maintenance:** **Active** (Ubiquitous enterprise container platform; Apache-2.0).
- **Capability Reality:** **Real.** Programmatic orchestration of isolated cgroups, namespaces, and disposable container filesystems. Paired with `runsc` OCI runtime to prevent container escapes.
- **Tier Plausibility:** **Essential (S-Tier)** as the universal base substrate for packaging reproducible devcontainers and compiler toolchains.
- **Verdict:** **PASS** — Industry baseline for containerized environments.

---

### 3. Bubblewrap (`bwrap`)
- **Links:** [`containers/bubblewrap`](https://github.com/containers/bubblewrap) (Valid)
- **Maintenance:** **Active** (Maintained under Project Atomic / Red Hat / Flatpak; LGPL-2.0+).
- **Capability Reality:** **Real.** Unprivileged local sandboxing utility that creates isolated user, mount, PID, and network namespaces with seccomp filters. Sub-10ms invocation overhead with zero background daemons.
- **Tier Plausibility:** **Essential (S-Tier)** for local CLI workstations where running Docker or VM daemons imposes excessive latency.
- **Verdict:** **PASS** — Gold standard for unprivileged local Linux process confinement.

---

### 4. Open Policy Agent (OPA / Rego)
- **Links:** [`open-policy-agent/opa`](https://github.com/open-policy-agent/opa) · [`opa-python-client`](https://github.com/open-policy-agent/opa-python-client) (Valid)
- **Maintenance:** **Active** (CNCF Graduated project, Styra/OSS; Apache-2.0).
- **Capability Reality:** **Real.** Declarative Policy Decision Point (PDP) that evaluates structured JSON AST payloads against compile-time `.rego` policies to produce deterministic ALLOW/DENY decisions.
- **Tier Plausibility:** **Essential (S-Tier)** for enterprise-grade tool execution governance and CI/CD policy.
- **Verdict:** **PASS** — Universally adopted standard for decoupling authorization policy from application logic.

---

### 5. AWS Cedar (`cedar-policy`)
- **Links:** [`cedar-policy/cedar`](https://github.com/cedar-policy/cedar) · [`cedarpolicy` (PyPI)](https://github.com/cedar-policy/cedar-py) (Valid)
- **Maintenance:** **Active** (AWS Security Engineering; frequent releases; Apache-2.0).
- **Capability Reality:** **Real.** Fast, formally verified (Lean theorem prover) capability-based access control (CapBAC/ABAC) language. Native Rust core with sub-millisecond Python bindings.
- **Tier Plausibility:** **Essential (S-Tier)** for high-throughput, mathematically verified inline tool authorization.
- **Verdict:** **PASS** — High-performance, verified alternative to complex Rego rules for entity-based agent policies.

---

### 6. HashiCorp Vault / OpenBao (`hvac`)
- **Links:** [`hashicorp/vault`](https://github.com/hashicorp/vault) · [`openbao/openbao`](https://github.com/openbao/openbao) · [`hvac/hvac`](https://github.com/hvac/hvac) (Valid)
- **Maintenance:** **Active** (Vault active under BSL 1.1; OpenBao active under Linux Foundation MPL-2.0; `hvac` active Apache-2.0).
- **Capability Reality:** **Real.** Industry standard for dynamic JIT secret leasing (e.g., minting 5-minute ephemeral database/cloud credentials) and encrypted transit secret engines.
- **Tier Plausibility:** **Essential (S-Tier)** for DevOps (`C5`) and Cloud Migration (`C6`) archetypes.
- **Verdict:** **PASS** — Properly references OpenBao to hedge against HashiCorp's BSL license change.

---

### 7. Protect AI Rebuff / PromptInjectionDefender
- **Links:** [`protectai/rebuff`](https://github.com/protectai/rebuff) (Valid)
- **Maintenance:** **Slow / Stagnant** (Initial release in 2023 by Protect AI; minimal upstream commit activity over the past 12 months).
- **Capability Reality:** **Real concept, but brittle standalone.** Combines heuristic regex checks, canary token embeddings, and secondary LLM verification. Canary detection is effective, but regex/heuristic classifiers are easily bypassed by indirect injection variations.
- **Tier Plausibility:** **Optional (B-Tier / Educational)** in `T-D_SAFETY.md`. The document correctly demotes Rebuff/PromptInjectionDefender to *Optional* in favor of **Structural XML Fencing (Native Baseline)** and **Lakera Guard (Enterprise Firewall)**.
- **Verdict:** **QUALIFIED PASS (Outdated Maintenance Flag)** — The capability and canary pattern are valid, but developers should rely on structural delimiter fencing and active classifiers (Lakera/Llama Guard) rather than Rebuff for production.

---

### 8. LangGraph Human-in-the-Loop (HITL)
- **Links:** [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) (Valid)
- **Maintenance:** **Highly Active** (LangChain flagship framework; daily releases; MIT).
- **Capability Reality:** **Real.** Stateful cyclic graph execution with native `interrupt()` breakpoints, persistent checkpoint savers (`SqliteSaver`, `PostgresSaver`), and state-resumption commands (`Command(resume=...)`).
- **Tier Plausibility:** **Essential (S-Tier)** for synchronous pause/resume tool confirmation and human state inspection.
- **Verdict:** **PASS** — Premier implementation of stateful graph HITL orchestration.

---

### 9. Saga Frameworks (Temporal.io Saga Orchestrator)
- **Links:** [`temporalio/sdk-python`](https://github.com/temporalio/sdk-python) · [`temporal.io`](https://temporal.io) (Valid)
- **Maintenance:** **Highly Active** (Temporal Technologies; venture-backed enterprise standard; MIT).
- **Capability Reality:** **Real.** Durable execution engine implementing the Garcia-Molina & Salem Saga pattern. Guarantees deterministic rollback and reverse execution of compensating activities upon failure.
- **Tier Plausibility:** **Essential (S-Tier)** for multi-step distributed cloud provisioning and database schema migrations.
- **Verdict:** **PASS** — Industry benchmark for durable asynchronous transactions and compensation workflows.

---

## Tool Audit Summary Table

| Tool | Canonical Repo | Link Valid | Maintained | Capability Real | Plausible Tier | Audit Verdict |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **gVisor (`runsc`)** | `google/gvisor` | Yes | Yes (Google) | Yes (Syscall Kernel) | **Essential** | **PASS** |
| **Docker Ephemeral** | `moby/moby` | Yes | Yes (Docker) | Yes (Namespaces/Cgroups)| **Essential** | **PASS** |
| **Bubblewrap** | `containers/bubblewrap` | Yes | Yes (Red Hat) | Yes (Unprivileged sandbox)| **Essential** | **PASS** |
| **OPA (Rego)** | `open-policy-agent/opa` | Yes | Yes (CNCF) | Yes (AST Policy PDP) | **Essential** | **PASS** |
| **AWS Cedar** | `cedar-policy/cedar` | Yes | Yes (AWS) | Yes (Verified ABAC) | **Essential** | **PASS** |
| **HashiCorp Vault / OpenBao**| `hashicorp/vault` / `openbao` | Yes | Yes (LF) | Yes (JIT Secret Broker)| **Essential** | **PASS** |
| **Rebuff / PromptDefender** | `protectai/rebuff` | Yes | **Stagnant** | Partial (Canary/Heuristic)| **Optional** | **QUALIFIED PASS** |
| **LangGraph HITL** | `langchain-ai/langgraph` | Yes | Yes (LangChain) | Yes (`interrupt`/checkpoints)| **Essential** | **PASS** |
| **Temporal Saga** | `temporalio/sdk-python` | Yes | Yes (Temporal) | Yes (Compensating Sagas)| **Essential** | **PASS** |

---

## Key Findings & Recommendations

1. **Zero Fabricated Tools:** Every audited tool corresponds to an authentic, publicly accessible open-source project.
2. **Proper Architectural Layering:** The document avoids the critical anti-pattern of using regex guards as sandboxes. Mechanical containment (Bubblewrap/gVisor) is strictly decoupled from authorization (OPA/Cedar) and injection defense (XML delimiters/Lakera).
3. **Licensing Awareness:** Properly identifies HashiCorp Vault's BSL licensing and recommends the Linux Foundation fork (**OpenBao**) alongside the MIT-licensed `infisical` and `hvac` clients.
4. **Maintenance Note on Canary Injection Tools:** While Protect AI Rebuff pioneered canary token injection, its maintenance has slowed; retaining **Structural Delimiter Fencing** as the *Essential* foundation and **Lakera Guard / Llama Guard** as active classifiers is confirmed as the correct architectural choice.
