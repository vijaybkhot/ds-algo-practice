class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # if not nums:
        #     return 0
        if n == 1:
            return nums[0]

        def rob_normal(houses):
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            dp_0 = (houses[0], 0) #(with, without)
            for i in range(1, len(houses)):
                dp_curr = ((houses[i]+dp_0[1]), max(dp_0))
                dp_0 = dp_curr
            
            return max(dp_0)

        return max(rob_normal(nums[:-1]), rob_normal(nums[1:]))