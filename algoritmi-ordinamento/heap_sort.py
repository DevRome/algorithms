def heapify(arr, n, i):
    """
    Maintains the heap property for a subtree rooted at index i.

    Args:
        arr: List of elements.
        n: Size of the heap.
        i: Root index of the current subtree.
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Performs heap sort on the input list.

    Args:
        arr: List of elements to be sorted.
        
    Returns:
        The sorted list.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[i], arr[0] = arr[0], arr[i]
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

    return arr


# Example usage
numbers = [12, 11, 13, 5, 6, 7]
sorted_numbers = heap_sort(numbers)
print("Sorted array:", sorted_numbers)
