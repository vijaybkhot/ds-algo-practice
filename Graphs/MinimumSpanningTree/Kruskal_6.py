class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.rank = 0


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


class DisjointSet:
    def __init__(self):
        self.map = {}

    def make_set(self, data):
        node = Node(data)
        self.map[data] = node

    def find_set(self, node):
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.find_set(node.parent)
        return node.parent

    def find_set_data(self, data):
        node = self.map[data]
        root = self.find_set(node)
        return root.data

    def union(self, data1, data2):
        if data1 not in self.map or data2 not in self.map:
            return
        node1 = self.map[data1]
        node2 = self.map[data2]

        root1 = self.map[node1]
        root2 = self.map[node2]

        if root1.data == root2.data:
            return
        if root1.rank >= root2.rank:
            if root1.rank == root2.rank:
                root1.rank += 1

            root2.parent = root1
        else:
            root1.parent = root2


def kruskal(graph):
    all_edges = sorted(graph, key=lambda x: x.weight)
    mst = []
    disjoint_set = DisjointSet()
    vertices = set()
    for edge in all_edges:
        vertices.add(edge.vertex1)
        vertices.add(edge.vertex2)

    for vertex in vertices:
        disjoint_set.make_set(vertex)

    for edge in all_edges:
        root1 = disjoint_set.find_set_data(edge.vertex1)
        root2 = disjoint_set.find_set_data(edge.vertex2)

        if root1 != root2:
            mst.append(edge)
            disjoint_set.union(edge.vertex1, edge.vertex2)

    return mst










