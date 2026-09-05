# /imagine

Phase 3: async poller **stub** only. No `api.x.ai`. No MP4 downloads. No CapCut.

**Official vs community:** Official Imagine API (`POST /v1/videos/generations`, `/extensions`, poll `GET /v1/videos/{request_id}`). SDK later: `client.video.generate` / `client.video.extend`. **This folder does not call them.** No official Imagine ↔ CapCut plugin exists. Do not invent one.

**Phase 0 limits** (from `/research/RESEARCH.md`, docs updated 2026-07-30):

- Async jobs: `request_id` then poll. Do not block a TUI on a multi-minute render.
- T2V/I2V clips: **1–15 seconds**. 1080p on `grok-imagine-video-1.5` T2V/I2V only.
- Extend: last-frame continuity; input **2–15s** MP4; extend **2–10s** (default 6); output **capped at 720p**.
- Watermark cannot be removed. Model slug stays in config (`grok-imagine-video-1.5`). Not `grok-4.7`.

## Files

| Path | Role |
|---|---|
| `DESIGN.md` | generate → poll → extend-from-last-frame loop |
| `poller.py` | Stub over a fake job list. No HTTP. No `XAI_API_KEY`. |
| `fixtures/fake_jobs.json` | Local shot list. Fake URLs, not downloads. |

## Run the stub

```bash
python3 imagine/poller.py
```
