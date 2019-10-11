import numpy as np


def binaryNumbers(n):
    b = list(map(int, bin(n)[2:]))
    return list(np.ediff1d(b)).count(0) + 1


n = 13
print(binaryNumbers(n))
