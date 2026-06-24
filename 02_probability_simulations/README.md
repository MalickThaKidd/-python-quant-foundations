# 02 Probability Simulations

## Goal

Use Python to build intuition for probability, randomness and uncertainty.

Key idea for quant trading: do not think only in single outcomes. Think in distributions of outcomes.

## Why this matters for quant trading

Markets are uncertain. A trader or quant researcher does not only ask:

```text
What will happen?
```

A better question is:

```text
What are the possible outcomes, how likely are they, and what is the risk?
```

Simulations help you develop this mindset.

## Files in this section

```text
coin_flip_simulation.py     Simulate coin flips and estimate probability
 dice_simulation.py          Simulate dice rolls and estimate average outcome
law_of_large_numbers.py     See how averages converge with many trials
```

## How to study each file

For every file:

1. Run the script.
2. Change the number of simulations.
3. Observe how the result changes.
4. Rewrite the simulation in a `_practice.py` file.
5. Add one new experiment.

Example:

```bash
python 02_probability_simulations/coin_flip_simulation.py
```

Then create:

```text
02_probability_simulations/coin_flip_practice.py
```

## Questions you must answer before moving on

For `coin_flip_simulation.py`:

- Why does the result change when the number of flips is small?
- Why does it get closer to 0.5 when the number of flips is large?
- What does this teach you about randomness?

For `dice_simulation.py`:

- What is the theoretical expected value of a fair die?
- Why is it 3.5 even though 3.5 is not a possible roll?
- What happens when you increase the number of rolls?

For `law_of_large_numbers.py`:

- What is the law of large numbers?
- Why does the running average stabilize?
- Why is this important for simulations and Monte Carlo?

## Exercises

Add your own scripts:

```text
biased_coin_simulation.py
multiple_dice_simulation.py
lottery_simulation.py
trading_payoff_simulation.py
```

Suggested trading payoff simulation:

```text
Probability of winning trade: 55%
Average gain when winning: +2%
Average loss when losing: -1.5%
Simulate 1,000 trades.
```

Questions:

- What is the average return?
- What is the worst sequence of losses?
- Does the edge survive randomness?

## Completion checklist

You can move to folder 03 only when you can:

- simulate coin flips without looking;
- simulate dice rolls without looking;
- explain the law of large numbers;
- understand why more simulations usually produce more stable estimates;
- create your own simple random experiment.
