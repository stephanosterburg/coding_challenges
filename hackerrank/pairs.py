# Determine the number of pairs of array elements that have a difference
# equal to a target value. For example, given an array of [1, 2, 3, 4] and
# a target value of 1, we have three values meeting the condition:
# 2 -1 = 1, 3 -2 = 1, and 4 -3 = 1
#
# Your code did not execute within the time limits
# when using pairs_input09.txt
def pairs(k, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] - arr[j] == k:
                count += 1

    return count


k = 2
arr = [1, 5, 3, 4, 2]
print(pairs(k, arr))  # 3


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nk = input().split()
#
#     n = int(nk[0])
#
#     k = int(nk[1])
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = pairs(k, arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
