"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString="123aa1", the output should be
longestDigitsPrefix(inputString) = "123".
"""
import re


def longestDigitsPrefix(inputString):
    # if inputString[0].isdigit():
    #     pre = len(re.match('\d*', inputString).group())
    #     return(inputString[:pre])
    # else:
    #     return ""
    
    return re.findall('^\d*', inputString)[0]



print(longestDigitsPrefix("0123456789"))  # 0123456789
print(longestDigitsPrefix("123aa1"))  # 123
print(longestDigitsPrefix("  3) always check for whitespaces"))  # Empty
print(longestDigitsPrefix("12abc34"))  # 12
print(longestDigitsPrefix("the output is 42"))  # Empty
