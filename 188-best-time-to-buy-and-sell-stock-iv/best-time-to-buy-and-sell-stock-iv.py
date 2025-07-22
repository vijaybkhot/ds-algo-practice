class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if 2*k >= n: 
            return sum(max(0, prices[i]-prices[i-1]) for i in range(1, n))

        # # Dynamic programming - memoization approach - top down
        # dp = {}
        # def dfs(i, hold, count):
        #     if (i, hold, count) in dp:
        #         return dp[(i, hold, count)]
        #     if i == n:
        #         return 0
            
        #     profit = 0
        #     skip = dfs(i+1, hold, count)
        #     if hold:
        #         profit = max(prices[i] + dfs(i+1, False, count), skip)
        #     else:
        #         if count < k:
        #             profit = max(-prices[i]+dfs(i+1, True, count+1), skip)
            
        #     dp[(i, hold, count)] = profit
        #     return profit
        
        # return dfs(0, False, 0)
        # DP Bottom up
        n = len(prices)
        if n == 0:
            return 0
        
        if 2 * k >= n:
            return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, n))

        # Initialize DP table
        # dp[day][transactions_left][holding]
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]

        # Base case for day 0
        for t in range(1, k + 1):
            dp[0][t][0] = 0                    # skip
            dp[0][t][1] = -prices[0]           # buy on day 0
        
        # Fill the table
        for day in range(1, n):
            for t in range(1, k + 1):
                # Not holding
                dp[day][t][0] = max(
                    dp[day - 1][t][0],            # skip
                    dp[day - 1][t][1] + prices[day]  # sell
                )
                # Holding
                dp[day][t][1] = max(
                    dp[day - 1][t][1],            # skip
                    dp[day - 1][t - 1][0] - prices[day]  # buy
                )

        # Max profit is not holding any stock on last day
        return max(dp[n - 1][t][0] for t in range(k + 1))

