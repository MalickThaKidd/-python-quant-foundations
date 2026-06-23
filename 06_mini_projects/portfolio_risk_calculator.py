"""Simple portfolio risk calculator."""

import numpy as np


def portfolio_return(weights: np.ndarray, expected_returns: np.ndarray) -> float:
    return float(weights @ expected_returns)


def portfolio_volatility(weights: np.ndarray, covariance_matrix: np.ndarray) -> float:
    return float(np.sqrt(weights.T @ covariance_matrix @ weights))


if __name__ == "__main__":
    weights = np.array([0.5, 0.3, 0.2])
    expected_returns = np.array([0.08, 0.06, 0.10])
    covariance_matrix = np.array([
        [0.04, 0.01, 0.02],
        [0.01, 0.03, 0.01],
        [0.02, 0.01, 0.05],
    ])

    print("Expected return:", portfolio_return(weights, expected_returns))
    print("Volatility:", portfolio_volatility(weights, covariance_matrix))
