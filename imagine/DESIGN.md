# Imagine poller design

**Phase:** 3 (stub over fake jobs).  
**Skills:** `grok-stack-connectors`, `official-first-research`.  
**Sources:** `/research/RESEARCH.md`; [video generation](https://docs.x.ai/developers/model-capabilities/video/generation); [video extension](https://docs.x.ai/developers/model-capabilities/video/extension) (updated 2026-07-30).

Human approval is still required before any Imagine spend.

---

## Official vs community

| Piece | Status |
|---|---|
| Imagine generate / extend / poll | Official xAI |
| This stub (`poller.py` + fixtures) | Pack-local. Never hits `api.x.ai` |
| CapCut draft after download | Community — **out of this phase** |

Do not invent an official Imagine ↔ CapCut plugin. Do not invent `grok-4.7`.

---

## Loop

Grok 4.6 writes shot prompts (brain). Imagine does not share Build context — this poller is the glue.

```
for each shot in storyboard:
  if shot is clip 1:
    GENERATE  (T2V or I2V, prefer 1080p on grok-imagine-video-1.5)
    receive request_id
    POLL until done | failed | expired
  else:
    EXTEND from last completed clip (official last-frame endpoint)
    duration = length of NEW segment only (default 6, range 2–10)
    POLL until done | failed | expired
persist metadata (url is ephemeral on the real API)
# later phase: download MP4s → CapCut draft. Not here.
```

REST (when live, not now):

1. `POST /v1/videos/generations` or `POST /v1/videos/extensions` → `{ "request_id" }`
2. `GET /v1/videos/{request_id}` until `status` is `done` / `failed` / `expired`

SDK `generate()` / `extend()` poll internally (default timeout 10 minutes). This stub **does not import `xai_sdk`** and **does not call** those methods.

Do not block the Grok Build TUI on a render. Queue + poll.

---

## Resolution plan

| Path | Clip 1 | Clips 2..N | Result |
|---|---|---|---|
| Continuity chain | 1080p T2V/I2V | last-frame extend | Extend output **≤ 720p** (downscale) |
| Independent shots | 1080p each | generate, not extend | 1080p, cut later in CapCut (community) |

Stub default: continuity chain. Operator must accept 720p after shot 1.

---

## Validation (local, no API)

Reject before any future network call:

- Generate duration not in 1–15
- Extend duration not in 2–10
- Extend source duration not in 2–15
- `1080p` on extend or R2V
- Mixing image + reference_images
- Missing `XAI_API_KEY` is a **live** concern only — this stub never reads that env

---

## Out of scope (explicit)

- Setting `XAI_API_KEY` in files
- `client.video.generate` / `client.video.extend`
- Downloading MP4s
- CapCut
- Git commit or push
