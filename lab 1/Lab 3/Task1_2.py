def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage
number = int(input("Enter a number: "))
print(f"Factorial of {number} is: {factorial_recursive(number)}")