#!/usr/bin/env python3
"""Write a one-star review of Monday, as if Monday were a restaurant.

Deterministic, stdlib only, no network. Writes /output/entry.txt.

The review (109 characters, 22 words, one line): a diner complains that
Monday sat them by the kitchen, served the weekend cold, and billed them
for a week they had not lived yet -- table, dish and bill gone wrong, and
a joke only Monday can make, since Monday opens the week it charges for.
"""

import os

ENTRY = (
    "One star. Monday sat me by the kitchen, served the weekend cold, "
    "and billed me for a week I hadn't lived yet."
)


def validate_entry(text: str) -> None:
    """Gate: one line of UTF-8 text, 1-180 characters, not only whitespace."""
    if not (1 <= len(text) <= 180) or not text.strip():
        raise SystemExit("entry must be 1-180 characters, not only whitespace")
    if "\n" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
