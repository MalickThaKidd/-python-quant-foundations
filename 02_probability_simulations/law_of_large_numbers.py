"""Visualize the law of large numbers with dice rolls."""

import random


def running_average_dice(n_rolls: int) -> list[float]:
    averages = []
    total = 0
    for i in range(1, n_rolls + 1):
        total += random.randint(1, 6)
        averages.append(total / i)
    return averages


if __name__ == "__main__":
    averages = running_average_dice(10_000)
    print("First average:", averages[0])
    print("Final average:", averages[-1])
    print("Theoretical expected value:", 3.5)
