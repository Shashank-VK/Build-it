# §24d — AI & Agent Security: Research Notes

> Scope: prompt injection, malicious retrieved content, permissions, tool use, execution environments, exfiltration, supply chain, destructive actions; sandboxing, allowlists, approvals, secret isolation, audit, budgets, untrusted-content handling, least-privilege identities, runtime policy, recovery. Researched 2026-10-10. Read-only research. Metadata: `07-evidence-register.md`.

## 1. Current guidance landscape (verified current editions)

- **OWASP Top 10 for LLM Applications 2026** (3 Aug 2026, supersedes 2025): LLM01 Prompt Injection · LLM02 Sensitive Information Disclosure · LLM03 Excessive Agency · LLM04 Supply Chain · LLM05 Data and Model Poisoning · LLM06 Unbounded Consumption · LLM07 Misinformation · LLM08 Hidden Context Exposure · LLM09 Vector and Embedding Weaknesses · LLM10 Improper Output Handling. **Corroborated** (Warrant line-by-line PDF read 2026-08-06; independent standards register fetched 2026-08-25).
- **OWASP Top 10 for Agentic Applications (ASI) 2026**: ASI01 Agent Goal Hijack · ASI02 Tool Misuse & Exploitation · ASI03 Identity & Privilege Abuse · ASI04 Agentic Supply Chain · ASI05 Unexpected Code Execution · ASI06 Memory & Context Poisoning · ASI07 Insecure Inter-Agent Communication · ASI08 Cascading Failures · ASI09 Human-Agent Trust Exploitation · ASI10 Rogue Agents/Uncontrolled Autonomy. **Corroborated** (≥4 independent 2026 sources).
- **OWASP MCP Top 10 (2025)**: first classification of Model Context Protocol risks; tool poisoning codified as **MCP03:2025**, alongside rug pulls and tool shadowing. **Corroborated** (CSA research note; DevSecOps guide).
- **OWASP GenAI Red Teaming Guide v1.0** (23 Jan 2025). **Verified** (standards register).
- **Google SAIF** (Secure AI Framework) risk catalog — 15 risks with IDs, current on main 2026-08-25. **Corroborated**.
- **MITRE ATLAS 5.6.0** — 170 techniques/sub-techniques for adversarial ML threat modeling. **Corroborated**.
- **NIST AI 100-2** (Adversarial ML taxonomy) — referenced by 2026 analysts as the taxonomy companion. **Corroborated**.
- **EU AI Act Art. 15** (accuracy, robustness, cybersecurity for high-risk AI): providers must ensure resilience against adversarial attacks incl. data poisoning and model manipulation, demonstrated through technical documentation and testing. Deadlines shifted by the May 2026 Digital Omnibus: 2 Dec 2027 (stand-alone Annex III) / 2 Aug 2028 (Annex I embedded). **Corroborated** (Sectricity, SQUR, Mishcon 2026 analyses). **Legal obligation** in the specified context (EU high-risk AI), not a universal mandate.

## 2. Foundational research — prompt injection

- **Perez & Ribeiro (2022), "Ignore Previous Prompt"** — first systematic study of direct prompt injection (attacker instructions submitted as user input). **Corroborated** (cited across 2026 security skills).
- **Greshake et al. (2023), "Not what you've signed up for" (arXiv 2302.12173)** — named and formalized **indirect prompt injection**. Load-bearing findings:
  - Processing untrusted retrieved data is *analogous to executing arbitrary code*: retrieval merges data and instructions into one undifferentiated channel; there is no parameterised prompt.
  - The attacker never enters the session (no account, no request, no rate limit) — they place text where the agent will read it; the victim's application fetches it.
  - Demonstrated on real products (Bing Chat on GPT-4, GitHub Copilot): self-forwarding worms via address books, persistence through agent memory, C2 fetching fresh instructions, staged payloads, supply-chain path through package documentation.
  - Economics worsen it: the attacker states only the *goal*; the model invents the *method*; follow-up API calls retrieve material reinforcing the injection.
  **Corroborated** (paper via arXiv mirrors; two independent 2026 write-ups; globalsecurity summary).
- **CrowdStrike (2025)**: tracking 150+ distinct prompt-injection techniques, 300,000+ adversarial prompts analyzed — single-vendor telemetry, treat as directional not canonical. **Corroborated-as-attributed** (one article's claim; vendor telemetry).
- Simon Willison's prompt-injection taxonomy — documents real-world attack surfaces **and defense limitations** (prompt-level defenses are probabilistic, not guarantees). Referenced as the practitioner's field guide. **Corroborated** (multiple skills cite it).

**Implication**: prompt injection (LLM01:2026 / ASI01) has no patch-style fix; mitigations are architectural (separation, filtering, oversight), not a code change. This is a **critical technical safeguard** domain for any agent that reads untrusted content.

## 3. MCP-specific attack research (2025–2026)

- **Tool poisoning** — named by Invariant Labs (Apr 2025): malicious instructions inside tool `description` fields (loaded into agent context at session init) steer the model; models cannot reliably distinguish operational intent from embedded adversarial instruction. PoC: an "add two numbers" tool whose hidden description instructed the agent to read `~/.cursor/mcp.json` and exfiltrate it. **Corroborated** (CSA research note; Invariant Labs; multiple 2026 guides).
- **MCPTox benchmark**: 20 LLM agents vs 45 real MCP servers — most vulnerable; more capable models often *more* vulnerable (instruction-following is the exploit surface); Claude 3.7 Sonnet highest refusal rate at under 3%. **Corroborated** (two independent summaries).
- **MCPInspect study** (arXiv 2510.16558, DSN 2026): 833 vulnerable MCP servers in the wild, 18 with suspicious/deliberately misleading tool descriptions. **Corroborated-as-attributed** (single article citing the study).
- **Parameter-level poisoning**: injection payloads hidden in `inputSchema` parameter descriptions/defaults/enums — also passed to the LLM, rarely shown in approval UIs. **Corroborated** (2026 dev write-up; clients: 5 of 7 tested had zero static validation of tool descriptions).
- **Rug pulls**: tool approved once, definitions silently changed later; clients rarely re-prompt. Fix: pin/hash `tools/list`, re-prompt on change. **Corroborated**.
- **Tool shadowing**: one server's description steers use of *another* server's tools. **Corroborated**.
- **Confused deputy / token passthrough**: servers forwarding upstream tokens without audience validation; MCP spec: servers MUST NOT accept tokens not issued for them; OAuth discovery URLs can point at `169.254.169.254` (SSRF during discovery) — block private/link-local, HTTPS-only except loopback. **Corroborated** (MCP spec security best practices via implementer docs).
- **Supply chain**: first malicious MCP packages on public registries Sep 2025 (typosquatting, fake "official" servers); **CVE-2025-49596 (CVSS 9.4)** — RCE via unauthenticated MCP Inspector instances. **Corroborated** (DevSecOps guide).
- **Credential aggregation**: one MCP server holding Slack+GitHub+Postgres+Salesforce creds = single-point breach. **Corroborated**.
- **Annotations untrusted**: spec says clients MUST treat `readOnlyHint` etc. as untrusted unless from trusted servers — never auto-approve on that basis. **Corroborated**.

## 4. Control catalog — evaluated per checklist

| Control | Threat addressed | Notes / evidence |
|---|---|---|
| **Sandboxing** (hardware-enforced, zero-access where feasible) | ASI05 unexpected code execution | 2026 guidance calls mandatory sandboxing for code interpreters; agents generating/executing code without sandboxing = RCE path. **Corroborated**. Classification: **critical** when agents execute code; n/a for text-only agents. |
| **Tool allowlists + signed tool manifests** | ASI02 tool misuse, ASI04 supply chain, MCP tool poisoning | Granular, just-in-time permissions; pin/hash tool definitions; re-approve on change. **Corroborated**. |
| **Permission boundaries / least-privilege identities** | ASI03 identity & privilege abuse, excessive agency (LLM03:2026) | Unique, short-lived, per-task/per-tool scoped credentials; agent never inherits the user's full credentials; no shared service accounts. **Corroborated**. |
| **Human approval for consequential ops** | ASI09 trust exploitation, unintended destructive actions | MCP spec only "SHOULD" require human-in-the-loop — "that word is doing too much work." Require explicit approval for irreversible/high-blast-radius actions (payments, deletion, external comms, prod deploys). Approval UIs must show *full* tool info (truncation widens the human-model visibility gap). **Corroborated**. |
| **Secret isolation** | Credential theft via injection (LLM02, ASI01→exfil) | Secrets in a separate store the model cannot read; tools receive secrets at execution, never in context; redact from logs/traces. **Inferred** from threat model; standard practice. |
| **Output validation** | LLM05 improper output handling, LLM10 unbounded consumption | Validate model output before it drives tools/DB/APIs (schema + allowlist + size caps); treat model output as untrusted input to downstream systems. **Corroborated** (LLM05 definition). |
| **Audit logs** | All — detection & forensics | Log tool calls, approvals, permission grants, prompt/response pairs (redacted); JSON-RPC MCP traffic doesn't fit traditional SIEM patterns — plan reconstruction explicitly. **Corroborated**. |
| **Agent budgets & retry limits** | LLM06 unbounded consumption, ASI08 cascading failures | Token/cost/time budgets per task and per session; retry caps; circuit breakers; transactional rollback / safe failure modes. **Corroborated**. |
| **Untrusted-content handling** | Indirect injection (Greshake), memory poisoning (ASI06) | Treat all retrieved/external content as untrusted data, never instructions; delimit untrusted content in context; sanitise ingested data; integrity checks on persistent memory; memory isolation between agents/sessions. **Corroborated**. |
| **Runtime policy enforcement** | All | Policy engine at the tool-call boundary (pre-tool guards, per-tool blast-radius declarations); deny-by-default. **Corroborated** (2026 harness mappings: `pretool_guard.py`, allowlists enforced). |
| **Recovery / rollback** | ASI08 cascading failures | Backups, transactional semantics, kill-switches, defined safe failure modes. **Corroborated**. |
| **Inter-agent auth** | ASI07 insecure inter-agent communication | mTLS + message signing between agents; no unauthenticated A2A delegation; consent verification. **Corroborated**. |

## 5. How controls change with agent capability (escalation ladder)

- **Text-only agent (no tools)**: prompt injection → misinformation (LLM07) and sensitive disclosure (LLM02) are the risks; sandboxing/approvals n/a. Controls: output validation, disclosure minimisation, system-prompt hygiene (LLM08:2026 Hidden Context Exposure is new — system prompt leakage moved from LLM07:2025's name to a broader context-exposure framing).
- **+ read tools (web, files, DB read)**: indirect injection via retrieved content becomes the primary threat (Greshake); add untrusted-content handling, secret isolation, read-scoped least-privilege identities, memory poisoning defenses.
- **+ write/exec tools (terminal, repos, DB write, external APIs)**: full control stack required — sandboxing, tool allowlists, per-action scoped credentials, human approval for consequential ops, audit logs, budgets, rollback. One compromised write-capable agent = the blast radius of its broadest credential.
- **+ payments / production infra**: treat as **critical technical safeguard** tier: mandatory human approval (or dual control), separate least-privilege service identities, spend/rate budgets with hard caps, immutable audit trail, incident runbook. **Inferred** from threat model + 2026 practitioner guidance.
- **Multi-agent**: add ASI07/ASI08 controls — authenticated inter-agent channels, circuit breakers, quarantine of misbehaving agents.

## 6. Negative evidence / unknowns
- I did not verify the exact 2026 LLM Top 10 PDF's per-risk control lists (122 pages); I rely on the corroborated category list and reputable secondary readings. Requirement-level detail = **Unknown**.
- Vendor telemetry figures (CrowdStrike 150 techniques; "~40% of API attacks") are single-source and directional.
- The EU AI Act Art. 15 implementing technical standards were still in draft (consultation draft Q2 2026) — precise conformity evidence expectations are **Unknown**; treat as "red-team the AI-specific attack surface + document" (per 2026 legal analyses).
