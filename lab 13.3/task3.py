class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        if len(marks) != 3:
            raise ValueError("Marks must contain exactly three values.")
        self.marks = marks

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def total(self):
        """Return the total of all marks."""
        return sum(self.marks)

    def average(self):
        """Return the average of all marks."""
        return sum(self.marks) / len(self.marks)

# Example usage:
if __name__ == "__main__":
    student = Student("Alice", 20, [85, 90, 88])
    student.details()
    print(f"Total Marks: {student.total()}")
    print(f"Average Marks: {student.average()}")