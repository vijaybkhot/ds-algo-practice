class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.min_stack.append(val)
        else:
            self.stack.append(val)
            if self.min_stack and self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
    def pop(self) -> None:
       self.stack.pop()
       self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()