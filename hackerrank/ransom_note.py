#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    x = Counter(note)
    y = Counter(magazine)

    overlap = list((x & y).elements())

    if len(note) - len(overlap) > 0:
        print('No')
    else:
        print('Yes')



if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/ctci-ransom-note-testcases/input/input00.txt", 'r')

    mn = list(map(int, filename.readline().split()))
    m = int(mn[0])
    n = int(mn[1])

    magazine = list(map(str, filename.readline().split()))
    note = list(map(str, filename.readline().split()))

    checkMagazine(magazine, note)
