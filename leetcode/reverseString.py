# Recursion is an approach to solving problems using a function that calls itself as a subroutine.
#
# You might wonder how we can implement a function that calls itself. The trick is that each time
# a recursive function calls itself, it reduces the given problem into subproblems. The recursion
# call continues until it reaches a point where the subproblem can be solved without further recursion.
#
# A recursive function should have the following properties so that it does not result in an infinite loop:
#
# A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.
# A set of rules, also known as recurrence relation that reduces all other cases towards the base case.
# Note that there could be multiple places where the function may call itself.

# Do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory.

def reverseString(s):
    return [s[-1]] + reverseString(s[:-1]) if s else []
# class Solution:
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: void Do not return anything, modify s in-place instead.
#         """
#
#         def helper(start, end, ls):
#             if start >= end:
#                 return
#
#             # swap the first and last element
#             ls[start], ls[end] = ls[end], ls[start]
#
#             return helper(start + 1, end - 1, ls)
#
#         helper(0, len(s) - 1, s)

char1 = ["h","e","l","l","o"]  # Output: ["o","l","l","e","h"]
print(reverseString(char1))

char2 = ["H","a","n","n","a","h"]  # Output: ["h","a","n","n","a","H"]
print(reverseString(char2))


