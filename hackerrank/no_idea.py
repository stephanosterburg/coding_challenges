import os
from collections import Counter


# Input Format
# The first line contains integers  and  separated by a space.
# The second line contains  integers, the elements of the array.
# The third and fourth lines contain  integers,  and , respectively.
#
# Output Format
# Output a single integer, your total happiness.
#
# Sample Input
# 3 2
# 1 5 3
# 3 1
# 5 7
#
# Sample Output
# 1
def noidea(arr, A, B):
    # check = all(item in List1 for item in List2)
    # check =  any(item in List1 for item in List2)

    # count = 0
    # for i in A:
    #     if i in arr:
    #         count += 1
    #
    # for j in B:
    #     if j in arr:
    #         count -= 1

    arr = Counter(arr)
    A = Counter(A)
    B = Counter(B)

    A_overlap = list((A & arr).elements())
    B_overlap = list((B & arr).elements())

    return len(A_overlap) - len(B_overlap)


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/no-idea-testcases/input/input00.txt", 'r')

    nm = list(map(int, filename.readline().split()))
    arr = list(map(int, filename.readline().split()))
    A = list(map(int, filename.readline().split()))
    B = list(map(int, filename.readline().split()))

    result = noidea(arr, A, B)
    print(result)
