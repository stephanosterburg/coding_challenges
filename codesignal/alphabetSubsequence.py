import string


def alphabetSubsequence(s):
    seen = -1
    for i in s:
        index = string.ascii_lowercase.find(i)
        if index > seen:
            seen = index
        else:
            return False
    return True


s = "effg"
print(alphabetSubsequence(s))
