def binary_search(array: list, low: int, high: int, target: int) -> int:
    """
    function that take sorted array and search for passed target index

    params:
        array: array to search
        low: low index
        high: high index
        target: target element to search for

    returns:
        index: index of the target element if fount
               returns -1 if not found
    """
    if low == high:
        return -1
    # Calculate the mid element of the array
    mid = (low + high) // 2
    # Check for the target element
    if array[mid] == target:
        return mid
    else:
        # Re calculate the low and high indices of the array
        if mid > target:
            high = mid
        else:
            low = mid
    return binary_search(array, low, high, target)

