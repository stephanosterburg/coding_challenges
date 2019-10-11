"""
Given the positions of a white bishop and a black pawn on the standard
chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited
to diagonal movement. Check out the example below to see how it can move:

Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.
"""
def bishopAndPawn(bishop, pawn):
    # We could use a dict to map A-H but we can use the ord function instead
    # cols = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
    #
    # x1 = ord(bishop[0])
    # y1 = int(bishop[1])
    #
    # x2 = ord(pawn[0])
    # y2 = int(pawn[1])
    #
    # # Here we check if the movement is diagonal
    # # eg: a1 = 0, 0; c3 = 3, 3 ->
    # #   0 +  3 ==  0 + 3  or  0 - 3  ==  0 -  3
    # if x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
    #     return True
    #
    # return False

    # Short and Simple
    b = [ord(bishop[0]), int(bishop[1])]
    p = [ord(pawn[0]), int(pawn[1])]

    return b[1] - b[0] == p[1] - p[0] or sum(b) == sum(p)


print(bishopAndPawn("a1", "c3"))  # true
print(bishopAndPawn("h1", "h3"))  # false
