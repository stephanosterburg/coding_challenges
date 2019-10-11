#sequence = [40, 50, 60, 10, 20, 30]
#sequence = [1, 1]
#sequence = [1, 3, 2, 1]
sequence = [1, 3, 2]


# def first_bad_pair(sequence):
#     """Return the first index of a pair of elements where the earlier
#     element is not less than the later elements. If no such pair
#     exists, return -1."""
#     print(sequence)
#     for i in range(len(sequence)-1):
#         if sequence[i] >= sequence[i+1]:
#             print(i)
#             return i
#     return -1
#
# def almostIncreasingSequence(sequence):
#     """Return whether it is possible to obtain a strictly increasing
#     sequence by removing no more than one element from the array."""
# j = first_bad_pair(sequence)
#
# if j == -1:
#     print("true1")  # List is increasing
#
# if first_bad_pair(sequence[j-1:j] + sequence[j+1:]) == -1:
#     print("true2")  # Deleting earlier element makes increasing
#
# if first_bad_pair(sequence[j:j+1] + sequence[j+2:]) == -1:
#     print("true3")  # Deleting later element makes increasing
#
# print("False")

for i, x in enumerate(sequence):
    s = sequence[:i]
    s.extend(sequence[i + 1:])
    if s == sorted(set(s)):
        print("True")