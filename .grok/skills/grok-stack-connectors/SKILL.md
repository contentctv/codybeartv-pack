---
name: grok-stack-connectors
description: Connector map across Grok Build, Grok Bot, Grok 4.6 API, and Grok Imagine. Use when wiring MCP, plugins, bot teams, last-frame video chains, or explaining how the four Grok products talk.
when-to-use: connector, MCP, Grok Bot, Grok Imagine, last frame, plugin, wrapper, Imagine API, Grok Build MCP
metadata:
  author: CodyBearTV
  short-description: Build Bot Imagine API glue
---

# Grok stack connectors

The four products do not auto-share context. You glue them.

## How each product takes extensions

| Product | Where you add tools | Notes |
|---|---|---|
| Grok Build | `grok mcp add`, `.grok/skills/`, plugins, `~/.grok/config.toml` | Terminal agent. Best place to generate code and MCP servers. |
| Grok Bot | Marketplace plugins or ask the bot in chat | No config.toml MCP paste. Skills copy as SKILL.md packs. |
| Grok chat | grok.com/connectors custom MCP | Different surface from Build. |
| Grok 4.6 API | Tools in the request (web_search, x_search, code_interpreter, function calling, image_generation) | Brain for research and prompt fine-tune. |
| Grok Imagine API | `client.video.generate` / `client.video.extend` | Async. Poll. Do not block the TUI on a 3-minute render. |

## First connector to build

Imagine last-frame chain → CapCut draft.

1. Grok 4.6 researches and writes shot prompts.
2. Imagine generates clip 1 (I2V or T2V, prefer 1080p on 1.5).
3. Call video extend on the official last-frame endpoint for clips 2..N. Extension output is capped at 720p — plan resolution accordingly.
4. Download MP4s. Do not hand-write CapCut JSON.
5. Drive capcut-cli or a CapCut MCP (`create_draft`, `add_video`, `add_text`, `save_draft`).
6. Operator opens the draft in CapCut Pro. Human finishes export.

## Bot crew wiring

Share the same SKILL.md files with the Grok Bot team channel. Roles

- builder — runs Grok Build headless (`grok -p`) on approved tickets
- educator — answers novices from `/docs`
- moderator — Discord roles from Stripe webhooks only
- publisher — drafts X posts, never auto-posts

## Headless Build pattern

```bash
grok -p "Using grok-stack-connectors, draft the Imagine-to-CapCut poller. Do not call Imagine yet."
```

## Do not invent

- An official Grok Imagine ↔ CapCut plugin
- An official SuperCool MCP URL
- Automatic DNS / GoDaddy control from Grok Build unless an MCP for it is installed
