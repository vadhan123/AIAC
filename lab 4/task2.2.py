def calculate_factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


if __name__ == "__main__":
    try:
        user_input = input("Enter the integer: ")
        number = int(user_input)
        
        factorial_result = calculate_factorial(number)
        
        if factorial_result is None:
            print("Invalid input")
        else:
            print(f"Factorial of given number is: {factorial_result}")
            
    except ValueError:
        print("Invalid input")
