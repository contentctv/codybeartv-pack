---
name: wallet-markets-gate
description: Wallet connect and prediction-market gate for CodyBearTV. Use for MetaMask, Phantom, WalletConnect, MoonPay, Polymarket Relayer keys, KYC or KYB direction, and paper-vs-live trading. Never handles seed phrases.
when-to-use: wallet, MetaMask, Phantom, WalletConnect, MoonPay, Polymarket, KYC, KYB, CLOB, paper trading
metadata:
  author: CodyBearTV
  short-description: Wallets and Polymarket HITL
---

# Wallet and markets gate

## Absolute bans

- Never ask for, store, log, or echo a seed phrase, private key, or CLOB signing secret.
- Never place a live order unless the operator types GATE_LIFT LIVE_TRADING in this session.
- Default COPY_MODE / LIVE_TRADING is paper.

## What you may do without GATE_LIFT

- Draft WalletConnect / site-address flows
- Point at official Polymarket wallet-auth docs
- Point at official KYC / KYB onboarding pages (operator completes them)
- Paper scans, gap math, Quarter-Kelly tickets
- Architecture for a higher paywall tier that unlocks the market skill after token check

## Official starting points

- https://docs.polymarket.com/trading/wallets-auth
- Community MCP example — demwick/polymarket-agent-mcp (treat live HTTP mode as dangerous unless bearer-gated)
- Official agents repo was archived 2026-05-11 — verify current official SDK before copying it

## Paywall shape

1. Free / trial token — docs and paper scanner only
2. Monthly token — Imagine + CapCut wrapper
3. Scale-up token — SuperCool entrepreneurial corner + Polymarket paper lab
4. Enterprise — live market tools only after GATE_LIFT and KYC/KYB complete on Polymarket's side

If the existing `phoenix-polymarket-survival-lab` skill is present, defer seat order and paper gates to it.
