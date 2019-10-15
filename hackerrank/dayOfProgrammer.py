import math
import os
import random
import re
import sys
import calendar


# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if int(year)  == 1918:
        return '26.09.1918'
    elif ((int(year) <= 1917) & (int(year) % 4 == 0)) or ((int(year) > 1918) & (int(year) % 400 == 0 or ((int(year) % 4 == 0) & (int(year) % 100 != 0)))):
        return('12.09.' + str(year))
    else:
        return('13.09.' + str(year))


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/day-of-the-programmer-testcases/input/input00.txt", 'r')

    year = filename.readline().split()[0]

    result = dayOfProgrammer(int(year))
    print(result)