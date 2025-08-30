class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        res = 0

        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            curr_max = nums[right]

            while left <= right and curr_max*(right-left+1)-curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            
            res = max(res, right-left+1)
        
        return res