def segregate_signed_numbers(array: list) -> list:
    """function that returns a sorted list using merge sort algorithm"""
    if len(array) == 1: return
    # calculate the mid index
    mid = len(array) // 2
    # divide the array into two lists
    right_array = array[mid:]
    left_array = array[:mid]
    # call the merge function recursively twice
    segregate_signed_numbers(left_array)
    segregate_signed_numbers(right_array)
    i = j = k = 0
    # start comparing the two lists
    while i < len(left_array) and left_array[i] <= 0:
        array[k] = left_array[i]
        i+= 1
        k += 1

    while(j < len(right_array)) and right_array[j] <= 0:
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

array = [6,-5,12,10,-9,-1]
print(array)
print(segregate_signed_numbers(array))