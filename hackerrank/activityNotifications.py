import os
import math
import statistics

# Given the number of trailing days d and a client's total daily expenditures
# for a period of n days, find and print the number of times the client will
# receive a notification over all n days.
#
# For example, d=3 and expenditure=[10,20,30,40,50]. On the first three days,
# they just collect spending data. At day 4, we have trailing expenditures
# of [10,20,30]. The median is 20 and the day's expenditure is 40.
# Because 40>=2x20, there will be a notice. The next day, our trailing
# expenditures are [20,30,40] and the expenditures are 50. This is less than
# 2x30 so no notice will be sent. Over the period, there was one notice sent.

# def median(lst):
#     n = len(lst)
#     s = sorted(lst)
#     return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None
#
# 4 thoughts that may help:
# 1.) Counting sort
# 2.) A Queue
# 3.) Pay attention to the even case.
# 4.) Integer division is a blessing and a curse, be careful.
#
# Your code did not execute within the time limits :-(
#
def activityNotifications(expenditure, d):
    count = 0
    r = len(expenditure) - d
    for i in range(r):
        m = statistics.median(expenditure[i:i+d])
        # print(expenditure[i:i+d])
        # print('median: {}'.format(m))
        # print('next : {}\n'.format(expenditure[i+d]))

        if m * 2 <= expenditure[i + d]:
            count += 1

    return count

if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/fraudulent-activity-notifications-testcases/input/input14.txt", 'r')
    d = list(map(int, filename.readline().split()))[1]
    expenditure = list(map(int, filename.readline().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
