# Digit root of some positive integer is defined as the sum of all of its digits.
#
# You are given an array of integers. Sort it in such a way that if a comes
# before b then the digit root of a is less than or equal to the digit root of b.
# If two numbers have the same digit root, the smaller one (in the regular sense)
# should come first. For example 4 and 13 have the same digit root, however 4 < 13
# thus 4 comes before 13 in any digitRoot sorting where both are present.
#
# Example
#
# For a = [13, 20, 7, 4], the output should be [20, 4, 13, 7].
#
import collections


def digit_root(n):
    # https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
    # The if-statement is there to catch if a given number is negative
    return (n - 1) % 9 + 1 if n else 0


def digitRootSort(a):
    val_list = []
    for i in a:
        val_list.append(digit_root(i))

    # This works but still fails on the last test in codesignal
    d = [x for _, x in sorted(zip(val_list, a))]

    # This only works if all numbers a unique
    #
    # d = dict(zip(a, val_list))
    # sorted_by_key = collections.OrderedDict(sorted(d.items(), key=lambda k: len(str(k[0]))))
    # sorted_by_value = sorted(sorted_by_key.items(), key=lambda v: v[1])
    #
    # new_list = []
    # for i in sorted_by_value:
    #     new_list.append(i[0])

    return d


print(digitRootSort([13, 20, 7, 4]))
print(digitRootSort([100, 22, 4, 11, 31, 103]))
print(digitRootSort([100, 22, 4, 11, 11, 7, 31, 103]))
print(digitRootSort([13, 20, 7, 4, 13, 11, 11, 11]))
print(digitRootSort([2, 1]))


