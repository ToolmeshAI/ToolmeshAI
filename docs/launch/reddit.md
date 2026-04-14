# Reddit Launch Copy

## English

### Suggested communities

- `r/mcp`
- `r/LocalLLaMA`
- `r/programming`
- `r/node`
- niche devtool / AI agent communities where self-promo rules allow it

### `mcp-saas-foundry`

Title:
`I built a forkable starter blueprint for SaaS-focused MCP servers`

Body:
I kept seeing MCP repos that were either too vague or too toy-like to reuse in a real team setting, so I put together `mcp-saas-foundry`.

It includes:
- blueprint docs
- a zero-dependency Node starter
- concrete SaaS and internal API examples
- a release-readiness checklist

Repo:
https://github.com/ToolmeshAI/mcp-saas-foundry

### `safe-mcp-config`

Title:
`I made a small CLI to catch risky MCP config patterns before sharing them`

Body:
`safe-mcp-config` scans MCP config files for a few high-signal mistakes that are easy to leak publicly:
- inline tokens
- dangerous shell invocations
- wildcard env passthrough

It is intentionally tiny and zero-dependency so it is easy to drop into local checks or CI.

Repo:
https://github.com/ToolmeshAI/safe-mcp-config

### `mcp-smoke-test`

Title:
`I built a tiny CLI to verify a stdio MCP server actually initializes and answers a probe`

Body:
I kept wanting a fast interoperability check for MCP servers that does more than lint config files.

`mcp-smoke-test` starts a stdio server, sends `initialize`, emits `initialized`, and attempts a real follow-up probe like `tools/list`.

It is zero-dependency and works well as a local check before publishing examples or wiring a server into a bigger workflow.

Repo:
https://github.com/ToolmeshAI/mcp-smoke-test

### `docs-to-context`

Title:
`docs-to-context: bundle scattered docs into one Markdown context file for coding agents`

Body:
This repo exists because feeding docs into AI workflows is still too manual.

`docs-to-context` takes mixed files/directories and emits one clean Markdown bundle with stable headings. Zero runtime deps.

Repo:
https://github.com/ToolmeshAI/docs-to-context

### `llms-txt-check`

Title:
`I built a tiny CLI to validate llms.txt files before they go public`

Body:
More repos are adding `llms.txt`, but a lot of them still ship weak summaries, duplicate headings, or malformed links.

`llms-txt-check` is a zero-dependency CLI that catches those obvious issues before the file lands in a public repo, docs page, or AI-tooling index.

Repo:
https://github.com/ToolmeshAI/llms-txt-check

### `mcp-http-smoke`

Title:
`I built a small HTTP MCP smoke tester for initialize + one real probe`

Body:
`mcp-http-smoke` exists for the hosted-endpoint side of MCP, where I still wanted the same fast answer:
does this endpoint really initialize, accept `initialized`, and answer one live capability probe?

It uses Node 20 `fetch`, stays lightweight, and is easy to run against local gateways or deployed MCP endpoints.

Repo:
https://github.com/ToolmeshAI/mcp-http-smoke

### `browser-agent-starter`

Title:
`browser-agent-starter: a minimal browser-ready starter for dry-run agent workflows`

Body:
This repo exists because a lot of browser-agent examples jump straight to flashy automation without giving you a credible starting shape.

`browser-agent-starter` gives you:
- a shared run config
- dry-run planning
- structured `run.json` and `plan.json` artifacts
- starter workflows for docs audit, signup smoke tests, and pricing watch

Repo:
https://github.com/ToolmeshAI/browser-agent-starter

### `github-agent-action`

Title:
`github-agent-action: turn workflow inputs into a clean execution brief and manifest`

Body:
I wanted a very small GitHub Action that takes normal workflow inputs and writes a durable handoff artifact for an agent or operator.

`github-agent-action` outputs:
- a markdown execution brief
- a JSON manifest
- GitHub output paths for downstream workflow steps

Repo:
https://github.com/ToolmeshAI/github-agent-action

## 中文

### 建议社区

- MCP / AI agent 相关 subreddit
- Node / programming / open source 相关社区
- 允许自荐的细分 devtool 社区

### `mcp-saas-foundry`

标题：
`我做了一个可 fork 的 SaaS 向 MCP starter blueprint`

正文：
我一直看到很多 MCP 仓库要么太空、要么太像玩具 demo，所以整理了一个 `mcp-saas-foundry`。

它包括：
- 蓝图文档
- 零依赖 Node starter
- SaaS / 内部 API 示例
- 发布前检查清单

仓库：
https://github.com/ToolmeshAI/mcp-saas-foundry

### `safe-mcp-config`

标题：
`我做了一个小 CLI，用来在分享 MCP 配置前先抓风险模式`

正文：
`safe-mcp-config` 会扫描 MCP 配置里几类很容易被公开泄漏的问题：
- 内联 token
- 危险 shell 调用
- 环境变量通配透传

它刻意保持很小、零依赖，方便塞进本地检查或 CI。

仓库：
https://github.com/ToolmeshAI/safe-mcp-config

### `mcp-smoke-test`

标题：
`我做了一个很小的 CLI，用来验证 stdio MCP server 是否真的能 initialize 并完成 probe`

正文：
我一直想要一个比“只查配置”更进一步的 MCP 互操作性检查工具。

`mcp-smoke-test` 会启动 stdio server，发送 `initialize`、`initialized`，再尝试一次真实的后续 probe，比如 `tools/list`。

它保持零依赖，很适合放在公开发布前的本地自检里。

仓库：
https://github.com/ToolmeshAI/mcp-smoke-test

### `docs-to-context`

标题：
`docs-to-context：把散落文档打成一份给 coding agent 用的 Markdown 上下文`

正文：
这个仓库是因为“把文档喂给 AI”这件事现在还太手工。

`docs-to-context` 支持混合文件/目录输入，输出一份标题稳定的 Markdown bundle，而且零运行时依赖。

仓库：
https://github.com/ToolmeshAI/docs-to-context

### `llms-txt-check`

标题：
`我做了一个小 CLI，用来在 llms.txt 公开前先做校验`

正文：
现在越来越多仓库开始加 `llms.txt`，但很多文件里还是会带着弱摘要、重复标题和损坏链接直接上线。

`llms-txt-check` 是一个零依赖 CLI，专门在文件进入公开仓库、文档页面或 AI 工具索引前先抓这些明显问题。

仓库：
https://github.com/ToolmeshAI/llms-txt-check

### `mcp-http-smoke`

标题：
`我做了一个很小的 HTTP MCP smoke tester，用来验证 initialize + 真实 probe`

正文：
`mcp-http-smoke` 是给 hosted endpoint 这一侧准备的 MCP 工具，我想要的还是那个简单答案：
这个 endpoint 到底能不能完成 `initialize`、接受 `initialized`，并返回一次真实 capability probe？

它基于 Node 20 `fetch`，很轻，适合对本地 gateway 或已部署 MCP endpoint 做快速检查。

仓库：
https://github.com/ToolmeshAI/mcp-http-smoke

### `browser-agent-starter`

标题：
`browser-agent-starter：一个面向 dry-run agent workflow 的最小 browser-ready starter`

正文：
很多 browser-agent 示例一上来就直奔炫技自动化，但没有给出一个可信的起步结构。

`browser-agent-starter` 提供的是：
- 统一 run config
- dry-run 规划
- `run.json` 和 `plan.json` 结构化产物
- docs audit、signup smoke test、pricing watch 三种 starter workflow

仓库：
https://github.com/ToolmeshAI/browser-agent-starter

### `github-agent-action`

标题：
`github-agent-action：把 workflow 输入整理成干净的执行简报和 manifest`

正文：
我想要一个非常小的 GitHub Action，把普通 workflow 输入整理成后续 agent 或人工可以直接接手的交付物。

`github-agent-action` 会输出：
- Markdown 执行简报
- JSON manifest
- 供后续步骤继续消费的 GitHub output 路径

仓库：
https://github.com/ToolmeshAI/github-agent-action
