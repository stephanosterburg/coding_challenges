# Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
#
# Example
#
# For n = 152, the output should be
# deleteDigit(n) = 52;
# For n = 1001, the output should be
# deleteDigit(n) = 101.


def deleteDigit(n):
    num = 0

    s = str(n)
    for i in range(len(s)):
        if int(s[:i] + s[i + 1:]) > num:
            num = int(s[:i] + s[i + 1:])

    return num


print(deleteDigit(1001))
print(deleteDigit(152))

