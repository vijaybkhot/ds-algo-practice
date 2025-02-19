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
        cur = self.set[index]
        if cur is None:
            self.set[index] = ListNode(key)
            return
        if cur.key == key:
            return
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key):
        index = key % self.size
        cur = self.set[index]
        if cur is None:
            return
        if cur.key == key:
            self.set[index] = cur.next  
            return
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return

    def contains(self, key):
        index = key % self.size
        cur = self.set[index]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False