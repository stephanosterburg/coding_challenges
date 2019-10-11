"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would 
be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output 
would be [2, 3, 6].
"""
import numpy as np
from operator import mul
from functools import reduce

def list_prod_np(l):
	return [np.prod([a for a in l if a != i], dtype=int) for i in l]

def list_prod_mul(l):
	return [reduce(mul, [a for a in l if a != i]) for i in l]


l = [70, 60, 64, 54, 63, 34, 89, 93, 86, 45]

# 67.5 µs ± 227 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
print(list_prod_np(l))

# 14.8 µs ± 106 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
print(list_prod_mul(l))
