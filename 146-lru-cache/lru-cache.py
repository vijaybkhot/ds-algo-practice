# class ListNode:
#     def __init__(self, key=0, value=0, next=None, prev=None):
#         self.key = key
#         self.value = value
#         self.next = next
#         self.prev = prev

# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.size = capacity
#         self.count = 0
#         self.map = {}
#         self.front, self.rear = None, None
    
#     def remove_node(self, node):
#         """Helper function to remove a node from the doubly linked list"""
#         if node.prev:
#             node.prev.next = node.next
#         if node.next:
#             node.next.prev = node.prev
#         if node == self.front:  # If it's the front, update self.front
#             self.front = self.front.next
#             if self.front:
#                 self.front.prev = None
#         if node == self.rear:  # If it's the rear, update self.rear
#             self.rear = self.rear.prev
#             if self.rear:
#                 self.rear.next = None


#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.map:
#             return -1
        
#         node = self.map[key]

#         if node != self.rear:
#             self.remove_node(node)
#             self.rear.next = node
#             node.prev = self.rear
#             node.next = None
#             self.rear = node

#         return node.value


#     def put(self, key, value):
#         if key in self.map:
#             node = self.map[key]
#             node.value = value
#             self.get(key)  # Move to the rear
#             return

#         new_node = ListNode(key=key, value=value)

#         if self.count == self.size:
#             # Cache is full: remove the least recently used node (front)
#             del self.map[self.front.key]
#             self.remove_node(self.front)
#             self.count -= 1

#         # Insert the new node at the rear
#         if not self.front:
#             self.front = self.rear = new_node
#         else:
#             self.rear.next = new_node
#             new_node.prev = self.rear
#             self.rear = new_node

#         self.map[key] = new_node
#         self.count += 1
        

# Simplified solution:

class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}  
        self.head = ListNode() 
        self.tail = ListNode()  
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
    

    def _insert_at_end(self, node):
        prev, last = self.tail.prev, self.tail
        prev.next = last.prev = node
        node.prev, node.next = prev, last


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert_at_end(node)

        return node.value


    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_at_end(node)
        else:
            if len(self.cache) == self.capacity:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = ListNode(key=key, value=value)
            self.cache[key] = new_node
            self._insert_at_end(new_node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)