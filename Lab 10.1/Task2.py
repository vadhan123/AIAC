
def calculate_rectangle_area(length, breadth):
    """
    Calculate the area of a rectangle.

    Parameters:
        length (float or int): The length of the rectangle. Must be positive.
        breadth (float or int): The breadth of the rectangle. Must be positive.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If length or breadth is not positive.
    """
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive numbers.")
    return length * breadth


if __name__ == "__main__":
    try:
        # Calculate and print the area of a rectangle with length 10 and breadth 20
        area = calculate_rectangle_area(10, 20)
        print(
            f"The area of a rectangle with length 10 and breadth 20 is {area}."
        )
    except ValueError as e:
        print(f"Error: {e}")

