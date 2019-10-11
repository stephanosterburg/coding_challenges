"""
You are given an array of integers representing coordinates of obstacles
situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right.
You are allowed only to make jumps of the same length represented by some
integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.

[19, 32, 11, 23] = 3 -> [11, 19, 23, 32]
[1000, 999] = 6
[5, 8, 9, 13, 14] = 6

[    1, 2,    4,    6,          10] = 7
[ 0,     , 3,  , 5,  , 7, 8, 9,   ]
[ 0  .  .  .  .  .  .  7  .  .   .
"""

def avoidObstacles(inputArray):
    # inputArray.sort()
    #
    # # step size to jump - set to max 100000 because codesight didn't like the smaller numbers
    # for i in range(2, 1000000):
    #     t = True
    #     for n in inputArray:
    #         t = t and (n % i != 0)  # check if number in array can be divided by step size i
    #
    #     if t:
    #         return i

    count = 2
    while True:
        if sorted([i % count for i in inputArray])[0] > 0:
            return count

        count += 1


print(avoidObstacles([19, 32, 11, 23]))
print(avoidObstacles([1000, 999]))
print(avoidObstacles([5, 3, 6, 7, 9]))
