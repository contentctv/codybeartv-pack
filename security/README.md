# /security

Phase 6: integrity and allowlist **stubs**. No host firewall changes. No git push.

**Official vs community:** Pack security gate (Red Hat-style). Aligns with official Grok Build sandbox/permissions and OWASP MCP Top 10. Community CapCut tool names are listed as unofficial and disconnected.

**Phase 0 / Phase 6 limits:** Default deny. SHA-256 of pack `SKILL.md` files only (no whole-disk scan). Fail closed on mismatch when a checker exists later. Human approval for post / spend / live trade / DNS / collaborator invite. Healer tickets do **not** auto-push to main. Secrets stay in env.

## Files

| Path | Role |
|---|---|
| `hashes.json` | SHA-256 of the eight pack `SKILL.md` files; empty plugin list |
| `ALLOWLIST.md` | Repo / Discord / IP / MCP name placeholders — not applied |
| `healer-ticket.md` | Template when a check fails |
