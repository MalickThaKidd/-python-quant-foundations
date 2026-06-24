# 03 NumPy Basics

## Goal

Move from pure Python loops to vectorized numerical computing.

NumPy is central for Monte Carlo, matrices, simulations, portfolio risk and quantitative research.

## Why this matters for quant finance

In quant finance, you often work with arrays of prices, returns, simulations, portfolios and matrices.

Pure Python loops are useful for learning, but NumPy is faster and cleaner for numerical work.

You need NumPy for:

- simulations;
- returns;
- covariance matrices;
- portfolio volatility;
- Monte Carlo;
- linear algebra;
- PCA and risk models.

## Files in this section

```text
arrays_basics.py      First NumPy arrays and return calculation
vectorization.py      Calculate returns without manual loops
random_numbers.py     Generate random returns for simulations
```

## How to study each file

For every file:

1. Run the script.
2. Print each intermediate variable.
3. Rewrite the code in a practice file.
4. Replace the example values with your own.
5. Explain why NumPy is better than loops for this case.

Example:

```bash
python 03_numpy_basics/arrays_basics.py
```

Then create:

```text
03_numpy_basics/arrays_basics_practice.py
```

## Questions you must answer before moving on

For `arrays_basics.py`:

- What is a NumPy array?
- What does `prices[1:]` mean?
- What does `prices[:-1]` mean?
- Why does `prices[1:] / prices[:-1] - 1` calculate returns?

For `vectorization.py`:

- What is vectorization?
- Why is it cleaner than writing a loop?
- What would the same return calculation look like with a loop?

For `random_numbers.py`:

- What does `rng.normal()` generate?
- What do `loc`, `scale` and `size` mean?
- Why is randomness important for Monte Carlo?
- Why do we use a seed?

## Exercises

Add your own scripts:

```text
dot_product.py
vector_norm.py
matrix_multiplication.py
correlation_matrix.py
simulated_returns.py
```

Imperial Mathematics for Machine Learning connection:

```text
Dot product     -> portfolio weights and returns
Norm            -> vector length / risk magnitude
Matrix product  -> portfolio covariance calculations
Eigenvalues     -> PCA and factor models
```

## Mini challenge

Create a file:

```text
03_numpy_basics/simulated_returns_practice.py
```

It should:

1. simulate 252 daily returns;
2. calculate the mean daily return;
3. calculate daily volatility;
4. calculate annualized volatility;
5. print all results clearly.

## Completion checklist

You can move to folder 04 only when you can:

- create NumPy arrays;
- slice arrays with `[1:]` and `[:-1]`;
- calculate returns using vectorization;
- simulate random returns;
- explain what mean and standard deviation represent in finance.
