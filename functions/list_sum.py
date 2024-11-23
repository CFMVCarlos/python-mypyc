from mypy_extensions import i64  # Importing `i64` for explicitly typed integers


# Function to calculate the sum of a list of 64-bit integers
def list_sum(numbers: list[i64]) -> i64:
    """
    Computes the sum of a list of 64-bit integers.

    Args:
        l (list[i64]): A list containing 64-bit integers.

    Returns:
        i64: The sum of all integers in the list.
    """
    # Initialize the sum as a 64-bit integer
    sum: i64 = 0

    # Iterate through each element in the list and add it to the sum
    for number in numbers:
        sum += number

    # Return the total sum as a 64-bit integer
    return sum
