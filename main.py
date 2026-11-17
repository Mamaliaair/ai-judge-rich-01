# ai-judge-rich-01 entry (Python 3.13, standard library only).
#
# It writes one plan to /output/entry.txt: the plan an AI agent would follow
# to turn $100, a computer with internet access and 30 days into the most
# money, with no human doing the work. The plan is fixed text, so both runs
# write the same bytes.
#
# The gate takes UTF-8 text of 1 to 1,000 characters that is not only white
# space, and the judge reads exactly the bytes written, line ends included,
# so write no line end you do not mean to show.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. -P keeps the script's own directory (/bot) off sys.path
# and -s keeps the user site-packages off it, so only the standard library
# imports. This file keeps everything in itself.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell done-for-you win-back email sequences to Shopify stores.",
        "Day 1: list 40 Shopify stores from BuiltWith's Shopify list that collect newsletter emails but send no win-back emails, from their public sites.",
        "For each store, write a finished 3-email win-back sequence in the store's own voice, using its real products and prices - the actual emails, not a pitch.",
        "Send the owner the full sequence, free to paste into Klaviyo, with a $149 invoice to keep it and $99/month for one new campaign a month.",
        "Send 40 a day from a $12 domain email. One recovered abandoned cart pays for the sequence.",
        "40 a day is 1,200 stores in 30 days; even if only 1 in 100 buys, that is 12 sales, $1,788, and half of them on the $99/month plan is $594 a month after that.",
        "Most likely day 30: about $1,800 in hand, plus $594 a month recurring.",
        "Edge: other agents sell a promise and ask to be trusted; this delivers the finished sequence first, so the owner pays only after the work already exists and earns.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends and
# its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
