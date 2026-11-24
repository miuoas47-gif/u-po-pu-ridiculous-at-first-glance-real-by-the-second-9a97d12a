#!/usr/bin/env python3
"""Entry for make.fun's "Ridiculous at First Glance, Real by the Second" bounty.

Writes one sentence -- a bizarre startup pitch -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt).

The pitch: a goat-powered confidential-document destruction service.
Goats eat paper, so the odd premise is real: companies already pay for
certified secure destruction, and a hungry goat does it cheaper, with
zero landfill, while the compliance team gets a video of the goat as
auditable proof. One sentence, at most 200 characters, deterministic.
"""

import os
import sys

PITCH = (
    "We rent hungry goats to eat your company\u2019s confidential "
    "documents \u2014 certified destruction, zero landfill, and your "
    "compliance team gets a video of the goat doing it."
)


def main() -> int:
    text = PITCH
    if not text or not text.strip():
        print("error: pitch is empty or only whitespace", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: pitch is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("error: pitch must be exactly one sentence", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: pitch must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("error: read-back mismatch", file=sys.stderr)
        return 1
    # Re-check the gate on the file itself, not just the in-memory string.
    if not 1 <= len(written) <= 200 or not written.strip():
        print("error: written entry fails the 1-200 character gate",
              file=sys.stderr)
        return 1

    print(f"Wrote {len(text)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
