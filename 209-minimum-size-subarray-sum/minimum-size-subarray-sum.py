class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) < target:
            return 0
        left = 0
        min_len = n
        curr_sum = 0
        # l
        # [1,   1,  1,  1,  1,  1,  1,  1]
        # r
        # curr_sum = 1
        for right in range(len(nums)):
            curr_sum += nums[right]
            while left <= right and curr_sum >= target:
                min_len = min(min_len, right-left+1)
                curr_sum -= nums[left]
                left += 1
        
        return min_len