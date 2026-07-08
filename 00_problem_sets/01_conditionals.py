"""
Problem Set 01 — Conditionals: if / elif / else

Goal:
Practice decision-making in Python using if, elif, and else.
Do not use pandas or NumPy here.

How to work:
Pick one mini-problem at a time. Write the solution below the problem.
When it works, comment it out or move it to a _practice.py file and redo it from memory.

------------------------------------------------------------
Problem 1 — Market mood
------------------------------------------------------------
Ask the user for today's market return in percent.

Examples:
- If the user enters 2.5, print: "strong green day"
- If the user enters 0.4, print: "green day"
- If the user enters 0, print: "flat day"
- If the user enters -0.6, print: "red day"
- If the user enters -3, print: "strong red day"

Suggested ranges:
return >= 2        -> strong green day
0 < return < 2     -> green day
return == 0        -> flat day
-2 < return < 0    -> red day
return <= -2       -> strong red day

Hints:
- input() returns a string.
- Convert the input to float.
- Be careful with the order of your conditions.

------------------------------------------------------------
Problem 2 — Trading fee calculator
------------------------------------------------------------
Ask the user for a trade amount in FCFA.

Fee rules:
- If amount < 10_000, fee = 100
- If amount is between 10_000 and 100_000 included, fee = 500
- If amount > 100_000, fee = 1% of the amount

Print the fee.

Examples:
Amount: 5000       -> Fee: 100
Amount: 50000      -> Fee: 500
Amount: 200000     -> Fee: 2000.0

Hints:
- Use int or float.
- Think about inclusive boundaries.

------------------------------------------------------------
Problem 3 — Risk level
------------------------------------------------------------
Ask the user for portfolio volatility as a decimal.

Examples:
0.05 means 5% volatility.
0.20 means 20% volatility.

Rules:
volatility < 0.10       -> low risk
0.10 <= volatility < 0.25 -> medium risk
volatility >= 0.25      -> high risk

Print the risk level.

------------------------------------------------------------
Problem 4 — Simple login logic
------------------------------------------------------------
Ask the user for a username and a password.

Rules:
- username must be "malick"
- password must be "quant2026"

If both are correct, print: "access granted"
If username is correct but password is wrong, print: "wrong password"
If username is wrong, print: "unknown user"

Hints:
- Use and.
- The order matters.

------------------------------------------------------------
Problem 5 — Meal time, simplified
------------------------------------------------------------
Ask the user for an hour as an integer, for example 7, 12, 18.

Rules:
7 or 8    -> breakfast time
12 or 13  -> lunch time
18 or 19  -> dinner time
otherwise -> not meal time

Challenge:
After solving it with integers, modify it to accept floats like 7.5 or 18.75.
"""

# Write your solutions below.

