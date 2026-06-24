# 06 Mini Projects

## Goal

Combine fundamentals into small, serious projects.

These scripts are the bridge between learning Python and building full quant finance projects.

## Why this matters

A certificate shows that you studied.

A project shows that you can build.

This folder is where you start turning Python, probability, NumPy, returns and risk metrics into small projects that look closer to quantitative finance work.

## Files in this section

```text
random_walk.py                 Simulate a simple random path
mini_monte_carlo.py            Simulate terminal prices with Monte Carlo
portfolio_risk_calculator.py   Calculate portfolio return and volatility
```

## How to study each file

For every project:

1. Run the file.
2. Identify the inputs.
3. Identify the outputs.
4. Explain the financial intuition.
5. Rewrite the project in a practice file.
6. Add one improvement.
7. Write a short note in the file explaining what you learned.

Example:

```bash
python 06_mini_projects/mini_monte_carlo.py
```

Then create:

```text
06_mini_projects/mini_monte_carlo_practice.py
```

## Questions you must answer before moving on

For `random_walk.py`:

- What is a random walk?
- Why can random walks be useful for market intuition?
- What are the limits of a simple random walk?

For `mini_monte_carlo.py`:

- What is Monte Carlo simulation?
- Why do we simulate many possible paths?
- What does the 5th percentile represent?
- Why is downside risk important?

For `portfolio_risk_calculator.py`:

- What are portfolio weights?
- What is a covariance matrix?
- Why does correlation matter for portfolio risk?
- Why is portfolio volatility not just the weighted average of individual volatilities?

## Exercises

Add your own scripts:

```text
monte_carlo_with_plot.py
portfolio_risk_report.py
two_asset_portfolio.py
scenario_analysis.py
```

Suggested scenario analysis:

```text
Asset A expected return: 8%
Asset B expected return: 5%
Asset C expected return: 12%
Try different portfolio weights and compare risk/return.
```

## Mini challenge

Create a file:

```text
06_mini_projects/portfolio_risk_report.py
```

It should:

1. define expected returns;
2. define a covariance matrix;
3. test at least three different portfolios;
4. calculate return and volatility for each;
5. print the best risk-return balance in your own words.

## Long-term upgrades

After mastering this folder, build larger projects:

```text
Portfolio Risk Engine
Monte Carlo Option Pricing
Simple Backtesting Engine
Market Microstructure Simulator
Yakaar-Teranga Monte Carlo Simulation
```

## Completion checklist

You are done with this section when you can:

- explain Monte Carlo in simple words;
- simulate terminal prices;
- calculate portfolio expected return;
- calculate portfolio volatility using a covariance matrix;
- modify a mini project without breaking it;
- write a short explanation of your results.
