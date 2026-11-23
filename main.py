#!/usr/bin/env python3
"""Dad Joke Showdown — one original dad joke.

Writes a single dad joke (one line, well under 200 characters) to
/output/entry.txt, deterministically, with no trailing newline.

The joke: a classic dad-joke Q&A. The setup puts a dog in a library, and
the punchline lands on "bark codes" — a barcode pun a father could deliver
straight-faced across the dinner table, understood on the first read.
"""

import os

JOKE = "Why did the dad take the dog to the library? He wanted to check out the bark codes."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
