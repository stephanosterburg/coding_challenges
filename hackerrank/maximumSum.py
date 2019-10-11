# Given an n element array of integers, a, and an integer, m, determine the
# maximum value of the sum of any of its subarrays modulo m. For example,
# assume a = [1, 2, 3] and m = 2. The following table lists all subarrays
# and their moduli:
#
# 		      sum	%2
# [1]		    1	1
# [2]		    2	0
# [3]		    3	1
# [1,2]		    3	1
# [2,3]		    5	1
# [1,2,3]		6	0
#
# The maximum modulus is 1.
#
import math
import os
import random
import re
import sys
import filecmp

def maximumSum(a, m):

    result = 0
    min, max, k = 0, 1, 0
    for i in range(len(a)):
        for j in range(len(a)-k):
            temp = sum(a[min:max]) % m
            if temp > result:
                result = temp
            min += 1
            max += 1
        min = 0
        max = k+1
        k += 1

    return result


if __name__ == '__main__':
    input_f = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/maximum-subarray-sum-testcases/input/input99.txt'
    output_f = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/maximum-subarray-sum-testcases/output/output99.txt'
    result_f = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/maximum-subarray-sum-testcases/output/result99.txt'
    fptr = open(result_f, 'w')

    with open(input_f) as f:
        lines = [line.rstrip('\n') for line in f]
        q = int(lines[0]) * 2

    for i in range(1, q, 2):
        nm = lines[i].split()

        n = int(nm[0])
        m = int(nm[1])
        a = list(map(int, lines[i+1].rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

    
    print(filecmp.cmp(output_f, result_f))


"""    test cases
m = 7
a = [3, 3, 9, 9, 5]
print(maximumSum(a, m))

m = 5
a = [1, 5, 9]
print(maximumSum(a, m))  # 4


m = 1804289384
a = [846930887, 1681692778, 1714636916, 1957747794, 424238336, 719885387, 1649760493,
    596516650, 1189641422, 1025202363, 1350490028, 783368691, 1102520060, 2044897764 ,
    1967513927, 1365180541, 1540383427, 304089173, 1303455737, 35005212, 521595369 ,
    294702568, 1726956430, 336465783, 861021531, 278722863, 233665124, 2145174068,
    468703136, 1101513930, 1801979803, 1315634023, 635723059, 1369133070, 1125898168,
    1059961394, 2089018457, 628175012, 1656478043, 1131176230, 1653377374, 859484422,
    1914544920, 608413785, 756898538, 1734575199, 1973594325, 149798316, 2038664371,
    1129566414]
print(maximumSum(a, m))  # 1802192837
"""
