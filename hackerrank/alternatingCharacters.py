
# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    s = list(s)
    p = s[0]
    count = 0
    print(s[1:])
    for c in s[1:]:
        if c == p:
            count += 1
        else:
            p = c

    return count



s = 'AAABBB'
print(alternatingCharacters(s))

s = 'ABABABAB'
print(alternatingCharacters(s))
