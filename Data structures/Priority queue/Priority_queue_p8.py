class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.map = {}

    def insert(self, node):
        self.queue.append(node)
        idx = len(self.queue) - 1
        self.map[node.value] = idx
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

    def swap(self, idx, parent_idx):
        self.map[self.queue[idx].value] = parent_idx
        self.map[self.queue[parent_idx].value] = idx
        self.queue[idx], self.queue[parent_idx] = self.queue[parent_idx], self.queue[idx]

    def extract_min(self):
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            min_node = self.queue.pop()
            del self.map[min_node.value]
            return min_node

        self.swap(0, len(self.queue)-1)
        min_node = self.queue.pop()
        del self.map[min_node.value]
        self.bubble_down(0)
        return min_node

    def bubble_down(self, idx):
        smallest = idx
        left = (2*idx) + 1
        right = (2*idx) + 2

        if left < len(self.queue) and self.queue[left].priority < self.queue[smallest].priority:
            smallest = left
        if right < len(self.queue) and self.queue[right].priority < self.queue[smallest].priority:
            smallest = right
        if smallest != idx:
            self.swap(smallest, idx)
            self.bubble_down(smallest)

    def decrease_priority(self, value, new_priority):
        idx = self.map.get(value)
        if idx is not None:
            self.queue[idx].priority = new_priority
            self.bubble_up(idx)

    def is_empty(self):
        return len(self.queue) == 0


# Example usage:
pq = PriorityQueue()
pq.insert(Node('a', 5))
pq.insert(Node('b', 2))
pq.insert(Node('c', 8))

print(pq.extract_min().value)  # Output: b
print(pq.extract_min().value)  # Output: a
print(pq.extract_min().value)  # Output: c

pq.insert(Node('a', 5))
pq.insert(Node('b', 2))
pq.decrease_priority('a', 1)
print(pq.extract_min().value)  # Output: a

