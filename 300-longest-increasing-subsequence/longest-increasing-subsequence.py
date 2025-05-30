class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # # Brute force - Backtraking
        # self.LIS = 1
        # def dfs(i, path, curr_min_num):
        #     if i == len(nums):
        #         return path

        #     if nums[i] > curr_min_num:
        #         path += 1
        #         self.LIS = max(dfs(i+1, path, nums[i]), self.LIS)
        #         path -= 1

        #     return dfs(i+1, path, curr_min_num)
        
        # dfs(0, 0, float('-inf'))
        # return self.LIS


        # # Optimized approach - using memoization dictionary
        # n = len(nums)

        # memo = {}
        # def dfs(i, prev_val_index):
        #     if i == n:
        #         return 0
        #     if (i, prev_val_index) in memo:
        #         return memo[(i, prev_val_index)]
            
        #     take = 0
        #     if prev_val_index == -1 or nums[i] > nums[prev_val_index]:
        #         take = 1 + dfs(i + 1, i)
        #     skip = dfs(i + 1, prev_val_index)
        #     memo[(i, prev_val_index)] = max(take, skip)
        #     return memo[(i, prev_val_index)]

        # return dfs(0, -1)

        # # Optimized approach - using memoization array
        # n = len(nums)
        # memo = [-1] * n

        # def dfs(i):
        #     if memo[i] != -1:
        #         return memo[i]

        #     LIS = 1
        #     for j in range(i + 1, n):
        #         if nums[i] < nums[j]:
        #             LIS = max(LIS, 1 + dfs(j))

        #     memo[i] = LIS
        #     return LIS

        # return max(dfs(i) for i in range(n))


        # Bottom up DP
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)