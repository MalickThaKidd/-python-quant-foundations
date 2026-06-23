"""Historical Value at Risk."""

import numpy as np


def historical_var(returns: np.ndarray, confidence_level: float = 0.95) -> float:
    """Return historical VaR as a positive loss number."""
    percentile = (1 - confidence_level) * 100
    return -np.percentile(returns, percentile)


if __name__ == "__main__":
    rng = np.random.default_rng(seed=42)
    returns = rng.normal(0.001, 0.02, 10_000)
    print(historical_var(returns, 0.95))
