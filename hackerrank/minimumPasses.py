import math
import os
import random
import re
import sys

# Sample Input
#
# 3 1 2 12
# Sample Output
#
# 3
# Explanation
#
# Karl makes three passes:
# 1. In the first pass, he makes m * w = 3 * 1 = 3 candies. He then spends p = 2 of them hiring another worker,
#    so w = 2 and he has one candy left over.
# 2. In the second pass, he makes 3 * 2 = 6 candies. He spends 2 * p = 4 of them on another machine and another
#    worker, so w = 3 and m = 4 and he has 3 candies left over.
# 3. In the third pass, Karl makes 4 * 3 = 12 candies. Because this satisfies his goal of making at least n =12 candies,
#    we print the number of passes (i.e., 3) as our answer.
def minimumPasses(m, w, p, n):
    print(m, w, p, n)

if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/making-candies-testcases/input/input00.txt", 'r')

    mwpn = list(map(int, filename.readline().split()))
    m = mwpn[0]
    w = mwpn[1]
    p = mwpn[2]
    n = mwpn[3]

    result = minimumPasses(m, w, p, n)
    print(result)