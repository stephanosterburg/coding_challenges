# Program the function distance(p1, p2) which returns the distance between the points p1 and p2 in
# n-dimensional space. p1 and p2 will be given as arrays.
#
# Your program should work for all lengths of arrays, and should return -1 if the arrays aren't of
# the same length or if both arrays are empty sets.
#
# If you don't know how to measure the distance between two points,
# go here: http://mathworld.wolfram.com/Distance.html
import numpy as np


def distance(p1, p2):
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)

    # compare if both arrays are of same shape, and neither one of them of size zero
    if p1.shape == p2.shape and (np.size(p1) != 0 or np.size(p2) != 0):
        return np.linalg.norm(p1 - p2)
    else:
        return -1


print(distance([2, 2], [1, 1]))
print(distance([1], [1, 1, 1, 1, 1, 1, 1, 1, 1]))
# test.describe("Normal cases")
# test.assertEqual(distance([2,2],[1,1]), 2**0.5)
# test.assertEqual(distance([4],[1]), 3)
# test.assertEqual(distance([1,1,1],[0,0,0]), 3**0.5)
# test.assertEqual(distance([2,1,3,1],[2,0,2,-1]), 6**0.5)
# test.assertEqual(distance([3,2,3],[0,1,1]), 14**0.5)

# test.describe("Bad input/edge cases")
# test.assertEqual(distance([],[]), -1)
# test.assertEqual(distance([1],[1,1,1,1,1,1,1,1,1]), -1)
