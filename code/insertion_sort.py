from typing import List

def insertion_sort(array: List[int]) -> List[int]:
    """
    Sort a list of integers using insertion sort algorithm.
    param array (List[int])     : list of un sorted integers.
    return array (List[int])    : the list of sorted integers.
    """
    # loop over each element
    for i in range(1, len(array)):
        # get the second element from the array
        key = array[i]
        # get the first element index from the array
        j = i-1
        # loop over tha array start from i-1 to 0 to shift elements
        # if the prev element is > the current element.
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        # shift back the current element.
        array[j+1] = key
    # return the sorted array
    return array


array = [10, 6, 5, 9, 1, 2, 0, 4]
print(insertion_sort(array))
