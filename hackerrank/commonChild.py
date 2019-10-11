def commonChild(s1, s2):
    lengths = [[0] * int(len(s2)+1)] * int(len(s1)+1)

    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    return lengths[-1][-1]


s1 = 'SHINCHAN'
s2 = 'NOHARAAA'
print(commonChild(s1, s2))
