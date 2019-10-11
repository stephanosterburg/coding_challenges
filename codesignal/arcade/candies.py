def candies(n, m):
    return m - (m % n)

n = 3
m = 10
print(candies(n, m))  # 9
