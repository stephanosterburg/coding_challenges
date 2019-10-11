filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/nested-list-testcases/input/input00.txt'

with open(filename) as f:
    lines = [line.rstrip('\n') for line in f]
    print(int(lines[0]))

mylist = []
for i in range(1, len(lines), 2):
    mylist.append([lines[i], float(lines[i+1])])
# print(mylist)

# Get second highest value
second_highest = sorted(list(set([notes for name, notes in mylist])))[1]
# Print names with second highest valeus
print('\n'.join([a for a, b in sorted(mylist) if b == second_highest]))
