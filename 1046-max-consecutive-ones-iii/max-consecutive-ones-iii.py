class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        one_count = 0
        left = 0
        max_ones = 0
        for right in range(len(nums)):
            # add right
            if nums[right] == 1:
                one_count += 1
            while (right - left + 1) - one_count > k:
                if nums[left] == 1:
                    one_count -= 1
                left += 1
            max_ones = max(max_ones, (right - left + 1))
        
        return max_ones
