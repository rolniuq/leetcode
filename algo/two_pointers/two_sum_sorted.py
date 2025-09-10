def two_sum_sorted(arr: list[int], target: int) -> (int, int):
    first, second = 0, 0
    while first < second:
        sum = arr[first] + arr[second]
        if sum == target:
            return first + 1, second + 1
        elif sum < target:
            first += 1
        else:
            second += 1
    return -1, -1


print(two_sum_sorted([2, 3, 4, 5, 8, 11, 18], 8))
