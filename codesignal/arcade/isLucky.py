# Ticket numbers usually consist of an even number of digits.
# A ticket number is considered lucky if the sum of the first
# half of the digits is equal to the sum of the second half.
#
# Given a ticket number n, determine if it's lucky or not.
#
# Example
#
# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.

n = 239017
firstpart, secondpart = str(n)[:len(str(n))//2], str(n)[len(str(n))//2:]
n1 = sum(map(int, firstpart))
n2 = sum(map(int, secondpart))
print(n1, n2)