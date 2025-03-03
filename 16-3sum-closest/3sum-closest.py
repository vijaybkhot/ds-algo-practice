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
                if abs(target - (nums[i] + nums[left] + nums[right])) < curr_closest:
                    curr_closest = abs(target - (nums[i] + nums[left] + nums[right]))
                    res = (nums[i] + nums[left] + nums[right])

                if nums[i] + nums[left] + nums[right] == target:
                    return target
                elif right == left + 1:
                    break
                elif nums[i] + nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
            
        return res
