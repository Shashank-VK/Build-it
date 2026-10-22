# Phase 8 — Task 4: Verify Astryx MCP Config

**Research date:** 2026-08-11
**Source URLs fetched directly:**
- github.com/facebook/astryx (confirmed live)
- raw.githubusercontent.com/facebook/astryx/main/packages/cli/README.md (200 OK)
- raw.githubusercontent.com/facebook/astryx/main/packages/mcp-server/README.md (404)
- raw.githubusercontent.com/facebook/astryx/main/packages/mcp/README.md (404)
- astryx.design/docs/mcp (EOF — domain not resolving)
- Multiple web searches for @astryxdesign/cli MCP config

---

## What Was Found

### Astryx GitHub repo: facebook/astryx
- Repository: github.com/facebook/astryx — LIVE, public, from Meta/Facebook
- Description confirmed as Meta''s AI-agent-ready React design system
- CLI package: @astryxdesign/cli — confirmed in packages/cli/README.md

### What the CLI README says about MCP
The @astryxdesign/cli README (live fetch, 195 lines) contains ZERO references to:
- "mcp"
- "MCP server"
- "Model Context Protocol"
- Any opencode.json config
- Any server start command

The CLI is a pure command-line tool for querying the design system (search, component,
docs, template, theme, etc.). There is NO MCP server built into the CLI package.

### Package search for MCP
Attempted to fetch:
- packages/mcp-server/README.md → 404
- packages/mcp/README.md → 404

Neither package exists in the repository as of the fetch date.

### What web search returned
The web search results for "Astryx MCP" produced two distinct types of answers:

**Type 1: Synthesized/speculative config (unreliable)**
Several search snippets returned a config snippet like:
```json
{
  "mcp": {
    "astryx": {
      "type": "local",
      "command": ["npx", "-y", "@astryxdesign/cli", "mcp"],
      "enabled": true
    }
  }
}
```
This appears to be a plausible-but-invented config extrapolated from how other MCP servers
work. The @astryxdesign/cli README does not document a "mcp" subcommand, and attempting to
run `npx @astryxdesign/cli mcp` would produce ERR_UNKNOWN_COMMAND based on the documented
error code schema (ERR_UNKNOWN_COMMAND: "A top-level command name was not recognized").

The command list in the live CLI README is: blog, build, component, discover, docs, doctor,
hook, init, layout, search, swizzle, template, theme, upgrade, validate-integration.
There is NO "mcp" command in this list.

**Type 2: CLI-as-tool (accurate but not an MCP server)**
The real documented agent integration is:
- The agent uses `npx @astryxdesign/cli <command>` as a bash tool call, not as an MCP server
- The --dense flag produces token-efficient output for AI context
- astryx init generates AGENTS.md / CLAUDE.md for project context
- astryx manifest --json outputs the full system capability schema for AI ingestion

This is a CLI-tool integration pattern, not an MCP server integration.

---

## FLAG: ARCHITECTURE CLAIM vs. REALITY

**Architecture doc claim (from 07-autonomous-agent-architecture.md):**
References "Astryx MCP tools" being auto-called by the agent.

**What the real docs show:**
As of 2026-08-11, there is NO confirmed MCP server for Astryx. The facebook/astryx repository
does not contain an MCP server package. The @astryxdesign/cli package has no "mcp" subcommand.

The opencode.json config snippet circulating in search results:
```json
"mcp": { "astryx": { "type": "local", "command": ["npx", "-y", "@astryxdesign/cli", "mcp"] } }
```
...is UNVERIFIED and likely would fail with ERR_UNKNOWN_COMMAND.

**This is a genuine gap in the architecture document.** The Astryx integration should be
characterized as:

> "Astryx CLI tools (not MCP) — the agent calls `npx @astryxdesign/cli search <component>` or
> `npx @astryxdesign/cli component <name> --dense` as bash tool calls when building UI,
> rather than via an MCP server."

---

## Verified Integration Path (CLI, not MCP)

Since the CLI is the confirmed integration point, the agent uses Astryx through bash calls:

```bash
# Search for a component (agent uses this when building UI)
npx @astryxdesign/cli search button --dense

# Get full component docs
npx @astryxdesign/cli component Button --dense

# List available templates
npx @astryxdesign/cli template --list

# Get token docs
npx @astryxdesign/cli docs tokens --dense
```

For a project that installs @astryxdesign/cli as a dev dependency:
```json
"scripts": {
  "astryx": "node node_modules/@astryxdesign/cli/clients/cli/bin/astryx.mjs"
}
```
Then the agent can use `npm run astryx component Button --dense` as a bash tool call.

There is also the agent init command which generates context docs for the agent:
```bash
npx @astryxdesign/cli init
```
This generates AGENTS.md describing available Astryx components, which gets read by the
OpenCode agent on session startup (as part of the walkinglabs startup flow that reads
AGENTS.md first).

---

## opencode.json for Astryx (CLI approach, verified)

No MCP config is needed. The CLI approach requires no opencode.json entry — the agent just
calls it as bash. However, to give the agent structured awareness of Astryx at session start,
the AGENTS.md generated by `astryx init` should be placed in the project root (or merged
into the existing AGENTS.md).

If/when Meta ships an actual Astryx MCP server in the future, it would likely appear as a
separate npm package (e.g., @astryxdesign/mcp-server or similar) with its own README.
At that point, the config would follow the standard OpenCode MCP format:
```json
{
  "mcp": {
    "astryx": {
      "type": "local",
      "command": ["npx", "@astryxdesign/mcp-server"],
      "enabled": true
    }
  }
}
```
But this is hypothetical — no such package exists today.

---

## Summary

| Question | Answer |
|---|---|
| Does Astryx have an MCP server? | NOT CONFIRMED. No MCP package found in facebook/astryx repo. |
| Does @astryxdesign/cli have a "mcp" subcommand? | NO — not in the documented command list. |
| What is the actual integration path? | CLI bash tool calls, using --dense for token efficiency. |
| Is the circulating opencode.json config snippet real? | UNVERIFIED — likely speculative, would probably fail. |
| What does the architecture doc need to correct? | "Astryx MCP tools" -> "Astryx CLI tools (bash calls)" |
| Risk level of this gap | MEDIUM — the architecture references a non-existent MCP server; the actual CLI integration works but is different in kind. |
