def sum_even_odd(numbers):
    """Return a tuple of (even_sum, odd_sum) from the given iterable of integers."""
    even_sum = 0
    odd_sum = 0
    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    return even_sum, odd_sum


if __name__ == "__main__":
    try:
        user_input = input("Enter integers separated by spaces (or commas): ").strip()
        # Support both spaces and commas as separators
        tokens = user_input.replace(",", " ").split() if user_input else []
        numbers = [int(token) for token in tokens]

        even_sum, odd_sum = sum_even_odd(numbers)
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces or commas.")


