class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # # Brute Force solution:
        # res = float('-inf')
        # for i in range(len(nums)):
        #     curr_prefix = 0
        #     for j in range(i, len(nums)):
        #         curr_prefix += nums[j]
        #         res = max(res, curr_prefix)
        
        # return res

        # # Top-down DP
        # dp = {}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]

        #     if i == len(nums)-1:
        #         return nums[i]
        
            
        #     dp[i] = max(nums[i], (nums[i]+dfs(i+1)))
        #     return dp[i]
        
        # return max(dfs(i) for i in range(len(nums)))

        # Bottom-up DP
        n = len(nums)
        dp = [0]*n
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i], nums[i]+dp[i+1])
        
        return max(dp)

            

