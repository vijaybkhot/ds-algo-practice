class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack)-1):
            self.stack2.append(self.stack.pop())
        pop_item = self.stack.pop()
        for i in range(len(self.stack2)):
            self.stack.append(self.stack2.pop())
        return pop_item

    def peek(self):
        """
        :rtype: int
        """
        for i in range(len(self.stack)-1):
            self.stack2.append(self.stack.pop())
        peek_item = self.stack[-1]
        for i in range(len(self.stack2)):
            self.stack.append(self.stack2.pop())
        return peek_item
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()