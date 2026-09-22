---
name: official-first-research
description: Official-first research protocol for CodyBearTV. Use when scraping docs, comparing APIs, writing RESEARCH.md, or deciding if a connector is official vs community. Prefers xAI, X, Stripe, GitHub, Polymarket primary sources.
when-to-use: research, scrape docs, official docs, RESEARCH.md, Phase 0, verify API, source hierarchy
metadata:
  author: CodyBearTV
  short-description: Official-first scrape order
---

# Official-first research

Never treat a blog, YouTube transcript, or X thread as the source of truth for an API.

## Source ladder (always)

1. Official docs and product pages
   - https://docs.x.ai/build/overview
   - https://docs.x.ai/build/features/skills-plugins-marketplaces
   - https://docs.x.ai/build/features/mcp-servers
   - https://docs.x.ai/developers (Imagine video, extension, tools, pricing)
   - https://github.com/xai-org/plugin-marketplace
   - https://github.com/xai-org/grok-build
   - https://help.x.com/en/using-x/original-content-rewards
   - https://docs.polymarket.com
   - Stripe and GitHub official docs
2. Official SDKs and example repos (xai_sdk, Polymarket agents)
3. Community code that writes real files (capcut-cli, CapCutAPI, garageband-llm-bridge)
4. Secondary blogs / X posts — tag UNVERIFIED

## Procedure

1. List the question as a capability check (exists / does not exist / unofficial wrapper).
2. Fetch official pages before community pages.
3. Extract limits in a table — duration, resolution, rate limit, auth, official vs not.
4. If official docs contradict a blog, official wins. Note the date.
5. Write findings to `/research/RESEARCH.md` with citation URLs.

## Capability facts to keep current

- Grok Build is a terminal agent. Install `curl -fsSL https://x.ai/cli/install.sh | bash`. Skills live in `.grok/skills/` and `~/.grok/skills/`.
- Imagine video 1.5 — async jobs, 1–15s clips, 1080p on T2V/I2V. Extension uses last-frame continuity, output capped at 720p, input 2–15s, extend 2–10s.
- No official CapCut editing API. No official GarageBand API. No documented SuperCool public MCP (supercool.com / aiagency.supercool.com exist as products).
- Emergent public MCP — https://mcp.emergent.sh/
- Grok 4.6 is current. Do not invent Grok 4.7 endpoints.

## Output shape

```
Claim
Official source + date
Limit / constraint
Wrapper path if unofficial
Risk if we build on it
```
