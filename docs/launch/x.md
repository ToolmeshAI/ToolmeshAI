# X Launch Copy

## English

### Post 1: `mcp-saas-foundry`

Built `mcp-saas-foundry` because too many MCP repos stop at toy demos.

This one starts where teams actually need help:
- starter blueprint
- zero-dependency Node template
- concrete SaaS/internal API examples
- release-readiness checklist

Repo:
https://github.com/ToolmeshAI/mcp-saas-foundry

### Post 2: `mcp-smoke-test`

Built `mcp-smoke-test` because MCP repos still miss a simple answer to one basic question:
does the server actually start, initialize, and answer a real probe?

This CLI checks that over stdio:
- initialize
- initialized notification
- a follow-up probe like `tools/list`
- text or JSON output for CI and local debugging

Repo:
https://github.com/ToolmeshAI/mcp-smoke-test

### Post 3: `safe-mcp-config`

`safe-mcp-config` is a small CLI for one annoying real problem:
MCP configs get copied into docs, issues, repos, and screenshots before anyone checks them.

It catches:
- inline secrets
- dangerous shell usage
- wildcard env passthrough

Repo:
https://github.com/ToolmeshAI/safe-mcp-config

### Post 4: `docs-to-context`

`docs-to-context` turns scattered docs into one clean Markdown context bundle for coding agents and LLM workflows.

No runtime deps.
Works on mixed files/directories.
Useful immediately if you keep feeding repos into AI tools.

Repo:
https://github.com/ToolmeshAI/docs-to-context

### Post 5: `browser-agent-starter`

`browser-agent-starter` is the repo I wanted before writing browser-agent demos from scratch.

It gives you:
- a shared run config
- dry-run planning for real workflows
- structured artifacts
- a clean seam for Playwright-style execution later

Repo:
https://github.com/ToolmeshAI/browser-agent-starter

### Post 6: portfolio thread

I renamed the account to `ToolmeshAI` and started a tighter open-source portfolio around:
- MCP tooling
- safer config workflows
- docs-to-context pipelines
- browser-agent recipes

Start here:
https://github.com/ToolmeshAI

## 中文

### 帖子 1：`mcp-saas-foundry`

我做了一个 `mcp-saas-foundry`，因为很多 MCP 仓库都停在 demo 层。

这个仓库直接从团队真正需要的部分开始：
- starter blueprint
- 零依赖 Node 模板
- SaaS / 内部 API 示例
- 发布前检查清单

仓库：
https://github.com/ToolmeshAI/mcp-saas-foundry

### 帖子 2：`mcp-smoke-test`

我做了一个 `mcp-smoke-test`，因为现在很多 MCP 仓库都还缺一个简单但关键的问题答案：
这个 server 到底能不能真的启动、initialize，并返回一次真实 probe？

这个 CLI 会通过 stdio 去检查：
- initialize
- initialized notification
- `tools/list` 这种后续 probe
- 同时支持 text / JSON 输出，方便本地和 CI

仓库：
https://github.com/ToolmeshAI/mcp-smoke-test

### 帖子 3：`safe-mcp-config`

`safe-mcp-config` 解决的是一个很烦但很真实的问题：
MCP 配置经常在没人检查之前，就已经被复制进文档、issue、仓库和截图里了。

它能抓：
- 内联 secret
- 危险 shell 调用
- 环境变量通配透传

仓库：
https://github.com/ToolmeshAI/safe-mcp-config

### 帖子 4：`docs-to-context`

`docs-to-context` 用来把分散文档打成一份干净的 Markdown 上下文包，方便喂给 coding agent 和 LLM 工作流。

零运行时依赖。
支持混合文件/目录输入。
只要你在给 AI 工具喂仓库文档，它就能立刻派上用场。

仓库：
https://github.com/ToolmeshAI/docs-to-context

### 帖子 5：`browser-agent-starter`

`browser-agent-starter` 是我想要的那种 browser agent 起步仓库：不是空 scaffold，也不假装自己已经是完整自动化引擎。

它现在提供：
- 统一 run config
- 面向真实 workflow 的 dry-run 规划
- 结构化产物
- 后续接 Playwright 的清晰接缝

仓库：
https://github.com/ToolmeshAI/browser-agent-starter

### 帖子 6：作品集串帖

我把账号改成了 `ToolmeshAI`，然后开始更聚焦地做一套开源作品集，方向包括：
- MCP tooling
- 更安全的配置工作流
- docs-to-context pipeline
- browser-agent recipe

入口：
https://github.com/ToolmeshAI
