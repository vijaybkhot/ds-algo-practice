class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        used = 0  # bitmask of current window
        res = 0

        for right in range(len(nums)):
            
            while (used & nums[right]) != 0:
                used ^= nums[left]  
                left += 1
            used |= nums[right]  
            res = max(res, right - left + 1)

        return res