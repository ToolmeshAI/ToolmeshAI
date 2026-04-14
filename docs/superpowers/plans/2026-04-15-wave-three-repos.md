# Third Wave Repositories Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Launch three search-friendly repos that expand the ToolmeshAI portfolio into `llms.txt`, HTTP MCP smoke testing, and GitHub-native agent workflow automation.

**Architecture:** Build three independent Node-first repositories so they can ship in parallel and cross-link cleanly. Each repo gets a small CLI or Action core, bilingual docs, release notes, and GitHub-ready community files; the profile repo then updates the launch queue and portfolio README to route traffic into the new repos.

**Tech Stack:** Node.js 20, built-in `node:test`, zero or minimal runtime dependencies, Markdown docs, GitHub Actions workflow YAML.

---

### Task 1: `llms-txt-check`

**Files:**
- Create: `llms-txt-check/package.json`
- Create: `llms-txt-check/bin/llms-txt-check.js`
- Create: `llms-txt-check/src/cli.js`
- Create: `llms-txt-check/src/check.js`
- Create: `llms-txt-check/test/check.test.js`
- Create: `llms-txt-check/examples/good/llms.txt`
- Create: `llms-txt-check/examples/bad/llms.txt`
- Create: `llms-txt-check/README.md`
- Create: `llms-txt-check/README.zh-CN.md`
- Create: `llms-txt-check/docs/releases/v0.1.0.md`
- Create: `llms-txt-check/.github/workflows/ci.yml`

- [ ] Write failing tests for valid, warning, and failing `llms.txt` cases.
- [ ] Run `npm test` and verify the new tests fail for the expected missing-module reason.
- [ ] Implement the smallest parser/checker that validates heading presence, section order, link formatting, and missing summary lines.
- [ ] Implement CLI flags for `--file`, `--format text|json`, and nonzero exit on errors.
- [ ] Re-run `npm test` and `npm pack --dry-run`.
- [ ] Add bilingual README, examples, release note, and community files.
- [ ] Commit with `feat: add llms txt checker`.

### Task 2: `mcp-http-smoke`

**Files:**
- Create: `mcp-http-smoke/package.json`
- Create: `mcp-http-smoke/bin/mcp-http-smoke.js`
- Create: `mcp-http-smoke/src/cli.js`
- Create: `mcp-http-smoke/src/http-smoke.js`
- Create: `mcp-http-smoke/test/http-smoke.test.js`
- Create: `mcp-http-smoke/test/fixtures/fake-http-mcp-server.js`
- Create: `mcp-http-smoke/examples/request.headers.json`
- Create: `mcp-http-smoke/README.md`
- Create: `mcp-http-smoke/README.zh-CN.md`
- Create: `mcp-http-smoke/docs/releases/v0.1.0.md`
- Create: `mcp-http-smoke/.github/workflows/ci.yml`

- [ ] Write failing tests for successful initialize flow, auth header passthrough, and probe failure handling.
- [ ] Run `npm test` and verify the new tests fail before implementation exists.
- [ ] Implement minimal HTTP JSON-RPC smoke logic around `initialize`, `notifications/initialized`, and one capability probe.
- [ ] Implement CLI flags for `--url`, repeatable `--header`, `--format text|json`, and configurable probe timeout.
- [ ] Re-run `npm test` and `npm pack --dry-run`.
- [ ] Add bilingual README, local fixture instructions, release note, and community files.
- [ ] Commit with `feat: add http mcp smoke tester`.

### Task 3: `github-agent-action`

**Files:**
- Create: `github-agent-action/action.yml`
- Create: `github-agent-action/package.json`
- Create: `github-agent-action/src/index.js`
- Create: `github-agent-action/src/brief.js`
- Create: `github-agent-action/test/index.test.js`
- Create: `github-agent-action/examples/workflow.yml`
- Create: `github-agent-action/README.md`
- Create: `github-agent-action/README.zh-CN.md`
- Create: `github-agent-action/docs/releases/v0.1.0.md`
- Create: `github-agent-action/.github/workflows/ci.yml`

- [ ] Write failing tests for markdown brief generation, JSON manifest generation, and default output path handling.
- [ ] Run `npm test` and verify the tests fail before implementation exists.
- [ ] Implement the smallest Node-based GitHub Action that reads inputs, writes a bilingual-ready execution brief, and exposes output paths.
- [ ] Add a sample workflow and honest README that explains where this fits in an agent-assisted GitHub workflow.
- [ ] Re-run `npm test` and `npm pack --dry-run`.
- [ ] Add release note and community files.
- [ ] Commit with `feat: add github agent action`.

### Task 4: Portfolio Integration

**Files:**
- Modify: `ToolmeshAI/README.md`
- Modify: `ToolmeshAI/README.zh-CN.md`
- Modify: `ToolmeshAI/docs/launch/README.md`
- Modify: `ToolmeshAI/docs/launch/launch-queue.md`
- Modify: `PORTFOLIO.md`

- [ ] Add the three new repos to the portfolio matrix and launch order.
- [ ] Update homepage copy so the new repos strengthen the MCP/docs/browser/GitHub workflow story instead of fragmenting it.
- [ ] Re-check links and sequencing for wave-three promotion.

### Task 5: Verification and Publish Prep

**Files:**
- Modify: each new repo `.gitignore`, social/demo assets, and release metadata as needed

- [ ] Run each repo’s `npm test`.
- [ ] Run each repo’s `npm pack --dry-run`.
- [ ] Create initial git commits in each new repo.
- [ ] Create GitHub remotes under `ToolmeshAI`, push `main`, set descriptions/topics, create `v0.1.0` releases, and upload social preview images.
