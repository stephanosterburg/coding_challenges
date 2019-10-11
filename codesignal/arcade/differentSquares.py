# Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
#
# Example
#
# For
#
# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
# the output should be
# differentSquares(matrix) = 6.
#
# Here are all 6 different 2 × 2 squares:
#
# * 1 2
#   2 2
# * 2 1
#   2 2
# * 2 2
#   2 2
# * 2 2
#   1 2
# * 2 2
#   2 3
# * 2 3
#   2 1


matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

# matrix = [[9,9,9,9,9],
#           [9,9,9,9,9],
#           [9,9,9,9,9],
#           [9,9,9,9,9],
#           [9,9,9,9,9],
#           [9,9,9,9,9]]


def differentSquares(mat):
    all_coord = getCoord(mat)

    a_set = set()
    for coord in all_coord:
        # add matrix of string values to a_set if it is unique
        a_set.add(getStringSquare(mat, coord[0], coord[1]))

    return len(a_set)


def getCoord(mat):
    # get all coords for 2x2 matrix (top left corner)
    result = []
    deep = len(mat)
    wide = len(mat[0])

    for i in range(0, deep -1):
        for j in range(0, wide - 1):
            result.append([i, j])

    return result


def getStringSquare(mat, x, y):
    # get 2x2 matrix as string values
    string = str(mat[x][y])
    string += str(mat[x + 1][y + 1])
    string += str(mat[x + 1][y])
    string += str(mat[x][y + 1])

    return string


print(differentSquares(matrix))
