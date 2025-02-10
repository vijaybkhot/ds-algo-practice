from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_build_stack(self, u, visited, stack):
        visited.add(u)
        for v in self.graph[u]:
            if v not in visited:
                self.dfs_build_stack(v, visited, stack)

        stack.append(u)

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
        for u in keys_copy:
            if u not in visited:
                self.dfs_build_stack(u, visited, stack)

        visited.clear()
        sccs = []

        reversed = self.transpose()

        while stack:
            u = stack.pop()
            if u not in visited:
                scc = []
                reversed.dfs_build_stack(u, visited, scc)
                sccs.append(scc)
        return sccs

# Test Case 1
graph1 = Graph()
graph1.add_edge(0, 1)
graph1.add_edge(0, 2)
graph1.add_edge(1, 3)
graph1.add_edge(2, 3)
print(graph1.kosaraju())
assert graph1.kosaraju() == [[3], [1], [2], [0]]





