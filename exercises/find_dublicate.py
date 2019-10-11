from collections import Counter

def get_dup(numbers):
    return [k for k, v in Counter(numbers).items() if v > 1]


my_list = [1, 2, 3, 4, 5, 2]
print(get_dup(my_list))
