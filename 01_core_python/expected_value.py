"""Expected value from outcomes and probabilities."""


def expected_value(outcomes: list[float], probabilities: list[float]) -> float:
    """Return the expected value of a discrete random variable."""
    if len(outcomes) != len(probabilities):
        raise ValueError("outcomes and probabilities must have the same length")
    if abs(sum(probabilities) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")

    return sum(x * p for x, p in zip(outcomes, probabilities))


if __name__ == "__main__":
    dice_outcomes = [1, 2, 3, 4, 5, 6]
    dice_probabilities = [1 / 6] * 6
    print(expected_value(dice_outcomes, dice_probabilities))
