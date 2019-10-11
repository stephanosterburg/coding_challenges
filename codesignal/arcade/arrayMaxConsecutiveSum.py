# Given array of integers, find the maximal possible sum of some of its k consecutive elements.
#
# Example
#
# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
# All possible sums of 2 consecutive elements are:
#
# 2 + 3 = 5;
# 3 + 5 = 8;
# 5 + 1 = 6;
# 1 + 6 = 7.
# Thus, the answer is 8.

inputArray = [2, 3, 5, 1, 6]
k = 2


def arrayMaxConsecutiveSum(inputArray, k):
    i = 0
    max = 0
    sum = 0
    n = len(inputArray)
    while i < k:
        sum += inputArray[i]
        i += 1
    if sum > max:
        max = sum
    v = sum
    for j in range(k, n):
        v = v - inputArray[j - k] + inputArray[j]
        if v > max:
            max = v
    return(max)


print(arrayMaxConsecutiveSum(inputArray, k))