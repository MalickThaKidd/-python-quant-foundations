"""Simulate dice rolls and estimate the average outcome."""

import random


def roll_die() -> int:
    return random.randint(1, 6)


def simulate_dice_average(n_rolls: int) -> float:
    total = 0
    for _ in range(n_rolls):
        total += roll_die()
    return total / n_rolls


if __name__ == "__main__":
    for n in [10, 100, 1_000, 10_000]:
        print(n, simulate_dice_average(n))
