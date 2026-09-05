# CapCut draft-builder design

**Phase:** 4 (stub over fake local shots).  
**Skills:** `grok-stack-connectors`, `redhat-security-gate`.  
**Sources:** `/research/RESEARCH.md` — no official CapCut editing API.

Human finishes export in CapCut Pro later. This phase does not open the app.

---

## Official vs community

| Piece | Status |
|---|---|
| CapCut / JianYing NLE | Product only — **no public editing API** |
| Imagine → MP4 | Official xAI (already stubbed in `/imagine`; this folder does not call it) |
| capcut-cli | **Unofficial** community CLI — [renezander030/capcut-cli](https://github.com/renezander030/capcut-cli) |
| CapCutAPI / capcut-mcp | **Unofficial** community MCP/HTTP (`create_draft`, `add_video`, `add_text`, `save_draft`) |
| This stub | Pack-local. Prints intended calls. Writes fake `out/draft.json`. No subprocess, no MCP |

Do not invent an official Imagine ↔ CapCut plugin.

---

## Input

A list of **local MP4 paths + titles** (from Imagine downloads later). This phase uses `fixtures/fake_shots.json` placeholders. Files do not need to exist.

---

## Intended unofficial tool sequence

Allowlisted names only (default deny anything else):

| Step | Unofficial tool | Args (structured, not shell-concatenated) |
|---|---|---|
| 1 | `create_draft` | `width`, `height` (e.g. 1920×1080). capcut-cli analog: `capcut init` / `quickstart` |
| 2 | `add_video` | `draft_id`, `video_url` (local path), `start`, `end` — one call per shot, in order |
| 3 | `add_text` | `draft_id`, `text` (title), `start`, `end` |
| 4 | `save_draft` | `draft_id` — writes a draft folder the operator copies into CapCut later |

capcut-cli mapping (still **unofficial**, not executed this phase):

```
capcut init <project> --ratio 16:9
capcut add-video <project> --file <local.mp4>
capcut add-text <project> --text <title>
capcut …   # save is the write-back; no daemon
```

CapCutAPI MCP mapping (still **unofficial**, not connected this phase):

```
create_draft → add_video → add_text → save_draft
```

Operator then opens the draft in **CapCut Pro**. Human export. No auto-export.

---

## Security gate

- Do not `npx -y` unpinned CapCut servers.
- Parameterized tool args only. Never `os.system(f"capcut {user_text}")`.
- Treat MCP tool results as untrusted (strip instruction-like tags before they re-enter the model).
- Token-gate paid CapCut write later (`capcut:draft` on the monthly entitlement). Stub does not check Stripe.
- No Discord / GitHub invites. No GarageBand.

---

## Out of scope (explicit)

- Installing CapCut
- Live MCP / `npx` install
- Opening CapCut Pro
- Real CapCut draft schema
- GarageBand
- Git commit or push
