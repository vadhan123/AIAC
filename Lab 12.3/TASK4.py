def f(x):
    """
    Original function f(x) = 2x³ + 4x + 5
    """
    return 2 * x**3 + 4 * x + 5

def df(x):
    """
    Derivative of f(x): f'(x) = 6x² + 4
    """
    return 6 * x**2 + 4

def binary_search_minimum():
    """
    Find the value of x where f(x) is minimum using binary search
    Since f'(x) = 6x² + 4 is always increasing, there's only one minimum
    """
    left = -10  # Starting with a reasonable range
    right = 10
    epsilon = 0.0000001  # Desired precision
    
    while right - left > epsilon:
        x = (left + right) / 2
        derivative = df(x)
        
        if abs(derivative) < epsilon:
            return x
        elif derivative > 0:
            right = x
        else:
            left = x
    
    return (left + right) / 2

def check_points_around(x_min):
    """
    Check points around the minimum to verify it's indeed a minimum
    """
    delta = 0.1
    f_min = f(x_min)
    f_left = f(x_min - delta)
    f_right = f(x_min + delta)
    
    return f_left > f_min and f_right > f_min

if __name__ == "__main__":
    # Find the minimum point
    x_min = binary_search_minimum()
    
    print("\nResults:")
    print("-" * 50)
    print(f"The function f(x) = 2x³ + 4x + 5 has a minimum at:")
    print(f"x = {x_min:.6f}")
    print(f"f(x) = {f(x_min):.6f}")
    
    # Verify it's a minimum
    is_minimum = check_points_around(x_min)
    print(f"\nVerification:")
    print(f"Is this point a minimum? {is_minimum}")
    
    # Calculate second derivative at minimum point
    second_derivative = 12 * x_min
    print(f"Second derivative at this point: {second_derivative:.6f}")
    
    # Show some additional points for comparison
    print("\nValues around the minimum point:")
    print("-" * 50)
    for dx in [-0.1, 0, 0.1]:
        x = x_min + dx
        print(f"f({x:.6f}) = {f(x):.6f}")
