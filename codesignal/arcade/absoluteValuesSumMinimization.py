# Given a sorted array of integers a, find an integer x from a such that the value of
#
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
# is the smallest possible (here abs denotes the absolute value).
# If there are several possible answers, output the smallest one.
#
# Example
#
# For a = [2, 4, 7], the output should be
# absoluteValuesSumMinimization(a) = 4.


#
# The goal of the program is to find the sum of the smallest absolute value of all numbers
# if those numbers were to be subtracted by a number. Thanks to comment, you are finding
# the number in the middle. This is since that number will be set to 0 and all other numbers
# will be reduced the most. If the list is even, you find the smaller one out of the two.
# So here is what it looks like:
#
import math

a = [2, 4, 7]

if len(a) % 2 == 1:
    print(a[math.floor(len(a)/2)])
else:
    print(a[int((len(a)/2))-1])
