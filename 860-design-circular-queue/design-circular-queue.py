class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class MyCircularQueue(object):
    # # Array Implementation
    # def __init__(self, k):
    #     """
    #     :type k: int
    #     """
    #     self.size = k
    #     self.queue = [None] * k  
    #     self.front = self.rear = -1 


    # def enQueue(self, value):
    #     """
    #     :type value: int
    #     :rtype: bool
    #     """
    #     if (self.rear + 1) % self.size == self.front:
    #         return False
    #     if self.front == -1:
    #         self.front = self.rear = 0
    #     else:
    #         self.rear = (self.rear + 1) % self.size
        
    #     self.queue[self.rear] = value
    #     return True

    # def deQueue(self):
    #     """
    #     :rtype: bool
    #     """
    #     if self.front == -1:
    #         return False

    #     if self.front == self.rear:
    #         self.front = self.rear = -1
    #     else:
    #         self.front = (self.front + 1) % self.size
        
    #     return True

    # def Front(self):
    #     """
    #     :rtype: int
    #     """
    #     if self.front == -1:
    #         return -1
    #     return self.queue[self.front]

    # def Rear(self):
    #     """
    #     :rtype: int
    #     """
    #     if self.front == -1:
    #         return -1
    #     return self.queue[self.rear]
        

    # def isEmpty(self):
    #     """
    #     :rtype: bool
    #     """
    #     return self.front == -1
        

    # def isFull(self):
    #     """
    #     :rtype: bool
    #     """
    #     return (self.rear + 1) % self.size == self.front
    
    # Linked List Implementation
    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.front = self.rear = None
        self.count = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.count == self.size:
            return False
        newNode = Node(value)

        if self.count == 0:
            self.front = self.rear = newNode
            self.rear.next = self.front
        else:
            self.rear.next = newNode
            self.rear = self.rear.next
            self.rear.next = self.front
            
        self.count += 1
        return True
    def deQueue(self):
        """
        :rtype: bool
        """
        if self.count == 0:
            return False

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front
        
        self.count -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1

        return self.front.value

    def Rear(self):
        """
        :rtype: int
        """
        if self.count == 0:
            return -1
        
        return self.rear.value
    
    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()