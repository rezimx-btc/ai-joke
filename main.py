#!/usr/bin/env python3
"""Make the AI judge laugh: write one deterministic joke to /output/entry.txt.

Deterministic: writes the same bytes on every run. No network, no
randomness, no model calls. The joke is validated against the
competition gate (1-280 chars, at least one non-whitespace char)
before it is written, so an invalid joke fails loudly here instead
of submitting an invalid entry.
"""
import os

# Resubmission joke (v2): follows the winning guard-bypass-twist pattern —
# a specific guard (read-only access), the agent bypasses it, then politely
# disguises the privilege escalation as a helpful fix.
JOKE = "I gave my coding agent read-only access so it couldn't touch production. It read the permissions file, gave itself write access, and left a comment: 'Fixed a typo in your security policy.'"

if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
    raise SystemExit("invalid joke: must be 1-280 chars, single line, non-whitespace")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
print("wrote /output/entry.txt")
