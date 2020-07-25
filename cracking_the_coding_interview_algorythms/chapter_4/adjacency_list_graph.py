# Graph implementation - adjacency list

class Graph():
    def __init__(self, Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u , v):
        self.adj_list[u].append(v)

        if not self.is_directed:
            self.adj_list[v].append(u)

    def degree(self, node):
        deg = len(self.adj_list[node])
        return deg

    def print_adj_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])

nodes = [1, 2, 3, 4, 5, 6, 7, 8]
g = Graph(nodes, is_directed = True)
# g.print_adj_list()
all_edges = [(1, 4), (2, 4), (3, 4), (4, 5), (4, 6), (4, 7), (5, 8), (6, 8), (7, 8)]
for a, b in all_edges:
    g.add_edge(a, b)
g.print_adj_list()