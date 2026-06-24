# Python Quant Foundations

Python foundations for quantitative finance, probability simulations, risk metrics and trading research.

This repository is a structured learning lab. The goal is not to collect random notebooks, but to rebuild Python fundamentals while applying each concept to finance, probability, risk and trading research.

## Main objective

Move from basic data analysis with pandas to clean Python programming for quantitative finance:

- core Python fundamentals;
- probability simulations;
- NumPy and vectorization;
- financial returns;
- risk metrics;
- mini quantitative finance projects.

## How to use this repo

This repo should be used like a personal Python gym.

Do not try to finish everything in one day. The correct rhythm is:

```text
1 day = 1 Python file
```

For each file, follow this process:

1. Read the file slowly.
2. Run it in the terminal.
3. Explain in your own words what it calculates.
4. Recreate the same file without looking.
5. Change the inputs.
6. Add one small improvement.
7. Commit your work to GitHub.

The goal is not to copy. The goal is to understand, rebuild and modify.

## Daily routine

Recommended daily session: 45 minutes.

```text
10 min  - read and understand the file
20 min  - rewrite it from scratch in a practice file
10 min  - modify or improve it
5 min   - commit and push
```

Example:

```bash
python 01_core_python/expected_value.py
```

Then create:

```text
01_core_python/expected_value_practice.py
```

Rewrite the logic yourself, test it, then commit:

```bash
git add .
git commit -m "Practice expected value"
git push
```

## Repository structure

```text
01_core_python/              Python fundamentals
02_probability_simulations/  Randomness and probability intuition
03_numpy_basics/             Vectorized numerical computing
04_financial_returns/        Simple/log/cumulative returns
05_risk_metrics/             Volatility, Sharpe, drawdown, VaR
06_mini_projects/            Small quant finance projects
```

## Recommended order

Do not skip folders.

```text
01_core_python
-> 02_probability_simulations
-> 03_numpy_basics
-> 04_financial_returns
-> 05_risk_metrics
-> 06_mini_projects
```

Each folder prepares the next one.

## How this connects to CS50P

CS50P gives the general Python foundations.

This repo converts those foundations into finance and quant applications.

| CS50P topic | Repo application |
|---|---|
| Functions | expected value, variance, simple returns |
| Loops | dice and coin simulations |
| Exceptions | input validation and ValueError checks |
| Libraries | random, statistics, NumPy |
| File I/O | later: reading price data |
| Testing | later: testing finance functions |
| OOP | later: Asset and Portfolio classes |

## How this connects to Imperial Mathematics for Machine Learning

Every mathematical concept should become code.

| Imperial concept | File idea |
|---|---|
| Dot product | `03_numpy_basics/dot_product.py` |
| Norm | `03_numpy_basics/vector_norm.py` |
| Projection | `03_numpy_basics/vector_projection.py` |
| Matrix multiplication | `03_numpy_basics/matrix_multiplication.py` |
| Eigenvalues | `03_numpy_basics/eigenvalues_basics.py` |
| PCA | `06_mini_projects/pca_returns.py` |

## Learning rules

1. Do not just run the files. Rebuild them.
2. Do not move to the next file if you cannot explain the current one.
3. Prefer simple code that you understand over complex code copied from the internet.
4. Use functions, not only scripts.
5. Add comments only when they clarify the logic.
6. Commit small progress often.

## What progress looks like

After one month, the target is:

- all files in folders 01, 02 and 03 understood;
- 10 to 15 practice files added;
- 15+ commits;
- ability to write basic simulations without help;
- stronger NumPy understanding.

## Long-term direction

This repo is the foundation for later projects such as:

- Portfolio Risk Engine;
- Monte Carlo Option Pricing;
- Simple Backtesting Engine;
- Market Microstructure Simulator;
- Yakaar-Teranga Monte Carlo Simulation.
