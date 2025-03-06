class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        
        left = 0
        profit = 0
        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                curr_profit = prices[right] - prices[left]
                if curr_profit > profit:
                    profit = curr_profit
            else:
                left = right
        
        return profit
            
            



