def doesIntersect(box1, box2):
    res = 0
    if (box1[0] <= box2[0] <= box1[2]) or \
        (box1[1] <= box2[1] <= box1[3]) or \
        (box2[0] <= box1[0] <= box2[2]) or \
        (box2[1] <= box1[1] <= box2[3]):
        
        res = 1

    return res



box1 = [-5, -5, 3, 3]
box2 = [3, 0, 6, 5]
print(doesIntersect(box1, box2))

box1 = [0, 0, 1, 1]
box2 = [2, 2, 3, 3]
print(doesIntersect(box1, box2))
