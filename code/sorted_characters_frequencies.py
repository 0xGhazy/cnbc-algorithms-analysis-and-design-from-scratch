from typing import List

class CharFreq:

  def __init__(self):
    pass

  def AnyCodeMethod(self, message: str):
    freq = {}
    # Count the frequency of any character in the string
    for i in message:
        if freq.get(i) is None:
            freq[i] = 1
        else:
            freq[i] += 1
    self.SortHash(freq)

  def SortHash(self, freq: dict):
    freqArray = [[ord(k), v] for k, v in freq.items()]
    # Sort the array in descending order based on the frequency count
    self.sort(freqArray, 0, len(freq) - 1)
    print("Print Sorted data ...")
    # Print the characters and their corresponding frequencies
    for rec in freqArray:
      print(chr(rec[0]), rec[1])

  def sort(self, array: List[List[int]], start: int, end: int):
    if end <= start:
      return

    midpoint = (end + start) // 2
    self.sort(array, start, midpoint)
    self.sort(array, midpoint + 1, end)
    self.merge_(array, start, midpoint, end)

  def merge_(self, array: List[List[int]], start: int, mid: int, end: int):
    # Calculate lengths of two sub-arrays
    left_length = mid - start + 1
    right_length = end - mid
    # Create temporary sub-arrays

    left_array = [[0, 0] for i in range(left_length)]
    right_array = [[0, 0] for j in range(right_length)]

    # Copy data to temporary sub-arrays
    for i in range(left_length):
      left_array[i][0] = array[start + i][0]
      left_array[i][1] = array[start + i][1]
    for j in range(right_length):
      right_array[j][0] = array[mid + 1 + j][0]
      right_array[j][1] = array[mid + 1 + j][1]

    # Merge the temporary sub-arrays back into the original array
    i = 0
    j = 0
    k = start
    while i < left_length and j < right_length:
      if left_array[i][1] <= right_array[j][1]:
        array[k][0] = left_array[i][0]
        array[k][1] = left_array[i][1]
        i += 1
      else:
        array[k][0] = right_array[j][0]
        array[k][1] = right_array[j][1]
        j += 1
      k += 1

    # Copy the remaining elements of left_array[] if any
    while i < left_length:
      array[k][0] = left_array[i][0]
      array[k][1] = left_array[i][1]
      i += 1
      k += 1

    # Copy the remaining elements of right_array[] if any
    while j < right_length:
      array[k][0] = right_array[j][0]
      array[k][1] = right_array[j][1]
      j += 1
      k += 1

if __name__ == "__main__":
    c = CharFreq()
    c.AnyCodeMethod("hossam")
