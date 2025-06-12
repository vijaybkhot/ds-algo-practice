class Solution:
    def jump(self, nums: List[int]) -> int:

        # Dynamic Programming appraoch:
        dp = {}
        
        def dfs(i):
            if i >= len(nums)-1:
                return 0
            
            if i in dp:
                return dp[i]
            
            min_jumps = float('inf')
            for j in range(nums[i]):
                min_jumps = min(min_jumps, 1 + dfs(i+j+1))
            
            dp[i] = min_jumps
            return min_jumps
        
        return dfs(0)



        # # Greedy Approach
        # i, last, jumps = len(nums)-2, len(nums)-1, 0
        # while i > -1 and last > -1:
        #     while i >= 0 and i + nums[i] >= last:
        #         i -= 1
        #     last = i
        #     i -= 1
        #     jumps += 1
        
        # return jumps
        

        