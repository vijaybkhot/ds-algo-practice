class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # # Solution - I
        # # Top-down approach
        # dp = {}
        # def dfs(i, curr_stock, cooldown):
        #     if i == len(prices):
        #         return 0
        #     if (i, curr_stock, cooldown) in dp:
        #         return dp[(i, curr_stock, cooldown)]
        #     total = 0
        #     if not curr_stock and not cooldown:
        #         buy_stock = dfs(i+1, True, cooldown) - prices[i]
        #         skip_stock = dfs(i+1, curr_stock, cooldown)
        #         total = max(buy_stock, skip_stock)
        #     elif curr_stock:
        #         sell_stock = dfs(i+1, False, True) + prices[i]
        #         skip_stock = dfs(i+1, curr_stock, cooldown)
        #         total = max(sell_stock, skip_stock)
        #     elif cooldown:
        #         total = dfs(i+1, curr_stock, False)
            
        #     dp[(i, curr_stock, cooldown)] = total
        #     return total
        
        # return dfs(0, False, False)

        # # Sloution - II
        # # BFS approach - Correct but not optimal - very inefficient
        # visited = set()
        # res = 0
        # q = deque()
        # take_zero = (-prices[0], 1, True, False)
        # skip_zero = (0, 1, False, False)
        # q.append(take_zero)
        # q.append(skip_zero)
        # visited.add(take_zero)
        # visited.add(skip_zero)
        # while q:
        #     curr_profit, idx, holding, cooldown = q.popleft()
        #     if idx == len(prices):
        #         res = max(res, curr_profit)
        #         continue
        #     elif not holding and not cooldown:
        #         # Buy
        #         if (curr_profit-prices[idx], idx+1, True, False) not in visited:
        #             visited.add((curr_profit-prices[idx], idx+1, True, False))
        #             q.append((curr_profit-prices[idx], idx+1, True, False))
        #         # Skip
        #         if (curr_profit, idx+1, False, False) not in visited:
        #             visited.add((curr_profit, idx+1, False, False))
        #             q.append((curr_profit, idx+1, False, False))
        #         continue
        #     elif holding and not cooldown:
        #         # sell
        #         if (curr_profit+prices[idx], idx+1, False, True) not in visited:
        #             visited.add((curr_profit+prices[idx], idx+1, False, True))
        #             q.append((curr_profit+prices[idx], idx+1, False, True))
        #         # skip
        #         if (curr_profit, idx+1, True, False) not in visited:
        #             visited.add((curr_profit, idx+1, True, False))
        #             q.append((curr_profit, idx+1, True, False))
        #         continue
        #     elif not holding and cooldown:
        #         if (curr_profit, idx+1, False, False) not in visited:
        #             q.append((curr_profit, idx+1, False, False))
        #             visited.add((curr_profit, idx+1, False, False))
        
        # return res

        # # Solution - III
        # # Bottom-up solution:   
        # if not prices:
        #     return 0
        
        # n = len(prices)
        # # Initialize DP states
        # rest = [0] * n         # Max profit on day i in rest state
        # hold = [0] * n         # Max profit on day i holding a stock
        # sold = [0] * n         # Max profit on day i having just sold a stock

        # # Base cases
        # hold[0] = -prices[0]   # If we buy on day 0
        # rest[0] = 0            # If we do nothing on day 0
        # sold[0] = 0            # Cannot sell on day 0

        # for i in range(1, n):
        #     # On day i:
        #     rest[i] = max(rest[i-1], sold[i-1])         # Either keep resting or enter rest after selling
        #     hold[i] = max(hold[i-1], rest[i-1] - prices[i])  # Either keep holding, or buy today
        #     sold[i] = hold[i-1] + prices[i]             # Sell today from previously holding

        # # Final answer must be in rest or sold state (cannot end in hold)
        # return max(rest[-1], sold[-1])

        # Solution - IV
        # Space optimized Bottom-up solution:   
        if not prices:
            return 0
        
        n = len(prices)

        # Base cases
        hold = -prices[0]   # If we buy on day 0
        rest = 0            # If we do nothing on day 0
        sold = 0            # Cannot sell on day 0

        for i in range(1, n):
            new_hold, new_rest, new_sold = 0, 0, 0
            # On day i:
            new_rest = max(rest, sold)         # Either keep resting or enter rest after selling
            new_hold = max(hold, rest - prices[i])  # Either keep holding, or buy today
            new_sold = hold + prices[i]             # Sell today from previously holding

            rest, hold, sold = new_rest, new_hold, new_sold
        # Final answer must be in rest or sold state (cannot end in hold)
        return max(rest, sold)

                




        