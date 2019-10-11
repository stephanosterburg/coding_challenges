# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid
# with digits so that each columns, each rows, and each of the nine 3 × 3 sub-grids
#  that compose the grid contains all of the digits from 1 to 9.
#
# This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
#
# Example
#
# For the first example below, the output should be true. For the other grid,
# the output should be false: each of the nine 3 × 3 sub-grids should contain
# all of the digits from 1 to 9.

# True
grid1 = [[1,3,2,5,4,6,9,8,7],
         [4,6,5,8,7,9,3,2,1],
         [7,9,8,2,1,3,6,5,4],
         [9,2,1,4,3,5,8,7,6],
         [3,5,4,7,6,8,2,1,9],
         [6,8,7,1,9,2,5,4,3],
         [5,7,6,9,8,1,4,3,2],
         [2,4,3,6,5,7,1,9,8],
         [8,1,9,3,2,4,7,6,5]]

# False
grid2 = [[1,3,2,5,4,6,9,2,7],
         [4,6,5,8,7,9,3,8,1],
         [7,9,8,2,1,3,6,5,4],
         [9,2,1,4,3,5,8,7,6],
         [3,5,4,7,6,8,2,1,9],
         [6,8,7,1,9,2,5,4,3],
         [5,7,6,9,8,1,4,3,2],
         [2,4,3,6,5,7,1,9,8],
         [8,1,9,3,2,4,7,6,5]]


def sudoku(grid):
    # Loop over 9x9 matrix and check if numbers horizontally, vertically and for each 3x3 square
    for rows in range(9):
        for columns in range(9):
            if not check_horizontal(rows, columns, grid):
                return False
            if not check_vertical(rows, columns, grid):
                return False
            if not check_square(rows, columns, grid):
                return False

    return True


def check_horizontal(rows, columns, grid):
    for c in range(9):
        if columns == c:
            continue
        if check_position(rows, columns, rows, c, grid):
            return False

    return True


def check_vertical(rows, columns, grid):
    for r in range(9):
        if rows == r:
            continue
        if check_position(rows, columns, r, columns, grid):
            return False

    return True


def check_square(rows, columns, grid):
    center_point = get_square_center_pos(rows, columns)
    all_points = get_all_points_in_square(center_point[0], center_point[1])
    for point in all_points:
        if rows == point[0] and columns == point[1]:
            continue
        if check_position(rows, columns, point[0], point[1], grid):
            return False

    return True


def get_square_center_pos(rows, columns):
    centers = [[1, 1], [1, 4], [1, 7], [4, 1], [4, 4], [4, 7], [7, 1], [7, 4], [7, 7]]
    for r in range(rows - 1, rows + 2):
        for c in range(columns - 1, columns + 2):
            if [r, c] in centers:
                return [r, c]


def get_all_points_in_square(row, col):
    # Return all points from each 3x3 square
    return [[rows, columns] for rows in range(row - 1, row + 2) for columns in range(col - 1, col + 2)]


def check_position(r1, c1, r2, c2, grid):
    # Returns True if a number already exists in row or column or square
    return grid[r1][c1] == grid[r2][c2]


print(sudoku(grid1))
print(sudoku(grid2))


