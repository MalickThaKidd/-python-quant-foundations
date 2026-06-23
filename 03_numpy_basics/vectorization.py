"""Vectorization example with returns."""

import numpy as np


def calculate_returns(prices: np.ndarray) -> np.ndarray:
    """Calculate simple returns from a price array."""
    return prices[1:] / prices[:-1] - 1


if __name__ == "__main__":
    prices = np.array([100, 101, 103, 99, 104])
    print(calculate_returns(prices))
