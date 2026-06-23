"""Simple returns."""

import numpy as np


def simple_returns(prices: np.ndarray) -> np.ndarray:
    return prices[1:] / prices[:-1] - 1


if __name__ == "__main__":
    prices = np.array([100, 105, 102, 108])
    print(simple_returns(prices))
