# Third-Party MCP Registry

EXTERNAL MCP servers cited in the corpus (B-category-catalogs/10-mcp,
atlas/04-mcp, how-to-use/02-mcp.md). Enable per MCP_SECURITY.md rules
(default-deny remote, token scopes, poisoning defense, Inspector first).
Four are pre-wired in `.harness/mcp/tools.yaml` (filesystem, playwright,
context7, github); the rest below install on demand.

| Server | Use / trigger | Source |
|---|---|---|
| github-mcp-server | GitHub issues/PRs/Actions as tools | https://github.com/github/github-mcp-server |
| brave-search-mcp-server | Web search grounding | https://github.com/brave/brave-search-mcp-server |
| sentry-mcp | Error/issue tracking | https://github.com/getsentry/sentry-mcp |
| playwright-mcp | Browser automation (Microsoft build) | https://github.com/microsoft/playwright-mcp |
| docker/mcp-servers | Container-lifecycle tools | https://github.com/docker/mcp-servers |
| context7 (upstash) | Library docs grounding | https://github.com/upstash/context7 |
| stripe/agent-toolkit | Payments tooling | https://github.com/stripe/agent-toolkit |
| mcp-server-kubernetes | K8s cluster tools | https://github.com/Flux159/mcp-server-kubernetes |
| mcp-use | MCP client framework | https://github.com/mcp-use/mcp-use |
| langchainjs | Agent framework (NOT-MCP alternative path) | https://github.com/langchain-ai/langchainjs |

Spec/SDK/inspector references (build-your-own path):
modelcontextprotocol/servers, inspector, typescript-sdk, python-sdk, go-sdk,
rust-sdk, csharp-sdk (all under `https://github.com/modelcontextprotocol/`).
