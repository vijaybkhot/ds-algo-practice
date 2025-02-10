from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0
        self.edges = []

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
                self.edges.append((u, v, 'tree'))   # Tree Edge
                self.DFS_VISIT(v)
            elif v.color == 'GRAY':
                if v.d < u.d:
                    self.edges.append((u, v, 'back'))
                elif v.d > u.d:
                    self.edges.append((u, v, 'forward'))
                else:
                    self.edges.append((u, v, 'cross'))
        u.color = 'BLACK'
        self.time += 1
        u.f = self.time



