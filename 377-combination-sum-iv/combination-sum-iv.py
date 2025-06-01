class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # # Top-down DP
        # memo = {}
        # def dfs(curr_sum):
        #     if curr_sum == target:
        #         return 1
        #     if curr_sum > target:
        #         return 0
        #     if curr_sum in memo:
        #         return memo[curr_sum]
        #     total = 0
        #     for num in nums:
        #         total += dfs(curr_sum + num)
        #     memo[curr_sum] = total
        #     return total

        # return dfs(0)
        
        # Bottop-up DP
        dp = [0]*(target+1)
        dp[0] = 1
        for total in range(1, target+1):
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total-num]
        
        return dp[target]