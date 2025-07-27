class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            left_mid = nums[mid-1] if mid-1 >= 0 else float('-inf')
            right_mid = nums[mid+1] if mid+1 < len(nums) else float('-inf')

            if left_mid < nums[mid] > right_mid:
                return mid
            elif left_mid < nums[mid] < right_mid:
                l = mid+1
            else:
                r = mid-1
        
