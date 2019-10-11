import math
import os
import random
import re
import sys
import functools

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def  greatest_common_devisor(a, b):
    while a % b != 0:
        a, b = b, (a % b)

    return b


def least_common_multiplier(a, b):
    return a * b // greatest_common_devisor(a, b)


def getTotalX(a, b):
    gcd = functools.reduce(greatest_common_devisor, b)
    lcm = functools.reduce(least_common_multiplier, a)
    count = sum([1 for x in range(lcm, gcd + 1, lcm) if gcd % x == 0])

    return count


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/between-two-sets-testcases/input/input00.txt", 'r')

    first_multiple_input = filename.readline().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = list(map(int, filename.readline().rstrip().split()))
    brr = list(map(int, filename.readline().rstrip().split()))

    total = getTotalX(arr, brr)
    print(total)