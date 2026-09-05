# Allowlist

**Default deny.** Phase 6 stub — placeholders only. Not applied to host firewall, Discord, or MCP runtime. Do not change firewall rules from this file.

**Official vs community:** Pack gate (Red Hat-style). Aligns with Grok Build permissions/sandbox and OWASP MCP Top 10. Community CapCut tools stay unofficial if ever enabled.

## Repo

| Field | Value |
|---|---|
| Git remote | unset this phase — no push |
| Collaborator invites | deny until human approval |
| GitHub PAT | env only, fine-grained, repo-scoped, invite permission only **later** |

## Discord guild

| Field | Value |
|---|---|
| Guild id | `GUILD_PLACEHOLDER` — not a real id |
| Bot token | host env only; never in this repo |
| Message send | deny |
| Role sync | deny until Stripe webhook signature verified |

## IP / webhook sources

| Source | Rule |
|---|---|
| Stripe webhooks | deny until signature verify (official Stripe docs later) |
| GitHub webhooks | deny until signature verify |
| Unknown IPs | deny |
| Local loopback for stubs | allow `127.0.0.1` / `::1` for local Python stubs only — **do not bind `0.0.0.0`** |

This list is documentation. It does not call `pfctl`, `iptables`, or cloud security groups.

## MCP / unofficial tool names

Default deny. Names below are the only ones the pack stubs talk about. **None are connected this phase.**

| Name | Status |
|---|---|
| `create_draft` | unofficial CapCut — stub print only |
| `add_video` | unofficial CapCut — stub print only |
| `add_text` | unofficial CapCut — stub print only |
| `save_draft` | unofficial CapCut — stub print only |

Forbidden until explicit operator enable: live Imagine (`client.video.generate` / `extend`), Stripe spend, Discord send, live Polymarket CLOB, GarageBand bridge, invented SuperCool MCP URL, `npx` CapCut servers.

If an agent retries a forbidden tool: rate-limit, log the **tool name**, notify the operator, do not escalate privileges.

## Secrets

Never in files: Stripe secret keys, Discord bot tokens, private keys, seed phrases, `XAI_API_KEY`. Local models never receive production secrets.
