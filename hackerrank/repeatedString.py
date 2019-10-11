# Lilah has a string, , of lowercase English letters that she repeated
# infinitely many times.
#
# Given an integer, , find and print the number of letter a's in the first
# letters of Lilah's infinite string.
#
# For example, if the string  and , the substring we consider is , the first
# characters of her infinite string. There are  occurrences of a in the substring.

def repeat_string(s, n):
    if len(s) == 1 and s == 'a':
        return n

    if 'a' in s:
        a  = s.count('a')
        m = n // len(s)=
        d = n - (m * len(s))
        return (m * a) + s[:d].count('a')
    else:
        return 0

# s = 'aba'
# n = 10
# print(repeat_string(s, n))  # 7
#
# s = 'a'
# n = 1000000000000
# print(repeat_string(s, n))
#
# s = 'aab'
# n = 882787
# print(repeat_string(s, n))  # 588525

s = 'udjlitpopjhipmwgvggazhuzvcmzhulowmveqyktlakdufzcefrxufssqdslyfuiahtzjjdeaxqeiarcjpponoclynbtraaawrps'
n = 872514961806
print(repeat_string(s, n))  # 69801196944
