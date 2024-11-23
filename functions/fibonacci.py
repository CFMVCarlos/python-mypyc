def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using dynamic programming (bottom-up approach).

    Args:
        n (int): The index in the Fibonacci sequence to compute.
                 Must be a non-negative integer.

    Returns:
        int: The nth Fibonacci number.

    Example:
        fibonacci(5) -> 5 (since the sequence is 0, 1, 1, 2, 3, 5, ...)
    """
    # Edge case handling: return 0 for n=0 and 1 for n=1 directly.
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize a list to store Fibonacci numbers, with base cases already set
    fib = [0] * (n + 1)  # List of size (n+1), all initialized to 0
    fib[1] = 1  # Base case: Fibonacci(1) = 1

    # Loop to calculate Fibonacci numbers from 2 up to n
    for i in range(2, n + 1):
        fib[i] = (
            fib[i - 1] + fib[i - 2]
        )  # Each number is the sum of the two preceding numbers

    # Return the nth Fibonacci number
    return fib[n]
