class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        max_profit = []
        for i in range(len(profits)):
            profit = profits[i]
            investment = capital[i]
            # net_profit = profit - investment      
            heapq.heappush(max_profit, (-profit, investment))
        
        for i in range(k):
            stack = []
            while max_profit and max_profit[0][1] > w:
                stack.append(heapq.heappop(max_profit))

            if max_profit:
                net_profit, investment = heapq.heappop(max_profit)
                w += -net_profit
            else:
                break
                
            while stack:
                heapq.heappush(max_profit, stack.pop())
        return w
            






        