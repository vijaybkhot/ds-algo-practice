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


        # Optimized approach - using caching
        # n = len(nums)

        # memo = {}
        # def dfs(i, prev_val):
        #     if i == n:
        #         return 0
        #     if (i, prev_val) in memo:
        #         return memo[(i, prev_val)]
            
        #     take = 0
        #     if nums[i] > prev_val:
        #         take = 1 + dfs(i + 1, nums[i])
        #     skip = dfs(i + 1, prev_val)
        #     memo[(i, prev_val)] = max(take, skip)
        #     return memo[(i, prev_val)]

        # return dfs(0, float('-inf'))

        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]  

        def dfs(i, j):
            if i == n:
                return 0
            if memo[i][j + 1] != -1:
                return memo[i][j + 1]

            LIS = dfs(i + 1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            memo[i][j + 1] = LIS
            return LIS

        return dfs(0, -1)