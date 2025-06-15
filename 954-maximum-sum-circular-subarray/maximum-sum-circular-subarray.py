class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = max(nums)
        # Case I: Normal non-circular sub-array
        dp = [0]*n
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(nums[i], nums[i]+dp[i+1])

        non_wrap_max = max(dp)

        # Case II: Case for wrapped sub-array. We subtract min-subarray sum from total sum
        dp = [0]*n
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = min(nums[i], nums[i]+dp[i+1])

        wrap_max = sum(nums) - min(dp)
        if non_wrap_max < 0:
            return max_num

        return max(non_wrap_max, wrap_max)
        

        
        