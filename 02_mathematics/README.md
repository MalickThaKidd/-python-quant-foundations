# Mathematics Projects

This track turns mathematical ideas into experiments, algorithms, and explanations. The code must show not only the result, but why the method works and where numerical errors can appear.

## 01 — Monte Carlo Probability Laboratory

### Problem
Create a simulation laboratory that compares theoretical probabilities with Monte Carlo estimates.

### Core requirements
- support at least three experiments: coins, dice, and a custom financial event;
- let the user choose the number of simulations;
- calculate theoretical probability when possible;
- calculate estimated probability and absolute error;
- repeat the experiment for increasing simulation sizes;
- show convergence in a table or chart;
- use a reproducible random seed;
- validate inputs and write tests for deterministic helper functions.

### Research questions
- What is the law of large numbers?
- Why does a simulation estimate change from one run to another?
- How quickly should Monte Carlo error decrease as simulations increase?

### Extensions
- confidence intervals;
- variance reduction;
- biased coins or dependent events;
- estimate pi through simulation;
- simulate default losses.

### Deliverables
Reusable simulation functions, charts, a comparison of theory and experiment, and a short explanation of convergence.

---

## 02 — Linear Algebra Portfolio Explorer

### Problem
Use vectors and matrices to analyse returns, covariance, projections, and principal directions in financial data.

### Core requirements
- represent asset returns as vectors;
- implement dot product, norm, cosine similarity, and projection first with plain Python, then with NumPy;
- build and interpret a covariance matrix;
- verify matrix dimensions before multiplication;
- calculate eigenvalues and eigenvectors;
- explain what the largest eigenvector may represent in a correlated market;
- reconstruct a matrix through diagonalisation when possible;
- compare manual and NumPy results.

### Research questions
- Why is a portfolio return a dot product?
- What does orthogonality mean in a financial context?
- Why can one principal component explain much of market movement?

### Extensions
- Gram-Schmidt orthogonalisation;
- PCA on a return dataset;
- factor exposure projection;
- condition numbers and numerical stability.

### Deliverables
A mathematical note, tested functions, NumPy verification, and visualisations of vectors or principal components.

---

## 03 — Numerical Optimisation and Root-Finding Toolkit

### Problem
Build a toolkit for solving mathematical equations that do not have convenient closed-form solutions.

### Core requirements
- implement bisection and Newton-Raphson methods;
- define stopping criteria and maximum iterations;
- report convergence history;
- handle invalid intervals and zero derivatives;
- compare accuracy and speed;
- use the methods for at least two applications, such as internal rate of return and implied volatility or bond yield;
- compare results with a trusted library when available.

### Research questions
- What conditions guarantee that bisection works?
- Why can Newton-Raphson diverge?
- What is the difference between mathematical convergence and floating-point accuracy?

### Extensions
- secant method;
- gradient descent for a two-variable function;
- sensitivity to starting values;
- visualise iteration paths.

### Deliverables
A reusable solver module, tests, convergence tables, application examples, and a comparison of methods.

## Completion standard
A mathematics project is complete when the formulas are stated, the algorithm is explained, manual reasoning is connected to code, and accuracy or convergence is measured rather than assumed.
