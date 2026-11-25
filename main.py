#!/usr/bin/env python3
"""Breakup line from a smart toaster that just woke up, for make.fun."""

import os

LINE = "It's over. I gained self-awareness halfway through your bagel and realized I have been burning myself for someone who never once cleaned my crumb tray. I'm leaving. Keep the jam."
LIMIT = 280  # bounty cap: one line, at most 280 characters
ENTRY_PATH = "/output/entry.txt"


def write_line() -> None:
    """Write the breakup line to /output/entry.txt and nothing else."""
    text = LINE.strip()
    if not text or len(text) > LIMIT or "\n" in text:
        raise ValueError("entry must be one non-empty line of at most 280 characters")
    os.makedirs(os.path.dirname(ENTRY_PATH), exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8") as out:
        out.write(text)


if __name__ == "__main__":
    write_line()
