filename = './python-lists-testcases/input/input00.txt'

with open(filename) as f:
    lines = [line.rstrip('\n') for line in f]
    # print(int(lines[0]))

mylist = []
for i in range(1, len(lines)):
    command = lines[i].split()
    if command[0] == 'insert':
        mylist.insert(int(command[1]), int(command[2]))
    elif command[0] == 'print':
        print(mylist)
    elif command[0] == 'remove':
        mylist.remove(int(command[1]))
    elif command[0] == 'append':
        mylist.append(int(command[1]))
    elif command[0] == 'sort':
        mylist.sort()
    elif command[0] == 'pop':
        mylist.pop()
    elif command[0] == 'reverse':
        mylist.reverse()
