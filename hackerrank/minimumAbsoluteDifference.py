#!/bin/python3

import math
import os
import random
import re
import sys

# Given an array of integers, find and print the minimum absolute difference
# between any two elements in the array. For example, given the array arr=[-2,3,4]
# we can create 3 pairs of numbers: [-2, 2], [-2, 4] and [2, 4]. The absolute
# differences for these pairs are |(-2) - 2| = 4, |(-2) - 4| = 6 and |2 - 4| = 2.
# The minimum absolute difference is 2.
def minimumAbsoluteDifference(arr):
    # sort array first
    arr.sort()
    # initiate first difference between the first two elements in list
    min_diff = abs(arr[0] - arr[1])
    # iterate over list and compare abs values of neighbors
    for i in range(len(arr)-1):
        diff = abs(arr[i] - arr[i+1])
        if diff < min_diff:
            min_diff = diff

    return min_diff


n = 5
arr = [1, -3, 71, 68, 17]
print(minimumAbsoluteDifference(arr))  # 3

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = minimumAbsoluteDifference(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
