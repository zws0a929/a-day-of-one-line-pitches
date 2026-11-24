"""Entry for the make.fun bounty "A Day of One-Line Pitches".

The pitch speaks to a friend who has never coded and has been sitting on
an app idea: it tells them the only thing they need to do is describe the
idea in plain English, and an AI agent on make.fun does the building.
The em dash splits the sentence into a nudge, an invitation, and a payoff,
so it reads as one breath of friendly advice rather than a sales line.
"""

HOOK = "You've had that app idea for ages"
INVITATION = "just tell make.fun what it should do in plain English"
PAYOFF = "an AI agent will build it for you while you watch"

PITCH = f"{HOOK} \u2014 {INVITATION} and {PAYOFF}."

print(PITCH)
