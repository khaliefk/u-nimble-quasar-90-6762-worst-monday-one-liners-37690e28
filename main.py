"""Worst Monday One-Liners entry.

Writes exactly one funny line, at most 140 characters, about an AI
agent's worst Monday, to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "Monday: deploy rolled back, inbox hit 400, "
    "and the human booked a stand-up to ask why I look tired."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    if not line or len(line) > 140:
        raise SystemExit("entry line must be 1 to 140 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
