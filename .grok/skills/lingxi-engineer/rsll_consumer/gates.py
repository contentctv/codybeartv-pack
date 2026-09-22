"""Paper gate checks from cycle JSON + anchors/0001-gates.jsonl."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Gates:
    live_trading: bool
    live_training: bool
    generate: str
    publish: str
    gold_checkbox: bool
    promoted_to_local: bool


def parse_gates(cycle: dict[str, Any]) -> Gates:
    g = cycle.get("gates") or {}
    return Gates(
        live_trading=bool(g.get("LIVE_TRADING", False)),
        live_training=bool(g.get("LIVE_TRAINING", False)),
        generate=str(g.get("GENERATE", "off")).lower(),
        publish=str(g.get("PUBLISH", "off")).lower(),
        gold_checkbox=bool(cycle.get("gold_checkbox", False)),
        promoted_to_local=bool(cycle.get("promoted_to_local", False)),
    )


def assert_paper_gates(gates: Gates) -> str:
    """Never-raise: OK or ERROR:…"""
    if gates.live_trading:
        return "ERROR: LIVE_TRADING=true refused"
    if gates.live_training:
        return "ERROR: LIVE_TRAINING=true refused"
    if gates.generate not in {"off", "false", "0"}:
        return f"ERROR: GENERATE={gates.generate!r} not off"
    if gates.publish not in {"off", "false", "0"}:
        return f"ERROR: PUBLISH={gates.publish!r} not off"
    return "OK"


def read_anchor_gates_line(rsll_root: Path) -> str:
    """Return first line of anchors/0001-gates.jsonl or ERROR — never raises."""
    try:
        p = Path(rsll_root) / "anchors" / "0001-gates.jsonl"
        if not p.is_file():
            # pack root form
            p = Path(rsll_root) / "rsll" / "anchors" / "0001-gates.jsonl"
        if not p.is_file():
            return "ERROR: MISSING_ANCHOR"
        line = p.read_text(encoding="utf-8").splitlines()[0].strip()
        json.loads(line)  # validate JSON
        return "OK"
    except Exception as exc:  # noqa: BLE001
        return f"ERROR: ANCHOR:{type(exc).__name__}"


def list_adapter_ids(rsll_root: Path) -> list[str]:
    """List-only — no writes."""
    d = Path(rsll_root) / "adapters"
    if not d.is_dir():
        d = Path(rsll_root) / "rsll" / "adapters"
    if not d.is_dir():
        return []
    return sorted(p.name for p in d.iterdir() if p.is_file())


def gold_empty(rsll_root: Path) -> bool:
    d = Path(rsll_root) / "gold"
    if not d.is_dir():
        d = Path(rsll_root) / "rsll" / "gold"
    if not d.is_dir():
        return True
    return not any(d.iterdir())
