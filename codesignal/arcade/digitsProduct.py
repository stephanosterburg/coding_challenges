# For a given n, following are the two cases to be considered.
#
# Case 1: n < 10 When n is smaller than n, the output is always n+10.
# For example for n = 7, output is 17. For n = 9, output is 19.
#
# Case 2: n >= 10 Find all factors of n which are between 2 and 9 (both
# inclusive). The idea is to start searching from 9 so that the number of
# digits in result are minimized. For example 9 is preferred over 33 and 8 is
# preferred over 24. Store all found factors in an array. The array would
# contain digits in non-increasing order, so finally print the array in
# reverse order.
#
#
#
# Given an integer product, find the smallest positive (i.e. greater than 0) integer
# the product of whose digits is equal to product. If there is no such integer, return -1 instead.
#
# Example
#
# For product = 12, the output should be
# digitsProduct(product) = 26;
# For product = 19, the output should be
# digitsProduct(product) = -1.
#
# [input] integer product
# Guaranteed constraints: 0 ≤ product ≤ 600.


def digitsProduct(num):

    # the range of numbers which could be the product of num (eg. 12 = 2 x 6 => 26 aka i)
    for i in range(1, 10000):
        product = 1

        # we "split" the number by converting it to a string and loop over each part
        for d in str(i):

            # we multiply the single digit by product and check if it is equal num
            product *= int(d)
            if product == num:
                return i

    return -1


print(digitsProduct(12))  # 26
# print(digitsProduct(19))  # -1
# print(digitsProduct(13))  # -1
# print(digitsProduct(1))  # 1
# print(digitsProduct(0))  # 10
# print(digitsProduct(243))  # 239
# print(digitsProduct(576))  # 889





