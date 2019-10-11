# Complete the solution so that it splits the string into pairs of
# two characters. If the string contains an odd number of characters
# then it should replace the missing second character of the final
# pair with an underscore ('_').
#
# Examples:
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']
import re


def solution(s):
    result = []
    for i in range(0, len(s), 2):
        if len(str(s[i : i + 2])) == 1:
            result.append(s[i : i + 2] + "_")
        else:
            result.append(s[i : i + 2])

    return result

    # we can use regular expression
    # return re.findall('.{2}', s + '_')


print(solution("abc"))  # ['ab', 'c_']
print(solution("abcdef"))  # ['ab', 'cd', 'ef']
print(solution("asdfadsf"))  # ['as', 'df', 'ad', 'sf']
print(solution("asdfads"))  # ['as', 'df', 'ad', 's_']
print(solution(""))  # []
print(solution("x"))  # ['x_']
