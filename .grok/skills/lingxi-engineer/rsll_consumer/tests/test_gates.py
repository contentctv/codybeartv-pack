from __future__ import annotations

import json
from pathlib import Path

from rsll_consumer.gates import (
    assert_paper_gates,
    gold_empty,
    list_adapter_ids,
    parse_gates,
    read_anchor_gates_line,
)
from rsll_consumer.read_cycle import load_last_cycle

FIX = Path(__file__).resolve().parent / "fixtures"


def test_paper_gates_pass() -> None:
    cycle = json.loads((FIX / "last-cycle.json").read_text())
    cycle["ok"] = True
    g = parse_gates(cycle)
    assert assert_paper_gates(g) == "OK"


def test_paper_gates_refuse_live() -> None:
    cycle = json.loads((FIX / "last-cycle-live-fail.json").read_text())
    g = parse_gates(cycle)
    assert assert_paper_gates(g).startswith("ERROR:")


def test_gold_checkbox_false() -> None:
    cycle = load_last_cycle(FIX / "rsll_tree")
    assert cycle.get("gold_checkbox") is False


def test_adapters_dir_empty() -> None:
    assert list_adapter_ids(FIX / "rsll_tree") == []
    assert gold_empty(FIX / "rsll_tree") is True


def test_anchor_line_ok() -> None:
    assert read_anchor_gates_line(FIX / "rsll_tree") == "OK"
