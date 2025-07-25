class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        dp = {}
        # def dfs(i, prev):
        #     if i == len(nums):
        #         return 0
        #     if (i, prev) in dp:
        #         return dp[(i, prev)]
        #     total = 0
        #     if nums[i] > prev:
        #         # take or skip
        #         total = max(1+dfs(i+1, nums[i]), dfs(i+1, prev))
        #     else:
        #         total = dfs(i+1, prev)
        #     dp[(i, prev)] = total
        #     return total

        # return dfs(0, float('-inf'))
        # @lru_cache(maxsize=None)
        # def dfs(i, prev_idx):
        #     if i == len(nums):
        #         return 0
        #     # if (i, prev_idx) in dp:
        #     #     return dp[(i, prev_idx)]
        #     take = 0
        #     if prev_idx == -1 or nums[i] > nums[prev_idx]:
        #         # take
        #         take = 1+dfs(i+1, i)
            
        #     skip = dfs(i+1, prev_idx)
        #     return max(take, skip)
        #     # dp[(i, prev_idx)] = max(take, skip)
        #     # return dp[(i, prev_idx)]

        # return dfs(0, -1)


        
        # # # Brute force - Backtraking
        # # self.LIS = 1
        # # def dfs(i, path, curr_min_num):
        # #     if i == len(nums):
        # #         return path

        # #     if nums[i] > curr_min_num:
        # #         path += 1
        # #         self.LIS = max(dfs(i+1, path, nums[i]), self.LIS)
        # #         path -= 1

        # #     return dfs(i+1, path, curr_min_num)
        
        # # dfs(0, 0, float('-inf'))
        # # return self.LIS


        # # # Optimized approach - using memoization dictionary
        # # n = len(nums)

        # # memo = {}
        # # def dfs(i, prev_val_index):
        # #     if i == n:
        # #         return 0
        # #     if (i, prev_val_index) in memo:
        # #         return memo[(i, prev_val_index)]
            
        # #     take = 0
        # #     if prev_val_index == -1 or nums[i] > nums[prev_val_index]:
        # #         take = 1 + dfs(i + 1, i)
        # #     skip = dfs(i + 1, prev_val_index)
        # #     memo[(i, prev_val_index)] = max(take, skip)
        # #     return memo[(i, prev_val_index)]

        # # return dfs(0, -1)

        # # # Optimized approach - using memoization array
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


        # # # # Bottom up DP
        # LIS = [1] * len(nums)

        # for i in range(len(nums) - 1, -1, -1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        # return max(LIS)

    

        # # using DP array
        # n = len(nums)
        # LIS = [1]*n
        # for i in range(n-2, -1, -1):
        #     for j in range(i+1, n):
        #         if nums[j] > nums[i]:
        #             LIS[i] = max(LIS[i], 1+LIS[j])
        
        # return max(LIS)

        # Lazy sorting - Patience sorting

        LIS = []

        for num in nums:
            if not LIS or LIS[-1] < num:
                LIS.append(num)
            else:
                insert_idx = bisect_left(LIS, num)
                LIS[insert_idx] = num
        
        return len(LIS)