class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet(object):

    def __init__(self):
        self.size = 10007
        self.set = [None] * self.size  

    def add(self, key):
        index = key % self.size
        if self.set[index] is None:
            self.set[index] = ListNode(key)
            return
        cur = self.set[index]
        while cur:
            if cur.key == key:
                return  # Key already exists
            if cur.next is None:
                break
            cur = cur.next
        cur.next = ListNode(key)  # Append at end

    def remove(self, key):
        index = key % self.size
        cur = self.set[index]
        if cur is None:
            return
        if cur.key == key:
            self.set[index] = cur.next  # Remove head
            return
        prev = None
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev, cur = cur, cur.next

    def contains(self, key):
        index = key % self.size
        cur = self.set[index]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False