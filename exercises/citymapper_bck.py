# The data file contains a list of OSM labels that are contained in the street graph, followed by  a list of blabelirectional
# edges, with distances between them given in meters. The edges represent the walkable streets in the graph.
#
# <number of nodes>
# <OSM label of node>
# …
# <OSM label of node>
# <number of edges>
# <from node OSM label> <to node OSM label> <length in meters>
# …
# <from node OSM label> <to node OSM label> <length in meters>

"""citymapper

Usage:
    citypampper data_file start_node end_node
    city (-h | --help

Options:
    -h --help

"""

import sys
from itertools import islice

INFINITY = float('inf')


class Node:
    def __init__(self, label):
        self.label = label


class Edge:
    def __init__(self, from_node, to_node, length):
        self.from_node = from_node
        self.to_node = to_node
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(from_node, to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]

        from_node_edges[to_node.label] = edge


def min_distance(queue, dist):
    """
    Returns node with smallest distance in queue
    """
    min_node = None
    for node in queue:
        if min_node is None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node

    return min_node


def dijkstra(graph, source):
    queue = set()
    dist = dict()
    prev = dict()

    for v in graph.nodes:
        dist[v] = INFINITY
        prev[v] = INFINITY
        queue.add(v)

    # initial node has a distance of 0
    dist[source] = 0

    while queue:
        vertex = min_distance(queue, dist)
        queue.remove(vertex)

        if vertex.label in graph.edges:
            for _, v in graph.edges[vertex.label].items():
                d = dist[vertex] + v.length
                if d < dist[v.to_node]:
                    dist[v.to_node] = d
                    prev[v.to_node] = vertex

    return dist, prev


def create_path(prev, from_node):
    prev_node = prev[from_node]
    route = [from_node.label]

    while prev_node != INFINITY:
        route.append(prev_node.label)
        temp = prev_node
        prev_node = prev[temp]

    route.reverse()
    return route


def main():
    filename = 'citymapper-coding-test-graph.dat'
    start_node = '876500321'
    end_node = '1524235806'

    # build graph
    graph = Graph()

    with open(filename, 'r') as reader:
        num_nodes = int(reader.readline())
        for line in islice(reader, 1, num_nodes):
            line = line.split('\n')[0]
            tmp = vars()['node_{}'.format(line)] = Node(line)
            graph.add_node(tmp)

        for line in islice(reader, num_nodes+1, None):
            values = line.split()
            node_a = vars()['node_{}'.format(values[0])]
            node_b = vars()['node_{}'.format(values[1])]
            graph.add_edge(Node(node_a), Node(node_b), int(values[2]))

    node_a = vars()['node_{}'.format(start_node)]
    node_b = vars()['node_{}'.format(end_node)]
    dist, prev = dijkstra(graph, node_a)

    print("The quickest path from {} to {} is [{}] with a distance of {}".format(
        node_a.label,
        node_b.label,
        " -> ".join(create_path(prev, node_b)),
        str(dist[node_b])
        )
    )


if __name__ == '__main__':
    main()

#
# graph = Graph()
# node_a = Node("A")
# graph.add_node(node_a)
# node_b = Node("B")
# graph.add_node(node_b)
# node_c = Node("C")
# graph.add_node(node_c)
# node_d = Node("D")
# graph.add_node(node_d)
# node_e = Node("E")
# graph.add_node(node_e)
# node_f = Node("F")
# graph.add_node(node_f)
# node_g = Node("G")
# graph.add_node(node_g)
#
# graph.add_edge(node_a, node_b, 4)
# graph.add_edge(node_a, node_c, 3)
# graph.add_edge(node_a, node_e, 7)
# graph.add_edge(node_b, node_c, 6)
# graph.add_edge(node_b, node_d, 5)
# graph.add_edge(node_c, node_d, 11)
# graph.add_edge(node_c, node_e, 8)
# graph.add_edge(node_d, node_e, 2)
# graph.add_edge(node_d, node_f, 2)
# graph.add_edge(node_d, node_g, 10)
# graph.add_edge(node_e, node_g, 5)
# graph.add_edge(node_f, node_g, 3)
#
# dist, prev = dijkstra(graph, node_a)
#
# print("The quickest path from {} to {} is [{}] with a distance of {}".format(
#     node_a.label,
#     node_f.label,
#     " -> ".join(create_path(prev, node_f)),
#     str(dist[node_f])
#     )
# )
