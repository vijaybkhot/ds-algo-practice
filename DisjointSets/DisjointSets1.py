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

ds = DisjointSet()
for i in range(1, 8):
    ds.make_set(i)

assert ds.find_set_data(1) == 1
assert ds.find_set_data(2) == 2
assert ds.find_set_data(3) == 3
assert ds.find_set_data(4) == 4
assert ds.find_set_data(5) == 5
assert ds.find_set_data(6) == 6
assert ds.find_set_data(7) == 7

assert ds.union(1, 2) == True
assert ds.union(2, 3) == True
assert ds.union(4, 5) == True
assert ds.union(6, 7) == True
assert ds.union(5, 6) == True
assert ds.union(3, 7) == True

print(ds.find_set_data(1))
assert ds.find_set_data(1) == 4
assert ds.find_set_data(2) == 4
assert ds.find_set_data(3) == 4
assert ds.find_set_data(4) == 4
assert ds.find_set_data(5) == 4
assert ds.find_set_data(6) == 4
assert ds.find_set_data(7) == 4

assert ds.union(1, 4) == False  # Already in the same set
assert ds.find_set_data(1) == 4
assert ds.find_set_data(4) == 4

