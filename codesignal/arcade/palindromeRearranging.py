"""
Given a string, find out if its characters can be rearranged
to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""
from collections import Counter
def palindromeRearranging(inputString):
    count = 0
    for k, val in Counter(inputString).items():
        if abs(val % 2) == 1:
            count += 1

    return False if count > 1 else True

inputString = "aabb"
print(palindromeRearranging(inputString))
