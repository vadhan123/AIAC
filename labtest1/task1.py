# SRU_Student class initialization
class SRU_Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        print("SRU_Student class initialization")

    def Student_Data(self, filename="student_data.txt"):
        data = f"Name: {self.name}\nRoll No: {self.roll_no}\nDepartment: {self.department}\n\n"
        with open(filename, "a") as file:  # Append mode
            file.write(data)
        print("Student_Data")

if __name__ == "__main__":
    while True:
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        department = input("Enter department: ")
        student = SRU_Student(name, roll_no, department)
        student.Student_Data()
        print("Text Document having student data updated.")
        more = input("Add another student? (y/n): ").strip().lower()
        if more != 'y':
            break
