# A string is said to be a special string if either of two conditions is met:
#
# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
def substrCount(n, s):
    s = list(s)
    count = len(s)

    for i in range(1, len(s)-1):
        if s[i-1] == s[i+1]:
            count += 1

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1

    if len(set(s)) == 1:
        count += 1

    return count



n = 7
s = 'abcbaba'
print(substrCount(n, s))  # 10
# The special palindromic substrings of
# s = abcbaba -> {a, b, c, b, a, b, a, bcb, bab, aba}
