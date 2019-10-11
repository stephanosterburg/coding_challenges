# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do
# in 0(1) timing.
from scipy.spatial.distance import euclidean


def distance(x1, y1, x2, y2):
    return round(euclidean([x1, y1], [x2, y2]), 2)


print(distance(1, 1, 0, 0))  # 1.41
