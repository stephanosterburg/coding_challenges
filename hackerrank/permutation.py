from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations

filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/itertools-permutations-testcases/input/input00.txt'
print('\npermutations \n')
S, number = ["HACK", 2]
mylist = sorted(list(permutations(S, int(number))))
for _ in mylist:
    print(''.join(_))

print('\ncombinations \n')
S, number = ["ABCD", 3]
for i in range(1, int(number) + 1):
    c = sorted(list(combinations(sorted(S), i)))
    for _ in c:
        print(''.join(_))

print('\ncombinations_with_replacement \n')
S, number = ["HACK", 2]
for c in list(combinations_with_replacement(sorted(S), number)):
    print(''.join(c))
