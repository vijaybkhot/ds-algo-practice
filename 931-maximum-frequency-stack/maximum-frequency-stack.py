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
        self.group[curr_freq] = self.group.get(curr_freq, [])
        self.group[curr_freq].append(val)
        self.max_freq = max(self.max_freq, self.freq[val])
        
    def pop(self):
        """
        :rtype: int
        """
        if self.group[self.max_freq]:
            most_freq = self.group[self.max_freq].pop()
            if not self.group[self.max_freq]:
                del self.group[self.max_freq]
                self.max_freq -= 1
            
            self.freq[most_freq] = self.freq.get(most_freq) - 1
                
            if self.freq[most_freq] == 0:
                del self.freq[most_freq]
            
            return most_freq

    