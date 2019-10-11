def cont_list(num, k):
    result = []
    # print(str(k) + '\n')
    for i in range(len(num)):
        for j, v in enumerate(num[i:]):
            result.append(v)
            if sum(result) == k:
                return result
            elif j == len(num)-1:
                result = []

my_list = [1, 2, 3, 4, 5]
K = 9
print(cont_list(my_list, K))
