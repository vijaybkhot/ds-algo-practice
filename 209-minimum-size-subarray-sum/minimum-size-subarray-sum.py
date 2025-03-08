class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minimal_length = len(nums) + 1
        left = 0
        curr_sum = 0
        for right in range(len(nums)):
            # Include right in widow
            curr_sum += nums[right]

            while (curr_sum - nums[left]) >= target:
                    curr_sum -= nums[left]
                    left += 1
            
            if curr_sum >= target:
                minimal_length = min(minimal_length, (right-left+1))
        
        if minimal_length <= len(nums):
            return minimal_length
        else:
            return 0

        