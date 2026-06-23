"""Random numbers for simulations."""

import numpy as np


if __name__ == "__main__":
    rng = np.random.default_rng(seed=42)
    simulated_returns = rng.normal(loc=0.001, scale=0.02, size=10)
    print(simulated_returns)
    print("Mean:", simulated_returns.mean())
    print("Volatility:", simulated_returns.std())
