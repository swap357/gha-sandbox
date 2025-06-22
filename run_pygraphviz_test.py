import networkx as nx
from graphviz import Source
from IPython.display import display

# Minimal example to trigger pygraphviz usage via networkx

def to_graphviz():
    g = nx.DiGraph()
    g.add_edge("a", "b")
    return Source(nx.nx_agraph.to_agraph(g).string())

if __name__ == "__main__":
    try:
        gviz = to_graphviz()
        print(gviz.source)
        # Emulate notebook usage
        display(gviz)
    except Exception as e:
        print("Encountered error:", e)
        raise
