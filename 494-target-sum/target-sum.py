class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # # Top-down approach
        # dp = {}
        # def dfs(i, curr_total):
        #     if i == len(nums) and curr_total == target:
        #         return 1
        #     if i == len(nums):
        #         return 0
        #     if (i, curr_total) in dp:
        #         return dp[(i, curr_total)]
            
        #     dp[(i, curr_total)] = dfs(i+1, curr_total-nums[i]) + dfs(i+1, curr_total+nums[i])
            
        #     return dp[(i, curr_total)]
        
        # return dfs(0, 0)

        # Bottom-up approach:
        dp = [defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1 # -> (0 elements, 0 sum) -> one possible way. i.e. One way to sum to zero with zero elements

        for i in range(len(nums)):
            for curr_sum, num_ways in dp[i].items():
                dp[i+1][curr_sum + nums[i]] += num_ways
                dp[i+1][curr_sum - nums[i]] += num_ways
        
        return dp[len(nums)][target]

