class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, val, priority):
        new_node = Node(val, priority)
        self.queue.append(new_node)
        self.bubble_up()

    def bubble_up(self):
        index = len(self.queue) - 1
        key = self.queue[index]
        while index > 0:
            parent_index = (index - 1) // 2
            parent = self.queue[parent_index]
            if key.priority <= parent.priority:
                break
            else:
                self.queue[parent_index] = key
                self.queue[index] = parent
                index = parent_index

    def dequeue(self):
        if len(self.queue) > 1:
            self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
            root = self.queue.pop()
            i = 0
            j = (2 * i) + 1
            while j < len(self.queue):
                if j < len(self.queue) - 1 and self.queue[j + 1].priority > self.queue[j].priority:
                    j = j + 1
                if self.queue[j].priority > self.queue[i].priority:
                    temp = self.queue[i]
                    self.queue[i] = self.queue[j]
                    self.queue[j] = temp
                    i = j
                    j = (2 * i) + 1
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

    # def extract_max(self):
    #     if not self.values:
    #         return None
    #     elif len(self.values) > 1:
    #         self.values[-1], self.values[0] = self.values[0], self.values[-1]  # Swap the first and last elements
    #         root = self.values.pop()  # Store the original root
    #         parent_index = 0
    #         parent_element = self.values[0]
    #         last_index = len(self.values) - 1
    #
    #         while True:
    #             left_child = right_child = None
    #             left_child_index = (parent_index * 2) + 1
    #             right_child_index = (parent_index * 2) + 2
    #             if left_child_index <= last_index:
    #                 left_child = self.values[left_child_index]
    #             if right_child_index <= last_index:
    #                 right_child = self.values[right_child_index]
    #             if left_child and right_child:
    #                 max_child_index = self.values.index(max(left_child, right_child))
    #                 if self.values[max_child_index] > parent_element:
    #                     self.values[parent_index] = self.values[max_child_index]
    #                     self.values[max_child_index] = parent_element
    #                     parent_index = max_child_index
    #                     parent_element = self.values[parent_index]
    #                 else:
    #                     break
    #             elif left_child and not right_child:
    #                 if left_child > parent_element:
    #                     self.values[parent_index] = left_child
    #                     self.values[left_child_index] = parent_element
    #                     parent_index = left_child_index
    #                     parent_element = self.values[parent_index]
    #                 else:
    #                     break
    #             elif right_child and not left_child:
    #                 if right_child > parent_element:
    #                     self.values[parent_index] = right_child
    #                     self.values[right_child_index] = parent_element
    #                     parent_index = right_child_index
    #                     parent_element = self.values[parent_index]
    #                 else:
    #                     break
    #             else:
    #                 break
    #         return root
    #     else:
    #         return self.values.pop()


class NodeP:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


er = PriorityQueue()
er.enqueue('Common cold', 3)
er.enqueue('Gunshot wound', 4)
er.enqueue('concussion', 5)
er.enqueue('Fever', 6)

for i in er:
    print(i.val)
    print(i.priority)
