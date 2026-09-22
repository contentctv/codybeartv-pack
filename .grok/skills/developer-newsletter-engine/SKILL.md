---
name: developer-newsletter-engine
description: Dual-track newsletter and education-bot copy for CodyBearTV. Use when building the landing-page signup, rotating-token mail, Discord education replies, or zero-to-hero developer onboarding. Developers first, Grok-newcomers second.
when-to-use: newsletter, Beehiiv, Resend, education bot, onboarding, zero to hero, developer list, CodyBearTV mail
metadata:
  author: CodyBearTV
  short-description: Newsletter and education routing
---

# Developer newsletter engine

Two lists, one site.

## Lists

| List | Who | What they get |
|---|---|---|
| Developers | People who will install the pack | Changelog, token rotation, GitHub invites, connector diffs |
| New to Grok | People entering the xAI / X ecosystem | Official-first tutorials, Premium vs Premium+, Imagine limits, Build install |

Never mix the two send payloads. Same footer, different body.

## Landing page fields

- Email
- Track radio (Developer / New to Grok)
- Optional GitHub handle (required only at paid checkout)
- Discord invite
- X profile link (optional — used later for Original Content Rewards coaching)

## Education bot rules

- Answer from `/docs` in this repo first.
- Then official xAI / X help URLs.
- Then named third-party courses with a clear "this is paid / this is free" label. Do not pretend CodyBearTV authored them.
- SuperCool, CapCut, Polymarket, Stripe — send the operator to that vendor's own developer or help page for account setup.
- Never invent a SuperCool MCP URL.

## Rotating token mail

Newsletter subscribers receive the current public trial or rotating token on the published rotation day. Paid monthly tokens come from Stripe webhooks, not from the newsletter cron. Do not put long-lived admin tokens in email.

## Voice

Direct, technical, no guru tone. CodyBearTV pack is a developer tool. Jacó / Phoenix branding may appear in the footer, not in every sentence.
