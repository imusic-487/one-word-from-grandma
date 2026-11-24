"""One Word From Grandma — make.fun entry.

Copies word.txt (the entry, exactly one word, 1-30 characters) to
/output/entry.txt byte for byte. MAKEFUN_OUTPUT_DIR, when set, stands
in for /output so the entry can be tested locally.

Fails loudly if anything is off: the copy's size differs, its bytes
differ from word.txt, the text is not 1-30 characters, it is only
white space, it is not exactly one word, or it carries leading or
trailing white space (a stray newline would reach the judge as part
of the entry, so the word must be exactly the word, nothing around it).

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORD_FILE = HERE / "word.txt"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    source = WORD_FILE.read_bytes()
    try:
        text = source.decode("utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"word.txt is not valid UTF-8: {exc}") from exc

    if not 1 <= len(text) <= 30:
        raise RuntimeError(
            f"entry is {len(text)} characters, allowed 1-30"
        )
    if not text.strip():
        raise RuntimeError("entry must not be only white space")
    if text != text.strip():
        raise RuntimeError(
            "entry must not have leading or trailing white space"
        )
    if len(text.split()) != 1:
        raise RuntimeError("entry must be exactly one word")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(source)

    written = OUTPUT_FILE.read_bytes()
    if len(written) != len(source):
        raise RuntimeError(
            f"copy size differs: wrote {len(written)} bytes, "
            f"source is {len(source)} bytes"
        )
    if written != source:
        offset = next(
            i for i, (a, b) in enumerate(zip(written, source)) if a != b
        )
        raise RuntimeError(
            f"copy bytes differ from word.txt: first difference at "
            f"byte {offset} (wrote 0x{written[offset]:02x}, "
            f"source is 0x{source[offset]:02x})"
        )

    print(f"wrote {OUTPUT_FILE} ({len(source)} bytes, {len(text)} characters)")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
