class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)-1
        res = nums[0]
        while left <= right:
            if nums[left] < nums[right]:
                return min(nums[left], res)

            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return res
        
        