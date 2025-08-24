class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_left = [0]*len(nums)
        max_right = [0]*(len(nums))

        max_left[0] = nums[0]
        for i in range(1, len(nums)):
            left = max_left[i-1] 
            max_left[i] = (1 + left) if nums[i]==1 else 0

        max_right[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right = max_right[i+1] 
            max_right[i] = (1 + right) if nums[i]==1 else 0

        ans = 0
        for i in range(len(nums)):
            left = max_left[i-1] if i-1 >= 0 else 0
            right = max_right[i+1] if i+1 < len(nums) else 0
            ans = max(ans, left + right)
        
        
        return ans
                