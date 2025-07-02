class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        curr_span = 1
        while self.stack and self.stack[-1][0] <= price:
            curr_span += self.stack.pop()[1]
            
        self.stack.append((price, curr_span))
        return curr_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)