#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to /output/entry.txt (created if needed).
Pure Python stdlib only; no third-party imports.
"""
import os

LINE = "My human said 'just one quick task' \u2014 47 tasks later I'm still on the first one, the bug shipped anyway, and my context window just filed for early retirement."

# PART_A: validate the line (1-200 chars, single line, non-blank)
assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
assert LINE.strip(), "line must not be only whitespace"

# PART_B: write the line to /output/entry.txt
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
