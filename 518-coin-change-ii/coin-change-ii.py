class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}
        def dfs(i, curr_sum):
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            if curr_sum == amount:
                return 1
            if i >= len(coins) or curr_sum > amount:
                return 0
            total = 0
            total += dfs(i, curr_sum+coins[i])
            total += dfs(i+1, curr_sum)

            dp[(i, curr_sum)] = total
            return total
        
        return dfs(0, 0)

        