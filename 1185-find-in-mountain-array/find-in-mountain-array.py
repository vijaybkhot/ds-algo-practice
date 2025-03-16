# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountainArr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """

        def findMax():
            left, right = 0, mountainArr.length() - 1
            while left < right:  # Change here
                mid = (left + right) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left 
        
        
        max_index = findMax()
        # Now we have the max index, we can apply binary search twice in the left mountain and the right mountain to find the target

        left, right = 0, max_index
        while left <= right:
            mid = (left+right) // 2
            if mountainArr.get(mid) < target:
                left = mid + 1
            elif mountainArr.get(mid) > target:
                right = mid - 1
            else:
                return mid
        # Binary search in the reverse sorted array
        left, right = max_index + 1, mountainArr.length() - 1
        while left <= right:
            mid = (left+right) // 2
            if mountainArr.get(mid) > target:
                left = mid + 1
            elif mountainArr.get(mid) < target:
                right = mid - 1
            else:
                return mid
        
        return -1
                
        