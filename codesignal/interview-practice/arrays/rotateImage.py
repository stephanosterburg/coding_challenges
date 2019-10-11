import numpy as np
def rotateImage(a):
	return np.rot90(np.array(a), k=-1)


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(rotateImage(a))