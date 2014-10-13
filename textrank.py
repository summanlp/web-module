
from pygraph.classes.digraph import digraph as pydigraph
from pygraph.algorithms.pagerank import pagerank
from math import log10

TEST_FILE = "testdata/textrank_example.txt"


def textrank(filename):
    graph = get_graph(filename)
    set_graph_edge_weights(graph)

    d = pagerank(graph)
    #print d


def get_graph(filename):
    graph = pydigraph()

    # Creates the graph.
    with open(filename) as fp:
        for line in fp:
            graph.add_node(line)

    return graph


def set_graph_edge_weights(graph):
    for sentence_1 in graph.nodes():
        for sentence_2 in graph.nodes():
            if sentence_1 == sentence_2:
                continue

            edge_1 = (sentence_1, sentence_2)
            edge_2 = (sentence_2, sentence_1)

            if graph.has_edge(edge_1) or graph.has_edge(edge_2):
                continue

            similarity = get_similarity(sentence_1, sentence_2)

            graph.add_edge(edge_1, similarity)
            graph.add_edge(edge_2, similarity)


def get_similarity(s1, s2):
    s1_list = s1.split()
    s2_list = s2.split()

    common_word_count = get_common_word_count(s1_list, s2_list)

    log_s1 = log10(len(s1_list))
    log_s2 = log10(len(s2_list))

    return common_word_count / (log_s1 + log_s2)


def get_common_word_count(s1_list, s2_list):
    return sum(1 for w in set(s1_list) if w in set(s2_list))


textrank(TEST_FILE)