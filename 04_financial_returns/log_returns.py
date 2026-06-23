"""Log returns."""

import numpy as np


def log_returns(prices: np.ndarray) -> np.ndarray:
    return np.log(prices[1:] / prices[:-1])


if __name__ == "__main__":
    prices = np.array([100, 105, 102, 108])
    print(log_returns(prices))
