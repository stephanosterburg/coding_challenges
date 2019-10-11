# Given 3 arrays a, b, c of different sizes, find the number of distinct
# triplets (p, q, r) where p is an element of a, written as p E a, q E b,
# and r E c, satisfying the criteria: p <= q and q >= r.
#
# For example, given a = [3, 5, 7], b = [3, 6] and c = [4, 6, 9],
# we find four distinct triplets: (3, 6, 4), (3, 6, 6), (5, 6, 4), (5, 6, 6).

def triplets(a, b, c):
    check = []
    for i in range(len(a)):
        for j in range(len(b)):
            for k in range(len(c)):
                if a[i] <= b[j] and b[j] >= c[k]:
                    check.append((a[i], b[j], c[k]))


    # print(set(check))
    return len(set(check))


arra = [3, 5, 7]
arrb = [3, 6]
arrc = [4, 6, 9]
print(triplets(arra, arrb, arrc))  # 4

arra = [1, 3, 5, 7]
arrb = [5, 7, 9]
arrc = [7, 9, 11, 13]
print(triplets(arra, arrb, arrc))  # 12

arra = [1, 4, 5]
arrb = [2, 3, 3]
arrc = [1, 2, 3]
print(triplets(arra, arrb, arrc))  # 5
