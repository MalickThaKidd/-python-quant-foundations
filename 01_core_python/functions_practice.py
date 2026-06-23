"""Basic functions practice for quant-style calculations."""


def simple_return(start_price: float, end_price: float) -> float:
    """Return the simple return between two prices."""
    if start_price <= 0:
        raise ValueError("start_price must be positive")
    return (end_price - start_price) / start_price


def percentage(value: float) -> str:
    """Format a decimal value as a percentage string."""
    return f"{value:.2%}"


if __name__ == "__main__":
    result = simple_return(100, 110)
    print(percentage(result))
