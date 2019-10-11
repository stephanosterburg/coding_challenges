"""
Some people are standing in a row in a park. There are trees between them
which cannot be moved. Your task is to rearrange the people by their heights
in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""
def sortByHeight(a):
    # string_dict = {i: val for i, val in enumerate(a)}
    # # {0: -1, 1: 150, 2: 190, 3: 170, 4: -1, 5: -1, 6: 160, 7: 180}
    #
    # a.sort() #[-1, -1, -1, 150, 160, 170, 180, 190]
    #
    # while -1 in a:
    #     a.remove(-1) # removes all -1
    #
    # b = []
    # j = 0
    # for i, val in string_dict.items():
    #     if val == -1:
    #         b.append(val)
    #     else:
    #         b.append(a[j])
    #         j += 1
    #
    # return b

    # Short and Simple
    l = sorted([i for i in a if i > 0])
    for k, v in enumerate(a):
        if v == -1:
            l.insert(k, v)
    return l


a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))  # [-1, 150, 160, 170, -1, -1, 180, 190]
