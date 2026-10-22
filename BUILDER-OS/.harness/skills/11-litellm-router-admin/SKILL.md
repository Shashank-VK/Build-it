---
name: bos-litellm-router-admin
domain: Integration & Extensibility
version: 1.0.0
tier: Essential
cap: CAP-22/CAP-23
triggers:
  - "model routing"
  - "litellm"
  - "API gateway"
  - "rate limit"
  - "model fallback"
---

# LiteLLM Router Administration Runbook

## Objective
Operate and administer the LiteLLM Proxy Gateway as the unified model routing layer for autonomous agent fleets. This runbook establishes standard procedures for startup, virtual model routing, real-time token spend auditing, health monitoring, automatic rate-limit failover, and budget cycle resets.

---

## When to Activate
- When initializing or configuring the local or CI LLM API gateway.
- When configuring agent SDKs and CLI tools to route completions through a unified proxy.
- When establishing multi-provider fallback chains (Anthropic $\to$ Gemini $\to$ OpenAI) to handle upstream outages or rate limits.
- When monitoring agent token consumption, auditing cost logs, or resetting budget limits.

---

## Required Environment Variables
Ensure the following environment variables are exported before starting the gateway or making authenticated admin requests:

```bash
# Gateway Master Key for proxy administration
export LITELLM_MASTER_KEY="sk-harness-master-key"

# Upstream Provider API Keys
export ANTHROPIC_API_KEY="sk-ant-..."
export GEMINI_API_KEY="AIzaSy..."
export OPENAI_API_KEY="sk-proj-..."  # Optional / Secondary Fallback
```

---

## Step-by-Step Runbook

### Step 1: Start the LiteLLM Proxy Gateway
Launch the proxy with the repository's telemetry configuration on port 4000:

```bash
litellm --config .harness/telemetry/litellm-config.yaml --port 4000
```

To run as a detached background daemon in Linux/WSL environments:
```bash
nohup litellm --config .harness/telemetry/litellm-config.yaml --port 4000 > .harness/telemetry/litellm.log 2>&1 &
```

### Step 2: Point Agent API Calls to the Gateway
Direct all agent SDKs, CLI tools, and background subagents to the OpenAI-compatible proxy endpoint at `http://localhost:4000/v1`. Configure standard environment variables:

```bash
export OPENAI_API_BASE="http://localhost:4000/v1"
export OPENAI_API_KEY="$LITELLM_MASTER_KEY"
```

Use virtual model aliases rather than hardcoded vendor model strings:
- **`coding-primary`**: High-reasoning model for complex architecture, planning, and refactoring (Primary: Claude 3.7 Sonnet / Gemini 1.5 Pro).
- **`coding-fast`**: High-speed, low-cost model for repo exploration, syntax checks, and unit test generation (Primary: Claude 3.5 Haiku / Gemini 1.5 Flash).

#### Python SDK Example:
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:4000/v1",
    api_key="sk-harness-master-key"
)

response = client.chat.completions.create(
    model="coding-primary",
    messages=[{"role": "user", "content": "Analyze repository architecture"}]
)
print(response.choices[0].message.content)
```

### Step 3: Monitor Real-Time Spend & Token Logs
Audit real-time spend, token consumption, and per-model utilization:

```bash
curl -s http://localhost:4000/spend/logs \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" | jq .
```

To view aggregate spend by key or user:
```bash
curl -s http://localhost:4000/global/spend \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" | jq .
```

### Step 4: Check Model Health & Latency
Verify provider connectivity, active endpoints, and model health status:

```bash
curl -s http://localhost:4000/health \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" | jq .
```

A healthy response returns `{"status": "healthy"}` with individual model latency stats.

### Step 5: Automated Rate-Limit & Outage Failover
When an upstream provider returns HTTP 429 (Rate Limit Exceeded) or 5xx (Service Unavailable), the LiteLLM router automatically intercepts the failure and fails over to the next configured fallback model in the chain without interrupting agent execution.

Fallback hierarchy defined in `.harness/telemetry/litellm-config.yaml`:
```yaml
model_list:
  - model_name: coding-primary
    litellm_params:
      model: anthropic/claude-3-7-sonnet-20250219
      api_key: os.environ/ANTHROPIC_API_KEY
      rpm: 60
      tpm: 100000
  - model_name: coding-primary-fallback-1
    litellm_params:
      model: gemini/gemini-1.5-pro-latest
      api_key: os.environ/GEMINI_API_KEY
  - model_name: coding-fast
    litellm_params:
      model: anthropic/claude-3-5-haiku-20241022
      api_key: os.environ/ANTHROPIC_API_KEY
  - model_name: coding-fast-fallback-1
    litellm_params:
      model: gemini/gemini-1.5-flash-latest
      api_key: os.environ/GEMINI_API_KEY

router_settings:
  fallbacks:
    - coding-primary: ["coding-primary-fallback-1"]
    - coding-fast: ["coding-fast-fallback-1"]
  num_retries: 3
  timeout: 60
  allowed_fails: 2
  cooldown_time: 30
```

### Step 6: Reset Daily Spend & Budget Quotas
Reset spend tracking at the start of new test iterations or evaluation runs:

```bash
curl -X POST http://localhost:4000/spend/reset \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json"
```

---

## Completion Gate
Before considering LiteLLM router administration complete:
- [ ] **Environment active**: `LITELLM_MASTER_KEY`, `ANTHROPIC_API_KEY`, and `GEMINI_API_KEY` exported in environment.
- [ ] **Process healthy**: `curl http://localhost:4000/health` returns HTTP 200 with status healthy.
- [ ] **Virtual routing verified**: Request to `coding-primary` and `coding-fast` returns valid completions.
- [ ] **Spend tracking confirmed**: `/spend/logs` logs request tokens and estimated cost.
- [ ] **Fallback verified**: Triggering rate limit or invalid key properly falls over to secondary provider.

---

## Common Pitfalls

| Anti-Pattern | Bad Implementation | Correct Solution |
| :--- | :--- | :--- |
| **Bypassing Proxy** | Directly invoking `Anthropic()` or `GoogleGenerativeAI()` SDKs | Point standard OpenAI client to `http://localhost:4000/v1` |
| **Hardcoding Vendor Names** | Agent requesting `claude-3-7-sonnet-20250219` directly | Request virtual alias `coding-primary` to preserve fallback |
| **Missing Auth Headers** | `curl http://localhost:4000/spend/logs` without bearer token | Include `-H "Authorization: Bearer $LITELLM_MASTER_KEY"` |
| **Unbounded Budget** | Omitting `max_budget` or spend circuit breaker in config | Configure daily spend caps in `litellm-config.yaml` |
| **Silent Fallback Loops** | Omitting `cooldown_time`, causing spam against failing API | Configure `cooldown_time: 30` and `allowed_fails: 2` |
Ref: verbatim runbook from solo the-harness; skill card in `../how-to-use/01-skills.md`.
