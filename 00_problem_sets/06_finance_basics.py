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

'''
------------------------------------------------------------
Problem 1 — Simple return from prices
------------------------------------------------------------
Ask the user for a start price and an end price.
Calculate the simple return:

(end_price - start_price) / start_price

Print the return.

Challenge:
Print it as a percentage.
'''

def problem_1():
    end_price = int(input("Enter the end price: "))
    start_price = int(input("Enter the start price: "))

    simple_return = (end_price - start_price) / start_price

    return f"The simple return value is: {simple_return * 100:.2f}%"




'''
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
'''

def problem_2():
    
    portfolio = {}

    while True:
        try:
            
            ticker = input("What's the name of your share? : ").upper()
            share = int(input("What's the number of shares that you own? : "))
            price_per_share = int(input("What's the price of the share? : "))
            cash_balance = float(input("Enter your cash balance: "))
            
            value_of_share = share * price_per_share
            
            portfolio[ticker] = {
                "Quantity of share": share,
                "Price per share": price_per_share,
                "What is the value of your share": value_of_share
            }
            
            total_assets_value = 0

            for ticker in portfolio:
                total_assets_value += portfolio[ticker]["What is the value of your share"]
            
            total_account_value = total_assets_value + cash_balance



        except EOFError:
            print()
            print("┌────────────────────────────────────────────────────────────┐")
            print("│                      Portfolio value                       │")
            print("├────────────────────────────────────────────────────────────┤")

            for ticker, details in portfolio.items():
                print(
                    f"│ {ticker:<8} "
                    f"Quantity: {details['Quantity of share']:<8} "
                    f"Price: {details['Price per share']:<10.2f} "
                    f"Value: {details['What is the value of your share']:<10.2f} │"
                )
            print("└────────────────────────────────────────────────────────────┘")
            print()
            print(f"Your Total Account Value is : {total_account_value} ")
            break

def problem_20():
    portfolio = {}

    while True:
        try:
            ticker = input("\nWhat's the name of your share? ").strip().upper()

            shares = int(input("How many shares do you own? "))
            price_per_share = float(input("What is the price per share? "))

            if shares < 0 or price_per_share < 0:
                print("Shares and prices cannot be negative.")
                continue

            value_of_shares = shares * price_per_share

            portfolio[ticker] = {
                "quantity": shares,
                "price": price_per_share,
                "value": value_of_shares,
            }

        except EOFError:
            print()
            break

        except ValueError:
            print("Please enter valid numbers.")

    cash_balance = float(input("Enter your cash balance: "))

    total_assets_value = 0

    for details in portfolio.values():
        total_assets_value += details["value"]

    total_account_value = total_assets_value + cash_balance

    width = 78

    print("┌" + "─" * width + "┐")
    print(f"│{'Portfolio value':^{width}}│")
    print("├" + "─" * width + "┤")

    for ticker, details in portfolio.items():
        row = (
            f"{ticker:<12}"
            f"Quantity: {details['quantity']:<10}"
            f"Price: {details['price']:<14.2f}"
            f"Value: {details['value']:.2f}"
        )

        print(f"│{row:<{width}}│")

    print("├" + "─" * width + "┤")

    print(f"│{f'Cash balance: {cash_balance:.2f}':<{width}}│")
    print(f"│{f'Total assets value: {total_assets_value:.2f}':<{width}}│")
    print(f"│{f'Total account value: {total_account_value:.2f}':<{width}}│")

    print("└" + "─" * width + "┘")






"""
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

def problem_6():
    prices = input("What's are the price of the week ? (seperate each price by ','): ")

    prices = prices.split(sep = ",")
    prices = [float(price.strip()) for price in prices]

    up_day = 0
    down_day = 0
    flat_day = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            up_day += 1
            
        elif prices[i] < prices[i-1]:
            down_day += 1
            
        else:
            flat_day += 1
        
    print(f"There are {up_day} up-day this week")
    print(f"There are {down_day} down-day this week")
    print(f"There are {flat_day} flat day this week")

problem_6()
