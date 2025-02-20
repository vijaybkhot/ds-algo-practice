class ListNode(object):
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None

    

class MyHashMap(object):

    def __init__(self):
        self.size = 1007
        self.map = [ListNode(key=0) for i in range(self.size)]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.size
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
        return
            

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.size
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1


    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.size
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)