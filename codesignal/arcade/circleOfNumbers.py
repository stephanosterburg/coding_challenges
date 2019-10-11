# Consider integer numbers from 0 to n - 1 written down along the circle in
# such a way that the distance between any two neighboring numbers is equal
# (note that 0 and n - 1 are neighboring, too).
#
# Given n and firstNumber, find the number which is written in the radially
# opposite position to firstNumber.
#
# Example
#
# For n = 10 and firstNumber = 2, the output should be
# circleOfNumbers(n, firstNumber) = 7.

def circleOfNumbers(n, firstNumber):
    # keys = [i for i in range(1, n)]
    # values = keys[::-1]
    # d = dict(zip(keys, values))
    # print(d)
    # return d[firstNumber]
    return (firstNumber + n / 2) % n


n = 10
firstNumber = 2
print(circleOfNumbers(n, firstNumber))  # 7

n = 10
firstNumber = 7
print(circleOfNumbers(n, firstNumber))  # 2

n = 4
firstNumber = 1
print(circleOfNumbers(n, firstNumber))  # 3

n = 6
firstNumber = 3
print(circleOfNumbers(n, firstNumber))  # 0
