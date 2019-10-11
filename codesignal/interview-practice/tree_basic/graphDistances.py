"""
You have a strongly connected directed graph that has positive weights in the adjacency matrix g.
The graph is represented as a square matrix, where g[i][j] is the weight of the edge (i, j), or -1
if there is no such edge.

Given g and the index of a start vertex s, find the minimal distances between the start vertex s and
each of the vertices of the graph.

Example:
    For g = [[-1, 3, 2],
             [2, -1, 0],
             [-1, 0, -1]]

    and s = 0,
    the output should be graph_distance(g, s) = [0, 2, 2].

    [0] -> 3 -> [1]
    [0] -> 2 -> [2]

    [1] -> 2 -> [0]
    [1] -> 0 -> [2]

    [2] -> 0 -> [1]

The distance from the start vertex 0 to itself is 0.
The distance from the start vertex 0 to vertex 1 is 2 + 0 = 2.
The distance from the start vertex 0 to vertex 2 is 2.

"""


def graph_distance(g: object, s: object) -> object:
    """
    Dijkstra Algorithm -> find the shortest path between two vertices
    :param g: a square matrix
    :param s: start index
    :return: shortest path
    """
    n = len(g)
    distances = [float('Inf')] * n
    queue = set(range(n))

    # initial node has a distance of 0
    distances[s] = 0

    while len(queue):
        # find the element with min distance
        min_index = -1
        for i in queue:
            if min_index == -1 or distances[i] < distances[min_index]:
                min_index = i

        # remove min_index from the queue
        queue.remove(min_index)

        # look at all of the unvisited neighbours
        for next_index in range(n):
            weight = g[min_index][next_index]
            if weight != -1:
                # re-assess distance
                other_dist = distances[min_index] + weight

                if other_dist < distances[next_index]:
                    distances[next_index] = other_dist

    return distances


g = [[-1,  3,  2],
     [ 2, -1,  0],
     [-1,  0, -1]]
s = 0
print(graph_distance(g, s))  # [0, 2, 2]

g = [[-1,  1,  2],
     [ 0, -1,  3],
     [ 0,  0, -1]]
s = 1
print(graph_distance(g, s))  # [0, 0, 2]

g = [[-1,  0,  0,  0],
     [-1, -1, -1, 30],
     [ 1,  1, -1,  1],
     [ 2,  2,  0, -1]]
s = 3
print(graph_distance(g, s))  # [1, 1, 0, 0]
