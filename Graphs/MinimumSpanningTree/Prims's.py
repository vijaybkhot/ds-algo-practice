class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.position = {}

    def insert(self, node):
        self.queue.append(node)
        idx = len(self.queue) - 1
        self.position[node.value] = idx
        self.bubble_up(idx)

    def bubble_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.queue[parent_idx].priority > self.queue[idx].priority:
                self._swap(idx, parent_idx)
                idx = parent_idx
            else:
                break

    def _swap(self, i, j):
        self.position[self.queue[i].value] = j
        self.position[self.queue[j].value] = i
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def extract_min(self):
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            node = self.queue.pop()
            del self.position[node.value]
            return node
        self._swap(0, len(self.queue) - 1)
        min_node = self.queue.pop()
        del self.position[min_node.value]
        self._bubble_down(0)
        return min_node

    def _bubble_down(self, idx):
        length = len(self.queue)
        smallest = idx
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        if left_child_idx < length and self.queue[left_child_idx].priority < self.queue[smallest].priority:
            smallest = left_child_idx
        if right_child_idx < length and self.queue[right_child_idx].priority < self.queue[smallest]:
            smallest = right_child_idx
        if smallest != idx:
            self._swap(idx, smallest)
            self._bubble_down(smallest)

    def decrease_priority(self, value, new_priority):
        # Find the node in the heap

        # # Locating the node using iteration
        # for i in range(len(self.queue)):
        #     if self.queue[i].value == value:
        #         if self.queue[i].priority > new_priority:
        #             self.queue[i].priority = new_priority
        #             self.bubble_up(i)
        #         break
        # Locating the node using the position dictionary
        idx = self.position[value]
        if idx is not None:
            if new_priority < self.queue[idx].priority:
                self.queue[idx].priority = new_priority
                self.bubble_up(idx)

    def is_empty(self):
        return len(self.queue) == 0


def prim(graph, start):
    # Graph is represented as an adjacency list
    # graph[u] is a list of tuples (v, weight) representing edges (u, v) with given weights

    # Initialize data structures
    mst = []
    priority_map = {vertex: float('inf') for vertex in graph}
    parent = {vertex: None for vertex in graph}
    min_heap = PriorityQueue()
    in_mst = set()

    priority_map[start] = 0
    min_heap.insert(Node(start, 0))

    while not min_heap.is_empty():
        min_node = min_heap.extract_min()
        u = min_node.value

        if u in in_mst:
            continue

        # Add to mst
        in_mst.add(u)
        if parent[u] is not None:
            mst.append((parent[u], u, min_node.priority))

        for v, weight in graph[u]:
            if v not in in_mst and weight < priority_map[v]:
                priority_map[v] = weight
                parent[v] = u

                if v in min_heap.position:
                    min_heap.decrease_priority(v, priority_map[v])
                else:
                    min_heap.insert(Node(v, priority_map[v]))
        return mst
