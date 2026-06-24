# 01 Core Python

## Goal

Rebuild Python fundamentals before going deeper into NumPy, backtesting, Monte Carlo or portfolio risk.

This folder is the foundation. If this part is weak, the rest of the repo will feel confusing.

## What you should learn here

- how to write clean functions;
- how to use inputs and outputs;
- how to use lists;
- how to loop over values;
- how to raise basic errors;
- how to test a function with simple examples;
- how to connect basic Python to probability and finance.

## Files in this section

```text
expected_value.py       Expected value of a discrete random variable
variance.py             Variance of a discrete random variable
functions_practice.py   Simple finance-style function practice
```

## How to study each file

For every file:

1. Read the code.
2. Run the file.
3. Explain the formula in your own words.
4. Recreate the file with `_practice.py` at the end.
5. Change the examples.
6. Add one small improvement.

Example:

```bash
python 01_core_python/expected_value.py
```

Then create:

```text
01_core_python/expected_value_practice.py
```

## Questions you must answer before moving on

For `expected_value.py`:

- What are the outcomes?
- What are the probabilities?
- Why must probabilities sum to 1?
- Why do we multiply each outcome by its probability?
- How is this connected to trading payoffs?

For `variance.py`:

- What is the mean?
- Why do we subtract the mean from each outcome?
- Why do we square the difference?
- What does a high variance mean?
- How is variance connected to risk?

For `functions_practice.py`:

- What is a function input?
- What is a return value?
- Why do we check if `start_price <= 0`?
- Why is a return expressed as a percentage?

## Exercises

After understanding the files, add your own practice scripts:

```text
expected_value_practice.py
variance_practice.py
payoff_expected_value.py
simple_return_practice.py
```

Suggested payoff example:

```text
Scenario A: lose 10 with probability 0.30
Scenario B: gain 5 with probability 0.40
Scenario C: gain 20 with probability 0.30
```

Calculate the expected value and variance.

## Completion checklist

You can move to folder 02 only when you can:

- write an expected value function without looking;
- write a variance function without looking;
- explain the connection between variance and risk;
- create and run a Python file from the terminal;
- commit your practice files to GitHub.
