class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.use_count = 1  # For LFU

class DoublyLinkedList:
    def __init__(self):
        self.head = ListNode()  # Dummy head
        self.tail = ListNode()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0  # Number of real nodes
        self.key_map = {}  # key -> node

    def insert_at_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.key_map[node.key] = node
        self.count += 1

    def remove_node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.key_map[node.key]
        self.count -= 1

    def pop_from_tail(self):
        # Remove the least recently used node (before dummy tail)
        if self.count == 0:
            return None
        lru_node = self.tail.prev
        self.remove_node(lru_node)
        return lru_node

    def is_empty(self):
        return self.count == 0


class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.count = 0
        self.key_node_map = {}
        self.frequency_nodes_map = defaultdict(DoublyLinkedList)
        self.min_count = 0
        

    def get(self, key: int) -> int:
        if key not in self.key_node_map or self.size == 0:
            return -1
        node = self.key_node_map[key]
        old_freq = node.use_count
        self.frequency_nodes_map[old_freq].remove_node(node)
        
        if self.frequency_nodes_map[old_freq].is_empty():
            del self.frequency_nodes_map[old_freq]
            if self.min_count == old_freq:
                self.min_count += 1

        # Increment frequency and insert into new freq list
        node.use_count += 1
        self.frequency_nodes_map[node.use_count].insert_at_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.size == 0:
            return
        
        if key in self.key_node_map:
            node = self.key_node_map[key]
            node.value = value
            self.get(key)  # Reuses get() logic to update frequency
            return
        
        # Evict if full
        if self.count == self.size:
            evict_list = self.frequency_nodes_map[self.min_count]
            evicted_node = evict_list.pop_from_tail()
            del self.key_node_map[evicted_node.key]
            self.count -= 1
        
        # Create and insert new node
        new_node = ListNode(key, value)
        self.key_node_map[key] = new_node
        self.frequency_nodes_map[1].insert_at_head(new_node)
        self.min_count = 1
        self.count += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)