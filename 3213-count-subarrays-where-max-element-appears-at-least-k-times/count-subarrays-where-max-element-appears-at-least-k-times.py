class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        max_num = max(nums)
        max_num_freq = 0

        num_subarrays = 0

        for right in range(len(nums)):
            num = nums[right]
            if num == max_num:
                max_num_freq += 1
            
            while max_num_freq >= k:
                num_subarrays += len(nums) - right
                if nums[left] == max_num:
                    max_num_freq -= 1
                left += 1
        
        return num_subarrays
        