class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        curr_closest = float('inf')
        res = float('inf')
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - res):
                    res = current_sum
                
                # If the current sum is exactly equal to the target, return target
                if current_sum == target:
                    return target
                
                # Adjust the pointers based on the current sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
            
        return res
