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
2. `safe-mcp-config`
3. `docs-to-context`
4. `ToolmeshAI`
5. `awesome-mcp-workflows`
6. `browser-agent-recipes`

---

## 建议渠道

- V2EX
- 掘金
- 少数派社区里的开发/效率相关板块
- 即刻 / X 中文开发者圈
- 微信群 / Telegram / Discord 中的 AI 工具和开发者群

## 主推顺序

1. `mcp-saas-foundry`
2. `safe-mcp-config`
3. `docs-to-context`
4. `ToolmeshAI`
5. `awesome-mcp-workflows`
6. `browser-agent-recipes`

## 长帖模板

这两天把 GitHub 账号重新整理成了 `ToolmeshAI`，开始集中做一批更像“能拿来用”的项目，而不是继续铺很多空壳仓库。

第一批里我最想先推 3 个：

1. `mcp-saas-foundry`
   一个可 fork 的 SaaS 向 MCP starter blueprint，目标是补上“玩具 demo”和“团队能直接起步的 starter”之间的空白。

2. `safe-mcp-config`
   一个零依赖 CLI，在分享 MCP 配置之前先抓高风险模式，比如内联 token、危险 shell 调用、环境变量通配透传。

3. `docs-to-context`
   一个零依赖 CLI，把散落文档打成一份干净的 Markdown 上下文，方便直接喂给 coding agent / LLM 工作流。

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

### `docs-to-context`

`docs-to-context` 用来把文档打成一份 agent 能直接吃的 Markdown 上下文包，省掉手工整理。

仓库：
https://github.com/ToolmeshAI/docs-to-context
