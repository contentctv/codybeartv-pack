# /tokens

Phase 2: token-gate **design** only. No Stripe calls. No live keys. No Discord or GitHub invites.

**Official vs community:** Paid entitlement will later come from official Stripe webhooks (Checkout / Billing). Trial and newsletter tokens are pack-issued, short-lived, and stored as **fake fixtures** in this phase. Not an xAI product.

**Phase 0 / Phase 2 limits:**

- Default deny. Token-gate every paid tool when connectors exist.
- Newsletter token rotates on a fixed weekday (see `ROTATION.md`). Paid token is **not** minted by that cron — Stripe webhook later.
- Revoke paid access on Stripe cancel (webhook, not implemented).
- Human approval before any spend. No Stripe secret keys in files, logs, or chat.
- Do not mix Developer vs New-to-Grok newsletter payloads.
- Do not put long-lived admin tokens in email.

## Files

| Path | Role |
|---|---|
| `DESIGN.md` | Three token types, gates, future webhook shape |
| `ROTATION.md` | Calendar: newsletter weekday vs paid webhook |
| `license_check.py` | Stub checker — local fake tokens only, no network |
| `fixtures/fake_tokens.json` | Obviously fake records. Not secrets. |

## Run the stub

```bash
python3 tokens/license_check.py
```

Expected: trial and newsletter fakes allow named scopes; unknown tokens deny; no HTTP.
