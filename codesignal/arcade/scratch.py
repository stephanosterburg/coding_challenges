# Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid
# with digits so that each column, each row, and each of the nine 3 × 3 sub-grids
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
grid = [[1,3,2,5,4,6,9,8,7],
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
    for deep in range(9):
        for wide in range(9):
            if not check_horizontal(deep, wide, grid):
                return False
            if not check_vertical(deep, wide, grid):
                return False
            if not check_square(deep, wide, grid):
                return False

    return True


def check_horizontal(deep, wide, grid):
    for w in range(9):
        if wide == w:
            continue
        if equal_pos(deep, wide, deep, w, grid):
            return False

    return True


def check_vertical(deep, wide, grid):
    for d in range(9):
        if deep == d:
            continue
        if equal_pos(deep, wide, d, wide, grid):
            return False

    return True


def check_square(deep, wide, grid):
    center_point = get_square_center_pos(deep, wide)
    all_points = get_all_points_in_square(center_point[0], center_point[1])
    for point in all_points:
        if deep == point[0] and wide == point[1]:
            continue
        if equal_pos(deep, wide, point[0], point[1], grid):
            return False

    return True


def get_square_center_pos(deep, wide):
    centers = [[1,1], [1,4], [1,7], [4,1], [4,4], [4,7], [7,1], [7,4], [7,7]]
    for d in range(deep - 1, deep + 2):
        for w in range(wide - 1, wide + 2):
            if [d, w] in centers:
                return [d, w]


def get_all_points_in_square(d, w):
    return [[deep, wide] for deep in range(d - 1, d + 2) for wide in range(w - 1, w + 2)]
    # return points


def equal_pos(d1, w1, d2, w2, grid):
    return grid[d1][w1] == grid[d2][w2]


print(sudoku(grid))
