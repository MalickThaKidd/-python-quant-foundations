# Finance Projects

This track moves from account-level calculations to portfolio risk and systematic strategy research. Each project should be written as a small professional application, not as a single calculation.

## 01 — Portfolio Account Engine

### Problem
Build a terminal application that lets a user create and analyse an investment account containing several assets and cash.

### Core requirements
- add, update, and remove positions;
- store ticker, quantity, purchase price, and current price;
- calculate market value, cost basis, unrealised profit/loss, return percentage, portfolio weight, total invested value, cash, and total account value;
- handle duplicate tickers intelligently;
- reject invalid quantities and prices;
- display a clean dynamic table;
- save and reload the portfolio from CSV or JSON;
- split the program into functions and write basic tests.

### Research questions
- What is the difference between cost basis, market value, realised P&L, and unrealised P&L?
- How should multiple purchases of the same asset affect the average purchase price?
- Why can portfolio weights change even when no trade occurs?

### Extensions
- transaction history;
- weighted-average purchase price;
- fees and taxes;
- currency conversion;
- performance relative to a benchmark.

### Deliverables
`README.md`, source code, sample data, tests, example terminal output, and a short explanation of the design choices.

---

## 02 — Portfolio Risk Laboratory

### Problem
Analyse the risk of a multi-asset portfolio using historical return data.

### Core requirements
- import a CSV of asset prices;
- calculate simple and log returns;
- align missing dates and explain the chosen policy;
- calculate mean return, volatility, covariance, and correlation;
- accept portfolio weights and verify that they sum to one;
- calculate expected portfolio return and volatility using matrix operations;
- calculate historical Value at Risk and maximum drawdown;
- compare individual-asset risk with portfolio risk;
- produce charts and a written interpretation.

### Research questions
- Why does covariance matter more than individual volatility for diversification?
- What assumptions are hidden inside annualisation?
- What does VaR fail to explain?

### Extensions
- rolling volatility and correlation;
- parametric VaR;
- expected shortfall;
- stress scenarios;
- risk contribution by asset.

### Deliverables
A reproducible analysis, documented formulas, charts, tests for core functions, and a one-page risk memo.

---

## 03 — Rule-Based Backtesting Engine

### Problem
Build a reusable backtester for a simple trading rule and determine whether the apparent performance survives realistic assumptions.

### Core requirements
- import dated prices;
- calculate returns without look-ahead bias;
- implement at least one rule, such as moving-average crossover or momentum;
- generate positions and strategy returns;
- include transaction costs;
- compare the strategy with buy-and-hold;
- calculate cumulative return, volatility, Sharpe ratio, drawdown, win rate, and turnover;
- separate training and testing periods;
- explain every major modelling decision.

### Research questions
- What is look-ahead bias?
- Why does overfitting make a strategy appear better than it is?
- Why can a high win rate coexist with poor profitability?

### Extensions
- parameter sensitivity grid;
- walk-forward testing;
- multiple assets;
- stop-loss rules;
- bootstrap confidence intervals.

### Deliverables
Source code, tests, result tables, equity-curve and drawdown charts, and a research note concluding whether the rule is credible.

## Completion standard
A finance project is complete when the calculations are correct, the assumptions are explicit, edge cases are handled, and the output can be interpreted by someone who did not write the code.
