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
        if value is not None:
            idx = self.position_map[value]
            self.queue[idx].priority = new_priority
            self.bubble_up(idx)
        else:
            return

    def is_empty(self):
        return len(self.queue) == 0


def djikstra(graph, start):
    if not graph:
        return {}, {}
    PQ = PriorityQueue()
    distance = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    distance[start] = 0

    for vertex in graph:
        PQ.insert(Node(vertex, float('inf')))

    PQ.decrease_priority(start, 0)
    distance[start] = 0
    parent[start] = None

    while not PQ.is_empty():
        curr_node = PQ.extract_min()
        curr_vertex = curr_node.value

        distance[curr_vertex] = curr_node.priority

        for neighbour, dist in graph[curr_vertex]:
            if neighbour not in PQ.position_map:
                continue

            new_distance = curr_node.priority + dist
            if new_distance < PQ.queue[PQ.position_map[neighbour]].priority:
                PQ.decrease_priority(neighbour, new_distance)
                parent[neighbour] = curr_vertex

    return distance, parent


def shortest_path(parent_map, destination):
    current = destination
    path = []
    while current is not None:
        path.append(current)
        current = parent_map[current]
    return path[::-1]


def shortest_distance(distance_map, destination):
    return distance_map[destination]


def djikstra_1(graph, start):
    PQ = PriorityQueue()
    parent_map = {vertex: None for vertex in graph}
    distance_map = {vertex: float('inf') for vertex in graph}

    distance_map[start] = 0

    for vertex in graph:
        PQ.insert(Node(vertex, float('inf')))
    PQ.decrease_priority(start, 0)

    while not PQ.is_empty():
        curr_node = PQ.extract_min()
        curr_vertex = curr_node.value

        distance_map[curr_vertex] = curr_node.priority
        for neighbour, dist in graph[curr_vertex]:
            new_distance = curr_node.priority + dist

            if neighbour not in PQ.position_map:
                continue

            if new_distance < PQ.queue[PQ.position_map[neighbour]].priority:
                PQ.decrease_priority(neighbour, new_distance)
                parent_map[neighbour] = curr_vertex
    return distance_map, parent_map


def shortest_path_1(parent_map, destination):
    curr = destination
    path = []
    while curr is not None:
        path.append(curr)
        curr = parent_map[curr]
    return path[::-1]


def shortest_distance_1(distance_map, destination):
    return distance_map[destination]


def djikstra_2(graph, start):
    distance_map = {vertex: float('inf') for vertex in graph}
    parent_map = {vertex: None for vertex in graph}
    PQ = PriorityQueue()
    for vertex in graph:
        PQ.insert(Node(vertex, float('inf')))
    distance_map[start] = 0
    PQ.decrease_priority(start, 0)
    while not PQ.is_empty():
        curr_node = PQ.extract_min()
        curr_vertex = curr_node.value

        distance_map[curr_vertex] = curr_node.priority

        for neighbour, dist in graph[curr_vertex]:
            if neighbour in PQ.position_map:
                new_dist = distance_map[curr_vertex] + dist
                if new_dist < PQ.queue[PQ.position_map[neighbour]].priority:
                    PQ.decrease_priority(neighbour, new_dist)
                    parent_map[neighbour] = curr_vertex
    return parent_map, distance_map


def shortest_path_2(parent_map, destination):
    curr = destination
    path = []
    while curr is not None:
        path.append(curr)
        curr = parent_map[curr]
    return path[::-1]




def test_djikstra(djikstra):
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
    print(distance)
    print(parent)

    graph_2 = {
        'A': [('B', 2), ('C', 5), ('D', 1)],
        'B': [('C', 2), ('E', 3)],
        'C': [('D', 3), ('E', 1)],
        'D': [('F', 4)],
        'E': [('F', 1)],
        'F': []
    }
    start_node = 'A'
    expected_distances_2 = {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 5, 'F': 5}
    expected_parents_2 = {'A': None, 'B': 'A', 'C': 'B', 'D': 'A', 'E': 'C', 'F': 'D'}

    distance, parent = djikstra(graph_2, start_node)
    print(distance, parent)
    print(distance)
    print(parent)

    graph_3 = {
        'A': [('B', 2)],
        'B': [('C', 3)],
        'C': [],
        'D': []
    }
    start_node = 'A'
    expected_distances_3 = {'A': 0, 'B': 2, 'C': 5, 'D': float('inf')}
    expected_parents_3 = {'A': None, 'B': 'A', 'C': 'B', 'D': None}

    distance, parent = djikstra(graph_3, start_node)
    print(distance)
    print(parent)

    # Graph with only one node
    graph_4 = {'A': []}
    start_node = 'A'
    expected_distances_4 = {'A': 0}
    expected_parents_4 = {'A': None}

    distance, parent = djikstra(graph_4, start_node)
    print(distance)
    print(parent)

    # Empty graph
    graph_5 = {}
    start_node = None
    expected_distances_5 = {}
    expected_parents_5 = {}

    distance, parent = djikstra(graph_5, start_node)
    print(distance)
    print(parent)


test_djikstra(djikstra_2)