#!/bin/bash
# Hook: Remind operator to verify state after file modifications.
# Contract for $1 (modified files list) is UNVERIFIED.
# DO NOT auto-run Ollama from this hook.

MODIFIED_FILES="$1"

echo "================================================================="
echo "[!] DESK REMINDER: Files modified."
echo "[!] Action Required: Run ./verify.sh manually to confirm state."
echo "[!] Fences: GENERATE=off | PUBLISH=off"
echo "================================================================="
