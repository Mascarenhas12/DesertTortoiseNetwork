import matplotlib.pyplot as plt
import networkx as nx

def rw_graph_ex(n: int, m: int):
    G = nx.grid_2d_graph(n,m)  # 5x5 grid

    # print the adjacency list
    for line in nx.generate_adjlist(G):
        print(line)
    # write edgelist to grid.edgelist
    nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
    # read edgelist from grid.edgelist
    H = nx.read_edgelist(path="grid.edgelist", delimiter=":")

    nx.draw(H)
    plt.show()


def prop_graph_ex(n: int, m: int):
    G = nx.lollipop_graph(4, 6)

    pathlengths = []

    print("source vertex {target:length, }")
    for v in G.nodes():
        spl = dict(nx.single_source_shortest_path_length(G, v))
        print(f"{v} {spl} ")
        for p in spl:
            pathlengths.append(spl[p])

    print()
    print(f"average shortest path length {sum(pathlengths) / len(pathlengths)}")
    print(pathlengths)

    # histogram of path lengths
    dist = {}
    for p in pathlengths:
        if p in dist:
            dist[p] += 1
        else:
            dist[p] = 1

    print()
    print("length #paths")
    verts = dist.keys()
    for d in sorted(verts):
        print(f"{d} {dist[d]}")

    print(f"radius: {nx.radius(G)}")
    print(f"diameter: {nx.diameter(G)}")
    print(f"eccentricity: {nx.eccentricity(G)}")
    print(f"center: {nx.center(G)}")
    print(f"periphery: {nx.periphery(G)}")
    print(f"density: {nx.density(G)}")

    nx.draw(G, with_labels=True)
    plt.show()


def path_graph_ex(nodes: int):
    G = nx.path_graph(nodes)
    nx.draw(G)
    plt.show()


def cycle_graph_ex(nodes: int):
    G = nx.cycle_graph(nodes)
    pos = nx.spring_layout(G, iterations=200)
    nx.draw(G, pos, node_color=range(24), node_size=800, cmap=plt.cm.Blues)
    plt.show()