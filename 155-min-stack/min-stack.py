class MinStack(object):

    def __init__(self):
        self.stack = []
        self. min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.min:
            self.min.append(min(self.min[-1], val))
        else:
            self.min.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.min.pop()
        return self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()