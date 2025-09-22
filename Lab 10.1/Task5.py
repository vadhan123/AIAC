import time

def generate_squares(limit):
    """
    Generate a list of squares from 1 to limit (exclusive).

    Parameters:
        limit (int): The upper bound (exclusive) for generating squares.

    Returns:
        list: List of squares from 1 to limit-1.
    """
    # Use a list comprehension for optimal performance
    return [n ** 2 for n in range(1, limit)]


if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    # Generate squares for numbers from 1 to 999,999
    squares = generate_squares(1_000_000)
    end_time = time.time()    # Record the end time
    print(len(squares))       # Output the number of squares generated
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")