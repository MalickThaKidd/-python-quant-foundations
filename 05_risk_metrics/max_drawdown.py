"""Maximum drawdown calculation."""

import numpy as np


def max_drawdown(returns: np.ndarray) -> float:
    """Return the maximum drawdown from a return series."""
    wealth = np.cumprod(1 + returns)
    running_max = np.maximum.accumulate(wealth)
    drawdowns = wealth / running_max - 1
    return drawdowns.min()


if __name__ == "__main__":
    returns = np.array([0.05, -0.02, -0.10, 0.03, 0.04])
    print(max_drawdown(returns))
