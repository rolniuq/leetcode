def find_boundary(arr: list[bool]) -> int:
  '''
  Input: arr = [false, false, true, true, true]
  Output: 2
  '''
  index = -1
  left, right = 0, len(arr) - 1
  while left <= right:
    mid = (right + left) // 2
    if arr[mid]:
      index = mid
      right = mid - 1
    else:
      left = mid + 1

  return index

find_boundary([False, False, True, True, True])
