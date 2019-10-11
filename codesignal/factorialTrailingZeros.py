n = 29
factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print(str(factorial)[::-1])

count = 0
for s in str(factorial)[::-1]:
    if s == '0':
        count += 1
    else:
        break

print(count)
