class DisjointSet:
    def __init__(self):
        self.map = {}

    class Node:
        def __init__(self, data):
            self.data = data
            self.parent = self
            self.rank = 0

    def make_set(self, data):
        node = self.Node(data)
        self.map[data] = node

    def find_set(self, node):
        parent = node.parent
        if node == parent:
            return parent
        node.parent = self.find_set(node.parent)
        return node.parent

    def find_set_data(self, data):
        return self.find_set(self.map[data]).data

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]

        root1 = self.find_set(node1)
        root2 = self.find_set(node2)

        if root1.data == root2.data:
            return

        if root1.rank >= root2.rank:
            root2.parent = root1
            if root1.rank == root2.rank:
                root1.rank += 1

        else:
            root1.parent = root2


class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.weight = weight
        self.vertex1 = vertex1
        self.vertex2 = vertex2


def kruskal_mst(graph):
    mst = []
    disjoint_set = DisjointSet()
    all_edges = sorted(graph, key=lambda x: x.weight)

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


if __name__ == "__main__":
    graph = [
        Edge(1, 2, 4),
        Edge(1, 3, 1),
        Edge(2, 5, 1),
        Edge(2, 6, 3),
        Edge(2, 4, 2),
        Edge(6, 5, 2),
        Edge(6, 4, 3),
        Edge(4, 7, 2),
        Edge(3, 4, 5),
        Edge(3, 7, 8)
    ]
    mst = kruskal_mst(graph)
    for edge in mst:
        print(f"{edge.vertex1} {edge.vertex2}")



