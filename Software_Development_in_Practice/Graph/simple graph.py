class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def edges(self):
        return self.find_edges()

    # Get the keys of the dictionary
    def get_vertices(self):
        return list(self.gdict.keys())

    # Find the distinct list of edges
    def find_edges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    # Add the vertex as a key
    def add_vertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    # Add the new edge
    def add_edge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


# Create the dictionary with graph elements
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}
g = graph(graph_elements)
print(f"Elements of the graph are: {graph_elements}")
print(f"Verticies are : {g.get_vertices()}")
print(f"Graph edges are: {g.edges()}")
