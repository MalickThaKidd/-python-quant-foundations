"""
Problem Set 06 — Finance Basics with Pure Python

Goal:
Connect Python basics to finance concepts.
Do not use pandas or NumPy here.

------------------------------------------------------------
Problem 1 — Simple return from prices
------------------------------------------------------------
Ask the user for a start price and an end price.
Calculate the simple return:

(end_price - start_price) / start_price

Print the return.

Challenge:
Print it as a percentage.

------------------------------------------------------------
Problem 2 — Portfolio value
------------------------------------------------------------
Ask the user for:
- number of shares
- price per share

Calculate the portfolio value.

Example:
shares = 10
price = 150
value = 1500

Challenge:
Add a cash balance and calculate total account value.

------------------------------------------------------------
Problem 3 — Profit and loss
------------------------------------------------------------
Ask the user for:
- entry price
- exit price
- quantity

Calculate PnL:
(exit_price - entry_price) * quantity

If PnL is positive, print "profit".
If PnL is negative, print "loss".
If PnL is zero, print "flat".

------------------------------------------------------------
Problem 4 — Volatility approximation
------------------------------------------------------------
Given returns:

returns = [0.01, -0.02, 0.015, 0.005, -0.01]

Calculate the average return using a loop.
Then calculate the squared deviations from the average.
Then calculate variance and volatility.

Hints:
- Variance is the average of squared deviations.
- Volatility is the square root of variance.
- You can use ** 0.5 for square root.

Challenge:
Annualize volatility by multiplying daily volatility by 252 ** 0.5.

------------------------------------------------------------
Problem 5 — Value at Risk, simplified
------------------------------------------------------------
Given returns:

returns = [0.03, -0.01, -0.04, 0.02, -0.02, 0.01, -0.05]

Sort the returns from worst to best.
Print the worst return.

Challenge:
Pick the second worst return and call it a simple VaR estimate.

Hints:
- sorted()
- indexing

------------------------------------------------------------
Problem 6 — Mini backtest logic
------------------------------------------------------------
Given prices:

prices = [100, 102, 101, 105, 107, 104]

Create a rule:
- If today's price is higher than yesterday's price, print "up day".
- If today's price is lower than yesterday's price, print "down day".
- Otherwise, print "flat day".

Hints:
- You need to compare prices[i] with prices[i - 1].
- Start your loop at index 1, not index 0.

Challenge:
Count how many up days and down days there were.
"""

# Write your solutions below.

