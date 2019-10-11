# Looking at consecutive powers of n=2, starting with 2^1:
#
# 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768....
#
# Note that out of all the digits 0-9, the last one ever to appear is 7.
# It only shows for the first time in the number 2^15=32768. So let us
# define LAST DIGIT TO APPEAR as:
#
# LDTA(n) = The last digit to be written down when writing all the powers
# of n, starting with n^1
#
# You'll be given a positive integer 1 =< n <= 10000, and must return the
# integer number LDTA(n)
#
# If for any reason there are digits which never appear in the sequence
# of powers, return None.
#
# Please note: The Last digit to appear can be in the same number as the
# penultimate one, e.g: LDTA(8)=7 though the digit '3' appears slightly
# before it, in the same number: 8, 64, 512, 4096, 32768....
def LDTA(n):
    return pow(n, 2)


print(LDTA(1))  # None
print(LDTA(2))  # 7
print(LDTA(8))  # 7
print(LDTA(1111))  # 9
