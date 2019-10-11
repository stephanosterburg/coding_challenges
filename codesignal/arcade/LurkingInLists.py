def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)

    # res = [*lst1, *lst2]
    #
    return res


lst1 = [2, 2, 1]
lst2 = [10, 11]
# print(listsConcatenation(lst1, lst2)) # [2, 2, 1, 10, 11].

#-------------------------------------------------------------------------------
def twoTeams(students):
    return sum(students[0::2]) - sum(students[1::2])


students = [1, 11, 13, 6, 14]
# print(twoTeams(students)) # 11

# Students with numbers 1, 13 and 14 will join team A, and students with
# numbers 11 and 6 will join team B. Thus, the answer is
# (1 + 13 + 14) - (11 + 6) = 11.

#-------------------------------------------------------------------------------
def removeTasks(k, toDo):
    del toDo[k - 1::k]
    return toDo

k = 3
toDo = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]
print(removeTasks(k, toDo)) #  [1237, 2847, 2947, 1, 374827, 22]

#-------------------------------------------------------------------------------
def printList(lst):
    return "This is your list: {}".format(lst)

lst = [1, 2, 3, 4, 5], the output should be
printList(lst) = "This is your list: [1, 2, 3, 4, 5]"
