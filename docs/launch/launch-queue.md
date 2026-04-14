# Launch Queue

This file turns the current launch kit into an execution queue for manual posting or future automation handoff.

Status snapshot: April 15, 2026

- Current browser sessions are not logged into `X`, `Hacker News`, or `V2EX`.
- `Reddit` is currently blocked by a prove-human gate in the active browser session.
- Use this file as the control document once accounts are available.

## Platform Status / 平台状态

| Platform | Current status | Direct URL | First target | Next action |
| --- | --- | --- | --- | --- |
| X | Blocked until login | https://x.com/compose/post | `mcp-saas-foundry` | Log in, post from [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), then queue follow-ups. |
| Hacker News | Blocked until login | https://news.ycombinator.com/submit | `mcp-saas-foundry` | Log in, submit the flagship repo first, then wait before any second HN launch. |
| Reddit | Blocked by prove-human gate in current session | https://www.reddit.com/submit | `mcp-saas-foundry` | Retry in a clean logged-in browser profile, or wait until the gate clears, then submit to one relevant subreddit at a time. |
| V2EX | Blocked until login | https://www.v2ex.com/new | `mcp-saas-foundry` | Log in, post the Chinese long-form version, and choose the most relevant node manually. |
| Juejin | Available if account is ready | https://juejin.cn/editor/drafts/new/v2 | `mcp-saas-foundry` | Use the Chinese long-form framing from [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md). |
| Chinese groups | Manual only | No universal composer URL | Portfolio summary | Use the long-form Chinese post or short repo blurbs in Telegram, Discord, or WeChat groups. |

Direct prefill patterns where supported:

- Hacker News: `https://news.ycombinator.com/submitlink?u=<repo-url>&t=<title>`
- Reddit: `https://www.reddit.com/submit?url=<repo-url>&title=<title>`

## Recommended Posting Order / 建议发帖顺序

Use one flagship repo at a time. The current priority should stay:

1. `mcp-saas-foundry`
2. `mcp-smoke-test`
3. `safe-mcp-config`
4. `docs-to-context`
5. `browser-agent-starter`
6. `ToolmeshAI` portfolio/org post
7. `awesome-mcp-workflows`
8. `browser-agent-recipes`

Execution sequence:

1. Launch `mcp-saas-foundry` on `Hacker News` first if the account is available.
2. Post the matching `X` version the same day or the next day.
3. Use `Reddit` once the prove-human gate is cleared.
4. Push the Chinese long-form version to `V2EX` or `Juejin`.
5. Move to `mcp-smoke-test` once the flagship repo has opened the MCP tooling conversation.
6. Move to `safe-mcp-config` after `mcp-smoke-test`.
7. Move to `docs-to-context` after `safe-mcp-config`.
8. Use `browser-agent-starter` once browser-agent interest appears in replies or adjacent channels.
9. Use the `ToolmeshAI` portfolio thread and Chinese long post to cross-link the rest of the portfolio.
10. Keep `awesome-mcp-workflows` and `browser-agent-recipes` as secondary links unless a platform-specific conversation clearly fits them.

Practical spacing:

- Do not stack multiple `Hacker News` launches close together.
- Prefer one primary repo post per platform per day.
- Use comments, replies, and follow-up posts to mention secondary repos instead of opening with them.

## Per-Platform Queue

### X

- Composer: https://x.com/compose/post
- Copy source: [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md)
- Posting order:
  1. `mcp-saas-foundry`
  2. `mcp-smoke-test`
  3. `safe-mcp-config`
  4. `docs-to-context`
  5. `browser-agent-starter`
  6. `ToolmeshAI` portfolio thread
- Next action:
  Log in, paste the matching copy, attach one repo hero asset if available, and keep each post focused on one repo.

### Hacker News

- Submit: https://news.ycombinator.com/submit
- Prefill pattern: `https://news.ycombinator.com/submitlink?u=<repo-url>&t=<title>`
- Copy source: [hacker-news.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/hacker-news.md)
- Posting order:
  1. `Show HN: mcp-saas-foundry – a forkable starter blueprint for SaaS-focused MCP servers`
  2. `Show HN: mcp-smoke-test – verify that a stdio MCP server actually initializes and answers a probe`
  3. `Show HN: safe-mcp-config – scan MCP configs for risky patterns before sharing them`
  4. `Show HN: docs-to-context – bundle scattered docs into one Markdown context file for coding agents`
- Next action:
  Log in, submit only `mcp-saas-foundry` first, and hold the other two until there is enough time between launches.

### Reddit

- Submit: https://www.reddit.com/submit
- Prefill pattern: `https://www.reddit.com/submit?url=<repo-url>&title=<title>`
- Copy source: [reddit.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/reddit.md)
- Suggested communities:
  `r/mcp`, `r/LocalLLaMA`, `r/programming`, `r/node`, plus niche communities that allow self-promo
- Next action:
  Clear the prove-human gate first. Then submit one repo per subreddit, starting with `mcp-saas-foundry`, then `mcp-smoke-test`.

### V2EX

- New topic: https://www.v2ex.com/new
- Copy source: [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md)
- First target:
  `mcp-saas-foundry`, then the 3-repo long post if the node allows broader sharing
- Next action:
  Log in, choose the right node manually, and lead with the practical SaaS starter angle rather than the whole portfolio at once.

### Juejin

- Editor: https://juejin.cn/editor/drafts/new/v2
- Copy source: [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md)
- First target:
  the 3-repo long-form summary
- Next action:
  Turn the long post into a more explanatory article, then add direct repo links near the top.

## Repo-by-Repo Queue

| Priority | Repo | Primary link | Launch angle | First platform | Copy source | Operator note |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `mcp-saas-foundry` | https://github.com/ToolmeshAI/mcp-saas-foundry | Strongest flagship: forkable SaaS-focused MCP starter | Hacker News | [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), [reddit.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/reddit.md), [hacker-news.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/hacker-news.md), [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md) | Use this repo to open every platform where possible. |
| 2 | `mcp-smoke-test` | https://github.com/ToolmeshAI/mcp-smoke-test | Fast interoperability check for MCP builders | X or Hacker News | [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), [reddit.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/reddit.md), [hacker-news.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/hacker-news.md), [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md) | Best second wave if MCP builders ask “how do I verify my server?” |
| 3 | `safe-mcp-config` | https://github.com/ToolmeshAI/safe-mcp-config | Small CLI, clear pain point, easy follow-up launch | X | [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), [reddit.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/reddit.md), [hacker-news.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/hacker-news.md), [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md) | Good third wave once the MCP validation angle lands. |
| 4 | `docs-to-context` | https://github.com/ToolmeshAI/docs-to-context | Clean utility angle for coding-agent workflows | X | [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), [reddit.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/reddit.md), [hacker-news.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/hacker-news.md), [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md) | Launch after `safe-mcp-config`, not before. |
| 5 | `browser-agent-starter` | https://github.com/ToolmeshAI/browser-agent-starter | Runnable browser-agent starter with dry-run artifacts | X or Reddit | [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), [reddit.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/reddit.md), [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md) | Use after some browser-agent curiosity is already present. |
| 6 | `ToolmeshAI` portfolio/org | https://github.com/ToolmeshAI | Cross-link the portfolio after the top repos are visible | X | [x.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/x.md), [zh-communities.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/zh-communities.md) | Use as a thread or long post, not as the first cold-start post. |
| 7 | `awesome-mcp-workflows` | https://github.com/ToolmeshAI/awesome-mcp-workflows | Secondary credibility/supporting repo | Replies, comments, or portfolio thread | [README.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/README.md) | Mention when someone asks for adjacent resources. |
| 8 | `browser-agent-recipes` | https://github.com/ToolmeshAI/browser-agent-recipes | Secondary supporting repo for browser-agent interest | Replies, comments, or portfolio thread | [README.md](/home/knox/workspace/github_work/ToolmeshAI/docs/launch/README.md) | Use as a related follow-up, not a first-wave launch. |

## Operator Checklist / 操作检查清单

- Confirm the target platform is logged in before opening the composer.
  确认目标平台已经登录，再打开发布页面。
- Open the repo landing page first and make sure the README hero and links are ready.
  先打开仓库首页，确认 README 首屏和链接状态正常。
- Post only one primary repo at a time.
  每次只主推一个仓库。
- Use the matching copy file instead of rewriting from scratch.
  直接使用对应文案文件，不要临时重写。
- Record the final post URL and platform outcome after each submission.
  每次发完后记录帖子链接和平台结果。
