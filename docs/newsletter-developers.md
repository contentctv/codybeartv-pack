# Developers list — newsletter stub

**Track:** Developers (people who will install the pack).  
**Do not send this body to the New to Grok list.** Same footer as the other track, different body.

Phase 5 copy only. No live mailer. No Stripe secret. No Discord bot token. GitHub collaborator invites are **not** implemented.

---

Subject: CodyBearTV pack notes — rotation Wednesday, unofficial CapCut still community

Body:

You are on the **Developers** list.

This week:

- Token rotation is **Wednesday 16:00 UTC** (24h grace). You get the current public newsletter or trial token only. Paid monthly seats come from Stripe webhooks later, not this mail. We will not email admin tokens.
- Connector diffs (stubs, not live): `/imagine` poller is fake jobs only — no `api.x.ai`. `/capcut` prints unofficial `create_draft` / `add_video` / `add_text` / `save_draft`. CapCut has **no official public editing API**. Human still exports in CapCut Pro.
- Storefront checkout stays **TEST MODE** and disabled. No live Payment Link until a human approves spend.
- GitHub and Discord links on the site are placeholders. Invites are not wired.

Install reminder (official): `curl -fsSL https://x.ai/cli/install.sh | bash` then `grok` in the pack repo. Brain model is `grok-4.6`. Do not assume Grok 4.7.

Changelog this phase: Phase 5 static landing + these two newsletter files. No git push from the agent.

---

Footer (shared):

CodyBearTV developer pack · Jacó / Phoenix · Official docs first: docs.x.ai/build · help.x.com Original Content Rewards · US payouts: X Money after 2026-09-07 · Unsubscribe later · This is not a live send.
