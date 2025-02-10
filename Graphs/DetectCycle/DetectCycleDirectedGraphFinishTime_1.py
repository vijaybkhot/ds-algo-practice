from collections import defaultdict


class Vertex:
    def __init__(self, val):
        self.val = val
        self.color = 'WHITE'
        self.parent = None
        self.d = float('inf')


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = []
        self.time = 0
        self.cycle_nodes = []
        self.has_cycle = False

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def DFS(self):
        for vertex in self.graph:
            vertex.color = 'WHITE'
            vertex.parent = None
        self.time = 0

        for vertex in self.graph:
            if vertex.color == 'WHITE':
                self.DFS_VISIT(vertex)

    def DFS_VISIT(self, vertex):
        self.time += 1
        vertex.d = self.time
        vertex.color = 'GRAY'

        for neighbour in self.graph[vertex]:
            if neighbour.color == 'WHITE':
                self.edges.append((vertex, neighbour, 'tree'))
                neighbour.parent = vertex
                self.DFS_VISIT(neighbour)
            elif neighbour.color == 'GRAY':
                if neighbour.d < vertex.d:
                    self.edges.append((vertex, neighbour, 'back'))
                    self.has_cycle = True
                    self.traceback_cycle(vertex, neighbour)

                elif neighbour.d > vertex.d:
                    self.edges.append((vertex, neighbour, 'forward'))
                else:
                    self.edges.append((vertex, neighbour, 'cross'))
        vertex.color = 'BLACK'
        self.time += 1
        vertex.f = self.time

    def traceback_cycle(self, u, v):
        while u != v:
            self.cycle_nodes.append(u)
            u = u.parent
        self.cycle_nodes.append(u)

    def hasCycle(self):
        return self.has_cycle

    def getCycleNodes(self):
        return self.cycle_nodes
