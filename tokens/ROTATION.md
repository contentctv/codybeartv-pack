# Rotation calendar

Pack-issued newsletter tokens rotate on a **fixed weekday**. Paid tokens do **not**.

Default timezone: **UTC**. Operator can change the weekday in this file; do not rotate from chat.

## Newsletter token (type 2)

| Setting | Value |
|---|---|
| Weekday | **Wednesday** |
| Time | 16:00 UTC |
| Grace | 24 hours after rotation — previous token still accepted so late readers are not locked out mid-send |
| After grace | Previous newsletter token → `rotated` → DENY |
| Who gets mail | Both lists, **separate bodies**: Developers (changelog, connector diffs, rotation notice) vs New to Grok (official-first tutorials, Imagine limits). Same footer |
| What is mailed | The **current** newsletter token or public trial — never a paid entitlement, never an admin token |

This phase has no cron job. The weekday is the contract for a later scheduler.

## One-week trial (type 1)

No weekday rotation. Clock starts at `issued_at`. Dies at `issued_at + 7 days`. A new trial is a new id.

## Monthly Stripe entitlement (type 3)

**Not on this calendar.** Mint / renew / revoke from Stripe webhooks later (`invoice.paid`, `customer.subscription.deleted`). Newsletter Wednesday must never mint a paid seat.

## Cadence (security gate)

| Job | Frequency | This phase |
|---|---|---|
| Newsletter rotate | weekly, Wednesday 16:00 UTC | notes only |
| Rehash manifests | every session start | `/security` later |
| Revoke on Stripe cancel | on webhook | not implemented |
| Dependency audit | weekly | not this folder |

Human approval still required before any spend.
