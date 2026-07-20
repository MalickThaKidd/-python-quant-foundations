# Python Quant Foundations

A project-based Python laboratory for finance, mathematics, economics, and energy & commodities.

The repository is no longer organised as a collection of disconnected micro-exercises. The `00_cheatsheets/` and `00_problem_sets/` folders remain the technical training area. Everything after them is organised around complete problems that require modelling, research, clean Python, interpretation, and communication.

## Repository structure

```text
00_cheatsheets/              Syntax and concepts to consult quickly
00_problem_sets/             Short exercises for Python fundamentals
01_finance/                  Portfolio, pricing, risk, and backtesting projects
02_mathematics/              Numerical methods, probability, calculus, and linear algebra
03_economics/                Inflation, growth, debt, exchange rates, and policy analysis
04_energy_commodities/       Oil, gas, LNG, power markets, and commodity risk
```

## What counts as a complete problem?

Every project should contain:

1. a real question;
2. assumptions and definitions;
3. a mathematical model;
4. a Python implementation;
5. input validation and tests;
6. tables or charts when useful;
7. interpretation of the results;
8. limitations and possible extensions;
9. a short written conclusion.

The objective is not only to obtain a number. It is to understand what the number means, when the model works, and when it can fail.

## Working method

For each project:

```text
Research -> Plan -> Build -> Test -> Interpret -> Improve -> Document
```

Recommended workflow:

1. Read the project brief completely.
2. Research any unfamiliar finance, mathematical, economic, or energy concepts.
3. Write the formulas and assumptions before coding.
4. Divide the project into small functions.
5. Start with a simple working version.
6. Add validation, tests, and edge cases.
7. Explain the results in your own words.
8. Commit meaningful milestones rather than one huge final commit.

## Difficulty levels

- **Level 1 — Builder:** clean functions, loops, dictionaries, files, and basic calculations.
- **Level 2 — Analyst:** NumPy/pandas, statistical reasoning, charts, tests, and interpretation.
- **Level 3 — Researcher:** external data, model comparison, sensitivity analysis, and a written report.

A project is complete only when the core requirements are satisfied. The extensions are optional and can be revisited later.

## Suggested order

```text
01_finance/01_portfolio_account_engine
02_mathematics/01_monte_carlo_probability_lab
03_economics/01_inflation_and_purchasing_power
04_energy_commodities/01_oil_revenue_scenario_engine
```

Then continue with the remaining projects in each group according to your interests.

## Long-term target

By completing the repository, you should be able to:

- translate a real problem into variables, assumptions, and formulas;
- build reusable Python functions rather than one-off scripts;
- work with financial and economic data;
- simulate uncertainty and analyse risk;
- explain quantitative results clearly;
- produce portfolio-ready projects aligned with quantitative finance, macroeconomics, and commodities.

The repo should function as a serious preparation ground for larger work such as a portfolio risk engine, Monte Carlo option pricing, sovereign-risk analysis, commodity scenario models, and a simple systematic trading research platform.
