class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit = 0
        # left = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[left]:
        #         profit = max(profit , prices[i]-prices[left])
        #     else:
        #         left = i

        
        # return profit
        # dp = {}
        # def dfs(i, hold):
        #     if (i, hold) in dp:
        #         return dp[(i, hold)]
        #     if i == len(prices):
        #         return 0
            
        #     if not hold:
        #         dp[(i, hold)] = max((dfs(i+1, True)-prices[i]), dfs(i+1, False))
        #     else:
        #         dp[(i, hold)] = max(prices[i], dfs(i+1, True))
            
        #     return dp[(i, hold)]
        
        # return dfs(0, False)


        min_stock = prices[0]
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price-min_stock)
            min_stock = min(price, min_stock)
        
        return max_profit