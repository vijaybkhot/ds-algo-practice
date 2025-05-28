
# class MyCircularQueue:
#     def __init__(self, k: int):
#         self.queue = [None]*k
#         self.size = k
#         self.count = 0
#         self.front = 0
#         self.rear = 0
        

#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False

#         self.queue[self.rear] = value
#         self.rear = (self.rear + 1) % self.size
#         self.count += 1
#         return True
        

#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
            
#         self.queue[self.front] = None
#         self.front = (self.front + 1) % self.size
#         self.count -= 1
#         return True
        

#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.front]
        

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[(self.rear - 1 + self.size) % self.size]
        

#     def isEmpty(self) -> bool:
#         return self.count == 0
        
#     def isFull(self) -> bool:
#         return self.count == self.size

# Linked list implementation
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.front = None
        self.rear = None
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        if self.isEmpty():
            self.front, self.rear = newNode, newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
        self.count += 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.count -= 1
        if self.isEmpty():
            self.front, self.rear = None, None
        else:
            newFront = self.front.next
            self.front.next = None
            self.front = newFront
        return True

    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val 

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.rear.val 
    
    def isEmpty(self) -> bool:
        return self.count == 0
        
    def isFull(self) -> bool:
        return self.count == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()