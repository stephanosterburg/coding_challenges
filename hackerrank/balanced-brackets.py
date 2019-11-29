import os


# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
#
# Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the
# left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs
# of brackets: [], {}, and ().
#
# A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example,
# {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets
# encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced
# closing square bracket, ].
#
# By this logic, we say a sequence of brackets is balanced if the following conditions are met:
#
# It contains no unmatched brackets.
# The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
# Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced,
#
# return YES. Otherwise, return NO.
# Input Format
# The first line contains a single integer n, the number of strings.
# Each of the next n lines contains a single string s, a sequence of brackets.
#
# Sample Input
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}
#
# Sample Output
# YES
# NO
# YES
#
def is_balanced(string):
    brackets = []
    valid = True

    for char in string:
        if char == ')':
            if not brackets or brackets[-1] != '(':
                valid = False
                break
            else:
                brackets.pop()
        elif char == ']':
            if not brackets or brackets[-1] != '[':
                valid = False
                break
            else:
                brackets.pop()
        elif char == '}':
            if not brackets or brackets[-1] != '{':
                valid = False
                break
            else:
                brackets.pop()
        else:
            brackets += [char]

    return "YES" if valid and not brackets else "NO"


if __name__ == '__main__':
    pwd = os.getcwd()
    # input18 -> YES NO YES
    # input19 -> YES NO
    # input20 -> YES NO YES
    filename = open(pwd + "/balanced-brackets-testcases/input/input18.txt", 'r')

    t = list(map(int, filename.readline().split()))[0]
    for t_itr in range(t):
        s = filename.readline().split()[0]
        print(is_balanced(s))
