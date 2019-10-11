"""
Given a string s consisting of small English letters, find and return the first instance 
of a non-repeating character in it. If there is no such character, return '_'.

Example
For s = "abacabad", the output should be
firstNotRepeatingCharacter(s) = 'c'.

There are 2 non-repeating characters in the string: 'c' and 'd'. 
Return c since it appears in the string first.
"""
from collections import Counter

def firstNotRepeatingCharacter(s):
	dup = [item for item, count in Counter(s).items() if count > 1]
	new_list = [l for l in list(s) if l not in dup]

	if len(new_list) > 0:
		return new_list[0]
	else:
		return '_'

s = "abacabad"
print(firstNotRepeatingCharacter(s))

s = "abacabaabacaba"
print(firstNotRepeatingCharacter(s))

s = "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"
print(firstNotRepeatingCharacter(s))

s = "xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc"
print(firstNotRepeatingCharacter(s))  # d


