class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # # Inefficient recursive approach
        # self.res = float('inf')
        # def dfs(idx, num_coins, curr_sum):
        #     if idx == len(coins) or curr_sum > amount:
        #         return
           
        #     if curr_sum == amount:
        #         self.res = min(self.res, num_coins)
        #         return
        #     for i in range(idx, len(coins)):
        #         dfs(i, num_coins+1, curr_sum+coins[i])
        
        # dfs(0, 0, 0)
        # return self.res if self.res != float('inf') else -1
        dp = {}
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in dp:
                return dp[rem]
            
            dp[rem] = min(1+dfs(rem-coin) for coin in coins)
            return dp[rem]
        
        res = dfs(amount)
        return res if res != float('inf') else -1
            

            

        # # # Greedy apporoach - not correct for all cases
        # # if amount == 0:
        # #     return 0
        # # is_possible = False
        # # coins.sort()
        # # prefix = 0
        # # for coin in coins:
        # #     prefix += coin
        # #     if amount % coin == 0 or amount % prefix == 0:
        # #         is_possible = True
        # #         break
            
        # # if not is_possible:
        # #     return -1 
        
        # # self.count = 0
        # # self.is_possible = True
        # # def dfs(i, curr_amount):
        # #     if i == -1:
        # #         return
        # #     if coins[i] > curr_amount:
        # #         dfs(i-1, curr_amount)
        # #     else:    
        # #         num_coins_i = curr_amount // coins[i]
        # #         remainder =  curr_amount % coins[i]
        # #         self.count += num_coins_i
        # #         dfs(i-1, remainder)
        
        # # dfs(len(coins)-1, amount)
    
        # # return self.count if self.is_possible else -1

        # # # Simple backtracking recursion
        # # def dfs(amount):
        # #     if amount == 0:
        # #         return 0
            
        # #     res = float('inf')
        # #     for coin in coins:
        # #         if amount - coin >= 0:
        # #             res = min(res, 1 + dfs(amount-coin))
        # #     return res
        
        # # minCoins = dfs(amount)

        # # return minCoins if minCoins < float('inf') else -1

        # # # Memoized recursion: top-down DP
        # # memo = {0: 0}
        # # def dfs(amount):
        # #     if amount in memo:
        # #         return memo[amount]
        
            
        # #     res = float('inf')
        # #     for coin in coins:
        # #         if amount - coin >= 0:
        # #             res = min(res, 1 + dfs(amount-coin))
        # #     memo[amount] = res
        # #     return res

        # # res = dfs(amount)
        # # return res if res != float('inf') else -1

        # # Bottom-up DP
        # dp = [float('inf')]*(amount+1)
        # dp[0] = 0
        # for a in range(1, amount+1):
        #     for coin in coins:
        #         if a - coin >=0:
        #             dp[a] = min(dp[a], 1+dp[a-coin])
        
        # return dp[amount] if dp[amount] != float('inf') else -1