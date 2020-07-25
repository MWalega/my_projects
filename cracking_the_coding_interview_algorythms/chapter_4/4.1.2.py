# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, ' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    
    def DFS(self, v):
        visited = [False] * (max(self.graph) + 1)
        return print(visited)
        self.DFSUtil(v, visited)


g = Graph()
edges = [(1,2),(2,3),(2,4),(3,3),(4,4)]
for edge in edges:
    g.add_edge(edge[0], edge[-1])
print(g.graph)
g.DFS(2)