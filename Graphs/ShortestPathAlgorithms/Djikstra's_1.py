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

    def swap(self, index1, index2):
        self.position_map[self.queue[index1].value] = index2
        self.position_map[self.queue[index2].value] = index1
        self.queue[index1], self.queue[index2] = self.queue[index2], self.queue[index1]

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


def djikstra(graph, source):
    distance = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    PQ = PriorityQueue()
    distance[source] = 0
    PQ.insert(Node(source, 0))

    while not PQ.is_empty():
        curr_vertex_node = PQ.extract_min()
        curr_vertex = curr_vertex_node.value

        for adjacent_vertex, weight in graph[curr_vertex]:
            alt = distance[curr_vertex] + weight

            if alt < distance[adjacent_vertex]:
                distance[adjacent_vertex] = alt
                parent[adjacent_vertex] = curr_vertex

                if adjacent_vertex in PQ.position_map:
                    PQ.decrease_priority(adjacent_vertex, alt)
                else:
                    PQ.insert(Node(adjacent_vertex, alt))
    return distance, parent


def shortest_path(parent_map, destination):
    curr_vertex = destination
    path = []

    while curr_vertex is not None:
        path.append(curr_vertex)
        curr_vertex = parent_map[curr_vertex]
    return path[::-1]


def shortest_distance(destination, distance_map):
    return distance_map[destination]


graph = {
    'A': [('B', 3), ('C', 1)],
    'B': [('C', 7), ('D', 5)],
    'C': [('D', 2)],
    'D': []
}
source = 'A'

distance_map, parent = (djikstra(graph, source))
print(distance_map)
print(parent)
print(shortest_path(parent_map=parent, destination='D'))
# Expected Output
# Shortest Distance: {'A': 0, 'B': 3, 'C': 1, 'D': 3}
# Shortest Path to D: ['A', 'C', 'D']


graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 4)],
    'C': [('D', 2)],
    'D': [('E', 3)],
    'E': []
}
source = 'A'

distance_map, parent = djikstra(graph, source)
print("Shortest Distance:", distance_map)
print("Shortest Path to E:", shortest_path(parent, 'E'))

# Shortest Distance: {'A': 0, 'B': 2, 'C': 1, 'D': 3, 'E': 6}
# Shortest Path to E: ['A', 'C', 'D', 'E']

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}
source = 'A'

distance_map, parent = djikstra(graph, source)
print("Shortest Distance:", distance_map)
print("Shortest Path to E:", shortest_path(parent, 'E'))
