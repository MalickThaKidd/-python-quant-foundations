# 05 Risk Metrics

## Goal

Code the basic metrics used to evaluate risk and performance.

A quant trader must care about risk first: volatility, drawdown, losses, tails and stability.

## Why this matters for quant trading

A strategy is not good just because it makes money in a backtest.

You must ask:

- How volatile is it?
- How bad can the losses get?
- What is the worst drawdown?
- Does the return compensate the risk?
- What happens in the left tail?

Risk metrics help answer these questions.

## Files in this section

```text
volatility.py        Annualized volatility from returns
sharpe_ratio.py      Risk-adjusted performance
max_drawdown.py      Worst peak-to-trough loss
value_at_risk.py     Historical Value at Risk
```

## How to study each file

For every file:

1. Run the script.
2. Change the return values.
3. Print intermediate variables.
4. Rewrite the metric in a `_practice.py` file.
5. Explain what the metric means in plain English.

Example:

```bash
python 05_risk_metrics/volatility.py
```

Then create:

```text
05_risk_metrics/volatility_practice.py
```

## Questions you must answer before moving on

For `volatility.py`:

- What does standard deviation measure?
- Why do we annualize volatility?
- Why do we multiply by `sqrt(252)` for daily returns?

For `sharpe_ratio.py`:

- What is excess return?
- Why do we divide by volatility?
- Why can a high return still be bad if risk is too high?

For `max_drawdown.py`:

- What is a wealth curve?
- What is a running maximum?
- Why is drawdown psychologically and financially important?

For `value_at_risk.py`:

- What does 95% VaR mean?
- Why is VaR a loss number?
- What is the weakness of VaR?
- Why should we later learn Expected Shortfall?

## Exercises

Add your own scripts:

```text
expected_shortfall.py
risk_report.py
compare_two_strategies.py
rolling_volatility.py
```

Suggested exercise:

Compare two strategies:

```text
Strategy A: higher average return, higher volatility
Strategy B: lower average return, lower volatility
```

Calculate:

- average return;
- volatility;
- Sharpe ratio;
- max drawdown;
- VaR.

Then answer:

```text
Which strategy would you prefer and why?
```

## Mini challenge

Create a file:

```text
05_risk_metrics/basic_risk_report.py
```

It should take a NumPy array of returns and print:

- mean return;
- volatility;
- Sharpe ratio;
- max drawdown;
- 95% VaR.

## Completion checklist

You can move to folder 06 only when you can:

- calculate volatility;
- explain annualization;
- calculate Sharpe ratio;
- calculate max drawdown;
- calculate historical VaR;
- explain why risk matters more than raw return.
