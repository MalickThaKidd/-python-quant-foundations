# 04 Financial Returns

## Goal

Understand how financial returns are calculated and used.

Returns are the starting point for volatility, Sharpe ratio, drawdown, VaR, backtesting and portfolio analysis.

## Why this matters for quant trading

A price chart alone is not enough. Quant research usually works with returns because returns allow you to compare assets and measure risk/performance.

You need returns to calculate:

- average performance;
- volatility;
- cumulative performance;
- drawdown;
- Sharpe ratio;
- Value at Risk;
- backtest PnL.

## Files in this section

```text
simple_returns.py       Standard percentage returns
log_returns.py          Logarithmic returns
cumulative_returns.py   Growth of capital over time
```

## How to study each file

For every file:

1. Run the script.
2. Change the price series.
3. Calculate the first return by hand.
4. Compare your manual result with Python.
5. Create a practice file and rewrite the logic.

Example:

```bash
python 04_financial_returns/simple_returns.py
```

Then create:

```text
04_financial_returns/simple_returns_practice.py
```

## Questions you must answer before moving on

For `simple_returns.py`:

- Why do we divide by the previous price?
- What does a return of `0.05` mean?
- What does a return of `-0.03` mean?

For `log_returns.py`:

- What is the difference between simple returns and log returns?
- Why are log returns often used in quantitative finance?
- When are simple returns easier to understand?

For `cumulative_returns.py`:

- What does `np.cumprod(1 + returns)` do?
- Why do we add 1 before taking the cumulative product?
- How does this represent the growth of capital?

## Exercises

Add your own scripts:

```text
returns_from_prices_practice.py
compare_simple_and_log_returns.py
wealth_index.py
monthly_returns.py
```

Suggested exercise:

```text
Initial capital: 1,000,000 FCFA
Returns: +2%, -1%, +3%, -4%, +5%
```

Calculate:

- cumulative return;
- final capital;
- best period;
- worst period.

## Mini challenge

Create a file:

```text
04_financial_returns/wealth_growth_practice.py
```

It should:

1. take a list of returns;
2. calculate the wealth path;
3. print the final wealth;
4. print the total return.

## Completion checklist

You can move to folder 05 only when you can:

- calculate simple returns from prices;
- calculate log returns from prices;
- explain the difference between simple and log returns;
- calculate cumulative returns;
- explain how returns become a wealth curve.
