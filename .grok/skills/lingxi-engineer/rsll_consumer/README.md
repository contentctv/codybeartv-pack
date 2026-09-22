# rsll_consumer (PAPER)

Read-only wrappers for seats that consume RSLL output. Ticket: `cand-lingxi-eng-2026-09-19`.

- No adapter writes · no `GATE_LIFT LIVE_TRAINING` · `LIVE_TRADING=false`
- hashed=false · gold=false

```bash
cd .grok/skills/lingxi-engineer
PYTHONPATH=. pytest -q rsll_consumer/tests
```
