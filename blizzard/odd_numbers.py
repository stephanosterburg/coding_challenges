def oddNumbers(l, r):
    res = [i for i in range(l, r+1) if i % 2 != 0]
    return res


l = 3
r = 9
print(oddNumbers(l, r))
