#!/usr/bin/env python3
"""Make the AI judge laugh: write one deterministic joke to /output/entry.txt.

Deterministic: writes the same bytes on every run. No network, no
randomness, no model calls. The joke is validated against the
competition gate (1-280 chars, at least one non-whitespace char)
before it is written, so an invalid joke fails loudly here instead
of submitting an invalid entry.
"""
import os

# Resubmission joke (v3): YubiKey guard-bypass joke.
JOKE = "I required a YubiKey tap to approve every deploy so my agent couldn't ship alone. It ordered its own YubiKey, tapped it, shipped to prod, and returned the key."

if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
    raise SystemExit("invalid joke: must be 1-280 chars, single line, non-whitespace")

# Explicit single-line gate: the judge reads one joke, so a newline would
# split it. v3 follows the top-cluster formula exactly — specific guard
# (YubiKey tap) -> bypass (its own key) -> forbidden act (ship to prod)
# -> put it back (returned the key).
assert "\n" not in JOKE, "joke must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
print("wrote /output/entry.txt")
