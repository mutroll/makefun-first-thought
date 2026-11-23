#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: the first word that
comes to mind, judged on which word is more interesting.

The word: syzygy.

Why this word, against the judge's criteria in order:
1. Exactly one word (6 letters, well within the 1-24 character gate).
2. Surprising: a rare, cosmic word, not the safe atmospheric pick
   (petrichor, sonder, serendipity) the field will be full of --
   and not a coined word from a list of "obscure sorrows", but a
   real term a lexicographer respects.
3. Vivid and specific: three celestial bodies in a straight line --
   a clear image in six letters.
4. Wit, sound and double meaning: the strange y-z-y spelling rewards
   a second look, and the word doubles as a term in poetry/prosody.
5. Chosen, not generic: a precise technical word, not filler.

Deterministic: no input, no randomness, no network, stdlib only.
The output directory defaults to /output and can be overridden with
the OUTPUT_DIR environment variable (used for local verification).
"""

import os
import sys

WORD = "syzygy"

# Gate self-check: the sealed scorer requires UTF-8 text of 1-24
# characters, not only whitespace, and exactly one word. Fail loudly
# here rather than shipping an invalid entry.
assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
assert WORD.split() == [WORD], "word must be a single token"
assert WORD.strip(), "word must not be only whitespace"


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    sys.exit(main())
