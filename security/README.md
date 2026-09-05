# /security

Integrity hashes, allowlists, and healer tickets. Empty in Phase 1.

**Official vs community:** Pack security gate (Red Hat-style). Aligns with official Grok Build sandbox/permissions and OWASP MCP Top 10. Planned file: `hashes.json` (SHA-256 of plugin manifests and SKILL.md). Fail closed on mismatch.

**Phase 0 limits:** Default deny. Allowlist IPs / repo / Discord guild / MCP tool names. Treat every tool result as untrusted. Human approval for post / spend / live trade / DNS / collaborator invite. No hashes written yet — stubs only.
