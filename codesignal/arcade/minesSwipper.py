"""
In the popular Minesweeper game you have a board with some mines and those cells that
don't contain a mine have a number in it that indicates the total number of mines in
the neighboring cells. Starting off with some arrangement of mines we want to create
a Minesweeper game setup.

Example

For

matrix = [[true,  false, false],
          [false, true,  false],
          [false, false, false]]

the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell
contains a mine, false otherwise.

Guaranteed constraints:
2 <= matrix.length <= 100,
2 <= matrix[0].length <= 100.
"""
def countNeighbors(column, row, matrix):
    """

    :param column: column index in matrix
    :param row: row index in matrix
    :param matrix: matrix itself
    :return: count it found
    """
    # count = 0
    # depth = len(matrix) - 1
    # width = len(matrix[0]) - 1
    #
    # column_left = findBorder(column - 1, depth)
    # column_right = findBorder(column + 1, depth)
    # row_top = findBorder(row - 1, width)
    # row_btn = findBorder(row + 1, width)
    # print(column_left, column_right, row_top, row_btn)
    #
    # for wide in range(column_left, column_right + 1):
    #     for high in range(row_top, row_btn + 1):
    #         if wide == column and high == row:
    #             continue
    #
    #         if matrix[wide][high]:
    #             count += 1
    #
    # return count


def findBorder(num, border):
    """
    Determine if there is anything next to num (index)
    :param num:
    :param border:
    :return:
    """
    if num < 0:
        return 0

    if num > border:
        return border

    return num


def minesweeper(matrix):
    # create empty array to fill
    # result = [[] for x in range(len(matrix))]
    #
    # # walk thru matrix
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #         # look around i,j and see whats there
    #         result[i].append(countNeighbors(i, j, matrix))
    #
    # return result

    # Short and Simple
    result = []

    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[0]):
                        l += matrix[i + x][j + y]

            result[i].append(l)

    return result


matrix = [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]
print(minesweeper(matrix))
