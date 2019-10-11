# You are given an array of desired filenames in the order of their creation.
# Since two files cannot have equal names, the one which comes later will have
# an addition to its name in a form of (k), where k is the smallest positive
# integer such that the obtained name is not used yet.
#
# Return an array of names that will be given to the files.
#
# Example
#
# For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
# fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].


def fileNaming(names):
    new_names = []

    for name in names:
        if name in new_names:
            name = add_suffix(name, new_names)

        new_names.append(name)

    return new_names


def add_suffix(name, new_names):
    count = 1
    new_name = name + "(" + str(count) + ")"

    while new_name in new_names:
        count += 1
        new_name = name + "(" + str(count) + ")"

    return new_name


print(fileNaming(["doc", "doc", "image", "doc(1)", "doc"]))
