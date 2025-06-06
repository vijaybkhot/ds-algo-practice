class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # # Top - down DP
        # dp = {}
        # def dfs(i, curr_sum):
        #     if curr_sum == amount:
        #         return 1
        #     if i >= len(coins) or curr_sum > amount:
        #         return 0
        #     if (i, curr_sum) in dp:
        #         return dp[(i, curr_sum)]
        #     total = 0
        #     total += dfs(i, curr_sum+coins[i])
        #     total += dfs(i+1, curr_sum)

        #     dp[(i, curr_sum)] = total
        #     return total
        
        # return dfs(0, 0)

        # Bottom-up DP
        dp = [0]*(amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
    

        return dp[amount]
        