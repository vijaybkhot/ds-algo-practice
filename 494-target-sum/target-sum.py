class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Top-down approach
        dp = {}
        def dfs(i, curr_total):
            if i == len(nums) and curr_total == target:
                return 1
            if i == len(nums):
                return 0
            if (i, curr_total) in dp:
                return dp[(i, curr_total)]
            
            dp[(i, curr_total)] = dfs(i+1, curr_total-nums[i]) + dfs(i+1, curr_total+nums[i])
            
            return dp[(i, curr_total)]
        
        
        return dfs(0, 0)