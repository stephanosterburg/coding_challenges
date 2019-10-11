# Starting with a 1-indexed array of zeros and a list of operations, for each
# operation add a value to each of the array element between two given indices,
# inclusive. Once all operations have been performed, return the maximum value
# in your array
#
# Sample Input
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100
#
# Sample Output
# 200
#
# Explanation
#
# After the first update list will be 100 100 0 0 0.
# After the second update list will be 100 200 100 100 100.
# After the third update list will be 100 200 200 200 100.
# The required answer will be .
#
import os

def arrayManipulation(n, queries):
    arr = [0] * n # (n+1)
    for query in queries:
        for i in range(int(query[0])-1, int(query[1]), 1):
            arr[i] += int(query[2])
    # The below code passes on hackerrank
    #     a, b, k = query[0], query[1], query[2]
    #     arr[a - 1] = arr[a - 1] + k
    #     arr[b] = arr[b] - k
    #
    # for i in range(1, n):
    #     arr[i] += arr[i - 1]

    return max(arr)


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/hackerrank/crush-testcases/input/input00.txt", 'r')

    nm = filename.readline().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, filename.readline().rstrip().split())))

    print(arrayManipulation(n, queries))  # 7542539201
