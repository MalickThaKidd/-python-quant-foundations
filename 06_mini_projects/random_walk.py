"""Simple random walk simulation."""

import numpy as np


def random_walk(start: float = 100, steps: int = 252, mu: float = 0.0, sigma: float = 1.0) -> np.ndarray:
    rng = np.random.default_rng(seed=42)
    shocks = rng.normal(mu, sigma, steps)
    return start + np.cumsum(shocks)


if __name__ == "__main__":
    path = random_walk()
    print(path[:10])
    print(path[-1])
