# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# Tower block is represented as *
#
# Python: return a list;
def tower_builder(n_floors):
    pyramid = []
    for i in range(1, 2 * n_floors, 2):
        pyramid.append("{:^{}}".format("*" * i, (2 * n_floors) - 1))

    return pyramid


print(tower_builder(1))  # ['*', ]
print(tower_builder(2))  # [' * ', '***']
print(tower_builder(3))  # ['  *  ', ' *** ', '*****']
