import networkx as nx
from graphviz import Source

G = nx.DiGraph([(1, 2), (2, 3)])
try:
    src = Source(nx.nx_agraph.to_agraph(G).string())
    src.pipe(format="png")  # ensure Graphviz runs
    print("SUCCESS")
except Exception as e:
    print("FAILED:", e)
    raise
