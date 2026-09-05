# /core

Orchestrator, token middleware, and model router. Empty in Phase 1.

**Official vs community:** Official. Talks to Grok Build and the xAI API (`grok-4.6`). Model IDs live in config, never hard-coded. Do not invent `grok-4.7`.

**Phase 0 limits:** `grok-4.6` is current (500k context, no Batch API). Secrets stay in env. No connectors implemented here yet. Human approval before spend.
