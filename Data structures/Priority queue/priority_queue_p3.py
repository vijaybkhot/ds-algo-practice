class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, val, priority):
        new_node = Node(val, priority)
        self.queue.append(new_node)
        self.bubble_up()

    def bubble_up(self):
        new_element_index = len(self.queue) - 1
        while new_element_index > 0:
            new_element_parent_index = (new_element_index - 1) // 2
            element = self.queue[new_element_index]
            parent = self.queue[new_element_parent_index]
            if element.priority > parent.priority:
                self.queue[new_element_parent_index] = element
                self.queue[new_element_index] = parent
                new_element_index = new_element_parent_index
            else:
                break

    def dequeue(self):
        if len(self.queue) > 1:
            self.queue[-1], self.queue[0] = self.queue[0], self.queue[-1]
            root = self.queue.pop()
            index = 0
            child_index = 2 * index + 1
            while child_index < len(self.queue):
                if child_index < len(self.queue) - 1 and self.queue[child_index].priority < self.queue[child_index + 1].priority:
                    child_index = child_index + 1
                parent = self.queue[index]
                child = self.queue[child_index]
                if parent.priority >= child.priority:
                    break
                else:
                    self.queue[index] = child
                    self.queue[child_index] = parent
                    index = child_index
                    child_index = 2 * index + 1
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

# After enqueue, the queue should be ['D', 'B', 'A', 'C'] with priorities [7, 5, 3, 2]
print([node.val for node in pq.queue])  # Expected output: ['D', 'B', 'A', 'C']

# Test iteration
for node in pq:
    print(node.val, node.priority)  # Expected output: D 7, B 5, A 3, C 2
# Test dequeue
print("Dequeuing elements:")
while not pq.is_empty():
    node = pq.dequeue()
    print(f"Dequeued: {node.val} with priority {node.priority}")