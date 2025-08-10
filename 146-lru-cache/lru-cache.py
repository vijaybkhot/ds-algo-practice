class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
       
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.num_nodes = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = dict()
        
    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove_from_list(node)
            self.insert_at_head(node)
            return node.val
        else:
            return -1
       
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove_from_list(node)
            self.insert_at_head(node)
            return
        else:
            if self.num_nodes == self.size:
                # Evict last Node
                last_node = self.tail.prev
                last_node_key = last_node.key
                # delete from the map
                del self.map[last_node_key]
                # remove from list
                self.remove_from_list(last_node)
                self.num_nodes -= 1
            
            new_node = ListNode(key=key, val=value)
            self.insert_at_head(new_node)
            self.num_nodes += 1
            self.map[key] = new_node

    def insert_at_head(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
    
    def remove_from_list(self, node):
        prev_node, nxt_node = node.prev, node.next
        prev_node.next, nxt_node.prev = nxt_node, prev_node

        
    
  
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)