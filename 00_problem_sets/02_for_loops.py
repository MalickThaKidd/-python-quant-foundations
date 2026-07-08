"""
Problem Set 02 — for loops

Goal:
Practice repeating actions with for loops.
Do not use pandas or NumPy here.

------------------------------------------------------------
Problem 1 — Count trading days
------------------------------------------------------------
Use a for loop to print the trading days from Day 1 to Day 10.

Expected output:
Day 1
Day 2
...
Day 10

Hint:
- range() is useful.

------------------------------------------------------------
Problem 2 — Sum daily returns
------------------------------------------------------------
You have this list of daily returns:

returns = [0.01, -0.02, 0.015, 0.005, -0.01]

Use a for loop to calculate the total return by adding them one by one.
Print the total.

Challenge:
Also print whether the total return is positive, negative, or flat.

------------------------------------------------------------
Problem 3 — Count positive and negative days
------------------------------------------------------------
Using the same returns list:

returns = [0.01, -0.02, 0.015, 0.005, -0.01]

Count:
- how many days were positive
- how many days were negative
- how many days were exactly zero

Print the three counts.

Hint:
- Start counters at 0.
- Increase the right counter inside the loop.

------------------------------------------------------------
Problem 4 — Average return without sum()
------------------------------------------------------------
Given:

returns = [0.01, -0.02, 0.015, 0.005, -0.01]

Calculate the average return using a for loop.
Do not use sum().

Hints:
- First calculate total.
- Then divide by len(returns).

------------------------------------------------------------
Problem 5 — Find the best return
------------------------------------------------------------
Given:

returns = [0.01, -0.02, 0.015, 0.005, -0.01]

Use a for loop to find the best daily return.
Do not use max().

Hint:
- Start with the first value as the best value.
- Compare each value to the current best.

------------------------------------------------------------
Problem 6 — Simple compound growth
------------------------------------------------------------
Start with capital = 100_000.
You have daily returns:

returns = [0.01, -0.02, 0.015, 0.005, -0.01]

Update the capital each day:
capital = capital * (1 + daily_return)

Print the capital after each day.

Challenge:
Print the final profit or loss.
"""

# Write your solutions below.

