class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


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
            if parent.weight > child.weight:
                self.swap(parent_idx, idx)
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
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self.queue) and self.queue[left].weight < self.queue[smallest].weight:
            smallest = left
        if right < len(self.queue) and self.queue[right].weight < self.queue[smallest].weight:
            smallest = right

        if smallest != idx:
            self.swap(smallest, idx)
            self.bubble_down(smallest)

    def decrease_priority(self, value, new_weight):
        # Locate the node from value
        idx = self.position_map[value]
        if idx is not None:
            self.queue[idx].weight = new_weight
            self.bubble_up(idx)

    def is_empty(self):
        return len(self.queue) == 0


def djikstra(graph, start):
    dist = {vertex: float('inf') for vertex in graph}
    dist[start] = 0
    parent = {vertex: None for vertex in graph}
    PQ = PriorityQueue()
    PQ.insert(Node(start, 0))

    while not PQ.is_empty():
        closest_node = PQ.extract_min()
        u = closest_node.value

        for v, weight in graph[u]:
            alt = dist[u] + weight

            if alt < dist[v]:
                dist[v] = alt
                parent[v] = u

                if v in PQ.position_map:
                    PQ.decrease_priority(v, dist[v])
                else:
                    PQ.insert(Node(v, dist[v]))
    return dist, parent


def shortest_path(parent_map, destination):
    path = []
    current_vertex = destination

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = parent_map[current_vertex]

    return path[::-1]



def shortest_path_distance(distance_map, destination):
    return distance_map[destination]


graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('C', 1), ('D', 2)],
    'C': [('D', 4)],
    'D': []
}
start_node = 'A'
expected_distances = {'A': 0, 'B': 5, 'C': 3, 'D': 7}
expected_parents = {'A': None, 'B': 'A', 'C': 'A', 'D': 'B'}

distance, parent = djikstra(graph, start_node)
print(shortest_path(parent, destination='D'))
print(shortest_path_distance(distance, 'D'))
