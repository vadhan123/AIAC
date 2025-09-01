class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll number: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            grade = 'A'
        elif self.marks >= 75:
            grade = 'B'
        elif self.marks >= 60:
            grade = 'C'
        else:
            grade = 'Fail'
        print(f"Grade: {grade}")


student1 = Student("vadhan", 2266, 95)
student1.display()
student2 = Student("Ramu", 2268, 45)
student2.display()
student3 = Student("hrishik", 2271, 78)
student3.display()
student1.calculate_grade()
student2.calculate_grade()
student3.calculate_grade()
    
    
    