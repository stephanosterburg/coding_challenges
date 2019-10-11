"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""
def commonCharacterCount(s1, s2):
    string_dict1 = {i: s1.count(i) for i in "".join(set(s1))}
    string_dict2 = {i: s2.count(i) for i in "".join(set(s2))}

    num = 0
    for k in string_dict1:
        if k in string_dict2:
            if string_dict1[k] > string_dict2[k]:
                num += string_dict2[k]
            else:
                num += string_dict1[k]

    return num


s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))
