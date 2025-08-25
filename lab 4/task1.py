import re

def is_valid_indian_mobile(number):
    """
    Validates if the given number is a valid Indian mobile number.
    Requirements:
    - Starts with 6, 7, 8, or 9
    - Contains exactly 10 digits
    """
    pattern = r'^[6-9]\d{9}$'
    return bool(re.match(pattern, number))

if __name__ == "__main__":
    phone = input("Enter an Indian mobile number: ")
    print(is_valid_indian_mobile(phone))