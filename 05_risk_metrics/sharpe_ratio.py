"""Sharpe ratio calculation."""

import numpy as np


def sharpe_ratio(
    returns: np.ndarray,
    risk_free_rate: float = 0.0,
    annualization_factor: int = 252,
) -> float:
    """Return annualized Sharpe ratio."""
    excess_returns = returns - risk_free_rate / annualization_factor
    return excess_returns.mean() / excess_returns.std(ddof=1) * np.sqrt(annualization_factor)


if __name__ == "__main__":
    returns = np.array([0.01, -0.02, 0.005, 0.012, -0.004])
    print(sharpe_ratio(returns))
