"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""
def addBorder(picture):
    border = []
    char = '*'

    l = len(picture[0]) + 2
    b = str(char * l)

    border.insert(0, b)

    for i in picture:
        string = char + i + char
        border.append(string)

    border.append(b)
    return border


picture = ["abc",
           "ded"]
print(addBorder(picture))
