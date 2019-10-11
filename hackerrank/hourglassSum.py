#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    smax = -10 * 10

    for row in range(len(arr) - 2):
        for column in range(len(arr[row]) - 2):
            s = arr[row][column]
            s += arr[row][column + 1]
            s += arr[row][column + 2]
            s += arr[row + 1][column + 1]
            s += arr[row + 2][column]
            s += arr[row + 2][column + 1]
            s += arr[row + 2][column + 2]
            smax = max(s, smax)

    return(smax)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
