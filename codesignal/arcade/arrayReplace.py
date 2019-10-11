"""
Given an array of integers, replace all the occurrences of
elemToReplace with substitutionElem.

Example

For
    inputArray = [1, 2, 1],
    elemToReplace = 1, and
    substitutionElem = 3,
the output should be
arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
"""
def arrayReplace(inputArray, elemToReplace, substitutionElem):

    # new_array = []
    # for i in inputArray:
    #     if i == elemToReplace:
    #         new_array.append(substitutionElem)
    #     else:
    #         new_array.append(i)
    #
    # return new_array

    return [x if x != elemToReplace else substitutionElem for x in inputArray]
    

inputArray = [1, 2, 1]
elemToReplace = 1
substitutionElem = 3
print(arrayReplace(inputArray, elemToReplace, substitutionElem))
