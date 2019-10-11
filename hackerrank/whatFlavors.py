# They pool together money = $4; there are five flavors avaiilable.
# The flavors 1 and 4 have a total cost of 1 + 3 = 4
#
# Print two space-separated integers denoting the respective indices for the two
# distinct flavors they choose to purchase in ascending order.
#
def whatFlavors(cost, money):
    f = []
    b = 0
    for k, v in enumerate(reversed(cost)):
        if b <= money:
            if v + b <= money:
                f.append(k + 1)
                b += v
            print(b)

    print(' '.join(str(n) for n in f))


# money = 4
# cost = [1, 4, 5, 3, 2]
# whatFlavors(cost, money) # 1 4

money = 5
cost = [1, 2, 3, 4, 5]
whatFlavors(cost, money) # 2 3
