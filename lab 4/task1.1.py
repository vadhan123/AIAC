def validate_indian_mobile(mobile_number):
    """
    Validates an Indian mobile number.
    Returns True if valid, False otherwise.
    
    Valid Indian mobile number criteria:
    - Must start with 6, 7, 8, or 9
    - Must contain exactly 10 digits
    """
    # Remove any spaces or special characters
    mobile_number = ''.join(filter(str.isdigit, str(mobile_number)))
    
    # Check if it's exactly 10 digits
    if len(mobile_number) != 10:
        return False
    
    # Check if it starts with 6, 7, 8, or 9
    if mobile_number[0] not in ['6', '7', '8', '9']:
        return False
    
    return True


if __name__ == "__main__":
    try:
        user_input = input("Enter an Indian mobile number: ").strip()
        is_valid = validate_indian_mobile(user_input)
        print(f"Mobile number validation result: {is_valid}")
    except Exception as e:
        print(f"Error: {e}")
