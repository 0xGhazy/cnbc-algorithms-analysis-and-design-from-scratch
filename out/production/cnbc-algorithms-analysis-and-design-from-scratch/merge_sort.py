
def merge_sort(array: list) -> list:
    """function that returns a sorted list using merge sort algorithm"""
    if len(array) == 1: return
    # calculate the mid index
    mid = len(array) // 2
    # divide the array into two lists
    right_array = array[mid:]
    left_array = array[:mid]
    # call the merge function recursively twice
    merge_sort(left_array)
    merge_sort(right_array)
    i = j = k = 0
    # start comparing the two lists
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i+= 1
        else:
            array[k] = right_array[j]
            j+= 1
        k += 1
    # moving all elements that left
    while i < len(left_array):
        array[k] = left_array[i]
        i+= 1; k +=1
    while j < len(right_array):
        array[k] = right_array[j]
        j+= 1; k +=1
    return array

print(merge_sort([10,5,4,8,9,6,3,44,15,78,98,65,45,12,48,78,89,65,32]))
