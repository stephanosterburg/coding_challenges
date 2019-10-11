from itertools import product

filename = '..../practice-coding/hackerrank/itertools-product-testcases/input/input00.txt'

with open(filename) as f:
    lines = [list(map(int, line.rstrip('\n').split())) for line in f]
    print(list(product(*lines)))

# hackerrank version
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# print(*product(A, B))
