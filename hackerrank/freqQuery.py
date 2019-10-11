import math
import os
import random
import re
import sys

from collections import defaultdict, deque

# You are given q queries. Each query is of the form two integers described below:
# - 1 x: Insert x in your data structure.
# - 2 y: Delete one occurence of y from your data structure, if present.
# - 3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.
#
# The queries are given in the form of a 2-D array querries of size q where
# querries[i][0] contains the operation, and querries[i][1] contains the data element.
# For example, you are given array
# querries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)].
# The results of each operation are:
#
# Operation   Array   Output
# (1,1)       [1]
# (2,2)       [1]
# (3,2)                   0
# (1,1)       [1,1]
# (1,1)       [1,1,1]
# (2,1)       [1,1]
# (3,2)                   1
# Return an array with the output: [0, 1].
#
# Sample Input 0
#
# 8
# 1 5
# 1 6
# 3 2
# 1 10
# 1 10
# 1 6
# 2 5
# 3 2
# Sample Output 0
#
# 0
# 1
# Explanation 0
#
# For the first query of type 3, there is no integer whose frequency is 2 (array=[5,6]).
# So answer is 0.
# For the second query of type 3, there are two integers in array=[6, 10, 10, 6]
# whose frequency is 2 (integers = 6 and 10). So, the answer is 1.
#
# input99.txt
# NOTE: Your code did not execute within the time limits
#
def freqQuery(queries):
    d = defaultdict(int)
    result = []
    for q in queries:
        op, data = q
        if op == 1:
            d[data] += 1
        elif op == 2:
            if data in d:
                d[data] -= 1

            d[data] = 0 if d[data] < 0 else d[data]
        elif op == 3:
            result.append(1 if data in d.values() else 0)

    return result

if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/frequency-queries-testcases/input/input09.txt", 'r')

    q = int(filename.readline().strip())
    queries = []

    for _ in range(q):
        queries.append(list(map(int, filename.readline().rstrip().split())))

    print(freqQuery(queries))
