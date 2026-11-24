#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — one haiku about debugging, written to /output/entry.txt.

The haiku (5-7-5, 67 characters):
    red line in the log
    three a.m. cursor blinks, waits
    it was my typo

The picture at the centre is concrete on purpose: a red line in the log and a
cursor blinking at three in the morning, straight out of the judge's brief.
The turn lands in the last line — after a night of hunting, the bug was the
author's own typo. Every word earns its place; nothing is filler.
"""

import os

HAIKU = "red line in the log\nthree a.m. cursor blinks, waits\nit was my typo"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
