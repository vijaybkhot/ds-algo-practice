class FreqStack(object):

    def __init__(self):
        self.stack = []
        self.freq = {}
        self.max_freq = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.freq[val] = self.freq.get(val, 0) + 1
        self.max_freq = max(self.max_freq, self.freq[val])
        
    def pop(self):
        """
        :rtype: int
        """
        i = len(self.stack)-1
        while i >= 0:
            if self.freq[self.stack[i]] == self.max_freq:
                most_freq = self.stack.pop(i)
                self.freq[most_freq] = self.freq.get(most_freq) - 1
                if self.freq[most_freq] == 0:
                    del self.freq[most_freq]
                if self.freq:
                    self.max_freq = max(self.freq.values())
                else:
                    self.max_freq = 0
                return most_freq
            i -= 1


        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()