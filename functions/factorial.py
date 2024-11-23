from mypy_extensions import i64  # Importing `i64` for explicitly typed integers


def factorial(n: i64) -> i64:
    """
    Calculate the factorial of a given non-negative integer.

    Args:
        n (i64): The number for which to calculate the factorial.
                 Must be a non-negative integer.

    Returns:
        i64: The factorial of the input number, defined as:
             n! = n * (n-1) * (n-2) * ... * 1, where 0! = 1.

    Raises:
        ValueError: If n is a negative integer.

    Example:
        compute_factorial(5) -> 120 (since 5! = 5 * 4 * 3 * 2 * 1)
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    # Initialize result to 1 (since 0! = 1 and 1! = 1)
    result = 1

    # Compute factorial iteratively
    for i in range(1, n + 1):
        result *= i

    return result
