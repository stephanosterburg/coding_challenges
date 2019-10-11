def findNumber(arr, k):
    if k in arr:
        return("YES")
    else:
        return("NO")


k = 5
arr = [2, 3, 1]
print(findNumber(arr, k))
