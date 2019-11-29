import os


# Sample Input
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3
#
# Sample Output
# 1 4
# 1 2
#
# They pool together money = $4; there are five flavors avaiilable.
# The flavors 1 and 4 have a total cost of 1 + 3 = 4
#
# Print two space-separated integers denoting the respective indices for the two
# distinct flavors they choose to purchase in ascending order.
#
def whatFlavors(cost: list, money: int):
    cost_dict = {}
    for k, v in enumerate(cost):
        if money - v in cost_dict:
            print(str(cost_dict[money - v] + 1) + ' ' + str(k + 1))
            return
        else:
            cost_dict[v] = k


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/ctci-ice-cream-parlor-testcases/input/input14.txt", 'r')

    t = list(map(int, filename.readline().split()))[0]
    for t_itr in range(t):
        money = int(filename.readline().split()[0])
        n = filename.readline().split()[0]
        cost = list(map(int, filename.readline().rstrip().split()))

        whatFlavors(cost, money)
