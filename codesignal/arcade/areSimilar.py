# Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.
#
# Given two arrays a and b, check whether they are similar.
#
# Example
#
# For a = [1, 2, 3] and b = [1, 2, 3], the output should be
# areSimilar(a, b) = true.
#
# The arrays are equal, no need to swap any elements.
#
# For a = [1, 2, 3] and b = [2, 1, 3], the output should be
# areSimilar(a, b) = true.
#
# We can obtain b from a by swapping 2 and 1 in b.
#
# For a = [1, 2, 2] and b = [2, 1, 1], the output should be
# areSimilar(a, b) = false.
#
# Any swap of any two elements either in a or in b won't make a and b equal.

# def areSimilar(A, B):
#     count = 0
#     list_a = []
#     list_b = []
#     for i in range(len(a)):
#         if a[i] != b[i]:
#             count += 1
#             # If differ append each to lists
#             list_a.append(a[i])
#             list_b.append(b[i])
#
#     if count == 0:
#         return True
#     elif count == 2:
#         # Check if lists are different
#         return set(list_a) == set(list_b)
#     else:
#         return False

# SHort and Simple
from collections import Counter as C

def areSimilar(A, B):
    return C(A) == C(B) and sum(a != b for a, b in zip(A, B)) < 3

a = [4, 6, 3]
b = [3, 4, 6]
print(areSimilar(a, b))
