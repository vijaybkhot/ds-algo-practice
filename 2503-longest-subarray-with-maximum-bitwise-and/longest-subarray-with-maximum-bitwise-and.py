class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)

        count = 0
        curr_count = 0

        i = 0
        while i < len(nums):
            if nums[i] == max_num:
                curr_count = 0
                while i < len(nums) and nums[i] == max_num:
                    curr_count += 1
                    
                    i += 1
                count = max(count, curr_count)
            i += 1
        
        return count

