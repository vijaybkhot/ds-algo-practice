class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        i = 0

        while i < len(nums):
            left_nei = nums[i-1] if i-1 >= 0 else float('-inf')
            right_nei = nums[i+1] if i+1 < len(nums) else float('-inf')

            if left_nei < nums[i] > right_nei:
                return i
            
            i += 1
        
        