from collections import namedtuple
from collections import defaultdict
from scipy.spatial import distance

#
# "Top-down" means that in each recursion level, we will visit the node first
# to come up with some values, and pass these values to its children when calling
# the function recursively. So the "top-down" solution can be considered as kind
# of preorder traversal. To be specific, the recursion function top_down(root, params)
# works like this:
#
# 1. return specific value for null node
# 2. update the answer if needed                      // answer <-- params
# 3. left_ans = top_down(root.left, left_params)      // left_params <-- root.val, params
# 4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params
# 5. return the answer if needed                      // answer <-- left_ans, right_ans
# For instance, consider this problem: given a binary tree, find its maximum depth.
#
# We know that the depth of the root node is 1. For each node, if we know the
# depth of the node, we will know the depth of its children. Therefore, if we
# pass the depth of the node as a parameter when calling the function recursively,
# all the nodes know the depth of themselves. And for leaf nodes, we can use the
# depth to update the final answer. Here is the pseudocode for the recursion
# function maximum_depth(root, depth):
#
# 1. return if root is null
# 2. if root is a leaf node:
# 3.      answer = max(answer, depth)         // update the answer if needed
# 4. maximum_depth(root.left, depth + 1)      // call the function recursively for left child
# 5. maximum_depth(root.right, depth + 1)     // call the function recursively for right child
#
Mine = namedtuple("Mine", ["name", "x", "y", "blast_radius"])


def get_dist(x1, y1, x2, y2):
    return distance.euclidean([x1, y1], [x2, y2])


def longest_chain(mines):
    conn = defaultdict(set)

    for mine in mines:
        for otherMine in mines:
            if mine == otherMine:
                continue
            else:
                dist = get_dist(mine.x, mine.y, otherMine.x, otherMine.y)
                if dist <= mine.blast_radius:
                    conn[mine.name].add(otherMine.name)

    # for k, v in conn.iteritems():

    return conn


# Diagram: https://i.imgur.com/xEZZQKP.png
mines = [
    Mine("A", 7, 13, 3),
    Mine("B", 6.5, 17, 5),
    Mine("C", 12, 10, 4.5),
    Mine("D", 14.5, 7, 3.5),
    Mine("E", 17, 9, 2),
    Mine("F", 7, 11, 2.5),
    Mine("G", 8.5, 11.5, 3),
]

print(longest_chain(mines))
# print(longest_chain(mines) == ('C', 6))
