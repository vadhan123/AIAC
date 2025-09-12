def sum_even_odd(evensum, oddsum):
    """
    Calculates the sum of even and odd numbers from a user-provided list.
    Args:
        evensum (int): Initial sum for even numbers.
        oddsum (int): Initial sum for odd numbers.
    Returns:
        tuple: A tuple containing the sum of even numbers and the sum of odd numbers.
    Prompts the user to enter a list of numbers separated by spaces, then computes and returns the sums of even and odd numbers separately.
    """
    user_input = input("Enter a list of numbers separated by spaces: ")
    number_list = list(map(int, user_input.split()))
    for num in number_list:
        if num % 2 == 0:
            evensum += num
        else:
            oddsum += num
    return evensum, oddsum

even_total, odd_total = sum_even_odd(0, 0)
print("Sum of even numbers:", even_total)
print("Sum of odd numbers:", odd_total)
