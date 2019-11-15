import os


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
def isBalanced(string):
    brackets = {'{': '}', '[': ']', '(': ')'}

    if len(string) % 2 == 0:
        firstpart, secondpart = string[:len(string) // 2], string[len(string) // 2:][::-1]
        print(firstpart, secondpart)
        for i in range(len(s) // 2):
            if secondpart[i] != brackets[firstpart[i]]:
                return 'NO'

        return 'YES'


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/balanced-brackets-testcases/input/input18.txt", 'r')

    t = list(map(int, filename.readline().split()))[0]
    for t_itr in range(t):
        s = filename.readline().split()[0]
        print(isBalanced(s))
