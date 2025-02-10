class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.queue.append(node)
        index = len(self.queue) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            parent = self.queue[parent_index]
            if parent.priority < node.priority:
                self.queue[index] = parent
                index = parent_index
            else:
                break
        self.queue[index] = node

    def dequeue(self):
        if len(self.queue) > 1:
            self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
            root = self.queue.pop()
            index = 0
            child_index = (2 * index) + 1
            while child_index < len(self.queue):
                if child_index < len(self.queue) - 1 and self.queue[child_index].priority < self.queue[
                    child_index + 1].priority:
                    child_index += 1
                parent = self.queue[index]
                child = self.queue[child_index]
                if parent.priority < child.priority:
                    self.queue[index] = child
                    self.queue[child_index] = parent
                    index = child_index
                    child_index = (2 * index) + 1
                else:
                    break
            return root
        elif len(self.queue) == 1:
            return self.queue.pop()
        else:
            return None

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.queue):
            result = self.queue[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration



# Test enqueue with bubble_up
pq = PriorityQueue()
pq.enqueue('A', 3)  # Insert 'A' with priority 3
pq.enqueue('B', 5)  # Insert 'B' with priority 5
pq.enqueue('C', 2)  # Insert 'C' with priority 2
pq.enqueue('D', 7)  # Insert 'D' with priority 7
pq.enqueue('E', 9)  # Insert 'E' with priority 9
pq.enqueue('F', 6)  # Insert 'F' with priority 6
pq.enqueue('G', 1)  # Insert 'G' with priority 1

# After enqueue, the queue should be ['D', 'B', 'A', 'C'] with priorities [7, 5, 3, 2]
print([node.value for node in pq.queue])  # Expected output: ['D', 'B', 'A', 'C']

# Test iteration
for node in pq:
    print(node.value, node.priority)  # Expected output: D 7, B 5, A 3, C 2
# Test dequeue
print("Dequeuing elements:")
while not pq.is_empty():
    node = pq.dequeue()
    print(f"Dequeued: {node.value} with priority {node.priority}")

# Create an empty priority queue
pq = PriorityQueue()

# Enqueue elements
pq.enqueue('A', 3)
pq.enqueue('B', 5)
pq.enqueue('C', 2)
pq.enqueue('D', 7)

# Check size
assert pq.size() == 4

# Dequeue elements
assert pq.dequeue().value == 'D'
assert pq.dequeue().value == 'B'
assert pq.dequeue().value == 'A'
assert pq.dequeue().value == 'C'

# Check if queue is empty
assert pq.is_empty()

print("All tests passed!")
