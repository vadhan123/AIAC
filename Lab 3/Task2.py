def bubble_sort(arr):
    """Simple bubble sort"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
    
    return arr_copy

def selection_sort(arr):
    """Simple selection sort"""
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    
    return arr_copy

def main():
    # Test arrays
    arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3]
    ]
    
    print("=== Simple Sorting Demo ===")
    
    for i, arr in enumerate(arrays, 1):
        print(f"\nArray {i}: {arr}")
        
        bubble_result = bubble_sort(arr)
        selection_result = selection_sort(arr)
        
        print(f"Bubble Sort: {bubble_result}")
        print(f"Selection Sort: {selection_result}")
        print(f"Python sorted(): {sorted(arr)}")

if __name__ == "__main__":
    main()
