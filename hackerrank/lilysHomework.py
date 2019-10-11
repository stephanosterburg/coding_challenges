import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
# [2, 5, 3, 1] -> [1, 2, 5, 3] -> [1, 2, 3, 5]
def countSwaps(arr):
    # Create a list of sets with index, value -> [(3, 1), (0, 2), (2, 3), (1, 5)]
    pos = sorted(list(enumerate(arr)), key=lambda i: i[1])
    swaps = 0

    for i in range(len(arr)):
        while True:
            if (pos[i][0] == i):
                break
            else:
                swaps += 1
                swapped_i = pos[i][0]
                pos[i], pos[swapped_i] = pos[swapped_i], pos[i]

    return swaps


def lilysHomework(arr):
    return min(countSwaps(arr), countSwaps(arr[::-1]))


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/lilys-homework-testcases/input/input00.txt", 'r')

    n = map(int, filename.readline().split())
    arr = list(map(int, filename.readline().rstrip().split()))

    result = lilysHomework(arr)
    print(result)
