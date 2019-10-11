import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    c = Counter(arr)
    return c.most_common(1)[0][0]


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/migratory-birds-testcases/input/input00.txt", 'r')

    count = filename.readline().rstrip().split()
    arr = list(map(int, filename.readline().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)