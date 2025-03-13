class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] = self.freq.get(val, 0) + 1
        curr_freq = self.freq[val]
        prev_freq = curr_freq - 1
        self.group[curr_freq] = self.group.get(curr_freq, [])
        self.group[curr_freq].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])
        
    def pop(self):
        """
        :rtype: int
        """
        # # O(n) pop method
        # i = len(self.stack)-1
        # while i >= 0:
        #     if self.freq[self.stack[i]] == self.max_freq:
        #         most_freq = self.stack.pop(i)
        #         self.freq[most_freq] = self.freq.get(most_freq) - 1
        #         if self.freq[most_freq] == 0:
        #             del self.freq[most_freq]
        #         if self.freq:
        #             self.max_freq = max(self.freq.values())
        #         else:
        #             self.max_freq = 0
        #         return most_freq
        #     i -= 1

        # More optimal O(1) pop method

        if self.group[self.max_freq]:
            most_freq = self.group[self.max_freq].pop()
            if not self.group[self.max_freq]:
                del self.group[self.max_freq]
                self.max_freq -= 1
            
            self.freq[most_freq] = self.freq.get(most_freq) - 1
                
            if self.freq[most_freq] == 0:
                del self.freq[most_freq]
            
            return most_freq

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()