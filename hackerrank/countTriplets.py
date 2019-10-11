from collections import defaultdict

def countTriplets(arr, r):
    temp1, temp2 = defaultdict(int), defaultdict(int)

    triplets = 0
    for i in reversed(arr):
        if (i * r) in temp2:
            triplets += temp2[i * r]

        if (i * r) in temp1:
            temp2[i] += temp1[i * r]

        temp1[i] += 1

    return triplets


r = 3
arr = [1, 3, 9, 9, 27, 81]
print(countTriplets(arr, r))
