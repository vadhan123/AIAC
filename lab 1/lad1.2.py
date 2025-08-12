#write a Function to check if a string is a valid palindrome ignoring spaces and case .If it is a palindrome give me as true not a palindeome false.
def is_valid_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c != ' ')
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print(is_valid_palindrome(user_input))
