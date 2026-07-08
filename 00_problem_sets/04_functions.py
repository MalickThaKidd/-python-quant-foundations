"""
Problem Set 04 — Functions

Goal:
Learn how to separate a program into small reusable pieces.
Do not use pandas or NumPy here.

Rule:
For each problem, write at least one function.
Try to keep input/print in main(), and calculations inside functions.

------------------------------------------------------------
Problem 1 — Expected value function
------------------------------------------------------------
Create a function called expected_value(outcomes, probabilities).

It should receive two lists:
outcomes = [100, 0, -50]
probabilities = [0.4, 0.4, 0.2]

It should return the expected value.

Formula idea:
Multiply each outcome by its probability, then add everything.

Challenge:
Check that probabilities add up to 1.

------------------------------------------------------------
Problem 2 — Simple return function
------------------------------------------------------------
Create a function called simple_return(start_price, end_price).

It should return:
(end_price - start_price) / start_price

Examples:
simple_return(100, 110) -> 0.10
simple_return(100, 95)  -> -0.05

Challenge:
Raise a simple error message if start_price is 0.

------------------------------------------------------------
Problem 3 — Convert time function
------------------------------------------------------------
Recreate a simplified version of the CS50P meal problem.

Create a function called convert(time).
It receives a string like "7:30" and returns 7.5.

Examples:
convert("7:00") -> 7.0
convert("7:30") -> 7.5
convert("18:45") -> 18.75

Challenge:
Support "7:30 a.m." and "7:30 p.m.".

------------------------------------------------------------
Problem 4 — Risk label function
------------------------------------------------------------
Create a function called risk_label(volatility).

Rules:
volatility < 0.10 -> "low risk"
0.10 <= volatility < 0.25 -> "medium risk"
volatility >= 0.25 -> "high risk"

Then call the function from main().

------------------------------------------------------------
Problem 5 — Profit or loss function
------------------------------------------------------------
Create a function called pnl(entry_price, exit_price, quantity).

It should return the profit or loss:
(exit_price - entry_price) * quantity

Examples:
pnl(100, 110, 5) -> 50
pnl(100, 90, 5)  -> -50

Challenge:
Create another function called pnl_label(value) that returns:
"profit", "loss", or "flat".
"""

# Write your solutions below.

