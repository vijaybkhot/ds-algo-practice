class ListNode(object):
    
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet(object):

    def __init__(self):
        self.size = 10**4
        self.set = [ListNode(0) for i in range(self.size)]        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        cur = self.set[key % self.size] 
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        cur = self.set[key % self.size] 
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        cur = self.set[key % self.size] 
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)