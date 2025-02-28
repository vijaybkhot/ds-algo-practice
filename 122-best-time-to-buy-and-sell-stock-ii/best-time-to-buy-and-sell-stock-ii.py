class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        if len(prices) == 2:
            if (prices[1] - prices[0]) > 0:
                return prices[1] - prices[0]
            else:
                return 0

        prices.append(-1)

        profit = 0
        curr_profit = 0
        curr_stock = 0

        for i in range(len(prices) - 1):
            if i == len(prices) - 2 and curr_stock > 0 and curr_profit > 0:
                if (prices[i + 1] - prices[i] + curr_profit) > curr_profit:
                    curr_profit += prices[i + 1] - prices[i]
                    profit += curr_profit
                    curr_stock, curr_profit = 0, 0

            if (prices[i + 1] - prices[i] + curr_profit) > curr_profit:
                if curr_stock == 0:
                    curr_stock = prices[i]
                curr_profit += prices[i + 1] - prices[i]
            else:
                if curr_profit > 0:
                    curr_stock = 0
                    profit += curr_profit
                    curr_profit = 0
                else:
                    continue
        return profit


            