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

### `docs-to-context`

Title:
`docs-to-context: bundle scattered docs into one Markdown context file for coding agents`

Body:
This repo exists because feeding docs into AI workflows is still too manual.

`docs-to-context` takes mixed files/directories and emits one clean Markdown bundle with stable headings. Zero runtime deps.

Repo:
https://github.com/ToolmeshAI/docs-to-context

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

### `docs-to-context`

标题：
`docs-to-context：把散落文档打成一份给 coding agent 用的 Markdown 上下文`

正文：
这个仓库是因为“把文档喂给 AI”这件事现在还太手工。

`docs-to-context` 支持混合文件/目录输入，输出一份标题稳定的 Markdown bundle，而且零运行时依赖。

仓库：
https://github.com/ToolmeshAI/docs-to-context
