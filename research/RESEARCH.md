# CodyBearTV Phase 0 research

**Status:** Phase 0 complete. No scaffold. No application code. No git commit. No push. No Imagine, Stripe, Discord, CapCut, or Polymarket live calls were made.

**Fetched:** 2026-09-05  
**Operator:** James Jenkins / CodyBearTV  
**Skills loaded this session:** `codybeartv-os` (prior turn), `redhat-security-gate`, `official-first-research`  
**Default model:** `grok-4.6`. Do not assume `grok-4.7` exists.

Source ladder used: official docs first, official SDKs second, community file-writing repos third, blogs/X tagged **UNVERIFIED**.

Note: `https://docs.x.ai/developers` (bare path) returns 404. Imagine and API docs live under `https://docs.x.ai/developers/model-capabilities/...`, `https://docs.x.ai/developers/models`, and `https://docs.x.ai/llms.txt`.

---

## 1. Confirmed official capabilities

### 1.1 Grok Build (terminal agent)

**Claim:** Grok Build is SpaceXAI's terminal coding agent. Interactive TUI, headless (`grok -p`), or ACP (`grok agent stdio`).

| Item | Value |
|---|---|
| Official source | [docs.x.ai/build/overview](https://docs.x.ai/build/overview), [github.com/xai-org/grok-build](https://github.com/xai-org/grok-build) README |
| Date | Fetched 2026-09-05 (docs live; grok-build README current on `main`) |
| Install | `curl -fsSL https://x.ai/cli/install.sh \| bash` (macOS/Linux); PowerShell `irm https://x.ai/cli/install.ps1 \| iex` |
| Auth | Browser OIDC on first launch, or `XAI_API_KEY` |
| Headless | `grok -p "..."`, `--output-format json\|streaming-json\|plain` |
| Skills | `.grok/skills/`, `~/.grok/skills/`, plugin `skills/` |
| MCP | `grok mcp add`, namespaced as `<server>__<tool>`, `${VAR}` expansion, OAuth tokens in `~/.grok/mcp_credentials.json` |
| Plugins | `.grok/plugins/`, `~/.grok/plugins/`, marketplace under `~/.grok/plugins/marketplaces/` |
| Project rules | `AGENTS.md` / `Agents.md` / `AGENT.md` walked cwd → git root |
| Brain model | Same `grok-4.6` as API (`POST https://api.x.ai/v1/responses`) |
| Constraint | External contributions to grok-build are **not accepted** (CONTRIBUTING.md) |
| Risk | Treat third-party plugins as untrusted code with host filesystem access |

### 1.2 Skills, plugins, marketplaces

**Claim:** Skills are `SKILL.md` folders. Plugins bundle skills, agents, hooks, MCP, LSP. Official catalog is `xai-org/plugin-marketplace`.

| Item | Value |
|---|---|
| Official source | [docs.x.ai/build/features/skills-plugins-marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces), [github.com/xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace) |
| Date | Fetched 2026-09-05 |
| Catalog source of truth | `.grok-plugin/marketplace.json` |
| Remote plugin pin | Full 40-char lowercase commit SHA required; Grok re-verifies `git rev-parse HEAD == sha` after clone |
| Third-party warning | xAI does **not** endorse, verify, or warrant third-party plugins; they may execute code and access data |
| Limit | `allowed-tools` in SKILL.md does **not** grant or restrict tools |
| Wrapper | None needed for first-party Grok Build surfaces |
| Risk | Marketplace install is a supply-chain event. Pin SHAs. Rehash manifests (`/security/hashes.json` in this pack). |

### 1.3 MCP in Grok Build

**Claim:** MCP servers are first-class. Local stdio or remote HTTP. OAuth handled automatically. Compatible with Claude/Cursor MCP files at lower priority than `config.toml`.

| Item | Value |
|---|---|
| Official source | [docs.x.ai/build/features/mcp-servers](https://docs.x.ai/build/features/mcp-servers) |
| Date | Fetched 2026-09-05 |
| Add local | `grok mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path` |
| Add remote | `grok mcp add --transport http linear https://mcp.linear.app/mcp` |
| Project scope | `--scope project` writes `.grok/config.toml` |
| Doctor | `grok mcp doctor`; stderr at `~/.grok/logs/mcp/<server>.stderr.log` |
| Constraint | Default-deny allowlists for tool names (pack security gate). Do not concatenate LLM text into shell. |
| Risk | Token leakage via `mcp_credentials.json`, tool-result injection, schema drift on community servers |

### 1.4 Grok 4.6 API (brain)

**Claim:** `grok-4.6` is the current flagship for code, chat, and agentic work. There is **no** `grok-4.7` model ID on official docs.

| Item | Value |
|---|---|
| Official source | [docs.x.ai/developers/models/grok-4.6](https://docs.x.ai/developers/models/grok-4.6), [docs.x.ai/developers/models](https://docs.x.ai/developers/models), [docs.x.ai/developers/quickstart](https://docs.x.ai/developers/quickstart) |
| Date | Fetched 2026-09-05; models page last-updated note in search index 2026-08-21 |
| Model name | `grok-4.6` |
| Context | 500,000 tokens |
| Modalities | text, image → text |
| Function calling | Yes |
| Structured outputs | Yes |
| Reasoning | Yes (`low` / `medium` / `high` / `xhigh`) |
| Batch API | **Not supported** on grok-4.6 |
| Knowledge cutoff | 2026-02-01 |
| Pricing (< 200k prompt) | $2.00 / 1M in, $0.50 cached, $6.00 out |
| Pricing (≥ 200k prompt) | $4.00 / 1M in, $1.00 cached, $12.00 out |
| Rate limits | 150 rps, 50,000,000 tokens/min |
| Regions | us-east-1, us-west-2 |
| Listed models (no 4.7) | grok-4.6, grok-4.5, grok-4.3, grok-4.20-0309-*, grok-build-0.1, grok-4.20-multi-agent-0309 |
| Constraint | Keep model IDs in config. Do not hard-code a future slug. |
| Risk | Inventing `grok-4.7` endpoints will fail closed and burn tokens |

### 1.5 Imagine video 1.5 + last-frame extend

**Claim:** Video generation is **async**. REST returns `request_id`; poll `GET /v1/videos/{request_id}` until `done` / `failed` / `expired`. SDK `generate()` / `extend()` poll for you. Do not block a TUI on a multi-minute render.

| Item | Value |
|---|---|
| Official source | [Video generation](https://docs.x.ai/developers/model-capabilities/video/generation), [Video extension](https://docs.x.ai/developers/model-capabilities/video/extension) (last updated **2026-07-30**), [REST videos](https://docs.x.ai/developers/rest-api-reference/inference/videos), [grok-imagine-video-1.5](https://docs.x.ai/developers/models/grok-imagine-video-1.5) |
| Date | Fetched 2026-09-05 |
| Models | `grok-imagine-video-1.5` (T2V/I2V/R2V, native 1080p on T2V/I2V); `grok-imagine-video` (edits/extend examples) |
| Endpoints | `POST /v1/videos/generations`, `/edits`, `/extensions`; poll `GET /v1/videos/{request_id}` |
| SDK | `client.video.generate`, `client.video.extend`, `start`/`extend_start`/`get` |
| T2V/I2V duration | **1–15 seconds** (REST default 8) |
| T2V/I2V resolution | `480p` (default), `720p`, `1080p` on 1.5 for T2V and I2V |
| R2V resolution | Capped at **720p**; max 7 reference images; max 3 preset voices |
| Extend input | `.mp4` with H.264 / H.265 / AV1 etc.; duration **2–15 seconds** |
| Extend output | Last-frame continuity; extend **2–10 seconds** (default 6); `aspect_ratio`/`resolution` **not supported**; output matches input, **capped at 720p** |
| Extend duration semantics | `duration` is the **new segment only**. 10s in + 5s extend = 15s total |
| Edit input cap | **8.7 seconds**; output inherits duration/AR; resolution capped at 720p |
| Auth | `Authorization: Bearer $XAI_API_KEY` |
| Pricing | 1.5: **$0.080 / sec**; `grok-imagine-video`: **$0.050 / sec** |
| 1.5 rate limit | 10 rps |
| Batch | Supported for video; **no batch discount** (standard Imagine rates) |
| SDK poll default | timeout 10 minutes; interval 100 ms |
| Output URL | Temporary xAI-hosted URL; persist via Files API `storage_options` if needed |
| Watermark | Grok watermark is required; removal prohibited ([Grok FAQ](https://docs.x.ai/grok/faq)) |
| Constraint | One mode per request. `image` + `reference_images` = 400. |
| Risk | Cost scales with seconds × $0.08. 1080p T2V then 720p extend downscales the chain. Ephemeral URLs expire. |

### 1.6 Grok Bot (workers)

**Claim:** Grok Bots are named persistent agents on a **shared** user-scoped cloud computer. They do not auto-share context with Grok Build.

| Item | Value |
|---|---|
| Official source | [docs.x.ai/grok-bot/overview](https://docs.x.ai/grok-bot/overview), [security FAQ](https://docs.x.ai/grok-bot/security-faq) |
| Date | Fetched 2026-09-05 (security FAQ published 2026-09-03) |
| Isolation | Firecracker microVM per user; Bots on one user share that computer |
| Constraint | A login or file on the computer is available to **every** Bot for that user |
| Glue | Share the same `SKILL.md` packs; do not paste `config.toml` MCP into Bot chat as if it were Build |
| Risk | Over-broad connector grants. Human approval for post/spend. |

### 1.7 Official plugin marketplace + grok-build repo facts

| Claim | Official source + date | Limit / constraint |
|---|---|---|
| Official catalog of Grok Build plugins | [xai-org/plugin-marketplace](https://github.com/xai-org/plugin-marketplace) README, fetched 2026-09-05 | First-party in `plugins/`; third-party in `external_plugins/` or remote SHA pin |
| Grok Build source is Apache-2.0, synced from SpaceXAI monorepo | [xai-org/grok-build](https://github.com/xai-org/grok-build) README, fetched 2026-09-05 | Binary artifact `xai-grok-pager` ships as `grok`; `SOURCE_REV` records monorepo SHA |
| Docs live at docs.x.ai/build/overview | Same | User guide also in-tree under pager crate |

---

## 2. Hard limits (does not exist / unofficial)

### 2.1 CapCut — no official public editing API

| Field | Finding |
|---|---|
| Capability check | **Does not exist** as a public CapCut NLE / draft API |
| Official source | CapCut.com product/help pages describe the editor UI, templates, and AI features. No public REST/MCP for creating or editing drafts. Seedance marketing on capcut.com is **generation** (BytePlus ModelArk “API access coming soon”), not CapCut timeline control. |
| Date | Fetched 2026-09-05 |
| Wrapper path | Community draft-file writers (section 3) |
| Risk | Schema drift on `draft_content.json`. CapCut updates can break drafts. Not affiliated with ByteDance. Human finishes export. |

### 2.2 GarageBand — no official public editing API

| Field | Finding |
|---|---|
| Capability check | **Does not exist** as a public GarageBand project API |
| Official source | Apple Developer docs expose Audio Units / Core Audio for **hosts and plug-ins**, not a GarageBand document API. No GarageBand REST/MCP in Apple docs. |
| Date | Fetched 2026-09-05 |
| Wrapper path | [extao15/garageband-llm-bridge](https://github.com/extao15/garageband-llm-bridge) — AppleScript `renderPreview` + Accessibility menus. Community. Brittle. |
| Risk | UI-state dependent. macOS only. Accessibility permissions. Do not treat as an API. |

### 2.3 SuperCool — no documented public MCP

| Field | Finding |
|---|---|
| Capability check | **Product exists; public MCP does not** (no docs found) |
| Official/product pages | [go.supercool.com](https://go.supercool.com/), viral.supercool.com, coder.supercool.com, book.supercool.com, App Store “SuperCool - Do Anything”. Skill also cites supercool.com / aiagency.supercool.com. |
| Date | Fetched 2026-09-05 |
| Search result | No SuperCool MCP endpoint, OpenAPI, or connector URL in official docs |
| Wrapper path | If needed later: **community-maintained wrapper**, marked unofficial |
| Risk | Do not invent an official SuperCool MCP URL. Marketing pages are not APIs. |

### 2.4 Grok 4.7 — do not assume

| Field | Finding |
|---|---|
| Capability check | **Does not exist** on official model list |
| Official source | [docs.x.ai/developers/models](https://docs.x.ai/developers/models): “For everything else, including code, use Grok 4.6. It is the most intelligent and fastest model we’ve built.” |
| Date | Fetched 2026-09-05 |
| Constraint | Keep slugs in config. Never hard-code `grok-4.7`. |

### 2.5 Imagine async + last-frame extend caps (hard)

See §1.5. Recap for implementers:

- Async jobs: `request_id` then poll. SDK timeout default **10 minutes**.
- T2V/I2V: 1–15s; 1080p only on `grok-imagine-video-1.5` T2V/I2V.
- Extend: input 2–15s MP4; extend 2–10s (default 6); **output ≤ 720p**.
- Edit: input ≤ 8.7s; output 720p cap.
- R2V: 720p cap, ≤7 images, ≤3 voices.
- Plan resolution: prefer 1080p on clip 1, then accept 720p on extend chain — or generate each shot independently at 1080p and cut in CapCut (community draft).

---

## 3. Community wrapper options

Tag: **community / unofficial**. Not ByteDance, not Apple, not xAI.

### 3.1 CapCut drafts

| Wrapper | What it is | Tools / surface | Brittleness |
|---|---|---|---|
| [renezander030/capcut-cli](https://github.com/renezander030/capcut-cli) | Independent CLI + library. JSON in/out on local draft store. **Not affiliated with ByteDance.** MIT. npm `capcut-cli`. | `init`, `quickstart`, `add-video`, `add-text`, `caption`, `compile`, `serve` JSONL. Optional experimental Wasm MCP **read-only** inspect/diff/lint. | CapCut version schema drift. Pin `capcut-cli@latest` (≥0.18.0; older versions had injection / credential issues). Human opens draft and exports. |
| [ashreo/CapCutAPI](https://github.com/ashreo/CapCutAPI) / forks (`sun-guannan/CapCutAPI`, `fancyboi999/capcut-mcp`) | Community Python MCP/HTTP: `create_draft`, `add_video`, `add_text`, `add_audio`, `save_draft` | stdio MCP or HTTP `:9000/mcp` | Draft JSON reverse-engineering. Copy `dfd_*` folder into CapCut drafts dir. |
| [JmsLdrn/capcut-mcp](https://github.com/JmsLdrn/capcut-mcp) | Clone-from-template MCP. Explicitly: CapCut draft format is proprietary/undocumented. | `capcut_list_drafts`, `capcut_add_video`, validate, atomic save | CapCut update can shift schema. |

**Recommended pack path (when Phase 1+ is approved):** Imagine poller downloads MP4s → `capcut-cli` (or CapCut MCP) `create_draft` / `add_video` / `add_text` / `save_draft` → operator opens CapCut Pro. **Do not hand-write CapCut JSON. Do not auto-export.**

### 3.2 Emergent MCP — `https://mcp.emergent.sh/`

| Field | Finding |
|---|---|
| Capability check | **Exists** as a remote MCP connector (vendor product, not xAI) |
| Official Emergent pages | [getmcp.emergent.sh](https://getmcp.emergent.sh/), [emergent.sh/blog/emergent-mcp-connector](https://emergent.sh/blog/emergent-mcp-connector) (2026-06-22), [help.emergent.sh](https://help.emergent.sh/introduction/faq) |
| Date | Fetched 2026-09-05 |
| Connector URL | `https://mcp.emergent.sh/` — **trailing slash is required** |
| Auth | OAuth. Unauthenticated GET returns `{"error":"invalid_token","error_description":"missing bearer token"}` (confirms the endpoint, not a public anonymous API) |
| Job | Full-stack app build + live preview from chat (auth, DB, backend) |
| Grok Build glue | `grok mcp add --transport http emergent https://mcp.emergent.sh/` then OAuth on first use |
| Limit | Connector handles build/preview; deploy/publish often moves to Emergent's own UI |
| Risk | Third-party remote MCP. Treat tool results as untrusted. Do not store Emergent tokens in git. |

### 3.3 GarageBand

[extao15/garageband-llm-bridge](https://github.com/extao15/garageband-llm-bridge) — local CLI + MCP. Honest limit from the repo: GarageBand has no broad public automation API; `renderPreview` is the useful AppleScript command; rest is menus/keyboard. **Community. Brittle. macOS only.**

---

## 4. X Original Content Rewards / X Money (after 2026-09-07)

**Today is 2026-09-05.** Creator Revenue Sharing retires **2026-09-07**.

### Official program switch

| Event | Date | Source |
|---|---|---|
| New enrollments closed for Creator Revenue Sharing | 2026-08-07 | [help.x.com Creator Revenue Sharing](https://help.x.com/en/using-x/creator-revenue-sharing) |
| Revenue Sharing earnings continue through | 2026-09-07 | Same |
| Final CRS payouts | Aug 14, Aug 28, and ~Sep 11 for earnings through Sep 7 | Same |
| Existing CRS members may apply to Original Content Rewards | starting **2026-09-08** | [Original Content Rewards](https://help.x.com/en/using-x/original-content-rewards) (page published 2026-09-02) |
| Terms | [legal.x.com/original-content-rewards-terms](https://legal.x.com/original-content-rewards-terms) | Official |

### Original Content Rewards — eligibility (official)

Must meet **all** at application time:

- Country on the OCR availability list (includes United States)
- Age 18+
- Account in good standing
- Personal or Business account (political/government orgs ineligible)
- Active **Premium, Premium+, or Premium Business**
- **≥ 500,000** Home Timeline impressions from verified users in last 90 days (replies excluded)
- **≥ 500** verified followers
- Actively post original content as defined

Admission is not guaranteed. Review within 3 business days. One appeal; then 90-day wait.

### Qualified impressions (official)

Unique impressions from Premium users (Basic, Premium, Premium+, Premium Business) on Home Timeline where **≥ 50% of the post is visible**. Excludes same-account duplicates, paid/promoted/artificial, and fraudulent impressions.

### Originality rules (official — pack-critical)

Original = personally created; commentary that adds genuine perspective **counts**.

**Not original:**

- Copied text/images/videos with no contribution (including download-from-X-and-reupload)
- Minimally modified (filter, speed change, text overlay)
- Aggregated compilations without substantial framing
- Cross-platform reposts by someone other than the original creator

**Also ineligible for payouts:** sexually explicit/harmful; exclusively monetization coaching; **created or posted using automated means**; disinformation; Community Notes; ToS/copyright violations.

**Armed-conflict AI video:** effective 2026-03-03, AI-generated videos of an armed conflict **without AI disclosure** → 90-day OCR/CRS suspension; subsequent → permanent payment ban.

**Grok Imagine watermark:** official xAI FAQ — generated images/videos include a Grok watermark; **no setting to remove it**; obscuring provenance is prohibited under xAI AUP. That watermark is a disclosure signal, not a license to auto-post.

### Payout rails (official help vs official account)

| Audience | Official help.x.com OCR (fetched 2026-09-05) | Official @XCreators (2026-09-02) |
|---|---|---|
| **US users** | Payouts through **X Money**. One X Money account per person (SSN). One X account per X Money account. Start at [x.com/i/money](https://x.com/i/money) | “Starting today, U.S. payouts for Original Content Rewards and Subscriptions will be paid through @XMoney.” Access when sent. |
| **Non-US users** | Connect **Stripe** payout account + Stripe identity verification | TechCrunch (2026-09-02) reports non-US remain on Stripe — **secondary; matches help page** |
| Cadence / minimum | Help page still: **every two weeks**, **minimum $30** | @XCreators: access the moment sent. Blogs claiming the $30 floor is gone are **UNVERIFIED** against the help page. Prefer help.x.com until it is updated. |
| Tax | @XCreators: 1099-NEC for US creator payouts; W-9 for LLCs later | Official X account, not a help article |

**Pack implication:** US CodyBearTV payouts after 2026-09-07 go through **X Money**, not a new Stripe CRS enrollment. Stripe remains the **product** rail (pack sales), not the X creator rail for US. Identity verification is required. Never store SSN, seed phrases, or Stripe secret keys in this repo.

**Do not auto-post to X.** OCR disqualifies automated posting. Publisher bot drafts; human posts.

---

## 5. Risk list

| Risk | Why it matters | Mitigation (pack gate) |
|---|---|---|
| **Schema drift** | CapCut/JianYing draft JSON is undocumented. MCP tool schemas change. Imagine REST fields evolve. | Pin wrapper versions. Version-aware lint (`capcut doctor`). Fail closed on unknown fields. Re-fetch official docs before Phase 2 connectors. |
| **Token leakage** | MCP OAuth in `~/.grok/mcp_credentials.json`. `XAI_API_KEY` in env. Discord/Stripe/GitHub tokens. OWASP **MCP01:2025 Token Mismanagement**. Contextual secret leakage into model memory/logs. | Env-only secrets. Never echo keys. Short-lived tokens. Rotate on calendar / Stripe cancel. Local models never see prod secrets. Fine-grained GitHub PAT. |
| **KYC / identity** | X Money is SSN-bound, one account per person. Non-US OCR uses Stripe identity verification. Polymarket live trading and wallet onramps imply KYC/KYB. MoonPay etc. | Human completes KYC in vendor UI. Pack never stores ID docs, SSN, seed phrases. Wallet connect is public address only. |
| **Unofficial wrappers** | CapCut, GarageBand, SuperCool MCP. Third-party marketplace plugins execute host code. OWASP **MCP03 tool poisoning**, **MCP04 supply chain**, rug pulls. | Label community. SHA-pin plugins. Rehash `/security/hashes.json`. Allowlist MCP tool names. Treat tool **results** as untrusted (strip instruction-like tags). |
| **Originality rules** | OCR excludes copies, minimal edits, aggregations, **automated posts**. Imagine outputs are watermarked AI. Armed-conflict AI video needs disclosure. | Human-in-the-loop publish. Add original commentary, research, and developer teaching — not clip dumps. Never strip watermarks. Never auto-post. |
| **Imagine cost / rate** | $0.080/sec on 1.5; 10 rps; 10-minute default poll; ephemeral URLs | Async poller, not TUI-blocking. Budget per shot. Persist via Files API. Human approval before batch spend. |
| **Resolution chain** | 1080p T2V then 720p extend | Storyboard: independent 1080p shots + CapCut cut, **or** accept 720p continuity chain. |
| **Live spend / trade** | Stripe live, Discord send, git push main, live CLOB, DNS | Hard gate. Human approval. Polymarket stays **PAPER** until operator types `GATE_LIFT LIVE_TRADING`. |
| **Prompt injection via MCP** | Tool descriptions and return values enter the model as trusted text | Parameterized APIs only. Default-deny tools. Rate-limit retry storms on forbidden tools. Notify operator. Do not escalate privileges. |
| **Grok Bot shared VM** | All Bots share one computer and logins | Least privilege connectors. Separate Cursor/user if workload needs isolation. |
| **Webhook spoofing** | Stripe/GitHub/Discord webhooks | Verify signatures before role/invite. Allowlist IPs/guild/repo. |

OWASP references (official-adjacent, not xAI): [MCP Top 10](https://owasp.org/www-project-mcp-top-10/), [MCP01 Token Mismanagement](https://owasp.org/www-project-mcp-top-10/2025/MCP01-2025-Token-Mismanagement-and-Secret-Exposure), [MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning), [MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html).

---

## 6. Recommended libraries and official URLs (with dates)

Fetched **2026-09-05** unless a page last-updated date is listed.

### Use these (official)

| Library / product | Install / ID | Official URL | Role |
|---|---|---|---|
| Grok Build CLI | `curl -fsSL https://x.ai/cli/install.sh \| bash` | https://docs.x.ai/build/overview · https://x.ai/cli | Scaffold later (Phase 1+), headless `grok -p` |
| grok-build source | n/a (do not fork for contrib) | https://github.com/xai-org/grok-build | Reference TUI/runtime |
| Plugin marketplace | SHA-pinned catalog | https://github.com/xai-org/plugin-marketplace | First-party plugins only unless reviewed |
| xAI Python SDK | `pip install xai-sdk` | https://github.com/xai-org/xai-sdk-python · https://docs.x.ai/developers/quickstart | Chat, Imagine image/video, extend, tools |
| OpenAI-compatible | `pip install openai` / `npm install openai` with `base_url=https://api.x.ai/v1` | https://docs.x.ai/developers/quickstart | Responses API, `grok-4.6` |
| Vercel AI SDK xAI | `npm install ai @ai-sdk/xai` | same | JS video `experimental_generateVideo` |
| Model IDs | `grok-4.6`, `grok-imagine-video-1.5`, `grok-imagine-image-2.0` | https://docs.x.ai/developers/models | Config, never 4.7 |
| Imagine video | `client.video.generate` / `extend` | https://docs.x.ai/developers/model-capabilities/video/generation · [extension](https://docs.x.ai/developers/model-capabilities/video/extension) (updated 2026-07-30) | Async jobs |
| Grok Bot | product, not a pip lib | https://docs.x.ai/grok-bot/overview | Education/moderation/builder crew |
| Stripe Checkout | Checkout Sessions API | https://docs.stripe.com/payments/checkout | Pack storefront (test mode until approved) |
| GitHub REST + Octokit | `@octokit/rest` | https://docs.github.com/en/rest | Pages, releases, fine-grained PAT |
| Polymarket docs | `@polymarket/client` / `polymarket` | https://docs.polymarket.com | **PAPER only** until `GATE_LIFT LIVE_TRADING` |
| X OCR / X Money | product | https://help.x.com/en/using-x/original-content-rewards · https://x.com/i/money | US payout rail after 2026-09-07 |
| Emergent MCP | remote HTTP + OAuth | https://mcp.emergent.sh/ (trailing slash) · https://getmcp.emergent.sh/ | App-build connector |

### Use these only as community wrappers (label them)

| Library | URL | Use |
|---|---|---|
| capcut-cli | https://github.com/renezander030/capcut-cli | Preferred draft writer (CLI, no daemon) |
| CapCutAPI MCP | https://github.com/ashreo/CapCutAPI | MCP `create_draft` / `add_video` / `save_draft` |
| capcut-mcp (clone-template) | https://github.com/JmsLdrn/capcut-mcp | Safer JSON clone-from-template |
| garageband-llm-bridge | https://github.com/extao15/garageband-llm-bridge | macOS AppleScript/Accessibility only |

### Do not invent

- Official Grok Imagine ↔ CapCut plugin
- Official SuperCool MCP URL
- `grok-4.7` model ID
- CapCut or GarageBand public editing APIs
- Auto-post to X, auto-spend Stripe live, live Polymarket CLOB

---

## Capability check summary

| Question | Result |
|---|---|
| Grok Build TUI + headless + MCP + skills? | **Exists** (official) |
| grok-4.6 API + Imagine video 1.5 + last-frame extend? | **Exists** (official, async, capped) |
| grok-4.7? | **Does not exist** |
| Official CapCut editing API? | **Does not exist** |
| Official GarageBand editing API? | **Does not exist** |
| SuperCool public MCP? | **Not documented** |
| CapCut draft wrappers? | **Unofficial** (capcut-cli / CapCutAPI) |
| Emergent MCP at mcp.emergent.sh? | **Exists** (OAuth remote MCP) |
| US X payouts after 2026-09-07? | **X Money** + Original Content Rewards |

---

## Phase 0 stop

This file is the only deliverable. No monorepo scaffold. No application code. No commit. No push.

**Waiting for operator approval before Phase 1 scaffold.**
