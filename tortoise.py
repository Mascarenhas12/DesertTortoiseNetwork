import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections


def graph_inline(G: nx.Graph, pos: dict) -> None:
    # draw graph in inset
    degrees = G.degree()  # Dict with Node ID, Degree
    nodes = G.nodes()
    n_color = np.asarray([degrees[n] for n in nodes])
    nx.draw_networkx_nodes(G, pos, nodelist=nodes,
                           node_color=n_color, node_size=200,
                           cmap="Blues", vmin=-8)
    nx.draw_networkx_edges(G, pos, alpha=0.4)


def add_degree_label(G: nx.Graph, pos: dict) -> None:
    labels = {}

    for node in G.nodes():
        labels[node] = G.degree[node]
    nx.draw_networkx_labels(G, pos, labels, font_size=16, font_color="white")


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


def graph_display(G: nx.Graph, options: dict) -> None:
    pos = nx.spring_layout(G, k=0.8)

    if options.get("inline"):
        graph_inline(G, pos)
    if options.get("labeled"):
        add_degree_label(G, pos)

    plt.axis("off")
    plt.show()

def averageDegree(graph: nx.Graph) -> float:
    degrees = graph.degree()
    if not len(degrees):
        return 0

    degSum = sum([n for _, n in degrees])
    return degSum / len(degrees)


def degreeDistributionHist(graph: nx.Graph) -> None:

    degree_sequence = sorted([d for _, d in graph.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    prob = [cnt[i] / len(degree_sequence) for i in range(len(cnt))]

    fig, ax = plt.subplots()
    plt.bar(deg, prob, width=0.80, color="b")
    #plt.plot(deg, prob, color="black")
    ax.set_xticks([d for d in deg])
    ax.set_xticklabels(deg)

    plt.title("Degree Histogram")
    plt.ylabel("Probability")
    plt.xlabel("Degree")
    plt.show()


def APLConnectedComponents(graph: nx.Graph) -> int:
    gph = graph.subgraph(sorted(nx.connected_components(graph), key=len, reverse=True)[0])
    return nx.average_shortest_path_length(gph)
