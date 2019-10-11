#!/bin/python3

# Each contest is described by two integers, L[i] and T[i]:
#
# - L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will
#        decrease by L[i]; if she loses it, her luck balance will increase by L[i].
# - T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal
#        to 0 if it's unimportant.
# If Lena loses no more than k important contests, what is the maximum amount of luck she can have after
# competing in all the preliminary contests? This value may be negative.
#
# For example, k=2 and:
#
# Contest		L[i]	T[i]
# 1		        5	    1
# 2		        1	    1
# 3		        4	    0
# If Lena loses all of the contests, her will be 5 + 1 + 4 = 10. Since she is allowed to lose 2 important contests,
# and there are only  important contests. She can lose all three contests to maximize her luck at 10. If k = 1, she
# has to win at least 1 of the 2 important contests. She would choose to win the lowest value important contest
# worth 1. Her final luck will be 5 + 4 - 1 = 8.
#
# Sample Input
# 6  3
# 5  1
# 2  1
# 1  1
# 8  1
# 10 0
# 5  0
#
# Sample Output
# 29
#
# Explanation
#
# There are n=6 contests. Of these contests, 4 are important and she cannot lose more than k=3 of them.
# Lena maximizes her luck if she wins the 3rd important contest (where L[i]=1) and loses all of the other
# five contests for a total luck balance of 5+2+8+10-5-1=29.
def luckBalance(k, contests):
    balance = 0
    more_important = []
    for i in range(len(contests)):
        li, ti = contests[i]
        if ti == 0:
            balance += li
        else:
            more_important.append(li)

    more_important.sort()

    if len(more_important) > k:
        for i in range(len(more_important) - k):
            balance -= more_important[i]
        for i in range(len(more_important) - k, len(more_important)):
            balance += more_important[i]
    elif len(more_important) <= k:
        for i in range(len(more_important)):
            balance += more_important[i]

    return balance


if __name__ == '__main__':
    filename = '/Users/stephanosterburg/Projects/practice-coding/hackerrank/luck-balance-testcases/input/input00.txt'

    with open(filename) as f:
        nk = f.readline().split()
        n = int(nk[0])
        k = int(nk[1])

        contests = [list(map(int, line.rstrip('\n').split())) for line in f]

    print(luckBalance(k, contests))
