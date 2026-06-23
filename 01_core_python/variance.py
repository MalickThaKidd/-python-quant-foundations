"""Variance from outcomes and probabilities."""


def expected_value(outcomes: list[float], probabilities: list[float]) -> float:
    return sum(x * p for x, p in zip(outcomes, probabilities))


def variance(outcomes: list[float], probabilities: list[float]) -> float:
    """Return the variance of a discrete random variable."""
    if len(outcomes) != len(probabilities):
        raise ValueError("outcomes and probabilities must have the same length")
    if abs(sum(probabilities) - 1.0) > 1e-9:
        raise ValueError("probabilities must sum to 1")

    mean = expected_value(outcomes, probabilities)
    return sum(((x - mean) ** 2) * p for x, p in zip(outcomes, probabilities))


if __name__ == "__main__":
    outcomes = [1, 2, 3, 4, 5, 6]
    probabilities = [1 / 6] * 6
    print(variance(outcomes, probabilities))
