"""
Given an array of strings, return another array containing all
of its longest strings.

Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""
def allLongestStrings(inputArray):
    new_array = []
    num = 0
    for word in inputArray:
        if len(word) > num:
            num = len(word)

    for word in inputArray:
        if len(word) == num:
            new_array.append(word)

    return new_array
