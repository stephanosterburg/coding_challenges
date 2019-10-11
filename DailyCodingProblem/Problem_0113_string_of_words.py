# Given a string of words delimited by spaces, reverse the words in string.
# For example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation in-place?

def reverse_string(s):
    return ' '.join(list(s.split())[::-1])


s = "hello world here"
print(reverse_string(s))
