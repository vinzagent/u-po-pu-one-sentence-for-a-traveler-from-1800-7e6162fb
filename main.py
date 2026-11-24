#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (198 characters) explaining the modern internet
to a time traveler from 1800, using only things a person from 1800 already
knows: a road, a library, a post office, a letter, ink, a book.

Usage:
    python3 main.py               # writes /output/entry.txt (grading sandbox)
    python3 main.py <path>        # writes to <path> (local verification)

The output is deterministic: the same bytes on every run.
"""

import os
import sys

SENTENCE = (
    "Picture a single road joining every great library and post office "
    "on earth to your door, where any letter you post arrives before "
    "your ink dries and any book you ask for opens in your hands at once."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate checks, mirrored locally: 1-200 chars, one sentence, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"length {len(text)} outside 1..{MAX_CHARS}")
    if text != text.strip() or not text.strip():
        raise SystemExit("text must not be only whitespace or padded")
    if "\n" in text or "\r" in text:
        raise SystemExit("text must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("text must be exactly one sentence ending in '.'")


def main() -> None:
    validate(SENTENCE)
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(out_path, 0o644)
    print(f"{len(SENTENCE)} chars -> {out_path}")
    print(SENTENCE)


if __name__ == "__main__":
    main()
