"""
A string is said to be beautiful if b occurs in it no more times than a;
c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be
isBeautifulString(inputString) = true;

For inputString = "aabbb", the output should be
isBeautifulString(inputString) = false;

For inputString = "bbc", the output should be
isBeautifulString(inputString) = false.
"""
import string

def isBeautifulString(inputString):
    # letters = sorted(set(inputString))
    #
    # num = inputString.count('a')
    # on = ord('a')
    #
    # if len(letters) == 1:
    #     return False if ord(letters[0]) > on else True
    #
    # for l in letters[1:]:
    #     if ord(l) - 1 == on:
    #         on = ord(l)
    #         if inputString.count(l) > num:
    #             return False
    #         else:
    #             num = inputString.count(l)
    #     else:
    #         return False
    #
    # return True

    # Short and Simple
    r = [inputString.count(i) for i in string.ascii_lowercase]

    return r[::-1] == sorted(r)


print(isBeautifulString("bbbaacdafe"))
print(isBeautifulString("aabbb"))
print(isBeautifulString("bbc"))
print(isBeautifulString("zzz"))
print(isBeautifulString("bba"))
print(isBeautifulString("abcdefghijklmabcdefghijklmnpnopqrstuvwxyzz"))  # False
