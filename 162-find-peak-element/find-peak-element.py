class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # i = 0
        # while i < len(nums):
        #     left_nei = nums[i-1] if i-1 >= 0 else float('-inf')
        #     right_nei = nums[i+1] if i+1 < len(nums) else float('-inf')

        #     if left_nei < nums[i] > right_nei:
        #         return i
            
        #     i += 1
        # l  mid    r
        # [1, 2, 3, 1]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            num = nums[mid]
            left_num = nums[mid-1] if mid > 0 else float('-inf')
            right_num = nums[mid+1] if mid < len(nums)-1 else float('-inf')
            
            # 1 - 2 - 3
            if left_num < num > right_num:
                return mid

            elif left_num < num < right_num:
                left = mid + 1
            else:
                right = mid - 1
        