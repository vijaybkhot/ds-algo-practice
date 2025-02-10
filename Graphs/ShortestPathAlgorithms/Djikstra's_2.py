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
            child = self.queue[idx]
            parent_idx = (idx - 1) // 2
            parent = self.queue[parent_idx]
            if parent.priority > child.priority:
                self.swap(idx, parent_idx)
                idx = parent_idx
            else:
                break

    def swap(self, parent_idx, idx):
        self.position_map[self.queue[parent_idx].value] = idx
        self.position_map[self.queue[idx].value] = parent_idx
        self.queue[parent_idx], self.queue[idx] = self.queue[idx], self.queue[parent_idx]

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

        if idx != smallest:
            self.swap(smallest, idx)
            self.bubble_down(smallest)

    def decrease_priority(self, value, new_priority):
        idx = self.position_map[value]
        self.queue[idx].priority = new_priority
        self.bubble_up(idx)

    def is_empty(self):
        return len(self.queue) == 0


def djikstra(graph, start_vertex):
    PQ = PriorityQueue()
    distance = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    distance[start_vertex] = 0
    PQ.insert(Node(start_vertex, 0))

    while not PQ.is_empty():
        current_node = PQ.extract_min()
        current_vertex = current_node.value

        for nxt, weight in graph[current_vertex]:
            alt = distance[current_vertex] + weight
            if alt < distance[nxt]:
                distance[nxt] = alt
                parent[nxt] = current_vertex

                if nxt in PQ.position_map:
                    PQ.decrease_priority(nxt, distance[nxt])
                else:
                    PQ.insert(Node(nxt, distance[nxt]))

    return distance, parent


def shortest_path(parent_map, destination):
    if destination in parent_map:
        curr = destination
        path = []
        while curr is not None:
            path.append(curr)
            curr = parent_map[curr]
        return path[::-1]
    else:
        raise ValueError("The vertex does not exist in the graph.")


def shortest_distance(distance_map, destination):
    if destination in distance_map:
        return distance_map[destination]
    else:
        raise ValueError("The vertex does not exist in the graph.")
