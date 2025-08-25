def extract_student_info(student_dict):
    full_name = student_dict.get('FullName', 'N/A')
    branch = student_dict.get('Branch', 'N/A')
    sgpa = student_dict.get('SGPA', 'N/A')
    
    return f"FullName: {full_name}, Branch: {branch}, SGPA: {sgpa}"


def create_student_dictionary():
    students = {
        'student1': {
            'FullName': 'arjun reddy',
            'Branch': 'CSEAIML',
            'SGPA': 9.1
        },
        'student2': {
            'FullName': 'priya patel',
            'Branch': 'EEE',
            'SGPA': 7.1
        },
        'student3': {
            'FullName': 'rahul sharma',
            'Branch': 'mechanical',
            'SGPA': 8.5
        }
    }
    return students


if __name__ == "__main__":
    student_data = create_student_dictionary()
    
    print("Student Information:")
    print("-" * 50)
    
    for student_id, student_info in student_data.items():
        extracted_info = extract_student_info(student_info)
        print(f"Example{student_id[-1]}: {extracted_info}")
    
    print("\n" + "=" * 50)
    print("Individual Student Details:")
    
    for student_id, student_info in student_data.items():
        print(f"\n{student_id.upper()}:")
        for key, value in student_info.items():
            print(f"  {key}: {value}")
