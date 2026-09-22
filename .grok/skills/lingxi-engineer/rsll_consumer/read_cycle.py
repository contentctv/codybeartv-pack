"""Read-only loader for rsll/telemetry/last-cycle.json."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

_SECRET_KEY = re.compile(r"(key|secret|seed|private)", re.I)
_HEX64 = re.compile(r"\b[0-9a-fA-F]{64}\b")


def _scrub(obj: Any) -> Any:
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            if _SECRET_KEY.search(str(k)):
                out[k] = "[REDACTED]"
            else:
                out[k] = _scrub(v)
        return out
    if isinstance(obj, list):
        return [_scrub(x) for x in obj]
    if isinstance(obj, str) and _HEX64.search(obj) and "0x" not in obj[:2].lower():
        # scrub bare 64-hex blobs that look like keys (not addresses)
        return "[REDACTED_HEX]"
    return obj


def load_last_cycle(root: Path) -> dict[str, Any]:
    """Load last-cycle.json under rsll root or skill-relative pack root.

    ``root`` may be the pack root (contains ``rsll/``) or the ``rsll/`` dir itself.
    Never raises — returns ``{"ok": False, "error": "..."}`` on failure.
    """
    try:
        root = Path(root)
        candidates = [
            root / "rsll" / "telemetry" / "last-cycle.json",
            root / "telemetry" / "last-cycle.json",
            root / "last-cycle.json",
        ]
        path = next((p for p in candidates if p.is_file()), None)
        if path is None:
            return {"ok": False, "error": "MISSING_CYCLE"}
        raw = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            return {"ok": False, "error": "CYCLE_NOT_OBJECT"}
        cleaned = _scrub(raw)
        cleaned["ok"] = True
        cleaned["_path"] = str(path)
        return cleaned
    except Exception as exc:  # noqa: BLE001 — never-raise contract
        return {"ok": False, "error": f"LOAD_FAIL:{type(exc).__name__}"}


def require_schema(cycle: dict[str, Any], expect: str = "crystal-learn-card.v1") -> str:
    """Return OK or ERROR:… — never raises."""
    if not cycle.get("ok", True) and cycle.get("error"):
        return f"ERROR: {cycle['error']}"
    schema = cycle.get("schema")
    if schema != expect:
        return f"ERROR: schema={schema!r} expect={expect!r}"
    return "OK"
