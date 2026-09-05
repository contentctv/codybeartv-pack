# CodyBearTV pack

Developer-facing stubs for a Grok 4.6 + Grok Build + Grok Imagine + Grok Bot workflow.
Public repo is the free core. Paid modules stay out of this tree until they exist.

**Status:** research and offline stubs only. No live Stripe charges. No live Imagine API calls. No Discord bot. No CapCut Pro export. No Polymarket live orders.

Official research (read this first): [research/RESEARCH.md](research/RESEARCH.md)

Project rules for Grok Build: [AGENTS.md](AGENTS.md)

## What this is

A pack a developer can clone, then grow:

1. Grok 4.6 researches and writes shot prompts.
2. Imagine (later) generates clips and extends from the last frame.
3. A community CapCut draft planner (later) assembles a draft. A human finishes in CapCut Pro.
4. Token types, a static storefront, and two newsletter tracks are designed, not wired to production.

Target customer is a developer (novice through professional), not a general consumer.

## What does not exist

Do not document or invent these:

- Grok 4.7 (not on official model lists as of 2026-09-05)
- An official Grok Imagine ↔ CapCut plugin
- An official GarageBand public editing API
- A documented SuperCool public MCP URL

CapCut and GarageBand bridges in this repo are **community / unofficial**. Label them that way in every README and call site.

## Layout

| Path | Role |
| --- | --- |
| `research/` | Phase 0 official-first notes |
| `core/` | Orchestrator (stub) |
| `imagine/` | Async generate → poll → last-frame extend stub |
| `capcut/` | Unofficial draft planner stub |
| `garageband/` | macOS AppleScript note only |
| `tokens/` | Fake trial / newsletter / monthly license check |
| `storefront/` | Static landing page, Stripe button disabled TEST MODE |
| `docs/` | Dual-track newsletter copy |
| `bots/` | Grok Bot crew notes |
| `discord/` | Bot notes, no token |
| `polymarket/` | Paper-only until `GATE_LIFT LIVE_TRADING` |
| `supercool/` | Unofficial wrapper placeholder |
| `x-monetize/` | Original Content Rewards + X Money direction |
| `security/` | Skill hashes, allowlist, healer ticket template |

## Hard gates

- Human approval before git push to a new remote, Stripe live mode, Discord send, live CLOB, wallet spend, or DNS change.
- Never commit `XAI_API_KEY`, Stripe secrets, Discord bot tokens, or seed phrases.
- Imagine jobs are async. Last-frame extend output is capped at 720p on current official docs.
- Polymarket default is paper.
- X Creator Revenue Sharing retired 2026-09-07. US payouts go through X Money. Original Content Rewards is the new rail. Automated posts are ineligible.

## Local use

```bash
git clone https://github.com/contentctv/codybeartv-pack.git
cd codybeartv-pack
python3 tokens/license_check.py
python3 imagine/poller.py
python3 capcut/draft_builder.py
```

Those scripts use `FAKE` fixtures only. They do not call `api.x.ai` or Stripe.

Grok Build skills used to author this pack live in `.grok/skills/` on the operator machine. That folder is not in this public repo yet.

## Install Grok Build (official)

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
```

Docs: [Grok Build overview](https://docs.x.ai/build/overview)

## License

No license file yet. Treat the public tree as source-available stubs until a LICENSE is added. No warranty.
