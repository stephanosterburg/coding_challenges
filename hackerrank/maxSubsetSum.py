import math
import os
import random
import re
import sys

# Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
# Calculate the sum of that subset.
#
# For example, given an array arr = [-2, 1, 3, -4, 5] we have the following possible subsets:
#
# Subset      Sum
# [-2, 3, 5]   6
# [-2, 3]      1
# [-2, -4]    -6
# [-2, 5]      3
# [1, -4]     -3
# [1, 5]       6
# [3, 5]       8
# Our maximum subset sum is 8
def maxSubsetSum(arr):
    # Too Slow!
    # l = [sum(arr[i::2]) for i in range(len(arr) - 2)]
    #
    # for i in range(len(arr) - 2):
    #     for j in range(i+2, len(arr)):
    #         l.append(sum((arr[i], arr[j])))
    #
    # return max(l)

    lst = []
    for i in range(0, len(arr)):
        if i == 0:
            lst.append(max(0, 0, arr[i]))
        elif i == 1:
            lst.append(max(lst[0], 0, arr[i]))
        else:
            lst.append(max(lst[i - 1], lst[i - 2], lst[i - 2] + arr[i]))

    return lst[len(arr) - 1]


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/max-array-sum-testcases/input/input00.txt", 'r')

    n = int(filename.readline().split()[0])
    arr = list(map(int, filename.readline().split()))

    res = maxSubsetSum(arr)
    print(res)
