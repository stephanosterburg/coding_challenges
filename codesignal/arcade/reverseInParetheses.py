"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""
# from pyparsing import nestedExpr
#
#
# def reverseInParentheses(inputString):
#     if not inputString.startswith('('):
#         inputString = '(' + inputString + ')'
#
#     expr = nestedExpr('(', ')')
#     print(expr.)
#     result = expr.parseString(inputString).asList()[0]
#
#     new_string = []
#     for s in result:
#         if type(s) is list:
#             new_string.append(s[0][::-1])
#         else:
#             new_string.append(s)
#
#     return ''.join(new_string)


from collections import Counter


def reverseInParentheses(s):
    # # Counter returns number of times '(' appears in s
    # while range(Counter(s)['(']):
    #     # split at the right most '('
    #     one = s.rsplit('(', 1)
    #
    #     # split at the first ')'
    #     two = one[1].split(')', 1)
    #
    #     # one[0] ADD the reverse of two[0] PLUS two[1]
    #     s = one[0] + two[0].replace(two[0], two[0][::-1] + two[1])
    #
    # return s

    # Short and Simple
    return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')


s = "foo(bar)baz(blim)"
print(reverseInParentheses(s))

s = "foo(bar(baz))blim"
print(reverseInParentheses(s))
