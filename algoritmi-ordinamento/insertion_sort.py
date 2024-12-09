def insertion_sort(arr):
    """
    Perform insertion sort on the input list.
    
    Args:
        arr: List of elements to be sorted.
        
    Returns:
        The sorted list.
    """
    for i in range(1, len(arr)):
        # Extract the current element to be positioned
        current = arr[i]
        j = i - 1

        # Shift elements of the sorted segment that are greater than current
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the current element in its correct position
        arr[j + 1] = current

    return arr

# Example usage
numbers = [12, 11, 13, 5, 6]
sorted_numbers = insertion_sort(numbers)
print("Sorted array:", sorted_numbers)