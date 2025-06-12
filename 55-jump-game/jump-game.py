class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # Dynamic Programming approach:
        # dp = {}
        # def dfs(i):
        #     if i >= len(nums)-1:
        #         return True
        #     if nums[i] == 0:
        #         return False
        #     if i in dp:
        #         return dp[i]

        #     can_reach = False
        #     for j in range(nums[i], 0, -1):
        #         if dfs(i+j):
        #             can_reach = True
        #             break

        #     dp[i] = can_reach
        #     return can_reach
        
        # return dfs(0)

        # Greedy Approach:
        i = len(nums)-2
        last = len(nums)-1
        while last > -1 and i > -1:
            while i >= 0 and i + nums[i] < last:
                i -= 1
            if i >= 0:
                last = i
                i -= 1
        return last <= 0
