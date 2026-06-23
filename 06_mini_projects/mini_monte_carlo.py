"""Mini Monte Carlo simulation for asset prices."""

import numpy as np


def simulate_terminal_prices(
    start_price: float,
    expected_return: float,
    volatility: float,
    days: int,
    n_simulations: int,
) -> np.ndarray:
    rng = np.random.default_rng(seed=42)
    daily_returns = rng.normal(
        loc=expected_return / days,
        scale=volatility / np.sqrt(days),
        size=(days, n_simulations),
    )
    price_paths = start_price * np.cumprod(1 + daily_returns, axis=0)
    return price_paths[-1]


if __name__ == "__main__":
    terminal_prices = simulate_terminal_prices(100, 0.08, 0.20, 252, 10_000)
    print("Mean terminal price:", terminal_prices.mean())
    print("5th percentile:", np.percentile(terminal_prices, 5))
