def insertionSort(a_list):
  print(f"Original list: {a_list}")
  for i in range(1, len(a_list)):
    while a_list[i] < a_list[i-1] and i > 0:
      a_list[i], a_list[i-1] = a_list[i-1], a_list[i]
      i -= 1
  print(f"Sorted list: {a_list}")


## Example use
original_list = [3, 5, 1, 7, 2, 8, 6]
insertionSort(original_list)
