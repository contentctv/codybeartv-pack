# GitHub merge runbook — HOLD

Status: BLOCKED. PUBLISH=off. No push executed this turn.
Remote (local git): `git@github.com:contentctv/codybeartv-pack.git`
GitHub MCP `GET /repos/contentctv/codybeartv-pack`: **404** on the connected token.
Do not force-push. Do not dump `node_modules/`. Do not publish Book A.

Operator said “MERGE TO GITHUB.” Desk law: human approval before git push to main,
and this tree is not a clean public slice.

## Why this turn did not push

| Blocker | Fact |
|---|---|
| Dirty tree | Untracked `node_modules/`, `coast-chips/`, `memory/`, TRACKING, HANDOFF, ISA dist still CYCLE 1 only |
| Secrets risk | `.env` ignored; MCP credentials must stay out |
| Marketplace | Public listing requires a **reachable public** SHA. MCP cannot see this repo yet |
| ISA gate | `GATE_LIFT EXECUTE_PUBLISH` not typed |
| Academy | M1–M4 chapters not written; do not ship a half corpus as “the app” |

## Allowlist for a later public commit (operator runs)

Include:

- `.grok/plugins/piggywiggy/`
- `artifacts/isa-academy/dist/publish/DISCLAIMER.md`
- `artifacts/isa-academy/dist/publish/GROK-BOT-PROFILE.md`
- `artifacts/isa-academy/dist/chapters/TEASER.md`
- `bots/README.md`
- `.gitignore`
- existing Phase 0–6 stubs already on `origin/main`

Exclude:

- `node_modules/`
- `coast-chips/node_modules/`
- `memory/`
- `TRACKING.md` / `HANDOFF.md` (desk tutor store)
- `Modelfile.edu-deep`
- `*.bak*`
- any Book A / INT pack
- Stripe live keys, seeds, receive addresses (none should exist)

## Commands the **human** runs after GATE_LIFT

```bash
# 1. Confirm ignore
git status --ignored

# 2. Branch — do not commit straight to main until reviewed
git checkout -b piggywiggy-plugin-public

# 3. Add only the allowlist
git add .gitignore .grok/plugins/piggywiggy bots/README.md \
  artifacts/isa-academy/dist/publish/DISCLAIMER.md \
  artifacts/isa-academy/dist/publish/GROK-BOT-PROFILE.md \
  artifacts/isa-academy/dist/publish/MARKETPLACE-LISTING.md \
  artifacts/isa-academy/dist/publish/GITHUB-MERGE-RUNBOOK.md \
  artifacts/isa-academy/dist/chapters/TEASER.md

# 4. Human reviews diff, then:
git commit -m "Add PiggyWiggy education plugin (unpublished marketplace packet)"

# 5. Push branch (not main) after GATE_LIFT EXECUTE_PUBLISH GITHUB
git push -u origin piggywiggy-plugin-public
```

Merge to `main` is a second human action (GitHub PR merge). This desk does not
call `github__merge_pull_request` until that lift.

## After the commit is on a public default branch

```bash
git ls-remote https://github.com/contentctv/codybeartv-pack.git HEAD
```

Paste the SHA into `MARKETPLACE-LISTING.md`. Human opens the xAI catalog PR.

---

Financial Engineering Notice. This material is education and operating procedure
for studio-scale liability defeasance. It is not an offer to sell, and not a
solicitation to buy, any note, token, share, or investment contract. Access is
sold as tuition. SOP files and the Custom Connector are delivery methods for
that education corpus. API tokens (cca_) are login credentials, not securities.
PiggyWiggy the Hedgefund Companion by CodyBearTV is the named education agent.
It is a character title. It is not a hedge fund, not an investment adviser, and not a solicitation.
No results are promised.
