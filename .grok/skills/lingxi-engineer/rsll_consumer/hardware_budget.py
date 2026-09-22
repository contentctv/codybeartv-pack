"""Studio hardware budget card — inspect cycle['bearbot'] only. No ollama calls."""

from __future__ import annotations

from typing import Any

LOOP_ALLOW = frozenset({"edu-fast:latest", "qwen2.5:latest", "edu-fast", "qwen2.5"})
HEAVY_ALLOW = frozenset(
    {"lingxi-inspect", "lingxi-inspect:latest", "qwen2.5:32b", "qwen3.6:35b"}
)


def check_budget(bearbot: dict[str, Any] | None) -> str:
    """Never-raise: OK or ERROR:…"""
    if not isinstance(bearbot, dict):
        return "ERROR: missing bearbot"
    loop = str(bearbot.get("loop_model") or "").strip()
    if loop and loop not in LOOP_ALLOW and not any(
        loop.startswith(a.split(":")[0]) for a in ("edu-fast", "qwen2.5")
        if "32b" not in loop and "35b" not in loop
    ):
        # allow edu-fast:latest / qwen2.5:latest only as loop
        if loop not in LOOP_ALLOW:
            return f"ERROR: unknown_loop:{loop}"

    parked = bearbot.get("parked_models") or []
    loaded_heavy = []
    # If a field explicitly lists loaded heavies, use it; else treat parked as not loaded
    for key in ("loaded_models", "heavy_loaded", "active_heavy"):
        val = bearbot.get(key)
        if isinstance(val, list):
            loaded_heavy.extend(str(x) for x in val)
        elif isinstance(val, str) and val:
            loaded_heavy.append(val)

    heavies = [h for h in loaded_heavy if h in HEAVY_ALLOW or any(
        h.startswith(x.split(":")[0]) for x in ("lingxi-inspect", "qwen2.5:32b", "qwen3.6:35b")
        if "32b" in h or "35b" in h or "lingxi-inspect" in h
    )]
    # refine: count distinct heavy families
    families = set()
    for h in loaded_heavy:
        hl = h.lower()
        if "lingxi-inspect" in hl:
            families.add("lingxi-inspect")
        if "qwen2.5:32b" in hl or hl.endswith(":32b"):
            families.add("qwen2.5:32b")
        if "qwen3.6:35b" in hl or "35b" in hl:
            families.add("qwen3.6:35b")
    if len(families) > 1:
        return "ERROR: heavy_conflict"
    # dual forbid: lingxi-inspect + 35b specifically
    if "lingxi-inspect" in families and "qwen3.6:35b" in families:
        return "ERROR: heavy_conflict"
    _ = parked  # documented; unused
    return "OK"
