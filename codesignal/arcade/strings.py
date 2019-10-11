def permutationCipher(password, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)

password = "iamthebest"
key = "zabcdefghijklmnopqrstuvwxy"
# print(permutationCipher(password, key)) # "hzlsgdadrs"

#-------------------------------------------------------------------------------
import textwrap

def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)

feedback = "This is an example feedback"
size = 8
# print(feedbackReview(feedback, size)) # ["This is", "an", "example", "feedback"]

#-------------------------------------------------------------------------------
def competitiveEating(t, width, precision):
    return "{0:.{1}f}".format(t, precision).center(width)

t = 29.8245
width = 10
precision = 0
# print(competitiveEating(t, width, precision)) # ("   30   ")

#-------------------------------------------------------------------------------
import re

def newStyleFormatting(s):
    return '%'.join(re.sub('%\w', '{}', part) for part in s.split('%%'))

s = "We expect the %f%% growth this week"
# print(newStyleFormatting(s)) # "We expect the {}% growth this week".

#-------------------------------------------------------------------------------
def getCommit(commit):
    return re.sub("[^a-zA-Z]", "", commit)

commit = "0??+0+!!someCommIdhsSt"
print(getCommit(commit)) # "someCommIdhsSt".
