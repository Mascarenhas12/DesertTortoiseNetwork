import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections


def graph_inline(G: nx.Graph, pos: dict) -> None:
    # draw graph in inset
    degrees = G.degree()  # Dict with Node ID, Degree
    nodes = G.nodes()
    n_color = np.asarray([degrees[n] for n in nodes])
    nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=n_color, node_size=200, cmap="Blues")
    nx.draw_networkx_edges(G, pos, alpha=0.4)


def add_degree_label(G: nx.Graph, pos: dict) -> None:
    labels = {}

    for node in G.nodes():
        labels[node] = G.degree[node]
    nx.draw_networkx_labels(G, pos, labels, font_size=16)


def parse_graphs_year(path: str, start_year: int, end_year: int) -> dict:
    graphs = {}
    with open(path, 'r') as file:
        lines = [n[:-1] for n in file.readlines()]
        G = nx.parse_edgelist(lines, nodetype=int, data=(("year", int),))
        for i in range(start_year, end_year + 1):
            edges = [n for n in G.edges(data=True) if n[2].get("year") == i]
            sub = nx.Graph()
            sub.add_edges_from(edges)
            graphs[i] = sub
    return graphs
