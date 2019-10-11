def sum_of_digits(n):
    current_sum = 0
    while n > 0:
        current_sum += n % 10
        n = n // 10
    return current_sum


def perfect_number(n):
    i, current = 0, 0
    while current < n:
        i += 1
        if sum_of_digits(i) == 10:
            current += 1
    return i


print(perfect_number(1))
print(perfect_number(2))
print(perfect_number(10))
