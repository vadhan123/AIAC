def factorial(n):
    """Calculate factorial using iteration"""
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    print("=== Factorial Calculator (Iterative Method) ===")
    print("This program calculates factorial using iteration")
    print("=" * 50)
    
    while True:
        try:
            number = int(input("\nEnter a number: "))
            result = factorial(number)
            
            if isinstance(result, str):
                print(f"Error: {result}")
            else:
                print(f"Factorial of {number} is: {result}")
                print(f"Calculation: {number}! = {result}")
            
            another = input("\nCalculate another factorial? (y/n): ")
            if another.lower() != 'y':
                print("Thank you for using the calculator!")
                break
                
        except ValueError:
            print("Error: Please enter a valid integer")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()

