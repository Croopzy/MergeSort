# Merge Algorithm
def merge(arrIn, low, mid, high, reverse = False):
  pos1 = 0  # Position in Buffer Array (First Half of arrIn)
  pos2 = mid + 1  # Position in Second Half of arrIn
  posM = low  # Merge Position

  # Create Buffer Array
  arr1 = arrIn[low:(mid + 1)]  # Starts Inclusive, Ends Exclusive (Hence mid -> (mid + 1))
  len1 = len(arr1)  # Number of Items in Buffer Array

  # Merging Arrays
  while (pos1 < len1) and (pos2 <= high):  # While Not At End of Either List
    if (arr1[pos1] < arrIn[pos2]) if (not reverse) else (arr1[pos1] > arrIn[pos2]):  #  Compare Current Buffer Array Element To Current Second Half Element
      arrIn[posM] = arr1[pos1]  # Write Current Buffer Element To Merged Array
      pos1 += 1  # Next Item in Buffer Array
    else:
      arrIn[posM] = arrIn[pos2] # Write Current Element From Second Array To Merged Array
      pos2 += 1  # Next Item in Second Half
    posM += 1  # Always Increment Position in Merged Array
  # endwhile

  while pos1 < len1:  # Executes IF pos2 == (high + 1)
    arrIn[posM] = arr1[pos1]  # Copy Remaining Buffer Array To Merged Array
    pos1 += 1  # Next Item in Buffer Array
    posM += 1  # Increment Position in Merged Array
  # endwhile

  while pos2 <= high:  # Executes IF pos1 == len1
    arrIn[posM] = arrIn[pos2]  # Copy Remaining Second Half To Merged Array
    pos2 += 1  # Next Item in Second Half
    posM += 1  # Increment Position in Merged Array
# endprocedure


# Full Merge Sort Algorithm
def merge_sort(arrIn, low, high, reverse = False):
  if low < high:
    mid = (low + high) // 2
    merge_sort(arrIn, low, mid, reverse) # Sort First Half
    merge_sort(arrIn, (mid + 1), high, reverse) # Sort Second Half
    merge(arrIn, low, mid, high, reverse) # Merge Sorted Halves
# endprocedure
    
