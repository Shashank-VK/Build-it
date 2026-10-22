---
name: secrets-entropy-sanitizer
domain: Security & Hardening
version: 1.0.0
tier: Essential
cap: CAP-26
triggers:
  - "check for secrets"
  - "credential scan"
  - "before commit"
  - "secret leak"
---

# Secrets & High-Entropy Sanitizer

## Objective
Enforce automated pre-commit scanning and Shannon entropy heuristics to intercept, redact, and prevent hardcoded credentials, API keys, private keys, and high-entropy secret payloads from entering version control or execution logs.

## When to Activate
- Executing pre-commit or pre-push verification gates.
- Before committing new code, test fixtures, or configuration updates.
- Adding third-party service clients, database connections, or cloud integrations.
- Auditing repository history or newly generated scratch files.

## Step-by-Step Runbook

### Step 1: Execute Structured Gitleaks Scan
Scan staged changes and local working tree using Gitleaks to catch known signatures across popular providers:

```bash
# Scan staged changes with verbose logging and redacted secret payloads
gitleaks protect --staged --verbose --redact
```

If checking full repository history or unstaged files:
```bash
gitleaks detect --verbose --redact
```

---

### Step 2: High-Entropy Heuristic Fallback Scan
If Gitleaks finds no signature matches (or in environments without Gitleaks binary installed), execute the deep regex entropy scan across source and configuration files:

```bash
grep -r --include="*.py" --include="*.ts" --include="*.env" -E "[A-Za-z0-9+/]{40,}" . | grep -v ".git"
```

*Rule: Any contiguous token of 40 or more base64/hex characters is flagged as a high-entropy secret candidate.*

---

### Step 3: Candidate Verification & Triage
Examine flagged candidate lines to distinguish genuine secrets from harmless static artifacts:
- **False Positives**: Git commit SHAs, package lockfile integrity hashes (`sha512-...`), UUID fixtures, base64-encoded SVG icons, or standardized mock tokens.
- **True Positives**: Active credentials, private keys, OAuth client secrets, connection strings with embedded passwords.

---

### Step 4: Remediation Protocol (True Positives)
When a real secret is identified:
1. **DO NOT COMMIT**: Immediately unstage any affected files (`git reset HEAD <file>`).
2. **Sanitize Source**: Replace the hardcoded literal with an environment variable lookup (e.g. `os.environ["API_KEY"]` or `process.env.API_KEY`).
3. **Template Environment**: Place placeholder entries inside `.env.example` (e.g. `API_KEY=your_key_here`).
4. **Ignore Sensitive Files**: Verify that `.env`, `.env.local`, and credential files are explicitly listed in `.gitignore`.
5. **Rotate Credential**: Treat the credential as compromised. Rotate and revoke the secret immediately via the issuing provider's console or IAM API.

---

### Common Secret Signatures & Patterns

| Provider / Type | Pattern Prefix / Regex | Example Representation | Risk Tier |
| :--- | :--- | :--- | :--- |
| **AWS Access Key** | `AKIA[0-9A-Z]{16}` | `AKIAIOSFODNN7EXAMPLE` | Critical |
| **GitHub Personal Access Token** | `ghp_[a-zA-Z0-9]{36}` / `github_pat_` | `ghp_16CharacterSecretTokenHere...` | Critical |
| **Anthropic API Key** | `sk-ant-[a-zA-Z0-9_-]{32,}` | `sk-ant-api03-...` | Critical |
| **OpenAI API Key** | `sk-[a-zA-Z0-9]{20,}` / `sk-proj-` | `sk-proj-abc123...` | Critical |
| **Private RSA / EC Key** | `-----BEGIN (RSA|EC|OPENSSH) PRIVATE` | `-----BEGIN RSA PRIVATE KEY-----` | Critical |
| **Slack Bot Token** | `xoxb-[0-9]{10,}-[0-9]{10,}-[a-zA-Z0-9]{24}` | `xoxb-1234567890-abcdef...` | High |
| **Generic JWT Token** | `eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?` | `eyJhbGciOiJIUzI1NiIsInR5cCI6...` | High |

---

### Helper Script Invocation
Execute the automated two-tier scan with a single command:
```bash
bash .harness/skills/32-secrets-entropy-sanitizer/scripts/entropy_scan.sh
```

## Completion Gate
- Both Gitleaks and entropy regex scanners execute with exit code `0` on all staged changes.
- Zero plaintext API keys, tokens, or private keys exist in source code or committed artifacts.
- All secrets are resolved dynamically at runtime through secured environment variables.

## Common Pitfalls
- **Committing "Test" Secrets**: Placing real API keys in unit tests with the assumption that test suites are private. Use fake mock tokens (e.g. `sk-test-mock-00000000000000000000`).
- **Ignoring Staged Diffs**: Scanning only saved files while uncommitted staged indexes still contain sensitive tokens.
- **Bypassing with `--no-verify`**: Overriding Git commit hooks instead of resolving flagged candidate strings.
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
