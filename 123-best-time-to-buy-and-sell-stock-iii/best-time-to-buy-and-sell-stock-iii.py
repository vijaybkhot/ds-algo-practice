class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
                if count < 2:
                    profit = max(-prices[i]+dfs(i+1, True, count+1), skip)
            
            dp[(i, hold, count)] = profit
            return profit
        
        return dfs(0, False, 0)

        # Divide and conquer - at any index, calculate max profit in a single transaction for left side and also max profit in a single transaction for right side and then add the two to get max possible profit at that point
        left_profit = [0]*n
        right_profit = [0]*n
        # caclulate left max profit for a single transaction
        l_min = prices[0]
        for i in range(1, n):
            left_profit[i] = max(left_profit[i-1], prices[i]-l_min)
            l_min = min(l_min, prices[i])
        
        # caclulate right max profit for a single transaction
        r_max = prices[-1]
        for i in range(n-2, -1, -1):
            right_profit[i] = max(right_profit[i+1], r_max - prices[i])
            r_max = max(r_max, prices[i])
        
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, left_profit[i-1]+right_profit[i])
        
        return max(max_profit, left_profit[-1]) # ensure one transaction max is considered too