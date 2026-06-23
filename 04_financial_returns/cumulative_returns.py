"""Cumulative returns from periodic returns."""

import numpy as np


def cumulative_returns(returns: np.ndarray) -> np.ndarray:
    return np.cumprod(1 + returns) - 1


if __name__ == "__main__":
    returns = np.array([0.02, -0.01, 0.03])
    print(cumulative_returns(returns))
