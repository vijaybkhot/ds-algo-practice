class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
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
        index = len(self.queue) - 1
        key = self.queue[index]
        while index > 0:
            parent_index = (index - 1) // 2
            if key.priority < self.queue[parent_index].priority:
                self.queue[index] = self.queue[parent_index]
                index = parent_index
            else:
                break
        self.queue[index] = key

    def dequeue(self):
        if len(self.queue) > 1:
            self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
            root = self.queue.pop()
            i = 0
            j = 2 * i + 1
            while j < len(self.queue):
                if j < len(self.queue) - 1 and self.queue[j].priority < self.queue[j + 1].priority:
                    j = j + 1

                if self.queue[i].priority < self.queue[j].priority:
                    self.queue[i], self.queue[j] = self.queue[j], self.queue[i]
                    i = j
                    j = 2 * i + 1
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


er = PriorityQueue()
er.enqueue('Common cold', 3)
er.enqueue('Gunshot wound', 4)
er.enqueue('concussion', 5)
er.enqueue('Fever', 6)

for i in er:
    print(i.val)
    print(i.priority)

er = PriorityQueue()
print(er.is_empty())  # Expected: True

er.enqueue('Common cold', 3)
print(er.is_empty())  # Expected: False

er.dequeue()
print(er.is_empty())  # Expected: True

er = PriorityQueue()
er.enqueue('Common cold', 3)
er.enqueue('Gunshot wound', 4)
er.enqueue('Concussion', 5)
er.enqueue('Fever', 6)

for i in er:
    print(i.val, i.priority)
# Expected output:
# Common cold 3
# Gunshot wound 4
# Concussion 5
# Fever 6
