---
name: docker-sandbox-runner
domain: Safety & Sandboxing
version: 1.0.0
tier: Essential
cap: CAP-24/CAP-25
triggers:
  - "run command safely"
  - "sandbox execution"
  - "docker run"
  - "isolated exec"
---

# Docker & Sandbox Execution Runner

## Objective
Execute commands, test suites, builds, and untrusted scripts within strict hermetic sandbox environments orchestrated by `.harness/sandbox/gate.sh` to enforce zero-trust credential masking, air-gapped network policies, and read-only filesystem immutability.

## When to Activate
- Executing test suites (pytest, jest, vitest, cargo test) that could produce side-effects.
- Running third-party package managers or build scripts (`npm install`, `pip install`, `make`).
- Executing speculative, unverified, or dynamically generated code.
- Performing read-only static analysis and runtime inspections in secure environments.

## Step-by-Step Runbook

### The Three Sandbox Isolation Modes
The harness dynamically detects and manages execution across three isolation tiers:
1. **Bubblewrap (`bwrap`) [Priority 1]**: Unprivileged zero-daemon Linux namespace isolation. Provides PID, IPC, UTS, and user namespace virtualization, mounts the root host filesystem read-only, provisions ephemeral in-memory tmpfs for `/tmp`, unshares network interfaces by default, and masks sensitive credential paths (`~/.ssh`, `~/.aws`, `~/.kube`, `~/.gnupg`, `/root`).
2. **Docker / Podman Container [Priority 2]**: Containerized isolation running with dropped capabilities (`--cap-drop=ALL`), non-root UID/GID mapping, read-only rootfs (`--read-only`), `no-new-privileges` security options, and air-gapped network namespace (`--network none` by default).
3. **None / Unsupported [Veto Shield]**: If neither `bwrap`, `docker`, nor `podman` is available, unsandboxed execution is blocked with exit code `126` to satisfy the SC-07 Harm 4-5 safety shield.

---

### Step 1: Always Call Via `gate.sh` (Never Raw `docker run`)
Never execute raw `docker run`, unshielded subshells, or direct host commands for untrusted operations. Always invoke through `.harness/sandbox/gate.sh` (or the `sandbox_run.sh` helper) to guarantee invariant policy enforcement and credential masking.

```bash
# Correct canonical invocation:
bash .harness/sandbox/gate.sh [OPTIONS] -- <COMMAND> [ARGS...]
```

---

### Step 2: Enforce Read-Only Mode for Safe Inspections
For commands that do not require writing to the workspace (such as test runners, linters, syntax checks, or exploratory commands), explicitly pass the `--ro` flag:

```bash
bash .harness/sandbox/gate.sh --ro -- pytest tests/
```

---

### Step 3: Explicit Network Egress Allowance
By default, the sandbox is completely air-gapped (`--network none`). When network access is strictly necessary (e.g. downloading verified dependencies or fetching remote schema definitions), pass `--network allow` (or `--network allow-egress`) explicitly and log the operational justification:

```bash
# Explicit network authorization with audit reason
echo "[AUDIT] Allowing network egress to install verified dependencies"
bash .harness/sandbox/gate.sh --network allow -- npm install --package-lock-only
```

---

### Step 4: Validate Exit Codes & Policy Violations
Inspect return codes from `gate.sh`:
- Exit Code `0`: Successful execution.
- Exit Code `126`: Critical safety block — no approved sandbox runtime available on host.
- Exit Code `2`: Invalid argument, unrecognized network mode, or missing command separator `--`.
- Exit Code `137` / Timeout: Execution exceeded configured timeout (default 60s).
- Non-zero command codes: Inspect stderr to differentiate between application-level test failures and sandbox permission violations (e.g., attempt to write in `--ro` mode or access masked `~/.ssh`).

---

### Example Invocations

#### 1. Running Pytest in Sandbox (Read-Only)
```bash
bash .harness/sandbox/gate.sh --ro -- pytest tests/unit -q
```

#### 2. Running NPM Install in Sandbox (Writable Workspace + Network Allowed)
```bash
bash .harness/sandbox/gate.sh --network allow -- npm install
```

#### 3. Running a Python Script Read-Only
```bash
bash .harness/sandbox/gate.sh --ro -- python3 src/app/verify_signatures.py
```

#### 4. Using the `sandbox_run.sh` Wrapper
```bash
# Defaults to read-only workspace
bash .harness/skills/09-docker-sandbox-runner/scripts/sandbox_run.sh pytest tests/

# Pass --rw to enable writable workspace
bash .harness/skills/09-docker-sandbox-runner/scripts/sandbox_run.sh --rw npm run build
```

## Completion Gate
- Command executes inside an isolated container or namespace without accessing host secrets.
- Read-only commands strictly prevent modifications to workspace files.
- Network access remains completely disabled unless `--network allow` is explicitly supplied.
- Process exit codes and standard error outputs are accurately captured and logged.

## Common Pitfalls
- **Bypassing the Gate**: Running raw `docker run` or host bash directly, which bypasses credential masking and permission validation.
- **Accidental Write Permissions**: Omitting `--ro` during test or inspection phases, allowing errant test scripts to modify source files or create untracked artifacts.
- **Unrestricted Network Egress**: Leaving network mode set to `allow` when local hermetic execution was possible.
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
