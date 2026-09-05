# Healer ticket

Open when an integrity or allowlist check fails. **Do not auto-push to main.** Human approval for post / spend / live trade / DNS / collaborator invite.

## Ticket

| Field | Fill in |
|---|---|
| Id | `HEAL-YYYYMMDD-NNN` |
| Opened | ISO-8601 UTC |
| Opened by | agent or operator |
| Severity | low / medium / high / block |
| Check | rehash SKILL.md / allowlist / webhook signature / forbidden-tool retry |
| Failed path | e.g. `.grok/skills/…/SKILL.md` |
| Expected SHA-256 | from `hashes.json` |
| Observed SHA-256 | |
| Tool name (if MCP) | |
| Retry count | |
| Secrets exposed? | yes / no — never paste the secret |
| Proposed fix | |
| Operator decision | approve patch / reject / rotate tokens |
| Push to main | **no** until human says so |

## Notes

What failed and what we will not do (no firewall change, no live Stripe, no Discord send):

```
```

## Close-out

- [ ] Rehash limited to pack `SKILL.md` + plugin manifests (no whole-disk scan)
- [ ] `hashes.json` updated only after operator review
- [ ] Forbidden tool remains denied
- [ ] No git push from the healer
