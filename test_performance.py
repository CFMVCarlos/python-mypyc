import time
from functions.factorial import factorial
from functions.fibonacci import fibonacci
from functions.list_sum import list_sum
from compiled_functions.factorial import factorial as factorial_compiled
from compiled_functions.fibonacci import fibonacci as fibonacci_compiled
from compiled_functions.list_sum import list_sum as list_sum_compiled

# Define the input for benchmarking
N = 100_000


def benchmark_function(func, *args, **kwargs):
    """
    Benchmark a single function by measuring its execution time.

    Args:
        func (callable): The function to benchmark.
        *args: Positional arguments passed to the function.
        **kwargs: Keyword arguments passed to the function.

    Returns:
        tuple: The result of the function and the time taken to execute it in seconds.
    """
    start_time = time.perf_counter()  # Record the start time
    result = func(*args, **kwargs)  # Execute the function
    end_time = time.perf_counter()  # Record the end time
    execution_time = end_time - start_time  # Calculate the execution time
    return result, execution_time


def wrapper_benchmark_function(normal_func, compiled_func, argument=N):
    """
    Benchmark and compare the execution time of a normal Python function
    and its mypyc-compiled counterpart.

    Args:
        normal_func (callable): The normal Python function to benchmark.
        compiled_func (callable): The mypyc-compiled function to benchmark.
        argument: The argument to pass to the functions (default is N).

    Prints:
        Execution times and speedup factor.
    """
    # Benchmark the normal Python function
    print(f"Running normal {normal_func.__name__} Python function...")
    _, normal_time = benchmark_function(normal_func, argument)
    print(
        f"Normal {normal_func.__name__} Python execution time: {normal_time:.6f} seconds"
    )

    # Benchmark the mypyc-compiled function
    print(f"Running mypyc-compiled {compiled_func.__name__} function...")
    _, compiled_time = benchmark_function(compiled_func, argument)
    print(
        f"mypyc-compiled {compiled_func.__name__} execution time: {compiled_time:.6f} seconds"
    )

    # Calculate and print the performance comparison (speedup)
    speedup = normal_time / compiled_time
    print(f"Speedup with mypyc: {speedup:.2f}x\n")


def main():
    """
    Main function to run the benchmarking tests for factorial,
    fibonacci, and sum functions (both normal and compiled versions).
    """
    print(f"Benchmarking with input: {N}\n")

    # Run the benchmarking for factorial
    wrapper_benchmark_function(factorial, factorial_compiled)

    # Run the benchmarking for fibonacci
    wrapper_benchmark_function(fibonacci, fibonacci_compiled)

    # Run the benchmarking for sum with a list as input
    wrapper_benchmark_function(
        list_sum,
        list_sum_compiled,
        list(range(N)),  # Generate a list of N numbers for sum
    )


if __name__ == "__main__":
    main()  # Call the main function to start benchmarking
