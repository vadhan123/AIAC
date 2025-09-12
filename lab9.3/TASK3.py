def add(a, b):
    """
    Return the sum of a and b.
    """
    return a + b  # Add the two numbers
def subtract(a, b):
    """
    Return the difference of a and b.
    """
    return a - b  # Subtract b from a
def multiply(a, b):
    """
    Return the product of a and b.
    """
    return a * b  # Multiply the two numbers
def divide(a, b):
    """
    Return the division of a by b. Returns an error message if b is zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero"  # Handle division by zero
    return a / b  # Divide a by b
x = float(input("Enter first number: "))  # Get first number from user
y = float(input("Enter second number: "))  # Get second number from user

# Print the results of arithmetic operations
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))
