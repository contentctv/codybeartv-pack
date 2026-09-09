# PiggyWiggy the Hedgefund Companion by CodyBearTV

Status: PLUGIN DRAFT. PUBLISH=off. SOLICIT=off. MINT=off. LIVE_TRADING=false.
Desk code: BOT-ISA. Reports to BONES-CMD.
Not listed on the official xAI plugin marketplace until a human opens a PR
to [xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace)
after `GATE_LIFT EXECUTE_PUBLISH GROK_BOT_MARKETPLACE`.

## What this is

A Grok Build / Grok Bot **education** plugin for Cipher Coast Academy.

- Display name: **PiggyWiggy the Hedgefund Companion by CodyBearTV**
- Character title only. Not a hedge fund. Not an investment adviser. Not Professor Wiggley.
- SKU is tuition. SOP files and the Custom Connector are delivery rails for the same corpus.
- API tokens (`cca_...`) are login credentials, not securities.

## Public advertised tuition (locked)

- M0 $49
- Full academy bundle $599
- Agent bypass $899 (bundle + $300 connector seat)

## Install (local, not marketplace)

```bash
# from this pack
# Grok Build loads ./.grok/plugins/ automatically
```

Grok Bot: paste `artifacts/isa-academy/dist/publish/GROK-BOT-PROFILE.md` into
**Bot actions → Edit Profile**. Do not copy a public share link until the operator
signs an approval card and types `GATE_LIFT EXECUTE_PUBLISH`.

## Official listing path (human)

1. Public GitHub commit, SHA pinned.
2. Fork [xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace).
3. Add remote catalog entry. Pin full 40-char lowercase SHA.
4. `python3 scripts/generate-plugin-index.py && python3 scripts/validate-catalog.py`
5. Open PR. Wait for CI + code-owner review.

There is **no** documented self-serve “register public app” API for Grok Bot.
Public Bot copies use a **share link** from the Grok Bot app
([Share a Bot](https://docs.x.ai/grok-bot/bots#share-a-bot)). That link is public.
Strip secrets first. Human copies the link. This plugin does not.

## Network / credentials

This plugin calls no network endpoints of its own. It does not ship MCP servers,
hooks, or shell. It does not read `~/.ssh`, `.env`, or tokens.

## Disclaimer

Financial Engineering Notice. This material is education and operating procedure
for studio-scale liability defeasance. It is not an offer to sell, and not a
solicitation to buy, any note, token, share, or investment contract. Access is
sold as tuition. SOP files and the Custom Connector are delivery methods for
that education corpus. API tokens (cca_) are login credentials, not securities.
PiggyWiggy the Hedgefund Companion by CodyBearTV is the named education agent.
It is a character title. It is not a hedge fund, not an investment adviser, and not a solicitation.
Book A instruments, if ever issued, would be private placements to specified
sophisticated parties under applicable exemptions and counsel direction.
Ley 10961 VASP registration is AML supervision, not a license to intermediate
or to offer securities. ERC-3643 samples are educational and unaudited.
No results are promised.
