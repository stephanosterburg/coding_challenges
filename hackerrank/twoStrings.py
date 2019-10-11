def twoStrings(s1, s2):
    return "YES" if set(s1).intersection(set(s2)) else "NO"


s1 = 'hello'
s2 = 'world'
print(twoStrings(s1, s2))
