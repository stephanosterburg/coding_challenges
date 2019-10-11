# The first line contains an integer , the number of test cases.
#
# Each of the next  pairs of lines are as follows:
# - The first line contains an integer , the number of people
#   in the queue
# - The second line has  space-separated integers describing
#   the final state of the queue.
#
def minimumBribes(q):
    moves = 0
    for key, value in enumerate(q):
        # print(value-1, key)
        # Check if current value has a larger step size then 2
        if (value-1) - key > 2:
            print("Too chaotic")
            return

        for i in range(max(0, value-2), key):
            if q[i] > value:
                moves += 1

    print(moves)


q = '2 1 5 3 4'
q = list(map(int, q.rstrip().split()))
print(minimumBribes(q))

q = '2 5 1 3 4'
q = list(map(int, q.rstrip().split()))
print(minimumBribes(q))
