from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_fill_stack(self, vertex, visited, stack):
        visited.add(vertex)

        for neighbour in self.graph[vertex]:
            if neighbour not in visited:
                self.dfs_fill_stack(neighbour, visited, stack)
        stack.append(vertex)

    def transpose(self):
        transposed = Graph()
        for u in self.graph:
            for v in self.graph[u]:
                transposed.add_edge(v, u)
        return transposed

    def kosaraju(self):
        stack = []
        visited = set()

        keys_copy = list(self.graph.keys())
        for vertex in keys_copy:
            if vertex not in visited:
                self.dfs_fill_stack(vertex, visited, stack)

        visited.clear()
        transposed_graph = self.transpose()
        sccs = []

        while stack:
            u = stack.pop()
            if u not in visited:
                scc = []
                transposed_graph.dfs_fill_stack(u, visited, scc)
                sccs.append(scc)

        return sccs


# Test Case 1
graph1 = Graph()
graph1.add_edge(0, 1)
graph1.add_edge(0, 2)
graph1.add_edge(1, 3)
graph1.add_edge(2, 3)
print(graph1.kosaraju())
assert graph1.kosaraju() == [[0], [2], [1], [3]]

# Test Case 2
graph2 = Graph()
graph2.add_edge(0, 1)
graph2.add_edge(1, 2)
graph2.add_edge(2, 0)
graph2.add_edge(1, 3)
graph2.add_edge(1, 4)
graph2.add_edge(3, 5)
graph2.add_edge(4, 5)
print(graph2.kosaraju())
assert graph2.kosaraju() == [[1, 2, 0], [4], [3], [5]]


# Test Case 3
graph3 = Graph()
graph3.add_edge(0, 1)
graph3.add_edge(1, 2)
graph3.add_edge(2, 3)
graph3.add_edge(3, 0)
graph3.add_edge(2, 4)
graph3.add_edge(4, 5)
graph3.add_edge(5, 6)
graph3.add_edge(6, 4)
print(graph3.kosaraju())
assert graph3.kosaraju() == [[1, 2, 3, 0], [5, 6, 4]]

# Test Case 4 (Disconnected Graph)
graph4 = Graph()
graph4.add_edge(0, 1)
graph4.add_edge(1, 2)
graph4.add_edge(2, 0)
graph4.add_edge(3, 4)
graph4.add_edge(4, 5)
graph4.add_edge(5, 3)
print(graph4.kosaraju())
assert graph4.kosaraju() == [[4, 5, 3], [1, 2, 0]]


# Test Case 5 (Single Vertex)
graph5 = Graph()
graph5.add_edge(0, 0)
assert graph5.kosaraju() == [[0]]





