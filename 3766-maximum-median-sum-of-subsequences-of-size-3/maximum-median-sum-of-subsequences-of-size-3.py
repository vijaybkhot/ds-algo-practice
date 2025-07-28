class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        res = 0

        while l < r:
            curr_median = nums[r-1]
            res += curr_median
            r -= 2
            l += 1
        
        return res
            