import math

def get_dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def findProbability(X, Y, C, xpos, ypos, radius):
    color = []
    for k, v in enumerate(X):
        dist = get_dist(X[k], Y[k], xpos, ypos)
        if dist <= radius:
            color.append(C[k])

    res = sum(color)/float(len(color))
    print round(res)



X = [2.0,1.0,3.0,2.0,0.0,0.0,7.0,6.0,8.0,7.0,7.0,6.0]
Y = [0.0,3.0,1.0,1.0,2.0,2.0,7.0,6.0,8.0,7.0,6.0,8.0]
C = [1,1,0,0,1,1,1,1,1,1,1,1]
xpos = 2.0
ypos = 2.0
radius = 2.0
findProbability(X, Y, C, xpos, ypos, radius)
