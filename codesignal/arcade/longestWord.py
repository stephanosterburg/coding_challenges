# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
#
# Example
#
# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".
import re


def longestWord(text):
    lgth = 0
    longest = ""
    string = re.sub(r'[^a-zA-Z]+', ' ', text).split()
    for i in string:
        if len(i) > lgth:
            lgth = len(i)
            longest = i

    return longest


print(longestWord("Ready, steady, go!"))