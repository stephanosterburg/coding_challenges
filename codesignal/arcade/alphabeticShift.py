# Given a string, replace each its character by the next one in the English alphabet
# (z would be replaced by a).
#
# Example
#
# For inputString = "crazy", the output should be
# alphabeticShift(inputString) = "dsbaz".

name = "crazy"
string = ""

for i in range(0, len(name)):
    s = ord(name[i]) + 1
    if s > 122:
        s = 97
    letter = chr(s)
    string += letter

print(string)

