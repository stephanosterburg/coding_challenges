"""
Let's define digit degree of some positive integer as the number of
times we need to replace this number with the sum of its digits until
we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;

For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.

For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
"""

def digitDegree(n):
    # s = 0
    # i = 1
    #
    # if n < 10: return 0
    #
    # num_list = list(str(n))
    # results = sum(list(map(int, num_list)))
    # length = len(list(str(results)))
    # # print(results, length)
    #
    # while length > 1:
    #     num_list = list(str(results))
    #     results = sum(list(map(int, num_list)))
    #     length = len(list(str(results)))
    #     i += 1
    #
    # return i
    if n < 10:
        return 0

    sumOfDigits = sum([int(i) for i in str(n)])

    return digitDegree(sumOfDigits) + 1


print(digitDegree(5))
print(digitDegree(100))
print(digitDegree(91))
