class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.stocks = []
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # curr_index = len(self.stack)
        # self.stack.append([price, curr_index])
        # self.backup_stack = []
        # while self.stack and self.stack[-1][0] <= price:
        #     self.backup_stack.append(self.stack.pop())
        # res = len(self.backup_stack)
        # self.stack.extend(self.backup_stack[::-1])
        # self.backup_stack = []
        # return res

        # Monotonically decreasing stack
        curr_span = 1
        while self.stack and self.stack[-1][0] <= price:
            curr_span += self.stack.pop()[1]
        self.stack.append([price, curr_span])
        return curr_span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)