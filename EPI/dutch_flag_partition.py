# Write a function that takes an array A and an index i, and rearranges the
# elements such that all elements less than A[i] (the pivot) appear first,
# followed by elements equal to the pivot, followed by elements greater than
# the pivot
#
# Example:
# A = [0, 1, 2, 0, 2, 1, 1]
# pivot = 3
# Then A[3] = 0, so [0, 0, 1, 2, 2, 1, 1] is valid
def dutch_flag_partition(A, i):
    # This not in-place
    # t0 = [x for x in A if x < A[i]]
    # t1 = [x for x in A if x == A[i]]
    # t2 = [x for x in A if x > A[i]]
    #
    # return t0 + t1 + t2

    pivot = A[i]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
        elif A[equal] == pivot:
            equal += 1
        else: # A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]

    return A

A = [0, 1, 2, 0, 2, 1, 1]
print(dutch_flag_partition(A, 3))
