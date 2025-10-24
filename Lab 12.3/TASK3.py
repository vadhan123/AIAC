def find_optimal_production():
    """
    Find the optimal production quantities for chocolates A and B
    using a systematic approach to maximize profit.
    
    Constraints:
    - Milk: 1A + 1B ≤ 5
    - Choco: 3A + 2B ≤ 12
    - A, B ≥ 0
    
    Profit = 6A + 5B (maximize)
    """
    max_profit = 0
    optimal_A = 0
    optimal_B = 0
    
    # Try all possible combinations within constraints
    # Since we know A and B can't be negative and must be less than or equal to 5 (milk constraint)
    for a in range(6):  # 0 to 5
        for b in range(6):  # 0 to 5
            # Check milk constraint
            if a + b > 5:
                continue
                
            # Check choco constraint
            if 3*a + 2*b > 12:
                continue
                
            # Calculate profit for this combination
            profit = 6*a + 5*b
            
            # Update if this profit is better than previous max
            if profit > max_profit:
                max_profit = profit
                optimal_A = a
                optimal_B = b
    
    return optimal_A, optimal_B, max_profit

def print_solution(A, B, profit):
    """Print the solution in a formatted way"""
    print("\nOptimal Production Plan:")
    print("-" * 30)
    print(f"Chocolate A: {A} units")
    print(f"Chocolate B: {B} units")
    print(f"Maximum Profit: Rs {profit}")
    
    # Print resource utilization
    milk_used = A + B
    choco_used = 3*A + 2*B
    
    print("\nResource Utilization:")
    print("-" * 30)
    print(f"Milk: {milk_used}/5 units")
    print(f"Choco: {choco_used}/12 units")
    
    # Verify constraints
    print("\nConstraints Verification:")
    print("-" * 30)
    print(f"Milk Constraint (≤ 5): {milk_used} ✓")
    print(f"Choco Constraint (≤ 12): {choco_used} ✓")

if __name__ == "__main__":
    # Find optimal solution
    optimal_A, optimal_B, max_profit = find_optimal_production()
    
    # Print results
    print_solution(optimal_A, optimal_B, max_profit)
