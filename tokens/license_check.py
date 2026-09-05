"""Stub license check. Fake tokens only. No Stripe, no network, no real keys."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "fake_tokens.json"

# Scopes the stub knows. Unknown scope → deny (default deny).
KNOWN_SCOPES = frozenset(
    {
        "docs:read",
        "imagine:dry-run",
        "imagine:poller",
        "capcut:draft",
        "newsletter:current",
    }
)


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str
    token_id: str | None
    token_type: str | None


def _parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value)


def load_fixtures(path: Path = FIXTURES) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("tokens") or [])


def check(
    presented: str,
    requested_scope: str,
    now: datetime | None = None,
    records: list[dict] | None = None,
) -> Decision:
    """Default-deny lookup against local fake records. No HTTP."""
    clock = now or datetime.now(timezone.utc)
    if clock.tzinfo is None:
        clock = clock.replace(tzinfo=timezone.utc)

    if requested_scope not in KNOWN_SCOPES:
        return Decision(False, "unknown_scope", None, None)

    secret = (presented or "").strip()
    if not secret:
        return Decision(False, "missing_token", None, None)

    for row in records if records is not None else load_fixtures():
        if row.get("secret") != secret:
            continue
        token_id = str(row.get("id") or "")
        token_type = str(row.get("type") or "")
        if row.get("status") != "active":
            return Decision(False, "inactive", token_id, token_type)
        expires = _parse_dt(str(row["expires_at"]))
        if clock > expires:
            return Decision(False, "expired", token_id, token_type)
        scopes = set(row.get("scopes") or [])
        if requested_scope not in scopes:
            return Decision(False, "scope_denied", token_id, token_type)
        return Decision(True, "ok", token_id, token_type)

    return Decision(False, "unknown_token", None, None)


def _demo() -> None:
    now = datetime(2026, 9, 5, 12, 0, tzinfo=timezone.utc)
    cases = [
        ("cbtv_trial_FAKE_week_001", "docs:read"),
        ("cbtv_trial_FAKE_week_001", "imagine:poller"),
        ("cbtv_news_FAKE_2026w36", "newsletter:current"),
        ("cbtv_paid_FAKE_monthly_001", "capcut:draft"),
        ("cbtv_news_FAKE_expired", "docs:read"),
        ("not-a-token", "docs:read"),
    ]
    for secret, scope in cases:
        d = check(secret, scope, now=now)
        print(f"{scope:20} allowed={d.allowed!s:5} {d.reason:16} id={d.token_id}")


if __name__ == "__main__":
    _demo()
