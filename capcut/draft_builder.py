"""CapCut draft stub. Prints unofficial tool calls. No MCP, no CapCut, no npx."""

from __future__ import annotations

import json
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "fake_shots.json"
OUT_DIR = Path(__file__).resolve().parent / "out"
DRAFT_PATH = OUT_DIR / "draft.json"

# Unofficial community tools only. CapCut has no official public editing API.
# Allowlist (default deny): create_draft, add_video, add_text, save_draft
# capcut-cli / CapCutAPI — not affiliated with ByteDance. Schema drifts.
# Parameterized args only. Never concatenate LLM text into a shell string.
# Do not npx-install CapCut servers. Do not call live MCP. Do not open CapCut Pro.
# Human still finishes export in CapCut Pro later. Do not touch GarageBand.

ALLOWED_TOOLS = ("create_draft", "add_video", "add_text", "save_draft")


def load_shots(path: Path = FIXTURES) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def plan_calls(spec: dict) -> list[dict]:
    """Build the unofficial call list. No subprocess."""
    width = int(spec.get("width") or 1920)
    height = int(spec.get("height") or 1080)
    shots = list(spec.get("shots") or [])
    draft_id = "draft_fake_001"
    cursor = 0.0
    calls: list[dict] = [
        {
            "unofficial": True,
            "tool": "create_draft",
            "args": {"draft_id": draft_id, "width": width, "height": height},
        }
    ]
    for shot in shots:
        start = cursor
        end = cursor + float(shot.get("duration") or 0)
        calls.append(
            {
                "unofficial": True,
                "tool": "add_video",
                "args": {
                    "draft_id": draft_id,
                    "video_url": shot["mp4"],
                    "start": start,
                    "end": end,
                    "shot_id": shot["id"],
                },
            }
        )
        calls.append(
            {
                "unofficial": True,
                "tool": "add_text",
                "args": {
                    "draft_id": draft_id,
                    "text": shot["title"],
                    "start": start,
                    "end": end,
                    "shot_id": shot["id"],
                },
            }
        )
        cursor = end
    calls.append(
        {
            "unofficial": True,
            "tool": "save_draft",
            "args": {"draft_id": draft_id, "path": str(DRAFT_PATH)},
        }
    )
    for call in calls:
        if call["tool"] not in ALLOWED_TOOLS:
            raise ValueError(f"denied_tool:{call['tool']}")
    return calls


def write_fake_draft(calls: list[dict], spec: dict) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "_comment": "FAKE draft stub. Not CapCut draft_content.json. Unofficial tools only.",
        "unofficial": True,
        "width": spec.get("width"),
        "height": spec.get("height"),
        "shots": spec.get("shots"),
        "intended_calls": calls,
        "human_export": "Operator opens CapCut Pro later. This stub does not launch it.",
    }
    DRAFT_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return DRAFT_PATH


def run(path: Path = FIXTURES) -> list[dict]:
    spec = load_shots(path)
    calls = plan_calls(spec)
    write_fake_draft(calls, spec)
    return calls


def _demo() -> None:
    calls = run()
    for call in calls:
        args = " ".join(f"{k}={v}" for k, v in call["args"].items())
        print(f"UNOFFICIAL  {call['tool']:12}  {args}")
    print(f"wrote {DRAFT_PATH}")


if __name__ == "__main__":
    _demo()
