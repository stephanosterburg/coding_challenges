# Construct a square matrix with a size N × N containing integers
# from 1 to N * N in a spiral order, starting from top-left and in
# clockwise direction.
#
# Example
#
# For n = 3, the output should be
#
# spiralNumbers(n) = [[1, 2, 3],
#                     [8, 9, 4],
#                     [7, 6, 5]]


def spiralNumbers(n):
    m = [[0] * n for i in range(n)]         # create matrix

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]   # Starting increments in E, S, W, or N direction
    x, y, c = 0, -1, 1                      # Starting location (row, column) and number c (or count)

    for i in range(n + n - 1):              # iterate over all cells, but only looking at number of rows AND columns - 1
        for j in range((n + n - i) // 2):   # iterate over the remaining length (r + c - 1) // 2, eg 10 = 5 and 9 = 4...
            x += dx[i % 4]                  # Get location, % 4 is based on the E, S, W and N direction
            y += dy[i % 4]                  # and add the value back on x, y
            m[x][y] = c                     # Set cell value
            c += 1                          # Increment value

    return m


print(spiralNumbers(5))
print(spiralNumbers(3))
