class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # # Brute force approach
        # max_sum = 0
        # if len(nums) == 1:
        #     max_sum = nums[0]
        # for i in range(0, len(nums)-k+1):
        #     curr_sum = 0
        #     for j in range(i, i+k):
        #         curr_sum += nums[j]
        #     if curr_sum > max_sum:
        #         max_sum = curr_sum
        
        # return float(max_sum) / k

        # Using Sliding window approach
        window_sum = 0
        max_sum = 0
        # Set up initial window
        for i in range(0, k):
            window_sum += nums[i]
        
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            if window_sum > max_sum:
                max_sum = window_sum

        return float(max_sum) / k



        