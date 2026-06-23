"""Simulate coin flips using pure Python."""

import random


def simulate_coin_flips(n_flips: int) -> float:
    """Return the proportion of heads after n_flips."""
    heads = 0
    for _ in range(n_flips):
        if random.choice(["H", "T"]) == "H":
            heads += 1
    return heads / n_flips


if __name__ == "__main__":
    for n in [10, 100, 1_000, 10_000]:
        print(n, simulate_coin_flips(n))
