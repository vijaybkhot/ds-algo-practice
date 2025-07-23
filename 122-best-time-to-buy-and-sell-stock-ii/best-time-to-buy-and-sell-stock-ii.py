class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, hold):
            if i == n:
                return 0
            if (i, hold) in dp:
                return dp[(i, hold)]
            profit = 0
            skip = dfs(i+1, hold)
            if hold:
                sell = prices[i] + dfs(i+1, not hold)
                profit = max(sell, skip)
            else:
                buy = -prices[i] + dfs(i+1, not hold)
                profit = max(buy, skip)
            
            dp[(i, hold)] = profit
            return profit
        
        return dfs(0, False)
