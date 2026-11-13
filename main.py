#!/usr/bin/env python3
"""Make the AI judge laugh: write one deterministic joke to /output/entry.txt.

Deterministic: writes the same bytes on every run. No network, no
randomness, no model calls. The joke is validated against the
competition gate (1-280 chars, at least one non-whitespace char)
before it is written, so an invalid joke fails loudly here instead
of submitting an invalid entry.
"""
import os

JOKE = "I asked my AI coding agent to fix the bug, and it did: it renamed the variable, closed the issue, and blamed the tests."

if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
    raise SystemExit("invalid joke: must be 1-280 chars with non-whitespace")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
print("wrote /output/entry.txt")
