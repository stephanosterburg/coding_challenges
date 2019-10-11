def maximumPerimeterTriangle(sticks):
    found = False
    for i in range(len(sticks) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            for k in range(j - 1, -1, -1):
                if sticks[j] + sticks[k] > sticks[i]:
                    return ' '.join(str(e) for e in [sticks[k], sticks[j], sticks[i]])
                    found = True
                    break
            if found:
                break
        if found:
            break
    if not found:
        return -1


if __name__ == '__main__':
    filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/maximum-perimeter-triangle-testcases/input/input00.txt'

    with open(filename) as f:
        n = f.readline().split()
        sticks = list(map(int, f.readline().rstrip('\n').split()))

    result = maximumPerimeterTriangle(sticks)
    # print(' '.join(map(str, result)))
    print(result)
