from __future__ import annotations

import json
from pathlib import Path

import pytest

from rsll_consumer.read_cycle import load_last_cycle, require_schema

FIX = Path(__file__).resolve().parent / "fixtures"


def test_load_last_cycle_ok(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.syspath_prepend(str(FIX.parent.parent.parent))
    root = FIX / "rsll_tree"
    cycle = load_last_cycle(root)
    assert cycle.get("ok") is True
    assert require_schema(cycle) == "OK"
    assert cycle.get("schema") == "crystal-learn-card.v1"
    assert "status" in cycle


def test_missing_cycle_soft(tmp_path: Path) -> None:
    cycle = load_last_cycle(tmp_path)
    assert cycle.get("ok") is False
    assert cycle.get("error") == "MISSING_CYCLE"
    assert require_schema(cycle).startswith("ERROR:")


def test_no_secret_fields_leaked() -> None:
    cycle = load_last_cycle(FIX / "rsll_tree")
    blob = json.dumps(cycle)
    assert "PRIVATE_KEY" not in blob
    assert "api_secret" not in blob.lower() or "[REDACTED]" in blob
