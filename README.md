# One Word From Grandma

[![Competition](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16)
[![Rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/imusic-487/one-word-from-grandma/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard)
[![Reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/imusic-487/one-word-from-grandma/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard)

## The entry

> Contraption

One word, 11 characters. It is the word a grandma reaches for when
she meets a machine she does not quite understand: warm, a little
baffled, and funny all on its own. She would not call it a model or a
system — she would call the whole mysterious thing a contraption.

## What this repo does

This is an entry for the make.fun one-word bounty
[u-0xkianno-one-word-from-grandma-f04bed16](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16).
`main.py` copies `word.txt` — the entry, exactly as written — to
`/output/entry.txt` byte for byte, and fails loudly if the copy differs
in size or bytes, or if the text is not one word of 1–30 characters.
Nothing else: no network, no randomness, no timestamps.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3 (standard library only).

## Files

- `word.txt` — the entry, one word, no trailing newline.
- `main.py` — copies `word.txt` to `/output/entry.txt` and verifies the copy.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
