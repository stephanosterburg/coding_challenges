from itertools import groupby

# Basically I'm unpacking the list comprehension and printing each element of it.
# The list is built of elements of (len(list(c)), int(k)). len(list(c)) is simply
# the number of occurences of a character c returned by the groupby function. k is
# just the key value, the character itself.
S = "1222311"
print(*[(len(list(c)), int(k)) for k, c in groupby(S)])
