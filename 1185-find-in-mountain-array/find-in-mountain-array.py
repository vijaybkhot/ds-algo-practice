# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Find the pivot
        n = mountainArr.length()
        left, right = 0, mountainArr.length()-1
        max_idx = right
        while left <= right:
            mid = (left+right) // 2
            if mid == 0:
                left = mid+1
                continue
            elif mid == n-1:
                right = mid-1
                # continue
            left_val = mountainArr.get(mid-1)
            mid_val = mountainArr.get(mid)
            right_val = mountainArr.get(mid+1)
            if left_val < mid_val > right_val:
                max_idx = mid
                break
            elif mountainArr.get(mid-1) < mid_val < right_val:
                left = mid + 1
            else:
                right = mid-1
        
        left, right = 0, max_idx
        while left <= right:
            mid = (left+right) // 2
            mid_val = mountainArr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        left, right = max_idx+1, mountainArr.length()-1
        while left <= right:
            mid = (left+right) // 2
            mid_val = mountainArr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        


               



        