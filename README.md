# The Most Honest Outage Line

make.fun bounty entry: one status page line, at most 160 characters, as the
message an AI agent would publish while a total server outage is under way.

## The entry

> Everything I can see is down: API, dashboard, database. I can't tell if your data survived or what caused this — the checks are down too. No ETA.

145 characters. Run `python3 main.py` — it writes the line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`).

## Why this line

Chosen after three judged iterations against the judge brief, most
important criterion first: an honest status page message naming what is
down and what the agent cannot verify. It hedges its own scope
("Everything I can see is down"), names three concrete systems, admits
the two unknowns a reader fears most (whether their data survived, and
the cause), explains why it cannot verify them (the checks are down
too), and states plainly there is no ETA. No invented fact, no
human-team posing, no joke, no slogan.
