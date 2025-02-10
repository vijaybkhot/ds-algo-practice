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
                self.swap(parent_idx, idx)
                idx = parent_idx
            else:
                break

    def swap(self, id1, id2):
        self.position_map[self.queue[id1].value] = id2
        self.position_map[self.queue[id2].value] = id1
        self.queue[id1], self.queue[id2] = self.queue[id2], self.queue[id1]

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
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.queue) and self.queue[left].priority < self.queue[smallest].priority:
            smallest = left

        if right < len(self.queue) and self.queue[right].priority < self.queue[smallest].priority:
            smallest = right

        if smallest != idx:
            self.swap(smallest, idx)
            self.bubble_down(smallest)

    def decrease_priority(self, value, new_priority):
        idx = self.position_map[value]
        self.queue[idx].priority = new_priority
        self.bubble_up(idx)

    def is_empty(self):
        return len(self.queue) == 0


def djikstra(graph, start):
    PQ = PriorityQueue()
    distance_map = {vertex: float('-inf') for vertex in graph}
    parent_map = {vertex: None for vertex in graph}
    distance_map[start] = 0
    PQ.insert(Node(start, 0))

    while not PQ.is_empty():
        curr_node = PQ.extract_min()
        curr_vertex = curr_node.value

        for adj_vertex, weight in graph[curr_vertex]:
            alt = distance_map[curr_vertex] + weight

            if alt < distance_map[adj_vertex]:
                distance_map[adj_vertex] = alt
                parent_map[adj_vertex] = curr_vertex

                if adj_vertex in PQ.position_map:
                    PQ.decrease_priority(adj_vertex, alt)
                else:
                    PQ.insert(Node(adj_vertex, alt))

    return distance_map, parent_map


def shortest_path(parent_map, destination):
    curr = destination
    path = []

    while curr is not None:
        path.append(curr)
        curr = parent_map[curr]

    return path[::-1]


def shortest_distance(distance_map, destination):
    return distance_map[destination]


def prims(graph, start):
    mst = []
    in_mst = set()
    PQ = PriorityQueue()
    priority = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}

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


def prims_2(graph):
    mst = []
    PQ = PriorityQueue()
    parent_map = {vertex: None for vertex in graph}

    for vertex in graph:
        PQ.insert(Node(vertex, float('inf')))

    start = next(iter(graph))
    PQ.decrease_priority(start, 0)

    while not PQ.is_empty():
        min_node = PQ.extract_min()
        u = min_node.value

        if parent_map[u] is not None:
            mst.append((parent_map[u], u, min_node.priority))

        for v, weight in graph[u]:
            if v in PQ.position_map:
                if weight < PQ.queue[PQ.position_map[v]].priority:
                    PQ.decrease_priority(v, weight)
                    parent_map[v] = u

    return mst


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 3), ('B', 2)]
}
# Expected MST: [('A', 'B', 1), ('B', 'C', 2)]

graph_1 = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1)],
    'C': [('A', 3)],
    'D': [('E', 2)],
    'E': [('D', 2)]
}
# Expected MST: [('A', 'B', 1), ('A', 'C', 3), ('D', 'E', 2)]

print(prims_2(graph_1))


graph_3 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2)],
    'C': [('A', 4), ('B', 2)],
    'D': [('E', 3)],
    'E': [('D', 3)]
}
# Expected MST: [('A', 'B', 1), ('B', 'C', 2), ('D', 'E', 3)]
# Another MST: [('A', 'B', 1), ('A', 'C', 4), ('D', 'E', 3)]
print(djikstra(graph_3, 'A'))