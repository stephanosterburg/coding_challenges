# Given a position of a knight on the standard chessboard, find the number of
# different moves the knight can perform.
#
# The knight can move to a square that is two squares horizontally and one
# square vertically, or two squares vertically and one square horizontally
# away from it. The complete move therefore looks like the letter L. Check
# out the image below to see all valid moves for a knight piece that is
# placed on one of the central squares.
#
# Example
#
# For cell = "a1", the output should be
# chessKnight(cell) = 2.
#
# For cell = "c2", the output should be
# chessKnight(cell) = 6.
#
#       2 3 4 4 4 4 3 2     8
#       3 4 6 6 6 6 4 3     7
#       4 6 8 8 8 8 6 4     6
#       4 6 8 8 8 8 6 4     5
#       4 6 8 8 8 8 6 4     4
#       4 6 8 8 8 8 6 4     3
#       3 4 6 6 6 6 4 3     2
#       2 3 4 4 4 4 3 2     1
#
#       A B C D E F G H
#

def chessKnight(cell):

    max_moves = 8
    border = 0
    near_border = 0

    # Check if the cell is either on the edge or next to it
    # if cell[0 ] in "ah" -> cell either letter a or h etc
    if cell[0] in "ah":
        border += 1
    if cell[1] in "18":
        border += 1
    if cell[0] in "bg":
        near_border += 1
    if cell[1] in "27":
        near_border += 1

    # We were at the border
    if border == 1 and near_border == 0:
        return 4

    # Calc steps
    max_moves -= 3 * border
    max_moves -= 2 * near_border

    return max_moves


print(chessKnight("a1"))  # 2
print(chessKnight("c2"))  # 6
print(chessKnight("d4"))
print(chessKnight("g2"))

