# /storefront

Phase 5: static landing stub. GitHub Pages later. **No live Stripe Payment Link.**

**Official vs community:** Official Stripe Checkout (later, test mode first) and GitHub Pages. This `index.html` is pack-local static markup. Newsletter tracks follow `developer-newsletter-engine`.

**Phase 0 / Phase 5 limits:**

- Stripe button is **disabled** and labeled TEST MODE. No Payment Link URL. No `sk_live` / `sk_test` in files.
- Discord and GitHub are placeholder anchors (`#placeholder-discord`, `#placeholder-github`). No bot token, no invite send.
- Form does not POST. Dual tracks: Developers vs New to Grok — never mix send payloads.
- GitHub handle optional on this page; required only at paid checkout later.
- Human approval before any spend. Do not bind a public server to `0.0.0.0` for this stub.
- Webhooks (later) must verify Stripe / GitHub signatures before any role or invite.

## Files

| Path | Role |
|---|---|
| `index.html` | CodyBearTV developer pack landing stub |

Copy for the two lists lives in `/docs/newsletter-developers.md` and `/docs/newsletter-new-to-grok.md`.
