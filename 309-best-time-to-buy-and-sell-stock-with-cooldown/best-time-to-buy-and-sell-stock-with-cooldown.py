class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        def dfs(i, curr_stock, cooldown):
            if i == len(prices):
                return 0
        
            if (i, curr_stock, cooldown) in dp:
                return dp[(i, curr_stock, cooldown)]
            
            total = 0
            if not curr_stock and not cooldown:
                buy_stock = dfs(i+1, True, cooldown) - prices[i]
                skip_stock = dfs(i+1, curr_stock, cooldown)
                total = max(buy_stock, skip_stock)
            elif curr_stock:
                sell_stock = dfs(i+1, False, True) + prices[i]
                skip_stock = dfs(i+1, curr_stock, cooldown)
                total = max(sell_stock, skip_stock)
            elif cooldown:
                total = dfs(i+1, curr_stock, False)
            
            dp[(i, curr_stock, cooldown)] = total
            return total
        
        return dfs(0, False, False)

        