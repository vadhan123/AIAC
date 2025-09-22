
# Data type of marks: list of numbers (int or float)
def calculate_average(marks):
	"""
	Calculate the average of a list of marks.

	Args:
		marks (list): A list of numerical marks.

	Returns:
		float: The average of the marks.
	Raises:
		ValueError: If the marks list is empty or contains non-numeric values.
	"""
	if not marks:
		raise ValueError("The marks list is empty.")
	total = 0
	for m in marks:
		if not isinstance(m, (int, float)):
			raise ValueError("All elements in marks must be numbers.")
		total += m
	average = total / len(marks)
	return average

marks = [85, 90, 78, 92]

try:
	print("Average Score is", calculate_average(marks))
except ValueError as e:
	print("Error:", e)
	