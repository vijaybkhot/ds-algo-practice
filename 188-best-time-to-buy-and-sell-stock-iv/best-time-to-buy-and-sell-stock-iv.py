class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # Dynamic programming - memoization approach
        dp = {}
        def dfs(i, hold, count):
            if (i, hold, count) in dp:
                return dp[(i, hold, count)]
            if i == n:
                return 0
            
            profit = 0
            skip = dfs(i+1, hold, count)
            if hold:
                profit = max(prices[i] + dfs(i+1, False, count), skip)
            else:
                if count < k:
                    profit = max(-prices[i]+dfs(i+1, True, count+1), skip)
            
            dp[(i, hold, count)] = profit
            return profit
        
        return dfs(0, False, 0)