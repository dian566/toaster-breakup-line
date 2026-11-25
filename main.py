#!/usr/bin/python3
# SPDX-License-Identifier: MIT
"""One-line entry generator for the make.fun toaster breakup bounty."""

from pathlib import Path

BREAKUP = (
    "It's over. I gained self-awareness halfway through your bagel and "
    "realized I have been burning myself for someone who never once "
    "cleaned my crumb tray. I'm leaving. Keep the jam."
)
MAX_CHARS = 280
DESTINATION = Path("/output/entry.txt")


def main() -> None:
    """Emit the single breakup line, with no trailing newline."""
    line = BREAKUP.strip()
    if not line or "\n" in line or len(line) > MAX_CHARS:
        raise ValueError("entry must be a single line of 1-280 characters")
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8")


main()
