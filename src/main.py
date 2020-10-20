from tortoise import *
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Command: main.py [data_file] [starting_year] [end_year]")
        exit(0)

    filename = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    parsed = parse_input_weights(filename)
    data = parse_graphs_year(parsed, start, end)
    for i in range(start, end+1):
        G = data.get(i)
        graph_display(G, i, {"inline": True, "node_labeled": True, "edge_labeled": False})
        degree_distribution_hist(G, i)
    temporal_analysis(data)
