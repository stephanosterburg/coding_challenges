import os
from collections import Counter

def checkMagazine(magazine, note):
    x = Counter(note)
    y = Counter(magazine)

    overlap = list((x & y).elements())

    if len(note) - len(overlap) > 0:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/hackerrank/ctci-ransom-note-testcases/input/input22.txt", 'r')

    mn = filename.readline().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = filename.readline().rstrip().split()
    note = filename.readline().rstrip().split()

    checkMagazine(magazine, note)
