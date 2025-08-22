class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount = [0] * len(prices)

        stack = []
        
        for idx, price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                original_price, index = stack.pop()
                discount[index] = price
            stack.append((price, idx))
        
        return [prices[i]-discount[i] for i in range(len(prices))]
                