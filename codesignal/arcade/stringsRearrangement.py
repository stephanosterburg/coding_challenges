# Given an array of equal-length strings, check if it is possible to rearrange the strings
# in such a way that after the rearrangement the strings at consecutive positions would
# differ by exactly one character.
#
# Example
#
# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false.
#
# All rearrangements don't satisfy the description condition.
#
# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.
#
# Strings can be rearranged in the following way: "aa", "ab", "bb".


from itertools import permutations


def diffLetters(first_string, second_string):
    # create a letter pair
    letter_pairs = zip(first_string, second_string)
    # compare letter pair
    misses = (a != b for (a, b) in letter_pairs)
    # return True if sum(misses) == 1 else False
    if sum(misses) == 1:
        return True
    else:
        return False


def stringsRearrangement(inputArray):
    # create all possible orderings
    arrangements = permutations(inputArray)

    for current_arrangement in arrangements:
        # create string pairs where second input doesn't start with first letter
        string_comparisons = zip(current_arrangement, current_arrangement[1:])
        # compare letters and return a true/false pair
        comparison_results = (diffLetters(a, b) for (a, b) in string_comparisons)
        if all(comparison_results):
            return True
    return False


print(stringsRearrangement(["aba", "bbb", "bab"]))
print(stringsRearrangement(["ab", "bb", "aa"]))


