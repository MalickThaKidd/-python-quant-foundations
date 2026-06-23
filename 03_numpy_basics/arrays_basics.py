"""Basic NumPy arrays."""

import numpy as np


if __name__ == "__main__":
    prices = np.array([100, 102, 101, 105, 110])
    returns = prices[1:] / prices[:-1] - 1

    print("Prices:", prices)
    print("Returns:", returns)
    print("Average return:", returns.mean())
