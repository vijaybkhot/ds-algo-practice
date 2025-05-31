class ListNode:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt 
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.count = 0
        self.dict = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if self.count == 0 or key not in self.dict:
            return -1
        node = self.dict[key]
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        head_node = self.head.next
        node.next, node.prev = head_node, self.head
        self.head.next, head_node.prev = node, node
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            existing_node = self.dict[key]
            existing_node.val = value
            prev_node, next_node = existing_node.prev, existing_node.next
            prev_node.next, next_node.prev = next_node, prev_node
            head_node = self.head.next
            self.head.next, head_node.prev = existing_node, existing_node
            existing_node.next, existing_node.prev = head_node, self.head
            return
        # Remove the last node, if the cache is full
        if self.count == self.size:
            node_to_delete = self.tail.prev
            node_to_delete.prev.next = self.tail
            self.tail.prev = node_to_delete.prev
            node_to_delete.next, node_to_delete.prev = None, None
            del self.dict[node_to_delete.key]
            self.count -= 1
        new_node = ListNode(key=key, val=value)
        head_node = self.head.next
        head_node.prev, self.head.next = new_node, new_node
        new_node.next, new_node.prev = head_node, self.head
        self.dict[key] = new_node
        self.count += 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)