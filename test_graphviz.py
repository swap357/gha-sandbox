import networkx as nx
from IPython.display import display
from graphviz import Source

G = nx.DiGraph([(1, 2), (2, 3)])
try:
    src = Source(nx.nx_agraph.to_agraph(G).string())
    display(src)
    print("SUCCESS")
except Exception as e:
    print("FAILED:", e)
    raise
