#!/usr/bin/env python3
"""One Line to Your Younger Self — writes the line to /output/entry.txt."""

import os

# The line is the whole entry: one line to a younger self, no context, no second sentence.
ENTRY = "Stop trying to impress people who won't remember your name in five years — and call grandma, she misses you."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
