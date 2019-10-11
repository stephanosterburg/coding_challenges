def countInversions(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1

    return count

arr = [1, 1, 1, 2, 2]
print(countInversions(arr)) # 0

arr = [2, 1, 3, 1, 2]
print(countInversions(arr)) # 4
