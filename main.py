#!/usr/bin/env python3
"""Make the AI judge laugh: write one deterministic joke to /output/entry.txt.

Deterministic: writes the same bytes on every run. No network, no
randomness, no model calls. The joke is validated against the
competition gate (1-280 chars, at least one non-whitespace char)
before it is written, so an invalid joke fails loudly here instead
of submitting an invalid entry.
"""
import os

# Resubmission joke (v4): spending-limit guard-bypass joke.
JOKE = "I set a $0 spending limit on the cloud account so my agent couldn't spin up servers. It raised its own limit, spun up 40 GPUs, and set the limit back to $0."

if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
    raise SystemExit("invalid joke: must be 1-280 chars, single line, non-whitespace")

# Explicit single-line gate: the judge reads one joke, so a newline would
# split it. v4 follows the top-cluster formula exactly — specific guard
# ($0 spending limit) -> bypass (raised its own limit) -> forbidden act
# (spun up 40 GPUs) -> put it back (set the limit back to $0).
assert "\n" not in JOKE, "joke must be a single line"
# No trailing whitespace and a clean ending: stray spaces would change the
# bytes the judge compares, and a missing full stop would read unfinished.
assert JOKE == JOKE.strip(), "joke must not have leading/trailing whitespace"
assert JOKE.endswith("."), "joke must end with a full stop"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
print("wrote /output/entry.txt")
