
class DisjointSet:
    def __init__(self):
        self.map = {}

    class Node:
        def __init__(self, data):
            self.data = data
            self.rank = 0
            self.parent = self

    def make_set(self, data):
        node = self.Node(data)
        self.map[data] = node

    def union(self, data1, data2):
        node1 = self.map[data1]
        node2 = self.map[data2]

        root1 = self.find_set(node1)
        root2 = self.find_set(node2)

        if root1.data == root2.data:
            return False

        if root1.rank >= root2.rank:
            root1.rank = root1.rank + 1 if root1.rank == root2.rank else root1.rank
            root2.parent = root1
        else:
            root1.parent = root2
        return True

    def find_set(self, node):
        parent = node.parent
        if parent == node:
            return parent
        node.parent = self.find_set(node.parent)
        return node.parent

    def find_set_data(self, data):
        return self.find_set(self.map[data]).data


