import numpy as np

grid = [['X', 'X', '?'], ['X', '?', 'X'], ['X', '?', '?']]

# Convert list of lists to a numpy array
arr = np.array(grid)
# Pad the array
arr_pad = np.pad(arr, ((1, 1), (1, 1)), 'constant')
arr_pad[arr_pad == '?'] = 0

count = 0
for i in range(1, len(grid) + 1):
    for j in range(1, len(grid) + 1):
        if arr_pad[i][j] == '0':
            for m in [i - 1, i, i + 1]:
                for n in [j - 1, j, j + 1]:
                    if arr_pad[m][n] == 'X':
                        count += 1
                        arr_pad[i][j] = count

            count = 0

print(arr_pad[1:4, 1:4])
