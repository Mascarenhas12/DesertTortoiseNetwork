import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections


def create_wsg(nodes: int, degree: int, probability: float) -> nx.Graph:
    return nx.watts_strogatz_graph(nodes, degree, probability)


def graph_inline(G: nx.Graph, pos: dict) -> None:
    # draw graph in inset
    degrees = G.degree() #Dict with Node ID, Degree
    nodes = G.nodes()
    n_color = np.asarray([degrees[n] for n in nodes])
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=n_color, node_size=200, cmap="Blues")
    nx.draw_networkx_edges(G, pos, alpha=0.4)


def add_degree_label(G: nx.Graph, pos: dict) -> None:
    labels = {}

    for node in G.nodes():
        labels[node] = G.degree[node]
    nx.draw_networkx_labels(G, pos, labels, font_size=16)


def degree_histogram(G: nx.Graph, inline: bool = False, labels: bool = False) -> None:
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)  # counting vector of degree (histogram values)
    deg, cnt = zip(*degreeCount.items())
    # matches degrees with counter (3,2,1) (2,4,2) means 2 nodes have degree 3;
    # 4 nodes have degree 2; 2 nodes have degree 2

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")

    plt.title("Degree Histogram")
    plt.ylabel("Count")  # Change to probability
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    plt.axes([0.45, 0.45, 0.45, 0.45])
    G = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    pos = nx.spring_layout(G)
    if inline:
        graph_inline(G, pos)
    if labels:
        add_degree_label(G, pos)

    plt.axis("off")
    plt.show()
