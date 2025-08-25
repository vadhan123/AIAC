def extract_student_details(students):
    for student in students:
        print(f"FullName: {student['FullName']}, Branch: {student['Branch']}, SGPA:{student['SGPA']}")

# Example usage:
students = [
    {"FullName": "vadhan ganji", "Branch": "CSEAIML", "SGPA": 9.1},
    {"FullName": "siddhu", "Branch": "EEE", "SGPA": 7.1},
    {"FullName": "rishi", "Branch": "mechanical", "SGPA": 8.5}
]

extract_student_details(students)