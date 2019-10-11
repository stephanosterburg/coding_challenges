# Given array of integers, for each position i, search among the previous
# positions for the last (from the left) position that contains a smaller
# value. Store this value at position i in the answer. If no such value
# can be found, store -1 instead.
#
# Example
#
# For items = [3, 5, 2, 4, 5], the output should be
# arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
#
def arrayPreviousLess(items):
    result = []

    for k, v in enumerate(items):
        for i in range(k, -1, -1):
            if v > items[i]:
                result.append(items[i])
                break
            elif i == 0:
                result.append(-1)

    return result


items = [3, 5, 2, 4, 5]
print(arrayPreviousLess(items))


items = [2, 2, 1, 3, 4, 5, 5, 3]
print(arrayPreviousLess(items))  # [-1, -1, -1, 1, 3, 4, 4, 1]
