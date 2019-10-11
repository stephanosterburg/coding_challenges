class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.value = x


def inOrder(root):
    if root:
        return inOrder(root.left), root.value, inOrder(root.right)
    else:
        return []


def preOrder(root):
    if root:
        return root.value, preOrder(root.left), preOrder(root.right)
    else:
        return []


def postOrder(root):
    if root:
        return postOrder(root.left), postOrder(root.right), root.value
    else:
        return []


# Given binary tree [3,9,20,null,null,15,7]
#   3
#  / \
# 9  20
#   /  \
#  15   7
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
def levelOrder(self, root):
    """
    :type root: Node
    :rtype: List[List[int]]
    """
    result = []

    if not root:
        return result

    curr_level = [root]
    while curr_level:
        level_result = []
        next_level = []

        for curr in curr_level:
            level_result.append(curr.value)
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)

        result.append(level_result)
        curr_level = next_level

    return result


def maxDepth(self, root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


def isSymmetric(self, root: TreeNode) -> bool:
    def isMirror(left, right):
        if left is None or right is None:
            return left == None and right == None

        return (
            left.value == right.value
            and isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    return isMirror(root, root)


def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if root == None:
        return False
    else:
        current = root
        result = []
        result.append(current)
        result.append(current.value)

        while result != []:
            pathsum = result.pop()
            current = result.pop()

            if not current.left and not current.right:
                if pathsum == sum:
                    return True

            if current.right:
                r_pathsum = pathsum + current.right.value
                result.append(current.right)
                result.append(r_pathsum)

            if current.left:
                l_pathsum = pathsum + current.left.value
                result.append(current.left)
                result.append(l_pathsum)

        return False
