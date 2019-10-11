# You are planning production for an order. You have a number of machines that
# each have a fixed number of days to produce an item. Given that all the
# machines operate simultaneously, determine the minimum number of days to
# produce the required order.

# For example, you have to produce goal = 10 items. You have three machines
# that take machines = [2, 3, 2] days to produce an item. The following is a
# schedule of items produced:
# Day Production  Count
# 2   2               2
# 3   1               3
# 4   2               5
# 6   3               8
# 8   2              10
#
# It takes 8 days to produce 10 items using these machines.
#
def minTime(machines, goal):
    min_time = goal * min(machines) // len(machines)
    max_time = goal * max(machines) // len(machines) + 1

    while min_time < max_time:
        days = (min_time + max_time) // 2
        produced = sum([days // machine for machine in machines])

        if produced >= goal:
            max_time = days
        else:
            min_time = days + 1

    return min_time




# In 7 minutes, M0 can produce 7 items, M1 can produce 2 items and M2 can
# produce 1 item, which totals up to 10.
goal = 10  # items
machines = [1, 3, 4]  # minutes per machine
print(minTime(machines, goal)) # 7 minutes
