from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0
        self.edges = []
        self.stack = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self):
        for u in self.graph:
            u.color = 'WHITE'
            u.parent = None
        self.time = 0
        for u in self.graph:
            if u.color == 'WHITE':
                self.DFS_VISIT(u)

    def DFS_VISIT(self, u):
        self.time += 1
        u.d = self.time
        u.color = 'GRAY'
        for v in self.graph[u]:
            if v.color == 'WHITE':
                v.parent = u
                self.edges.append((u, v, 'tree'))
                self.DFS_VISIT(v)
            elif v.color == 'GRAY':
                if v.d < u.d:
                    self.edges.append((u, v, 'back'))
                elif v.d > u.d:
                    self.edges.append((u, v, 'forward'))
                else:
                    self.edges.append((u, v, 'cross'))
        self.stack.append(u)

    def topological_sort(self):
        self.stack = []
        self.DFS()
        return self.stack[::-1]


# Example usage
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)

print("Topological Sort:", g.topological_sort())
