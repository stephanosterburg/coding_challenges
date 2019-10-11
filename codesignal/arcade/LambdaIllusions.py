repeatChar = lambda ch, n: ch * n

ch = '*'
n = 20
# print(repeatChar(ch, n))  # "********************".

#-------------------------------------------------------------------------------
def getPoints(answers, p):
    questionPoints = lambda i, ans: (i + 1) if ans else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res


# answers = [true, true, false, true]
p = 2
# print(getPoints(answers, p)) #  5. Here's why: 1 + 2 - 2 + 4 = 5.

#-------------------------------------------------------------------------------
def sortStudents(students):
    students.sort(key=lambda s: s.split()[-1])
    return students

students = ["John Smith", "Jacky Mon Simonoff",
            "Lucy Smith", "Angela Zimonova"]

# print(sortStudents(students))
# ["Jacky Mon Simonoff", "John Smith", "Lucy Smith", "Angela Zimonova"]

#-------------------------------------------------------------------------------
def isTestSolvable(ids, k):
    digitSum = lambda x: sum(map(int, str(x)))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)

    return sm % k == 0

ids = [529665, 909767, 644200]
k = 3
print(isTestSolvable(ids, k)) # true.

# The sum of digits is
# (5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87
# which is divisible by 3. Today is your lucky day after all!

#-------------------------------------------------------------------------------
