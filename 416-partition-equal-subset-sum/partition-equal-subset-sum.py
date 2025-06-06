class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # # First attempt
        # l_sum, r_sum = 0, 0
        # l_sum = nums[0]
        # for i in range(1, len(nums)):

        #     if nums[i] >= l_sum+r_sum:
        #         l_sum = l_sum + r_sum
        #         r_sum = nums[i]
        #     elif l_sum < r_sum:
        #         l_sum += nums[i]
        #     else:
        #         r_sum += nums[i]
        # return l_sum == r_sum

        # # Second attempt
        # total = sum(nums)
        # if total % 2:
        #     return False
        
        # l_sum, r_sum = 0, 0
        # l_sum = nums[0]

        # for i in range(1, len(nums)):
        #     if l_sum + nums[i] <= total//2:
        #         l_sum += nums[i]
        #     else:
        #         r_sum += nums[i]
        # return l_sum == r_sum
        

        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        # # Top-down memoization approach
        # memo = {}
        # def dfs(i, curr_sum):
        #     if (i, curr_sum) in memo:
        #         return memo[(i, curr_sum)]
        #     if curr_sum == target:
        #         return True
        #     if i == len(nums) or curr_sum > target:
        #         return False

        #     memo[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) or dfs(i + 1, curr_sum)
        #     return memo[(i, curr_sum)]
        
        # return dfs(0, 0)

        # # Bottom up DP using a set to store all the sums
        # dp = set()
        # dp.add(0)

        # for i in range(len(nums)-1, -1, -1):
        #     nextDP = set()
        #     for t in dp:
        #         if (t + nums[i]) == target:
        #             return True
        #         nextDP.add(t+nums[i])
        #         nextDP.add(t)
        #     dp = nextDP
        
        # return False

        # Bottom-up DP using an array
        dp = [False]*(target+1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        
        return dp[target]
        
            
            
