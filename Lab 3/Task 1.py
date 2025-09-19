def factorial(n):
    """Calculate factorial of a non-negative integer"""
    try:
        n = int(n)
        if n < 0:
            return "Error: Factorial is not defined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
    except ValueError:
        return "Error: Please enter a valid integer"
def main():
    print("Factorial Calculator")
    print("=" * 20)
    
    while True:
        user_input = input("\nEnter a number (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        result = factorial(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()