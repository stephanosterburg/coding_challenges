def rotLeft(a, d):
    N = len(a)
    r = a[d - N : N] + a[0 : d - N]
    return(' '.join(map(str, r)))



d = 4
a = [1, 2, 3, 4, 5]
print(rotLeft(a, d)) # 5 1 2 3 4

d = 13
a = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]
print(rotLeft(a, d)) # 87 97 33 47 70 37 8 53 13 93 71 72 51 100 60
