def find_last_occurrence(arr: list[int], target: int) -> int:
    left, right, last_pos = 1, len(arr) - 1, -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            left = mid + 1
            last_pos = mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return last_pos


print(find_last_occurrence([1, 2, 3, 3, 3, 4, 5, 6, 7], 3))
