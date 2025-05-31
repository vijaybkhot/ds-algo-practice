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
        self.detach_node(node)
        self.insert_at_head(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        # If key already exists in the cache, update the value for the key and move the node to the head 
        if key in self.dict:
            existing_node = self.dict[key]
            existing_node.val = value
            self.detach_node(existing_node)
            self.insert_at_head(existing_node)
            return
        # Remove the last node, if the cache is full
        if self.count == self.size:
            node_to_delete = self.tail.prev
            self.detach_node(node_to_delete)
            del self.dict[node_to_delete.key]
            self.count -= 1
        new_node = ListNode(key=key, val=value)
        self.insert_at_head(new_node)
        self.dict[key] = new_node
        self.count += 1
    
    def insert_at_head(self, node):
        head_node = self.head.next
        self.head.next, head_node.prev = node, node
        node.next, node.prev = head_node, self.head
    def detach_node(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)