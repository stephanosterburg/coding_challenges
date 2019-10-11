def jumpingOnClouds(c):
    keys = [k for k, v in enumerate(c) if v == 0]

    count = 0
    previous = keys[0]
    for k, v in enumerate(keys[1:]):
        if previous + 1 == v and count == 0:
            count = 1
        elif previous + 1 == v and count == 1:
            keys.remove(v)
            count = 0
        else:
            count = 0

        previous = v

    return len(keys)-1


c = [0, 0, 1, 0, 0, 1, 0]
print(jumpingOnClouds(c))
