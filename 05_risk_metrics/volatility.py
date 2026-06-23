"""Volatility calculation."""

import numpy as np


def volatility(returns: np.ndarray, annualization_factor: int = 252) -> float:
    """Return annualized volatility from daily returns."""
    return returns.std(ddof=1) * np.sqrt(annualization_factor)


if __name__ == "__main__":
    returns = np.array([0.01, -0.02, 0.005, 0.012, -0.004])
    print(volatility(returns))
