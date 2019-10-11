"""
Given an array of integers, find the maximal absolute difference
between any two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""
def arrayMaximalAdjacentDifference(inputArray):

    # count = 0
    # length = len(inputArray)
    #
    # for i in range(1, length - 1):
    #     if abs(inputArray[i] - inputArray[i - 1]) > count:
    #         count = abs(inputArray[i] - inputArray[i - 1])
    #
    #     if abs(inputArray[i] - inputArray[i + 1]) > count:
    #         count = abs(inputArray[i] - inputArray[i + 1])
    #
    # return count
    diffs = [abs(inputArray[i] - inputArray[i + 1]) for i in range(len(inputArray) - 1)]
    return max(diffs)

inputArray = [2, 4, 1, 0]
print(arrayMaximalAdjacentDifference(inputArray))
