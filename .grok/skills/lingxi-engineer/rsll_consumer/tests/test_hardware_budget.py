from __future__ import annotations

import json
from pathlib import Path

from rsll_consumer.hardware_budget import check_budget

FIX = Path(__file__).resolve().parent / "fixtures"


def test_hardware_loop_allowlist() -> None:
    assert check_budget({"loop_model": "edu-fast:latest"}) == "OK"
    assert check_budget({"loop_model": "qwen2.5:latest"}) == "OK"
    assert check_budget({"loop_model": "mystery:99b"}).startswith("ERROR: unknown_loop")


def test_hardware_one_heavy() -> None:
    cycle = json.loads((FIX / "last-cycle-heavy-conflict.json").read_text())
    assert check_budget(cycle["bearbot"]).startswith("ERROR: heavy_conflict")
    assert check_budget({"loop_model": "edu-fast:latest", "loaded_models": ["lingxi-inspect"]}) == "OK"
