import matplotlib.pyplot as plt
import networkx as nx
import collections


def create_wsg(nodes: int, degree: int, probability: float) -> nx.Graph:
    return nx.watts_strogatz_graph(nodes, degree, probability)


def graph_inline(G: nx.Graph) -> None:
    # draw graph in inset
    plt.axes([0.4, 0.4, 0.5, 0.5])
    G = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    pos = nx.spring_layout(G)
    plt.axis("off")
    nx.draw_networkx_nodes(G, pos, node_size=20)
    nx.draw_networkx_edges(G, pos, alpha=0.4)


def graph_coloured_degree(G: nx.Graph) -> None:
    plt.axes([0.4, 0.4, 0.5, 0.5])
    G = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    pos = nx.spring_layout(G)
    plt.axis("off")
    nx.draw(G, pos, node_color=range(G.number_of_nodes()), node_size=100, cmap=plt.cm.Blues)


def degree_histogram(G: nx.Graph, inline: bool = False, coloured: bool = False) -> None:
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
    degreeCount = collections.Counter(degree_sequence)  # counting vector of degree (histogram values)
    deg, cnt = zip(*degreeCount.items())
    # matches degrees with counter (3,2,1) (2,4,2) means 2 nodes have degree 3;
    # 4 nodes have degree 2; 2 nodes have degree 2

    fig, ax = plt.subplots()
    plt.bar(deg, cnt, width=0.80, color="b")

    plt.title("Degree Histogram")
    plt.ylabel("Count") #Change to probability
    plt.xlabel("Degree")
    ax.set_xticks([d + 0.4 for d in deg])
    ax.set_xticklabels(deg)
    if inline:
        graph_inline(G)
    elif coloured:
        graph_coloured_degree(G)
    plt.show()
