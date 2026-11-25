#!/usr/bin/env python3
"""One Line, No Deadline Met entry (account A).

Writes one single-line joke excusing a missed deadline to
/output/entry.txt. Deterministic, stdlib only, no network, no secrets.

The joke: instead of apologising, the speaker reframes the miss as
being early for a deadline that does not exist yet — a cornered-person
excuse with a surprise turn, and it dodges the stock dog-ate-it and
my-alarm-didn't-go-off retreads.
"""

import os

# The excuse: a reframe — not late, just early for the next deadline.
# Tightened: the em dash lands the turn right after "deadline", and the
# punch ("which nobody has announced yet") closes the sentence.
EXCUSE = (
    "I didn't miss the deadline — I'm just early for the next one, "
    "which nobody has announced yet."
)

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def verify(text: str) -> str:
    """Return the excuse, stripped, after enforcing the gate."""
    line = text.strip()
    if not line:
        raise ValueError("excuse is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"excuse is {len(line)} chars, must be at most {MAX_CHARS}")
    if "\n" in line:
        raise ValueError("excuse must be a single line")
    return line


def write_entry(text: str, path: str = OUT_PATH) -> str:
    """Verify the excuse and write it to the output file."""
    line = verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    return line


def main() -> None:
    line = write_entry(EXCUSE)
    print(f"Wrote {len(line)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
