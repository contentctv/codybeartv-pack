# Official plugin marketplace listing — DRAFT, UNSUBMITTED

Status: UNPOSTED. PUBLISH=off. FIVERR_SUBMIT=off. X_POST=off.
Official catalog: [github.com/xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace)
Process: [CONTRIBUTING.md](https://github.com/xai-org/plugin-marketplace/blob/main/CONTRIBUTING.md)
Docs: [Skills, Plugins & Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)

This is **not** a Grok Bot “app store” API. Grok Bot Settings → Plugins → Marketplace
is for **installing** connectors. Third-party **listing** is a PR to the Grok Build
catalog after a public SHA-pinned source repo.

Do not open the PR until the operator types `GATE_LIFT EXECUTE_PUBLISH GROK_BOT_MARKETPLACE`
and is the one who submits.

---

## Catalog entry (paste into a fork of xai-org/plugin-marketplace)

`.grok-plugin/marketplace.json` plugins[] append. SHA is a placeholder until a
public commit exists. CI rejects branch/tag/abbrev SHAs.

```json
{
  "name": "piggywiggy",
  "description": "PiggyWiggy the Hedgefund Companion by CodyBearTV. Cipher Coast Academy education agent for studio-scale liability defeasance. Character title only — not a hedge fund, not an investment adviser. Tuition SKU; SOP files are byproducts.",
  "category": "productivity",
  "source": {
    "source": "url",
    "url": "https://github.com/contentctv/codybeartv-pack.git",
    "sha": "REPLACE_WITH_40_CHAR_LOWERCASE_COMMIT_SHA",
    "path": ".grok/plugins/piggywiggy"
  },
  "homepage": "https://github.com/contentctv/codybeartv-pack",
  "keywords": ["piggywiggy", "codybeartv", "cipher coast academy"],
  "domains": ["codybeartv.pw"]
}
```

`domains` lists a brand host. DNS_CUTOVER=off — do not claim the academy origin is live.

## After the source commit is public

```bash
git ls-remote https://github.com/contentctv/codybeartv-pack.git HEAD
# paste the 40-char sha into the entry
python3 scripts/generate-plugin-index.py
python3 scripts/validate-catalog.py
```

Then the **human** opens the PR on xai-org/plugin-marketplace.

## QC before submit

- [ ] Source repo public and reachable (GitHub MCP currently 404 on this token — confirm visibility)
- [ ] Plugin path `.grok/plugins/piggywiggy` contains `.grok-plugin/plugin.json`, README, LICENSE, skill
- [ ] No secrets, no Book A terms, no receive addresses, no APY calculator
- [ ] Keywords brand-scoped (not generic “hedge”, “invest”, “trading”)
- [ ] Disclaimer in README
- [ ] No MCP / hooks / shell in this plugin (least privilege)

---

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
