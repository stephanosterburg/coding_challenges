def minimumSwaps(arr):
    swaps = 0

    for i in range(len(arr)):
        # Check if key-value and value are equal,
        # if not swap previous and current
        while arr[i] != i + 1:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            swaps += 1

    return swaps


arr = [2, 3, 4, 1, 5]
print(minimumSwaps(arr))
