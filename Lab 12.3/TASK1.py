def linear_search(lst, target):
    """
    Perform linear search to find the target value in the list.
    
    Args:
        lst (list): The list to search through
        target: The value to search for
    
    Returns:
        int: The index of target if found, -1 if not found
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Example usage:
if __name__ == "__main__":
    # Test the function
    my_list = [4, 2, 7, 1, 9, 5, 3]
    search_value = 7
    
    result = linear_search(my_list, search_value)
    
    if result != -1:
        print(f"Element {search_value} found at index {result}")
    else:
        print(f"Element {search_value} not found in the list")
