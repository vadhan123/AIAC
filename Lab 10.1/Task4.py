def welcome_student(student_name):
    """
    Print a welcome message for a single student.

    Parameters:
        student_name (str): The name of the student to welcome.

    Raises:
        ValueError: If student_name is not a string or is empty.
    """
    # Check if the input is a valid non-empty string
    if not isinstance(student_name, str) or not student_name:
        raise ValueError("student_name must be a non-empty string.")
    print(f"Welcome {student_name}")  # Print the welcome message


def welcome_students(student_list):
    """
    Print welcome messages for a list of students.

    Parameters:
        student_list (list): List of student names (strings).

    Raises:
        ValueError: If student_list is not a list or contains invalid names.
    """
    # Check if the input is a list
    if not isinstance(student_list, list):
        raise ValueError("student_list must be a list.")
    for name in student_list:
        welcome_student(name)  # Use the reusable function for each student


# Example usage
if __name__ == "__main__":
    students1 = ["Alice", "Bob", "Charlie"]
    welcome_students(students1)

    # More examples
    students2 = ["David", "Eva"]
    welcome_students(students2)

    students3 = ["Frank"]
    welcome_students(students3)

    # Uncomment to see exception handling:
    # welcome_students(["Grace", 123, "Henry"])  # This will raise ValueError