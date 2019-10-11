import math
import os
import random
import re
import sys
import string

# Complete the abbreviation function below.
def abbreviation(a, b):
    if b.lower() in a.lower():
        return('YES')
    # else:
    #     return('NO')

if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/abbr-testcases/input/input01.txt", 'r') # YES NO NO YES NO YES YES YES NO NO

    q = int(filename.readline().strip())

    for q_itr in range(q):
        a = filename.readline().strip()
        b = filename.readline().strip()

        result = abbreviation(a, b)


