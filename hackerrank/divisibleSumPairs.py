import math
import os
import random
import re
import sys
import itertools

# See divisible-sum-pairs-testcases/divisible-sum-pairs-English.pdf for discription.
def divisibleSumPairs(n, k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] + arr[j]) % k == 0:
                count += 1

    return count


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/divisible-sum-pairs-testcases/input/input00.txt", 'r')

    nk = filename.readline().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, filename.readline().rstrip().split()))

    result = divisibleSumPairs(n, k, arr)
    print(result)