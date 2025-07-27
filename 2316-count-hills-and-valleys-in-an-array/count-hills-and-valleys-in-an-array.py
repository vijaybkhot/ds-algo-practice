class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res = 0
        i = 1
        while i < len(nums)-1:
            left_nei = nums[i-1]
            j = i + 1
            
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            right_nei = nums[j] if j < len(nums) else nums[i]
            if left_nei > nums[i] < right_nei or left_nei < nums[i] > right_nei:
                res += 1
            i = j
        return res

