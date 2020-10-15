from tortoise import *
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import collections

dec = parse_graphs_year("reptilia-tortoise-network-fi-parsed.edges", 2005, 2005)
graph_display(dec.get(2005), {"inline": True, "labeled": True})
