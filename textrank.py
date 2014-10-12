
from pygraph.classes.graph import graph as pygraph

TEST_FILE = "testdata/textrank_example.txt"


def textrank(filename):
    graph = get_graph(filename)

    set_graph_edge_weights(graph)


def get_graph(filename):
    graph = pygraph()

    # Creates the graph.
    with open(filename) as fp:
        for line in fp:
            graph.add_node(line)

    graph.complete()

    return graph


def set_graph_edge_weights(graph):
    for node in graph.nodes():
        print node


textrank(TEST_FILE)