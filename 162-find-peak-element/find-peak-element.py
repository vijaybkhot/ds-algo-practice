class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            left_mid_num = float('-infinity') if mid == 0 else nums[mid-1]
            right_mid_num = float('-infinity') if mid == len(nums)-1 else nums[mid+1]

            if nums[mid] > left_mid_num and nums[mid] > right_mid_num:
                return mid
            elif right_mid_num > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        
        