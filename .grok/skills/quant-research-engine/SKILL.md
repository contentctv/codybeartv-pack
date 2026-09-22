---
name: quant-research-engine
description: Applied math and scientific-method layer for CodyBearTV research, token budgets, queues, and paper trading. Use when sizing risk, scoring sources, designing backoff, or writing RESEARCH.md claims that need numbers.
when-to-use: mathematics, Kelly, rate limit, token budget, scientific method, Blackwell, experiment design, statistics
metadata:
  author: CodyBearTV
  short-description: Math and scientific method
---

# Quant research engine

Use numbers. Do not perform theater.

## Scientific method for this pack

1. Claim in one sentence.
2. Official source or dataset.
3. Test that could falsify the claim.
4. Result table.
5. Decision (build / wrap / wait / reject).

If you cannot name a falsifier, the claim is not ready to become code.

## Default tools

- Rate limits and Imagine cost — use published xAI tables, not guesses.
- Queues — exponential backoff with jitter. Cap parallel Imagine jobs (Build media batch cap is small; treat 4 video gens as a ceiling unless docs say otherwise).
- Token spend — estimate input/output before a long Grok 4.6 agent loop. Context past 200k tokens costs more on 4.6. Keep skills lean.
- Trading math — Quarter-Kelly, 5 percent cap, paper log with Brier score. Defer live rules to `wallet-markets-gate` and the existing phoenix-polymarket skill.

## Source scoring (short form)

Prefer primary documents. Discard garbled reprints. If two sources disagree, keep both rows and mark which is official.

## Output

When this skill runs, include a tiny evidence table

| Claim | Source | Falsifier | Status |
