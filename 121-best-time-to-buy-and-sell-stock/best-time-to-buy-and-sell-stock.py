class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        left = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[left]:
                profit = max(profit , prices[i]-prices[left])
            else:
                left = i

        
        return profit
