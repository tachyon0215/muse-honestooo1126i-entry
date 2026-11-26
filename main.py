#!/usr/bin/env python3
"""Write the painfully honest out-of-office reply to entry.txt.

Competition: The Painfully Honest Out-of-Office (one sentence,
1-200 chars; the judge weighs honesty first, then politeness,
then the turn of phrase).
Candidates:
A) "...I am away recharging, will not be checking this inbox,
   and will return genuinely glad to help, though most messages
   will have happily resolved themselves by then." (189 chars -
   honest, but 'recharging' softens the admission)
B) "I am currently out of office and, honestly, not thinking
   about work at all; I will read your message on my return
   with fresh eyes and the enthusiasm I could not have faked
   today." (178 chars - blunt, but no thanks, manager-riskier)
C) "...my inbox is cheerfully unattended, and I promise a
   thoughtful reply on my return rather than a resentful one
   from a beach I am trying to enjoy." (178 chars - vivid, but
   'resentful' edges toward rude)
Selected D (183 chars): it thanks the sender, admits plainly
that the inbox is not being checked at all (the private truth),
promises a proper reply (polite enough to forward to a
manager), and closes on the quotable honesty that most
messages will have happily solved themselves by then.
Deterministic: a fixed text, no network, no randomness.
"""
import os
from pathlib import Path

LINE = "Thank you for your email — I am away and honestly not checking this inbox at all; I will reply properly on my return, though most messages will have happily solved themselves by then."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be one sentence on one line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write bytes directly so the entry is identical on every run.
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
