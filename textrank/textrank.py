
from pygraph.classes.digraph import digraph as pydigraph
from pagerank_weighted import pagerank_weighted as pagerank
from math import log10

SUMMARY_LENGTH = .2
TEST_FILE = "test_data/textrank_example.txt"


def textrank(filename):
    # Creates the graph and calculates the simmilarity coefficient
    # for every pair of nodes.
    graph = get_graph(filename)
    set_graph_edge_weights(graph)

    # Ranks the sentences using the PageRank algorithm.
    scores = pagerank(graph)

    # Extracts the most important sentences.
    extracted_sentences = extract_sentences(graph.nodes(), scores)

    # Sorts the extracted sentences by apparition order in the
    # original text.
    return sort_by_apparition(extracted_sentences, filename)


def sort_by_apparition(extracted_sentences, filename):
    summary = []

    with open(filename) as text:
        for sentence in text:
            if sentence in extracted_sentences:
                summary.append(sentence)

    return summary


def extract_sentences(sentences, scores):
    sentences.sort(key=lambda s: scores[s], reverse=True)
    length = len(sentences) * SUMMARY_LENGTH
    return sentences[:int(length)]


def get_graph(filename):
    graph = pydigraph()

    # Creates the graph.
    with open(filename) as text:
        for line in text:
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


for line in textrank(TEST_FILE):
    print line