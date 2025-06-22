import networkx as nx
from graphviz import Source

# Minimal example to trigger pygraphviz usage via networkx

def to_graphviz():
    g = nx.DiGraph()
    g.add_edge("a", "b")
    return Source(nx.nx_agraph.to_agraph(g).string())

if __name__ == "__main__":
    try:
        # Print the dot source to exercise pygraphviz
        print(to_graphviz().source)
    except Exception as e:
        print("Encountered error:", e)
        raise
