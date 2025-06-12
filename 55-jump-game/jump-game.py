class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}

        def dfs(i):
            if i >= len(nums)-1:
                return True
            
            if nums[i] == 0:
                return False

            if i in dp:
                return dp[i]

            can_reach = False

            for j in range(nums[i], 0, -1):
                if dfs(i+j):
                    can_reach = True
                    dp[i] = True
                    return True
                    break

            dp[i] = can_reach
            return can_reach
        
        return dfs(0)