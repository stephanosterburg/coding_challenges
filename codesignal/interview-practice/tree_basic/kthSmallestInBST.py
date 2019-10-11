"""
A tree is considered a binary search tree (BST) if for each of its nodes the following is true:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and the right subtrees must also be binary search trees.
Given a binary search tree t, find the kth smallest element in it.

Note that kth smallest element means kth element in increasing order. 
See examples for better understanding.

Example

For

t = {
    "value": 3,
    "left": {
        "value": 1,
        "left": null,
        "right": null
    },
    "right": {
        "value": 5,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 6,
            "left": null,
            "right": null
        }
    }
}
and k = 4, the output should be
kthSmallestInBST(t, k) = 5.

Here is what t looks like:

   3
 /   \
1     5
     / \
    4   6
The values of t are [1, 3, 4, 5, 6], and the 4th smallest is 5.
"""
#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
import copy

arr = []
def inorder(tree, k, arr):
    if tree is not None:
	    inorder(tree.left, k, arr)
	    arr.append(copy.deepcopy(tree.value))
	    inorder(tree.right, k, arr)

    return arr

def kthSmallestInBST(t, k):
    result = inorder(t, k, arr)

    return result[k - 1] 
