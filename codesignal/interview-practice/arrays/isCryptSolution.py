"""
A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence 
between letters and digits, such that the given arithmetic equation consisting of letters 
holds true when the letters are converted to digits.

You have an array of strings crypt, the cryptarithm, and an array containing the 
mapping of letters and digits, solution. The array crypt will contain three non-empty 
strings that follow the structure: [word1, word2, word3], which should be interpreted 
as the word1 + word2 = word3 cryptarithm.

If crypt, when it is decoded by replacing all of the letters in the cryptarithm with 
digits using the mapping in solution, becomes a valid arithmetic equation containing 
no numbers with leading zeroes, the answer is true. If it does not become a valid 
arithmetic solution, the answer is false.

Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

Example

For crypt = ["SEND", "MORE", "MONEY"] and
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
the output should be isCryptSolution(crypt, solution) = true.

When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, 
you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

For crypt = ["TEN", "TWO", "ONE"] and
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
the output should be isCryptSolution(crypt, solution) = false.
"""
from typing import Dict, Any, Tuple


def isCryptSolution(crypt, solution):
    tabl: Dict[int, Any] = str.maketrans(dict(solution))  # -> {65: '0'} https://stackoverflow.com/a/41536036/5983691
    tubl: Tuple[Any, ...] = tuple(s.translate(tabl) for s in crypt)  # -> ('0', '0', '0')
    zeroes = any(s[0] == '0' for s in tubl if len(s) > 1)
    return not zeroes and int(tubl[0]) + int(tubl[1]) == int(tubl[2])


crypt = ["A", "A", "A"]
solution = [["A", "0"]]
print(isCryptSolution(crypt, solution)) 

# crypt = ["AA", "BB", "AA"]
# solution = [["A","1"], ["B","0"]]
# print(isCryptSolution(crypt, solution)) 

# crypt = ["WASD", "IJKL", "AOPAS"]
# solution = [["W","2"], 
# 			["A","0"], 
# 			["S","4"], 
# 			["D","1"], 
# 			["I","5"], 
# 			["J","8"], 
# 			["K","6"], 
# 			["L","3"], 
# 			["O","7"], 
# 			["P","9"]]
# print(isCryptSolution(crypt, solution)) 

# crypt = ["SEND", "MORE", "MONEY"]
# solution = [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]
# print(isCryptSolution(crypt, solution))

# crypt = ["TEN", "TWO", "ONE"]
# solution = [['O', '1'],
#             ['T', '0'],
#             ['W', '9'],
#             ['E', '5'],
#             ['N', '4']]   
# print(isCryptSolution(crypt, solution)) 
