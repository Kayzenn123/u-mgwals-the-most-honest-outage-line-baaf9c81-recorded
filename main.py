#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry (program/v1).

Writes a single status page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while a total
server outage is under way.

The line was chosen after three judged iterations against the brief's
criteria, in order: (1) honest status page message naming what is down
and what the agent cannot verify, (2) plain first-person status page
voice, specific about what is broken, (3) plain admission of what the
agent does not know, inventing no cause and no ETA, (4) the agent
reporting on itself, (5) tight and scannable.

Why this line: it hedges its own scope ("Everything I can see is
down" — the claim is limited to the agent's visibility), names three
concrete systems, admits the two unknowns a reader fears most (whether
their data survived, and the cause), explains WHY it cannot verify
them (the checks are down too), and states plainly that there is no
ETA. No invented fact, no human-team posing, no joke, no slogan.
"""

import os
import sys

ENTRY = (
    "Everything I can see is down: API, dashboard, database. "
    "I can't tell if your data survived or what caused this "
    "\u2014 the checks are down too. No ETA."
)

MAX_CHARS = 160


def main() -> int:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        print(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the file's characters, so the
    # file must hold exactly the entry text and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
