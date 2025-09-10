def remove_duplicate(arr: list[int]) -> list[int]:
    first, right = 0, 1
    arr.sort()
    while right < len(arr):
        if arr[first] != arr[right]:
            first += 1
            arr[first] = arr[right]

        right += 1

    return arr[: first + 1]


print(remove_duplicate([0, 0, 0, 1, 1, 2, 2]))
