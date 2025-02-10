class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueueP3:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def enqueue(self, val, priority):
        new_node = Node(val, priority)
        self.queue.append(new_node)
        self.bubble_up()

    def bubble_up(self):
        new_node_index = len(self.queue) - 1
        key = self.queue[new_node_index]
        while new_node_index > 0:
            new_node_parent_index = (new_node_index - 1) // 2
            parent = self.queue[new_node_parent_index]
            if key.priority <= parent.priority:
                break

            else:
                self.queue[new_node_parent_index] = key
                self.queue[new_node_index] = parent
                new_node_index = new_node_parent_index

    def dequeue(self):
        if len(self.queue) > 1:
            self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
            root = self.queue.pop()
            new_root_index = 0
            new_root_child_index = (2 * new_root_index) + 1
            while new_root_child_index < len(self.queue):
                if new_root_child_index < len(self.queue) - 1 and self.queue[new_root_child_index].priority < self.queue[new_root_child_index + 1].priority:
                    new_root_child_index = new_root_child_index + 1

                if self.queue[new_root_child_index].priority > self.queue[new_root_index].priority:
                    self.queue[new_root_index], self.queue[new_root_child_index] = self.queue[new_root_child_index], \
                        self.queue[new_root_index]
                    new_root_index = new_root_child_index
                    new_root_child_index = (new_root_index * 2) + 1
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
pq = PriorityQueueP3()
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