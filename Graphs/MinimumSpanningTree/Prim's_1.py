class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.position_map = {}

    def insert(self, node):
        self.queue.append(node)
        idx = len(self.queue) - 1
        self.position_map[node.value] = idx
        self.bubble_up(idx)

    def bubble_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            parent = self.queue[parent_idx]
            child = self.queue[idx]
            if parent.priority > child.priority:
                self.swap(idx, parent_idx)
                idx = parent_idx
            else:
                break

    def swap(self, u, v):
        self.position_map[self.queue[u].value] = v
        self.position_map[self.queue[v].value] = u
        self.queue[u], self.queue[v] = self.queue[v], self.queue[u]

    def extract_min(self):
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            min_node = self.queue.pop()
            del self.position_map[min_node.value]
            return min_node

        self.swap(0, len(self.queue) - 1)
        min_node = self.queue.pop()
        del self.position_map[min_node.value]
        self.bubble_down(0)
        return min_node

    def bubble_down(self, idx):
        length = len(self.queue) - 1
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < length and self.queue[left].priority < self.queue[smallest].priority:
            smallest = left
        if right < length and self.queue[right].priority < self.queue[smallest].priority:
            smallest = right
        if smallest != idx:
            self.swap(idx, smallest)
            self.bubble_down(smallest)

    def decrease_priority(self, value, new_priority):
        # Find the index of the  value node
        for i in range(len(self.queue)):
            if self.queue[i].value == value:
                if self.queue[i].priority > new_priority:
                    self.queue[i].priority = new_priority
                    self.bubble_up(i)
                break

    def is_empty(self):
        return len(self.queue) == 0


def prims(graph, start):
    # Graph is represented by adjacency list
    # graph[u] is a list of tuples in the form (v, weight) representing edge (u, v) with corresponding weight
    # Initialize data structures
    mst = []
    PQ = PriorityQueue()
    priority = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    in_mst = set()

    priority[start] = 0
    PQ.insert(Node(start, 0))

    while not PQ.is_empty():
        min_node = PQ.extract_min()
        u = min_node.value

        if u in in_mst:
            continue

        in_mst.add(u)
        if parent[u] is not None:
            mst.append((parent[u], u, min_node.priority))

        for v, weight in graph[u]:
            if v not in in_mst and weight < priority[v]:
                priority[v] = weight
                parent[v] = u

                if v in PQ.position_map:
                    PQ.decrease_priority(v, priority[v])
                else:
                    PQ.insert(Node(v, priority[v]))
    return mst


def prims_1(graph, start):
    mst = []
    PQ = PriorityQueue()
    priority = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    in_mst = set()

    priority[start] = 0
    PQ.insert(Node(start, 0))

    while not PQ.is_empty():
        min_node = PQ.extract_min()
        u = min_node.value

        if u in in_mst:
            continue
        in_mst.add(u)
        if parent[u] is not None:
            mst.append((parent[u], u, min_node.priority))

        for v, weight in graph[u]:
            if v not in in_mst and weight < priority[v]:
                priority[v] = weight
                parent[v] = u

                if v in PQ.position_map:
                    PQ.decrease_priority(v, priority[v])
                else:
                    PQ.insert(Node(v, priority[v]))

    return mst


def prims_2(graph, start):
    mst = []
    PQ = PriorityQueue()
    priority = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    in_mst = set()

    priority[start] = 0
    PQ.insert(Node(start, 0))

    while not PQ.is_empty():
        min_node = PQ.extract_min()
        u = min_node.value

        if u in in_mst:
            continue

        if parent[u] is not None:
            mst.append((parent[u], u, min_node.priority))
        in_mst.add(u)

        for v, weight in graph[u]:
            if v not in in_mst and weight < priority[v]:
                priority[v] = weight
                parent[v] = u

                if v in PQ.position_map:
                    PQ.decrease_priority(v, priority[v])
                else:
                    PQ.insert(Node(v, priority[v]))
    return mst


def prims_3(graph, start):
    mst = []
    priority = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    in_mst = set()
    PQ = PriorityQueue()

    priority[start] = 0
    PQ.insert(Node(start, 0))

    while not PQ.is_empty():
        min_node = PQ.extract_min()
        u = min_node.value

        if u in in_mst:
            continue

        in_mst.add(u)
        if parent[u] is not None:
            mst.append((parent[u], u, min_node.priority))

        for v, weight in graph[u]:
            if v not in in_mst and weight < priority[v]:
                priority[v] = weight
                parent[v] = u

                if v in PQ.position_map:
                    PQ.decrease_priority(v, priority[v])
                else:
                    PQ.insert(Node(v, priority[v]))
    return mst


def prims_4(graph, start_vertex):
    PQ = PriorityQueue()
    mst = []
    in_mst = set()
    priority = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    priority[start_vertex] = 0
    PQ.insert(Node(start_vertex, 0))

    while not PQ.is_empty():
        min_node = PQ.extract_min()
        u = min_node.value

        if u in in_mst:
            continue
        in_mst.add(u)
        if parent[u] is not None:
            mst.append((parent[u], u, min_node.priority))

        for v, weight in graph[u]:
            if v not in in_mst and weight < priority[v]:
                priority[v] = weight
                parent[v] = u

                if v in PQ.position_map:
                    PQ.decrease_priority(v, priority[v])
                else:
                    PQ.insert(Node(v, priority[v]))

    return mst





# Example usage
graph = {
    'A': [('B', 1), ('C', 3), ('D', 4)],
    'B': [('A', 1), ('C', 2), ('E', 5)],
    'C': [('A', 3), ('B', 2), ('D', 1), ('E', 4)],
    'D': [('A', 4), ('C', 1), ('E', 1)],
    'E': [('B', 5), ('C', 4), ('D', 1)]
}

start_vertex = 'A'
mst = prims_4(graph, start_vertex)
print("Minimum Spanning Tree:", mst)