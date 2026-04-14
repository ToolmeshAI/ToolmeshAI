[简体中文](./README.zh-CN.md)

# ToolmeshAI

![ToolmeshAI social preview](./docs/assets/social-preview.png)

Practical public repositories around MCP, agent workflows, docs-to-context tooling, and browser automation.

If you are new here, start with [`mcp-saas-foundry`](https://github.com/ToolmeshAI/mcp-saas-foundry).

## Quick Links

- [Profile launch note](./docs/releases/v0.1.0.md)
- [Now](./docs/now.md)
- [Launch kit](./docs/launch/README.md)
- [Support](./SUPPORT.md)
- [Security](./SECURITY.md)
- [Code of conduct](./CODE_OF_CONDUCT.md)

## Current Focus

Right now the goal is to sharpen a small, connected set of repositories instead of spreading effort across many loose experiments.

- production-minded MCP foundations
- executable MCP validation and smoke-test tooling
- safer MCP and agent configuration
- documentation pipelines that become usable AI context
- `llms.txt` validation and repo-facing context hygiene
- HTTP MCP smoke checks for teams moving beyond stdio demos
- GitHub-native agent handoff artifacts for workflow automation
- browser-agent starter scaffolds with dry-run artifacts
- browser-agent recipes that are short, repeatable, and worth shipping

## Featured Repositories

- [`mcp-saas-foundry`](https://github.com/ToolmeshAI/mcp-saas-foundry)
  Flagship blueprint for SaaS-focused MCP servers and the surrounding repo structure.
- [`safe-mcp-config`](https://github.com/ToolmeshAI/safe-mcp-config)
  Security utility for catching obvious MCP config mistakes before sharing them.
- [`docs-to-context`](https://github.com/ToolmeshAI/docs-to-context)
  Documentation bundler for turning source files into clean Markdown context for AI systems.
- [`awesome-mcp-workflows`](https://github.com/ToolmeshAI/awesome-mcp-workflows)
  Bilingual reference list of real MCP workflows, server patterns, and launch ideas.
- [`browser-agent-recipes`](https://github.com/ToolmeshAI/browser-agent-recipes)
  Reusable browser automation recipes for agentic workflows.

## Next Wave

- [`mcp-smoke-test`](https://github.com/ToolmeshAI/mcp-smoke-test)
  Zero-dependency CLI for validating whether a stdio MCP server can actually initialize and answer a basic probe.
- [`llms-txt-check`](https://github.com/ToolmeshAI/llms-txt-check)
  Zero-dependency CLI for checking whether your `llms.txt` is strong enough to publish.
- [`mcp-http-smoke`](https://github.com/ToolmeshAI/mcp-http-smoke)
  HTTP-side MCP smoke tester for `initialize`, `initialized`, and one live capability probe.
- [`browser-agent-starter`](https://github.com/ToolmeshAI/browser-agent-starter)
  Minimal browser-ready starter with dry-run planning, shared config, and structured artifacts for runnable browser-agent workflows.
- [`github-agent-action`](https://github.com/ToolmeshAI/github-agent-action)
  Small GitHub Action for turning workflow inputs into reusable execution briefs and JSON manifests.

## Why Follow

- the repositories are being built as one connected portfolio, not as isolated demos
- updates favor usable alpha quality over empty scaffolding
- README structure stays English-first for discovery, with Chinese mirrors where they help
- new repos only stay if they strengthen the portfolio's navigation and utility

## Update Rhythm

- work happens in small batches around a few active repositories at a time
- README and positioning updates land when a repository materially changes
- new public repos are added slowly, only when they strengthen the set

This profile stays intentionally short. The details live in each repository README, the release notes, and the now page.
