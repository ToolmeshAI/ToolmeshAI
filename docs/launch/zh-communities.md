# Chinese Community Launch Copy

## English

This file is the China-focused launch pack for developer communities where a Chinese-first post performs better than a translated X thread.

Use it for:

- V2EX
- Juejin
- Xiaohongshu or Shaoshu-style productivity/dev circles when relevant
- Chinese-speaking Telegram, Discord, and WeChat developer groups

The recommended order is still flagship-first:

1. `mcp-saas-foundry`
2. `mcp-smoke-test`
3. `safe-mcp-config`
4. `docs-to-context`
5. `llms-txt-check`
6. `mcp-http-smoke`
7. `browser-agent-starter`
8. `github-agent-action`
9. `ToolmeshAI`

---

## 建议渠道

- V2EX
- 掘金
- 少数派社区里的开发/效率相关板块
- 即刻 / X 中文开发者圈
- 微信群 / Telegram / Discord 中的 AI 工具和开发者群

## 主推顺序

1. `mcp-saas-foundry`
2. `mcp-smoke-test`
3. `safe-mcp-config`
4. `docs-to-context`
5. `llms-txt-check`
6. `mcp-http-smoke`
7. `browser-agent-starter`
8. `github-agent-action`
9. `ToolmeshAI`

## 长帖模板

这两天把 GitHub 账号重新整理成了 `ToolmeshAI`，开始集中做一批更像“能拿来用”的项目，而不是继续铺很多空壳仓库。

现在最适合先推的 8 个是：

1. `mcp-saas-foundry`
   一个可 fork 的 SaaS 向 MCP starter blueprint，目标是补上“玩具 demo”和“团队能直接起步的 starter”之间的空白。

2. `mcp-smoke-test`
   一个零依赖 CLI，用来验证 stdio MCP server 是否真的能启动、initialize，并完成一次基础 probe。

3. `safe-mcp-config`
   一个零依赖 CLI，在分享 MCP 配置之前先抓高风险模式，比如内联 token、危险 shell 调用、环境变量通配透传。

4. `docs-to-context`
   一个零依赖 CLI，把散落文档打成一份干净的 Markdown 上下文，方便直接喂给 coding agent / LLM 工作流。

5. `llms-txt-check`
   一个零依赖 CLI，用来在 `llms.txt` 公开前先检查标题、摘要、链接和常见结构问题。

6. `mcp-http-smoke`
   一个轻量 HTTP MCP smoke tester，用来确认 endpoint 能完成 `initialize`、接受 `initialized`，并返回一次真实 capability probe。

7. `browser-agent-starter`
   一个 browser-ready 的最小 starter，用 dry-run 规划和结构化产物把 browser agent workflow 先做成可信的起点。

8. `github-agent-action`
   一个小型 GitHub Action，把 workflow 输入整理成可复用的执行简报和 JSON manifest，方便后续 agent 或人工接手。

GitHub:
https://github.com/ToolmeshAI

## 短帖模板

### `mcp-saas-foundry`

我做了一个 `mcp-saas-foundry`，目标不是再做一个 MCP demo，而是做一个团队真能 fork 的 starter blueprint。

仓库：
https://github.com/ToolmeshAI/mcp-saas-foundry

### `safe-mcp-config`

`safe-mcp-config` 是个很小的 CLI，专门在分享 MCP 配置前先抓危险模式，适合放到 CI 或本地自检里。

仓库：
https://github.com/ToolmeshAI/safe-mcp-config

### `mcp-smoke-test`

`mcp-smoke-test` 用来回答一个最基础的问题：这个 MCP server 到底能不能真的跑起来，并且完成一次 probe。

仓库：
https://github.com/ToolmeshAI/mcp-smoke-test

### `docs-to-context`

`docs-to-context` 用来把文档打成一份 agent 能直接吃的 Markdown 上下文包，省掉手工整理。

仓库：
https://github.com/ToolmeshAI/docs-to-context

### `llms-txt-check`

`llms-txt-check` 用来在 `llms.txt` 公开前先检查标题、摘要、链接和重复标题，适合做最小但高价值的仓库上下文自检。

仓库：
https://github.com/ToolmeshAI/llms-txt-check

### `mcp-http-smoke`

`mcp-http-smoke` 是 HTTP 侧的 MCP smoke tester，适合在 endpoint 对外之前先确认 `initialize`、`initialized` 和 capability probe 都正常。

仓库：
https://github.com/ToolmeshAI/mcp-http-smoke

### `browser-agent-starter`

`browser-agent-starter` 提供一个更可信的 browser agent 起步结构：有 shared config、有 dry-run 规划、有结构化产物，不是空壳。

仓库：
https://github.com/ToolmeshAI/browser-agent-starter

### `github-agent-action`

`github-agent-action` 把 workflow 输入整理成执行简报和 manifest，适合给后续 agent 或人工流程做 handoff。

仓库：
https://github.com/ToolmeshAI/github-agent-action
