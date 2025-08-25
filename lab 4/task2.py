def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    num = int(input("Enter the integer: "))
    result = factorial(num)
    if result is None:
        print("Invalid input")
    else:
        print(f"The factorial of given number is : {result}")
