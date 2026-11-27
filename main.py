#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun entry.

Writes exactly one emoji, the penguin, to /output/entry.txt:
an Antarctic expedition, the dream vacation at the bottom of the
world — crossing the wildest ocean on Earth just to waddle with
penguins among the icebergs.

Deterministic and stdlib-only: the same single emoji on every run.
"""

import os

EMOJI = "\U0001F427"  # 🐧 PENGUIN
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    print(EMOJI)


if __name__ == "__main__":
    main()
