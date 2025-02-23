class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        right = 1
        diff_pair = 0
        while left < len(nums) and right < len(nums):
            right = left + 1
            curr_left = nums[left]
            possible_right = curr_left + k
            for i in range(right, len(nums)):
                if nums[i] == possible_right:
                    diff_pair += 1
                    break
            left += 1
            while left < len(nums) and nums[left] == curr_left:
                left += 1
        
        return diff_pair
            


            
        