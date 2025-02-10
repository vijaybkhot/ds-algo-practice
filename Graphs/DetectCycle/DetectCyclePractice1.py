from collections import defaultdict


class Vertex:
    def __init__(self, val):
        self.val = val
        self.color = 'WHITE'
        self.parent = None
        self.d = float('inf')
        self.f = float('inf')


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0
        self.edges = []
        self.cycle_nodes = []
        self.has_cycle = False

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
                self.DFS_VISIT(v)
                v.parent = u
                self.edges.append((u, v, 'tree'))
            elif v.color == 'GRAY':
                if v.d < u.d:
                    self.has_cycle = True
                    self.edges.append((u, v, 'back'))
                    self.traceback_cycle(u, v)
                elif v.d > u.d:
                    self.edges.append((u, v, 'forward'))
                else:
                    self.edges.append((u, v, 'cross'))

        u.color = 'BLACK'
        self.time += 1
        u.f = self.time

    def traceback_cycle(self, u, v):
        while u != v:
            self.cycle_nodes.append(u)
            u = u.parent
        self.cycle_nodes.append(u)

    def hasCycle(self):
        return self.has_cycle

    def getCycleNodes(self):
        return self.cycle_nodes




