class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = 0
        dp = {}
        # def dfs(i, prev):
        #     if (i, prev) in dp:
        #         return dp[i, prev]

        #     if i == len(nums):
        #         return 0
            
        #     total = 0
        #     if prev == i-1:
        #         total = dfs(i+1, prev)
        #     else:
        #         total = max(nums[i]+dfs(i+1, i), dfs(i+1, prev))
            
        #     dp[i, prev]= total
        #     return dp[i, prev]
        # return dfs(0, None)

        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(nums):
                return 0
            
            rob = nums[i] + dfs(i+2)
            skip = dfs(i+1)
            dp[i] =  max(rob, skip)
            return dp[i]
        return dfs(0)

        
        # # # Bottom-up Dynamic programming approach
        # # nums_record = [(0, 0)]*(n+1)    # with_curr, without_curr
        # # nums_record[0] = (nums[0], 0)
        # # nums_record[1] = (nums[1], nums_record[0][0])

        # # for i in range(2, n):
        # #     nums_record[i] = ((nums[i]+nums_record[i-1][1]), max(nums_record[i-1]))
        
        # # return max(nums_record[n-1])

        # # # Space optimized DP
        # # max_num_1 = (nums[1], nums[0])
        # # for i in range(2, n):
        # #     curr_max_set = ((nums[i]+ max_num_1[1]), max(max_num_1))
        # #     max_num_1 = curr_max_set
        
        # # return max(max_num_1)

        # # # Recursion:
        # # def dfs(i):
        # #     if i >= n:
        # #         return 0
        # #     return max(nums[i]+dfs(i+2), dfs(i+1))
        # # return dfs(0)

        # # Memoization
        # memo = [-1]*(n+1)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = max(nums[i]+dfs(i+2), dfs(i+1))
        #     return memo[i]
        # return dfs(0)

        