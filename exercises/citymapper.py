"""Citymapper Router Challenge

Using some data from Open Street Maps (OSM), we have created a data file representing a graph of
walkable streets. You may download the file here:
https://s3-eu-west-1.amazonaws.com/citymapper-assets/citymapper-coding-test-graph.dat
The data file contains a list of OSM ids that are contained in the street graph, followed by a
list of bidirectional edges, with distances between them given in meters. The edges represent
the walkable streets in the graph.

    <number of nodes>
    <OSM id of node>
    ...
    <OSM id of node>
    <number of edges>
    <from node OSM id> <to node OSM id> <length in meters>
    ...
    <from node OSM id> <to node OSM id> <length in meters>

We would like you to write a short program that takes a graph using this representation as
input, and computes the shortest walking distance in meters between two given OSM nodes in
the graph (assuming all edges are walkable.) For example
You may use any language you wish, though we are most familiar with Python, Go, Java, C++
and C. You may only use the standard library from your language of choice, excluding any
built-in graph libraries (e.g. you may not use networkx in Python.) Ask us if you have any
doubts about this. The code should compile and run on Linux or OS X.
Please provide a short README mentioning how to compile the code, and any design decisions o
r assumptions you have made.
Please email us back a tarball or zip with a README, all of the code, and a run.sh so that
we can run your code with ./run.sh <path to graph> <from-osm-id> <to-osm-id>. If a path exists
the program should output the length of the shortest path in meters, and nothing else.
We are looking for clean code that solves the problem, and does not do anything else. If you
wish, you may briefly mention any ideas for extensions in the README.

 ./run.sh citymapper-coding-test-graph.dat 876500321 1524235806
2709

NOTE:
    - Because we are using Python the following code should work on both Linux and MacOs.
"""
from collections import defaultdict
from itertools import islice
try:
    import click
except ImportError:
    raise ImportError('The command line interfaces "click" is not installed.')

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes; e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.distances has all the distances between two nodes, with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.distances = dict()

    def add_edge(self, start_vertex, end_vertex, distance):
        """
        All edges are bi-directional
        :param start_vertex: OSM id -> 876500321
        :param end_vertex: OSM id -> 1524235806
        :param distance: int -> kilometer
        :return:
        """
        self.edges[start_vertex].append(end_vertex)
        self.edges[end_vertex].append(start_vertex)
        self.distances[(end_vertex, start_vertex)] = distance
        self.distances[(start_vertex, end_vertex)] = distance


def shortest_path(graph, start, end):
    """
    Dijsktra's Algorithm:
        Find shortest paths and store it as a dict of nodes -> tuple of (previous node, distance)
    """
    path = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        dist_to_current_node = path[current_node][1]

        for next_node in destinations:
            distance = graph.distances[(current_node, next_node)] + dist_to_current_node

            if next_node not in path:
                path[next_node] = (current_node, distance)
            else:
                current_shortest_dist = path[next_node][1]
                if current_shortest_dist > distance:
                    path[next_node] = (current_node, distance)

        next_destinations = {node: path[node] for node in path if node not in visited}
        if not next_destinations:
            return "NOT POSSIBLE"

        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # # Work back through destinations in shortest path to show the path walked
    # path = []
    # while current_node is not None:
    #     path.append(current_node)
    #     next_node = path[current_node][0]
    #     current_node = next_node
    #
    # # Reverse path
    # path = path[::-1]
    
    return distance


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('filename', type=click.Path(exists=True))
@click.argument('start_node', nargs=1, type=click.INT)
@click.argument('end_node', nargs=1, type=click.INT)
def main(filename, start_node, end_node):
    """
    Read in data file and build a graph. We only need the second part of the data to build the graph.
    :param filename: data file -> citymapper-coding-test-graph.dat
    :param start_node: OSM id -> 876500321
    :param end_node: OSM id -> 1524235806
    """
    # initialize graph
    graph = Graph()

    with open(click.format_filename(filename), 'r') as reader:
        num_nodes = int(reader.readline())
        edges = []

        # build graph
        for line in islice(reader, num_nodes + 1, None):
            values = line.split()
            values[2] = int(values[2])
            edges.append(tuple(values))

        for edge in edges:
            graph.add_edge(*edge)

    dist = shortest_path(graph, start_node, end_node)
    print('The shortest path between OSM id {} - id {} is {} km long'.format(start_node, end_node, dist))


if __name__ == '__main__':
    main()
