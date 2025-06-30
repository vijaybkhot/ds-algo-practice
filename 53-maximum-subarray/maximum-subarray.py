class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # max_subarray = [float('-inf')]*n
        # max_subarray[n-1] = nums[n-1]
        # for i in range(n-2, -1, -1):
        #     max_subarray[i] = max(nums[i], nums[i]+max_subarray[i+1])
        
        # return max(max_subarray)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i == n-1:
                return nums[i]
            

            dp[i] = max(nums[i], nums[i]+dfs(i+1))
        
            return dp[i]

        return max(dfs(i) for i in range(len(nums)))









        # # # Brute Force solution:
        # # res = float('-inf')
        # # for i in range(len(nums)):
        # #     curr_prefix = 0
        # #     for j in range(i, len(nums)):
        # #         curr_prefix += nums[j]
        # #         res = max(res, curr_prefix)
        
        # # return res

        # # # Top-down DP
        # # dp = {}
        # # def dfs(i):
        # #     if i in dp:
        # #         return dp[i]

        # #     if i == len(nums)-1:
        # #         return nums[i]
        
            
        # #     dp[i] = max(nums[i], (nums[i]+dfs(i+1)))
        # #     return dp[i]
        
        # # return max(dfs(i) for i in range(len(nums)))

        # # # Bottom-up DP
        # # n = len(nums)
        # # dp = [0]*n
        # # dp[n-1] = nums[n-1]
        # # for i in range(n-2, -1, -1):
        # #     dp[i] = max(nums[i], nums[i]+dp[i+1])
        
        # # return max(dp)
        # # Top down two pointer approach - O(n^2) - Not optimal
        # dp = {}
        # n = len(nums)
        # prefix = [0] * (n + 1)
        
        # # Compute prefix sum
        # for i in range(n):
        #     prefix[i + 1] = prefix[i] + nums[i]

        # def get_sum(i, j):
        #     return prefix[j + 1] - prefix[i]

        # dp = {}

        # def dfs(i, j):
        #     if i > j:
        #         return float('-inf')
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     curr_sum = get_sum(i, j)
        #     dp[(i, j)] = max(curr_sum, dfs(i + 1, j), dfs(i, j - 1))
        #     return dp[(i, j)]

        # return dfs(0, n - 1)



                

