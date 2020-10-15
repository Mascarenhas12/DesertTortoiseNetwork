import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections

from matplotlib.legend_handler import HandlerLine2D


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


def add_edge_label(g: nx.Graph, pos: dict) -> None:
    label = {}

    for edge in g.edges(data=True):
        label[(edge[0], edge[1])] = edge[2].get("weight")
    nx.draw_networkx_edge_labels(g, pos, label, font_size=8)


def parse_input_weights(file_name: str) -> None:
    edges = {}

    with open(file_name, 'r') as file:
        lines = [n[:-1] for n in file.readlines()]
        for line in lines:
            if line in edges:
                edges[line] += 1
            else:
                edges[line] = 1

    name, extension = file_name.split(".")
    f = open(name + "-parsed." + extension, "w")
    for key in edges.keys():
        f.write(key + " " + str(edges[key]) + "\n")


def parse_graphs_year(path: str, start_year: int, end_year: int) -> dict:
    graphs = {}
    with open(path, 'r') as file:
        lines = [n[:-1] for n in file.readlines()]
        G = nx.parse_edgelist(lines, nodetype=int, data=(("year", int), ("weight", int),))
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
        add_edge_label(G, pos)

    plt.axis("off")
    plt.show()


def average_degree(graph: nx.Graph) -> float:
    degrees = graph.degree()
    if not len(degrees):
        return 0

    degSum = sum([n for _, n in degrees])
    return degSum / len(degrees)


def degree_distribution_hist(graph: nx.Graph) -> None:
    degree_sequence = sorted([d for _, d in graph.degree()], reverse=True)
    degreeCount = collections.Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    prob = [cnt[i] / len(degree_sequence) for i in range(len(cnt))]

    fig, ax = plt.subplots()
    plt.bar(deg, prob, width=0.80, color="b")
    # plt.plot(deg, prob, color="black")
    ax.set_xticks([d for d in deg])
    ax.set_xticklabels(deg)

    plt.title("Degree Histogram")
    plt.ylabel("Probability")
    plt.xlabel("Degree")
    plt.show()


def APL_connected_components(graph: nx.Graph) -> int:
    gph = graph.subgraph(sorted(nx.connected_components(graph), key=len, reverse=True)[0])
    return nx.average_shortest_path_length(gph)


def temporal_analysis(graphs: dict) -> None:
    avgDeg, avgClu, avgAPL = [], [], []
    for year in graphs.keys():
        avgDeg.append(average_degree(graphs.get(year)))
        avgClu.append(nx.average_clustering(graphs.get(year)))
        avgAPL.append(APL_connected_components(graphs.get(year)))

    line1, = plt.plot(list(graphs.keys()), avgDeg, label="Average Degree")
    plt.plot(list(graphs.keys()), avgClu, label="Average Clustering Coefficient")
    plt.plot(list(graphs.keys()), avgAPL, label="Average Path Length")

    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
    plt.yticks(np.arange(0, max(avgAPL) + 1, 0.5))

    plt.show()
