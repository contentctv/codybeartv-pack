"""Imagine poller stub. Fake jobs only. Never calls api.x.ai or xai_sdk."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "fake_jobs.json"

# Official Imagine limits — /research/RESEARCH.md (docs.x.ai video generation +
# extension, last updated 2026-07-30). This stub enforces them locally.
# - T2V/I2V clips: 1-15 seconds
# - 1080p on grok-imagine-video-1.5 T2V/I2V only
# - Extend: last-frame continuity; input 2-15s MP4; extend 2-10s (default 6)
# - Extend output capped at 720p (aspect_ratio/resolution params not supported)
# - duration on extend is the NEW segment only (10s in + 5s extend = 15s total)
# - Async: request_id then poll pending|done|failed|expired
# - Do not call client.video.generate or client.video.extend here
# - Do not set XAI_API_KEY in files
# - Do not download MP4s; do not touch CapCut

GENERATE_DURATION = range(1, 16)
EXTEND_DURATION = range(2, 11)
EXTEND_INPUT_DURATION = range(2, 16)
EXTEND_OUTPUT_CAP = "720p"
GENERATE_1080P_MODEL = "grok-imagine-video-1.5"


@dataclass
class Clip:
    shot_id: str
    mode: str
    status: str
    duration: int
    resolution: str
    request_id: str | None = None
    url: str | None = None
    reason: str | None = None
    ticks: list[str] = field(default_factory=list)


def load_jobs(path: Path = FIXTURES) -> tuple[str, list[dict]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return str(data.get("model") or GENERATE_1080P_MODEL), list(data.get("jobs") or [])


def validate(job: dict, source: Clip | None, model: str) -> str | None:
    mode = job.get("mode")
    duration = int(job.get("duration") or 0)
    if mode == "generate":
        if duration not in GENERATE_DURATION:
            return "invalid_generate_duration"
        if job.get("resolution") == "1080p" and model != GENERATE_1080P_MODEL:
            return "1080p_requires_imagine_video_1_5"
        return None
    if mode == "extend":
        if duration not in EXTEND_DURATION:
            return "invalid_extend_duration"
        if source is None or source.status != "done":
            return "missing_last_frame_source"
        if source.duration not in EXTEND_INPUT_DURATION:
            return "invalid_extend_input_duration"
        if job.get("resolution") == "1080p":
            return "extend_resolution_not_supported"
        return None
    return "unknown_mode"


def fake_poll(ticks: list[str]) -> str:
    """Walk a canned status list. No HTTP."""
    if not ticks:
        return "failed"
    return str(ticks[-1])


def run(path: Path = FIXTURES) -> list[Clip]:
    model, jobs = load_jobs(path)
    clips: dict[str, Clip] = {}
    order: list[Clip] = []

    for job in jobs:
        shot_id = str(job["id"])
        mode = str(job["mode"])
        duration = int(job.get("duration") or 0)
        source = clips.get(str(job["from_shot"])) if job.get("from_shot") else None
        reason = validate(job, source, model)
        if reason:
            clip = Clip(
                shot_id=shot_id,
                mode=mode,
                status="rejected",
                duration=duration,
                resolution=str(job.get("resolution") or "n/a"),
                reason=reason,
            )
            clips[shot_id] = clip
            order.append(clip)
            continue

        status = fake_poll(list(job.get("poll_ticks") or []))
        if mode == "extend":
            total = (source.duration if source else 0) + duration
            resolution = EXTEND_OUTPUT_CAP
        else:
            total = duration
            resolution = str(job.get("resolution") or "480p")

        clip = Clip(
            shot_id=shot_id,
            mode=mode,
            status=status,
            duration=total if status == "done" else duration,
            resolution=resolution,
            request_id=f"fake-{shot_id}",
            url=f"https://example.invalid/imagine/{shot_id}.mp4" if status == "done" else None,
            reason=None if status == "done" else status,
            ticks=list(job.get("poll_ticks") or []),
        )
        clips[shot_id] = clip
        order.append(clip)

    return order


def _demo() -> None:
    for clip in run():
        extra = clip.reason or clip.url or ""
        print(
            f"{clip.shot_id:20} {clip.mode:8} {clip.status:10} "
            f"{clip.duration:>3}s {clip.resolution:6} {extra}"
        )


if __name__ == "__main__":
    _demo()
