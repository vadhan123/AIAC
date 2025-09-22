def grade(score):
    """
    Return the letter grade for a given score.

    Parameters:
        score (int or float): The numeric score to grade.

    Returns:
        str: The letter grade (A, B, C, D, F).
    """
    # Check for grade A
    if score >= 90:
        return "A"
    # Check for grade B
    elif score >= 80:
        return "B"
    # Check for grade C
    elif score >= 70:
        return "C"
    # Check for grade D
    elif score >= 60:
        return "D"
    # If none of the above, return F
    else:
        return "F"

# Example usage
if __name__ == "__main__":
    scores = [95, 85, 75, 65, 55, 90, 80, 70, 60, 0, 100]
    for s in scores:
        print(f"Score: {s} => Grade: {grade(s)}")
