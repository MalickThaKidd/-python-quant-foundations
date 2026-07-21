import json


def save_account(account):
    with open("account.json", "w") as file:
        json.dump(account, file, indent=4)

def load_account():
    try:
        with open("account.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {
            "portfolio": {},
            "cash_balance": 0
        }

def portfolio_tool(account):
    portfolio = account["portfolio"]

    while True:
        try:
            ticker = input("\nWhat's the name of your share? ").strip().upper()

            shares = int(input("How many shares do you own? "))
            price_per_share = float(input("What is the price per share? "))

            if shares <= 0 or price_per_share <= 0:
                print("Shares and prices must be greater than zero.")
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

    try:
        cash_input = input("Enter cash to add, or press Enter to keep your current balance: ").strip()

        if cash_input != "":
            cash_to_add = float(cash_input)

            if cash_to_add < 0:
                raise ValueError

            account["cash_balance"] += cash_to_add

        cash_balance = account["cash_balance"]
        save_account(account)

    except ValueError:
        print("Please enter a valid cash amount.")
        return

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

def trade_pnl_tool(account):
    try:
        entry_price = float(input("Enter the entry price: "))
        exit_price = float(input("Enter the exit price: "))
        quantity = int(input("Enter the quantity bought: "))
        transaction_fee = float(input("Enter your transaction fees: "))

        if (entry_price <= 0 or exit_price <= 0 or quantity <= 0 or transaction_fee < 0):
            raise ValueError

    except ValueError:
        print("Please enter valid numbers.")
        return

    try:
        long_or_short = input("Is your trade long or short ? : ").strip().lower()

        if long_or_short == "short":
            gross_pnl = (entry_price - exit_price) * quantity

        elif long_or_short == "long":
            gross_pnl = (exit_price - entry_price) * quantity

        else:
            raise ValueError

    except ValueError:
        print("The answer can only be either long or short, Try Again !")
        return

    net_pnl = gross_pnl - transaction_fee

    initial_position_value = entry_price * quantity
    net_return_percentage = net_pnl / initial_position_value * 100

    if net_pnl > 0:
        trade_result = "PROFIT"

    elif net_pnl < 0:
        trade_result = "LOSS"

    else:
        trade_result = "FLAT"

    # Shared memory:
    # the realised trade result changes the account cash balance

    previous_cash_balance = account["cash_balance"]

    account["cash_balance"] += net_pnl
    save_account(account)

    new_cash_balance = account["cash_balance"]

    print(f"""
                                        ==================================================
                                                        TRADE REPORT
                                        ==================================================
                                        Trade type:           {long_or_short.upper()}
                                        Entry price:          {entry_price:,.2f}
                                        Exit price:           {exit_price:,.2f}
                                        Quantity:             {quantity}
                                        --------------------------------------------------
                                        Gross PnL:            {gross_pnl:,.2f}
                                        Transaction fees:     {transaction_fee:,.2f}
                                        Net PnL:              {net_pnl:,.2f}
                                        Net return:           {net_return_percentage:.2f}%
                                        --------------------------------------------------
                                        Previous cash:        {previous_cash_balance:,.2f}
                                        New cash balance:     {new_cash_balance:,.2f}
                                        --------------------------------------------------
                                        Trade result:         {trade_result}
                                        ==================================================
            """)


def var_tool(account):
    try:
        # 1 - Stored and sorted the returns of the week

        returns = input("Enter the weekly returns in (%) separated by commas: ")
        returns = returns.split(",")
        returns = [float(r.strip()) / 100 for r in returns]

        if len(returns) < 2:
            print("Please enter at least two returns.")
            return

        sorted_return = sorted(returns, reverse=True)

        # 2 - Counted the number of positive, negative and flat days

        positive_days = 0
        negative_days = 0
        flat_days = 0

        for r in sorted_return:
            if r > 0:
                positive_days += 1

            elif r < 0:
                negative_days += 1

            else:
                flat_days += 1

        # 3 - Assigned the second-worst return as the VaR rate

        portfolio = account["portfolio"]

        if len(portfolio) == 0:
            print("Please create your portfolio first.")
            return

        total_assets_value = 0

        for details in portfolio.values():
            total_assets_value += details["value"]

        cash_balance = account["cash_balance"]

        portfolio_value = total_assets_value + cash_balance

        var_rate = abs(sorted_return[-2])
        var = portfolio_value * var_rate

        # Printing the risk report

        print(f"""
                                        =========================================
                                                    WEEKLY RISK REPORT
                                        =========================================
                                        Best return:          {sorted_return[0] * 100:.2f}%
                                        Worst return:         {sorted_return[-1] * 100:.2f}%

                                        Positive days:        {positive_days}
                                        Negative days:        {negative_days}
                                        Flat days:            {flat_days}

                                        -----------------------------------------
                                        Portfolio value:      {portfolio_value:.2f}
                                        VaR rate:             {var_rate * 100:.2f}%
                                        Value at Risk:        {var:.2f}
                                        =========================================
                """)

    except ValueError:
        print("Please enter valid numbers.")
        return

def account_summary(account):
    portfolio = account["portfolio"]
    cash_balance = account["cash_balance"]

    if len(portfolio) == 0:
        print("Your portfolio is currently empty.")
        return

    total_assets_value = 0

    for details in portfolio.values():
        total_assets_value += details["value"]

    total_account_value = total_assets_value + cash_balance

    width = 78

    print("┌" + "─" * width + "┐")
    print(f"│{'ACCOUNT SUMMARY':^{width}}│")
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
    print(f"│{f'Cash balance: {cash_balance:,.2f}':<{width}}│")
    print(f"│{f'Total assets value: {total_assets_value:,.2f}':<{width}}│")
    print(f"│{f'Total account value: {total_account_value:,.2f}':<{width}}│")
    print("└" + "─" * width + "┘")

def main():
    account = load_account()
    
    while True:
        print("""
                                        ==================================================
                                                        FINANCE TOOLKIT
                                        ==================================================
                                        1. Portfolio valuation
                                        2. Trade PnL analysis
                                        3. Historical Value at Risk
                                        4. Account summary
                                        5. Exit
                                        ==================================================
            """)

        choice = input("Choose an option: ").strip()

        if choice == "1":
            portfolio_tool(account)

        elif choice == "2":
            trade_pnl_tool(account)

        elif choice == "3":
            var_tool(account)

        elif choice == "4":
            account_summary(account)

        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please choose an option between 1 and 5.")


main()
