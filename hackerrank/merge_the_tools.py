import math
import os
import random
import re
import sys

def merge_the_tools(string, k):
    strings = [string[i:i + k] for i in range(0, len(string), k)]

    for string in strings:
        letters = ''
        for ch in string:
            if ch in letters:
                continue
            else:
                letters += ch

        print(letters)


if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/merge-the-tools-testcases/input/input01.txt", 'r')
    # Expected Output
    # KYQTWXDLINFBHRGZVCUSAMOEPJ
    # YUGTZIWNVSALBXOCDMPFEKJRQH

    string = filename.readline().split()[0]
    k = list(map(int, filename.readline().split()))[0]

    # string, k = input(), int(input())
    merge_the_tools(string, k)