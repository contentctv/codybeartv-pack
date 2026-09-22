# Skill: desk-verify

**Description:** On-demand desk verification. Runs `./verify.sh` locally to confirm state.

**Execution Steps:**
1. Wait for operator to explicitly request this skill. Do not auto-run.
2. Execute `./verify.sh`.
3. Parse for `PASS` or `FAIL`.
4. **IF FAIL:** Do not weaken `verify.sh` or loosen the grep. First, propose a patch to the drill/router inject prompt to fix the string hallucination.
5. Only propose a patch to `verify.sh` if the target marker is genuinely absent from `TRACKING.md` itself.
