from tortoise import *


if __name__ == "__main__":
    data = parse_graphs_year("reptilia-tortoise-network-fi-parsed.edges", 2005, 2013)
    for i in range(2005, 2014):
        G = data.get(i)
        graph_display(G, i, {"inline": True, "node_labeled": True, "edge_labeled": False})
        degree_distribution_hist(G, i)
    temporal_analysis(data)
