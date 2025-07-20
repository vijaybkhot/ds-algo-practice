class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, hold, count):
            if (i, hold, count) in dp:
                return dp[(i, hold, count)]
            if i == n:
                return 0
            
            profit = 0
            if hold:
                profit = max(prices[i] + dfs(i+1, False, count), dfs(i+1, hold, count))
            else:
                if count < 2:
                    profit = max(-prices[i]+dfs(i+1, True, count+1), dfs(i+1, hold, count))
            
            dp[(i, hold, count)] = profit
            return profit
        
        return dfs(0, False, 0)
            