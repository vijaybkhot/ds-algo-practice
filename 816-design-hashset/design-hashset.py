class MyHashSet(object):

    def __init__(self):
        self.size = 10**7
        self.data = [False] * (self.size)
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if 0 <= key < self.size:
            if self.data[key] == True:
                return
            else:
                self.data[key]=True
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if 0 <= key < self.size:
            if self.data[key] == False:
                return
            else:
                self.data[key]=False

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if 0 <= key < self.size:
            return self.data[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)