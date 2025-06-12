class Solution:
    def jump(self, nums: List[int]) -> int:

        # # Dynamic Programming appraoch:
        # dp = {}
        
        # def dfs(i):
        #     if i >= len(nums)-1:
        #         return 0
            
        #     if i in dp:
        #         return dp[i]
            
        #     min_jumps = float('inf')
        #     for j in range(nums[i]):
        #         min_jumps = min(min_jumps, 1 + dfs(i+j+1))
            
        #     dp[i] = min_jumps
        #     return min_jumps
        
        # return dfs(0)



        # Greedy Approach
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest

        return jumps
        

        