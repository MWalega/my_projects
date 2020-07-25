# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

class Vertex():
    def __init__(self, n):
        self.name = n
        self.neighbors = set()

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.add(v)

class Graph():
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u ,v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            # self.vertices[v].add_neighbor(u)                  <-- w przypadku undirected 
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(list(self.vertices[key].neighbors)))

    def _dfs(self, vertex):
        vertex.color = 'red'
        vertex.discovery = self.time
        self.time += 1

        for v in vertex.neighbors:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
        vertex.color = 'blue'
        vertex.finish = self.time
        self.time += 1
    
    def dfs(self, vertex):
        self.time = 1
        self._dfs(vertex)

    def check_is_route(self, start, end):
        if start == end:
            return print('There is a way')
        start.color = 'red'

        for v in start.neighbors:
            if self.vertices[v].color == 'black':
                return self.check_is_route(self.vertices[v], end)

    def route_rec(self, start, end):
        self.check_is_route(start, end)
        if end.color == 'red':
            return print('There is a way')
        else:
            return print('No connection')

        
g = Graph()
for i in range(ord('A'), ord('F')):
    g.add_vertex(Vertex(chr(i)))
# g.print_graph()
edges = ['AB', 'AD', 'BC', 'DE']
for edge in edges:
    g.add_edge(edge[0], edge[-1])
# g.print_graph()
g.check_is_route(g.vertices['A'], g.vertices['C'])
