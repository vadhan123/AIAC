

import unittest

def calculate_percentage(x, y):
	"""
	Calculate the percentage value of x out of y.

	Parameters:
		x (float or int): The value to calculate the percentage for.
		y (float or int): The percentage rate.

	Returns:
		float: The calculated percentage.

	Raises:
		ValueError: If x or y is not a number.
	"""
	if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
		raise ValueError("Both x and y must be numbers.")
	return x * y / 100  # Multiply x by y and divide by 100 to get the percentage


if __name__ == "__main__":
	examples = [
		(200, 15),
		(100, 50),
		(250.5, 10),
		(0, 10),
		(10, 0),
		(-100, 10),
		(100, -10),
		("a", 10),
	]
	for a, b in examples:
		# Try to calculate the percentage for each pair (a, b)
		try:
			result = calculate_percentage(a, b)  # Call the function with current values
			print(f"{b}% of {a} is {result}")  # Print the result if successful
		except ValueError as e:
			# Print an error message if invalid input is encountered
			print(f"Error for input ({a}, {b}): {e}")


