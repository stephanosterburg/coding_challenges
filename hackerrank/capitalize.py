def solve(s):
    for c in s.split():
        s = s.replace(c, c.capitalize())

    return s


string = '1 w 2 r 3g'
print(solve(string))
