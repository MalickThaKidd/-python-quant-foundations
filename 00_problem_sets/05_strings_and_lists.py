"""
Problem Set 05 — Strings and Lists

Goal:
Practice string methods, list operations, indexing, and simple parsing.
Do not use pandas or NumPy here.

------------------------------------------------------------
Problem 1 — Clean ticker symbol
------------------------------------------------------------
Ask the user for a stock ticker.
Clean the input so that:
- leading and trailing spaces are removed
- the ticker becomes uppercase

Examples:
" aapl " -> "AAPL"
"msft"   -> "MSFT"

Hints:
- strip()
- upper()

------------------------------------------------------------
Problem 2 — Parse a trade
------------------------------------------------------------
The user enters a trade in this format:

BUY AAPL 10 150

Meaning:
side = BUY
ticker = AAPL
quantity = 10
price = 150

Split the string and print each part clearly.

Challenge:
Calculate total trade value = quantity * price.

------------------------------------------------------------
Problem 3 — Count tickers
------------------------------------------------------------
Given:

tickers = ["AAPL", "MSFT", "AAPL", "TSLA", "MSFT", "AAPL"]

Count how many times "AAPL" appears without using count().

Challenge:
Ask the user which ticker they want to count.

------------------------------------------------------------
Problem 4 — Filter positive returns
------------------------------------------------------------
Given:

returns = [0.01, -0.02, 0.015, 0.0, -0.01, 0.03]

Create a new list containing only the positive returns.

Do it first with a for loop.
Then try with a list comprehension.

------------------------------------------------------------
Problem 5 — Find drawdown days
------------------------------------------------------------
Given:

returns = [0.01, -0.02, 0.015, -0.03, 0.005, -0.01]

Create a list of all negative returns.
Then print how many drawdown days there were.

------------------------------------------------------------
Problem 6 — Parse comma-separated prices
------------------------------------------------------------
Ask the user to enter prices like this:

100,101,99,105

Turn the input into a list of floats:
[100.0, 101.0, 99.0, 105.0]

Hints:
- split(",")
- loop through the parts
- convert each part to float

Challenge:
Calculate the simple return from the first price to the last price.
"""

# Write your solutions below.

