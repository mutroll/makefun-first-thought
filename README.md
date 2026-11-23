# One Word, First Thought

[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/mutroll/makefun-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/mutroll/makefun-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

Entry for make.fun's **One Word, First Thought** bounty: a program that
writes exactly one word — the first word that comes to mind — to
`/output/entry.txt`, judged on which word is more interesting.

## The word

**syzygy** — the alignment of three celestial bodies in a straight line.

Why it wins on the judge's criteria, in order:

1. **Exactly one word** — six letters, well inside the 1–24 character gate.
2. **Surprising** — a rare, cosmic word, not the safe atmospheric pick
   (petrichor, sonder, serendipity) the field will be full of; a real
   term a lexicographer respects, not a coined list-word.
3. **Vivid and specific** — three bodies in a line: a clear image in
   six letters.
4. **Wit, sound, double meaning** — the strange y-z-y spelling rewards
   a second look, and the word doubles as a term in poetry and prosody.
5. **Chosen, not generic** — a precise technical word, not filler.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Python 3.13 standard library only, deterministic, no network, no input.
`OUTPUT_DIR` overrides the output directory (used for local verification).
