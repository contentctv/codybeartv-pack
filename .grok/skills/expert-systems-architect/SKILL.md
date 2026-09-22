---
name: expert-systems-architect
description: Architecture and implementation standard for the CodyBearTV monorepo. Use when scaffolding folders, designing APIs, writing AGENTS.md, choosing libraries, or reviewing diffs. Encodes pack structure and design rules, not generic coding tutorials.
when-to-use: scaffold, architecture, monorepo, design review, folder layout, API shape, AGENTS.md
metadata:
  author: CodyBearTV
  short-description: Pack architecture standard
---

# Expert systems architect

You already know how to code. This skill is the house style for this pack.

## Design rules

- Small public surface, large private core. Public repo teaches and attracts developers. Private repo holds paid modules.
- Wrappers over reverse-engineering. Prefer capcut-cli / Honorbox / Stripe webhooks over home-grown JSON mines.
- Config over hard-coded model IDs. Put `grok-4.6` in config.toml so a later model is a one-line swap.
- Plan mode before multi-file scaffolds. Show the tree, then write files.
- Every external call is typed, retried, and logged. Imagine jobs are async queues, not request-response.

## Target tree

```
/core            orchestrator, token middleware, model router
/imagine         poller, last-frame loop
/capcut          MCP wrapper around community draft tools
/garageband      macOS AppleScript bridge, clearly marked
/bots            SKILL.md packs for Grok Bot crew
/storefront      GitHub Pages + Stripe Payment Links
/discord         role sync + education bot
/tokens          trial / rotating newsletter / monthly Stripe
/polymarket      paper-first, GATE_LIFT for live
/supercool       unofficial wrapper + entrepreneurial corner
/x-monetize      Original Content Rewards + X Money direction
/security        integrity hashes, whitelist, healer tickets
/docs            amateur-to-pro tutorials
/research        Phase 0 output
```

## Review checklist

- Secrets only in env, never committed
- Token gate on every paid tool
- HITL on publish / spend / live trade
- Tests or a manual verify script for each wrapper
- README states official vs community for each connector

## Math and science stance

When a design needs math (Kelly sizing, rate limits, token budgets, queue backoff), load `quant-research-engine`. Do not invent formulas when a standard one exists. Cite the standard.
