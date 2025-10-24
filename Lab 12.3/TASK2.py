def bubble_sort(arr):
    """
    Implement bubble sort algorithm to sort a list in ascending order.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: The sorted list
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize the algorithm
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is already sorted
        if not swapped:
            break
    
    return arr

# Test the bubble sort implementation
if __name__ == "__main__":
    # Original unsorted list
    test_list = [64, 34, 25, 12, 22, 11, 90]
    
    print("Original list:", test_list)
    
    # Sort the list using bubble sort
    sorted_list = bubble_sort(test_list.copy())
    
    print("Sorted list:", sorted_list)
    
    # Verify if the list is actually sorted
    is_sorted = all(sorted_list[i] <= sorted_list[i+1] for i in range(len(sorted_list)-1))
    print("Is the list correctly sorted?", is_sorted)
