# Token-gate design

**Phase:** 2 (design + fake-token stub).  
**Skills:** `redhat-security-gate`, `developer-newsletter-engine`.  
**Not in this phase:** Stripe API, live webhooks, Discord roles, GitHub collaborator invites, spend.

Human approval is still required before any spend, refund, live key, or invite.

---

## Official vs community

| Piece | Status |
|---|---|
| Stripe Checkout / Billing webhooks (later) | Official — [docs.stripe.com](https://docs.stripe.com/payments/checkout) |
| Pack-issued trial token | Community / pack — not Stripe, not xAI |
| Pack-issued rotating newsletter token | Community / pack — mailed on rotation day |
| GitHub / Discord grants | Official vendor APIs — **not implemented** |

Model IDs stay in config (`grok-4.6`). Do not invent `grok-4.7`.

---

## Three token types

### 1. One-week trial

| Field | Rule |
|---|---|
| Issuer | Pack (local fixture today) |
| TTL | 7 days from `issued_at` |
| Scope | Public-core docs + Imagine **dry-run** docs only. No live Imagine, no CapCut write, no Discord send |
| Audience | Landing-page signups (either list track) |
| Rotate? | No. Expires. Re-issue is a new token, not a rotation |
| Revoke | Immediate on abuse or operator flag |
| Mail | May appear in the **current** public trial mail. Never an admin token |

### 2. Rotating newsletter token

| Field | Rule |
|---|---|
| Issuer | Pack cron / operator on a **fixed weekday** (see `ROTATION.md`) |
| TTL | Until next rotation day (inclusive of grace hours documented there) |
| Scope | Changelog, connector diffs, current public trial **or** the week's newsletter token. No paid modules |
| Audience | Dual lists — **Developers** vs **New to Grok**. Same footer, different body. Never mix send payloads |
| Rotate? | Yes. Old newsletter token denies after rotation + grace |
| Revoke | Rotation replaces it. Do not email a backlog of old tokens |
| Mail | Current public token only. Paid monthly tokens **do not** come from this cron |

### 3. Monthly Stripe entitlement

| Field | Rule |
|---|---|
| Issuer | Stripe (future). Stub uses a fake `entitlement_id`, never `sk_live` / `sk_test` |
| TTL | Current billing period; renew on `invoice.paid`; drop on `customer.subscription.deleted` / `charge.refunded` |
| Scope | Paid pack modules (`/imagine` poller, `/capcut` wrapper, `/tokens` admin tools). Still HITL on spend |
| Audience | Checkout with GitHub handle **required at paid checkout only** |
| Rotate? | No calendar rotation. Lifecycle is the subscription |
| Revoke | Stripe cancel / refund webhook — **later**. This phase does not call Stripe |
| Mail | Entitlement notice may mention “your paid seat is active.” The raw token is not a newsletter blast |

---

## Check algorithm (default deny)

```
input: presented_token, now, requested_scope
if token missing or unknown → DENY
if status != active → DENY
if now > expires_at → DENY
if requested_scope not in token.scopes → DENY
else ALLOW (log token id, not the secret)
```

Parameterized lookup only. Never concatenate the presented string into a shell command. Treat the token as untrusted input (OWASP MCP01 — do not persist it into model context or logs).

Local models never receive production secrets. This stub has no production secrets.

---

## Future Stripe webhook (not implemented)

When Phase 3+ is approved:

1. Verify Stripe signature before any mutation.
2. Map `checkout.session.completed` / `invoice.paid` → mint or extend **monthly entitlement**.
3. Map `customer.subscription.deleted` → revoke entitlement.
4. GitHub collaborator invite and Discord role sync stay **behind a second human-approved job**. This design does not implement them.

Test-mode Stripe only until the operator approves live keys.

---

## Out of scope (explicit)

- Calling Stripe
- Real API keys in repo
- Discord invites
- GitHub invites
- Imagine / CapCut / Polymarket live
- Git commit or push
