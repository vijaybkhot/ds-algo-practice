class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = {}
        def dfs(i, rob_first):
            if (i, rob_first) in dp:
                return dp[(i, rob_first)]
            if (i == len(nums)-1 and rob_first) or i >= len(nums):
                return 0
            
            rob = nums[i] + dfs(i+2, rob_first)
            skip = dfs(i+1, rob_first)
            dp[(i, rob_first)] = max(rob, skip)
            return dp[(i, rob_first)]
        
        rob_straight = max(nums[0]+dfs(2, True), dfs(1, False))
        nums = nums[::-1]
        dp = {}
        rob_reverse = max(nums[0]+dfs(2, True), dfs(1, False))
        return max(rob_straight, rob_reverse)

        # def rob_normal(houses):
        #     if not houses:
        #         return 0
        #     if len(houses) == 1:
        #         return houses[0]
            
        #     dp_0 = (houses[0], 0) #(with, without)
        #     for i in range(1, len(houses)):
        #         dp_curr = ((houses[i]+dp_0[1]), max(dp_0))
        #         dp_0 = dp_curr
            
        #     return max(dp_0)

        # return max(rob_normal(nums[:-1]), rob_normal(nums[1:]))