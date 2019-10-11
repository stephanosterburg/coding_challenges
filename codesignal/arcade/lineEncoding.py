# Given a string, return its encoding defined as follows:
#
# * First, the string is divided into the least possible number
#   of disjoint substrings consisting of identical characters
#   for example, "aabbbc" is divided into ["aa", "bbb", "c"]
# * Next, each substring with length greater than one is replaced
#   with a concatenation of its length and the repeating character
#   for example, substring "bbb" is replaced by "3b"
# * Finally, all the new strings are concatenated together in the
#   same order and a new string is returned.

# Example
#
# For s = "aabbbc", the output should be
# lineEncoding(s) = "2a3bc".


def lineEncoding(s):
    count = 1
    string = ""

    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
        else:
            if count == 1:
                string += s[i - 1]
            else:
                string += str(count) + s[i-1]
            count = 1

    if count == 1:
        string += s[i]
    else:
        string += str(count) + s[i]

    return string


print(lineEncoding("aabbbc"))
print(lineEncoding("abbcabb"))  # "a2bca2b"
print(lineEncoding("wwwwwwwawwwwwww"))  # "7wa7w"
print(lineEncoding("ccccccccccccccc"))